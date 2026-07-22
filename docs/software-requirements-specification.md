# Software requirements specification

## Introduction

This document lists the requirements of the project. Phase 1 requirements are mandatory now. Phase 2 and phase 3 requirements are recorded for design alignment, and are marked.

Requirement identifiers use the format `R-<area>-<number>`.

## Phase 1: study

### Problem collection

- R-COL-1: The collector must download recent Codeforces problems with statement, sample tests, and metadata.
- R-COL-2: The collector must only accept problems published after the knowledge cutoff of each tested model.
- R-COL-3: The collector must download accepted human submissions for each problem, with author rating, runtime, and memory.
- R-COL-4: The collector must store each problem in the canonical data schema. The schema is in the software design description.
- R-COL-5: The collector must record the collection date for each problem.
- R-COL-6: The system must support SWE-bench Verified tasks as a second problem source.

### Agent execution

- R-AGT-1: The runner must run each model through an agentic harness. The agent can execute code, read errors, and iterate.
- R-AGT-2: The runner must also support one-shot generation for the ablation comparison.
- R-AGT-3: The runner must record the exact model version, prompt, temperature, attempt count, tokens, money cost, and wall-clock time.
- R-AGT-4: All generated code must run in a sandbox with time and memory limits.

### Metrics

- R-MET-1: The system must record test results for each solution.
- R-MET-2: The system must measure runtime and memory for each solution, and compare them with the median accepted human submission.
- R-MET-3: The system must compute code-quality metrics: size, cyclomatic complexity, and lint results.
- R-MET-4: For SWE-bench tasks, the system must compare the agent patch with the merged human pull request: diff size and changed files.
- R-MET-5: The system must support a blind readability comparison between solution pairs.

### Reproducibility

- R-REP-1: The system must freeze and store all run parameters with each result.
- R-REP-2: A second person must be able to reproduce a run from the stored parameters.

## Phase 2: product MVP (marked, not current)

- R-PRD-1: A user can log in and receive one challenge.
- R-PRD-2: The platform must execute the user submission in the sandbox and score it with the phase 1 metrics engine.
- R-PRD-3: The platform must show the user solution and the pre-computed agent solution side by side after submission.
- R-PRD-4: The platform must create an immutable record of each match. See the transparency log design.
- R-PRD-5: The platform must serve problems through an API that uses the canonical data schema.

## Phase 3: gamification (marked, not current)

- R-GAM-1: The platform must show attribute cards for each match. The attribute mapping is in the design document.
- R-GAM-2: A user can have the judge role. Judges vote on blind solution pairs with a rubric.
- R-GAM-3: The judging system must distribute each pair to 3 or 5 judges, and must weight votes by judge reliability.
- R-GAM-4: The judging system must mix gold pairs into judge queues to measure reliability.
- R-GAM-5: The platform must compute a rating for each attribute and show leaderboards.
- R-GAM-6: The platform must collect editor telemetry to flag suspect submissions. Flags do not cause automatic bans.
- R-GAM-7: The competitive leaderboard must be separate from the casual mode.
