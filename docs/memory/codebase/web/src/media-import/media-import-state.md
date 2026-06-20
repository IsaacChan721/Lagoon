# mediaImportState.ts

## Purpose

Defines SP-02 import statuses, supported media formats, metadata confidence, and `UploadedMediaArtifact`.

## Real Code Path

`C:\Users\isaac\Documents\Projects\Lagoon\web\src\media-import\mediaImportState.ts`

## Owns

- `MediaImportStatus`
- `UploadedMediaArtifact`
- `acceptedMediaInput`
- `inspectSupportedFile()`
- `createUploadedMediaArtifact()`

## Gotchas

- Missing browser MIME type falls back to extension and marks `metadataConfidence: "extension-fallback"`.
- `objectUrl` is preview-only; durable storage is Python local boundary.

## Last Updated

SP-02 Lecture Media Import
