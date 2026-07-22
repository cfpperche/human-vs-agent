import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";

import type { MatchRecord } from "../src/generated/match-record.js";
import { summarizeMatch } from "../src/match.js";

const fixtureUrl = new URL("../../../data/fixtures/match_record.json", import.meta.url);
const record = JSON.parse(readFileSync(fixtureUrl, "utf-8")) as MatchRecord;

describe("schema bridge", () => {
  it("parses the shared fixture with the generated type", () => {
    expect(record.id).toBe("match-0001");
    expect(record.problem.source).toBe("codeforces");
    expect(record.metrics).toHaveLength(2);
  });

  it("summarizes a match record", () => {
    const summary = summarizeMatch(record);
    expect(summary.matchId).toBe("match-0001");
    expect(summary.humanRuntimeMs).toBe(15);
    expect(summary.agentModel).toBe("example-model-2026-05-01");
    expect(summary.agentCostUsd).toBeCloseTo(0.0125);
  });
});
