#!/bin/bash
# crb-doc-review Skill 安装脚本 (macOS/Linux)
# 使用方式: curl -sL https://raw.githubusercontent.com/Captainf5/Agent-Skill/main/crb-doc-review/install.sh | bash
# 或: bash install.sh

SKILL_NAME="crb-doc-review"
SKILL_DIR="$HOME/.workbuddy/skills/$SKILL_NAME"
REPO_RAW="https://raw.githubusercontent.com/Captainf5/Agent-Skill/main/crb-doc-review"

echo "=== 安装 $SKILL_NAME Skill ==="

# 创建目录
mkdir -p "$SKILL_DIR"

# 下载 SKILL.md
curl -sL "$REPO_RAW/SKILL.md" -o "$SKILL_DIR/SKILL.md"

if [ -f "$SKILL_DIR/SKILL.md" ]; then
    echo "✅ 安装成功: $SKILL_DIR/SKILL.md"
    echo "⚠️ 请重启 WorkBuddy 以加载新 Skill"
else
    echo "❌ 安装失败: 无法下载 SKILL.md"
    exit 1
fi
