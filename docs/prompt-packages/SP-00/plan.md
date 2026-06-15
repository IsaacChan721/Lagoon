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

### Lesson Depth Standard

Every lesson below must be written and taught as a 60-90 minute beginner module, not a quick concept note. Use the lesson bullets as topic seeds, then expand them with this structure:

1. Zero-prerequisite setup, 5-10 minutes: define every term used in the lesson, explain why the learner should care, and name the files or planned files they will touch.
2. File map, 10-15 minutes: list each relevant file, folder, command, schema, component, or artifact. For future files, mark them `planned`. Explain what each one owns and what it must not own.
3. Line-by-line code reading, 15-25 minutes: walk through the smallest real code sample available. If implementation does not exist yet, write planned pseudocode and later replace it with real code. Explain each line or block in beginner language, including imports, data shapes, function inputs, outputs, errors, and side effects.
4. Guided hands-on exercise, 15-25 minutes: have the learner run a command, inspect output, trace data through one function, update a harmless fixture, or write a tiny example. Include expected output and what to do if it differs.
5. Debugging or design exercise, 10-20 minutes: give one realistic failure, ask the learner to diagnose it, then provide the answer and the reasoning path.
6. Theory questions and answers, 10-15 minutes: include at least five Q/A pairs that connect the hands-on work to architecture, privacy, security, testing, or user experience.
7. Checkpoint, 5-10 minutes: include a small task the learner can complete without help, plus acceptance criteria.
8. Key takeaways, 5 minutes: list what the learner should remember before moving to the next lesson.

Each lesson must include concrete code or command examples. Prefer real snippets from this codebase once the phase exists. Avoid abstract-only examples. When a lesson covers safety, privacy, auth, encryption, destructive actions, or external providers, spell out the risk clearly and then return to concise style.
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
