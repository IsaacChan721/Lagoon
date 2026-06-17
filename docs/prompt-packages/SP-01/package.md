# SP-01 Local App Foundation Package

## Model

`gpt-5.4`

## Mandatory Skills

- `caveman`
- `Superpowers:test-driven-development`
- `react-best-practices`
- `composition-patterns`

## Conditional Skills

- `web-design-guidelines` for UI review
- `Browser:browser` for local app verification
- `playwright` for scripted E2E
- `security-best-practices` for secure defaults

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- `Browser:browser`
- `OpenAI Developers:openai-api-troubleshooting` only if an API decision blocks progress

## Context Budget

- 1-3 skills open
- 1-2 repo docs
- only files in `web/` and `api/` if present, otherwise scaffold targets only

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-01/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-01/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-01/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-01` phase agent for Lagoon.

Load `docs/prompt-packages/SP-01/plan.md` before phase work.
Execute only that phase plan.

Goal: scaffold the local web app foundation, local artifact boundary, SQLite metadata, and the first user-facing shell.

Use only the mandatory skills listed above.
Keep optional skills closed unless a UI or security trigger appears.
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

`docs/run-logs/SP-01-output.md`



