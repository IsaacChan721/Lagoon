import { ChangeEvent } from "react";
import { acceptedMediaInput } from "./mediaImportState";
import { useMediaImport } from "./useMediaImport";

export function MediaImportPanel() {
  const { state, importFile, saveArtifact, resetImport } = useMediaImport();
  const artifact = state.artifact;

  function handleFileChange(event: ChangeEvent<HTMLInputElement>) {
    void importFile(event.currentTarget.files?.[0] ?? null);
    event.currentTarget.value = "";
  }

  return (
    <section className="media-import-panel" aria-labelledby="media-import-title">
      <div className="media-import-copy">
        <p className="eyebrow">Import</p>
        <h2 id="media-import-title">Lecture Media</h2>
        <p className="media-import-message" data-status={state.status}>
          {state.message}
        </p>
      </div>

      <label className="file-picker">
        <span>Select lecture file</span>
        <input type="file" accept={acceptedMediaInput} onChange={handleFileChange} />
      </label>

      <div className="media-preview" data-empty={!artifact} aria-label="Lecture media preview">
        {artifact?.kind === "video" ? (
          <video controls src={artifact.objectUrl} />
        ) : artifact?.kind === "audio" ? (
          <audio controls src={artifact.objectUrl} />
        ) : (
          <span>{state.status}</span>
        )}
      </div>

      <div className="media-import-controls">
        <button type="button" onClick={saveArtifact} disabled={!artifact || state.status === "saved"}>
          Save Artifact
        </button>
        <button type="button" onClick={resetImport}>
          Reset
        </button>
      </div>

      {artifact ? (
        <dl className="artifact-card" aria-label="Uploaded media artifact">
          <div>
            <dt>Reference</dt>
            <dd>{artifact.localReference}</dd>
          </div>
          <div>
            <dt>Name</dt>
            <dd>{artifact.originalName}</dd>
          </div>
          <div>
            <dt>Kind</dt>
            <dd>{artifact.kind}</dd>
          </div>
          <div>
            <dt>MIME</dt>
            <dd>{artifact.mimeType}</dd>
          </div>
          <div>
            <dt>Size</dt>
            <dd>{formatBytes(artifact.sizeBytes)}</dd>
          </div>
          <div>
            <dt>Duration</dt>
            <dd>{artifact.durationMs === null ? "Unknown" : `${artifact.durationMs} ms`}</dd>
          </div>
          <div>
            <dt>Source</dt>
            <dd>{artifact.sourceType}</dd>
          </div>
          <div>
            <dt>Confidence</dt>
            <dd>{artifact.metadataConfidence}</dd>
          </div>
        </dl>
      ) : null}
    </section>
  );
}

function formatBytes(sizeBytes: number): string {
  if (sizeBytes < 1024) {
    return `${sizeBytes} B`;
  }

  if (sizeBytes < 1024 * 1024) {
    return `${(sizeBytes / 1024).toFixed(1)} KB`;
  }

  return `${(sizeBytes / (1024 * 1024)).toFixed(1)} MB`;
}
