$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$bundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if (Get-Command python -ErrorAction SilentlyContinue) {
    python "$repoRoot\scripts\verify_sp03_transcription.py"
} elseif (Test-Path $bundledPython) {
    & $bundledPython "$repoRoot\scripts\verify_sp03_transcription.py"
} else {
    throw "Python not found on PATH and bundled Codex Python is missing."
}
