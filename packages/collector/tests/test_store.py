import json
from pathlib import Path

import jsonschema
import pytest

from hva_collector.store import ProblemStore
from hva_schema import HumanSolution, Problem

MATCH_FIXTURE = Path(__file__).resolve().parents[3] / "data" / "fixtures" / "match_record.json"


def _fixture_problem() -> Problem:
    return Problem.model_validate(json.loads(MATCH_FIXTURE.read_text())["problem"])


def _fixture_solution() -> HumanSolution:
    return HumanSolution.model_validate(json.loads(MATCH_FIXTURE.read_text())["human_solution"])


def test_saves_valid_records(tmp_path: Path) -> None:
    store = ProblemStore(tmp_path)
    problem = _fixture_problem()
    solution = _fixture_solution()
    assert not store.exists(problem.id)
    store.save_problem(problem)
    store.save_solution(solution)
    assert store.exists(problem.id)
    on_disk = json.loads((tmp_path / problem.id / "problem.json").read_text())
    assert on_disk["title"] == problem.title
    solution_path = tmp_path / problem.id / "human-solutions" / f"{solution.id}.json"
    assert solution_path.exists()


def test_rejects_a_record_that_breaks_the_contract(tmp_path: Path) -> None:
    store = ProblemStore(tmp_path)
    broken = Problem.model_construct(id="cf-broken")
    with pytest.raises(jsonschema.ValidationError):
        store.save_problem(broken)
