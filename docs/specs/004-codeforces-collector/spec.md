# Spec 004: Codeforces collector

- Status: in-progress
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
  Status: partially met. See the finding below.
- Unit tests cover the API client, the page parser, the anonymizer, and the storage, with recorded fixtures. Met.
- All CI gates stay green. Met.
- The private mapping file never appears in git status. Met.

## Finding: submission source code is blocked

The smoke run of 2026-07-22 collected 3 live problems with statements and sample tests. Every record validated against the schema. Submission metadata (rating, runtime, memory, language) came back through the API for all 9 candidate human submissions. But every fetch of a submission page returned a Codeforces browser challenge instead of source code. This project does not try to defeat the challenge. See finding 6 in [data-licensing-review.md](../../data-licensing-review.md).

This blocks requirement 6 as written: the collector cannot fill `HumanSolution.source_code` from live submission pages today. Options for the owner, not yet decided:

1. Reuse human solutions already published under an open license by precedent datasets (CodeContests, Open-R1 `codeforces-cots`), for problems that those datasets cover. Consistent with the research already in the licensing review.
2. Collect with an authenticated Codeforces session (the owner logs in through a real browser and exports the session cookie). Using an account's own authenticated access differs from defeating anti-bot fingerprinting. This still needs a case-by-case terms check.
3. Ship phase 1 with problem statements and submission metadata only. Treat `source_code` as pending for a later spec once an approach is chosen. Metrics that only need metadata, like runtime and memory, still work. Readability and code-artifact comparisons wait.
4. Ask Codeforces for a data export or research access. Bundle this with the permission request already pending with the owner.

## Out of scope

- The SWE-bench source (a later spec).
- Volume collection. It waits for the owner actions in [data-licensing-review.md](../../data-licensing-review.md) and the registry verification.
- Agent runs and metrics.
- Hugging Face publication.
