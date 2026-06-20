export type MediaImportStatus =
  | "idle"
  | "validating"
  | "ready"
  | "unsupported"
  | "too-large"
  | "metadata-error"
  | "saved";

export type MediaKind = "video" | "audio";

export type MetadataConfidence = "browser" | "extension-fallback";

export type UploadedMediaArtifact = {
  id: string;
  sourceType: "uploaded-file";
  originalName: string;
  mimeType: string;
  extension: string;
  sizeBytes: number;
  durationMs: number | null;
  kind: "video" | "audio";
  localReference: string;
  objectUrl: string;
  createdAt: string;
  metadataConfidence: MetadataConfidence;
};

export type MediaImportState = {
  status: MediaImportStatus;
  message: string;
  artifact: UploadedMediaArtifact | null;
};

type SupportedMedia = {
  extension: string;
  mimeType: string;
  kind: MediaKind;
};

const supportedMedia: SupportedMedia[] = [
  { extension: ".mp4", mimeType: "video/mp4", kind: "video" },
  { extension: ".webm", mimeType: "video/webm", kind: "video" },
  { extension: ".mov", mimeType: "video/quicktime", kind: "video" },
  { extension: ".m4v", mimeType: "video/x-m4v", kind: "video" },
  { extension: ".mp3", mimeType: "audio/mpeg", kind: "audio" },
  { extension: ".m4a", mimeType: "audio/mp4", kind: "audio" },
  { extension: ".wav", mimeType: "audio/wav", kind: "audio" },
  { extension: ".mpeg", mimeType: "video/mpeg", kind: "video" },
  { extension: ".mpga", mimeType: "audio/mpeg", kind: "audio" },
];

export const acceptedMediaInput = supportedMedia.map((item) => item.extension).join(",");
export const maxPreviewBytes = 1024 * 1024 * 1024;

export const initialMediaImportState: MediaImportState = {
  status: "idle",
  message: "Choose an existing lecture audio or video file.",
  artifact: null,
};

export function describeSupportedExtensions(): string {
  return supportedMedia.map((item) => item.extension).join(", ");
}

export function inspectSupportedFile(file: File) {
  const originalName = file.name || "lecture-media";
  const extension = extensionFromName(originalName);
  const support = supportedMedia.find((item) => item.extension === extension);

  if (!support) {
    return null;
  }

  const mimeType = file.type || support.mimeType;
  const metadataConfidence: MetadataConfidence = file.type ? "browser" : "extension-fallback";

  return {
    originalName,
    extension,
    mimeType,
    kind: support.kind,
    metadataConfidence,
  };
}

export function createUploadedMediaArtifact(params: {
  file: File;
  objectUrl: string;
  durationMs: number | null;
}): UploadedMediaArtifact | null {
  const support = inspectSupportedFile(params.file);
  if (!support) {
    return null;
  }

  const id = crypto.randomUUID();

  return {
    id,
    sourceType: "uploaded-file",
    originalName: support.originalName,
    mimeType: support.mimeType,
    extension: support.extension,
    sizeBytes: params.file.size,
    durationMs: params.durationMs,
    kind: support.kind,
    localReference: `media/${id}${support.extension}`,
    objectUrl: params.objectUrl,
    createdAt: new Date().toISOString(),
    metadataConfidence: support.metadataConfidence,
  };
}

function extensionFromName(name: string): string {
  const dotIndex = name.lastIndexOf(".");
  if (dotIndex < 0) {
    return "";
  }

  return name.slice(dotIndex).toLowerCase();
}
