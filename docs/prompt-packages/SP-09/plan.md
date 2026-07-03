# SP-09 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Harden, package, and prepare Lagoon local MVP for release.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-09/index.md`
- app, media, transcript chunk, retrieval, security, tutor, and storage memory notes

## In Scope

- Security and privacy hardening.
- Media/transcript/chunk/embedding leak review.
- Packaging/install path.
- Regression verification.
- Release notes and rollback guidance.
- Observability/error reporting plan.

## Out Of Scope

- No new major features.
- No optional cloud sync.
- No broad redesign.

## Execution Steps

1. Read all phase gate outputs through memory.
2. Run narrow then broad checks.
3. Review secrets, provider keys, raw media, extracted audio, transcripts, transcript chunks, embeddings, local files, logs, temp paths, and unsafe IO.
4. Validate package/install path.
5. Document rollback and known risks.
6. Produce release readiness decision.

## Acceptance Criteria

- MVP checks pass or blockers are explicit.
- No known secret, raw media, extracted audio, transcript, transcript chunk, embedding, or tutor trace leak path remains.
- Install/run path is documented.
- Release decision is clear.

## Definition Of Done

- Test status, docs status, security status, and packaging status are reported.
- Rollback notes exist.
- Memory and handoff output are updated.

## Verification

- Run full available test/build suite.
- Run UI verification where app exists.
- Run security scan/checks available in repo.
- Run `git status --short`.

## Troubleshooting

- If broad checks fail, isolate first failing subsystem.
- If packaging fails, verify environment assumptions before changing code.
- If media/transcript/chunk privacy risk is high, mark blocked instead of shipping.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite release context first, then build toward hardening, packaging, regression checks, and rollback.

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

- Security and privacy hardening notes.
- Packaging/install path documentation.
- Regression verification report.
- Release notes, rollback guidance, and observability/error-reporting plan.

### Lesson 1: What Hardening Means

- Prerequisites: none.
- Explain: hardening reduces leaks, unsafe defaults, brittle errors, and release risk before packaging.
- Coding example: show checks for secrets, local data ignores, raw media/transcript/chunk paths, and disabled cloud upload defaults.
- Theory Q/A: Why avoid new major features here? Release phase should stabilize existing MVP, not add new uncertainty.
- Key takeaways: hardening is risk reduction, not feature growth.

### Lesson 2: Packaging And Install Path

- Prerequisites: understand hardening goal.
- Explain: packaging documents how a user installs, runs, and recovers Lagoon locally.
- Coding example: show commands from `package.json` and any app startup script, then explain expected output.
- Theory Q/A: Why verify environment assumptions first? Packaging bugs often come from missing runtime, path, or permission assumptions.
- Key takeaways: install docs should be executable by a beginner.

### Lesson 3: Regression Verification

- Prerequisites: understand install path.
- Explain: regression checks prove earlier phase contracts still hold.
- Coding example: run full test/build suite, then record exact failures by subsystem.
- Theory Q/A: Why isolate first failing subsystem? It avoids broad speculative fixes.
- Key takeaways: release readiness depends on known test status.

### Lesson 4: Rollback And Observability

- Prerequisites: understand regression status.
- Explain: rollback says how to recover; observability says how user/developer notices failure.
- Coding example: show a release note section with `known risks`, `rollback`, and `logs`.
- Theory Q/A: When should release be blocked? When privacy, data loss, install, or core workflow risk is unresolved.
- Key takeaways: readiness is explicit: ship, conditional, or blocked.

## Memory Updates

Update `docs/memory/phases/SP-09/index.md` and codebase notes for release status, package path, media/transcript privacy risks, and rollback.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-09>`.
3. Run `git commit -m "SP-09: complete phase"`.
4. Run `git push`.

Commit only scoped SP-09 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-09-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
