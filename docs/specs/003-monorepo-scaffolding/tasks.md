# Tasks: monorepo scaffolding

- [x] Create the root uv workspace with shared ruff, pyright, and pytest configuration.
- [x] Create the five packages with `src/` layout and one placeholder test each.
- [x] Write the Pydantic models in `packages/schema`.
- [x] Write the JSON Schema export script and commit the exported files.
- [x] Add a fixture record in `data/fixtures/` and the contract test.
- [x] Create `apps/web` with TypeScript strict, eslint, and vitest.
- [x] Generate a TypeScript type from the JSON Schema and add one test.
- [x] Write `.github/workflows/ci.yml` with the Python and Node jobs.
- [ ] Enable branch protection on `main` with both jobs required.
- [ ] Verify all acceptance criteria and set the spec status to `done`.
