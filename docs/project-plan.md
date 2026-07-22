# Project plan

## Roadmap

The project has three sequential phases. Each phase has deliverables and exit criteria.

## Phase 1: study

### Deliverables

1. Codeforces collector. This is the first deliverable. It downloads recent problems, sample tests, and accepted human submissions with metadata.
2. Problem store with the canonical data schema.
3. Runner with agent harnesses and sandbox execution.
4. Metrics engine.
5. Judging pilot with a small group of invited developers. The pilot tests the rubric, the gold pairs, and the judging flow.
6. Study report: artifact comparison, blind-judge results, cost analysis, and the one-shot against agentic ablation.

### Scale

- 30 problems at the start: about 20 Codeforces problems from rating 800 to 2400+, and about 10 SWE-bench Verified tasks.
- 3 or 4 models: one closed frontier model and open-source models for contrast.
- Validate the full pipeline at this scale before growth. Agentic API cost grows fast.

### Exit criteria

- Reproducible results for 30 or more problems and 3 or more models.
- Published report.

## Phase 2: product MVP

### Deliverables

1. Web platform: login, one challenge at a time, submission flow.
2. Sandbox service integration for user submissions.
3. Comparison screen: user solution and pre-computed agent solution side by side, with scores.
4. Transparency log with published hashes.

### Exit criteria

- One user completes the full loop: receive challenge, submit, see comparison.
- Each match has a verifiable log record.

## Phase 3: gamification

### Deliverables

1. Attribute cards and per-attribute ratings.
2. Judge role: queues, rubric votes, gold pairs, reliability weights.
3. Leaderboards and divisions. The competitive division is separate from the casual mode.
4. "Guess the AI" game mode.
5. Anti-cheat telemetry and flags.

### Exit criteria

- Judges produce verdicts with measured reliability.
- Leaderboards are active with the anti-cheat flags in place.

## Recurring work

- Content pipeline: collect new problems continuously. Fresh problems keep the human comparison fair and keep the contamination claim honest.
- Model updates: add new model versions and record their knowledge cutoffs.
