---
name: setup
description: "Interactive setup wizard for Rational Dvar Torah — checks Sefaria MCP, configures thinker preferences and writing style, scores readiness."
user-invocable: true
allowed-tools: [Read, Grep, Glob, Bash, Write, AskUserQuestion, mcp__claude_ai_Sefaria__get_current_calendar]
---

# /rational-dvar-torah:setup

Interactive onboarding wizard. Verifies your Sefaria MCP connection, sets your default thinkers and writing style, and generates a readiness score.

## Usage

```bash
/rational-dvar-torah:setup              # Full wizard (recommended on first install)
/rational-dvar-torah:setup --rescan     # Re-check MCP + score, skip preferences
/rational-dvar-torah:setup --score-only # Show readiness score only
/rational-dvar-torah:setup --plan-only  # Show improvement plan only
```

## What It Does

Invoke skill: `rational-dvar-torah:setup` with the provided arguments.
