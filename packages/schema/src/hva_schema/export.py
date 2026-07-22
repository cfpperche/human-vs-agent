"""Export the models as JSON Schema files.

The exported files are the cross-language contract. The TypeScript
app generates its types from them.
"""

import json
from pathlib import Path

from pydantic import BaseModel

from hva_schema import models

EXPORTED_MODELS: list[type[BaseModel]] = [
    models.TestCase,
    models.Problem,
    models.HumanSolution,
    models.AgentSolution,
    models.Metrics,
    models.MatchRecord,
]

DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[2] / "jsonschema"


def export_all(output_dir: Path = DEFAULT_OUTPUT_DIR) -> list[Path]:
    output_dir.mkdir(exist_ok=True)
    written: list[Path] = []
    for model in EXPORTED_MODELS:
        schema = model.model_json_schema()
        path = output_dir / f"{model.__name__}.schema.json"
        path.write_text(json.dumps(schema, indent=2, sort_keys=True) + "\n")
        written.append(path)
    return written
