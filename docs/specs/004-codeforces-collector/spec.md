# Spec 004: Codeforces collector

- Status: draft
- Date: 2026-07-22

## Goal

Implement the collector for the Codeforces source. The collector downloads recent problems and accepted human submissions, and stores them in the canonical schema. All later work (runner, metrics, judging) consumes this data.

## Requirements

1. The collector must use the official Codeforces API for problem metadata and submission metadata.
2. The request rate must stay at or below 1 request in 1 second, with backoff on errors. The documented platform limit is 5 in 1 second; we stay far under it.
3. The collector must fetch the statement and the sample tests from the problem page, at low volume, with a local cache.
4. The collector must accept only problems published after the freshness threshold in [model-registry.md](../../model-registry.md).
5. The rating range and the problem count must be command arguments.
6. For each problem, the collector must download up to K accepted human submissions across three rating bands, with author rating, runtime, and memory.
7. The collector must anonymize at ingestion: the handle becomes a stable pseudonymous `author_id`, and the private mapping stays outside git.
8. The output must validate against the exported JSON Schema (contract test).
9. Collected data goes to `data/collected/`, which is outside git. Only small anonymized fixtures enter git.
10. A second run must skip problems that are already collected.
11. Tests must use recorded fixtures only. No test makes a network call.

## Acceptance criteria

- A manual smoke run collects 3 problems with submissions from a live window, and every record validates against the schema.
- Unit tests cover the API client, the page parser, the anonymizer, and the storage, with recorded fixtures.
- All CI gates stay green.
- The private mapping file never appears in git status.

## Out of scope

- The SWE-bench source (a later spec).
- Volume collection. It waits for the owner actions in [data-licensing-review.md](../../data-licensing-review.md) and the registry verification.
- Agent runs and metrics.
- Hugging Face publication.
