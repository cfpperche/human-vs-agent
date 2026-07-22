# Spec 002: technology stack

- Status: done
- Date: 2026-07-22
- Note: this spec is retroactive. The work was complete before the spec process started.

## Goal

Decide and document the foundation: languages, tools, monorepo layout, data storage, test strategy, and CI.

## Requirements

1. The monorepo must be hybrid: Python for the pipeline packages, TypeScript for `apps/`.
2. `packages/schema` must be the only cross-language contract, through exported JSON Schema.
3. Data storage must split: metadata and fixtures in git, full dataset on Hugging Face Datasets.
4. The test strategy must have golden tests, schema contract tests, and unit tests with recorded fixtures.
5. The metrics engine must have a version number, recorded in each result.
6. CI must gate merges to `main` with a Python job and a Node job.

## Acceptance criteria

- `docs/technology-stack.md` records all decisions. ✔
- The design description and `AGENTS.md` show the monorepo structure. ✔
