#!/usr/bin/env bash
# Stop hook: verify that at least one output file was saved in output/divrei-torah/.
# Called at the end of a session/turn. If the session was writing a dvar torah,
# this ensures the file was actually saved.
# Exit 0 = allow. Exit 2 = block (print JSON reason to stdout).

set -euo pipefail

# Read the stop event from stdin
INPUT=$(cat)

# Check if this stop event is from a dvar-torah session.
# We look for "dvar-torah" in the transcript or session context.
SESSION_CONTEXT=$(echo "$INPUT" | jq -r '.session_context // .transcript // empty' 2>/dev/null || true)

# Only enforce file-save check if this was a dvar-torah writing session.
# Look for torah-writer agent or dvar-torah command in context.
if ! echo "$SESSION_CONTEXT" | grep -qiE 'torah-writer|dvar-torah|divrei.torah'; then
  exit 0
fi

# Find the repo root by looking for output/divrei-torah from common locations
SEARCH_DIRS=(
  "output/divrei-torah"
  "../output/divrei-torah"
  "../../output/divrei-torah"
)

OUTPUT_DIR=""
for dir in "${SEARCH_DIRS[@]}"; do
  if [[ -d "$dir" ]]; then
    OUTPUT_DIR="$dir"
    break
  fi
done

if [[ -z "$OUTPUT_DIR" ]]; then
  # Can't find output dir — don't block
  exit 0
fi

# Check if any .md file was written in the last 5 minutes
RECENT_FILES=$(find "$OUTPUT_DIR" -name "*.md" -newer "$OUTPUT_DIR/.gitkeep" 2>/dev/null | grep -v '.gitkeep' || true)

if [[ -z "$RECENT_FILES" ]]; then
  # Check if there are ANY non-gitkeep files at all (might be first run)
  ALL_FILES=$(find "$OUTPUT_DIR" -name "*.md" ! -name '.gitkeep' 2>/dev/null || true)
  if [[ -z "$ALL_FILES" ]]; then
    echo '{"decision": "block", "reason": "No dvar torah output found in output/divrei-torah/. Did the torah-writer agent save the file? Expected path: output/divrei-torah/<format>/YYYY-MM-DD-<topic>.md"}'
    exit 2
  fi
fi

exit 0
