# api/lagoon_local/transcription

> [!NOTE]
> Transcription owns media chunk planning, provider adapter boundaries, timestamp stitching, and artifact writing.

## Dashboard

| Item | Details |
| --- | --- |
| Real path | `C:\Users\isaac\Documents\Projects\Lagoon\api\lagoon_local\transcription\` |
| Phase | `SP-03` |
| Primary check | `npm run verify:sp03` |
| Provider status | Dry-run enabled; local/free `whisper.cpp` adapter enabled; OpenAI live adapter gated. |

## Files

| File | Purpose |
| --- | --- |
| `schema.py` | `MediaChunk`, `TranscriptSegment`, `TranscriptChunk` dataclasses and JSON shapes. |
| `chunking.py` | Provider/file-limit media chunk planner. |
| `provider.py` | `DryRunTranscriptionProvider`, `LocalWhisperCppProvider`, provider factory, and gated `OpenAITranscriptionProvider`. |
| `stitching.py` | Adds media chunk offsets to provider-relative segment times. |
| `pipeline.py` | End-to-end local pipeline: normalize audio, plan chunks, transcribe, stitch, chunk transcript, save artifacts. |

## Contracts

- Media chunking happens only for provider size, reliability, or duration needs.
- OpenAI file limit constant is `25 * 1024 * 1024` bytes.
- Segment timestamps are stored as absolute milliseconds against original lecture media.
- Provider segments must include `id`, `startMs`, `endMs`, and non-empty `text`; blank text is skipped and invalid timing/provenance fails clearly.
- Transcript artifacts include media chunks, provider metadata, diarization status, and segments.
- Pipeline result paths are typed as `Path`, not loose objects, so downstream code can use filesystem methods safely.
- Free local transcription uses `LocalWhisperCppProvider` with `LAGOON_TRANSCRIPTION_PROVIDER=local-whisper-cpp`, `LAGOON_WHISPER_CPP_BINARY`, and `LAGOON_WHISPER_CPP_MODEL`.
- OpenAI switch later uses the same `TranscriptionProvider` protocol and transcript schema.

## Gotchas

- Provider chunks and transcript chunks are different artifacts.
- `whisper.cpp` CLI needs a local binary and model; WAV/MP3/FLAC/OGG are safest based on current CLI docs.
- OpenAI provider adapter intentionally raises until credentials/sample/enablement are added.
