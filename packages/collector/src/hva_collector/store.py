"""Storage of collected records with schema validation on write."""

import json
from pathlib import Path
from typing import Any

import jsonschema

from hva_schema import HumanSolution, Problem
from hva_schema.export import DEFAULT_OUTPUT_DIR


def _load_schema(name: str) -> Any:
    return json.loads((DEFAULT_OUTPUT_DIR / f"{name}.schema.json").read_text())


class ProblemStore:
    def __init__(self, root: Path) -> None:
        self._root = root
        self._problem_schema = _load_schema("Problem")
        self._solution_schema = _load_schema("HumanSolution")

    def exists(self, problem_id: str) -> bool:
        return (self._root / problem_id / "problem.json").exists()

    def _write(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        return path

    def save_problem(self, problem: Problem) -> Path:
        payload = json.loads(problem.model_dump_json())
        jsonschema.validate(instance=payload, schema=self._problem_schema)
        return self._write(self._root / problem.id / "problem.json", payload)

    def save_solution(self, solution: HumanSolution) -> Path:
        payload = json.loads(solution.model_dump_json())
        jsonschema.validate(instance=payload, schema=self._solution_schema)
        path = self._root / solution.problem_id / "human-solutions" / f"{solution.id}.json"
        return self._write(path, payload)
