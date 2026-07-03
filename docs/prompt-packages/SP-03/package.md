# SP-03 Media + Transcription Package

## Model

`gpt-5.4`

## Mandatory Skills

- `caveman`
- `transcribe`
- `Superpowers:test-driven-development`
- `Superpowers:systematic-debugging`

## Conditional Skills

- `openai-docs` for model/API selection
- `OpenAI Developers:openai-api-troubleshooting` for API failures
- `Superpowers:verification-before-completion` before the gate

## Tools

- `rg`
- `Get-Content`
- `apply_patch`
- `git status`

## Plugins

- `OpenAI Developers:openai-api-troubleshooting`

## Context Budget

- 1-3 skills open
- 1-2 repo docs
- only media/transcription/chunking files

## Phase Plan

Load and execute:
- `docs/prompt-packages/SP-03/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.

## Dependency Scope

Prerequisite files to read:
- `docs/run-logs/SP-02-output.md`
- `docs/run-logs/SP-01-output.md`
- `docs/memory/phases/SP-02/index.md`
- `docs/memory/phases/SP-03/index.md`
- `docs/memory/codebase/web/src/media-import/index.md`
- `docs/memory/codebase/api/lagoon_local/storage.md`
- `docs/memory/codebase/scripts/index.md`

Editable scope roots:
- `api/lagoon_local/`
- `scripts/`
- `package.json`
- `docs/lessons/`
- `docs/memory/phases/SP-03/index.md`
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/scripts/`
- `docs/run-logs/SP-03-output.md`

Future roots this phase may create:
- `api/lagoon_local/media/`
- `api/lagoon_local/transcription/`
- `api/lagoon_local/jobs/`
- `api/lagoon_local/transcript_chunks/`
- `docs/memory/codebase/api/lagoon_local/media/`
- `docs/memory/codebase/api/lagoon_local/transcription/`
- `docs/memory/codebase/api/lagoon_local/jobs/`
- `docs/memory/codebase/api/lagoon_local/transcript_chunks/`

Reference-only roots:
- `web/src/media-import/`
- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/plans/markdown-presentation-rules.md`

Codebase memory mirrors to update:
- `docs/memory/codebase/api/lagoon_local/`
- `docs/memory/codebase/scripts/`
- `docs/memory/codebase/docs/lessons/`
## Memory Bank

Read first:
- docs/memory/index.md
- docs/memory/phases/SP-03/index.md
- relevant notes under docs/memory/codebase/

Update before finishing:
- docs/memory/phases/SP-03/index.md
- matching notes under docs/memory/codebase/ for generated or changed folders/components

## Prompt

You are the `SP-03` phase agent for Lagoon.

Load `docs/prompt-packages/SP-03/plan.md` before phase work.
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.

Goal: convert imported lecture media artifacts into timestamped, retry-safe transcripts plus semantic transcript chunks for later RAG.

Use only the mandatory skills listed above.
Keep optional skills closed unless API/model, pricing, or validation triggers appear.
Use memory notes before reading broad source.
Update memory notes for every generated or changed folder/component.
Use the Dependency Scope section for prerequisite files, editable roots, reference-only roots, future roots, and memory mirrors. Do not use stale paths outside that scope unless the current phase plan explains why.
Use durable local media artifact references from `SP-02`; browser object URLs are preview-only and must not drive backend processing.
Chunk media only for provider/file-limit reasons. Chunk transcripts for RAG after stitching, using sentence, pause, or segment boundaries.
Preserve absolute `startMs`/`endMs`, source segment IDs, and `mediaArtifactId` on every transcript chunk.
Diarization is optional and cost/provider-dependent; document whether skipped, deferred, or enabled.

Return:
- summary
- blockers
- contract changes
- provider/cost decision
- offline/free fallback status
- skill changes
- memory bank updates
- phase plan status
- tests run
- next gate

## Output File

Write your result to:

`docs/run-logs/SP-03-output.md`

