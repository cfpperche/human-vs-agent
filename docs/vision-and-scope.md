# Vision and scope

## Problem statement

Frontier models and some open-source models now solve most standard programming problems. Current benchmarks measure this with a pass rate. LiveCodeBench ranks models on recent competitive-programming problems. SWE-bench ranks models on real GitHub issues.

These benchmarks treat a solution as a boolean: pass or fail. They discard the solution after the tests run. Nobody compares the model solution with the human solution as two artifacts.

## The gap this project fills

This project answers questions that current benchmarks do not answer:

1. How is agent code different from human code for the same problem? We compare length, runtime, memory, structure, and approach.
2. Can a blind judge identify which solution is from an agent?
3. What is the cost difference? We compare human time with agent time and agent money cost.
4. How much does the agentic mode change results? We compare one-shot generation with iterative agent runs on the same problems.

The output is a characterization of differences, not a ranking. A ranking becomes stale with each model release. A characterization stays useful.

## Solution vision

The project has three phases. Each phase builds on the previous one.

### Phase 1: study

A comparative study on 30 to 50 recent problems. Problem sources:

- Codeforces rounds published after the model knowledge cutoffs. The Codeforces API gives human submissions with rating, runtime, and memory.
- SWE-bench Verified tasks, or fresh GitHub issues that we collect. The merged human pull request is the human solution.

Agents run in agentic mode: they can execute code, read errors, and iterate. The study report is the phase deliverable.

### Phase 2: product MVP

A web platform. A person logs in and receives a challenge. The person submits a solution. The platform then shows the human solution and the pre-computed agent solution side by side, with scores.

The agent solutions are pre-computed one time for each problem. The marginal cost for each user submission is only the sandbox execution.

### Phase 3: gamification

- Attribute cards for each match. The attributes map to benchmark metrics: strength, speed, agility, precision, efficiency, elegance.
- A judge role with calibration, vote weights, and progression.
- Ratings for each attribute, leaderboards, and divisions.
- A "guess the AI" game mode that also collects study data.

## Out of scope

- Competition with LeetCode or Codeforces on problem-bank size.
- A public model leaderboard.
- Blockchain infrastructure. The transparency log uses simple published hashes.

## Success criteria

- Phase 1: a published report with reproducible results for 30 or more problems and 3 or more models.
- Phase 2: a working platform where one user completes the full challenge loop.
- Phase 3: active judges produce verdicts with measured reliability.
