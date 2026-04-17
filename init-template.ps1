# init-template.ps1
# Usage: .\init-template.ps1

$docsDir = "docs"
$templateDir = "engineering-template"

if (-not (Test-Path $templateDir)) {
    Write-Host "Error: $templateDir folder not found." -ForegroundColor Red
    exit 1
}

# Remove old docs if exists
if (Test-Path $docsDir) {
    Remove-Item -Recurse -Force $docsDir
    Write-Host "Removed old $docsDir folder."
}

# Copy template
Copy-Item -Recurse $templateDir $docsDir
Write-Host "✓ Copied $templateDir to $docsDir" -ForegroundColor Green

# Create minimal _config.yml
$configYml = @"
# GitHub Pages Configuration
theme: jekyll-theme-minimal
title: Portfolio
description: My portfolio website
"@

Set-Content -Path "$docsDir\_config.yml" -Value $configYml
Write-Host "✓ Created $docsDir\_config.yml" -ForegroundColor Green

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Update content in $docsDir\"
Write-Host "  2. git add -A && git commit -m 'Initialize portfolio'"
Write-Host "  3. git push"
Write-Host "  4. Enable GitHub Pages from repo Settings (branch: main, folder: docs/)"
