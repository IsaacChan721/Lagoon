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
- Added transcription schema, media chunk planner, provider adapter shells, stitcher, and pipeline under `api/lagoon_local/transcription/`.
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
- Store all transcript and chunk times as absolute offsets into original lecture media: `startMs` and `endMs`.
- For provider media chunks, store `chunkStartMs` and convert returned provider-relative segment times into absolute lecture times.
- Diarization is optional. Enable only when provider support, cost, and lecture format justify it; otherwise store speaker as unknown/null.
- Provider-backed calls require explicit API configuration and current pricing check. Keep fixture/dry-run path available when credentials or sample media are missing.
- SP-03 MVP uses `DryRunTranscriptionProvider` for deterministic, free verification.
- OpenAI live adapter is a gated shell only. It does not call network until key, sample media, and explicit provider enablement exist.
- Current OpenAI speech-to-text docs checked during SP-03: transcription snapshots include `gpt-4o-mini-transcribe`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`; upload limit is 25 MB; supported formats include `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav`, and `webm`.
- Diarization is deferred. Use `gpt-4o-transcribe-diarize` only after cost/provider decision; docs say it supports `diarized_json` and needs `chunking_strategy` for audio longer than 30 seconds.

## Verification

- Red observed: bundled Python verifier failed on missing SP-03 files before implementation.
- Green: `npm run verify:sp03`.
- Green: `npm run verify:sp02`.
- Green: `npm run verify:sp01`.
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

## Release Caveat

- `api/lagoon_local/media/` is currently ignored by the existing root `.gitignore` pattern `media/`.
- The code exists locally and `npm run verify:sp03` passes, but a future commit needs either a scoped `.gitignore` exception or a package rename before the media helper can be staged.

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
