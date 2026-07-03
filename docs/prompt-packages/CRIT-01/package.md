# CRIT-01 Provenance Gate Package

## Model

`gpt-5.5`

## Mandatory Skills

- `caveman`
- `security-threat-model`
- `Superpowers:test-driven-development`

## Conditional Skills

- `security-best-practices`
- `Superpowers:verification-before-completion`

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- none unless the phase needs browser/UI evidence

## Context Budget

- 1-2 skills open
- 1 repo doc
- only provenance-related files

## Phase Plan

Load and execute:
- `docs/prompt-packages/CRIT-01/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Dependency Scope

Prerequisite files to read:
- `docs/run-logs/SP-03-output.md`
- `docs/run-logs/SP-02-output.md`
- `docs/memory/phases/SP-03/index.md`
- `docs/memory/phases/SP-02/index.md`
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/api/lagoon_local/transcription/`
- `docs/memory/codebase/api/lagoon_local/transcript_chunks/`
- `docs/memory/codebase/web/src/media-import/index.md`

Editable scope roots:
- `api/lagoon_local/`
- `scripts/`
- `docs/memory/phases/CRIT-01/index.md`
- `docs/memory/codebase/api/lagoon_local/`
- `docs/run-logs/CRIT-01-output.md`
- `docs/lessons/`

Future roots this phase may create:
- `api/lagoon_local/provenance/`
- `docs/memory/codebase/api/lagoon_local/provenance/`

Reference-only roots:
- `web/src/media-import/`
- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/plans/markdown-presentation-rules.md`

Codebase memory mirrors to update:
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/scripts/`
## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/CRIT-01/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/CRIT-01/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `CRIT-01` phase agent for Lagoon.

Load `docs/prompt-packages/CRIT-01/plan.md` before phase work.
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.

Goal: add the provenance gate so summaries, retrieval, and tutoring never lose source traceability.

Use only the mandatory skills listed above.
Keep optional skills closed unless a security or validation trigger appears.
Use memory notes before reading broad source.
Update memory notes for every generated or changed folder/component.
Use the Dependency Scope section for prerequisite files, editable roots, reference-only roots, future roots, and memory mirrors. Do not use stale paths outside that scope unless the current phase plan explains why.
Validate that transcript chunks preserve source transcript segments, `mediaArtifactId`, absolute `startMs`/`endMs`, and durable artifact references.
Block downstream phases if evidence depends on browser object URLs or provider-relative timestamps without absolute lecture offsets.

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

`docs/run-logs/CRIT-01-output.md`

