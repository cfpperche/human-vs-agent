# Human vs Agent

A comparative study of human solutions and AI-agent solutions to the same programming problems.

## What this project does

Current benchmarks rank models. They run a model on a problem, record pass or fail, and discard the solution. LiveCodeBench and SWE-bench work this way.

This project keeps the solutions. It puts the human solution and the agent solution side by side. Then it measures the differences between the two artifacts.

## What we measure

- **Correctness**: test results by difficulty level.
- **Performance**: run time and memory, compared with the median human submission.
- **Code quality**: complexity, size, and lint results.
- **Readability**: blind pairwise votes from calibrated judges.
- **Cost**: tokens, money, and wall-clock time for each solution.

## Why this is different

We ask a different question. We do not ask "which model has the highest pass rate?". We ask "when a human and an agent solve the same problem, what is different in the solutions, and at what cost?".

The answer stays useful when models improve. The characterization of the differences is the product, not the ranking.

## Project phases

1. **Study**: collect recent problems, run agents, compare artifacts, publish a report.
2. **Product MVP**: a web platform where a person solves a challenge and sees the agent comparison.
3. **Gamification**: attribute cards, judge roles, ratings, and leaderboards.

## Documentation

All project documents are in [/docs](docs/README.md). All documents follow ASD-STE100 (Simplified Technical English). See the [documentation standard](docs/documentation-standard.md).

## License

Apache-2.0. See [LICENSE](LICENSE).
