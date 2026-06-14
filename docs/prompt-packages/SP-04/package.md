# SP-04 Video Understanding Package

## Model

`gpt-5.4`

## Mandatory Skills

- `caveman`
- `Superpowers:systematic-debugging`
- `playwright`

## Conditional Skills

- `openai-docs` for vision/API decisions
- `screenshot` for frame/OCR QA
- `imagegen` only for generated visual fixtures/tests

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- `Browser:browser` only if visual inspection is needed

## Context Budget

- 1-2 skills open
- 1 repo doc
- only video understanding files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-04/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-04/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-04/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-04` phase agent for Lagoon.

Load `docs/prompt-packages/SP-04/plan.md` before phase work.
Execute only that phase plan.

Goal: extract frame evidence, OCR, and optional vision captions from lecture video.

Use only the mandatory skills listed above.
Keep optional skills closed unless a vision or visual QA trigger appears.
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

`docs/run-logs/SP-04-output.md`



