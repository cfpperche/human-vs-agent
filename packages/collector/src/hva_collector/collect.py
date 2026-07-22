"""Collection orchestration for the Codeforces source."""

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol

from hva_collector.anonymize import Anonymizer, rating_band
from hva_collector.api import ApiProblem, ApiSubmission, CodeforcesApi
from hva_collector.pages import ChallengeError, problem_url, submission_url
from hva_collector.parse import parse_problem_page, parse_submission_source
from hva_collector.store import ProblemStore
from hva_schema import HumanSolution, Problem, ProblemSource, TestCase


class Fetches(Protocol):
    def fetch(self, url: str) -> str: ...


@dataclass
class CollectionConfig:
    since: datetime
    min_rating: int
    max_rating: int
    limit: int
    solutions_per_problem: int


@dataclass
class CollectionResult:
    problem_ids: list[str]
    # Submissions behind the Codeforces browser challenge. The API gives
    # metadata (runtime, memory, rating) but not source code for these.
    # See docs/data-licensing-review.md.
    skipped_challenge: int = 0


def _pick_submissions(
    api: CodeforcesApi, contest_id: int, index: str, count: int
) -> tuple[list[ApiSubmission], dict[str, int | None]]:
    accepted = [
        s
        for s in api.contest_status(contest_id)
        if s.verdict == "OK" and s.problem.index == index and len(s.author.members) == 1
    ]
    by_author: dict[str, ApiSubmission] = {}
    for submission in accepted:
        by_author.setdefault(submission.author.members[0].handle, submission)
    if not by_author:
        return [], {}
    handles = list(by_author)[:100]
    ratings: dict[str, int | None] = {u.handle: u.rating for u in api.user_info(handles)}
    ranked = sorted(
        (by_author[h] for h in handles),
        key=lambda s: ratings.get(s.author.members[0].handle) or 0,
    )
    # An even spread over the rating-sorted list covers the rating bands.
    step = max(1, len(ranked) // count)
    return ranked[::step][:count], ratings


def _eligible_problems(
    api: CodeforcesApi, config: CollectionConfig
) -> list[tuple[ApiProblem, int, datetime]]:
    contests = {
        c.id: c
        for c in api.contest_list()
        if c.phase == "FINISHED"
        and c.startTimeSeconds is not None
        and datetime.fromtimestamp(c.startTimeSeconds, tz=UTC) > config.since
    }
    eligible: list[tuple[ApiProblem, int, datetime]] = []
    for problem in api.problemset_problems():
        cid = problem.contestId
        if cid is None or cid not in contests:
            continue
        if problem.rating is None or not config.min_rating <= problem.rating <= config.max_rating:
            continue
        start = contests[cid].startTimeSeconds
        assert start is not None
        eligible.append((problem, cid, datetime.fromtimestamp(start, tz=UTC)))
    return eligible


def collect(
    api: CodeforcesApi,
    fetcher: Fetches,
    store: ProblemStore,
    anonymizer: Anonymizer,
    config: CollectionConfig,
    now: datetime | None = None,
) -> CollectionResult:
    collected: list[str] = []
    skipped_challenge = 0
    for api_problem, contest_id, published_at in _eligible_problems(api, config):
        if len(collected) >= config.limit:
            break
        problem_id = f"cf-{contest_id}-{api_problem.index.lower()}"
        if store.exists(problem_id):
            continue

        url = problem_url(contest_id, api_problem.index)
        parsed = parse_problem_page(fetcher.fetch(url))
        problem = Problem(
            id=problem_id,
            source=ProblemSource.CODEFORCES,
            title=api_problem.name,
            statement=parsed.text,
            url=url,
            difficulty_rating=api_problem.rating,
            published_at=published_at,
            collected_at=now or datetime.now(UTC),
            tests=[TestCase(input=i, expected_output=o, hidden=False) for i, o in parsed.samples],
        )

        submissions, ratings = _pick_submissions(
            api, contest_id, api_problem.index, config.solutions_per_problem
        )
        solutions: list[HumanSolution] = []
        for submission in submissions:
            handle = submission.author.members[0].handle
            try:
                source = parse_submission_source(
                    fetcher.fetch(submission_url(contest_id, submission.id))
                )
            except ChallengeError:
                skipped_challenge += 1
                continue
            solutions.append(
                HumanSolution(
                    id=f"human-{submission.id}",
                    problem_id=problem_id,
                    author_id=anonymizer.author_id(handle),
                    author_rating_band=rating_band(ratings.get(handle)),
                    language=submission.programmingLanguage,
                    source_code=source,
                    runtime_ms=submission.timeConsumedMillis,
                    memory_kb=submission.memoryConsumedBytes // 1024,
                    submitted_at=datetime.fromtimestamp(submission.creationTimeSeconds, tz=UTC),
                )
            )

        store.save_problem(problem)
        for solution in solutions:
            store.save_solution(solution)
        collected.append(problem_id)
    return CollectionResult(problem_ids=collected, skipped_challenge=skipped_challenge)
