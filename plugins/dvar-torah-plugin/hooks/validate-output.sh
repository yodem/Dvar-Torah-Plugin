#!/usr/bin/env bash
# PostToolUse hook: validate dvar torah output on Write tool calls.
# Reads the tool_use event from stdin (JSON).
# Exit 0 = allow. Exit 2 = block (print JSON reason to stdout).

set -euo pipefail

# Read stdin — the tool result event
INPUT=$(cat)

# Extract the file path written (Claude Code PostToolUse passes tool_input.file_path)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null || true)

# Only validate files written to output/divrei-torah/
if [[ -z "$FILE_PATH" ]] || [[ "$FILE_PATH" != *"output/divrei-torah"* ]]; then
  exit 0
fi

# Check file exists and is readable
if [[ ! -f "$FILE_PATH" ]]; then
  exit 0
fi

CONTENT=$(cat "$FILE_PATH")
ERRORS=()

# 1. Must have a title (# heading)
if ! echo "$CONTENT" | grep -qE '^# '; then
  ERRORS+=("missing title (no # heading)")
fi

# 2. Must have a sources / מראי מקומות section
if ! echo "$CONTENT" | grep -qiE '## מראי מקומות|## Sources|## Bibliography|## מקורות'; then
  ERRORS+=("missing sources section (## מראי מקומות or ## Sources)")
fi

# 3. Must have YAML frontmatter
if ! echo "$CONTENT" | head -1 | grep -q '^---'; then
  ERRORS+=("missing YAML frontmatter")
fi

# 4. Check Hebrew characters are present (basic UTF-8 encoding sanity)
if ! echo "$CONTENT" | grep -qP '[\x{0590}-\x{05FF}]' 2>/dev/null; then
  # fallback: check for common Hebrew patterns
  if ! echo "$CONTENT" | grep -qE 'רמב|תורה|תלמוד|מקרא|פרשה|דבר'; then
    ERRORS+=("no Hebrew text detected — possible encoding issue")
  fi
fi

if [[ ${#ERRORS[@]} -gt 0 ]]; then
  ERROR_MSG=$(printf '%s; ' "${ERRORS[@]}")
  echo "{\"decision\": \"block\", \"reason\": \"Dvar torah output validation failed: ${ERROR_MSG}\"}"
  exit 2
fi

exit 0
