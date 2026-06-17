import { useEffect, useRef, useState } from "react";
import {
  CaptureState,
  captureInterrupted,
  createLocalMediaArtifact,
  initialCaptureState,
} from "./captureState";

function pickRecorderMimeType() {
  if (typeof MediaRecorder === "undefined") {
    return "video/webm";
  }

  for (const mimeType of ["video/webm;codecs=vp9,opus", "video/webm"]) {
    if (MediaRecorder.isTypeSupported(mimeType)) {
      return mimeType;
    }
  }

  return "video/webm";
}

export function useMediaCapture() {
  const [state, setState] = useState<CaptureState>(initialCaptureState);
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const recorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<BlobPart[]>([]);
  const stoppedBlobRef = useRef<Blob | null>(null);
  const objectUrlRef = useRef<string | null>(null);
  const startedAtRef = useRef<number | null>(null);
  const durationRef = useRef(0);

  useEffect(() => {
    return () => {
      cleanupObjectUrl();
      stopTracks();
    };
  }, []);

  function cleanupObjectUrl() {
    if (objectUrlRef.current) {
      URL.revokeObjectURL(objectUrlRef.current);
      objectUrlRef.current = null;
    }
  }

  function stopTracks() {
    streamRef.current?.getTracks().forEach((track) => track.stop());
    streamRef.current = null;
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
  }

  async function startCapture() {
    if (!navigator.mediaDevices?.getUserMedia || typeof MediaRecorder === "undefined") {
      setState(captureInterrupted("Browser capture is not supported here."));
      return;
    }

    cleanupObjectUrl();
    stoppedBlobRef.current = null;
    chunksRef.current = [];
    durationRef.current = 0;
    startedAtRef.current = performance.now();
    setState({
      ...initialCaptureState,
      status: "requesting-permission",
      message: "Waiting for camera and microphone permission.",
    });

    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
        video: true,
      });
      const mimeType = pickRecorderMimeType();
      const recorder = new MediaRecorder(stream, { mimeType });

      streamRef.current = stream;
      recorderRef.current = recorder;
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        await videoRef.current.play();
      }

      recorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          chunksRef.current.push(event.data);
        }
      };
      recorder.onerror = () => {
        stopTracks();
        setState(captureInterrupted("Recording device failed while active."));
      };
      recorder.onstop = () => {
        const durationMs = Math.max(0, Math.round(performance.now() - (startedAtRef.current ?? performance.now())));
        durationRef.current = durationMs;
        stoppedBlobRef.current = new Blob(chunksRef.current, { type: recorder.mimeType });
        stopTracks();
        setState({
          status: "stopped",
          message: "Recording stopped. Save local handoff when ready.",
          startedAt: null,
          durationMs,
          mimeType: recorder.mimeType,
          artifact: null,
        });
      };

      recorder.start();
      setState({
        status: "recording",
        message: "Recording camera and microphone locally.",
        startedAt: startedAtRef.current,
        durationMs: 0,
        mimeType,
        artifact: null,
      });
    } catch (error) {
      stopTracks();
      const errorName = error instanceof DOMException ? error.name : "";
      if (errorName === "NotAllowedError" || errorName === "SecurityError") {
        setState({
          ...initialCaptureState,
          status: "permission-denied",
          message: "Camera or microphone permission was denied.",
        });
        return;
      }
      setState(captureInterrupted("Capture request was interrupted before recording."));
    }
  }

  function pauseCapture() {
    const recorder = recorderRef.current;
    if (!recorder || recorder.state !== "recording") {
      return;
    }

    recorder.pause();
    setState((current) => ({
      ...current,
      status: "paused",
      message: "Recording paused.",
    }));
  }

  function resumeCapture() {
    const recorder = recorderRef.current;
    if (!recorder || recorder.state !== "paused") {
      return;
    }

    recorder.resume();
    setState((current) => ({
      ...current,
      status: "recording",
      message: "Recording resumed.",
    }));
  }

  function stopCapture() {
    const recorder = recorderRef.current;
    if (!recorder || recorder.state === "inactive") {
      setState(captureInterrupted("Recording stopped before media was ready."));
      return;
    }

    recorder.requestData();
    recorder.stop();
  }

  function saveCapture() {
    const blob = stoppedBlobRef.current;
    if (!blob) {
      setState(captureInterrupted("No stopped recording is ready to save."));
      return;
    }

    setState((current) => ({
      ...current,
      status: "saving",
      message: "Preparing local media handoff.",
    }));
    cleanupObjectUrl();
    const objectUrl = URL.createObjectURL(blob);
    objectUrlRef.current = objectUrl;
    const artifact = createLocalMediaArtifact({
      blob,
      durationMs: durationRef.current,
      objectUrl,
    });

    setState({
      status: "saved",
      message: "Local media handoff is ready. Save file to local Lagoon media folder.",
      startedAt: null,
      durationMs: artifact.durationMs,
      mimeType: artifact.mimeType,
      artifact,
    });
  }

  function resetCapture() {
    cleanupObjectUrl();
    stoppedBlobRef.current = null;
    chunksRef.current = [];
    durationRef.current = 0;
    setState(initialCaptureState);
  }

  return {
    state,
    videoRef,
    startCapture,
    pauseCapture,
    resumeCapture,
    stopCapture,
    saveCapture,
    resetCapture,
  };
}
