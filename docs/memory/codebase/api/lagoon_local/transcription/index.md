# api/lagoon_local/transcription

> [!NOTE]
> Transcription owns media chunk planning, provider adapter boundaries, timestamp stitching, and artifact writing.

## Dashboard

| Item | Details |
| --- | --- |
| Real path | `C:\Users\isaac\Documents\Projects\Lagoon\api\lagoon_local\transcription\` |
| Phase | `SP-03` |
| Primary check | `npm run verify:sp03` |
| Provider status | Dry-run enabled; OpenAI live adapter gated. |

## Files

| File | Purpose |
| --- | --- |
| `schema.py` | `MediaChunk`, `TranscriptSegment`, `TranscriptChunk` dataclasses and JSON shapes. |
| `chunking.py` | Provider/file-limit media chunk planner. |
| `provider.py` | `DryRunTranscriptionProvider` and gated `OpenAITranscriptionProvider`. |
| `stitching.py` | Adds media chunk offsets to provider-relative segment times. |
| `pipeline.py` | End-to-end local pipeline: normalize audio, plan chunks, transcribe, stitch, chunk transcript, save artifacts. |

## Contracts

- Media chunking happens only for provider size, reliability, or duration needs.
- OpenAI file limit constant is `25 * 1024 * 1024` bytes.
- Segment timestamps are stored as absolute milliseconds against original lecture media.
- Transcript artifacts include media chunks, provider metadata, diarization status, and segments.

## Gotchas

- Provider chunks and transcript chunks are different artifacts.
- Live provider adapter intentionally raises until credentials/sample/enablement are added.
