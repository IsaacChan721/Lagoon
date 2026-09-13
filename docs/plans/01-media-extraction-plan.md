# Worker Plan 01: MP4 Input and Audio Extraction

> [!IMPORTANT]
> Media exists only in a unique temporary job directory and is never lesson storage.

## Contract

| Item | Requirement |
| --- | --- |
| Prerequisite | Plan 00 passed |
| Deliverable | Single MP4 picker, server validation, FFmpeg extraction to 16 kHz mono MP3, reliable cleanup |
| Required fixtures | Tiny synthetic valid MP4, non-MP4, and controllable over-limit metadata fixture |
| Quality gate | [Readiness Audit](mvp-plan-readiness-audit.md) scores 10/10 before work; controller records all common quality checks afterward |

## Goal

Safely turn one valid temporary MP4 into the constrained audio artifact needed for transcription while proving all local media is cleaned up. Success means Plan 02 receives audio only and cannot inherit retained source media.

## Tasks

1. Add one upload control and an API endpoint with a clearly bounded request size and one-file handling.
2. Verify type and duration server-side; reject unsupported files and video over 60 minutes before downstream work.
3. Create a per-job temporary directory, extract 16 kHz mono MP3 with FFmpeg, and expose only the result needed by the next boundary.
4. Guarantee MP4 deletion after extraction attempts; guarantee job-directory cleanup on all error paths without deleting unrelated files.
5. Add fakeable FFmpeg/probe boundaries and automated success/failure cleanup tests.

## Acceptance Criteria

- [ ] A short synthetic MP4 is accepted and yields a mono 16 kHz MP3 in its job scope.
- [ ] Non-MP4 and over-60-minute inputs are rejected with useful errors.
- [ ] Tests prove the original temporary MP4 is deleted after successful extraction and extraction failure.
- [ ] Tests prove each job uses an isolated temporary location and no MP4/audio reaches lesson storage.
- [ ] The README contains the actual media-test command and the run log reports its output.

## Controller Verification

Run the media tests; inspect both cleanup paths and storage paths; manually select the valid fixture once; then apply every item in the controller's Common Independent Quality Gate. Do not supply a real transcription key or start Plan 02 until this passes and the quality-gate record is entirely pass.

## Outcome and Next Step

| Verification result | Report to user | Next step |
| --- | --- | --- |
| Pass | “Media extraction passed” with validation and cleanup-test results. | Commit/checkpoint; assign [Plan 02](02-transcription-plan.md). |
| Fail | “Media extraction failed” with the rejected/cleanup case that failed. | Repair Plan 01 only; re-run success and failure cleanup tests. |
| Blocked | “Media extraction blocked” with the FFmpeg or fixture issue. | Obtain the missing dependency/decision; do not implement transcription. |

## Stop Point

No previews, YouTube input, visual analysis, retained media, or transcription-provider request belongs here.
