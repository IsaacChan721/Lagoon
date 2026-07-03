# lagoon_local

## Purpose

Python package for local privacy defaults and persistence boundary.

## Contains

- `__init__.py`
- `settings.py`
- `storage.py`
- `media/`
- `transcription/`
- `transcript_chunks/`
- `jobs/`

## Key Files

- `settings.py`
- `storage.py`
- `media/audio.py`
- `transcription/pipeline.py`
- `transcript_chunks/chunker.py`
- `jobs/retry.py`

## Interfaces

- `default_privacy_settings()`
- `LocalStorageBoundary.ensure_layout()`
- `LocalStorageBoundary.write_content_blob()`
- `LocalStorageBoundary.save_media_artifact()`
- `LocalStorageBoundary.register_uploaded_media_artifact()`
- `normalize_audio_for_transcription()`
- `transcribe_media_artifact()`
- `build_transcript_chunks()`

## Dependencies

- `dataclasses`
- `pathlib`
- `sqlite3`

## Tests

- `npm run verify:sp01`
- `npm run verify:sp02`
- `npm run verify:sp03`

## Gotchas

- `write_content_blob` raises as a safety placeholder.
- SP-02 media artifact writes are allowed to local-only `media/` and SQLite metadata; no cloud or provider path.
- SP-03 transcript artifact writes are local JSON plus SQLite metadata; live provider path remains gated.

## Last Updated

SP-03
