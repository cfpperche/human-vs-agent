# Documentation standard

## Purpose

This document defines the writing standard for all documents in this project. The standard is ASD-STE100, Simplified Technical English (STE). All documents in this repository must obey this standard.

## Scope

The standard applies to:

- All files in `/docs`.
- `README.md` and the agent instruction files.
- All future user-facing documentation.

The standard does not apply to code comments or commit messages. But keep those short and clear.

## Note on the specification

ASD publishes the full ASD-STE100 specification. The specification is free, but ASD controls its distribution. This document codifies the subset of rules that this project applies. When a rule here and the official specification disagree, the official specification is correct.

## Writing rules

### Sentences

- Use the active voice.
- Keep procedural sentences at 20 words or fewer.
- Keep descriptive sentences at 25 words or fewer.
- Write one instruction in each procedural sentence.
- Start a safety instruction with the condition, then the instruction.

### Paragraphs

- Keep paragraphs at 6 sentences or fewer.
- Give each paragraph one topic.
- Use vertical lists for sequences of items or steps.

### Words

- Use one word for one meaning. Example: use "start" always, not "start", "begin", and "initiate" together.
- Use the simplest word that is correct.
- Do not use gerunds in procedural text. Write "Install the tool", not "Installing the tool".
- Do not use slang or idioms.
- Use "do not" and "must". Do not use "should" or "might" in requirements.

### Verb forms in requirements

- "must": a mandatory requirement.
- "can": a capability or a possibility.
- Do not use "shall", "should", "may", or "will" in requirements.

## Technical names

STE permits technical names and technical verbs that the project defines. This project defines these technical names:

- benchmark, sandbox, leaderboard, runner, collector
- agent, model, prompt, token
- rating, judge, rubric, gold pair
- repository, commit, pull request, issue
- pass rate, runtime, wall-clock time

Add new technical names to this list when the project needs them.

## Review procedure

Before you merge a document, do these checks:

1. Find sentences with more than 25 words. Split them.
2. Find passive voice. Change it to active voice.
3. Find gerunds in procedures. Change them to imperative verbs.
4. Find synonyms for one concept. Select one word and use it in all locations.
5. Find "should", "shall", "may", or "will" in requirements. Replace them with "must" or "can".
