# Worker Plan 03: Five-Section Notes

> [!IMPORTANT]
> Generate study notes from the transcript only, including transcripts too long for one model context.

## Contract

| Item | Requirement |
| --- | --- |
| Prerequisite | Plans 00-02 passed |
| Deliverable | Ollama-backed structured note generation and chunk/combine strategy |
| Required output | Summary, key concepts, specific details, definitions/terms, practical takeaways |
| Quality gate | [Readiness Audit](mvp-plan-readiness-audit.md) scores 10/10 before work; controller records all common quality checks afterward |

## Goal

Convert any completed transcript, including a long one, into validated study notes with all five required sections. Success means the tutor receives complete, transcript-derived notes rather than partial or invented material.

## Tasks

1. Define note data structures with exactly the five required sections.
2. Chunk long transcripts deterministically, request intermediate material through an Ollama client boundary, then combine it into one coherent note set.
3. Keep model prompting and response validation local; handle model errors as useful application errors.
4. Use a fake model to test output rules, long-input chunking, and failed-model behavior.
5. Display the five sections in the UI and update docs/run log.

## Acceptance Criteria

- [ ] A multi-chunk synthetic transcript produces all five named sections.
- [ ] Each section contains transcript-derived content and is structurally validated before display/persistence.
- [ ] Tests demonstrate chunking rather than a single unbounded prompt for long input.
- [ ] Model failure becomes a useful failed state, not partial success or invented notes.
- [ ] The actual test command, code map, and completion evidence are documented.

## Controller Verification

Run the fake-model suite with a multi-chunk fixture, inspect the five rendered sections, force one model error, and apply every item in the controller's Common Independent Quality Gate. Do not assign tutor work until notes are complete, validated, and the quality-gate record is entirely pass.

## Outcome and Next Step

| Verification result | Report to user | Next step |
| --- | --- | --- |
| Pass | “Notes passed” with multi-chunk test result and the five-section inspection. | Commit/checkpoint; assign [Plan 04](04-tutor-plan.md). |
| Fail | “Notes failed” with the missing section, chunking, validation, or error-state evidence. | Repair Plan 03 only; re-run long-input and model-failure checks. |
| Blocked | “Notes blocked” with the unavailable local Ollama/model prerequisite. | Resolve the prerequisite with the human; do not build tutor chat. |

## Stop Point

No editing, exports, flashcards, quizzes, cloud model, or external learning material.
