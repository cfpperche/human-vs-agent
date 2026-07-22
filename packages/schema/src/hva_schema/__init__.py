"""Canonical data schema for the human-vs-agent study."""

from hva_schema.models import (
    AgentSolution,
    HarnessMode,
    HumanSolution,
    MatchRecord,
    Metrics,
    Problem,
    ProblemSource,
    TestCase,
)

__version__ = "0.1.0"

__all__ = [
    "AgentSolution",
    "HarnessMode",
    "HumanSolution",
    "MatchRecord",
    "Metrics",
    "Problem",
    "ProblemSource",
    "TestCase",
]
