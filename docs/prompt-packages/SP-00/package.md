# SP-00 Product, Risk, Repo Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `Superpowers:brainstorming`
- `Superpowers:writing-plans`

## Conditional Skills

- `security-threat-model` when defining trust boundaries or threat paths
- `security-best-practices` when choosing secure defaults or APIs
- `openai-docs` when a provider/model decision is needed

## Tools

- `rg`
- `git status`
- `Get-Content`
- `apply_patch` for docs only

## Plugins

- `Browser:browser` only if a visual artifact or UI choice needs inspection
- `OpenAI Developers:openai-api-troubleshooting` only if API/key setup appears

## Context Budget

- 1-2 skills open
- 1-2 repo docs
- no implementation source files unless a contract references them

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-00/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-00/index.md
- docs/memory/decisions/index.md

Update before finishing:
- docs/memory/phases/SP-00/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-00` phase agent for Lagoon.

Load `docs/prompt-packages/SP-00/plan.md` before phase work.
Execute only that phase plan.

Goal: lock product scope, threat model, phase boundaries, and repo bootstrap decisions for a local-first lecture app.

Use only the mandatory skills listed above.
Keep optional skills closed unless a concrete security or provider trigger appears.
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

`docs/run-logs/SP-00-output.md`



