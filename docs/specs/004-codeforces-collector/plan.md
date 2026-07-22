# Plan: Codeforces collector

## Approach

All code goes to `packages/collector` as `hva_collector`. New dependency: `httpx`.

### Modules

- `api.py`: typed client for the official API (`problemset.problems`, `contest.status`, `user.info`). One retry policy, one rate limiter (1 request in 1 second).
- `pages.py`: fetch of problem pages and submission pages, with an on-disk cache in `data/collected/.cache/`.
- `parse.py`: extraction of the statement text and the sample tests from problem HTML.
- `anonymize.py`: stable pseudonymous `author_id` from a keyed hash. The key and the mapping live in `data/private/` (outside git).
- `store.py`: write `Problem` and `HumanSolution` records as JSON under `data/collected/<problem-id>/`, with schema validation on write.
- `cli.py`: `uv run hva-collect --since <date> --ratings 800-2400 --limit N --solutions-per-problem K`.

### Selection logic

1. List recent contests. Keep problems published after the freshness threshold plus the margin.
2. Filter by the rating range. Spread the picks across rating bands.
3. For each problem, take accepted submissions in three author-rating bands. Prefer submissions near the median runtime.

### Fixtures

Record real API and page responses one time with a helper script. Store scrubbed copies under `packages/collector/tests/fixtures/`. Tests replay them; no test touches the network.

## Order of work

1. API client with the rate limiter and recorded fixtures.
2. Page fetch, cache, and statement parser.
3. Anonymizer and storage with schema validation.
4. CLI and the idempotent skip logic.
5. Manual smoke run (3 problems) and the acceptance check.
