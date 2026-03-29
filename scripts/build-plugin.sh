#!/usr/bin/env bash
set -euo pipefail

# Build script for Dvar Torah Plugin
# Canonical source is plugins/dvar-torah-plugin (no src mirroring).

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
PLUGIN_DIR="$ROOT_DIR/plugins/dvar-torah-plugin"
PLUGIN_MANIFEST="$PLUGIN_DIR/.claude-plugin/plugin.json"
PACKAGE_JSON="$ROOT_DIR/package.json"

echo "=== Building Dvar Torah Plugin ==="

if [ ! -f "$PLUGIN_MANIFEST" ]; then
  echo "ERROR: Missing plugin manifest at $PLUGIN_MANIFEST" >&2
  exit 1
fi

echo "Canonical plugin root: $PLUGIN_DIR"

if command -v jq &> /dev/null; then
  PLUGIN_VERSION="$(jq -r '.version' "$PLUGIN_MANIFEST")"
  PACKAGE_VERSION="$(jq -r '.version' "$PACKAGE_JSON")"
  echo "Plugin version:  $PLUGIN_VERSION"
  echo "Package version: $PACKAGE_VERSION"

  if [ "$PLUGIN_VERSION" != "$PACKAGE_VERSION" ]; then
    echo "Version mismatch detected; syncing package.json to plugin version..."
    jq --arg v "$PLUGIN_VERSION" '.version = $v' "$PACKAGE_JSON" > /tmp/package.json.tmp
    mv /tmp/package.json.tmp "$PACKAGE_JSON"
    echo "Synced package.json to $PLUGIN_VERSION"
  fi
else
  echo "WARNING: jq not installed; skipping version consistency check."
fi

echo ""
echo "=== Build complete ==="
echo "Plugin root: $PLUGIN_DIR"
echo ""
echo "Skills:"
ls -1 "$PLUGIN_DIR/skills/"
echo ""
echo "Agents:"
ls -1 "$PLUGIN_DIR/agents/"
echo ""
echo "Commands:"
ls -1 "$PLUGIN_DIR/commands/"
