# Development workflow

## Purpose

This document defines the development flow for all contributors, human and agent. The flow connects the spec process, the CI gates, and the handoff file.

## Flow overview

```
approved spec -> branch -> implement -> local gates -> pull request + self-review -> owner merge -> post-merge updates
```

## Steps

### 1. Start from an approved spec

Work starts only when a spec in `docs/specs/` has the status `approved`. The spec process is in [specs/README.md](specs/README.md).

Exception: small corrections to documents or configuration do not need a spec. Use a `chore/short-name` branch for them.

### 2. Create a branch and a worktree

- Branch from `main`: `spec/NNN-short-name`.
- Create a git worktree for the branch, in a directory outside the repository clone:

```
git worktree add ../hva-worktrees/NNN-short-name -b spec/NNN-short-name main
```

- Do all work inside the worktree. Do not work in the main clone. The main clone always stays on `main`.
- One worktree for each active spec. Parallel agents then do not conflict in one working directory.
- After the merge, remove the worktree: `git worktree remove ../hva-worktrees/NNN-short-name`.
- `main` is protected. Only a pull request with green CI can merge.
- Do not push directly to `main`.

### 3. Implement

- Follow the order of work in the spec `plan.md`.
- Mark each task in `tasks.md` when it is complete.
- Follow the rules in [technology-stack.md](technology-stack.md).

### 4. Run the local gates before each push

- Python: `ruff check`, `ruff format --check`, `pyright`, `pytest`.
- Node: `eslint`, `tsc --noEmit`, `vitest run`.
- Do not push when a gate fails.

### 5. Open a pull request

The pull request must contain:

- A title in the commit convention format.
- A link to the spec.
- The list of acceptance criteria that the change covers.
- A note on each deviation from `plan.md`, with the reason.

After the pull request is open, the author agent must do an adversarial review of the full diff. The review looks for bugs, missing tests, and unnecessary complexity. The agent posts the findings as a pull request comment, with the fixes applied or the reasons to not fix.

### 6. Merge

- The owner merges. Agents must not merge.
- The merge method is squash. The squash message follows the commit convention.
- CI must be green before the merge.

### 7. After the merge

1. Update the baseline documents in `/docs` that the change affects.
2. Update the spec status. A spec becomes `done` only when all acceptance criteria pass.
3. Update `HANDOFF.md`.

## Commit convention

The project uses Conventional Commits.

- Format: `type(scope): subject`.
- Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`.
- Scopes: `schema`, `collector`, `runner`, `metrics`, `analysis`, `web`, `specs`, `docs`.
- Write the subject in the imperative mood, in English, at 72 characters or fewer.
- Add a body when the reason for the change is not obvious from the subject.
- An agent commit must name the agent in a `Co-Authored-By` trailer.

Examples:

```
feat(schema): add MatchRecord model with JSON Schema export
fix(collector): reject problems published before the model cutoff
docs(specs): mark spec 003 as done
```
