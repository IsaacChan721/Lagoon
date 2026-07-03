from __future__ import annotations

import re

from lagoon_local.transcription.schema import TranscriptChunk, TranscriptSegment


SENTENCE_PATTERN = re.compile(r"[^.!?]+[.!?](?:\s+|$)|[^.!?]+$")


def build_transcript_chunks(
    lecture_id: str,
    media_artifact_id: str,
    transcript_artifact_id: str,
    segments: list[TranscriptSegment],
    max_chars: int = 1_200,
    pause_boundary_ms: int = 1_500,
) -> list[TranscriptChunk]:
    chunks: list[TranscriptChunk] = []
    current: list[TranscriptSegment] = []

    def flush(boundary_reason: str) -> None:
        if not current:
            return
        chunks.append(_make_chunk(chunks, lecture_id, media_artifact_id, transcript_artifact_id, current, boundary_reason))
        current.clear()

    for segment in sorted(segments, key=lambda item: item.start_ms):
        if len(segment.text) > max_chars:
            flush("size-limit")
            chunks.extend(
                _split_oversized_segment(
                    len(chunks),
                    lecture_id,
                    media_artifact_id,
                    transcript_artifact_id,
                    segment,
                    max_chars,
                )
            )
            continue

        if current:
            previous = current[-1]
            pause_ms = segment.start_ms - previous.end_ms
            projected_text = " ".join([*(item.text for item in current), segment.text])
            if pause_ms >= pause_boundary_ms:
                flush("pause-boundary")
            elif len(projected_text) > max_chars:
                flush("sentence-boundary")

        current.append(segment)

    flush("end-of-transcript")
    return chunks


def _make_chunk(
    existing_chunks: list[TranscriptChunk],
    lecture_id: str,
    media_artifact_id: str,
    transcript_artifact_id: str,
    segments: list[TranscriptSegment],
    boundary_reason: str,
) -> TranscriptChunk:
    speakers = sorted({segment.speaker for segment in segments if segment.speaker})
    return TranscriptChunk(
        chunk_id=f"{transcript_artifact_id}-chunk-{len(existing_chunks):04d}",
        lecture_id=lecture_id,
        media_artifact_id=media_artifact_id,
        transcript_artifact_id=transcript_artifact_id,
        segment_ids=[segment.segment_id for segment in segments],
        start_ms=segments[0].start_ms,
        end_ms=segments[-1].end_ms,
        text=" ".join(segment.text for segment in segments).strip(),
        boundary_reason=boundary_reason,
        embedding_status="pending",
        provider_metadata={"chunker": "sentence-pause-segment-v1"},
        speaker_labels=speakers,
    )


def _split_oversized_segment(
    start_index: int,
    lecture_id: str,
    media_artifact_id: str,
    transcript_artifact_id: str,
    segment: TranscriptSegment,
    max_chars: int,
) -> list[TranscriptChunk]:
    sentence_parts = [part.strip() for part in SENTENCE_PATTERN.findall(segment.text) if part.strip()]
    if not sentence_parts:
        sentence_parts = [segment.text]

    chunks: list[TranscriptChunk] = []
    buffer = ""
    for sentence in sentence_parts:
        if len(sentence) > max_chars:
            if buffer:
                chunks.append(_text_chunk(start_index + len(chunks), lecture_id, media_artifact_id, transcript_artifact_id, segment, buffer, "sentence-boundary"))
                buffer = ""
            for index in range(0, len(sentence), max_chars):
                chunks.append(
                    _text_chunk(
                        start_index + len(chunks),
                        lecture_id,
                        media_artifact_id,
                        transcript_artifact_id,
                        segment,
                        sentence[index : index + max_chars].strip(),
                        "forced-size-limit",
                    )
                )
        elif not buffer:
            buffer = sentence
        elif len(f"{buffer} {sentence}") <= max_chars:
            buffer = f"{buffer} {sentence}"
        else:
            chunks.append(_text_chunk(start_index + len(chunks), lecture_id, media_artifact_id, transcript_artifact_id, segment, buffer, "sentence-boundary"))
            buffer = sentence
    if buffer:
        chunks.append(_text_chunk(start_index + len(chunks), lecture_id, media_artifact_id, transcript_artifact_id, segment, buffer, "end-of-segment"))
    return chunks


def _text_chunk(
    index: int,
    lecture_id: str,
    media_artifact_id: str,
    transcript_artifact_id: str,
    segment: TranscriptSegment,
    text: str,
    boundary_reason: str,
) -> TranscriptChunk:
    speaker_labels = [segment.speaker] if segment.speaker else []
    return TranscriptChunk(
        chunk_id=f"{transcript_artifact_id}-chunk-{index:04d}",
        lecture_id=lecture_id,
        media_artifact_id=media_artifact_id,
        transcript_artifact_id=transcript_artifact_id,
        segment_ids=[segment.segment_id],
        start_ms=segment.start_ms,
        end_ms=segment.end_ms,
        text=text,
        boundary_reason=boundary_reason,
        embedding_status="pending",
        provider_metadata={"chunker": "sentence-pause-segment-v1"},
        speaker_labels=speaker_labels,
    )
