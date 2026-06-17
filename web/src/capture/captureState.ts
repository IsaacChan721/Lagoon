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

export type LocalMediaArtifact = {
  id: string;
  kind: "browser-capture";
  mimeType: string;
  durationMs: number;
  sizeBytes: number;
  createdAt: string;
  localReference: string;
  downloadName: string;
  objectUrl: string;
};

export type CaptureState = {
  status: CaptureStatus;
  message: string;
  startedAt: number | null;
  durationMs: number;
  mimeType: string;
  artifact: LocalMediaArtifact | null;
};

export const initialCaptureState: CaptureState = {
  status: "idle",
  message: "Camera and microphone are off.",
  startedAt: null,
  durationMs: 0,
  mimeType: "video/webm",
  artifact: null,
};

export function createLocalMediaArtifact(params: {
  blob: Blob;
  durationMs: number;
  objectUrl: string;
}): LocalMediaArtifact {
  const id = crypto.randomUUID();
  const mimeType = params.blob.type || "video/webm";
  const extension = mimeType.includes("mp4") ? "mp4" : "webm";

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
}

export function captureInterrupted(message = "Recording was interrupted."): CaptureState {
  return {
    ...initialCaptureState,
    status: "interrupted",
    message,
  };
}
