<p align="center">
  <img src="https://img.shields.io/badge/version-4.0-blue" alt="Version 4.0">
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

## What It Does

An interactive Claude Code plugin that writes Torah content grounded in real sources. You choose the orientation, format, length, occasion, and thinkers — the plugin researches, analyzes, verifies, and writes.

**Every single citation is retrieved and verified through Sefaria** — the world's largest open library of Jewish texts.

### Supported Orientations

| Stream | Thinkers & Texts |
|--------|-----------------|
| **Jewish Philosophy** | Rambam, Saadia Gaon, Gersonides, Crescas, Albo, Kuzari, Ibn Ezra |
| **Kabbalah** | Zohar, Ari, Ramak, Ramchal |
| **Hasidut** | Baal Shem Tov, Tanya, Breslov, Kedushat Levi |
| **Talmud & Midrash** | Mishnah, Bavli, Yerushalmi, Bereishit Rabbah, Tanchuma |
| **Modern Scholarship** | Kaufmann, Cassuto, Pines, Altmann, ANE parallels |

### Formats & Lengths

| Format | Lengths | Best For |
|--------|---------|----------|
| **Dvar Torah** | Short (5 min) / Medium (15 min) / Long (30 min) | Shabbat table, synagogue, publication |
| **Post** | Short (5 min) | Social media, blog, newsletter |
| **Shiur** | Full (45 min) | Classroom, study group, lecture |

### Life-Cycle Contexts

Tailored tone and themes for: Birth, Brit Milah, Bar/Bat Mitzvah, Wedding, Shabbat, Holiday, Shiva, Yahrzeit, or General.

---

## Quick Start

### 1. Connect to Sefaria MCP (Required)

The plugin needs Sefaria MCP for source retrieval and citation verification. Choose one:

**Option A — Claude Account Connectors (Recommended)**

The simplest way. No Docker, no local setup.

1. Go to [claude.ai/settings/integrations](https://claude.ai/settings/integrations)
2. Find **Sefaria** and click **Connect**
3. Done — the connector is automatically available in all your Claude Code sessions

**Option B — Claude Code CLI**

```bash
claude mcp add-oauth Sefaria
```

**Option C — Docker (Self-Hosted)**

```bash
docker build -t sefaria-mcp https://github.com/Sefaria/sefaria-mcp.git
docker run -d --name sefaria-mcp -p 8089:8088 sefaria-mcp
```

Then add to your `.mcp.json`:
```json
{
  "mcpServers": {
    "sefaria": {
      "type": "sse",
      "url": "http://localhost:8089/sse"
    }
  }
}
```

### 2. Install the Plugin

```bash
/plugin install dvar-torah-plugin
```

### 3. Run Setup (Optional)

```bash
/dvar-torah-plugin:setup
```

The setup wizard checks your Sefaria connection, configures language, orientation, default thinkers, and writing style.

### 4. Write Your First Dvar Torah

```bash
/dvar-torah
```

The interactive wizard guides you through every choice — language, orientation, format, length, topic, thinkers, and occasion.

---

## Usage Examples

```bash
/dvar-torah                                              # Interactive wizard
/dvar-torah פרשת בראשית                                   # This week's parsha
/dvar-torah format: post, topic: divine providence        # Quick social post
/dvar-torah orientation: kabbalah, topic: sefirot          # Kabbalistic dvar torah
/dvar-torah orientation: hasidut, context: wedding         # Hasidic wedding speech
/dvar-torah format: shiur, length: shiur, topic: prophecy  # 45-min lesson plan
/dvar-torah type: research, topic: Code of Hammurabi       # Academic/historical
/dvar-torah format: dvar-torah, length: long, thinkers: Rambam, Crescas
```

---

## How It Works — Model-Smart Architecture

The plugin uses a three-tier model strategy to balance speed, depth, and quality:

```
Phase 0 — Selection (Haiku)                    ~5s
  └── Interactive wizard — instant responses

Phase 1 — Research (Haiku, parallel)           ~15s
  ├── Source researcher       → Sefaria lookups
  ├── Previous analyzer       → Learn from past writings
  ├── Historical researcher   → ANE parallels (if needed)
  └── Mussar researcher       → Ethics sources (if needed)

Phase 2 — Analysis (Sonnet + Haiku, parallel)  ~20s
  ├── Philosophical analyzer  → Deep reasoning
  └── Source verifier          → Verify every citation

Phase 3 — Writing (Opus)                       ~30s
  └── Torah writer            → Compose the final piece
```

> **Haiku** for selection and retrieval (fast). **Sonnet** for analysis (deep). **Opus** for writing (powerful).
> Total time: ~70 seconds for a fully researched, source-verified dvar torah.

---

## The 8 Skills

| Skill | What It Does |
|-------|-------------|
| **interactive-cli** | Guided wizard — language, orientation, format, length, topic, thinkers, occasion |
| **dvar-torah-writer** | Orchestrator — dispatches agents, assembles the final piece |
| **source-research** | Searches Sefaria for relevant texts across 15 API tools |
| **source-references** | Verifies every citation, formats uniform references |
| **philosophical-analysis** | Builds dialectical arguments between thinkers |
| **mussar-ethics** | Integrates ethical/practical dimensions |
| **historical-research** | ANE parallels, archaeology, biblical criticism |
| **previous-analysis** | Learns from your past writings — avoids repetition, detects patterns |

---

## Core Principles

1. **Retrieval over pre-training** — always search Sefaria before citing. Never fabricate.
2. **No unverified citations** — every source must pass Sefaria MCP verification.
3. **Learn from history** — analyze previous outputs to avoid repetition and maintain your voice.
4. **Respect every stream** — present each tradition in its strongest form.
5. **Depth with clarity** — dive into philosophical arguments, but explain technical terms.

---

## Output

All generated content is saved with full metadata:

```
output/divrei-torah/
  ├── dvar-torah/   2025-03-14-bereshit.md
  ├── posts/        2025-03-14-divine-providence.md
  └── shiurim/      2025-03-14-prophecy.md
```

Each file includes frontmatter with date, format, orientation, thinkers, source count, and agents used.

---

## MCP Dependencies

| Server | Status | Purpose |
|--------|--------|---------|
| **Sefaria** | Required | 15 tools for texts, search, links, calendar, dictionaries |
| **Sequential Thinking** | Recommended | Complex multi-step philosophical reasoning |
| **Memory** | Optional | Persistent thinker profiles and recurring themes |

The `.mcp.json` is pre-configured for Sequential Thinking and Memory. Sefaria connects via Account Connectors (see [Quick Start](#1-connect-to-sefaria-mcp-required)).

---

## Project Structure

```
plugins/
  dvar-torah-plugin/          ← v4.0 — all orientations, parallel agents
    skills/                     8 skills
    commands/                   /dvar-torah command
    CLAUDE.md                   Architecture guide
  rational-dvar-torah/        ← v2.0 — philosophy-focused
    skills/                     8 skills
    commands/                   /dvar-torah command
    CLAUDE.md                   Architecture guide
src/                          ← Source templates
output/divrei-torah/          ← Your generated content
manifests/                    ← Plugin manifests
scripts/                      ← Build scripts
```

## Build

```bash
npm run build
```

---

## License

MIT

---

<p align="center">
<strong>Built with Sefaria MCP + Claude Code</strong><br>
<sub>Write Torah grounded in real sources. Share wisdom backed by tradition.</sub>
</p>
