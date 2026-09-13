# Worker Plan 02: Audio-Only Transcription

> [!IMPORTANT]
> AssemblyAI receives extracted audio only. Completion is invalid if required cleanup fails.

## Contract

| Item | Requirement |
| --- | --- |
| Prerequisite | Plans 00-01 passed |
| Deliverable | Provider interface, AssemblyAI adapter, English plain-text transcript, cleanup/retry state |
| Automated dependency | Fake provider only; real calls belong in documented manual smoke testing |
| Quality gate | [Readiness Audit](mvp-plan-readiness-audit.md) scores 10/10 before work; controller records all common quality checks afterward |

## Goal

Produce an English plain-text transcript from extracted audio while proving that the MP4 is never sent and all temporary/provider data is deleted. Success means the notes worker receives transcript text with no unresolved privacy-cleanup failure.

## Tasks

1. Define a narrow transcription interface so tests use a fake and the UI/API avoid provider-specific leakage.
2. Submit only the extracted MP3, request English plain text, poll/retrieve completion, and return no timestamps or speaker labels.
3. Delete local audio immediately after every upload attempt, including failures.
4. After retrieval, delete the provider transcript and associated provider upload. Surface cleanup failure and provide in-session retry rather than declaring complete.
5. Disclose the audio transfer before upload; document real-key smoke-test prerequisites without storing a key.

## Acceptance Criteria

- [ ] Fake-provider tests prove an audio file—not an MP4—is submitted.
- [ ] Tests prove local audio removal after upload success and upload failure.
- [ ] Tests prove transcript and associated provider upload deletion are requested after retrieval.
- [ ] A simulated provider-cleanup failure is visible, prevents completion, and can be retried in session.
- [ ] A documented manual smoke test with a real key returns English plain text and leaves no provider data; credentials are absent from source/control logs.

## Controller Verification

Run fake-provider tests and inspect recorded request inputs/deletion calls. The controller performs or witnesses the optional credentialed smoke test only when the human supplies a key, then applies every item in the controller's Common Independent Quality Gate. Do not continue if cleanup is only best-effort or any quality-gate item fails.

## Outcome and Next Step

| Verification result | Report to user | Next step |
| --- | --- | --- |
| Pass | “Transcription passed” with fake-boundary evidence and real-smoke status. | Commit/checkpoint; assign [Plan 03](03-notes-plan.md). |
| Fail | “Transcription failed” with the specific transfer, deletion, retry, or transcript criterion. | Repair Plan 02 and re-run all cleanup checks; completion remains unavailable. |
| Blocked | “Transcription blocked” with the exact missing AssemblyAI credential/account decision. | Ask the human; keep fake-test evidence separate and do not start notes. |

## Stop Point

No multi-provider abstraction beyond the one testable interface, timestamps, speaker labels, or saved audio is in scope.
