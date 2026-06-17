# SP-02 Video + Audio Capture Lesson

## Beginner Path

This lesson explains the SP-02 capture slice only: browser permission, recording lifecycle, and local-only media handoff. It does not teach transcription, summarization, RAG, tutoring, providers, accounts, cloud sync, or encryption.

## Lesson 1: Browser Capture Basics

### Zero-Prerequisite Setup, 5-10 Minutes

Browser capture means a web page asks the browser for camera and microphone access. The browser, not the app, owns the permission prompt. User can allow, deny, or ignore it.

Terms:

- `navigator.mediaDevices`: browser object that exposes media devices.
- `getUserMedia`: browser function that asks for camera/microphone streams.
- `MediaStream`: live audio/video tracks returned after permission is granted.
- Permission denial: browser says no access, usually with `NotAllowedError`.

Files touched:

- `web/src/capture/useMediaCapture.ts`
- `web/src/capture/CapturePanel.tsx`
- `web/src/capture/captureState.ts`

Why care: denied permission is normal. App must recover instead of freezing.

### File Map, 10-15 Minutes

- `web/src/capture/useMediaCapture.ts`: owns permission request and recorder actions.
- `web/src/capture/CapturePanel.tsx`: owns buttons and visible status.
- `web/src/capture/captureState.ts`: owns state names and local artifact metadata shape.
- `web/src/app/LagoonShell.tsx`: places capture panel in app shell.

Must not own:

- Transcription.
- Summary.
- RAG.
- Provider calls.
- Cloud upload.

### Line-By-Line Code Reading, 15-25 Minutes

Core request:

```ts
const stream = await navigator.mediaDevices.getUserMedia({
  audio: true,
  video: true,
});
```

Line notes:

- `const stream`: stores successful browser media result.
- `await`: waits until user grants permission or browser rejects.
- `navigator.mediaDevices.getUserMedia`: asks browser for media devices.
- `{ audio: true, video: true }`: requests both microphone and camera.

Denied branch:

```ts
if (errorName === "NotAllowedError" || errorName === "SecurityError") {
  setState({
    ...initialCaptureState,
    status: "permission-denied",
    message: "Camera or microphone permission was denied.",
  });
  return;
}
```

Line notes:

- `errorName`: browser error type.
- `NotAllowedError`: common denied-permission result.
- `SecurityError`: browser/security context blocked capture.
- `status: "permission-denied"`: visible recoverable app state.
- `return`: stop before recorder setup.

### Guided Hands-On Exercise, 15-25 Minutes

Run:

```powershell
npm run verify:sp02
```

Expected output:

```text
SP-02 capture verification passed
```

If output says missing capture files, inspect:

```powershell
Get-ChildItem web\src\capture
```

Expected files:

```text
captureState.ts
CapturePanel.tsx
useMediaCapture.ts
```

### Debugging Or Design Exercise, 10-20 Minutes

Failure: user clicks Start and denies permission. App still shows `requesting-permission`.

Diagnosis path:

1. Check browser error branch in `startCapture`.
2. Confirm `NotAllowedError` maps to `permission-denied`.
3. Confirm `CapturePanel` renders `state.message`.
4. Confirm Start button is enabled again when status is `permission-denied`.

Answer: missing or wrong denied branch leaves UI stuck. Fix by setting `permission-denied` and allowing retry.

### Theory Q/A, 10-15 Minutes

Q: Why does browser ask permission before capture?
A: Camera and microphone are sensitive. User must control access.

Q: Why handle denial first?
A: Denial is common. Clean recovery makes app usable.

Q: Why request audio and video together?
A: SP-02 goal is combined lecture capture.

Q: Why no provider call after permission?
A: SP-02 is local-only capture, not upload or transcription.

Q: Why not hide permission errors?
A: User needs visible state and retry path.

### Checkpoint, 5-10 Minutes

Task: find all capture statuses.

Acceptance:

- You can point to `CaptureStatus` in `captureState.ts`.
- You can explain `permission-denied` vs `interrupted`.

### Key Takeaways, 5 Minutes

- Permission is browser-owned.
- Denial is normal.
- Capture code must keep UI recoverable.

## Lesson 2: Recording Lifecycle

### Zero-Prerequisite Setup, 5-10 Minutes

A recording lifecycle is the list of states a recording can move through. Clear states prevent race bugs.

Terms:

- `MediaRecorder`: browser API that turns a stream into chunks.
- Chunk: piece of recorded media data.
- Blob: browser object holding recorded bytes.
- Pause/resume: recorder can temporarily stop adding chunks without ending session.

Files touched:

- `web/src/capture/captureState.ts`
- `web/src/capture/useMediaCapture.ts`
- `web/src/capture/CapturePanel.tsx`

### File Map, 10-15 Minutes

- `captureState.ts`: state names and initial state.
- `useMediaCapture.ts`: transitions between states.
- `CapturePanel.tsx`: enables/disables controls based on state.

State order:

```text
idle -> requesting-permission -> recording -> paused -> recording -> stopped -> saving -> saved
```

Failure states:

```text
permission-denied
interrupted
```

### Line-By-Line Code Reading, 15-25 Minutes

State type:

```ts
export type CaptureStatus =
  | "idle"
  | "requesting-permission"
  | "recording"
  | "paused"
  | "stopped"
  | "saving"
  | "saved"
  | "permission-denied"
  | "interrupted";
```

Line notes:

- `export type`: lets other files use exact state names.
- Each string is one allowed UI state.
- TypeScript rejects typo states.

Pause:

```ts
recorder.pause();
setState((current) => ({
  ...current,
  status: "paused",
  message: "Recording paused.",
}));
```

Line notes:

- `recorder.pause()`: tells browser recorder to pause.
- `setState`: updates React UI.
- `...current`: keeps other metadata.
- `status: "paused"`: control buttons now change.

Stop:

```ts
recorder.requestData();
recorder.stop();
```

Line notes:

- `requestData()`: asks recorder to flush current data.
- `stop()`: ends recording and later triggers `onstop`.

### Guided Hands-On Exercise, 15-25 Minutes

Run:

```powershell
npm run build:web
```

Expected:

```text
built
```

Then inspect controls:

```powershell
Select-String -Path web\src\capture\CapturePanel.tsx -Pattern "Start|Pause|Resume|Stop|Save"
```

Expected: each control label appears.

### Debugging Or Design Exercise, 10-20 Minutes

Failure: Save button is active while recording.

Diagnosis path:

1. Open `CapturePanel.tsx`.
2. Find `isStopped`.
3. Confirm Save button has `disabled={!isStopped}`.

Answer: Save should only enable after recorder stops and Blob exists. Saving while recording can produce empty or partial metadata.

### Theory Q/A, 10-15 Minutes

Q: Why use explicit state strings?
A: They make valid transitions visible and testable.

Q: Why not one boolean like `isRecording`?
A: One boolean cannot distinguish paused, stopped, saving, denied, and interrupted.

Q: Why request data before stop?
A: It helps flush latest chunks before final Blob creation.

Q: Why clean up tracks?
A: Camera/microphone should turn off when recording ends.

Q: Why show interrupted separately?
A: Device/API failures differ from user denial.

### Checkpoint, 5-10 Minutes

Task: explain when `Stop` is enabled.

Acceptance:

- `Stop` enabled during `recording` or `paused`.
- `Stop` disabled after `stopped`, `saved`, `permission-denied`, or `interrupted`.

### Key Takeaways, 5 Minutes

- Lifecycle states prevent confusing button behavior.
- Recorder stop is asynchronous.
- Cleanup matters for privacy and device release.

## Lesson 3: Local Media Handoff

### Zero-Prerequisite Setup, 5-10 Minutes

Local media handoff means captured bytes and metadata stay on this machine. SP-02 does not transcribe or upload media. It prepares a stable reference for later local phases.

Terms:

- Local reference: path-like metadata such as `media/<id>.webm`.
- Metadata: small facts about media, like MIME type and duration.
- App data root: user-local folder outside repo.
- SQLite: local file database used for metadata.

Files touched:

- `web/src/capture/captureState.ts`
- `api/lagoon_local/storage.py`
- `.gitignore`
- `scripts/verify_sp02_capture.py`

### File Map, 10-15 Minutes

- `captureState.ts`: browser artifact metadata shape.
- `storage.py`: local app-data `media/` directory and `media_artifacts` table.
- `.gitignore`: prevents raw media from entering Git.
- `verify_sp02_capture.py`: checks both browser contract and Python storage handoff.

Must not own:

- Encryption.
- Cloud sync.
- Transcript creation.
- Provider calls.

### Line-By-Line Code Reading, 15-25 Minutes

Browser artifact:

```ts
return {
  id,
  kind: "browser-capture",
  mimeType,
  durationMs: params.durationMs,
  sizeBytes: params.blob.size,
  createdAt: new Date().toISOString(),
  localReference: `media/${id}.${extension}`,
  downloadName: `lagoon-capture-${id}.${extension}`,
  objectUrl: params.objectUrl,
};
```

Line notes:

- `id`: unique capture id.
- `kind`: says where artifact came from.
- `mimeType`: tells later code how bytes are encoded.
- `durationMs`: recording length.
- `sizeBytes`: blob size.
- `createdAt`: timestamp.
- `localReference`: stable local path-like reference.
- `downloadName`: suggested filename for browser save.
- `objectUrl`: temporary browser URL for download.

Python storage:

```python
artifact = boundary.save_media_artifact(
    content=b"fake-webm",
    mime_type="video/webm",
    duration_ms=1234,
)
```

Line notes:

- `content`: bytes to write locally.
- `mime_type`: stored in SQLite metadata.
- `duration_ms`: stored for later phases.
- Return value includes `local_path`.

### Guided Hands-On Exercise, 15-25 Minutes

Run:

```powershell
npm run verify:sp02
```

Then inspect media ignore rules:

```powershell
Select-String -Path .gitignore -Pattern "media/|*.webm"
```

Expected:

```text
media/
*.webm
```

### Debugging Or Design Exercise, 10-20 Minutes

Failure: `save_media_artifact` writes file into repo folder.

Diagnosis path:

1. Check `LocalStorageBoundary(Path(tmp))` in verifier.
2. Check `layout.media_dir`.
3. Confirm `artifact.local_path.parent == layout.media_dir`.
4. Confirm path starts with `layout.root`.

Answer: media must live under app-data root, not repo. Repo must only contain source, docs, and tests.

### Theory Q/A, 10-15 Minutes

Q: Why store metadata separately from bytes?
A: Later phases can find media without reading large files.

Q: Why ignore `*.webm`?
A: Raw lecture capture should not accidentally enter Git.

Q: Why no encryption here?
A: MVP contract says local-only files and clear boundaries; encryption is out of SP-02 scope.

Q: Why no transcript row?
A: Transcription starts in SP-03 or later, not capture.

Q: Why browser download plus Python save function?
A: Browser cannot directly write app-data safely without a local bridge. Python boundary shows approved local-only handoff for later integration.

### Checkpoint, 5-10 Minutes

Task: explain SP-02 artifact path.

Acceptance:

- Browser metadata uses `media/<id>.webm`.
- Python storage writes under app-data `media/`.
- No cloud or provider path exists.

### Key Takeaways, 5 Minutes

- SP-02 output is local media artifact metadata and bytes.
- Repo ignores raw media.
- Later phases can consume local references without changing capture contract.

## Sufficiency Review

SP-02 is sufficient when:

- Capture permission flow exists.
- Start, pause, resume, stop, save, and reset controls exist.
- Denied and interrupted states are visible.
- Browser handoff metadata has stable local reference.
- Python local storage can persist media artifact bytes and metadata.
- Verification passes.
