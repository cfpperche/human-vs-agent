# Handoff

This file gives the project state to the next person or agent. Update this file at the end of each work session.

- Last update: 2026-07-22
- Last commit: `15c2e93` (spec process with specs 001-003)

## Project summary

A comparative study of human solutions and AI-agent solutions to the same programming problems. The study grows into a gamified platform in later phases. Read `README.md` and `docs/vision-and-scope.md` for the full context.

## Current state

- The repository contains only documentation. No code exists yet.
- All SDLC documents are in `/docs` and follow ASD-STE100. See `docs/README.md` for the index.
- The spec process is active. See `docs/specs/README.md`.
- Spec 001 (project foundation) is done.
- Spec 002 (technology stack) is done.
- Spec 003 (monorepo scaffolding) is in `draft`. It waits for owner approval.

## Locked decisions

- Hybrid monorepo: Python pipeline (uv, Pydantic, ruff, pyright, pytest) and TypeScript web app (strict, pnpm, eslint, vitest).
- `packages/schema` is the only cross-language contract, through exported JSON Schema.
- Data split: metadata and fixtures in git, full dataset on Hugging Face Datasets.
- Test strategy: golden tests, schema contract tests, unit tests with recorded fixtures.
- CI: one GitHub Actions workflow, Python and Node jobs as mandatory merge gates.

Details are in `docs/technology-stack.md`.

## Next action

1. Get owner approval for spec 003.
2. Set the spec status to `approved`, then implement it. Follow `docs/specs/003-monorepo-scaffolding/plan.md` and update `tasks.md` during the work.
3. After spec 003, the next spec is the Codeforces collector. See `docs/project-plan.md`.

## Open decisions

- Web framework for `apps/web` (open until phase 2 starts).
- Hugging Face dataset name and organization.
- Model list for the study (one closed frontier model plus open-source models).

## Rules for the next session

- Read `AGENTS.md` first. It is the canonical agent instruction file.
- Do not start implementation without an approved spec.
- Write all documents in ASD-STE100. See `docs/documentation-standard.md`.
- Update this file before you end the session.
