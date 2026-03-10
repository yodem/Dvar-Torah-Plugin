---
name: setup
license: MIT
compatibility: "Claude Code 2.1.59+."
description: "Interactive setup wizard for Dvar Torah Plugin v3.0. Checks Sefaria MCP, configures language preference, orientation, preferred thinkers, writing style, and generates a readiness score."
argument-hint: "[--rescan] [--score-only] [--plan-only]"
context: inherit
version: 3.0.0
author: yodem
tags: [onboarding, setup, wizard, configuration, sefaria, mcp, language, orientation]
user-invocable: true
disable-model-invocation: true
allowed-tools: [Read, Grep, Glob, Bash, Write, AskUserQuestion, mcp__claude_ai_Sefaria__get_current_calendar]
metadata:
  category: configuration
---

# Dvar Torah Plugin — Setup Wizard

Interactive onboarding that checks your Sefaria MCP connection, configures language preference, orientation/subject stream, preferred thinkers, writing style, sets up your output directory, and generates a readiness score.

## When to Use

- First time after installing the plugin (`/plugin install dvar-torah-plugin@yodem`)
- When Sefaria MCP changes (Docker port, connector URL)
- To reconfigure orientation, thinker preferences, or writing style
- Run with `--score-only` to check current readiness

## Quick Start

```bash
/dvar-torah-plugin:setup              # Full wizard
/dvar-torah-plugin:setup --rescan     # Re-check MCP + score, skip preferences
/dvar-torah-plugin:setup --score-only # Readiness score only
/dvar-torah-plugin:setup --plan-only  # Improvement plan only
```

## Argument Resolution

```python
FLAG = "$ARGUMENTS[0]"  # --rescan | --score-only | --plan-only
# No arguments → full wizard
```

## The Eight Phases

| Phase | What | Output |
|-------|------|--------|
| 0. Language | Preferred language (Hebrew / English / Bilingual) | Language saved |
| 1. Sefaria MCP | Detect and verify Sefaria connection | MCP status |
| 2. Install Scope | Confirm user vs project install | Scope decision |
| 2.5. Orientation | Which subject stream(s) to default to | Orientation saved |
| 3. Thinkers | Choose default thinkers (filtered by orientation) | Preferences saved |
| 4. Style | Writing register, tradition | Style saved |
| 5. Score | Readiness score (0-10) | Score + gaps |
| 6. Plan | Prioritized improvement steps + keybinding | Action plan |

---

## Phase 0: Language Preference

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

## Phase 1: Sefaria MCP Detection

First, check what MCP servers are configured:

```python
# PARALLEL
Read(file_path=".mcp.json")
Bash(command="cat ~/.claude/settings.json 2>/dev/null | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('mcpServers',{}), indent=2))\" 2>/dev/null || echo '{}'")
```

Look for a Sefaria MCP entry in either file. Identify which connector type is configured:
- `claude_ai_Sefaria` — Claude native connector (cloud, recommended)
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
  "question": "Sefaria MCP is not responding. How would you like to fix this?",
  "header": "Sefaria MCP Setup",
  "options": [
    {
      "label": "Claude connector (Recommended)",
      "description": "Uses the built-in claude_ai_Sefaria connector. No Docker required.",
      "markdown": "```\nAdd to ~/.claude/settings.json:\n{\n  \"mcpServers\": {\n    \"claude_ai_Sefaria\": {\n      \"type\": \"claude_ai\",\n      \"name\": \"Sefaria\"\n    }\n  }\n}\n```"
    },
    {
      "label": "Docker (local SSE)",
      "description": "Run Sefaria MCP as a local Docker container on port 8089.",
      "markdown": "```bash\ndocker build -t sefaria-mcp \\\n  https://github.com/Sefaria/sefaria-mcp.git\ndocker run -d --name sefaria-mcp \\\n  -p 8089:8088 sefaria-mcp\n```"
    },
    {
      "label": "Skip for now",
      "description": "Continue setup without Sefaria. Source lookup will not work.",
      "markdown": "```\n⚠ Source verification will be disabled.\nRun /rational-dvar-torah:setup again after configuring Sefaria.\n```"
    }
  ],
  "multiSelect": false
}])
```

Show final status:
```
Sefaria MCP:  ✓ Connected (claude_ai connector)   — Parsha: פרשת X
              ✗ Not configured — source lookup disabled
              ✓ Connected (Docker, port 8089)
```

---

## Phase 2: Install Scope

```python
AskUserQuestion(questions=[{
  "question": "How should Rational Dvar Torah be installed?",
  "header": "Install scope",
  "options": [
    {
      "label": "User-only (Recommended)",
      "description": "Plugin loads only for you. Invisible to teammates.",
      "markdown": "```\nUser-Only Install\n─────────────────\n~/.claude/\n  └── plugins/\n        └── rational-dvar-torah/  ← only YOU see this\n\nTeammates: unaffected\nGit:       nothing committed\n```"
    },
    {
      "label": "Project-wide",
      "description": "Adds to .claude/plugins — loads for everyone in this repo.",
      "markdown": "```\nProject-Wide Install\n────────────────────\nyour-repo/\n  └── .claude/\n        └── plugins/\n              └── rational-dvar-torah/  ← everyone sees this\n\nTeammates: auto-loaded for all\nGit:       committed to repo\n```"
    },
    {
      "label": "Already installed",
      "description": "Skip installation, jump to preferences.",
      "markdown": "```\nSkip to Configure\n─────────────────\n✓ Plugin already installed\n→ Jump to Phase 3: Thinker preferences\n```"
    }
  ],
  "multiSelect": false
}])
```

---

## Phase 2.5: Orientation Preference

Which Jewish thought stream(s) to default to? This determines which thinkers appear in the `/dvar-torah` wizard.

```python
AskUserQuestion(questions=[{
  "question": "באיזה זרם מחשבה תרצה להתמקד בדרך כלל? / Which Jewish thought stream(s)?",
  "header": "אוריינטציה / Orientation",
  "options": [
    {
      "label": "פילוסופיה יהודית (לא קבלה) — Rationalists",
      "description": "רמב״ם, רס״ג, רלב״ג, קרשקש, אלבו, ר״י הלוי — Rambam, Saadia, Gersonides, Crescas, Albo, Kuzari",
      "markdown": "```\nRationalist Philosophy\n──────────────────────\nRambam, Rasag, Ralbag, Crescas, Albo, Ibn Ezra, Kuzari\nCore: Aristotelian rationalism, harmony of Torah & reason\n```"
    },
    {
      "label": "קבלה — Kabbalah",
      "description": "זוהר, האר״י, רמ״ק, רמח״ל / Zohar, Ari, Ramak, Ramchal",
      "markdown": "```\nKabbalah\n────────\nZohar, Pardes Rimonim, Etz Chaim, Daat Tevunot\nCore: Sefirot, Ein Sof, tzimtzum, tikkun\n```"
    },
    {
      "label": "חסידות — Hasidut",
      "description": "בעש״ט, תניא, ברסלב, קדושת לוי / Baal Shem Tov, Tanya, Breslov",
      "markdown": "```\nHasidut\n───────\nKeter Shem Tov, Maggid, Tanya, Likkutei Moharan\nCore: Devekut, simcha, Tzaddik, avodah\n```"
    },
    {
      "label": "חז״ל — Talmudic Sages",
      "description": "משנה, גמרא, מדרש / Mishnah, Talmud, Midrash",
      "markdown": "```\nHazal\n─────\nMishnah, Talmud Bavli, Bereishit Rabbah, Midrash Tanchuma\nCore: Halakha, Aggadah, rabbinic thought\n```"
    },
    {
      "label": "חוקרים מודרניים — Modern Scholars",
      "description": "Wissenschaft, ANE, ביקורת המקרא / biblical criticism, archaeology",
      "markdown": "```\nModern Scholarship\n──────────────────\nKaufmann, Cassuto, Pines, Wellhausen (contrast), ANE texts\nCore: Historical context, documentary hypothesis, counter-criticism\n```"
    }
  ],
  "multiSelect": true
}])
```

Persist as env var:
```
DVAR_TORAH_ORIENTATION="philosophy"  # philosophy | kabbalah | hasidut | hazal | modern (comma-separated for multiple)
```

---

## Phase 3: Thinker Preferences

Ask which thinkers to feature by default. These become the pre-selected defaults in the `/dvar-torah` wizard.
**Filter thinker list based on orientation(s) selected in Phase 2.5.**

Show thinker options filtered by the orientation(s) selected in Phase 2.5:

```python
AskUserQuestion(questions=[{
  "question": "אילו הוגים להגדיר כברירת מחדל? / Which thinkers as defaults?",
  "header": "הוגים / Default Thinkers",
  # Show only thinkers from selected orientation(s):
  # philosophy → Rambam, Rasag, Ralbag, Crescas, Albo, Ibn Ezra, Kuzari, Ibn Paquda
  # kabbalah   → Zohar, Ramak, Ari, Ramchal
  # hasidut    → Besht, Maggid, Admur HaZaken, Nachman, Levi Yitzchak
  # hazal      → Tannaim, Amoraim, Midrash, individual sages
  # modern     → Kaufmann, Cassuto, Pines, Altmann, Harvey, Wellhausen (contrast)
  "multiSelect": true
}])
```

Save the selection:

```python
# Env vars to persist:
DVAR_TORAH_DEFAULT_THINKERS="רמב״ם,קרשקש"   # comma-separated
```

---

## Phase 4: Writing Style

```python
AskUserQuestion(questions=[{
  "question": "What writing style should /dvar-torah use by default?",
  "header": "Writing Style",
  "options": [
    {
      "label": "Hebrew — רציונלי (Recommended)",
      "description": "Write in Hebrew, rationalist/philosophical register, academic references",
      "markdown": "```\nHebrew · Rationalist\n────────────────────\nLanguage:  Hebrew (עברית)\nRegister:  Philosophical, structured\nSources:   Sefaria primary texts + academic commentary\nAudience:  Hebrew-literate, philosophically inclined\n```"
    },
    {
      "label": "Hebrew — מוסרי",
      "description": "Write in Hebrew, mussar register, focus on practical ethics and character",
      "markdown": "```\nHebrew · Mussar\n───────────────\nLanguage:  Hebrew (עברית)\nRegister:  Mussar, practical ethics\nSources:   Mesillat Yesharim, Chovot ha-Levavot, Orchot Tzaddikim\nAudience:  Hebrew-literate, character-development focus\n```"
    },
    {
      "label": "English — Rationalist",
      "description": "Write in English, philosophical register, good for English-speaking audiences",
      "markdown": "```\nEnglish · Rationalist\n─────────────────────\nLanguage:  English\nRegister:  Philosophical, structured\nSources:   English translations + academic sources\nAudience:  English-literate, philosophically inclined\n```"
    },
    {
      "label": "Bilingual — Hebrew + English",
      "description": "Hebrew body, English summary and source citations",
      "markdown": "```\nBilingual\n─────────\nBody:      Hebrew (עברית)\nSummary:   English\nCitations: English transliteration + Hebrew original\nAudience:  Mixed Hebrew/English audience\n```"
    }
  ],
  "multiSelect": false
}])
```

Persist as env var:
```
DVAR_TORAH_DEFAULT_STYLE="hebrew-rationalist"  # hebrew-rationalist | hebrew-mussar | english-rationalist | bilingual
```

---

## Phase 5: Readiness Score

Compute a score (0–10) from 4 dimensions:

| Dimension | Weight | Signals |
|-----------|--------|---------|
| **Sefaria MCP** | 40% | Connected + live calendar test passes |
| **Output Directory** | 20% | `output/divrei-torah/` exists with subdirs |
| **Preferences Configured** | 25% | Default thinkers + style set in env |
| **Previous Writings** | 15% | ≥1 saved dvar-torah in `output/divrei-torah/` |

Check output directory:
```python
Glob(pattern="output/divrei-torah/**/*.md")
```

### Score Display

```
Dvar Torah Plugin Readiness: 7.5 / 10

  Sefaria MCP          ████████████░░░░  Connected ✓
  Output Directory     ████████████████  Set up ✓
  Preferences          ████████░░░░░░░░  Thinkers set, style missing
  Previous Writings    ░░░░░░░░░░░░░░░░  0 divrei torah yet

  Top gap: Set writing style → run /rational-dvar-torah:setup Phase 4
```

---

## Phase 6: Improvement Plan

Generate runnable next steps:

```
Your Setup Plan:

P0 (do now):
  Sefaria connected ✓ — ready to write

  Run your first dvar torah:
    /dvar-torah
  → Interactive wizard will guide you through language → orientation → parsha + thinkers.

P1 (this week):
  Build a writing history — run /dvar-torah 3-5 times.
  → previous-analysis skill will start detecting your patterns.

P2 (ongoing):
  /dvar-torah-plugin:setup --rescan
  → Re-run after writing a few divrei torah to track progress.
```

### Keybinding Offer

```python
AskUserQuestion(questions=[{
  "question": "Add a keyboard shortcut for /dvar-torah?",
  "header": "Keyboard Shortcut",
  "options": [
    {
      "label": "Yes — ctrl+shift+d (Recommended)",
      "description": "Opens the /dvar-torah wizard instantly"
    },
    {
      "label": "Skip",
      "description": "No shortcut"
    }
  ],
  "multiSelect": false
}])
```

If **Yes**: merge into `~/.claude/keybindings.json`:
```json
{"key": "ctrl+shift+d", "command": "/dvar-torah", "description": "Open Dvar Torah wizard"}
```

Read the existing file first, merge (never overwrite existing keys), then write back.

---

## CLI Flags

| Flag | Behavior |
|------|----------|
| (none) | Full 6-phase wizard |
| `--rescan` | Re-run MCP check + score, skip thinker/style phases |
| `--score-only` | Show readiness score only (Phase 5) |
| `--plan-only` | Show improvement plan only (Phase 6) |

---

## Post-Setup

> **Tip:** After setup completes, run `/reload-plugins` to activate any config changes without restarting your session.

## Related Commands

- `/dvar-torah` — Write a dvar torah (the main command this plugin provides)
- `/dvar-torah-plugin:setup --rescan` — Re-check MCP + readiness score after writing a few divrei torah
