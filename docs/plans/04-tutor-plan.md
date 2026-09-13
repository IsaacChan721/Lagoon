# Worker Plan 04: Transcript-Grounded Tutor

> [!IMPORTANT]
> The tutor teaches from the current lesson only and explicitly bounds unsupported questions.

## Contract

| Item | Requirement |
| --- | --- |
| Prerequisite | Plans 00-03 passed |
| Deliverable | Free-form chat API/UI, relevant transcript selection, notes context, Ollama prompting |
| Safety boundary | No web search, citations, tools, fine-tuning, or answers beyond lesson support |
| Quality gate | [Readiness Audit](mvp-plan-readiness-audit.md) scores 10/10 before work; controller records all common quality checks afterward |

## Goal

Let a learner ask a free-form question and receive a teacher-style answer grounded only in the current transcript and notes. Success means unsupported questions are explicitly bounded and no outside knowledge path is available.

## Tasks

1. Add free-form question input and chat display tied to the current lesson.
2. Select relevant transcript chunks deterministically and pair them with current notes in the local Ollama prompt.
3. Prompt the model to answer like a teacher only from supplied lesson material and to state when the lesson does not support an answer.
4. Test through a fake model that captures supplied context and emits an unsupported-answer case.
5. Add clear pending/error states and document the verification command.

## Acceptance Criteria

- [ ] A relevant question sends matching transcript text and current notes to the model boundary.
- [ ] A question not supported by the lesson produces a clear limitation instead of a fabricated answer.
- [ ] Chat is scoped to the current transcript/notes and cannot access a prior lesson or outside source.
- [ ] Automated fake-model tests and one UI interaction test pass.
- [ ] A run log identifies test fixture, commands, and results without recording a real chat.

## Controller Verification

Inspect captured fake-model prompts for both a supported and unsupported question; then exercise both in the UI and apply every item in the controller's Common Independent Quality Gate. Do not begin full-flow work if chat can answer from undeclared knowledge sources or any quality-gate item fails.

## Outcome and Next Step

| Verification result | Report to user | Next step |
| --- | --- | --- |
| Pass | “Tutor passed” with prompt-capture and supported/unsupported UI results. | Commit/checkpoint; assign [Plan 05](05-full-flow-plan.md). |
| Fail | “Tutor failed” with the grounding or limitation criterion that failed. | Repair Plan 04 and repeat prompt/context verification. |
| Blocked | “Tutor blocked” with the missing local-model requirement. | Resolve it with the human; do not integrate the full flow. |

## Stop Point

No retrieval database, browser/tool calls, citations, model fine-tuning, or multi-lesson chat.
