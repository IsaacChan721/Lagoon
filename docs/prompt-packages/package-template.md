# {PHASE_NAME} Package

## Use

Paste this package into a fresh convo for `{PHASE_ID}`.

## Model

`{MODEL}`

## Mandatory Skills

- `caveman`
{MANDATORY_SKILLS}

## Conditional Skills

{CONDITIONAL_SKILLS}

## Tools

{TOOLS}

## Plugins

{PLUGINS}

## Context Budget

{CONTEXT_BUDGET}

## Phase Plan

Load and execute:
- `docs/prompt-packages/{PHASE_ID}/plan.md`

Execution style:
- Execute this plan in `caveman full` unless clarity or safety requires temporary normal prose.
- Keep the phase simple: MVP slice only, beginner-readable code/docs, no extra logic unless required by acceptance criteria, safety, or verification.
- All new or updated Markdown must follow `docs/plans/markdown-presentation-rules.md` so GitHub renders it as learner-friendly docs, not plain text.
- Put marginal improvements in handoff next steps instead of implementing them during the phase.
- Final output must state whether the phase plan was followed or changed.
- If changed, explain the contract change and update memory.
- After verification and handoff, run `git add <files changed for {PHASE_ID}>`, `git commit -m "{PHASE_ID}: complete phase"`, and `git push` so each phase ships separately.

## Dependency Scope

Prerequisite files to read:
- `{PREREQUISITE_RUN_LOGS_AND_MEMORY}`

Editable scope roots:
- `{EDITABLE_SCOPE_ROOTS}`

Future roots this phase may create:
- `{FUTURE_ROOTS_OR_NONE}`

Reference-only roots:
- `{REFERENCE_ONLY_ROOTS}`

Codebase memory mirrors to update:
- `{MEMORY_MIRRORS}`

## Memory Bank

Read first:
- `docs/memory/index.md`
- `docs/memory/phases/{PHASE_ID}/index.md`
- `docs/plans/markdown-presentation-rules.md`

Update before finishing:
- `docs/memory/phases/{PHASE_ID}/index.md`
- matching notes under `docs/memory/codebase/` for generated or changed folders/components

## Prompt

You are the `{PHASE_ID}` phase agent for Lagoon.

Load `docs/prompt-packages/{PHASE_ID}/plan.md` before phase work.
Before writing or updating Markdown, read and follow `docs/plans/markdown-presentation-rules.md`.
Execute only that phase plan.
Load only the mandatory skills listed above.
Keep optional skills closed until a concrete trigger appears.
Use only the phase contract and Dependency Scope.
Use memory notes before reading broad source.
Update memory notes for every generated or changed folder/component.
Write no broad refactors.
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

`{OUTPUT_FILE}`
