import { privacyDefaults } from "./privacyDefaults";
import { storageBoundary } from "./storageBoundary";

const settings = [
  ["Local data", privacyDefaults.localOnly ? "On" : "Off"],
  ["Content network", privacyDefaults.networkEnabledForContent ? "On" : "Off"],
  ["Provider calls", privacyDefaults.providerCallsEnabled ? "On" : "Off"],
  ["Cloud sync", privacyDefaults.cloudSyncEnabled ? "On" : "Off"],
  ["Telemetry", privacyDefaults.telemetryEnabled ? "On" : "Off"],
  ["Log redaction", privacyDefaults.redactLogs ? "On" : "Off"],
] as const;

export function LagoonShell() {
  return (
    <main className="lagoon-shell">
      <section className="workspace-panel" aria-labelledby="workspace-title">
        <div className="workspace-copy">
          <p className="eyebrow">Lagoon</p>
          <h1 id="workspace-title">Local Lecture Workspace</h1>
          <p className="workspace-status">Ready for local metadata. Vault locked.</p>
        </div>
        <dl className="boundary-list" aria-label="Storage boundary">
          <div>
            <dt>Mode</dt>
            <dd>{storageBoundary.mode}</dd>
          </div>
          <div>
            <dt>Metadata</dt>
            <dd>{storageBoundary.metadata}</dd>
          </div>
          <div>
            <dt>Vault</dt>
            <dd>{storageBoundary.vault}</dd>
          </div>
          <div>
            <dt>Upload</dt>
            <dd>{storageBoundary.contentUploadDefault}</dd>
          </div>
        </dl>
      </section>

      <section className="settings-panel" aria-labelledby="settings-title">
        <h2 id="settings-title">Privacy Defaults</h2>
        <div className="settings-grid">
          {settings.map(([label, value]) => (
            <div className="setting-row" key={label}>
              <span>{label}</span>
              <strong data-state={value.toLowerCase()}>{value}</strong>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}

