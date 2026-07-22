# Software design description

## Overview

The system has five components. Phase 1 builds the first three. Phases 2 and 3 add the last two.

```
collector  ->  problem store  ->  runner  ->  metrics engine
                                                  |
                              judging system <----+----> transparency log
```

## Repository structure

The monorepo layout, the toolchains, and the dependency rules are in the [technology stack](technology-stack.md) document.

```
docs/                SDLC documents
packages/schema/     canonical data schema, JSON Schema export
packages/collector/  Codeforces and SWE-bench collection
packages/runner/     agent harnesses and sandbox execution
packages/metrics/    metrics engine
packages/analysis/   aggregation and report
apps/web/            web platform (phase 2)
data/                metadata and small test fixtures
```

## Components

### Collector

The collector downloads problems and human solutions.

- Codeforces source: the public API gives problems, ratings, and accepted submissions. Each human submission keeps author rating, runtime, and memory.
- SWE-bench source: each task keeps the issue, the test set, and the merged human pull request.
- The collector rejects problems published before the model knowledge cutoffs.

### Problem store and canonical data schema

Each problem is one record. The schema is API-ready for phase 2. The record contains:

- problem: identifier, source, statement, difficulty rating, publication date, collection date
- tests: sample tests and hidden tests
- human solutions: source code, author rating, runtime, memory, submission date
- agent solutions: source code, model version, harness mode, prompt, temperature, attempts, tokens, money cost, wall-clock time
- metrics: test results, runtime, memory, code-quality values
- verdicts: judge votes and aggregated results

### Runner

The runner executes agents and solutions.

- Agent harness: Claude Code in headless mode, and equivalent harnesses for other models. The agent can execute code and iterate.
- One-shot mode: a single generation call, for the ablation comparison.
- Sandbox: containers with time and memory limits. Generated code never runs outside the sandbox.

### Metrics engine

The metrics engine computes the comparison values:

- Correctness: test results, first-attempt success.
- Performance: runtime and memory against the median accepted human submission.
- Code quality: size, cyclomatic complexity, lint results.
- SWE tasks: diff size and changed-file overlap with the human pull request.
- Cost: tokens, money, and wall-clock time.

### Judging system (phases 1 pilot, 3 full)

The judging system measures what the metrics engine cannot measure: readability, maintainability, elegance.

- Votes are pairwise, not absolute scores. A judge sees two solutions and answers rubric questions. Example: "which solution has clearer names: A, B, or equal?".
- The system normalizes both solutions before display: one formatter, comments removed. Comments are a separate criterion.
- Blind protocol: the judge does not know which solution is human. After the quality votes, the judge guesses which solution is from an agent. The guess measures bias and feeds the "guess the AI" game mode.
- Gold pairs: the queue contains pairs with known answers. Gold-pair accuracy measures judge reliability.
- Aggregation: 3 or 5 judges for each pair. The verdict is a reliability-weighted vote. Close results escalate to more judges.
- Assignment is random and anonymous. A judge never judges an own match.
- Cold start: an LLM judge gives a provisional verdict. Human judges confirm or reverse it. The agreement rate between LLM and human judges is a study result.

### Transparency log (phase 2)

The log makes each match auditable.

- Each match becomes one canonical record: human code, agent code, benchmark results, timestamps, model versions, runner version.
- The system computes the SHA-256 hash of the record.
- Hashes go into an append-only log. The system publishes the log root periodically to an external location, for example a public repository.
- Any person can verify that a match record exists and did not change.
- The design does not use a blockchain. The requirement is auditability, not decentralized consensus.

## Attribute card mapping (phase 3)

| Card attribute | Benchmark metric |
|---|---|
| Strength | Highest problem rating solved |
| Speed | Solution runtime against human median and agent solution |
| Agility | Wall-clock time to submit |
| Precision | First-attempt success rate |
| Efficiency | Memory use |
| Elegance | Blind readability verdict |

Each attribute has its own rating and leaderboard.

## Design decisions

- Agent solutions are pre-computed one time for each problem. User submissions only cost a sandbox run.
- The data schema is API-ready from phase 1. This prevents a migration in phase 2.
- Sandbox execution can use an existing service, for example Judge0, in phase 2.
