# Lagoon MVP Build Plan

> [!IMPORTANT]
> Build and verify one learning flow only: temporary MP4 input -> extracted audio -> English transcript -> study notes -> transcript-grounded tutor chat.

## Plan Dashboard

| Item | Decision |
| --- | --- |
| Status | Planned - no application code yet |
| User | One local learner |
| Input | One MP4, maximum 2 GB and 60 minutes; temporary only, never saved as lesson data |
| Transcription | Extract mono audio locally, then send only that audio to AssemblyAI for an English plain-text transcript |
| Tutor | Local Ollama model; start with a Qwen instruct model that fits the machine |
| Data | Persist only the latest transcript, notes, and chat locally; delete temporary MP4 and audio files |
| UI | One simple local web page with loading and error states |
| Success check | A fixture reaches transcript, notes, and one grounded tutor answer |

## Quick Navigation

| Section | Purpose |
| --- | --- |
| [MVP Requirements](#mvp-requirements) | The required user-facing behavior |
| [Project Layout](#project-layout) | Where each responsibility belongs |
| [Build Slices](#build-slices) | The small, testable implementation order |
| [Definition of Done](#definition-of-done) | The MVP release gate |

## MVP Requirements

| Capability | Required behavior |
| --- | --- |
| Upload and extraction | Let the user select one local `.mp4` up to 2 GB; reject unsupported files, larger files, and videos longer than 60 minutes. Enforce the byte limit while receiving the request, not only from client-provided metadata. Write it only to a per-job temporary location using an application-generated filename, extract a 16 kHz mono MP3 with FFmpeg, then delete the temporary MP4 whether extraction succeeds or fails. |
| Transcript | Upload only the extracted audio to AssemblyAI and display the completed English transcript as plain text. Delete the local audio immediately after the upload attempt, whether it succeeds or fails; retrieve the completed transcript, then delete the AssemblyAI transcript and its associated upload. If provider deletion fails, show a cleanup failure instead of claiming completion and allow an in-session retry. No timestamps or speaker labels. |
| Notes | Create five sections from the transcript: summary, key concepts, specific details, definitions/terms, and practical takeaways. |
| Tutor chat | Accept free-form questions and answer like a teacher using only the current transcript and generated notes. State when the lesson does not support an answer. |
| Continuity | Reopen the latest completed transcript, notes, and chat after a local restart. |
| Feedback | Make the current state clear: ready, uploading, transcribing, creating notes, complete, or failed. |

> [!NOTE]
> [!NOTE]
> The MP4 is used only to make audio and is never retained as lesson data. The application and tutor run locally, but the extracted audio is sent to AssemblyAI; disclose that before upload. After Lagoon receives the transcript, it deletes the AssemblyAI transcript and associated uploaded audio. AssemblyAI documents transcript deletion and associated upload deletion for files sent to its upload endpoint. [AssemblyAI deletion documentation](https://www.assemblyai.com/docs/delete-transcripts)

## Boundaries

| In scope | Not in this MVP |
| --- | --- |
| MP4 input, temporary audio extraction, English transcription, notes, transcript-only chat, latest-lesson local persistence | YouTube, other media types, visual analysis, retained video or audio files, timestamps, speaker labels, editing, export, accounts, cloud sync, external references, quizzes, flashcards, analytics, billing, or model fine-tuning |

## Project Layout

Keep the familiar prototype split: React displays the product; Python handles local files, the transcription adapter, local storage, and Ollama calls.

```text
Lagoon/
|-- web/                 # React + TypeScript + Vite UI
|   `-- src/
|       |-- features/    # upload, transcript, notes, tutor
|       `-- api/         # local API client
|-- api/                 # Python local API
|   `-- lagoon/
|       |-- media/       # MP4 validation, FFmpeg extraction, temporary-file cleanup
|       |-- transcription/ # AssemblyAI adapter
|       |-- notes/       # structured note generation
|       |-- tutor/       # transcript chunk selection and Ollama prompt
|       `-- storage/     # latest-lesson local record
|-- tests/fixtures/      # tiny synthetic, non-sensitive samples only
|-- scripts/             # small verification commands
`-- docs/                # plans, decisions, code map, and verification notes
```

## Build Slices

Finish, test, and commit one slice before starting the next. If a later slice exposes a missing need, add it to the plan rather than quietly expanding scope.

| Slice | Deliverable | Minimum test | Keep out |
| --- | --- | --- | --- |
| 0. Foundation | Runnable Vite React UI, Python local API, health check, `.env.example`, and beginner setup README. | UI loads and reaches the local health endpoint. | Auth, deployment, database, UI polish. |
| 1. MP4 input and audio extraction | One file picker; server-side MP4, 2 GB size, and duration validation; FFmpeg extraction to compressed mono audio; cleanup on success and failure. | Accept a short MP4 fixture; reject non-MP4, over-2-GB upload, and over-limit duration; prove the temporary MP4 is deleted after extraction. | YouTube, previews, visual processing. |
| 2. Transcript | One transcription-provider interface and AssemblyAI implementation that uploads only extracted audio, returns plain English text, and deletes provider data after retrieval. | Fake-provider unit test proves audio—not MP4—is submitted, local audio is removed after upload attempt, and provider deletion is requested; documented manual smoke test with a real key. | Timestamps, labels, multi-provider support. |
| 3. Notes | Chunk long transcripts, then generate and combine five-section notes through Ollama. | Fake-model test requires all five sections from a multi-chunk transcript. | Editing, downloads, flashcards, quizzes. |
| 4. Tutor | Free-form chat that supplies relevant transcript chunks and notes to Ollama. | Test shows relevant lesson text is sent and unsupported questions are bounded. | Web search, citations, tool use, fine-tuning. |
| 5. Full flow | One-page upload-to-chat journey with persistence, loading, and error states. | Fixture smoke test completes every stage and the latest lesson restores after restart. | Multi-lesson library, accounts, cloud sync. |
| 6. Handoff | Setup, verification, limitations, and current code map documented. | A beginner follows the README and repeats the smoke test. | Hardening and new features. |

## Test Rules

- Use fake transcription and model clients in automated tests. Real API/model calls belong only in a documented manual smoke test.
- Keep test media synthetic or public and small. Never commit lectures, private transcripts, API keys, or tutor chats.
- Use a unique per-job temporary directory. Cleanup must run after every success or failure; never place original MP4s or extracted audio in local lesson storage.
- Test a service boundary as soon as it exists; do not defer all testing to the last slice.
- Add the actual verification command to the README when its tooling is created. Do not invent commands before then.

## Documentation Map

| Change | Update |
| --- | --- |
| Folder or component added | `docs/memory/` code map |
| Provider, model, or storage choice changed | `docs/decisions/` note and this plan if scope changes |
| Slice completed | `docs/run-logs/` result and beginner-facing setup/usage notes |
| Test command changed | Root README |

## Definition of Done

- [ ] A user can process one valid MP4 no larger than 2 GB and no longer than 60 minutes.
- [ ] The MP4 is deleted after audio extraction, the local audio is deleted after every upload attempt, and AssemblyAI data is deleted after transcript retrieval (or a visible cleanup failure is offered for retry).
- [ ] The English transcript and all five note sections are visible.
- [ ] The user can ask a free-form question and receive a tutor-style, lesson-grounded answer.
- [ ] Each long-running step shows progress or a useful error.
- [ ] The latest completed lesson restores locally after restart.
- [ ] Automated boundary tests and the documented end-to-end smoke test pass.
- [ ] A beginner can set up, run, and verify the MVP from the README.

## Stop Points

Do not add a queue, microservice split, vector database, custom speech-to-text engine, external-reference teaching, cloud deployment, or production hardening until this definition of done passes.

## First Implementation Step

Start Slice 0 only. Check the installed Node.js, Python, FFmpeg, and Ollama versions, then choose the smallest compatible dependencies and record any change to this plan in `docs/decisions/`.
