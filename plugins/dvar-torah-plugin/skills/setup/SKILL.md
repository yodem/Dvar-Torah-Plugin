---
name: setup
license: MIT
compatibility: "Claude Code 2.1.59+."
description: "Quick setup for Dvar Torah Plugin. Checks Sefaria MCP connection and configures language preference."
argument-hint: "[--rescan] [--score-only]"
context: inherit
version: 4.3.0
author: yodem
tags: [onboarding, setup, wizard, configuration, sefaria, mcp, language]
user-invocable: true
disable-model-invocation: false
allowed-tools: [Read, Grep, Glob, Bash, Write, AskUserQuestion, mcp__claude_ai_Sefaria__get_current_calendar]
metadata:
  category: configuration
---

# Dvar Torah Plugin — Setup

Quick onboarding: checks Sefaria MCP connection and sets your language preference.

## When to Use

- First time after installing the plugin (`/plugin install dvar-torah-plugin@yodem`)
- When Sefaria MCP changes (Docker port, connector URL)
- Run with `--score-only` to check current readiness

## Quick Start

```bash
/dvar-torah:setup              # Full setup
/dvar-torah:setup --rescan     # Re-check MCP + score
/dvar-torah:setup --score-only # Readiness score only
```

## Phases

| Phase | What | Output |
|-------|------|--------|
| 1. Language | Preferred language (Hebrew / English / Bilingual) | Language saved |
| 2. Sefaria MCP | Detect and verify Sefaria connection | MCP status |
| 3. Score | Readiness score (0-10) | Score + next steps |

---

## Phase 1: Language Preference

```python
AskUserQuestion(questions=[{
  "question": "באיזה שפה תרצה לעבוד? / In which language would you like to work?",
  "header": "שפה / Language",
  "options": [
    {
      "label": "עברית (Recommended)",
      "description": "כל הממשק, האשף, והפלט בעברית",
      "markdown": "```\nHebrew Mode\n───────────\nWizard:  עברית\nOutput:  עברית\nCitations: עברית ראשונה + תרגום\n```"
    },
    {
      "label": "English",
      "description": "All prompts and output in English",
      "markdown": "```\nEnglish Mode\n────────────\nWizard:  English\nOutput:  English\nCitations: English first + Hebrew original\n```"
    },
    {
      "label": "Bilingual / דו-לשוני",
      "description": "Hebrew body with English summary and citations",
      "markdown": "```\nBilingual Mode\n──────────────\nBody:     Hebrew (עברית)\nSummary:  English\nCitations: English transliteration + Hebrew original\n```"
    }
  ],
  "multiSelect": false
}])
```

Persist as env var:
```
DVAR_TORAH_LANGUAGE="he"  # he | en | bilingual
```

---

## Phase 2: Sefaria MCP Detection

Sefaria MCP is required for source lookups, text retrieval, and citation verification.

First, check what MCP servers are configured:

```python
# PARALLEL
Read(file_path=".mcp.json")
Bash(command="cat ~/.claude/settings.json 2>/dev/null | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('mcpServers',{}), indent=2))\" 2>/dev/null || echo '{}'")
```

Look for a Sefaria MCP entry in either file. Identify which connector type is configured:
- `claude_ai_Sefaria` — Claude Account Connector (cloud, recommended)
- `sefaria-mcp` with `url: http://localhost:{port}/sse` — Docker/local SSE

### Live Connection Test

Attempt a live calendar fetch to verify the connection is active:

```python
mcp__claude_ai_Sefaria__get_current_calendar()
```

If it succeeds: **Sefaria MCP ✓ — Connected**

If it fails, present repair options:

```python
AskUserQuestion(questions=[{
  "question": "Sefaria MCP is not responding. How would you like to connect?",
  "header": "Sefaria MCP Setup",
  "options": [
    {
      "label": "Claude Account Connector (Recommended)",
      "description": "One-click setup via Claude's built-in integrations. No Docker or local install needed.",
      "markdown": "```\nOption A — Claude.ai Account Connectors:\n  1. Go to claude.ai/settings/integrations\n  2. Find \"Sefaria\" and click Connect\n  3. Done! Available in all Claude Code sessions.\n\nOption B — Claude Code CLI:\n  Run: claude mcp add-oauth Sefaria\n  This connects your Claude account to\n  the Sefaria MCP server automatically.\n```"
    },
    {
      "label": "Docker (local SSE)",
      "description": "Self-host Sefaria MCP as a local Docker container on port 8089.",
      "markdown": "```bash\ndocker build -t sefaria-mcp \\\n  https://github.com/Sefaria/sefaria-mcp.git\ndocker run -d --name sefaria-mcp \\\n  -p 8089:8088 sefaria-mcp\n\n# Then add to .mcp.json:\n# \"sefaria\": {\n#   \"type\": \"sse\",\n#   \"url\": \"http://localhost:8089/sse\"\n# }\n```"
    },
    {
      "label": "Skip for now",
      "description": "Continue setup without Sefaria. Source lookup and citation verification will not work.",
      "markdown": "```\n⚠ Source verification will be disabled.\nRun /dvar-torah:setup again after\nconnecting Sefaria.\n```"
    }
  ],
  "multiSelect": false
}])
```

Show final status:
```
Sefaria MCP:  ✓ Connected (Account Connector)     — Parsha: פרשת X
              ✓ Connected (Docker, port 8089)
              ✗ Not configured — source lookup disabled
```

---

## Phase 3: Readiness Score

Compute a score (0–10) from 3 dimensions:

| Dimension | Weight | Signals |
|-----------|--------|---------|
| **Sefaria MCP** | 50% | Connected + live calendar test passes |
| **Output Directory** | 25% | `output/divrei-torah/` exists with subdirs |
| **Previous Writings** | 25% | ≥1 saved dvar-torah in `output/divrei-torah/` |

Check output directory:
```python
Glob(pattern="output/divrei-torah/**/*.md")
```

### Score Display

```
Dvar Torah Plugin Readiness: 5 / 10

  Sefaria MCP          ████████████████  Connected ✓
  Output Directory     ░░░░░░░░░░░░░░░░  Not set up yet
  Previous Writings    ░░░░░░░░░░░░░░░░  0 divrei torah yet
```

### Next Steps

```
Ready to go! Run:
  /dvar-torah                    ← write your first dvar torah
  /dvar-torah:profile            ← (optional) set default orientation, thinkers, and writing style
```

---

## CLI Flags

| Flag | Behavior |
|------|----------|
| (none) | Full setup (language + MCP + score) |
| `--rescan` | Re-check MCP + score only |
| `--score-only` | Show readiness score only |

---

## Post-Setup

> **Tip:** After setup completes, run `/reload-plugins` to activate any config changes without restarting your session.

## Related Commands

- `/dvar-torah` — Write a dvar torah (the main command)
- `/dvar-torah:profile` — (Optional) Configure default orientation, thinkers, and writing style
- `/dvar-torah:setup --rescan` — Re-check MCP + readiness score
