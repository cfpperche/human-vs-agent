import type { MatchRecord } from "./generated/match-record.js";

export interface MatchSummary {
  matchId: string;
  problemTitle: string;
  humanRuntimeMs: number | null;
  agentModel: string;
  agentCostUsd: number;
}

export function summarizeMatch(record: MatchRecord): MatchSummary {
  return {
    matchId: record.id,
    problemTitle: record.problem.title,
    humanRuntimeMs: record.human_solution.runtime_ms ?? null,
    agentModel: record.agent_solution.model_version,
    agentCostUsd: record.agent_solution.cost_usd,
  };
}
