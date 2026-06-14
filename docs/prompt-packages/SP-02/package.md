# SP-02 Video + Audio Capture Package

## Model

`gpt-5.4-mini`

## Mandatory Skills

- `caveman`
- `Superpowers:test-driven-development`
- `Superpowers:systematic-debugging`
- `Browser:browser`

## Conditional Skills

- `playwright` for scripted browser checks
- `screenshot` for media/permission states
- `web-design-guidelines` for capture UI review

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
- only capture-related files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-02/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-02/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-02/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-02` phase agent for Lagoon.

Load `docs/prompt-packages/SP-02/plan.md` before phase work.
Execute only that phase plan.

Goal: implement browser-based video + audio capture with chunked encrypted persistence and stable UI states.

Use only the mandatory skills listed above.
Keep optional skills closed unless a browser or visual trigger appears.
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

`docs/run-logs/SP-02-output.md`



