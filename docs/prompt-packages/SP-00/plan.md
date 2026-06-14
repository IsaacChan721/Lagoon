# SP-00 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Lock Lagoon MVP scope, local-first risk model, repo boundaries, and phase gates.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/plans/phase-skill-map.md`
- `docs/plans/context-and-skill-optimization.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-00/index.md`

## In Scope

- Define MVP and non-goals.
- Define privacy/security assumptions.
- Define repo bootstrap decisions.
- Define gate criteria for `SP-01`.

## Out Of Scope

- No app scaffolding.
- No UI implementation.
- No provider integration.

## Execution Steps

1. Read package, this plan, orchestration docs, and memory.
2. Lock MVP user journey and first implementation slice.
3. Identify local-first storage, privacy, and threat boundaries.
4. Record key architectural decisions and alternatives.
5. Define `SP-01` readiness gate.
6. Write handoff with blockers and decisions.

## Acceptance Criteria

- MVP scope is clear and testable.
- Local-first security assumptions are explicit.
- Repo boundaries and first folders are chosen.
- `SP-01` can start without product ambiguity.

## Definition Of Done

- Decisions are centralized in docs or memory.
- Phase gate criteria are visible.
- No implementation files changed.
- Handoff output is written.

## Verification

- Run `rg -n "MVP|local-first|gate|SP-01|threat" docs/plans docs/memory`.
- Run `git status --short`.

## Troubleshooting

- If scope expands, split into MVP and later backlog.
- If security choice is unclear, prefer local-only default and record open question.
- If phase boundary overlaps, keep earliest phase minimal and move extra work later.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite product context first, then build toward repo boundaries and gates.

### Created In This Phase

- MVP scope and non-goals in `docs/memory/phases/SP-00/index.md`.
- Decision notes under `docs/memory/decisions/`.
- Codebase mirror notes for docs touched by planning.
- Handoff report in `docs/run-logs/SP-00-output.md`.

### Lesson 1: What Lagoon Is Building First

- Prerequisites: none.
- Explain: Lagoon starts as a local-first lecture assistant for one user and one device.
- Coding example: show a markdown checklist for MVP scope, then explain how each checked item becomes a later phase gate.
- Theory Q/A: Why start with scope before code? Code structure should protect the first user journey and exclude tempting extras.
- Key takeaways: MVP scope is a safety rail; non-goals are as important as goals.

### Lesson 2: Local-First Risk Model

- Prerequisites: understand MVP scope.
- Explain: lecture media, transcripts, notes, embeddings, and keys are sensitive local assets.
- Coding example: show an example `.gitignore` rule such as `*.db` or `local-data/` and explain what leak it prevents.
- Theory Q/A: Why deny cloud upload by default? User lecture content should not leave the device without explicit consent.
- Key takeaways: privacy defaults shape storage, logs, tests, and future provider calls.

### Lesson 3: Phase Gates And Repo Boundaries

- Prerequisites: understand local-first risk.
- Explain: `SP-01` may only create foundation code after scope and security defaults are accepted.
- Coding example: trace `SP-01` gate terms with `rg -n "SP-01|gate|local-first" docs`.
- Theory Q/A: What makes a good phase gate? It is testable, narrow, and blocks ambiguous work.
- Key takeaways: boundaries prevent feature creep; gates make handoffs teachable.

## Memory Updates

Update `docs/memory/phases/SP-00/index.md` with MVP decisions, risks, phase gate, and unresolved blockers.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-00>`.
3. Run `git commit -m "SP-00: complete phase"`.
4. Run `git push`.

Commit only scoped SP-00 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-00-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
