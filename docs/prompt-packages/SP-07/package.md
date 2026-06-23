# SP-07 Tutor Practice Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `Superpowers:test-driven-development`
- `Superpowers:systematic-debugging`

## Conditional Skills

- `OpenAI Developers:openai-api-troubleshooting` only for explicit provider failures
- `speech` only for spoken tutor output

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
- only tutor files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-07/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Dependency Scope

Prerequisite files to read:
- `docs/run-logs/SP-06-output.md`
- `docs/run-logs/SP-05-output.md`
- `docs/run-logs/CRIT-01-output.md`
- `docs/run-logs/SP-03-output.md`
- `docs/memory/phases/SP-06/index.md`
- `docs/memory/phases/SP-05/index.md`
- `docs/memory/phases/CRIT-01/index.md`
- `docs/memory/codebase/api/lagoon_local/`

Editable scope roots:
- `api/lagoon_local/`
- `web/src/`
- `scripts/`
- `docs/lessons/`
- `docs/memory/phases/SP-07/index.md`
- `docs/memory/codebase/`
- `docs/run-logs/SP-07-output.md`

Future roots this phase may create:
- `api/lagoon_local/tutor/`
- `web/src/tutor/`
- `docs/memory/codebase/api/lagoon_local/tutor/`
- `docs/memory/codebase/web/src/tutor/`

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
- docs/memory/phases/SP-07/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-07/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-07` phase agent for Lagoon.

Load `docs/prompt-packages/SP-07/plan.md` before phase work.
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.

Goal: build simple selected-lecture tutor practice with evidence-backed feedback.

Use only the mandatory skills listed above.
Keep optional skills closed unless an explicit API or speech trigger appears.
Use memory notes before reading broad source.
Update memory notes for every generated or changed folder/component.
Use the Dependency Scope section for prerequisite files, editable roots, reference-only roots, future roots, and memory mirrors. Do not use stale paths outside that scope unless the current phase plan explains why.

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

`docs/run-logs/SP-07-output.md`

