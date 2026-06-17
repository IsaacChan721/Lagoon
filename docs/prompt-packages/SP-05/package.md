# SP-05 Local Memory + Retrieval Package

## Model

`gpt-5.4`

## Mandatory Skills

- `caveman`
- `Superpowers:test-driven-development`
- `Superpowers:systematic-debugging`

## Conditional Skills

- `jupyter-notebook` for eval experiments
- `Superpowers:verification-before-completion` before the gate

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- none unless the phase needs UI/browser evidence

## Context Budget

- 1-3 skills open
- 1-2 repo docs
- only retrieval/memory files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-05/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-05/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-05/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-05` phase agent for Lagoon.

Load `docs/prompt-packages/SP-05/plan.md` before phase work.
Execute only that phase plan.

Goal: build simple local lecture memory and text retrieval after provenance exists.

Use only the mandatory skills listed above.
Keep optional skills closed unless a security or eval trigger appears.
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

`docs/run-logs/SP-05-output.md`



