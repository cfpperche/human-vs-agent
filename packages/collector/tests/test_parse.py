from pathlib import Path

import pytest

from hva_collector.parse import parse_problem_page, parse_submission_source

FIXTURES = Path(__file__).parent / "fixtures"


def test_parses_statement_and_samples() -> None:
    parsed = parse_problem_page((FIXTURES / "problem_page.html").read_text())
    assert "Read two integers from the input." in parsed.text
    assert parsed.samples == [("1 2\n", "3\n"), ("40 2\n", "42\n")]


def test_parses_submission_source() -> None:
    source = parse_submission_source((FIXTURES / "submission_page.html").read_text())
    assert source == "a, b = map(int, input().split())\nprint(a + b)\n"


def test_raises_when_blocks_are_missing() -> None:
    with pytest.raises(ValueError, match="statement"):
        parse_problem_page("<html><body>nothing here</body></html>")
    with pytest.raises(ValueError, match="source"):
        parse_submission_source("<html><body>nothing here</body></html>")
