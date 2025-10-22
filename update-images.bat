@echo off
REM CALFEM Documentation Image Update Batch Script
REM This script updates PNG image references to SVG with conditional sizing

echo CALFEM Documentation Image Update
echo ===================================
echo.

REM Check if PowerShell is available
powershell -Command "Write-Host 'PowerShell is available'" >nul 2>&1
if errorlevel 1 (
    echo ERROR: PowerShell is required but not available
    echo Please ensure PowerShell is installed and accessible
    pause
    exit /b 1
)

echo Choose an option:
echo 1. Preview changes (no files modified)
echo 2. Apply changes to RST files
echo 3. Exit
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo Running in PREVIEW mode...
    powershell -ExecutionPolicy Bypass -File "%~dp0update-images.ps1" -WhatIf
) else if "%choice%"=="2" (
    echo.
    echo Applying changes to files...
    powershell -ExecutionPolicy Bypass -File "%~dp0update-images.ps1"
) else if "%choice%"=="3" (
    echo Exiting...
    exit /b 0
) else (
    echo Invalid choice. Please run the script again.
)

echo.
pause