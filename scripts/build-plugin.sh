#!/usr/bin/env bash
set -euo pipefail

# Build script for Dvar Torah Plugin
# Copies source files to plugins/ output directory

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
SRC_DIR="$ROOT_DIR/src"
PLUGIN_DIR="$ROOT_DIR/plugins/dvar-torah-plugin"

echo "=== Building Dvar Torah Plugin ==="

# Ensure output directories exist
mkdir -p "$PLUGIN_DIR/skills"
mkdir -p "$PLUGIN_DIR/agents"
mkdir -p "$PLUGIN_DIR/commands"
mkdir -p "$PLUGIN_DIR/.claude-plugin"

# Copy skills
echo "Copying skills..."
for skill_dir in "$SRC_DIR/skills"/*/; do
  skill_name="$(basename "$skill_dir")"
  echo "  - $skill_name"
  rm -rf "$PLUGIN_DIR/skills/$skill_name"
  cp -r "$skill_dir" "$PLUGIN_DIR/skills/$skill_name"
done

# Copy agents
echo "Copying agents..."
for agent_file in "$SRC_DIR/agents"/*.md; do
  agent_name="$(basename "$agent_file")"
  echo "  - $agent_name"
  cp "$agent_file" "$PLUGIN_DIR/agents/$agent_name"
done

# Copy settings
if [ -f "$SRC_DIR/settings/dvar-torah-plugin.settings.json" ]; then
  echo "Copying settings..."
  cp "$SRC_DIR/settings/dvar-torah-plugin.settings.json" "$PLUGIN_DIR/settings.json"
fi

# Sync version from manifest to plugin.json
if command -v jq &> /dev/null; then
  MANIFEST_VERSION=$(jq -r '.version' "$ROOT_DIR/manifests/dvar-torah-plugin.json")
  echo "Syncing version: $MANIFEST_VERSION"
  jq --arg v "$MANIFEST_VERSION" '.version = $v' "$PLUGIN_DIR/.claude-plugin/plugin.json" > /tmp/plugin.json.tmp
  mv /tmp/plugin.json.tmp "$PLUGIN_DIR/.claude-plugin/plugin.json"
fi

echo ""
echo "=== Build complete ==="
echo "Plugin output: $PLUGIN_DIR"
echo ""
echo "Skills:"
ls -1 "$PLUGIN_DIR/skills/"
echo ""
echo "Agents:"
ls -1 "$PLUGIN_DIR/agents/"
echo ""
echo "Commands:"
ls -1 "$PLUGIN_DIR/commands/"
