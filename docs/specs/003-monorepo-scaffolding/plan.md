# Plan: monorepo scaffolding

## Approach

### Python workspace

- Root `pyproject.toml` defines the uv workspace with `packages/*` as members.
- Each package has its own `pyproject.toml`, a `src/` layout, and a `tests/` directory.
- Shared configuration lives at the root: ruff, pyright, and pytest settings.

### Schema package

- `packages/schema` defines the first Pydantic models: `Problem`, `TestCase`, `HumanSolution`, `AgentSolution`, `Metrics`, `MatchRecord`.
- The field set follows the canonical data schema in the design description.
- A script `packages/schema/scripts/export_json_schema.py` writes JSON Schema files to `packages/schema/jsonschema/`.
- A contract test loads a fixture record from `data/fixtures/` and validates it against the exported JSON Schema.

### Web app skeleton

- `apps/web` is a pnpm package with TypeScript strict, eslint, and vitest.
- The package contains one module that loads a generated type from the JSON Schema, and one passing test.
- No framework and no UI. The package only proves the toolchain and the schema bridge.

### CI

- One workflow file: `.github/workflows/ci.yml`.
- Python job: `uv sync`, `ruff check`, `ruff format --check`, `pyright`, `pytest`.
- Node job: `pnpm install`, `eslint`, `tsc --noEmit`, `vitest run`.
- Both jobs run on pull requests and on pushes to `main`.
- Branch protection on `main` requires both jobs.

## Order of work

1. Python workspace and empty packages with one placeholder test each.
2. Schema models, JSON Schema export, fixture, and contract test.
3. Web app skeleton with the generated type and one test.
4. CI workflow and branch protection.
