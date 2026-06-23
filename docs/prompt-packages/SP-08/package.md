# SP-08 Post-MVP Improvement Proposals Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `skill-creator`
- `security-threat-model`
- `Superpowers:verification-before-completion`

## Conditional Skills

- `security-best-practices` for future skill proposal review
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

## Dependency Scope

Prerequisite files to read:
- `docs/run-logs/SP-07-output.md`
- `docs/run-logs/SP-06-output.md`
- `docs/run-logs/SP-05-output.md`
- `docs/run-logs/CRIT-01-output.md`
- `docs/memory/phases/SP-07/index.md`
- `docs/memory/phases/SP-06/index.md`
- `docs/memory/phases/SP-05/index.md`
- `docs/memory/phases/CRIT-01/index.md`
- `docs/memory/decisions/index.md`

Editable scope roots:
- `docs/proposals/`
- `docs/memory/phases/SP-08/index.md`
- `docs/memory/codebase/`
- `docs/run-logs/SP-08-output.md`
- `api/lagoon_local/`
- `web/src/`
- `scripts/`

Future roots this phase may create:
- `api/lagoon_local/proposals/`
- `web/src/proposals/`
- `docs/memory/codebase/docs/proposals/`
- `docs/memory/codebase/api/lagoon_local/proposals/`
- `docs/memory/codebase/web/src/proposals/`

Reference-only roots:
- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/plans/custom-skill-optimization.md`
- `docs/plans/markdown-presentation-rules.md`

Codebase memory mirrors to update:
- `docs/memory/codebase/`
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
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.

Goal: create manual post-MVP improvement proposals that require user approval and eval pass before implementation.

Use only the mandatory skills listed above.
Keep optional skills closed unless a security review trigger appears.
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

`docs/run-logs/SP-08-output.md`

