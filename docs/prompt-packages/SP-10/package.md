# SP-10 Deferred Cloud Sync Decision Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `Superpowers:verification-before-completion`
- `security-threat-model`

## Conditional Skills

- `security-best-practices` for future sync risk review

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- `Superpowers:verification-before-completion`

## Context Budget

- 1-3 skills open
- 1-2 repo docs
- only deferred sync decision docs

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-10/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Dependency Scope

Prerequisite files to read:
- `docs/run-logs/SP-09-output.md`
- all prior run logs in `docs/run-logs/`
- all phase memory notes in `docs/memory/phases/`
- `docs/memory/decisions/local-first-risk-model.md`
- `docs/memory/codebase/root/index.md`
- `docs/memory/codebase/api/index.md`

Editable scope roots:
- `docs/sync-decision/`
- `docs/no-upload-verification/`
- `docs/memory/phases/SP-10/index.md`
- `docs/memory/codebase/`
- `docs/run-logs/SP-10-output.md`

Future roots this phase may create only if explicitly approved:
- `api/lagoon_local/sync/`
- `web/src/sync/`
- `docs/memory/codebase/api/lagoon_local/sync/`
- `docs/memory/codebase/web/src/sync/`

Reference-only roots:
- `api/lagoon_local/`
- `web/src/`
- `scripts/`
- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/plans/markdown-presentation-rules.md`

Codebase memory mirrors to update:
- `docs/memory/codebase/docs/sync-decision/`
- `docs/memory/codebase/docs/no-upload-verification/`
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
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.

Goal: defer cloud sync from MVP and document the post-MVP decision gate.

Use only the mandatory skills listed above.
Keep optional skills closed unless a future sync security review trigger appears.
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

`docs/run-logs/SP-10-output.md`

