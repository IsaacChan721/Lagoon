import { useEffect, useRef, useState } from "react";
import {
  MediaImportState,
  createUploadedMediaArtifact,
  describeSupportedExtensions,
  initialMediaImportState,
  inspectSupportedFile,
  maxPreviewBytes,
} from "./mediaImportState";

export function useMediaImport() {
  const [state, setState] = useState<MediaImportState>(initialMediaImportState);
  const objectUrlRef = useRef<string | null>(null);

  useEffect(() => {
    return () => {
      cleanupObjectUrl();
    };
  }, []);

  function cleanupObjectUrl() {
    if (objectUrlRef.current) {
      URL.revokeObjectURL(objectUrlRef.current);
      objectUrlRef.current = null;
    }
  }

  async function importFile(file: File | null) {
    cleanupObjectUrl();

    if (!file) {
      setState(initialMediaImportState);
      return;
    }

    setState({
      status: "validating",
      message: "Validating lecture media.",
      artifact: null,
    });

    const support = inspectSupportedFile(file);
    if (!support) {
      setState({
        status: "unsupported",
        message: `Unsupported file. Use ${describeSupportedExtensions()}.`,
        artifact: null,
      });
      return;
    }

    const objectUrl = URL.createObjectURL(file);
    objectUrlRef.current = objectUrl;

    if (file.size > maxPreviewBytes) {
      const artifact = createUploadedMediaArtifact({
        file,
        objectUrl,
        durationMs: null,
      });

      setState({
        status: "too-large",
        message: "File is large. Metadata saved; SP-03 owns chunking and upload-limit handling.",
        artifact,
      });
      return;
    }

    const durationMs = await loadDurationMs(objectUrl, support.kind);
    const artifact = createUploadedMediaArtifact({
      file,
      objectUrl,
      durationMs,
    });

    setState({
      status: durationMs === null ? "metadata-error" : "ready",
      message:
        durationMs === null
          ? "Preview ready, but browser could not read duration metadata."
          : "Lecture media ready for local preview.",
      artifact,
    });
  }

  function saveArtifact() {
    if (!state.artifact) {
      return;
    }

    setState((current) => ({
      ...current,
      status: "saved",
      message: "Local media artifact contract ready for SP-03.",
    }));
  }

  function resetImport() {
    cleanupObjectUrl();
    setState(initialMediaImportState);
  }

  return {
    state,
    importFile,
    saveArtifact,
    resetImport,
  };
}

function loadDurationMs(objectUrl: string, kind: "video" | "audio"): Promise<number | null> {
  return new Promise((resolve) => {
    const element = kind === "video" ? document.createElement("video") : document.createElement("audio");
    let resolved = false;

    function finish(durationMs: number | null) {
      if (resolved) {
        return;
      }
      resolved = true;
      element.removeEventListener("loadedmetadata", handleLoadedMetadata);
      element.removeEventListener("error", handleError);
      element.removeAttribute("src");
      element.load();
      resolve(durationMs);
    }

    function handleLoadedMetadata() {
      const durationSeconds = element.duration;
      if (!Number.isFinite(durationSeconds)) {
        finish(null);
        return;
      }
      finish(Math.max(0, Math.round(durationSeconds * 1000)));
    }

    function handleError() {
      finish(null);
    }

    element.preload = "metadata";
    element.addEventListener("loadedmetadata", handleLoadedMetadata);
    element.addEventListener("error", handleError);
    element.src = objectUrl;
  });
}
