# Pre-code checklist

## Purpose

This document records all foundation steps, complete and pending, up to the first line of code. Steps that block later milestones are also here, with their block points. Mark each step when it is complete.

## Complete

- [x] Define the problem and the gap: artifact comparison, not a leaderboard. See [vision-and-scope.md](vision-and-scope.md).
- [x] Define the three phases: study, product MVP, gamification.
- [x] Create the public repository with the Apache-2.0 license.
- [x] Configure the AI agents: `AGENTS.md` canonical, `CLAUDE.md` and `GROK.md` pointers.
- [x] Adopt ASD-STE100 as the documentation standard. See [documentation-standard.md](documentation-standard.md).
- [x] Write the SDLC baseline documents in `/docs`.
- [x] Decide the technology stack: hybrid monorepo, schema contract, data split, test strategy, CI. See [technology-stack.md](technology-stack.md).
- [x] Adopt the spec process with `docs/specs/NNN-short-name/`. See [specs/README.md](specs/README.md).
- [x] Record the foundation work in the retroactive specs 001 and 002.
- [x] Create `HANDOFF.md` for session continuity.
- [x] Define the development workflow: branches, gates, self-review, owner merge, Conventional Commits. See [development-workflow.md](development-workflow.md).
- [x] Write spec 003 (monorepo scaffolding) with plan and tasks.
- [x] Create this checklist and review the plan for missing critical steps.

## Pending: before the first line of code

- [x] Define the goals and the non-goals of the project. See the goals and non-goals sections in [vision-and-scope.md](vision-and-scope.md).
- [x] Do a legal review of the data sources. See [data-licensing-review.md](data-licensing-review.md) for the findings, the decisions, and the anonymization rule.
- [x] Get owner approval for spec 003 and set its status to `approved`.

## Pending: before the first data collection

- [x] Create the model registry. See [model-registry.md](model-registry.md). The TBV cells block the first collection.
- [x] Set the study budget: USD 400 cap with alert and stop rules. See [model-registry.md](model-registry.md).
- [ ] Owner: read the Codeforces terms in a browser and decide on a permission request. See the open actions in [data-licensing-review.md](data-licensing-review.md).

## Pending: before the first agent run

- [ ] Pre-register the study: write the hypotheses, the metrics, and the analysis plan. Freeze them before the runs start. A frozen plan protects the study from result-driven analysis.
- [ ] Define the judging rubric and the gold-pair set for the pilot.

## Review note

Steps found in the review of 2026-07-22 that were not in the original plan:

1. Goals and non-goals (found by the owner).
2. Legal review of data sources and author anonymization.
3. Model registry with cutoff dates and a budget cap.
4. Study pre-registration with a frozen analysis plan.
