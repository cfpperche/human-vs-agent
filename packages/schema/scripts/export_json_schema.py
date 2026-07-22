"""Export the Pydantic models as JSON Schema files.

Run from the repository root:

    uv run python packages/schema/scripts/export_json_schema.py
"""

from hva_schema.export import export_all

if __name__ == "__main__":
    for path in export_all():
        print(f"wrote {path}")
