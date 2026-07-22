# Data licensing review

- Review date: 2026-07-22
- Note: this review is research, not legal advice. The owner accepts or rejects the residual risk.

## Scope

The review covers the two data sources of phase 1 and the plan to publish a dataset on Hugging Face:

1. Codeforces: problem statements and human submissions.
2. SWE-bench: tasks built from open-source repositories.

## Findings: Codeforces

1. Codeforces publishes problems and submissions publicly, but with no standard open license. Community discussions confirm this gap.
2. Codeforces has an official public API (`codeforces.com/apiHelp`) with a documented rate limit of 5 requests in one second. The API gives problems and submission metadata. It does not give submission source code. Source code needs page access.
3. Strong precedent exists for redistribution with attribution:
   - DeepMind CodeContests republishes Codeforces statements and human solutions (correct and incorrect). Non-code materials are under CC-BY 4.0, with the note "Codeforces materials are sourced from http://codeforces.com".
   - Open-R1 `codeforces-cots` republishes statements and solutions on Hugging Face under CC-BY 4.0.
   - LiveCodeBench hosts Codeforces problems on Hugging Face.
   These datasets are public since 2022 or later and stay online.
4. Precedent is not permission. The copyright of a submission stays with its author. The copyright of a statement stays with the problem author and the platform.
5. The Codeforces terms page (`codeforces.com/terms`) blocks automated access. A person must read it.
6. As of 2026-07-22, Codeforces submission pages return a browser challenge (a Cloudflare-style JavaScript check) to automated clients. The official API still gives submission metadata (rating, runtime, memory, language), but the collector cannot retrieve submission source code through the page. See `docs/specs/004-codeforces-collector/spec.md` for the technical finding. This project does not attempt to defeat the challenge: doing so conflicts with the low-volume, respectful-access approach in decision 1.

## Findings: SWE-bench

1. The SWE-bench code repository is MIT. Related dataset variants use MIT or CC-BY 4.0.
2. The underlying GitHub repositories are open source. Their licenses permit redistribution of issues and patches with attribution and license preservation.
3. SWE-rebench states the correct pattern: respect the license of each specific repository for each instance.
4. Risk level: low.

## Decisions

1. **Collection**: use the official Codeforces API where possible, and respect the rate limit. Page access only for submission source code, at low volume.
2. **Publication**: follow the CodeContests pattern. Our own materials (metadata, metrics, agent outputs under our control) are CC-BY 4.0. Human source code is redistributed as-is: the rights stay with the authors, and our license does not cover it.
3. **Attribution**: each problem record keeps the source URL. Each SWE-bench instance keeps the repository license.
4. **Takedown policy**: the dataset page states that Codeforces or an author can request removal of content, and we remove it.
5. **Anonymization**: the published dataset replaces the author handle with a stable pseudonymous identifier plus a rating band. The handle stays only in a private mapping for deduplication. Rating, runtime, and memory stay in the open data.

## Open actions for the owner

- [ ] Read `codeforces.com/terms` in a browser and confirm that the decisions above do not conflict with it.
- [ ] Decide on a permission request to Codeforces (a short message to the platform). A positive answer removes the residual risk. This is the recommended path.
- [ ] Decide how to handle submission source code, blocked by finding 6. See the options in `docs/specs/004-codeforces-collector/spec.md`.

## Sources

- [Codeforces terms page](https://codeforces.com/terms) (blocked to automated access)
- [Codeforces API help](https://codeforces.com/apiHelp)
- [Codeforces community discussion on datasets](https://codeforces.com/topic/145334/en1)
- [DeepMind CodeContests](https://github.com/google-deepmind/code_contests)
- [Open-R1 codeforces-cots dataset](https://huggingface.co/datasets/open-r1/codeforces-cots)
- [LiveCodeBench dataset](https://huggingface.co/datasets/livecodebench/code_generation)
- [SWE-bench dataset](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified)
- [SWE-rebench dataset](https://huggingface.co/datasets/nebius/SWE-rebench)
