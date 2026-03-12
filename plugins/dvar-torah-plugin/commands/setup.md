---
name: setup
description: "Interactive setup wizard for Dvar Torah Plugin — checks Sefaria MCP, configures language, orientation, thinker preferences, writing style, and scores readiness."
user-invocable: true
allowed-tools: [Read, Grep, Glob, Bash, Write, AskUserQuestion, mcp__claude_ai_Sefaria__get_current_calendar]
---

# /dvar-torah:setup

Interactive onboarding wizard. Verifies your Sefaria MCP connection, sets your preferred language, orientation, default thinkers and writing style, and generates a readiness score.

## Usage

```bash
/dvar-torah:setup              # Full wizard (recommended on first install)
/dvar-torah:setup --rescan     # Re-check MCP + score, skip preferences
/dvar-torah:setup --score-only # Show readiness score only
/dvar-torah:setup --plan-only  # Show improvement plan only
```

## What It Does

Invoke skill: `dvar-torah:setup` with the provided arguments.
