# SP-06 Transcript-Grounded Summaries Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `openai-docs`
- `Superpowers:systematic-debugging`

## Conditional Skills

- `Browser:browser` for summary UI checks
- `security-best-practices` for imported-content trust and leakage review
- `Superpowers:verification-before-completion` before the gate

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- `Browser:browser`

## Context Budget

- 1-2 skills open
- 1 repo doc
- only summary/local-evidence files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-06/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Dependency Scope

Prerequisite files to read:
- `docs/run-logs/SP-05-output.md`
- `docs/run-logs/SP-04-output.md`
- `docs/run-logs/CRIT-01-output.md`
- `docs/run-logs/SP-03-output.md`
- `docs/memory/phases/SP-05/index.md`
- `docs/memory/phases/SP-04/index.md`
- `docs/memory/phases/CRIT-01/index.md`
- `docs/memory/phases/SP-03/index.md`
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/api/lagoon_local/transcript_chunks/`
- `docs/memory/codebase/api/lagoon_local/retrieval/`

Editable scope roots:
- `api/lagoon_local/`
- `web/src/`
- `scripts/`
- `docs/lessons/`
- `docs/memory/phases/SP-06/index.md`
- `docs/memory/codebase/`
- `docs/run-logs/SP-06-output.md`

Future roots this phase may create:
- `api/lagoon_local/summaries/`
- `api/lagoon_local/evidence/`
- `web/src/summaries/`
- `docs/memory/codebase/api/lagoon_local/summaries/`
- `docs/memory/codebase/api/lagoon_local/evidence/`
- `docs/memory/codebase/web/src/summaries/`

Reference-only roots:
- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/plans/markdown-presentation-rules.md`

Codebase memory mirrors to update:
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/web/src/`
- `docs/memory/codebase/scripts/`
## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-06/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-06/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-06` phase agent for Lagoon.

Load `docs/prompt-packages/SP-06/plan.md` before phase work.
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.

Goal: produce grounded lecture summaries with transcript chunk, transcript segment, visual, and local artifact citations only.

Use only the mandatory skills listed above.
Keep optional skills closed unless a UI or imported-content safety trigger appears.
Use memory notes before reading broad source.
Update memory notes for every generated or changed folder/component.
Use the Dependency Scope section for prerequisite files, editable roots, reference-only roots, future roots, and memory mirrors. Do not use stale paths outside that scope unless the current phase plan explains why.
Use SP-03 transcript chunks and SP-05 retrieval outputs as primary summary evidence.
Every factual summary claim must cite source IDs and absolute time ranges.

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

`docs/run-logs/SP-06-output.md`

