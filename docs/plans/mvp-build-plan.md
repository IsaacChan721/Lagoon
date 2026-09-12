# Lagoon MVP Build Plan

> [!IMPORTANT]
> Build one local learning flow before adding features: upload one MP4, produce an English transcript, turn it into study notes, and chat with a tutor that uses only that lesson's material.

## Plan Dashboard

| Item | Decision |
| --- | --- |
| Status | Planned — no application code yet |
| User outcome | A learner can understand and ask questions about one uploaded lecture video |
| Supported input | One MP4 video, up to 60 minutes |
| Speech-to-text | English transcription through an existing transcription API (initial choice: AssemblyAI) |
| Teaching model | Local Ollama model; begin with a Qwen instruct model sized for the machine |
| Storage | Local-only storage for the latest completed lesson and its chat session |
| Interface | Minimal local web UI; function before visual polish |
| Primary check | An end-to-end fixture can reach transcript, notes, and a grounded chat answer |

## Quick Navigation

| Section | Best for |
| --- | --- |
| [MVP Contract](#mvp-contract) | Understanding exactly what will ship |
| [Proposed Layout](#proposed-layout) | Finding code and durable project knowledge |
| [Build Slices](#build-slices) | Implementing one small, testable part at a time |
| [Testing Strategy](#testing-strategy) | Knowing what each slice must prove |
| [Definition of Done](#definition-of-done) | Deciding whether the MVP is ready |
| [Stop Points](#stop-points) | Avoiding scope creep |

---

## MVP Contract

### In scope

| Capability | Minimum behavior |
| --- | --- |
| Video input | Select one `.mp4` from the local computer and reject unsupported files or videos longer than 60 minutes. |
| Transcription | Send the selected media to the configured transcription API and show the completed English transcript as plain text. |
| Learning notes | Generate five sections: broad summary, key concepts, specific details, definitions/terms, and practical takeaways. |
| Tutor chat | Accept free-form questions and answer as a teacher using only the current transcript and generated notes. |
| Local continuity | Restore the most recently completed lesson after a local app restart. |
| UI feedback | Show clear upload, processing, success, and error states. A simple loading indicator is sufficient. |

### Out of scope

| Not in this MVP | Why it waits |
| --- | --- |
| YouTube URLs or other video formats | MP4 removes source and compatibility complexity. |
| Visual/video understanding | The MVP learns from audio/transcript content only. |
| Timestamps, speaker labels, transcript editing, or export | They do not prove the core learning loop. |
| Accounts, cloud deployment, multi-user history, or sync | The first version is local and single-user. |
| External web references | Tutor answers must remain grounded in the selected lesson. |
| Quizzes, flashcards, citations, analytics, polished design, or billing | Useful future ideas, but not required for a working tutor. |
| Model fine-tuning or "training" | A clear system prompt and transcript grounding are sufficient for the MVP. |

### Important assumptions to validate before implementation

| Assumption | How to validate | Owner |
| --- | --- | --- |
| The chosen transcription API accepts MP4 uploads up to the desired size/duration. | Read current provider limits and run a short test upload. | Implementation slice 2 |
| The computer can run Ollama and a useful Qwen instruct model. | Install/run a small test prompt and record available memory. | Implementation slice 0 |
| A one-hour transcript fits the tutor workflow. | Split the transcript into small chunks and retrieve only relevant chunks per question. | Implementation slice 4 |
| Local persistence is enough for the first user. | Restore the latest lesson after restart. | Implementation slice 5 |

---

## Proposed Layout

The former prototype's easy-to-follow split remains: React handles the screen; Python owns media, API calls, local storage, and model orchestration. No framework, database, or deployment platform is required before the corresponding slice proves it is useful.

```text
Lagoon/
|-- web/                    # Vite + React + TypeScript user interface
|   |-- src/
|   |   |-- app/            # Page shell and app-level state
|   |   |-- features/       # upload/, transcript/, notes/, tutor/
|   |   `-- api/            # Small typed client for the local Python API
|   `-- tests/              # UI behavior tests
|-- api/                    # Python local API
|   |-- lagoon/             # Application package
|   |   |-- media/          # MP4 validation and duration inspection
|   |   |-- transcription/  # Provider adapter and transcription workflow
|   |   |-- notes/          # Note-generation prompts and validation
|   |   |-- tutor/          # Chunk retrieval and grounded chat prompts
|   |   `-- storage/        # Latest-lesson local persistence
|   `-- tests/              # API and service tests
|-- tests/fixtures/         # Small synthetic media/transcript fixtures only
|-- scripts/                # One-command, phase-scoped verification scripts
`-- docs/                   # Durable project knowledge; no secrets or user media
    |-- plans/              # Build plans and phase contracts
    |-- decisions/          # Architecture/provider decisions
    |-- lessons/            # Beginner-readable completion notes
    |-- memory/             # Folder/component maps for future agents
    `-- run-logs/           # Concise verification results
```

### Stack choices

| Layer | Initial choice | Why it is appropriate now |
| --- | --- | --- |
| Web UI | React, TypeScript, Vite | Matches the former prototype and stays small for a local UI. |
| Local API | Python | Clear standard-library-friendly path for files, local storage, and provider calls. |
| Transcription | AssemblyAI adapter | Existing hosted transcription avoids building speech recognition ourselves. Keep the provider behind one adapter so it can change later. |
| Tutor model | Ollama + Qwen instruct | Free to run locally after download; no per-answer API charge. |
| Lesson storage | A small local JSON or SQLite record | Enough for the latest lesson without prematurely creating a library system. |
| Tests | Python service tests, React UI tests, and a single end-to-end smoke test | Catches mistakes at the smallest useful layer. |

> [!NOTE]
> The transcription request is not fully local because it uses a hosted API. The app and tutor remain local; only media sent to the transcription provider leaves the machine. This must be clearly disclosed in the UI before upload.

---

## Build Slices

Each slice is small enough to build, test, explain, and commit independently. Do not begin a later slice until the previous slice's acceptance checklist passes.

| Slice | Goal | Main folders | Required proof | Do not add yet |
| --- | --- | --- | --- | --- |
| 0. Foundation | Create runnable local web/API skeleton and configuration template. | `web/`, `api/`, `docs/`, `scripts/` | Both processes start; health endpoint and blank page load. | Auth, deployment, database schema, UI polish. |
| 1. MP4 import | Accept one MP4 and inspect its duration. | `web/src/features/upload/`, `api/lagoon/media/` | Valid short fixture is accepted; non-MP4 and over-60-minute metadata are rejected. | YouTube, drag-and-drop enhancements, video previews. |
| 2. Transcription | Submit valid media, wait for English transcript, and return plain text. | `api/lagoon/transcription/`, `web/src/features/transcript/` | Mocked provider test plus a documented manual provider smoke test succeed. | Timestamps, speaker diarization, multi-provider routing. |
| 3. Notes | Convert the transcript into the five agreed learning-note sections. | `api/lagoon/notes/`, `web/src/features/notes/` | Deterministic fake-model test validates all five sections; manual local-model sample is readable. | Editing, downloads, flashcards, quizzes. |
| 4. Tutor chat | Answer a question using retrieved transcript chunks and notes only. | `api/lagoon/tutor/`, `web/src/features/tutor/` | Test proves the prompt includes relevant lesson text and declines unsupported claims. | Web search, citations, tool use, model fine-tuning. |
| 5. Full local flow | Connect the UI, persistence, loading/error states, and reset/replace behavior. | `web/src/app/`, `api/lagoon/storage/` | A fixture flows from upload to chat and the latest lesson reopens after restart. | Multi-lesson library, accounts, cloud sync. |
| 6. MVP handoff | Document setup, test results, limitations, and next candidates. | `README.md`, `docs/`, `scripts/` | A beginner can follow setup and repeat the full smoke test. | Production hardening and new features. |

### Slice 0: Foundation

#### Tasks

- [ ] Add a root README with local prerequisites, setup, and the exact start commands.
- [ ] Create the Vite React TypeScript app under `web/`.
- [ ] Create a minimal Python HTTP API under `api/` with a health check.
- [ ] Add `.env.example` files with names only, never real keys.
- [ ] Add one verification command for the web page and API health check.

#### Acceptance criteria

- [ ] A beginner can start both parts using documented commands.
- [ ] No API key is committed.
- [ ] The UI can reach the local API health endpoint.

### Slice 1: MP4 Import

#### Tasks

- [ ] Build one file-picker control and display the selected filename.
- [ ] Validate the `.mp4` extension/type and inspect actual media duration on the API side.
- [ ] Enforce the 60-minute maximum with a plain-language error.
- [ ] Replace any previous unfinished upload when a new file is selected.

#### Acceptance criteria

- [ ] A valid MP4 below the limit reaches the API.
- [ ] Invalid input produces a useful error without calling transcription.
- [ ] The original media is not retained after processing unless explicitly needed for the current session.

### Slice 2: Transcription

#### Tasks

- [ ] Define one `TranscriptionProvider` interface and an AssemblyAI implementation.
- [ ] Add configuration validation that explains when the provider key is missing.
- [ ] Submit media, poll or await completion, and map success/failure to simple statuses.
- [ ] Return only normalized English transcript text to the rest of the app.

#### Acceptance criteria

- [ ] Provider calls are mocked in automated tests.
- [ ] A real manual smoke test is documented separately and uses no committed media or key.
- [ ] Provider errors are visible to the user in plain language.

### Slice 3: Learning Notes

#### Tasks

- [ ] Define a structured note result with exactly five named sections.
- [ ] Chunk long transcripts before local-model processing.
- [ ] Ask the local model to preserve both major concepts and smaller specific details.
- [ ] Validate that all five sections have usable content before returning notes.

#### Acceptance criteria

- [ ] Notes are generated only from the transcript.
- [ ] The UI presents all five sections without requiring editing controls.
- [ ] An empty or failed model result yields an actionable error, not silently incomplete notes.

### Slice 4: Transcript-Grounded Tutor

#### Tasks

- [ ] Store each transcript chunk with a stable local ID.
- [ ] Retrieve a small set of relevant chunks for every question using a simple, inspectable method first.
- [ ] Send retrieved text, notes, and a teaching instruction to Ollama.
- [ ] Instruct the model to say it cannot answer when the lesson does not support an answer.

#### Acceptance criteria

- [ ] The model is told not to invent facts beyond the supplied lesson material.
- [ ] The app handles an unavailable Ollama service with setup guidance.
- [ ] A question unrelated to the transcript receives a bounded, honest response.

### Slice 5: Full Local Flow

#### Tasks

- [ ] Connect upload → transcription → notes → chat in one screen.
- [ ] Use simple state labels such as `Uploading`, `Transcribing`, `Creating notes`, and `Ready`.
- [ ] Persist only the latest successful lesson, notes, and chat locally.
- [ ] Provide a clear "start over" action that replaces the local lesson.

#### Acceptance criteria

- [ ] A new user can complete the workflow without reading source code.
- [ ] Restarting the local app restores the latest completed lesson.
- [ ] Starting over removes the previous local lesson record through a deliberate, visible action.

---

## Testing Strategy

| Layer | Test type | Example case | When it runs |
| --- | --- | --- | --- |
| Media validation | Unit test | Reject `.mov`; reject 60:01; accept a short MP4 fixture. | Slice 1 and later |
| Provider adapter | Unit test with fake provider | Map a completed job to plain English transcript text. | Slice 2 and later |
| Notes | Unit test with fake model | Require all five note sections. | Slice 3 and later |
| Tutor grounding | Unit/integration test with fake model | Relevant chunks are passed; unsupported question is bounded. | Slice 4 and later |
| Web UI | Component test | State label and error message change at each stage. | Relevant UI slice |
| Whole flow | Local smoke test | Fixture upload reaches transcript, notes, and one tutor answer. | Slice 5 and release |

### Fixture rules

- Use tiny synthetic MP4s or public, non-sensitive samples only.
- Keep large media out of Git; document where a local manual sample belongs instead.
- Never commit a real lecture, transcript, provider key, or tutor conversation.

### Verification convention

Every completed slice will add its exact command to the root README and record the result in `docs/run-logs/`. The final command names are deliberately undecided until the actual test tooling exists; do not invent commands before the foundation is created.

---

## Definition of Done

- [ ] A local user selects a valid MP4 no longer than 60 minutes.
- [ ] The app creates and displays an English transcript through the configured provider.
- [ ] The app displays all five agreed note sections.
- [ ] The user can ask free-form questions and receives tutor-style answers grounded only in the current lesson.
- [ ] A clear loading or error state is shown for each long-running operation.
- [ ] The latest completed lesson survives a local restart.
- [ ] Automated tests cover each service boundary; a manual end-to-end smoke test is documented and passes.
- [ ] Setup, known limitations, privacy disclosure, and verification commands are explained for a beginner.

## Project Knowledge Maintenance

| When this changes | Update this documentation |
| --- | --- |
| A folder or component is added | `docs/memory/` folder/component map |
| A provider, model, or storage choice changes | `docs/decisions/` decision note and this plan if scope changes |
| A slice is completed | A beginner lesson in `docs/lessons/` and a result in `docs/run-logs/` |
| A test command changes | Root README and the relevant slice documentation |
| MVP scope changes | This plan before implementation continues |

## Stop Points

| Do not build | Reason |
| --- | --- |
| A complex microservice, queue, or background-job system | One local user and one active lesson do not need it. |
| A general-purpose vector database | Start with transparent chunk retrieval; introduce more only if tests show it is necessary. |
| A custom transcription engine | The MVP deliberately uses a mature API. |
| Any external-reference teaching feature | It would break the clear transcript-only answer boundary. |
| Production security, scale, cloud, billing, or team features | They are separate decisions after the core loop works. |

## First Implementation Handoff

Begin with Slice 0 only. Before writing application code, verify the available Python, Node.js, package-manager, FFmpeg/FFprobe, and Ollama installations; then choose the smallest compatible dependencies and record them in a decision note.
