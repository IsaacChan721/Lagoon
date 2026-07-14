# SP-03 Media Transcription

> [!IMPORTANT]
> SP-03 turns durable imported lecture media into audio-first timed transcripts and RAG-ready transcript chunks; browser object URLs stay preview-only.

## Learning Dashboard

| Item | Details |
| --- | --- |
| Phase | `SP-03` |
| Learner goal | Understand local media artifact lookup, audio normalization, provider chunking, stitching, retry, and transcript chunking. |
| Main feature | `api/lagoon_local/transcription/pipeline.py` |
| Phase boundary | No source enrichment, no visual understanding, no tutor features. |
| Best first check | `npm run verify:sp03` |
| Time box | 60-90 minutes per lesson module. |

## Quick Navigation

| Section | Best for |
| --- | --- |
| [Beginner Path](#beginner-path) | File order for first read. |
| [Lesson 1: From Media To Transcript](#lesson-1-from-media-to-transcript) | Transcript basics. |
| [Lesson 2: Chunking Large Media](#lesson-2-chunking-large-media) | Provider/file limits. |
| [Lesson 3: Retry And Failure Handling](#lesson-3-retry-and-failure-handling) | Deterministic failures. |
| [Lesson 4: Stitching And Storage](#lesson-4-stitching-and-storage) | Absolute timestamps. |
| [Lesson 5: RAG-Ready Transcript Chunks](#lesson-5-rag-ready-transcript-chunks) | Retrieval evidence units. |

## Beginner Path

1. `api/lagoon_local/storage.py`
2. `api/lagoon_local/media/audio.py`
3. `api/lagoon_local/transcription/chunking.py`
4. `api/lagoon_local/transcription/provider.py`
5. `api/lagoon_local/transcription/stitching.py`
6. `api/lagoon_local/transcript_chunks/chunker.py`
7. `api/lagoon_local/transcription/pipeline.py`
8. `scripts/verify_sp03_transcription.py`

---

## Lesson 1: From Media To Transcript

### Zero-Prerequisite Setup

| Term | Meaning |
| --- | --- |
| Media artifact | Durable local record from SP-02 with file path, MIME type, duration, and ID. |
| Transcript segment | One timed piece of text from audio. |
| Primary evidence | Audio transcript is trusted first for later answers and citations. |

Care because later RAG must cite exact lecture time. Transcript is structured data, not one text blob.

### File Map

| File | Owns | Must not own |
| --- | --- | --- |
| `api/lagoon_local/media/audio.py` | Resolve media artifact and make transcription-ready audio. | Browser preview URLs. |
| `api/lagoon_local/transcription/schema.py` | Shared dataclasses. | Provider calls. |
| `api/lagoon_local/transcription/pipeline.py` | End-to-end fixture/free-local/live adapter flow. | Visual analysis. |

### Code Reading

```python
segment = TranscriptSegment(
    segment_id="tx-1-segment-0000",
    lecture_id="lecture-1",
    media_artifact_id="media-1",
    transcript_artifact_id="tx-1",
    start_ms=500,
    end_ms=1500,
    text="First sentence.",
    source_segment_id="provider-a",
    provider="dry-run",
)
```

`segment_id` is Lagoon ID. `source_segment_id` is provider ID. `start_ms` and `end_ms` point to original lecture media, not a temporary provider chunk.

### Hands-On Exercise

Run:

```powershell
npm run verify:sp03
```

Expected result:

```text
SP-03 media transcription verification passed
```

If Python is missing from PATH, wrapper uses bundled Codex Python.

### Debugging Exercise

Failure: `media artifact local file is missing`.

Answer: SP-03 found SQLite row but copied file is gone. Re-import media or repair local artifact path. Do not use `blob:` URL as substitute.

### Theory Q/A

| Question | Answer |
| --- | --- |
| Why keep timestamps? | They support exact citations and later visual alignment. |
| Why keep `mediaArtifactId`? | It ties transcript evidence to durable SP-02 artifact. |
| Why keep source provider ID? | It lets debugging compare Lagoon segment to provider output. |
| Why audio first? | Lecture speech usually carries primary teaching content. |
| Why no visual enrichment here? | SP-04 owns visuals. Scope stays small. |
| Why reject missing provider IDs? | Missing provenance makes transcript debugging and citations weak. |

### Checkpoint

- [ ] Explain why `blob:` URLs cannot enter backend transcription.
- [ ] Identify where transcript JSON is written.

### Key Takeaways

- Transcript is structured evidence.
- Every segment needs provenance and absolute time.

---

## Lesson 2: Chunking Large Media

### Zero-Prerequisite Setup

Provider upload APIs often have file-size limits. Chunking media solves upload and reliability, not retrieval.

### File Map

| File | Purpose |
| --- | --- |
| `transcription/chunking.py` | Creates deterministic media chunk descriptors. |
| `transcription/stitching.py` | Converts provider-relative times to original lecture time. |

### Code Reading

```python
chunks = plan_media_chunks(
    media_artifact_id="media-1",
    local_path=Path("lecture.m4a"),
    size_bytes=60 * 1024 * 1024,
    duration_ms=3_600_000,
)
```

Large media returns ordered chunks like `media-1-media-0000`. Each chunk records `start_ms`, `end_ms`, and `boundary_reason`.

### Hands-On Exercise

Open `scripts/verify_sp03_transcription.py` and find `assert_media_chunking_contract`. Change fixture duration in a scratch copy mentally: bigger duration means more chunks.

### Debugging Exercise

Failure: `large media requires known duration`.

Answer: deterministic chunking needs duration to preserve absolute offsets. Re-read metadata or block with clear message.

### Theory Q/A

| Question | Answer |
| --- | --- |
| Why chunk media at all? | Provider size limits or reliability. |
| Why avoid semantic media chunks? | Semantics are clearer after speech becomes text. |
| Why deterministic IDs? | Retries and stitching need stable references. |
| Why record boundary reason? | It explains forced splits and possible quality caveats. |
| Why avoid provider choice first? | Bad chunk offsets can break any provider. |

### Checkpoint

- [ ] Name two reasons media can be chunked.
- [ ] Find where `boundary_reason` is stored.

### Key Takeaways

- Media chunks solve transport.
- Transcript chunks solve retrieval.

---

## Lesson 3: Retry And Failure Handling

### Zero-Prerequisite Setup

Provider calls can fail. Some failures are permanent, like auth. Some can be retried, like network timeouts.

### File Map

| File | Purpose |
| --- | --- |
| `jobs/retry.py` | Classifies auth, quota, network, payload, codec, unknown. |
| `transcription/provider.py` | Dry-run provider, free local `whisper.cpp` provider, and gated OpenAI adapter shell. |

### Code Reading

```python
if failure_kind in {"network", "unknown"} and attempt < max_attempts:
    retry = True
```

Network/unknown can retry. Auth, quota, payload, and codec do not retry because repeating them wastes cost and hides setup errors.

Free MVP provider setup:

```powershell
$env:LAGOON_TRANSCRIPTION_PROVIDER = "local-whisper-cpp"
$env:LAGOON_WHISPER_CPP_BINARY = "C:\tools\whisper.cpp\build\bin\Release\whisper-cli.exe"
$env:LAGOON_WHISPER_CPP_MODEL = "C:\models\ggml-base.en.bin"
```

Then Lagoon can create a `LocalWhisperCppProvider` through the same provider protocol used by the future OpenAI adapter.

### Hands-On Exercise

Read `assert_retry_policy_classifies_failures` in verifier. Match each error string to class.

### Debugging Exercise

Failure: `401 invalid api key`.

Answer: classify as auth, stop retry, ask for proper local key setup. Never ask user to paste secret into chat.

### Theory Q/A

| Question | Answer |
| --- | --- |
| Why classify before retry? | Avoid waste and clearer user state. |
| Why retry unknown? | Some transient provider failures lack clean labels. |
| Why limit retries? | Infinite retries can burn time and money. |
| Why dry-run provider? | Tests stay free and deterministic. |
| Why local `whisper.cpp` provider? | MVP can transcribe without API cost. |
| Why adapter shell? | OpenAI can be swapped in later without changing artifacts. |

### Checkpoint

- [ ] Explain why quota is not retried.
- [ ] Find dry-run segment text.

### Key Takeaways

- Retry only likely temporary failures.
- Fixture path protects local-first workflow.

---

## Lesson 4: Stitching And Storage

### Zero-Prerequisite Setup

Provider chunk timestamps are relative to uploaded chunk. Lagoon needs absolute original lecture timestamps.

### File Map

| File | Purpose |
| --- | --- |
| `stitching.py` | Adds `chunk.start_ms` to provider segment times. |
| `storage.py` | Creates transcript tables and local output dirs. |
| `pipeline.py` | Writes transcript and chunk JSON files. |

### Code Reading

```python
start_ms = _required_ms(provider_segment, "startMs") + chunk.start_ms
end_ms = _required_ms(provider_segment, "endMs") + chunk.start_ms
```

If provider says segment starts at `250 ms` inside a chunk that began at `10,000 ms`, Lagoon stores `10,250 ms`.
Blank provider text is skipped. Missing provider IDs, missing times, non-numeric times, or `endMs <= startMs` raise clear `ValueError`s.

### Hands-On Exercise

Run verifier and inspect temp output if a test fails. The JSON has `segments`, `mediaChunks`, and `providerMetadata`.

### Debugging Exercise

Failure: timestamp drift after second media chunk.

Answer: inspect `chunk.start_ms`; if it is missing or in seconds instead of milliseconds, all later citations drift.

### Theory Q/A

| Question | Answer |
| --- | --- |
| Why JSON artifacts? | Easy local inspection for MVP. |
| Why SQLite rows too? | Fast artifact lookup later. |
| Why absolute times? | Later phases share one media timeline. |
| Why keep media chunks in transcript artifact? | Debugging provider offsets. |
| Why no encryption here? | SP-01 vault encryption remains separate; this MVP stores local media artifacts. |
| Why validate before stitching? | Bad provider payloads should fail before corrupt transcript artifacts. |

### Checkpoint

- [ ] Compute `provider 250 ms + chunk 10000 ms`.
- [ ] Name transcript output directory.

### Key Takeaways

- Stitching is offset math plus provenance.
- Storage keeps JSON and metadata rows.

---

## Lesson 5: RAG-Ready Transcript Chunks

### Zero-Prerequisite Setup

RAG retrieval works better with coherent evidence units. SP-03 chunks transcript after stitching so every chunk can cite source segments and original times.

### File Map

| File | Purpose |
| --- | --- |
| `transcript_chunks/chunker.py` | Groups stitched transcript segments. |
| `schema.py` | Defines `TranscriptChunk`. |

### Code Reading

```python
TranscriptChunk(
    chunk_id="tx-1-chunk-0000",
    segment_ids=["s1", "s2"],
    start_ms=3000,
    end_ms=5000,
    boundary_reason="end-of-transcript",
    embedding_status="pending",
)
```

Chunk IDs are stable inside an artifact. `embedding_status` is `pending` because SP-05 owns embeddings.

### Hands-On Exercise

Read `assert_transcript_chunks_preserve_boundaries_and_provenance`. Notice pause between `s1` and `s2` creates separate chunks.

### Debugging Exercise

Failure: chunk text splits a normal word.

Answer: use sentence or segment boundaries first. When `max_chars` forces an internal split, preserve word boundaries where possible and mark `forced-size-limit`.

### Theory Q/A

| Question | Answer |
| --- | --- |
| Why chunk after stitching? | Retrieval chunks need final absolute timestamps. |
| Why avoid mid-sentence splits? | Retrieval loses meaning and citations feel wrong. |
| Why keep `segmentIds`? | Later answers cite source transcript. |
| Why keep `mediaArtifactId`? | Cross-phase provenance. |
| Why `embeddingStatus: pending`? | Embeddings are later phase work. |
| Why validate `max_chars`? | Zero or negative sizes would make forced splitting unsafe. |

### Checkpoint

- [ ] Find `pause_boundary_ms`.
- [ ] Explain when `forced-size-limit` appears.

### Key Takeaways

- Transcript chunks are evidence units.
- Every chunk carries citations, time, and provenance.

## Verification

```powershell
npm run verify:sp03
```

Expected:

```text
SP-03 media transcription verification passed
```

## Stop Points

| Do not build | Reason |
| --- | --- |
| Source enrichment | Later phase owns enrichment. |
| Visual understanding | SP-04 owns visual evidence. |
| Tutor answers | SP-07 owns tutor behavior. |
| Live provider call without key/sample/cost check | Could spend money or fail auth. |
