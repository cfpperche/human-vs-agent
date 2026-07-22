"""Contract tests.

The exported JSON Schema files are the cross-language contract. These
tests check that the export is current and that the fixture record
validates against it.
"""

import json
from pathlib import Path

import jsonschema

from hva_schema.export import EXPORTED_MODELS

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "jsonschema"
FIXTURE = Path(__file__).resolve().parents[3] / "data" / "fixtures" / "match_record.json"


def test_exported_files_are_current() -> None:
    for model in EXPORTED_MODELS:
        path = SCHEMA_DIR / f"{model.__name__}.schema.json"
        assert path.exists(), f"missing export: {path.name} (run export_json_schema.py)"
        on_disk = json.loads(path.read_text())
        current = json.loads(json.dumps(model.model_json_schema(), sort_keys=True))
        assert on_disk == current, f"stale export: {path.name} (run export_json_schema.py)"


def test_fixture_validates_against_exported_schema() -> None:
    schema = json.loads((SCHEMA_DIR / "MatchRecord.schema.json").read_text())
    record = json.loads(FIXTURE.read_text())
    jsonschema.validate(instance=record, schema=schema)
