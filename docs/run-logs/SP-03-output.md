# SP-03 Output

> [!IMPORTANT]
> SP-03 built the local, audio-first transcript pipeline with dry-run verification and a free local `whisper.cpp` provider; no paid provider call ran.

## Dashboard

| Item | Status |
| --- | --- |
| Phase | `SP-03` |
| Goal | Convert durable lecture media artifacts into timestamped transcripts and RAG-ready transcript chunks. |
| Scope | `api/lagoon_local/`, `scripts/`, `package.json`, lessons, memory, run log. |
| Live provider | OpenAI blocked by missing `OPENAI_API_KEY` or sample media; free local provider available with `whisper.cpp`. |
| Verification | `npm run verify:sp03`, `npm run verify:sp02`, `npm run verify:sp01`, `git status --short`. |

## Summary

- Added durable media artifact audio normalization in `api/lagoon_local/media/audio.py`.
- Added transcription dataclasses, media chunk planning, dry-run provider, free local `whisper.cpp` provider, gated OpenAI adapter shell, stitching, and end-to-end pipeline under `api/lagoon_local/transcription/`.
- Added deterministic retry classification in `api/lagoon_local/jobs/retry.py`.
- Added RAG-ready transcript chunking in `api/lagoon_local/transcript_chunks/chunker.py`.
- Extended local storage with `transcripts/`, `transcript_chunks/`, `transcript_artifacts`, and `transcript_chunk_artifacts`.
- Added `npm run verify:sp03` and beginner lesson `docs/lessons/SP-03-media-transcription.md`.
- Hardening pass on 2026-07-14 tightened provider segment validation, path typing, word-safe forced chunk splitting, frontend async import race protection, and browser favicon noise.

## Blockers

| Blocker | Impact | Next action |
| --- | --- | --- |
| `OPENAI_API_KEY` or sample media missing | OpenAI transcription did not run. | Use free local `whisper.cpp` MVP path now; configure key/sample only when paid provider is wanted. |
| Local `whisper.cpp` binary/model not bundled | Free provider needs user-installed binary and downloaded `ggml` model. | Set `LAGOON_TRANSCRIPTION_PROVIDER`, `LAGOON_WHISPER_CPP_BINARY`, and `LAGOON_WHISPER_CPP_MODEL`. |
| Video audio extraction needs `ffmpeg` on PATH | Audio fixtures pass; video extraction blocks clearly if `ffmpeg` is missing. | Add bundled/validated ffmpeg strategy before relying on video imports. |

## Contract Changes

- Added local transcript artifact contract: JSON under app-data `transcripts/` plus SQLite row in `transcript_artifacts`.
- Added local transcript chunk artifact contract: JSON under app-data `transcript_chunks/` plus SQLite row in `transcript_chunk_artifacts`.
- Transcript segments preserve `segmentId`, `sourceSegmentId`, `mediaArtifactId`, `transcriptArtifactId`, `startMs`, `endMs`, `text`, provider, and optional speaker.
- Provider segments with blank text are skipped; provider segments with missing provenance, missing/non-numeric times, or non-increasing times fail before artifacts are written.
- Transcript chunks preserve `chunkId`, `lectureId`, `mediaArtifactId`, `transcriptArtifactId`, `segmentIds`, `startMs`, `endMs`, `text`, `boundaryReason`, `embeddingStatus`, provider metadata, and speaker labels.
- Forced transcript chunk splits preserve word boundaries when possible and validate positive `max_chars`.
- No source enrichment, visual understanding, tutor features, or broad refactor added.
- `.gitignore` local-data patterns were scoped to repo root so `api/lagoon_local/media/` source package can be tracked.

## Provider And Cost Decision

- Free MVP path: `LocalWhisperCppProvider`, using local `whisper.cpp` CLI and local `ggml` model. No API key, no network, no OpenAI billing.
- Dry-run provider remains default for deterministic verification.
- OpenAI provider-backed path is deferred behind explicit credentials/sample/live enablement.
- OpenAI docs checked on 2026-06-24: speech-to-text supports `gpt-4o-mini-transcribe`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`; uploads are limited to 25 MB; supported input formats include `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav`, and `webm`.
- OpenAI pricing page checked on 2026-06-24. No paid SP-03 call was made; exact live transcription cost must be re-confirmed before enabling provider calls.
- Diarization deferred. It requires cost/provider approval and a lecture need; future path likely uses `gpt-4o-transcribe-diarize` with `diarized_json`.

## Offline / Free Fallback Status

- Free local `whisper.cpp` provider implemented and covered by fake-CLI fixture test.
- No offline speech recognition binary/model is bundled in repo.
- Configure with `LAGOON_TRANSCRIPTION_PROVIDER=local-whisper-cpp`, `LAGOON_WHISPER_CPP_BINARY`, and `LAGOON_WHISPER_CPP_MODEL`.
- Local video extraction can use `ffmpeg` if installed; otherwise blocks clearly.

## Skill Changes

- Used mandatory `caveman`.
- Used mandatory `transcribe`.
- Used mandatory `Superpowers:test-driven-development`.
- Used mandatory `Superpowers:systematic-debugging`.
- Used conditional `openai-docs` for current provider/limit/pricing check.
- Used conditional `Superpowers:verification-before-completion` before final status.
- Did not use `OpenAI Developers:openai-api-troubleshooting`; no API failure occurred.

## Memory Bank Updates

- Updated `docs/memory/phases/SP-03/index.md`.
- Updated `docs/memory/codebase/api/lagoon_local/index.md`.
- Updated `docs/memory/codebase/api/lagoon_local/storage.md`.
- Added `docs/memory/codebase/api/lagoon_local/media/index.md`.
- Added `docs/memory/codebase/api/lagoon_local/transcription/index.md`.
- Added `docs/memory/codebase/api/lagoon_local/transcript_chunks/index.md`.
- Added `docs/memory/codebase/api/lagoon_local/jobs/index.md`.
- Updated `docs/memory/codebase/scripts/index.md`.
- Updated `docs/memory/codebase/docs/lessons/index.md`.

## Phase Plan Status

- Followed SP-03 plan for MVP pipeline, dry-run verification, free local provider adapter, storage, chunking, stitching, retry, docs, and memory.
- Changed provider decision from dry-run-only MVP to free local `whisper.cpp` MVP, while keeping OpenAI adapter for future paid path.
- Git checkpoint was not completed because repo had many pre-existing dirty docs changes and no remote status was resolved in this phase; `git status --short` was run as required.

## Tests Run

| Command | Result |
| --- | --- |
| `C:\Users\isaac\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\verify_sp03_transcription.py` before implementation | Failed as expected on missing SP-03 files. |
| `npm run verify:sp03` | Passed, including local `whisper.cpp` fake-CLI adapter test. |
| `npm run verify:sp02` | Passed. |
| `npm run verify:sp01` | Passed. |
| `npm run build:web` | Passed. |
| Browser E2E against `http://127.0.0.1:5173` | Passed: initial render, unsupported file, supported audio metadata error, save, reset, mobile overflow, no page errors. |
| `git status --short` | Ran; shows SP-03 changes plus pre-existing dirty docs. |
| `git status --short --ignored api\lagoon_local\media` | Previously showed ignored before `.gitignore` fix; rerun after fix no longer reports it ignored. |

## Next Gate

- Install/configure `whisper.cpp` binary and `ggml` model for real free local transcription.
- Add explicit OpenAI live provider integration once key, sample media, and current cost approval exist.
- Add validated `ffmpeg` dependency path or video fixture before relying on video lecture extraction.
- SP-04 can use transcript absolute timestamps as primary timeline after SP-03 artifacts are accepted.

## References

- [OpenAI speech-to-text docs](https://developers.openai.com/api/docs/guides/speech-to-text)
- [OpenAI API pricing](https://openai.com/api/pricing/)
- [whisper.cpp README](https://github.com/ggml-org/whisper.cpp)
