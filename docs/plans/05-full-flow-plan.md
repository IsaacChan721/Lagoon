# Worker Plan 05: Full Learner Flow and Continuity

> [!IMPORTANT]
> Integrate completed boundaries into one understandable local journey; do not add a lesson library.

## Contract

| Item | Requirement |
| --- | --- |
| Prerequisite | Plans 00-04 passed |
| Deliverable | One-page upload-to-chat flow, state feedback, latest-completed-lesson persistence and restore |
| Persist | Latest transcript, notes, and chat only; never MP4 or audio |
| Quality gate | [Readiness Audit](mvp-plan-readiness-audit.md) scores 10/10 before work; controller records all common quality checks afterward |

## Goal

Deliver the complete one-page learner journey from temporary MP4 through one grounded tutor answer, then restore the latest completed lesson after restart. Success means the MVP's functional and privacy boundaries work together, not merely as isolated components.

## Tasks

1. Connect upload, extraction, transcription, notes, and tutor flow on a single page.
2. Clearly display ready, uploading, transcribing, creating notes, complete, and failed states, including cleanup-failure retry.
3. Persist only a completed lesson's transcript, notes, and chat locally using a small storage boundary.
4. Restore the latest completed lesson after restart; ensure failed/incomplete work does not replace it.
5. Add a fixture-backed end-to-end smoke test using fake transcription/model clients and a restart verification.

## Acceptance Criteria

- [ ] The synthetic fixture completes upload through one grounded tutor answer without real provider/model calls.
- [ ] Each required state is observable, and a failure shows a useful message and appropriate retry path.
- [ ] Restart restores the latest completed transcript, five-section notes, and chat.
- [ ] Storage inspection proves it contains no MP4/audio and failed work does not overwrite the prior completed lesson.
- [ ] End-to-end smoke and restart tests pass; README contains exact commands and run log evidence.

## Controller Verification

Run the fixture smoke test, restart the local app, inspect restored data, and inspect storage/temp locations. The controller must also force a cleanup failure and verify that it is not reported as complete, then apply every item in the controller's Common Independent Quality Gate.

## Outcome and Next Step

| Verification result | Report to user | Next step |
| --- | --- | --- |
| Pass | “Full learner flow passed” with smoke, restart, state, and storage evidence. | Commit/checkpoint; assign [Plan 06](06-handoff-plan.md). |
| Fail | “Full learner flow failed” with the stage/state/persistence/cleanup criterion. | Return to the owning earlier plan if the boundary is defective; otherwise repair Plan 05 and re-run end-to-end checks. |
| Blocked | “Full learner flow blocked” with the required local dependency or human decision. | Stop release preparation until the blocker is resolved. |

## Stop Point

No multi-lesson history, accounts, cloud sync, analytics, billing, or UI-polish work beyond usable feedback.
