<p align="center">
  <img src="https://img.shields.io/badge/version-4.2-blue" alt="Version 4.2">
  <img src="https://img.shields.io/badge/Claude_Code-Plugin-blueviolet" alt="Claude Code Plugin">
  <img src="https://img.shields.io/badge/Sefaria-MCP_Powered-orange" alt="Sefaria MCP">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
</p>

<h1 align="center">דבר תורה<br><sub>Dvar Torah Plugin for Claude Code</sub></h1>

<p align="center">
Write beautiful, source-verified divrei Torah, posts, and shiurim — across every stream of Jewish thought.<br>
Powered by <strong>Sefaria MCP</strong> for real source retrieval. No fabricated citations. Ever.
</p>

---

## What Is This?

A plugin for **Claude Code** — Anthropic's AI assistant — that turns it into a Torah scholar. It guides you through a short interactive wizard, then researches real sources from Sefaria, analyzes them, and writes a fully verified dvar Torah, blog post, or shiur in ~70 seconds.

> **New to Claude Code?** See [Before You Start](#before-you-start) below.

---

## Before You Start

### What You Need

| Requirement | Notes |
|-------------|-------|
| **Claude Code** | [Install here](https://claude.ai/code) — free CLI tool |
| **Claude account** | claude.ai account (Pro/Max recommended — plugin uses Opus for writing) |
| **Sefaria MCP** | Free — setup in Step 1 below |

### Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Then run `claude` in your terminal and log in.

> **Prefer VS Code?** Install the [Claude Code extension](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code) and open any folder. All the same commands work there.

---

## Quick Start

All commands below are typed **inside a Claude Code session** (in your terminal after running `claude`, or in the VS Code Claude Code panel).

### Step 1 — Connect Sefaria (required)

The plugin retrieves and verifies every source from Sefaria in real time.

**Option A — Claude.ai Account Connectors (easiest, no setup)**

1. Go to [claude.ai/settings/integrations](https://claude.ai/settings/integrations)
2. Find **Sefaria** → click **Connect**
3. Done. The connection is available in all your Claude Code sessions automatically.

**Option B — Claude Code command**

```
/mcp add-oauth Sefaria
```

**Option C — Self-hosted Docker**

```bash
docker run -d --name sefaria-mcp -p 8089:8088 \
  $(docker build -q https://github.com/Sefaria/sefaria-mcp.git)
```

Add to `.mcp.json` in your project folder:

```json
{
  "mcpServers": {
    "sefaria": { "type": "sse", "url": "http://localhost:8089/sse" }
  }
}
```

### Step 2 — Install the Plugin

Inside Claude Code, type:

```
/plugin install dvar-torah-plugin@yodem
```

### Step 3 — First-Time Setup (~2 min)

```
/dvar-torah:setup
```

This checks your Sefaria connection and saves your language preference, default orientation, and writing style. You only need to do this once.

### Step 4 — Write Your First Dvar Torah

```
/dvar-torah
```

A short wizard will ask you:

1. **Language** — Hebrew / English / Bilingual
2. **Orientation** — Philosophy / Kabbalah / Hasidut / Hazal / Modern scholarship
3. **Format** — Dvar Torah / Post / Shiur
4. **Length** — 5 / 15 / 30 / 45 min
5. **Topic** — this week's parasha (auto-fetched) or a custom topic
6. **Thinkers** — filtered by the orientation you chose
7. **Occasion** — Shabbat, wedding, shiur, etc.

Then it researches, analyzes, verifies, and writes — automatically. No more input needed.

---

## Usage Examples

```
/dvar-torah                                              # guided wizard (start here)
/dvar-torah פרשת בראשית                                   # specific parsha
/dvar-torah format:post, topic:"divine providence"        # quick LinkedIn post
/dvar-torah orientation:kabbalah, topic:sefirot           # kabbalistic dvar torah
/dvar-torah orientation:hasidut, context:wedding          # hasidic wedding speech
/dvar-torah format:shiur, length:shiur, topic:prophecy    # 45-min lesson plan
/dvar-torah --parasha +1                                  # next week's parsha
/dvar-torah --parasha נח                                  # parsha Noach
/dvar-torah format:dvar-torah, thinkers:"Rambam,Crescas", topic:"free will"
```

---

## What It Can Write

### Streams of Jewish Thought

| Stream | Thinkers & Texts |
|--------|-----------------|
| **Jewish Philosophy** | Rambam, Saadia Gaon, Gersonides, Crescas, Albo, Yehuda HaLevi, Bahya Ibn Paquda |
| **Kabbalah** | Zohar, Ari, Ramak, Ramchal, Abulafia, Baal HaSulam |
| **Hasidut** | Baal Shem Tov, Maggid, Tanya/Chabad, Breslov, Kedushat Levi, Sefat Emet, Esh Kodesh |
| **Hazal / Midrash** | Mishnah, Tosefta, Bavli, Yerushalmi, Mekhilta, Midrash Rabbah, Tanchuma |
| **Modern Jewish Thought** | Rav Kook, Jonathan Sacks, Eliezer Berkovits, Y. Leibowitz + biblical scholarship |

### Occasions (tone & theme auto-adjusted)

Birth · Brit Milah · Bar/Bat Mitzvah · Wedding · Shabbat · Holiday · Shiva · Yahrzeit · General

---

## How It Works

```
Phase 0 — Wizard (Haiku)                  ~5s
  └── Short interactive questions

Phase 1 — Research (Haiku, parallel)      ~15s
  ├── Sefaria source search
  ├── Past writings analysis (avoids repetition)
  ├── Historical/ANE context (if needed)
  └── Mussar sources (if needed)

Phase 2 — Analysis + Verification         ~20s
  ├── Philosophical analysis (Sonnet)
  └── Citation verification (every source checked in Sefaria)

Phase 3 — Writing (Opus)                  ~30s
  └── Final polished output
```

**Total: ~70 seconds.** Every citation verified against Sefaria — no invented sources.

---

## All Commands

| Command | What It Does |
|---------|-------------|
| `/dvar-torah` | Main entry point — wizard or direct params |
| `/dvar-torah:setup` | First-time setup, Sefaria check, preferences |
| `/dvar-torah:research <topic>` | Search Sefaria without writing |
| `/dvar-torah:analyze <question>` | Philosophical analysis across thinkers |
| `/dvar-torah:verify` | Verify and reformat citations in a draft |
| `/dvar-torah:history <topic>` | Historical/ANE context for a topic |
| `/dvar-torah:previous` | Analyze your past writings for patterns |

---

## Output Location

```
output/divrei-torah/
  ├── dvar-torah/   YYYY-MM-DD-topic.md
  ├── posts/        YYYY-MM-DD-topic.md
  └── shiurim/      YYYY-MM-DD-topic.md
```

Each file includes metadata: date, format, orientation, thinkers, source count.

---

## Troubleshooting

**"Sefaria not connected"**
→ Use Option A (Account Connectors) at [claude.ai/settings/integrations](https://claude.ai/settings/integrations) — most reliable

**Plugin not found after install**
→ Restart your Claude Code session: `exit`, then `claude` again

**Output is in the wrong language**
→ Run `/dvar-torah:setup` to update your saved preference
→ Or pass directly: `/dvar-torah language:english`

**Response takes more than 2 minutes**
→ Normal for long formats — Opus is the most powerful but also the slowest model. Short posts take ~30s.

**Citations flagged as unverified**
→ Expected behavior — the plugin intentionally refuses to include any source it cannot confirm in Sefaria. It will suggest verified alternatives.

---

## Core Principles

1. **Retrieval over memory** — searches Sefaria before every citation. Never invents sources.
2. **No unverified citations** — every quote is verified via Sefaria MCP.
3. **Learns from history** — analyzes past outputs to avoid repeating topics, thinkers, or structures.
4. **Respects every tradition** — each stream presented in its strongest, most authentic form.
5. **Depth with clarity** — complex sources, clearly explained.

---

## License

MIT — built by [@yodem](https://github.com/yodem) · Powered by [Sefaria](https://www.sefaria.org) + [Claude Code](https://claude.ai/code)
