param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot
)

$dirs = @(
    "src",
    "tests",
    "docs",
    ".github/workflows"
)

foreach ($dir in $dirs) {
    $path = Join-Path $ProjectRoot $dir
    New-Item -ItemType Directory -Force -Path $path | Out-Null
}

$gitkeepTargets = @(
    "src/.gitkeep",
    "tests/.gitkeep",
    "docs/.gitkeep"
)

foreach ($target in $gitkeepTargets) {
    $path = Join-Path $ProjectRoot $target
    if (-not (Test-Path $path)) {
        New-Item -ItemType File -Path $path | Out-Null
    }
}

Write-Output "Initialized scaffold at $ProjectRoot"
