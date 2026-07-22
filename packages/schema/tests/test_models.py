import json
from pathlib import Path

from hva_schema import MatchRecord

FIXTURE = Path(__file__).resolve().parents[3] / "data" / "fixtures" / "match_record.json"


def test_fixture_parses_as_match_record() -> None:
    record = MatchRecord.model_validate_json(FIXTURE.read_text())
    assert record.id == "match-0001"
    assert record.problem.source == "codeforces"
    assert len(record.metrics) == 2


def test_round_trip_is_stable() -> None:
    record = MatchRecord.model_validate_json(FIXTURE.read_text())
    dumped = record.model_dump_json()
    again = MatchRecord.model_validate_json(dumped)
    assert again == record


def test_fixture_has_no_author_handle() -> None:
    raw = json.loads(FIXTURE.read_text())
    assert "author_handle" not in json.dumps(raw)
    assert raw["human_solution"]["author_id"].startswith("author-")
