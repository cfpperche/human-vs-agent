# Model registry and study budget

## Purpose

This document freezes the model list, the freshness rule, and the budget for the phase 1 study. The collector and the runner read their parameters from this document.

## Model list (proposal, owner ratifies)

One closed frontier model and three open-source models, as the project plan states.

| # | Model | Provider | Access | Exact API identifier | Release date | Knowledge cutoff |
|---|---|---|---|---|---|---|
| 1 | Claude Fable 5 | Anthropic | API | `claude-fable-5` | TBV | TBV |
| 2 | DeepSeek V4 | DeepSeek | API or self-host | TBV | TBV | TBV |
| 3 | GLM-5.2 | Zhipu | API or self-host | TBV | TBV | TBV |
| 4 | Kimi K2.7 Code | Moonshot | API | TBV | 2026-06-12 | TBV |

TBV = to be verified. Verification of every TBV cell is a blocker for the first collection. Record the verified values here with the source URL.

## Freshness rule

1. The collection threshold is the most recent date in the table: the latest release date or knowledge cutoff, whichever is later.
2. The collector accepts only problems published after the threshold plus a margin of 7 days.
3. A new model in the registry moves the threshold. Problems collected before the change stay valid only for the models that they already cover.
4. Each problem record stores its publication date. Each result records the model identifier. An audit can then check every pair.

## Study budget (proposal, owner ratifies)

- Cap: **USD 400** for all phase 1 agent runs.
- Scope: API costs of the four models, both modes (one-shot and agentic), all attempts.
- Each run records its cost in the `AgentSolution.cost_usd` field. A session report sums the total.
- Alert rule: at 50% of the cap, report the spend to the owner in the session summary.
- Stop rule: at 100% of the cap, stop all runs. Only the owner can raise the cap. Partial results stay valid and enter the report with a coverage note.

## Change rules

- A model version change is a new registry row, not an edit. Results never mix rows.
- Do not remove a row after runs used it. Mark it as retired.
