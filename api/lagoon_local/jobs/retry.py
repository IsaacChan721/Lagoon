from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar


T = TypeVar("T")
FailureKind = str


def classify_transcription_error(message: str) -> FailureKind:
    lowered = message.lower()
    if "401" in lowered or "403" in lowered or "api key" in lowered or "auth" in lowered:
        return "auth"
    if "quota" in lowered or "billing" in lowered or "429" in lowered:
        return "quota"
    if "payload" in lowered or "too large" in lowered or "413" in lowered:
        return "payload"
    if "connection" in lowered or "timeout" in lowered or "network" in lowered:
        return "network"
    if "codec" in lowered or "format" in lowered or "decode" in lowered:
        return "codec"
    return "unknown"


def should_retry(failure_kind: FailureKind, attempt: int, max_attempts: int) -> bool:
    return failure_kind in {"network", "unknown"} and attempt < max_attempts


def run_with_retry(operation: Callable[[], T], max_attempts: int = 3) -> T:
    attempt = 1
    while True:
        try:
            return operation()
        except Exception as exc:
            failure_kind = classify_transcription_error(str(exc))
            if not should_retry(failure_kind, attempt, max_attempts):
                raise
            attempt += 1
