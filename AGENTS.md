# Agent instructions

This file is the canonical instruction file for all AI agents (Claude Code, Codex, Grok, and others). `CLAUDE.md` and `GROK.md` point here. Do not duplicate content in those files.

## Project context

This repository contains a comparative study of human solutions and AI-agent solutions to programming problems. Read `README.md` for the project summary. Read `docs/vision-and-scope.md` for the full vision.

The project has three phases:

1. Study: collect problems, run agents, compare solution artifacts.
2. Product MVP: web platform for human challenges with agent comparison.
3. Gamification: cards, judges, ratings, leaderboards.

The current phase is phase 1.

## Spec process (mandatory)

The project uses spec-driven development. The process is in `docs/specs/README.md`. Key rules:

- Do not start implementation without an approved spec in `docs/specs/NNN-short-name/`.
- Update `tasks.md` of the active spec while you work.
- When a spec becomes `done`, update the baseline documents in `/docs`.
- Do not change a `done` spec. Create a new spec for a change.

## Documentation standard (mandatory)

All documents in this repository must follow ASD-STE100 (Simplified Technical English). The rules are in `docs/documentation-standard.md`. Read that file before you write or change any document.

Key rules:

- Write in English.
- Use the active voice.
- Write one instruction in each sentence.
- Keep procedural sentences at 20 words or fewer.
- Keep descriptive sentences at 25 words or fewer.
- Use one word for one meaning.

## Repository structure

```
docs/           SDLC documents (STE)
packages/       Python pipeline packages: schema, collector, runner, metrics, analysis
apps/           TypeScript applications: web (phase 2)
data/           problem metadata and small test fixtures
```

The toolchains, the dependency rules, and the test strategy are in `docs/technology-stack.md`. Read that file before you write code. Key rules:

- Python packages: uv, Pydantic, ruff, pyright, pytest.
- TypeScript: strict mode, pnpm, eslint, vitest.
- All packages can depend on `packages/schema`. The `schema` package must not depend on other packages.
- Tests must not call external APIs. Use recorded fixtures.
- A change to the metrics engine that alters a golden-test value must be intentional and must increase the engine version.

## Conventions

- All text in the repository is in English.
- Commit messages: imperative mood, short subject line, English.
- Do not commit secrets, API keys, or `.env` files.
- Update the documents in `/docs` when a design decision changes.
- Update `HANDOFF.md` at the end of each work session. It gives the project state to the next session.
