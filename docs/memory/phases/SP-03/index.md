# SP-03 Memory

## Purpose

Track media inspection, audio extraction, provider-limit media chunking, transcription jobs, retry logic, transcript schema, semantic transcript chunks, timestamp offsets, and provider/cost decisions.

## Expected Codebase Mirrors

- `docs/memory/codebase/api/lagoon_local/media/`
- `docs/memory/codebase/api/lagoon_local/transcription/`
- `docs/memory/codebase/api/lagoon_local/transcript_chunks/`
- `docs/memory/codebase/api/lagoon_local/jobs/`
- `docs/memory/codebase/scripts/`

## Implemented In SP-03

- Added durable media artifact audio normalization in `api/lagoon_local/media/audio.py`.
- Added transcription schema, media chunk planner, provider adapter shells, local/free Whisper CLI provider, stitcher, and pipeline under `api/lagoon_local/transcription/`.
- Added retry classification in `api/lagoon_local/jobs/retry.py`.
- Added RAG-ready transcript chunker in `api/lagoon_local/transcript_chunks/chunker.py`.
- Added local transcript output dirs to `StorageLayout`: `transcripts/` and `transcript_chunks/`.
- Added SQLite metadata tables: `transcript_artifacts` and `transcript_chunk_artifacts`.
- Added `npm run verify:sp03` fixture verifier.
- Added beginner lesson `docs/lessons/SP-03-media-transcription.md`.

## Prerequisite Context

- Read `docs/run-logs/SP-02-output.md` before implementation.
- Read `docs/memory/phases/SP-02/index.md` for the uploaded media artifact contract.
- Read `docs/memory/codebase/web/src/media-import/index.md` for frontend artifact fields.
- Read `docs/memory/codebase/api/lagoon_local/storage.md` for durable local media registration.

## Contract Decisions

- Use uploaded lecture media from durable local artifact storage, not browser object URLs.
- Treat audio transcript as primary evidence. Visuals are support handled by `SP-04`.
- Split media only when provider payload limits, duration reliability, or codec handling requires it.
- Split transcript into semantic RAG-ready chunks after stitching transcript segments.
- Prefer sentence, pause, or transcript-segment boundaries. Never split mid-sentence unless size limits force it; record `boundaryReason` when forced.
- When size limits force transcript splits, preserve word boundaries when possible and validate chunking knobs before work starts.
- Store all transcript and chunk times as absolute offsets into original lecture media: `startMs` and `endMs`.
- For provider media chunks, store `chunkStartMs` and convert returned provider-relative segment times into absolute lecture times.
- Validate provider segment payloads before stitching: require provenance ID and increasing millisecond times; skip blank text segments.
- Diarization is optional. Enable only when provider support, cost, and lecture format justify it; otherwise store speaker as unknown/null.
- Provider-backed calls require explicit API configuration and current pricing check. Keep fixture/dry-run path available when credentials or sample media are missing.
- SP-03 MVP uses `DryRunTranscriptionProvider` for deterministic verification and `LocalWhisperCppProvider` for free local transcription when `whisper.cpp` is installed.
- Free local provider config uses `LAGOON_TRANSCRIPTION_PROVIDER=local-whisper-cpp`, `LAGOON_WHISPER_CPP_BINARY`, and `LAGOON_WHISPER_CPP_MODEL`.
- OpenAI live adapter is a gated shell only. It does not call network until key, sample media, and explicit provider enablement exist.
- Current OpenAI speech-to-text docs checked during SP-03: transcription snapshots include `gpt-4o-mini-transcribe`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`; upload limit is 25 MB; supported formats include `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav`, and `webm`.
- Diarization is deferred. Use `gpt-4o-transcribe-diarize` only after cost/provider decision; docs say it supports `diarized_json` and needs `chunking_strategy` for audio longer than 30 seconds.

## Verification

- Red observed: bundled Python verifier failed on missing SP-03 files before implementation.
- Green: `npm run verify:sp03`.
- Green: `npm run verify:sp02`.
- Green: `npm run verify:sp01`.
- Green: `npm run build:web`.
- Green: Browser E2E smoke against Vite dev server for import, save, reset, and mobile overflow.
- Fixture live-call gate documented: `OPENAI_API_KEY` or sample media missing, so no paid provider call ran.

## Failure States

| Failure | Class | Retry |
| --- | --- | --- |
| Invalid API key or auth denied | `auth` | No |
| Quota or billing limit | `quota` | No |
| Payload too large | `payload` | No |
| Codec/decode failure | `codec` | No |
| Timeout or connection reset | `network` | Yes, bounded |
| Unknown provider failure | `unknown` | Yes, bounded |

## Free MVP Provider Decision

- Chosen free path: `whisper.cpp` CLI adapter.
- Reason: open-source local Whisper inference, offline/on-device use, CPU support, Windows support, JSON output, and simple command boundary.
- MVP does not vendor binaries or models. User installs `whisper.cpp` and downloads a local `ggml` model.
- Future iteration can switch provider name from `local-whisper-cpp` to `openai` without changing transcript/chunk artifact schemas.

## Transcript Chunk Shape

Each RAG-ready chunk should preserve enough evidence for `SP-05` retrieval and later citations:

- `chunkId`
- `lectureId`
- `mediaArtifactId`
- `transcriptArtifactId`
- `segmentIds`
- `startMs`
- `endMs`
- `text`
- `speakerIds` or `speakerLabels` when available
- `boundaryReason`
- `embeddingStatus`
- `providerMetadata`

## Downstream Expectations

- `CRIT-01` validates transcript/chunk provenance and trust boundaries before enrichment.
- `SP-04` links visual evidence to the same absolute media time ranges.
- `SP-05` indexes transcript chunks directly; embeddings may be added later without changing chunk IDs or citation fields.
- `SP-06` cites transcript chunks, transcript segments, and visual evidence by ID.
- `SP-07` tutor answers must stay inside selected lecture/chunk boundaries.
