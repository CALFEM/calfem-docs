# PowerShell script to update PNG image references to SVG with conditional sizing
# Usage: .\update-images.ps1

param(
    [string]$SourceDir = "source",
    [switch]$WhatIf = $false
)

# Function to update a single RST file
function Update-RstFile {
    param(
        [string]$FilePath,
        [switch]$WhatIf
    )
    
    $lines = Get-Content $FilePath
    $newLines = @()
    $changed = $false
    $i = 0
    
    while ($i -lt $lines.Count) {
        $line = $lines[$i]
        
        # Check if this line contains a PNG figure reference
        if ($line -match '(\s*)\.\.( figure:: images/[^.\s]+)\.png\s*$') {
            $indent = $matches[1]
            $imagePath = $matches[2]
            
            # Replace with conditional SVG block
            $newLines += "$indent.. only:: html"
            $newLines += "$indent    "
            $newLines += "$indent    .. figure:: $imagePath.svg"
            $newLines += "$indent        :align: center"
            $newLines += "$indent        :width: 400px"
            $newLines += "$indent"
            $newLines += "$indent.. only:: latex"
            $newLines += "$indent    "
            $newLines += "$indent    .. figure:: $imagePath.svg"
            $newLines += "$indent        :align: center"
            $newLines += "$indent        :width: 70%"
            
            $changed = $true
            
            # Skip the next few lines if they contain :width: or :align: directives
            $i++
            while ($i -lt $lines.Count -and $lines[$i] -match '^\s*:(width|align):') {
                $i++
            }
            continue
        }
        
        $newLines += $line
        $i++
    }
    
    if ($changed) {
        if ($WhatIf) {
            Write-Host "Would update: $FilePath" -ForegroundColor Yellow
        } else {
            Set-Content -Path $FilePath -Value $newLines
            Write-Host "Updated: $FilePath" -ForegroundColor Green
        }
        return $true
    }
    
    return $false
}

# Main script
Write-Host "CALFEM Documentation Image Update Script" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

if ($WhatIf) {
    Write-Host "PREVIEW MODE - No files will be modified" -ForegroundColor Yellow
    Write-Host ""
}

$sourceDir = Join-Path $PSScriptRoot $SourceDir
if (-not (Test-Path $sourceDir)) {
    Write-Error "Source directory not found: $sourceDir"
    exit 1
}

# Find all RST files in source directory
$rstFiles = Get-ChildItem -Path $sourceDir -Filter "*.rst" -Recurse | Where-Object {
    $_.Directory.Name -eq "source"    # Only process files directly in source folder
}

Write-Host "Found $($rstFiles.Count) RST files to process" -ForegroundColor Blue
Write-Host ""

$updatedCount = 0
$totalFiles = $rstFiles.Count

foreach ($file in $rstFiles) {
    $progress = [math]::Round(($updatedCount / $totalFiles) * 100, 1)
    Write-Progress -Activity "Updating RST files" -Status "$progress% Complete" -PercentComplete $progress
    
    # Check if file contains PNG references
    $content = Get-Content $file.FullName -Raw
    if ($content -match 'figure:: images/[^.]+\.png') {
        if (Update-RstFile -FilePath $file.FullName -WhatIf:$WhatIf) {
            $updatedCount++
        }
    }
}

Write-Progress -Activity "Updating RST files" -Completed

Write-Host ""
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "--------" -ForegroundColor Cyan
Write-Host "Files processed: $totalFiles"
if ($WhatIf) {
    Write-Host "Files that would be updated: $updatedCount" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "To actually update files, run without -WhatIf parameter:" -ForegroundColor White
    Write-Host ".\update-images.ps1" -ForegroundColor Gray
} else {
    Write-Host "Files updated: $updatedCount" -ForegroundColor Green
    if ($updatedCount -gt 0) {
        Write-Host ""
        Write-Host "Image references have been updated!" -ForegroundColor Green
        Write-Host "- PNG references changed to SVG" -ForegroundColor White
        Write-Host "- Added conditional sizing for HTML (400px) and LaTeX (70%)" -ForegroundColor White
    }
}

Write-Host ""
Write-Host "Note: Make sure your SVG files exist in the images/ directory" -ForegroundColor Yellow