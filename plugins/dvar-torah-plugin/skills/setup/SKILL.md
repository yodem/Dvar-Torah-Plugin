---
name: setup
license: MIT
compatibility: "Claude Code 2.1.59+."
description: "Quick setup for Dvar Torah Plugin. Checks Sefaria MCP connection and configures language preference."
argument-hint: "[--rescan] [--score-only]"
context: inherit
version: 4.4.0
author: yodem
tags: [onboarding, setup, wizard, configuration, sefaria, mcp, language, gemini]
user-invocable: true
disable-model-invocation: false
allowed-tools: [Read, Grep, Glob, Bash, Write, AskUserQuestion, mcp__claude_ai_Sefaria__get_current_calendar, mcp__gemini-api__gemini_raw]
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
| 2.5. Gemini (optional) | Configure GOOGLE_API_KEY for prose drafting | Key stored in `.dvar-torah/secrets.json` |
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

## Phase 2.5: Gemini (Optional) — Prose Drafting

The plugin ships with a bundled Gemini MCP server. When configured, the `torah-writer` agent routes the prose-drafting step to Gemini (faster, cheaper for long shiurim) while every Sefaria citation continues to be verified by Claude. This phase is optional — skipping leaves drafting on Claude.

### Check current state

```python
import os
have_env = bool(os.environ.get("GOOGLE_API_KEY", "").strip())
have_secrets = bool(Read(file_path=".dvar-torah/secrets.json").get("google_api_key"))
```

If either is set, show:
```
Gemini drafting:  ✓ Configured — torah-writer will use Gemini for prose
```
and skip the prompt below.

### Otherwise, offer setup

```python
AskUserQuestion(questions=[{
  "question": "Configure Gemini for prose drafting? (optional — Sefaria verification stays on Claude either way)",
  "header": "Gemini API Key",
  "options": [
    {
      "label": "Yes — paste my Google API key",
      "description": "Saved locally to .dvar-torah/secrets.json (gitignored). Used only by the bundled Gemini MCP server.",
      "markdown": "```\nKey → .dvar-torah/secrets.json\nUsed by torah-writer (drafting + synthesis)\nSefaria citations still verified by Claude\nGet a key: https://aistudio.google.com/apikey\n```"
    },
    {
      "label": "Skip — keep drafting on Claude",
      "description": "You can configure later by running /dvar-torah:setup again.",
      "markdown": "```\nDrafting:        Claude (opus)\nVerification:    Claude + Sefaria MCP\nGemini server:   inactive (no-op)\n```"
    }
  ],
  "multiSelect": false
}])
```

If user picked "Yes":

1. `AskUserQuestion` for the key (single text input — "Paste your Google API key").
2. Write the secrets file:
   ```python
   import json
   Bash(command="mkdir -p .dvar-torah")
   Write(file_path=".dvar-torah/secrets.json", content=json.dumps({"google_api_key": "<pasted>"}, indent=2))
   Bash(command="chmod 600 .dvar-torah/secrets.json")
   ```
3. Smoke-test the key via `mcp__gemini-api__gemini_raw` with a trivial system/prompt (e.g. `system="reply with OK"`, `prompt="ping"`, `max_output_tokens=8`). Report PASS / FAIL.
4. On PASS, write `.dvar-torah/gemini-approved` after the per-install calibration gate in `/dvar-torah:compose`.

```
Gemini drafting:  ✓ Configured + smoke-tested
                  Key stored in .dvar-torah/secrets.json (chmod 600, gitignored)
                  Calibration gate will run on first /dvar-torah session.
```

---

## Phase 3: Readiness Score

Compute a score (0–10) from 4 dimensions:

| Dimension | Weight | Signals |
|-----------|--------|---------|
| **Sefaria MCP** | 40% | Connected + live calendar test passes |
| **Gemini drafting** | 20% | `GOOGLE_API_KEY` set or `.dvar-torah/secrets.json` present (optional — not having this scores 0 on this dimension but does not block use) |
| **Output Directory** | 20% | `output/divrei-torah/` exists with subdirs |
| **Previous Writings** | 20% | ≥1 saved dvar-torah in `output/divrei-torah/` |

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

### What You Can Do Now

After setup, show the user this capabilities summary:

```
Setup complete! Here's everything the plugin can do:

── Writing ─────────────────────────────────────────
  /dvar-torah                  Interactive wizard → full dvar torah
  /dvar-torah פרשת בראשית       Direct parsha input
  /dvar-torah format:post       Quick post for blog/social
  /dvar-torah format:shiur      45-min shiur plan

── Research (standalone) ───────────────────────────
  /dvar-torah:research <topic>  Search Sefaria sources
  /dvar-torah:analyze <topic>   Philosophical analysis across thinkers
  /dvar-torah:history <topic>   Historical/ANE context
  /dvar-torah:verify            Verify citations in a draft

── Personalization ─────────────────────────────────
  /dvar-torah:profile           Set default orientation, thinkers, style
  /dvar-torah:previous          Analyze your past writings for patterns
                                (learns your style over time)

── Maintenance ─────────────────────────────────────
  /dvar-torah:setup --rescan    Re-check Sefaria + readiness score

── Orientations ────────────────────────────────────
  Philosophy · Kabbalah · Hasidut · Hazal · Modern Scholarship

── Output ──────────────────────────────────────────
  output/divrei-torah/dvar-torah/   Full divrei torah
  output/divrei-torah/posts/        Blog/social posts
  output/divrei-torah/shiurim/      Shiur plans
```

---

## CLI Flags

| Flag | Behavior |
|------|----------|
| (none) | Full setup (language + MCP + score) |
| `--rescan` | Re-check MCP + score only |
| `--score-only` | Show readiness score only |
