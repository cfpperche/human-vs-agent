# Technology stack

## Purpose

This document records the foundation decisions: languages, tools, monorepo layout, data storage, test strategy, and CI. Change this document when a foundation decision changes.

## Languages

The project is a hybrid monorepo with two languages:

- **Python** for the pipeline packages: collector, runner, metrics, analysis.
- **TypeScript** for the web application in `apps/`.

Reasons: the SWE-bench tools, the data-analysis ecosystem, and the LLM SDKs are Python-first. The web platform ecosystem is TypeScript-first.

## Python toolchain

- Python 3.12 or later.
- **uv** manages dependencies, the workspace, and the lockfile.
- **Pydantic** defines the canonical data schema.
- **ruff** does lint and format checks.
- **pyright** does type checks.
- **pytest** runs the tests.

## TypeScript toolchain

- TypeScript in strict mode.
- **pnpm** manages dependencies.
- **eslint** does lint checks.
- **vitest** runs the tests.
- The web framework decision stays open until phase 2 starts.

## Schema contract

The package `packages/schema` is the only shared contract between the two languages.

- Pydantic models define the schema.
- The build exports the schema as JSON Schema files.
- Python packages import the Pydantic models.
- The TypeScript app generates its types from the JSON Schema files.
- Dependency rule: all packages can depend on `schema`. The `schema` package must not depend on other packages.

## Monorepo layout

```
docs/                SDLC documents (STE)
packages/
  schema/            canonical data schema, JSON Schema export
  collector/         Codeforces and SWE-bench collection
  runner/            agent harnesses and sandbox execution
  metrics/           metrics engine
  analysis/          aggregation and report
apps/
  web/               web platform (TypeScript, phase 2)
data/                metadata and small test fixtures
```

## Data storage

Collected data grows fast and is not code. The storage split is:

- Git stores problem metadata and small test fixtures in `data/`.
- Hugging Face Datasets stores the full dataset: statements, tests, human solutions, and agent solutions.
- Each dataset publication has a version.

## Test strategy

The strategy has three layers, in order of importance:

1. **Golden tests** for the metrics engine. Fixed input solutions have expected metric values in the repository. A change that alters a value must fail a test.
2. **Contract tests** for the schema. Every record that a package produces must validate against the JSON Schema.
3. **Unit tests** for each package. Recorded fixtures replace network calls. Tests must not call external APIs.

The metrics engine has a version number. Each result records the engine version. Results from different engine versions are not comparable, and the version field shows this.

## CI

- GitHub Actions with one workflow.
- Python job: ruff, pyright, pytest.
- Node job: eslint, tsc, vitest.
- Both jobs are mandatory gates for a merge to `main`.
- The CI does not do deployments in phase 1.
