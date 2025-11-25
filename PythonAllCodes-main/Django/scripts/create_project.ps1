param(
    [Parameter(Mandatory=$true)][string]$Name,
    [string]$Path = "./projects",
    [switch]$WithVenv
)

$projPath = Join-Path -Path $Path -ChildPath $Name
if (Test-Path $projPath) {
    Write-Host "Project '$Name' already exists at $projPath" -ForegroundColor Yellow
    exit 1
}

New-Item -ItemType Directory -Path $projPath -Force | Out-Null

# Create basic files
$readme = "# $Name`n`nProject scaffold created by create_project.ps1`n"
$readme | Out-File -FilePath (Join-Path $projPath 'README.md') -Encoding UTF8

"# Add project-specific Python dependencies here" | Out-File -FilePath (Join-Path $projPath 'requirements.txt') -Encoding UTF8

New-Item -ItemType File -Path (Join-Path $projPath '.gitkeep') -Force | Out-Null

Write-Host "Created project at: $projPath" -ForegroundColor Green

if ($WithVenv) {
    Write-Host "To create a virtual environment, run:`n python -m venv .venv" -ForegroundColor Cyan
}
