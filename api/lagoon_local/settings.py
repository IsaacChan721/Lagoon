from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class PrivacySettings:
    local_only: bool = True
    network_enabled_for_content: bool = False
    provider_calls_enabled: bool = False
    cloud_sync_enabled: bool = False
    telemetry_enabled: bool = False
    redact_logs: bool = True

    def to_metadata(self) -> dict[str, bool]:
        return asdict(self)


def default_privacy_settings() -> PrivacySettings:
    return PrivacySettings()

