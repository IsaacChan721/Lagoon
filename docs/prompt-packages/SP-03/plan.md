# SP-03 Execution Plan

## Caveman Requirement

Execute in `caveman full`. Use normal prose only when clarity or safety would suffer, then resume `caveman full`.

## Keep It Simple

- Treat this phase as an MVP slice.
- Prefer beginner-readable code and docs over clever abstractions.
- Do not add extra logic unless required by acceptance criteria, safety, or verification.
- Put marginal improvements in handoff next steps, not in phase code.

## Goal

Implement audio-first media processing, transcription, and RAG-ready transcript chunk pipeline for imported lecture media.

## Inputs

- `docs/plans/main-orchestration.md`
- `docs/memory/index.md`
- `docs/memory/phases/SP-03/index.md`
- imported media artifact and storage memory notes
- current transcription provider docs and pricing, checked only when provider-backed calls are added

## In Scope

- Durable imported media lookup from the `SP-02` local artifact contract.
- Audio extraction from uploaded lecture media.
- Provider/file-limit media chunking when needed.
- Transcription request flow with cost-aware provider selection.
- Retry and failure handling.
- Transcript stitching with absolute media timestamps.
- Semantic transcript chunks for later RAG indexing.
- Transcript artifact storage.

## Out Of Scope

- No source enrichment.
- No visual understanding beyond needed media/audio metadata.
- No browser object URL use for durable processing.
- No tutor features.

## Execution Steps

1. Confirm `SP-02` media artifact contract and use only durable local artifact references for backend processing.
2. Read transcription skill/API docs only as needed; verify current provider limits and pricing before paid calls.
3. Extract or normalize audio from imported media into local temp/app-data paths; never treat browser object URLs as durable paths.
4. Chunk media only when provider limits, payload size, or long-duration reliability requires it.
5. Prefer silence, pause, or sentence-aware chunk boundaries; if forced to split by size/time, record boundary caveat.
6. Transcribe chunks with deterministic job IDs, retry policy, and provider metadata.
7. Stitch transcript segments into absolute lecture timestamps by adding each media chunk start offset.
8. Build semantic transcript chunks from stitched segments for RAG: preserve sentence boundaries, pause boundaries, source segment IDs, `startMs`, `endMs`, and `mediaArtifactId`.
9. Add retry/error states for auth, quota, network, payload, codec, and unknown failures.
10. Verify transcript and transcript-chunk output with fixture or sample media.

## Acceptance Criteria

- Media artifact can produce transcript artifact.
- Transcript keeps media provenance and timestamps.
- Transcript chunks are RAG-ready and cite source transcript segment IDs.
- Transcript chunks do not split mid-sentence unless size limits force a documented exception.
- Timestamp offsets remain absolute to the original lecture media, even when provider calls use smaller chunks.
- Browser object URLs are used only for frontend preview, never as backend durable inputs.
- Retry/failure behavior is deterministic.
- Large media is chunked or blocked with clear message.

## Definition Of Done

- Pipeline check passes with fixture/sample.
- Transcript artifact is saved locally.
- Transcript chunk artifact is saved locally for `SP-05`.
- Provider/cost choice and offline/free fallback status are documented in handoff.
- Failure states are documented in memory and handoff.

## Verification

- Run unit/integration tests for chunking and stitching.
- Run transcript-chunk boundary tests for sentence/pause preservation and absolute timestamps.
- Run one transcription fixture path if credentials and sample exist.
- If no credentials/sample exist, run provider-adapter dry-run or fixture-only path and document blocked live call.
- Run `git status --short`.

## Troubleshooting

- If API fails, classify auth, quota, network, or payload issue first.
- If timestamps drift, test chunk start offsets, provider timestamp units, and media extraction duration.
- If chunk text splits sentences poorly, tune pause/sentence boundary logic before changing retrieval model.
- If files are too large, reduce chunk size before changing API contract.
- If diarization is requested, treat it as optional: use speaker-aware model only when cost, provider support, and lecture format justify it.
- If cost is unacceptable, keep provider interface but allow local/open-source transcription adapter later; do not reshape artifact contracts.

## Lesson Plan

Design this phase memory as beginner lesson material. Put no-prerequisite transcription context first, then build toward chunking, provider calls, stitching, and storage.

### Lesson Depth Standard

Every lesson below must be written and taught as a 60-90 minute beginner module, not a quick concept note. Use the lesson bullets as topic seeds, then expand them with this structure:

1. Zero-prerequisite setup, 5-10 minutes: define every term used in the lesson, explain why the learner should care, and name the files or planned files they will touch.
2. File map, 10-15 minutes: list each relevant file, folder, command, schema, component, or artifact. For future files, mark them `planned`. Explain what each one owns and what it must not own.
3. Line-by-line code reading, 15-25 minutes: walk through the smallest real code sample available. If implementation does not exist yet, write planned pseudocode and later replace it with real code. Explain each line or block in beginner language, including imports, data shapes, function inputs, outputs, errors, and side effects.
4. Guided hands-on exercise, 15-25 minutes: have the learner run a command, inspect output, trace data through one function, update a harmless fixture, or write a tiny example. Include expected output and what to do if it differs.
5. Debugging or design exercise, 10-20 minutes: give one realistic failure, ask the learner to diagnose it, then provide the answer and the reasoning path.
6. Theory questions and answers, 10-15 minutes: include at least five Q/A pairs that connect the hands-on work to architecture, privacy, security, testing, or user experience.
7. Checkpoint, 5-10 minutes: include a small task the learner can complete without help, plus acceptance criteria.
8. Key takeaways, 5 minutes: list what the learner should remember before moving to the next lesson.

Each lesson must include concrete code or command examples. Prefer real snippets from this codebase once the phase exists. Avoid abstract-only examples. When a lesson covers safety, privacy, auth, encryption, destructive actions, or external providers, spell out the risk clearly and then return to concise style.
### Created In This Phase

- Durable media-to-audio processing path.
- Provider-limit media chunking pipeline.
- Transcription request and retry flow.
- Transcript stitching logic with absolute timestamps.
- Transcript artifact schema and local storage.
- Semantic transcript chunk schema for RAG.
- Tests or fixtures for chunking, retry, stitching, and transcript chunk boundaries.

### Lesson 1: From Media To Transcript

- Prerequisites: none.
- Explain: transcription turns local audio/video into timed text segments.
- Coding example: show a transcript segment object with `segmentId`, `startMs`, `endMs`, `text`, `mediaArtifactId`, `provider`, and optional `speaker`.
- Theory Q/A: Why keep timestamps? They connect answers, summaries, and citations back to exact lecture moments.
- Key takeaways: transcript is structured data, not just one text blob.

### Lesson 2: Chunking Large Media

- Prerequisites: understand transcript segments.
- Explain: large provider payloads must be split or rejected with clear reason; transcript chunks for retrieval are a separate artifact.
- Coding example: show pseudocode for `chunkMedia(file, maxDurationMs, maxBytes)` returning ordered chunk descriptors with `chunkStartMs`.
- Theory Q/A: Why avoid changing API contract first? Bad chunk boundaries usually cause drift before provider choice matters.
- Key takeaways: deterministic chunk IDs and time ranges make stitching testable.

### Lesson 3: Retry And Failure Handling

- Prerequisites: understand chunking.
- Explain: failures are classified as auth, quota, network, payload, or unknown.
- Coding example: show a retry rule that retries network errors but not auth errors.
- Theory Q/A: Why classify before retrying? Retrying permanent failures wastes time and can hide real setup issues.
- Key takeaways: retries need limits, error classes, and visible user states.

### Lesson 4: Stitching And Storage

- Prerequisites: understand chunking and retry.
- Explain: stitched transcript preserves segment order, media provenance, and absolute timestamps.
- Coding example: show sorting chunks by `chunkIndex`, then offsetting segment times by `chunkStartMs`.
- Theory Q/A: What proves stitching works? Fixture with known chunk boundaries and expected timestamps.
- Key takeaways: transcript storage must preserve source media ID, timestamps, and failure caveats.

### Lesson 5: RAG-Ready Transcript Chunks

- Prerequisites: understand stitched transcript segments.
- Explain: retrieval chunks group nearby transcript segments into evidence units that embeddings or local search can index later.
- Coding example: show a transcript chunk object with `chunkId`, `lectureId`, `segmentIds`, `startMs`, `endMs`, `text`, `boundaryReason`, and `embeddingStatus`.
- Theory Q/A: Why chunk after transcription instead of only before transcription? Provider chunks solve upload limits; transcript chunks solve retrieval quality.
- Key takeaways: RAG chunks must preserve citations back to transcript segments and original media time.

## Memory Updates

Update `docs/memory/phases/SP-03/index.md` and codebase notes for media pipeline, transcript schema, semantic transcript chunk schema, retry rules, timestamp offsets, provider/cost choice, and caveats.

## Git Checkpoint

After verification and handoff, push this phase by itself:

1. Run `git status --short`.
2. Run `git add <files changed for SP-03>`.
3. Run `git commit -m "SP-03: complete phase"`.
4. Run `git push`.

Commit only scoped SP-03 changes. Leave later-phase ideas in next steps.

## Handoff Output

Write `docs/run-logs/SP-03-output.md` with summary, blockers, contract changes, provider/cost decision, offline fallback status, skill changes, memory updates, tests run, and next gate.
