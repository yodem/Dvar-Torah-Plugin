#!/usr/bin/env bash
# Validation script for plugin refactor changes
# TDD: This script tests the 4 changes described in the requirements.
# Run BEFORE changes to see failures (RED), AFTER to see passes (GREEN).

set -euo pipefail
PASS=0
FAIL=0

check() {
  local desc="$1"
  local result="$2"
  if [ "$result" = "true" ]; then
    echo "PASS: $desc"
    PASS=$((PASS+1))
  else
    echo "FAIL: $desc"
    FAIL=$((FAIL+1))
  fi
}

PLUGIN_DIR="/Users/yotamfromm/dev/Rational-Dvar-Torah-Plugin/plugins/dvar-torah-plugin"
SRC_DIR="/Users/yotamfromm/dev/Rational-Dvar-Torah-Plugin/src"

# --- Change 1: torah-philosopher — WebFetch and WebSearch removed ---

file1="$PLUGIN_DIR/agents/torah-philosopher.md"
file2="$SRC_DIR/agents/torah-philosopher.md"

check "plugins: torah-philosopher does NOT have WebFetch" \
  "$(grep -q 'WebFetch' "$file1" && echo false || echo true)"

check "plugins: torah-philosopher does NOT have WebSearch" \
  "$(grep -q 'WebSearch' "$file1" && echo false || echo true)"

check "src: torah-philosopher does NOT have WebFetch" \
  "$(grep -q 'WebFetch' "$file2" && echo false || echo true)"

check "src: torah-philosopher does NOT have WebSearch" \
  "$(grep -q 'WebSearch' "$file2" && echo false || echo true)"

# --- Change 2: source-researcher — mcp__memory__* removed ---

file3="$PLUGIN_DIR/agents/source-researcher.md"
file4="$SRC_DIR/agents/source-researcher.md"

check "plugins: source-researcher does NOT have mcp__memory__*" \
  "$(grep -q 'mcp__memory__\*' "$file3" && echo false || echo true)"

check "src: source-researcher does NOT have mcp__memory__*" \
  "$(grep -q 'mcp__memory__\*' "$file4" && echo false || echo true)"

# --- Change 3: interactive-cli SKILL.md — AskUserQuestion in allowed-tools ---

file5="$PLUGIN_DIR/skills/interactive-cli/SKILL.md"
file6="$SRC_DIR/skills/interactive-cli/SKILL.md"

check "plugins: interactive-cli allowed-tools has AskUserQuestion" \
  "$(python3 -c "
import re, sys
with open('$file5') as f:
    c = f.read()
fm = re.search(r'^---\n(.*?)\n---', c, re.DOTALL)
section = fm.group(1) if fm else ''
at_match = re.search(r'allowed-tools:(.*?)(?=\n\S|\Z)', section, re.DOTALL)
at = at_match.group(1) if at_match else ''
print('true' if 'AskUserQuestion' in at else 'false')
")"

check "src: interactive-cli allowed-tools has AskUserQuestion" \
  "$(python3 -c "
import re, sys
with open('$file6') as f:
    c = f.read()
fm = re.search(r'^---\n(.*?)\n---', c, re.DOTALL)
section = fm.group(1) if fm else ''
at_match = re.search(r'allowed-tools:(.*?)(?=\n\S|\Z)', section, re.DOTALL)
at = at_match.group(1) if at_match else ''
print('true' if 'AskUserQuestion' in at else 'false')
")"

# --- Change 4: dvar-torah-writer — templates extracted to references/templates.md ---

tmpl1="$PLUGIN_DIR/skills/dvar-torah-writer/references/templates.md"
tmpl2="$SRC_DIR/skills/dvar-torah-writer/references/templates.md"
skill1="$PLUGIN_DIR/skills/dvar-torah-writer/SKILL.md"
skill2="$SRC_DIR/skills/dvar-torah-writer/SKILL.md"

check "plugins: references/templates.md exists" \
  "$([ -f "$tmpl1" ] && echo true || echo false)"

check "src: references/templates.md exists" \
  "$([ -f "$tmpl2" ] && echo true || echo false)"

check "plugins: templates.md contains the templates section header" \
  "$(grep -q 'תבניות לפי פורמט ואורך' "$tmpl1" && echo true || echo false)"

check "src: templates.md contains the templates section header" \
  "$(grep -q 'תבניות לפי פורמט ואורך' "$tmpl2" && echo true || echo false)"

check "plugins: SKILL.md references/templates.md pointer exists" \
  "$(grep -q 'references/templates.md' "$skill1" && echo true || echo false)"

check "src: SKILL.md references/templates.md pointer exists" \
  "$(grep -q 'references/templates.md' "$skill2" && echo true || echo false)"

check "plugins: SKILL.md no longer contains detailed template blocks inline" \
  "$(grep -q 'דבר תורה קצר (5 דקות' "$skill1" && echo false || echo true)"

check "src: SKILL.md no longer contains detailed template blocks inline" \
  "$(grep -q 'דבר תורה קצר (5 דקות' "$skill2" && echo false || echo true)"

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
