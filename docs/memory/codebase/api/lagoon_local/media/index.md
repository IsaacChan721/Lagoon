# api/lagoon_local/media

> [!NOTE]
> Media helpers convert durable SP-02 media artifacts into backend-safe audio inputs.

## Dashboard

| Item | Details |
| --- | --- |
| Real path | `C:\Users\isaac\Documents\Projects\Lagoon\api\lagoon_local\media\` |
| Main file | `audio.py` |
| Phase | `SP-03` |
| Verification | `npm run verify:sp03` |

## Public Interface

| Function/Class | Purpose |
| --- | --- |
| `normalize_audio_for_transcription(storage_boundary, media_artifact_id)` | Loads durable media artifact, copies audio files to temp transcription audio, or extracts video audio with `ffmpeg`. |
| `NormalizedAudio` | Records original media ID, source path, audio path, MIME type, duration, and boundary reason. |
| `MediaArtifactNotFoundError` | Unknown or missing durable artifact. |
| `AudioExtractionUnavailableError` | Video needs `ffmpeg` but unavailable. |

## Gotchas

- Browser `blob:` URLs are rejected.
- Audio files are copied into app-data temp path for provider upload.
- Video extraction is MVP-gated on local `ffmpeg`; no visual understanding occurs.
