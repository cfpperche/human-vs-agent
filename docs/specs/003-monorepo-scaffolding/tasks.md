# Tasks: monorepo scaffolding

- [ ] Create the root uv workspace with shared ruff, pyright, and pytest configuration.
- [ ] Create the five packages with `src/` layout and one placeholder test each.
- [ ] Write the Pydantic models in `packages/schema`.
- [ ] Write the JSON Schema export script and commit the exported files.
- [ ] Add a fixture record in `data/fixtures/` and the contract test.
- [ ] Create `apps/web` with TypeScript strict, eslint, and vitest.
- [ ] Generate a TypeScript type from the JSON Schema and add one test.
- [ ] Write `.github/workflows/ci.yml` with the Python and Node jobs.
- [ ] Enable branch protection on `main` with both jobs required.
- [ ] Verify all acceptance criteria and set the spec status to `done`.
