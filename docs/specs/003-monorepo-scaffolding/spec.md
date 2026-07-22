# Spec 003: monorepo scaffolding

- Status: draft
- Date: 2026-07-22

## Goal

Build the monorepo skeleton with the toolchains, the schema package, and the CI gates. After this spec, the first feature (the collector) starts on a foundation with working anti-regression gates.

## Requirements

1. The uv workspace must contain the five pipeline packages: `schema`, `collector`, `runner`, `metrics`, `analysis`.
2. `packages/schema` must contain the first version of the canonical record models in Pydantic.
3. A build step must export the schema as JSON Schema files.
4. `apps/web` must contain a minimal TypeScript package in strict mode, with eslint and vitest configured.
5. The CI workflow must run both gates on each pull request: Python (ruff, pyright, pytest) and Node (eslint, tsc, vitest).
6. Each package must contain at least one passing test, so the gates prove themselves.
7. A schema contract test must validate a fixture record against the exported JSON Schema.

## Acceptance criteria

- `uv sync` and `uv run pytest` pass at the workspace root.
- `pnpm install` and `pnpm test` pass in `apps/web`.
- The CI workflow passes on a pull request and blocks a merge on failure.
- The exported JSON Schema files exist and match the Pydantic models.

## Out of scope

- Collector, runner, and metrics logic. Those are later specs.
- Web framework selection and any web UI.
- Hugging Face dataset publication.
