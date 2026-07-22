# Risk register

Each risk has an identifier, a description, an impact level, and a mitigation.

## RSK-1: training contamination

- Description: models saw known benchmark problems during training. Results then measure memory, not capability.
- Impact: high. This invalidates the study.
- Mitigation: use only problems published after each model knowledge cutoff. Record publication dates and cutoffs. The collector rejects older problems.

## RSK-2: cheating on the platform

- Description: users submit AI-generated code in the human role. Leaderboards lose meaning.
- Impact: high for phases 2 and 3.
- Mitigation: editor telemetry flags suspect submissions. The competitive division requires monitored conditions or live events. A separate "centaur" division permits AI use and turns the problem into a feature.

## RSK-3: judge supply and quality

- Description: too few judges, or unreliable judges. Verdicts become noise.
- Impact: medium.
- Mitigation: judging is a role with progression and visible status. Gold pairs measure reliability. Votes are weighted by reliability. An LLM judge covers the cold start with provisional verdicts.

## RSK-4: blind protocol leaks

- Description: agent code has a recognizable style. Judges guess the source and vote with bias.
- Impact: medium.
- Mitigation: normalize both solutions before display. Record the judge guess and correct for bias in the analysis.

## RSK-5: agentic API cost

- Description: agentic runs consume many tokens. Costs grow fast with problem count and model count.
- Impact: medium.
- Mitigation: validate the pipeline at 30 problems before growth. Pre-compute agent solutions one time for each problem. Record cost for each run.

## RSK-6: content pipeline dries up

- Description: without fresh problems, humans memorize the bank and the contamination claim becomes false.
- Impact: medium.
- Mitigation: the collector runs as a recurring process, not one time. New Codeforces rounds and new GitHub issues supply content continuously.

## RSK-7: sandbox escape

- Description: generated code runs outside limits and damages the host.
- Impact: high, low probability with controls.
- Mitigation: all generated code runs in containers with time and memory limits. No network access from the sandbox by default.
