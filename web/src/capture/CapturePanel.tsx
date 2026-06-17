import { useMediaCapture } from "./useMediaCapture";

export function CapturePanel() {
  const {
    state,
    videoRef,
    startCapture,
    pauseCapture,
    resumeCapture,
    stopCapture,
    saveCapture,
    resetCapture,
  } = useMediaCapture();

  const isRecording = state.status === "recording";
  const isPaused = state.status === "paused";
  const isStopped = state.status === "stopped";
  const canStart =
    state.status === "idle" ||
    state.status === "permission-denied" ||
    state.status === "interrupted" ||
    state.status === "saved";

  return (
    <section className="capture-panel" aria-labelledby="capture-title">
      <div className="capture-copy">
        <p className="eyebrow">Capture</p>
        <h2 id="capture-title">Video + Audio</h2>
        <p className="capture-message" data-status={state.status}>
          {state.message}
        </p>
      </div>

      <div className="capture-preview" aria-label="Camera preview">
        <video ref={videoRef} muted playsInline />
        <span>{state.status}</span>
      </div>

      <div className="capture-controls" aria-label="Recording controls">
        <button type="button" onClick={startCapture} disabled={!canStart}>
          Start
        </button>
        <button type="button" onClick={pauseCapture} disabled={!isRecording}>
          Pause
        </button>
        <button type="button" onClick={resumeCapture} disabled={!isPaused}>
          Resume
        </button>
        <button type="button" onClick={stopCapture} disabled={!isRecording && !isPaused}>
          Stop
        </button>
        <button type="button" onClick={saveCapture} disabled={!isStopped}>
          Save
        </button>
        <button type="button" onClick={resetCapture}>
          Reset
        </button>
      </div>

      {state.artifact ? (
        <dl className="artifact-card" aria-label="Local media artifact">
          <div>
            <dt>Reference</dt>
            <dd>{state.artifact.localReference}</dd>
          </div>
          <div>
            <dt>Duration</dt>
            <dd>{state.artifact.durationMs} ms</dd>
          </div>
          <div>
            <dt>MIME</dt>
            <dd>{state.artifact.mimeType}</dd>
          </div>
          <a href={state.artifact.objectUrl} download={state.artifact.downloadName}>
            Download local media
          </a>
        </dl>
      ) : null}
    </section>
  );
}
