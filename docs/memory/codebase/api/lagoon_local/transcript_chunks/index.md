# api/lagoon_local/transcript_chunks

> [!NOTE]
> Transcript chunks are semantic evidence units for later RAG, not provider upload chunks.

## Dashboard

| Item | Details |
| --- | --- |
| Real path | `C:\Users\isaac\Documents\Projects\Lagoon\api\lagoon_local\transcript_chunks\` |
| Main file | `chunker.py` |
| Phase | `SP-03` |
| Downstream | `SP-05` embeddings and retrieval. |

## Public Interface

| Function | Purpose |
| --- | --- |
| `build_transcript_chunks(...)` | Groups stitched transcript segments by pause, sentence/segment size, and forced size limits. |

## Contract

- Every chunk keeps `mediaArtifactId`, `transcriptArtifactId`, `segmentIds`, `startMs`, `endMs`, `boundaryReason`, and `embeddingStatus`.
- Sentence/segment/pause boundaries are preferred.
- Mid-sentence splitting only happens when `max_chars` forces it; word boundaries are preserved when possible, and such chunks use `forced-size-limit`.
- `max_chars` must be positive and `pause_boundary_ms` cannot be negative.

## Gotchas

- Embeddings stay `pending`; SP-05 owns embedding generation.
- Forced splits preserve source segment IDs but time range remains whole source segment in MVP.
