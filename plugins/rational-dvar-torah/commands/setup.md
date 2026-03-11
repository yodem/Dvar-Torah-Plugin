---
name: setup
description: "Interactive setup wizard for Dvar Torah Plugin — checks Sefaria MCP, configures thinker preferences and writing style, scores readiness."
user-invocable: true
allowed-tools: [Read, Grep, Glob, Bash, Write, AskUserQuestion, mcp__claude_ai_Sefaria__get_current_calendar]
---

# /dvar-torah-plugin:setup

Interactive onboarding wizard. Verifies your Sefaria MCP connection, sets your default thinkers and writing style, and generates a readiness score.

## Usage

```bash
/dvar-torah-plugin:setup              # Full wizard (recommended on first install)
/dvar-torah-plugin:setup --rescan     # Re-check MCP + score, skip preferences
/dvar-torah-plugin:setup --score-only # Show readiness score only
/dvar-torah-plugin:setup --plan-only  # Show improvement plan only
```

## What It Does

Invoke skill: `dvar-torah-plugin:setup` with the provided arguments.
