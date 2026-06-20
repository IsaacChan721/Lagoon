# SP-02 Lecture Media Import Lesson

## Beginner Path

SP-02 lets a user select an existing lecture audio/video file, preview it locally, and create metadata that later phases can use. It does not transcribe, summarize, call providers, sync to cloud, or add encryption.

## Core Idea

Browser import reads a user-selected `File`. Lagoon validates the extension, creates an object URL for preview, reads duration metadata when the browser can, and displays a local artifact reference shaped like `media/<id>.<ext>`.

## Supported Media

- Video: `.mp4`, `.webm`, `.mov`, `.m4v`, `.mpeg`
- Audio: `.mp3`, `.m4a`, `.wav`, `.mpga`

If browser MIME type is missing, Lagoon infers type from extension and marks metadata confidence as `extension-fallback`.

## Files

- `web/src/media-import/mediaImportState.ts`
- `web/src/media-import/useMediaImport.ts`
- `web/src/media-import/MediaImportPanel.tsx`
- `api/lagoon_local/storage.py`
- `scripts/verify_sp02_media_import.py`

## Artifact Contract

`UploadedMediaArtifact` includes:

- `id`
- `sourceType: "uploaded-file"`
- `originalName`
- `mimeType`
- `extension`
- `sizeBytes`
- `durationMs`
- `kind`
- `localReference`
- `objectUrl`
- `createdAt`
- `metadataConfidence`

The object URL is for browser preview only. Durable local storage belongs to `LocalStorageBoundary.register_uploaded_media_artifact()`, which copies media into app-data `media/` and stores SQLite metadata.

## Visual + Audio Strategy

Transcript is primary evidence; visuals are supporting evidence unless a future phase proves visual extraction reliable and affordable. SP-03 should extract/transcribe audio with timestamps. SP-04 should sample frames or slides and link them to transcript segments.

Do not send whole lecture video to a multimodal model by default. Sample representative frames for budget control.

## Checks

Run:

```powershell
npm run verify:sp02
npm run verify:sp01
npm run build:web
```

Expected result: SP-02 import verification passes, SP-01 foundation still passes, and web build succeeds.
