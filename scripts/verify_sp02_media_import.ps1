$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$pathPython = Get-Command python -ErrorAction SilentlyContinue
$bundledPython = "C:\Users\isaac\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if ($pathPython) {
  & $pathPython.Source (Join-Path $repoRoot "scripts\verify_sp02_media_import.py")
} elseif (Test-Path $bundledPython) {
  & $bundledPython (Join-Path $repoRoot "scripts\verify_sp02_media_import.py")
} else {
  throw "Python runtime not found for SP-02 verification."
}

if ($LASTEXITCODE -ne 0) {
  exit $LASTEXITCODE
}
