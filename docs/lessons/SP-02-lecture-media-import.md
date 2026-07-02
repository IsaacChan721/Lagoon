# SP-02 Lecture Media Import Lesson

> [!NOTE]
> SP-02 teaches existing-file import. It does **not** record camera/microphone input, transcribe, summarize, call providers, sync cloud data, or add encryption.

## Learning Dashboard

| Item | Details |
| --- | --- |
| Learner goal | Select an existing lecture audio/video file, preview it locally, and understand the artifact metadata Lagoon creates. |
| Main feature | Lecture Media Import |
| Phase boundary | Import and metadata only. No transcript, tutor, upload, or cloud sync. |
| Best first check | `npm run verify:sp02` |
| Follow-up checks | `npm run verify:sp01`, then `npm run build:web` |
| Time box | 45-75 minutes |

## Beginner Path

Read in this order:

1. `web/src/media-import/mediaImportState.ts`
2. `web/src/media-import/useMediaImport.ts`
3. `web/src/media-import/MediaImportPanel.tsx`
4. `api/lagoon_local/storage.py`
5. `scripts/verify_sp02_media_import.py`

Why this order: start with the data contract, then browser behavior, then UI, then durable local storage, then verification.

## Lesson Map

| Lesson | Focus | Done when |
| --- | --- | --- |
| 1 | Import mental model | You can explain what happens after the user picks a file. |
| 2 | Supported media | You can tell accepted and rejected file types apart. |
| 3 | Artifact contract | You can describe each key field in `UploadedMediaArtifact`. |
| 4 | Browser preview | You know why object URLs are temporary. |
| 5 | Storage + checks | You can verify SP-02 without breaking SP-01. |

---

## Lesson 1: Import Mental Model

### Goal

Understand the SP-02 flow from file picker to preview-ready artifact.

### Core Idea

Browser import reads a user-selected `File`. Lagoon validates the extension, creates an object URL for preview, reads duration metadata when the browser can, and displays a local artifact reference shaped like:

```text
media/<id>.<ext>
```

### Flow

| Step | Code area | Result |
| --- | --- | --- |
| User selects file | `MediaImportPanel.tsx` | Browser gives Lagoon a `File`. |
| Lagoon validates file | `mediaImportState.ts` | Extension and size decide next state. |
| Lagoon creates preview URL | `useMediaImport.ts` | `<video>` or `<audio>` can preview locally. |
| Browser reads metadata | `useMediaImport.ts` | Duration is captured when available. |
| UI displays artifact | `MediaImportPanel.tsx` | Learner sees name, type, size, duration, local reference. |
| Backend can persist artifact | `storage.py` | File can be copied into app-data `media/` and tracked in SQLite. |

> [!IMPORTANT]
> The object URL is preview-only. It is not durable storage and must be revoked when no longer needed.

### Checkpoint

- [ ] I can explain why SP-02 starts from an existing file.
- [ ] I can name the frontend hook that creates the preview.
- [ ] I can explain why `media/<id>.<ext>` is a local reference, not a cloud URL.

---

## Lesson 2: Supported Media

### Goal

Know which lecture files SP-02 accepts and why unsupported files fail early.

| Kind | Extensions |
| --- | --- |
| Video | `.mp4`, `.webm`, `.mov`, `.m4v`, `.mpeg` |
| Audio | `.mp3`, `.m4a`, `.wav`, `.mpga` |

If browser MIME type is missing, Lagoon infers type from extension and marks metadata confidence as:

```text
extension-fallback
```

### State Outcomes

| State | Meaning | Learner action |
| --- | --- | --- |
| `idle` | No file selected yet. | Choose a supported lecture file. |
| `validating` | Lagoon is checking the file. | Wait. |
| `ready` | File can be previewed. | Inspect metadata and preview. |
| `unsupported` | Extension/type not accepted. | Pick a supported media file. |
| `too-large` | File exceeds the current size rule. | Use a smaller sample. |
| `metadata-error` | Browser could not read preview metadata cleanly. | Try another file and inspect console if needed. |
| `saved` | Artifact was registered locally. | Continue to later phase workflow. |

> [!TIP]
> Extension fallback is not a failure. It means the browser did not provide enough MIME confidence, so Lagoon used the file extension.

---

## Lesson 3: Artifact Contract

### Goal

Understand the shape of imported media metadata.

`UploadedMediaArtifact` includes:

| Field | Meaning |
| --- | --- |
| `id` | Unique artifact ID. |
| `sourceType: "uploaded-file"` | Confirms this came from file import. |
| `originalName` | User-visible original filename. |
| `mimeType` | Browser-reported or inferred media type. |
| `extension` | Accepted file extension. |
| `sizeBytes` | File size. |
| `durationMs` | Duration when browser can read it. |
| `kind` | `video` or `audio`. |
| `localReference` | Durable app-style reference, like `media/<id>.mp4`. |
| `objectUrl` | Temporary browser preview URL. |
| `createdAt` | Import timestamp. |
| `metadataConfidence` | Confidence source, such as `browser` or `extension-fallback`. |

### Beginner Translation

| Question | Answer |
| --- | --- |
| Is the file uploaded? | No. SP-02 is local-first. |
| Is the file transcribed? | No. Transcript work starts later. |
| Is the object URL permanent? | No. It is only for current browser preview. |
| Is metadata useful later? | Yes. Later phases can use the artifact reference and duration. |

---

## Lesson 4: Browser Preview

### Goal

Understand preview behavior without confusing it with durable storage.

<details>
<summary>Code tour: object URL lifecycle</summary>

Look for these tokens in `web/src/media-import/useMediaImport.ts`:

```ts
URL.createObjectURL(...)
URL.revokeObjectURL(...)
loadedmetadata
objectUrlRef
```

Meaning:

- `URL.createObjectURL(...)`: gives the browser a temporary preview URL for the selected file.
- `loadedmetadata`: event used to read media metadata such as duration.
- `objectUrlRef`: remembers the current object URL.
- `URL.revokeObjectURL(...)`: releases the temporary browser URL to avoid leaks.

</details>

<details>
<summary>Code tour: preview UI</summary>

Look for these tokens in `web/src/media-import/MediaImportPanel.tsx`:

```tsx
accept={acceptedMediaInput}
<video
<audio
```

Meaning:

- `accept={acceptedMediaInput}` hints allowed file types to the browser file picker.
- `<video>` renders local video preview when `kind` is video.
- `<audio>` renders local audio preview when `kind` is audio.

</details>

### Debugging Drill

Problem: preview appears, then another file is selected, and memory usage keeps growing.

Reasoning path:

1. Object URLs reserve browser resources.
2. Old object URLs must be revoked.
3. `URL.revokeObjectURL` should run when replacing or clearing preview.

Fix:

- Restore object URL cleanup in `useMediaImport.ts`.
- Run `npm run verify:sp02`.
- Run `npm run build:web`.

---

## Lesson 5: Storage And Checks

### Goal

Verify SP-02 while proving SP-01 foundation still holds.

Durable local storage belongs to:

```python
LocalStorageBoundary.register_uploaded_media_artifact()
```

That method copies media into app-data `media/` and stores SQLite metadata.

### Visual + Audio Strategy

Transcript is primary evidence; visuals are supporting evidence unless a future phase proves visual extraction reliable and affordable.

| Future phase | Expected role |
| --- | --- |
| SP-03 | Read durable imported media artifacts, extract audio, handle provider-size chunks, transcribe with absolute timestamps, and create semantic transcript chunks. |
| SP-04 | Sample frames or slides from durable media paths and link visual evidence to transcript segments/chunks. |

Do not send whole lecture video to a multimodal model by default. Sample representative frames for budget control, and keep SP-03 transcript chunks as primary retrieval evidence.

### Checks

Run:

```powershell
npm run verify:sp02
npm run verify:sp01
npm run build:web
```

Expected result:

- [ ] SP-02 import verification passes.
- [ ] SP-01 foundation still passes.
- [ ] Web build succeeds.

### Stop Before These Features

Do not add these in SP-02:

- recording,
- transcription,
- summarization,
- provider calls,
- cloud upload,
- cloud sync,
- account login,
- encryption system work.

Those belong to later phases or post-MVP hardening.
