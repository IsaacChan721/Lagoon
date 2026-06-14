# CRIT-01 Provenance Gate Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `security-threat-model`
- `Superpowers:test-driven-development`

## Conditional Skills

- `security-best-practices`
- `Superpowers:verification-before-completion`

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- none unless the phase needs browser/UI evidence

## Context Budget

- 1-2 skills open
- 1 repo doc
- only provenance-related files

## Phase Plan

Load and execute:
- `docs/prompt-packages/CRIT-01/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/CRIT-01/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/CRIT-01/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `CRIT-01` phase agent for Lagoon.

Load `docs/prompt-packages/CRIT-01/plan.md` before phase work.
Execute only that phase plan.

Goal: add the provenance gate so summaries, retrieval, and tutoring never lose source traceability.

Use only the mandatory skills listed above.
Keep optional skills closed unless a security or validation trigger appears.
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

`docs/run-logs/CRIT-01-output.md`



