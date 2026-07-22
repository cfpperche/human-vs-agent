import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx

from hva_collector.anonymize import Anonymizer
from hva_collector.api import CodeforcesApi
from hva_collector.collect import CollectionConfig, collect
from hva_collector.pages import ChallengeError
from hva_collector.store import ProblemStore

FIXTURES = Path(__file__).parent / "fixtures"


def _fixture(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text())


class FakeFetcher:
    def __init__(self, challenge_submissions: bool = False) -> None:
        self.urls: list[str] = []
        self._challenge_submissions = challenge_submissions

    def fetch(self, url: str) -> str:
        self.urls.append(url)
        if "/problem/" in url:
            return (FIXTURES / "problem_page.html").read_text()
        if self._challenge_submissions:
            raise ChallengeError(f"browser challenge returned for {url}")
        return (FIXTURES / "submission_page.html").read_text()


def _api() -> CodeforcesApi:
    files = {
        "contest.list": "contest_list.json",
        "problemset.problems": "problemset_problems.json",
        "contest.status": "contest_status.json",
        "user.info": "user_info.json",
    }

    def handler(request: httpx.Request) -> httpx.Response:
        method = request.url.path.rsplit("/", 1)[-1]
        return httpx.Response(200, json={"status": "OK", "result": _fixture(files[method])})

    client = httpx.Client(transport=httpx.MockTransport(handler))
    return CodeforcesApi(client=client, sleep=lambda s: None, clock=lambda: 0.0)


def _config() -> CollectionConfig:
    return CollectionConfig(
        since=datetime(2026, 6, 1, tzinfo=UTC),
        min_rating=800,
        max_rating=2400,
        limit=5,
        solutions_per_problem=2,
    )


def test_collects_eligible_problems_end_to_end(tmp_path: Path) -> None:
    store = ProblemStore(tmp_path / "collected")
    anonymizer = Anonymizer(tmp_path / "private")
    result = collect(_api(), FakeFetcher(), store, anonymizer, _config())

    # Contest 1500 is too old, contest 2101 still runs, and problem B
    # sits above the rating range. Only cf-2100-a stays.
    assert result.problem_ids == ["cf-2100-a"]
    assert result.skipped_challenge == 0

    problem = json.loads((tmp_path / "collected/cf-2100-a/problem.json").read_text())
    assert problem["difficulty_rating"] == 800
    assert problem["published_at"].startswith("2026-06")
    assert len(problem["tests"]) == 2

    solutions_dir = tmp_path / "collected/cf-2100-a/human-solutions"
    solution_files = sorted(solutions_dir.glob("*.json"))
    assert len(solution_files) == 2
    for path in solution_files:
        text = path.read_text()
        assert "alice" not in text
        assert "bob" not in text
        assert json.loads(text)["author_id"].startswith("author-")


def test_second_run_skips_collected_problems(tmp_path: Path) -> None:
    store = ProblemStore(tmp_path / "collected")
    anonymizer = Anonymizer(tmp_path / "private")
    first = collect(_api(), FakeFetcher(), store, anonymizer, _config())
    assert first.problem_ids == ["cf-2100-a"]
    second = collect(_api(), FakeFetcher(), store, anonymizer, _config())
    assert second.problem_ids == []


def test_challenge_blocks_source_but_keeps_the_problem(tmp_path: Path) -> None:
    store = ProblemStore(tmp_path / "collected")
    anonymizer = Anonymizer(tmp_path / "private")
    result = collect(_api(), FakeFetcher(challenge_submissions=True), store, anonymizer, _config())

    assert result.problem_ids == ["cf-2100-a"]
    assert result.skipped_challenge == 2

    solutions_dir = tmp_path / "collected/cf-2100-a/human-solutions"
    assert list(solutions_dir.glob("*.json")) == []
