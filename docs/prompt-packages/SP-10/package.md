# SP-10 Optional Cloud Sync Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `Supabase:supabase`
- `security-threat-model`

## Conditional Skills

- `Supabase:supabase-postgres-best-practices` for schema/RLS
- `security-best-practices` for crypto/auth review
- `Superpowers:verification-before-completion` before the gate

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- `Supabase:supabase`

## Context Budget

- 1-3 skills open
- 1-2 repo docs
- only sync files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-10/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-10/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-10/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-10` phase agent for Lagoon.

Load `docs/prompt-packages/SP-10/plan.md` before phase work.
Execute only that phase plan.

Goal: add opt-in encrypted cloud sync after the local MVP is stable.

Use only the mandatory skills listed above.
Keep optional skills closed unless a database/security trigger appears.
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

`docs/run-logs/SP-10-output.md`



