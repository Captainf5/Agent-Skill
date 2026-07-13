@echo off
REM crb-doc-review Skill 安装脚本 (Windows)
REM 使用方式: 在 CMD 或 PowerShell 中运行 install.bat

set SKILL_NAME=crb-doc-review
set SKILL_DIR=%USERPROFILE%\.workbuddy\skills\%SKILL_NAME%
set REPO_RAW=https://raw.githubusercontent.com/Captainf5/Agent-Skill/main/crb-doc-review

echo === 安装 %SKILL_NAME% Skill ===

REM 创建目录
if not exist "%SKILL_DIR%" mkdir "%SKILL_DIR%"

REM 下载 SKILL.md
powershell -Command "Invoke-WebRequest -Uri '%REPO_RAW%/SKILL.md' -OutFile '%SKILL_DIR%\SKILL.md'" 2>nul

if exist "%SKILL_DIR%\SKILL.md" (
    echo ✅ 安装成功: %SKILL_DIR%\SKILL.md
    echo ⚠️ 请重启 WorkBuddy 以加载新 Skill
) else (
    echo ❌ 安装失败: 无法下载 SKILL.md
    exit /b 1
)
