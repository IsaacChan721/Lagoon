"""Local-only Lagoon foundation package."""

from .settings import PrivacySettings, default_privacy_settings
from .storage import EncryptionNotConfiguredError, LocalStorageBoundary, StorageLayout

__all__ = [
    "EncryptionNotConfiguredError",
    "LocalStorageBoundary",
    "PrivacySettings",
    "StorageLayout",
    "default_privacy_settings",
]

