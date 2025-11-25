param(
    [string]$ProjectPath = '.',
    [string]$VenvName = '.venv'
)

if (-not (Test-Path "$ProjectPath\requirements.txt")) {
    Write-Host "requirements.txt not found in $ProjectPath" -ForegroundColor Yellow
    exit 1
}

python -m venv $VenvName
. .$VenvName\Scripts\Activate.ps1
pip install -r requirements.txt

Write-Host "Environment setup complete. Run: python manage.py runserver" -ForegroundColor Green
