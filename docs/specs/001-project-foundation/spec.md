# Spec 001: project foundation

- Status: done
- Date: 2026-07-22
- Note: this spec is retroactive. The work was complete before the spec process started.

## Goal

Create the public repository with the project documentation and the AI-agent configuration.

## Requirements

1. The repository `cfpperche/human-vs-agent` must be public on GitHub.
2. The license must be Apache-2.0.
3. Agent instructions must exist for Claude Code, Codex, and Grok, with one canonical file.
4. ASD-STE100 must be the documented standard for all project documents.
5. The SDLC documents must exist in `/docs`: vision and scope, SRS, design description, project plan, risk register.

## Acceptance criteria

- The repository is public and `main` is pushed. ✔
- `AGENTS.md` is canonical. `CLAUDE.md` imports it. `GROK.md` points to it. ✔
- `docs/documentation-standard.md` defines the STE rules and the review procedure. ✔
- All six SDLC documents exist and follow STE. ✔
