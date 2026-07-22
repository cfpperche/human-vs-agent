# Handoff

This file gives the project state to the next person or agent. Update this file at the end of each work session.

- Last update: 2026-07-22
- Last commit: `feat(collector): implement the Codeforces collector` (branch `spec/004-codeforces-collector`, PR #4 open, not merged)

## Project summary

A comparative study of human solutions and AI-agent solutions to the same programming problems. The study grows into a gamified platform in later phases. Read `README.md` and `docs/vision-and-scope.md` for the full context.

## Current state

- The monorepo scaffolding is on `main` (PR #1 merged). The CI gates and the branch protection are active.
- All SDLC documents are in `/docs` and follow ASD-STE100. See `docs/README.md` for the index.
- The spec process is active. See `docs/specs/README.md`.
- Spec 001 (project foundation) is done.
- Spec 002 (technology stack) is done.
- Spec 003 (monorepo scaffolding) is done.
- Spec 004 (Codeforces collector) is `in-progress`. PR #4 is open with green CI and a self-review comment, but not merged.
  - The collector works for problems, statements, and sample tests. A live smoke run collected 3 real problems, all schema-valid.
  - Submission source code is blocked: Codeforces returns a browser challenge to automated page fetches. The API gives submission metadata (rating, runtime, memory) but not source. The project does not attempt to defeat the challenge.
  - 4 options are documented in `docs/specs/004-codeforces-collector/spec.md` (finding section). The owner has not picked one yet.
- The model registry and the study budget are ratified (PR #3 merged): see `docs/model-registry.md`. The TBV cells (exact model IDs, release dates, cutoffs) still need verification before any study run.
- The goals and the non-goals are defined in `docs/vision-and-scope.md`.
- `docs/pre-code-checklist.md` governs the order of the remaining foundation work.

## Locked decisions

- Hybrid monorepo: Python pipeline (uv, Pydantic, ruff, pyright, pytest) and TypeScript web app (strict, pnpm, eslint, vitest).
- `packages/schema` is the only cross-language contract, through exported JSON Schema.
- Data split: metadata and fixtures in git, full dataset on Hugging Face Datasets. Collected data and the private author mapping live in `data/collected/` and `data/private/`, both outside git.
- Test strategy: golden tests, schema contract tests, unit tests with recorded fixtures. No test makes a network call.
- CI: one GitHub Actions workflow, Python and Node jobs as mandatory merge gates.
- Development workflow: spec branch in a dedicated worktree outside the clone, local gates, pull request with adversarial self-review, owner merges with squash, Conventional Commits. See `docs/development-workflow.md`.
- Model registry: one frontier model (Claude Fable 5) plus three open-source models (DeepSeek V4, GLM-5.2, Kimi K2.7 Code). Study runs must use a registry model; exploratory runs during development can use any model but never enter the published data. Budget cap: USD 400, alert at 50%, stop at 100%. See `docs/model-registry.md`.

Details are in `docs/technology-stack.md`.

## Next action

1. Owner: pick an option for the submission-source finding in `docs/specs/004-codeforces-collector/spec.md`, then review and merge PR #4 (or request changes first).
2. Owner: read the Codeforces terms in a browser and decide on a permission request. This can resolve the submission-source finding too (option 4). See the open actions in `docs/data-licensing-review.md`.
3. Verify the TBV cells in `docs/model-registry.md` (exact model IDs, release dates, cutoffs) before any study run.
4. Before agent runs: pre-register the study (hypotheses, metrics, analysis plan) and define the judging rubric and gold-pair set.
5. After spec 004 closes, the next spec is the runner (agent harnesses and sandbox execution). See `docs/project-plan.md`.

## Open decisions

- Web framework for `apps/web` (open until phase 2 starts).
- Hugging Face dataset name and organization.
- The submission-source approach (see spec 004's finding: reuse a precedent dataset, authenticated session, metadata-only for now, or a Codeforces data request).

## Rules for the next session

- Read `AGENTS.md` first. It is the canonical agent instruction file.
- Do not start implementation without an approved spec.
- Write all documents in ASD-STE100. See `docs/documentation-standard.md`.
- Update this file before you end the session.
