"""Command line for the collector.

Example:

    uv run hva-collect --since 2026-06-20 --ratings 800-2400 --limit 3

Take the --since value from the freshness threshold in
docs/model-registry.md.
"""

import argparse
from datetime import UTC, datetime
from pathlib import Path

from hva_collector.anonymize import Anonymizer
from hva_collector.api import CodeforcesApi
from hva_collector.collect import CollectionConfig, collect
from hva_collector.pages import PageFetcher
from hva_collector.store import ProblemStore


def _parse_since(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="hva-collect",
        description="Collect recent Codeforces problems and accepted human submissions.",
    )
    parser.add_argument(
        "--since",
        required=True,
        help="Freshness threshold (ISO date). Take it from docs/model-registry.md.",
    )
    parser.add_argument("--ratings", default="800-2400", help="Rating range, e.g. 800-2400.")
    parser.add_argument("--limit", type=int, default=5, help="Maximum problems to collect.")
    parser.add_argument("--solutions-per-problem", type=int, default=3)
    parser.add_argument("--out", type=Path, default=Path("data/collected"))
    parser.add_argument("--private", type=Path, default=Path("data/private"))
    args = parser.parse_args(argv)

    low, _, high = str(args.ratings).partition("-")
    config = CollectionConfig(
        since=_parse_since(str(args.since)),
        min_rating=int(low),
        max_rating=int(high),
        limit=int(args.limit),
        solutions_per_problem=int(args.solutions_per_problem),
    )
    out_dir: Path = args.out
    result = collect(
        api=CodeforcesApi(),
        fetcher=PageFetcher(cache_dir=out_dir / ".cache"),
        store=ProblemStore(out_dir),
        anonymizer=Anonymizer(args.private),
        config=config,
    )
    for problem_id in result.problem_ids:
        print(problem_id)
    print(f"collected {len(result.problem_ids)} problems")
    if result.skipped_challenge:
        print(
            f"skipped {result.skipped_challenge} submissions "
            "(Codeforces browser challenge blocked the source page)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
