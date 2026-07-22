# Handoff

This file gives the project state to the next person or agent. Update this file at the end of each work session.

- Last update: 2026-07-22
- Last commit: `ci: enforce the lockfile with uv sync --locked` (branch `spec/003-monorepo-scaffolding`)

## Project summary

A comparative study of human solutions and AI-agent solutions to the same programming problems. The study grows into a gamified platform in later phases. Read `README.md` and `docs/vision-and-scope.md` for the full context.

## Current state

- The monorepo scaffolding exists on the branch `spec/003-monorepo-scaffolding` (PR #1, CI green). `main` still has only documentation.
- All SDLC documents are in `/docs` and follow ASD-STE100. See `docs/README.md` for the index.
- The spec process is active. See `docs/specs/README.md`.
- Spec 001 (project foundation) is done.
- Spec 002 (technology stack) is done.
- Spec 003 (monorepo scaffolding) is `in-progress`. PR #1 is open with green CI and the self-review comment. It waits for the owner merge.
- The goals and the non-goals are defined in `docs/vision-and-scope.md`.
- `docs/pre-code-checklist.md` governs the order of the remaining foundation work. All items up to the first line of code are there.

## Locked decisions

- Hybrid monorepo: Python pipeline (uv, Pydantic, ruff, pyright, pytest) and TypeScript web app (strict, pnpm, eslint, vitest).
- `packages/schema` is the only cross-language contract, through exported JSON Schema.
- Data split: metadata and fixtures in git, full dataset on Hugging Face Datasets.
- Test strategy: golden tests, schema contract tests, unit tests with recorded fixtures.
- CI: one GitHub Actions workflow, Python and Node jobs as mandatory merge gates.
- Development workflow: spec branch in a dedicated worktree outside the clone, local gates, pull request with adversarial self-review, owner merges with squash, Conventional Commits. See `docs/development-workflow.md`.

Details are in `docs/technology-stack.md`.

## Next action

Work through the pending items in `docs/pre-code-checklist.md`, in this order:

1. Owner: merge PR #1 with squash. Then set spec 003 to `done`, update the baseline documents, and remove the worktree.
2. Owner: read the Codeforces terms in a browser and decide on a permission request. See the open actions in `docs/data-licensing-review.md`.
3. Before data collection: create the model registry and set the study budget.
4. Before agent runs: pre-register the study and define the judging rubric.
5. After spec 003, the next spec is the Codeforces collector. See `docs/project-plan.md`.

## Open decisions

- Web framework for `apps/web` (open until phase 2 starts).
- Hugging Face dataset name and organization.
- Model list for the study (one closed frontier model plus open-source models).

## Rules for the next session

- Read `AGENTS.md` first. It is the canonical agent instruction file.
- Do not start implementation without an approved spec.
- Write all documents in ASD-STE100. See `docs/documentation-standard.md`.
- Update this file before you end the session.
