$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$bundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$pathPython = Get-Command python -ErrorAction SilentlyContinue

if ($pathPython) {
  & $pathPython.Source (Join-Path $repoRoot "scripts\verify_sp01_foundation.py")
  exit $LASTEXITCODE
}

if (Test-Path $bundledPython) {
  & $bundledPython (Join-Path $repoRoot "scripts\verify_sp01_foundation.py")
  exit $LASTEXITCODE
}

throw "Python runtime not found. Install Python or run with Codex bundled Python."

