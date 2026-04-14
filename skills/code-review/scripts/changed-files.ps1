param(
    [string]$BaseRef = "origin/main"
)

$files = git diff --name-only $BaseRef...HEAD
if (-not $files) {
    Write-Output "No changed files detected."
    exit 0
}

$files | ForEach-Object { Write-Output $_ }
