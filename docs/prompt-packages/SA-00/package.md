# SA-00 Skill Acquisition Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `skill-installer`
- `skill-creator`

## Conditional Skills

- `security-threat-model` for third-party skill audit
- `security-best-practices` for risk review of installed skill behavior

## Tools

- `git`
- `rg`
- `Get-Content`
- `apply_patch`
- `uv`

## Plugins

- none required

## Context Budget

- 1-2 skills open
- 1 repo doc
- no implementation source files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SA-00/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Dependency Scope

Prerequisite files to read:
- `docs/memory/index.md`
- `docs/memory/phases/SA-00/index.md`

Editable scope roots:
- `docs/plans/skill-acquisition-report.md`
- `docs/plans/phase-skill-map.md`
- `docs/memory/phases/SA-00/index.md`
- `docs/run-logs/SA-00-output.md`

Reference-only roots:
- `docs/plans/main-orchestration.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/plans/custom-skill-optimization.md`
- `docs/plans/markdown-presentation-rules.md`

Codebase memory mirrors to update:
- none unless the phase creates or changes repo-local docs/scripts
## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SA-00/index.md

Update before finishing:
- docs/memory/phases/SA-00/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SA-00` phase agent for Lagoon.

Load `docs/prompt-packages/SA-00/plan.md` before phase work.
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.

Goal: install vetted global skills, validate them, audit them for risk, and write the phase skill map inputs used by later phases.

Use only the mandatory skills listed above.
Keep optional skills closed unless a third-party security trigger appears.
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

`docs/run-logs/SA-00-output.md`

