# SP-07 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Build tutoring agent over selected Lagoon lecture memories.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-07/index.md`
- RAG, summary, and provenance memory notes

## In Scope

- Selected-lecture tutoring boundary.
- Quiz mode.
- Hands-on question mode.
- End-to-end challenge mode.
- Grading and feedback policy.

## Out Of Scope

- No autonomous skill installation.
- No cloud sync.
- No unsupported citations.

## Execution Steps

1. Confirm RAG retrieval and citation contracts.
2. Define tutor input: selected lectures, mode, difficulty.
3. Implement tutor flow using retrieval boundary.
4. Add grading rubric and answer feedback.
5. Add tests for lecture boundary and citation behavior.
6. Verify challenge modes.

## Acceptance Criteria

- Tutor uses only selected lectures unless user allows sources.
- Quiz, hands-on, and end-to-end modes work.
- Feedback cites memory or source evidence.
- Unknown answers are admitted, not fabricated.

## Definition Of Done

- Tutor tests pass.
- Boundary violations are covered.
- Memory notes explain tutor policy.

## Verification

- Run tutor unit/integration tests.
- Test selected lecture filtering manually or by fixture.
- Run `git status --short`.

## Troubleshooting

- If tutor hallucinates, tighten retrieval-only answer policy.
- If grading is vague, add rubric examples.
- If context is too large, summarize lecture memory before retrieval prompt.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite tutor context first, then build toward modes, retrieval grounding, grading, and feedback.

### Created In This Phase

- Tutor boundary for selected lectures.
- Quiz, hands-on question, and end-to-end challenge modes.
- Grading rubric and feedback policy.
- Tests for citation use, unknown answers, and boundary violations.

### Lesson 1: What Tutor Mode Does

- Prerequisites: none.
- Explain: tutor helps learner practice selected lecture content using grounded evidence.
- Coding example: show a tutor request with `lectureIds`, `mode`, `question`, and `retrievedEvidence`.
- Theory Q/A: Why restrict to selected lectures? Learner expects answers from current class context, not unrelated memory.
- Key takeaways: tutor is scoped help, not open-ended chatbot.

### Lesson 2: Practice Modes

- Prerequisites: understand tutor request.
- Explain: quiz checks recall, hands-on mode guides applied work, challenge mode combines concepts.
- Coding example: show a discriminated union for `TutorMode = "quiz" | "hands_on" | "challenge"`.
- Theory Q/A: Why separate modes in code? Each mode needs different prompts, rubrics, and UI states.
- Key takeaways: mode shape controls user experience and test coverage.

### Lesson 3: Grounded Feedback

- Prerequisites: understand practice modes.
- Explain: feedback cites retrieved evidence or admits missing information.
- Coding example: show a response with `answer`, `feedback`, `citationIds`, and `unknownReason`.
- Theory Q/A: What if retrieval lacks answer? Tutor should say it cannot answer from selected material.
- Key takeaways: honest uncertainty beats fabricated confidence.

### Lesson 4: Grading Rubrics

- Prerequisites: understand grounded feedback.
- Explain: rubrics turn vague feedback into consistent beginner-friendly coaching.
- Coding example: show rubric criteria with `conceptAccuracy`, `evidenceUse`, and `nextStep`.
- Theory Q/A: Why add examples to rubrics? Examples make grading behavior predictable.
- Key takeaways: grading should teach what to improve, not only mark wrong.

## Memory Updates

Update `docs/memory/phases/SP-07/index.md` and codebase notes for tutor contract, modes, grading, and boundary rules.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-07>`.
3. Run `git commit -m "SP-07: complete phase"`.
4. Run `git push`.

Commit only scoped SP-07 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-07-output.md` with summary, blockers, contract changes, skill changes, memory updates, tests run, and next gate.
