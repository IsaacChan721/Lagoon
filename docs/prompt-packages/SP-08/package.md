# SP-08 Gated Improvement Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `skill-creator`
- `security-threat-model`
- `Superpowers:verification-before-completion`

## Conditional Skills

- `security-best-practices` for proposal sandboxing
- `Superpowers:subagent-driven-development` during execution

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- none unless a verification UI or external integration appears

## Context Budget

- 1-3 skills open
- 1-2 repo docs
- only proposal/governance files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-08/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-08/index.md
- docs/memory/decisions/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-08/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-08` phase agent for Lagoon.

Load `docs/prompt-packages/SP-08/plan.md` before phase work.
Execute only that phase plan.

Goal: create gated skill/rubric proposals that require human approval and eval pass before activation.

Use only the mandatory skills listed above.
Keep optional skills closed unless a security or execution trigger appears.
Use memory notes before reading broad source.
Update memory notes for every generated or changed folder/component.
Use only these files in scope:
- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/plans/custom-skill-optimization.md`

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

`docs/run-logs/SP-08-output.md`



