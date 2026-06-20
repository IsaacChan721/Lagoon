# SP-03 Media + Transcription Package

## Model

`gpt-5.4`

## Mandatory Skills

- `caveman`
- `transcribe`
- `Superpowers:test-driven-development`
- `Superpowers:systematic-debugging`

## Conditional Skills

- `openai-docs` for model/API selection
- `OpenAI Developers:openai-api-troubleshooting` for API failures
- `Superpowers:verification-before-completion` before the gate

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- `OpenAI Developers:openai-api-troubleshooting`

## Context Budget

- 1-3 skills open
- 1-2 repo docs
- only media/transcription files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-03/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-03/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-03/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-03` phase agent for Lagoon.

Load `docs/prompt-packages/SP-03/plan.md` before phase work.
Execute only that phase plan.

Goal: convert imported media artifacts into timestamped, retry-safe, diarized transcripts.

Use only the mandatory skills listed above.
Keep optional skills closed unless API/model or validation triggers appear.
Use memory notes before reading broad source.
Update memory notes for every generated or changed folder/component.
Use only these files in scope:
- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`

Return:
- summary
- blockers
- contract changes
- skill changes
- memory bank updates
- phase plan status
- tests run
- next gate

## Output File

Write your result to:

`docs/run-logs/SP-03-output.md`



