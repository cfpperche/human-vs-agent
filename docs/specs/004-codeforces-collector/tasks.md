# Tasks: Codeforces collector

- [x] Add `httpx` to `packages/collector` and create the module skeleton.
- [x] Implement the API client with the rate limiter and backoff.
- [x] Record the API fixtures and write the client tests.
- [x] Implement the page fetch with the on-disk cache.
- [x] Implement the statement and sample-test parser, with fixtures and tests.
- [x] Implement the anonymizer with the private mapping, and its tests.
- [x] Implement the storage with schema validation on write, and its tests.
- [x] Implement the CLI with the freshness, rating, and limit arguments.
- [x] Implement the idempotent skip logic.
- [x] Run the manual smoke run (3 problems). Problems and statements collect and validate. Submission source code is blocked; see the finding in `spec.md`.
- [ ] Owner: pick an option for the submission-source finding.
- [ ] Set the spec status to `done` and update the baseline documents. Blocked on the item above.
