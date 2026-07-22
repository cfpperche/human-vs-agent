"""Canonical data models for the human-vs-agent study.

These models are the single cross-language contract. The build exports
them as JSON Schema files, and the TypeScript app generates its types
from those files. See docs/software-design-description.md.
"""

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class ProblemSource(StrEnum):
    CODEFORCES = "codeforces"
    SWE_BENCH = "swe-bench"


class HarnessMode(StrEnum):
    ONE_SHOT = "one-shot"
    AGENTIC = "agentic"


class TestCase(BaseModel):
    input: str
    expected_output: str
    hidden: bool = False


class Problem(BaseModel):
    id: str
    source: ProblemSource
    title: str
    statement: str
    url: str
    difficulty_rating: int | None = None
    published_at: datetime
    collected_at: datetime
    tests: list[TestCase] = Field(default_factory=list[TestCase])


class HumanSolution(BaseModel):
    id: str
    problem_id: str
    # Pseudonymous identifier. The platform handle never enters the
    # published data (see docs/data-licensing-review.md).
    author_id: str
    author_rating_band: str | None = None
    language: str
    source_code: str
    runtime_ms: int | None = None
    memory_kb: int | None = None
    submitted_at: datetime | None = None


class AgentSolution(BaseModel):
    id: str
    problem_id: str
    model_version: str
    harness_mode: HarnessMode
    language: str
    source_code: str
    prompt: str
    temperature: float
    attempts: int
    input_tokens: int
    output_tokens: int
    cost_usd: float
    wall_clock_seconds: float


class Metrics(BaseModel):
    solution_id: str
    # Results from different engine versions are not comparable.
    engine_version: str
    tests_passed: int
    tests_total: int
    runtime_ms: int | None = None
    memory_kb: int | None = None
    lines_of_code: int
    cyclomatic_complexity: float | None = None
    lint_errors: int | None = None


class MatchRecord(BaseModel):
    id: str
    problem: Problem
    human_solution: HumanSolution
    agent_solution: AgentSolution
    metrics: list[Metrics] = Field(default_factory=list[Metrics])
    created_at: datetime
