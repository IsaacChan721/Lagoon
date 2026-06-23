# SP-02 Lecture Media Import Package

## Model

`gpt-5.4-mini`

## Mandatory Skills

- `caveman`
- `Superpowers:test-driven-development`
- `Superpowers:systematic-debugging`

## Conditional Skills

- `Browser:browser` for local UI verification when available
- `playwright` for scripted browser checks
- `web-design-guidelines` for import UI review

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Context Budget

- 1-2 skills open
- 1 repo doc
- only media-import-related files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-02/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Dependency Scope

Prerequisite files to read:
- `docs/run-logs/SP-01-output.md`
- `docs/memory/phases/SP-01/index.md`
- `docs/memory/codebase/web/index.md`
- `docs/memory/codebase/web/src/app/index.md`
- `docs/memory/codebase/api/lagoon_local/index.md`
- `docs/memory/codebase/api/lagoon_local/storage.md`
- `docs/memory/codebase/scripts/index.md`

Editable scope roots:
- `web/src/media-import/`
- `web/src/app/`
- `web/src/styles.css`
- `api/lagoon_local/`
- `scripts/`
- `package.json`
- `docs/lessons/`
- `docs/memory/phases/SP-02/index.md`
- `docs/memory/codebase/`
- `docs/run-logs/SP-02-output.md`

Reference-only roots:
- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/plans/markdown-presentation-rules.md`

Codebase memory mirrors to update:
- `docs/memory/codebase/web/src/media-import/`
- `docs/memory/codebase/web/src/app/`
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/scripts/`
- `docs/memory/codebase/docs/lessons/`
## Memory Bank

Read first:
- `docs/memory/index.md`
- `docs/memory/phases/SP-02/index.md`
- `docs/plans/markdown-presentation-rules.md`
- relevant notes under `docs/memory/codebase/`

Update before finishing:
- `docs/memory/phases/SP-02/index.md`
- matching notes under `docs/memory/codebase/` for generated or changed folders/components

## Prompt

You are the `SP-02` phase agent for Lagoon.

Load `docs/prompt-packages/SP-02/plan.md` before phase work.
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.

Goal: implement lecture media import with local preview, metadata extraction, local-only file handoff, and stable UI states.

Visual strategy: transcript is primary evidence; visuals are supporting evidence unless a future phase proves visual extraction reliable and affordable.

Use only mandatory skills listed above.
Keep optional skills closed unless browser or visual trigger appears.
Use memory notes before broad source reads.
Update memory notes for every generated or changed folder/component.

In scope:
- `web/`
- `api/lagoon_local/`
- `scripts/`
- `package.json`
- `web/package.json`
- `docs/memory/`
- `docs/run-logs/`
- `docs/lessons/`

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

Write result to:

`docs/run-logs/SP-02-output.md`

