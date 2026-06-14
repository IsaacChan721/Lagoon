export type PrivacyDefaults = {
  localOnly: boolean;
  networkEnabledForContent: boolean;
  providerCallsEnabled: boolean;
  cloudSyncEnabled: boolean;
  telemetryEnabled: boolean;
  redactLogs: boolean;
};

export const privacyDefaults: PrivacyDefaults = {
  localOnly: true,
  networkEnabledForContent: false,
  providerCallsEnabled: false,
  cloudSyncEnabled: false,
  telemetryEnabled: false,
  redactLogs: true,
};

