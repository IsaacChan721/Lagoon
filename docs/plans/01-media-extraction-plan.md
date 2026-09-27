# Worker Plan 01: MP4 Input and Audio Extraction

> [!IMPORTANT]
> Media exists only in a unique temporary job directory and is never lesson storage.

## Contract

| Item | Requirement |
| --- | --- |
| Prerequisite | Plan 00 passed |
| Deliverable | Single MP4 picker; server validation of MP4 type, 2 GB maximum size, and 60-minute maximum duration; FFmpeg extraction to 16 kHz mono MP3; reliable cleanup |
| Required fixtures | Tiny synthetic valid MP4, non-MP4, controllable over-limit duration metadata, and an oversized-request test that does not require creating a 2 GB fixture |
| Quality gate | [Readiness Audit](mvp-plan-readiness-audit.md) scores 10/10 before work; controller records all common quality checks afterward |

## Goal

Safely turn one valid temporary MP4 into the constrained audio artifact needed for transcription while proving all local media is cleaned up. Success means Plan 02 receives audio only and cannot inherit retained source media.

## Tasks

1. Add one upload control and an API endpoint accepting exactly one MP4, with a hard 2 GB request-body limit enforced during receipt; do not rely only on client-provided `Content-Length`.
2. Validate the media server-side and reject unsupported/non-MP4 inputs, actual files over 2 GB, or videos over 60 minutes before invoking FFmpeg. Use an application-generated temporary filename rather than the submitted filename as a filesystem path.
3. Create a unique per-job temporary directory, extract 16 kHz mono MP3 with FFmpeg, and expose only the audio artifact through a narrow boundary for Plan 02. Keep successful extracted audio temporary and available only until the next boundary consumes it; never persist it as lesson data.
4. Guarantee MP4 deletion after extraction attempts. On failure, remove the entire job directory; on success, remove the MP4 and retain only the extracted audio until consumption, then remove the job directory. Cleanup must not affect unrelated paths.
5. Add fakeable FFmpeg/probe boundaries and automated success/failure cleanup tests, including invalid media, over-duration media, and over-size request rejection before an unbounded body is written to disk.

## Acceptance Criteria

- [ ] A short synthetic MP4 is accepted and yields a mono 16 kHz MP3 in its job scope.
- [ ] Non-MP4, over-2-GB, and over-60-minute inputs are rejected with useful errors before FFmpeg runs.
- [ ] Upload-size enforcement is tested without allocating a 2 GB test file and proves the oversized body is not fully written to disk.
- [ ] Tests prove the original temporary MP4 is deleted after successful extraction and extraction failure.
- [ ] Tests prove each job uses an isolated temporary location, submitted filenames cannot escape it, and no MP4/audio reaches lesson storage.
- [ ] On success, only temporary extracted audio remains available to the next boundary; after consumption or any failure, the job directory is removed.
- [ ] The README contains the actual media-test command and the run log reports its output.

## Controller Verification

Run the media tests; inspect both cleanup paths and storage paths; manually select the valid fixture once; verify oversize rejection does not consume/write the full body; then apply every item in the controller's Common Independent Quality Gate. Do not supply a real transcription key or start Plan 02 until this passes and the quality-gate record is entirely pass.

## Outcome and Next Step

| Verification result | Report to user | Next step |
| --- | --- | --- |
| Pass | “Media extraction passed” with validation and cleanup-test results. | Commit/checkpoint; assign [Plan 02](02-transcription-plan.md). |
| Fail | “Media extraction failed” with the rejected/cleanup case that failed. | Repair Plan 01 only; re-run success and failure cleanup tests. |
| Blocked | “Media extraction blocked” with the FFmpeg or fixture issue. | Obtain the missing dependency/decision; do not implement transcription. |

## Stop Point

No previews, YouTube input, visual analysis, retained media, or transcription-provider request belongs here.
