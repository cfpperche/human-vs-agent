# Spec process

## Purpose

This project uses spec-driven development. Each unit of work has a spec before implementation starts. The specs are the change history of the project. The other documents in `/docs` show the current state.

## Location and names

- Each spec is one directory: `docs/specs/NNN-short-name/`.
- `NNN` is a three-digit sequential number.
- `short-name` is a short kebab-case name.

## Files in a spec

| File | Content | When |
|---|---|---|
| `spec.md` | Goal, requirements, acceptance criteria, status. | Mandatory, first. |
| `plan.md` | The technical approach. | Before implementation starts. |
| `tasks.md` | The task checklist with progress marks. | Before implementation starts, updated during the work. |

## Status values

A spec has one status in its header:

- `draft`: the spec is in discussion.
- `approved`: the owner approved the spec. Implementation can start.
- `in-progress`: implementation started.
- `done`: all acceptance criteria passed.

## Rules

- Do not start implementation without an approved spec.
- When a spec becomes `done`, update the baseline documents in `/docs` to show the new state.
- Do not delete or rewrite a `done` spec. Specs are history. Create a new spec for a change.
- All spec files must follow the [documentation standard](../documentation-standard.md).

## Spec index

| Spec | Title | Status |
|---|---|---|
| [001](001-project-foundation/spec.md) | Project foundation | done |
| [002](002-technology-stack/spec.md) | Technology stack | done |
| [003](003-monorepo-scaffolding/spec.md) | Monorepo scaffolding | draft |
