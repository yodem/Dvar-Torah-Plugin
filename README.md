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

## What It Does

An interactive Claude Code plugin that writes Torah content grounded in real sources. You choose the orientation, format, length, occasion, and thinkers — the plugin researches, analyzes, verifies, and writes.

**Every single citation is retrieved and verified through Sefaria** — the world's largest open library of Jewish texts.

### Supported Orientations

| Stream | Thinkers & Texts |
|--------|-----------------|
| **Jewish Philosophy** | Rambam, Saadia Gaon, Gersonides, Crescas, Albo, Yehuda HaLevi, Bahya Ibn Paquda, Ran, Akeidat Yitzchak |
| **Kabbalah** | Zohar, Ari, Ramak, Ramchal, Abulafia, Baal HaSulam |
| **Hasidut** | Baal Shem Tov, Maggid, Tanya/Chabad, Breslov, Kedushat Levi, Izhbitz, R. Tzadok, Sefat Emet, Esh Kodesh |
| **Hazal / Midrash** | Mishnah, Tosefta, Bavli, Yerushalmi, Mekhilta, Sifra, Sifrei, Midrash Rabbah, Tanchuma, Pesikta, Yalkut Shimoni |
| **Modern Jewish Thought** | Rav Kook, Jonathan Sacks, Eliezer Berkovits, Y. Leibowitz + academic lenses (Kaufmann, Cassuto, etc.) |
| **Musar + Halakhic Frameworks** | Sha'arei Teshuvah, Orchot Tzadikim, Mesillat Yesharim, Mishneh Torah, Shulchan Arukh, Sefer HaChinukh |

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
/dvar-torah:setup
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

## The 9 Skills

| Skill | What It Does |
|-------|-------------|
| **wizard** | Guided interactive intake — language, orientation, format, length, topic, thinkers, context |
| **compose** | Orchestrator — dispatches agents in parallel and assembles the final output |
| **research** | Searches Sefaria for relevant texts across Torah, Hazal, Jewish Thought, Kabbalah, Hasidut, Musar |
| **verify** | Verifies every citation and standardizes references |
| **analyze** | Builds dialectical/philosophical arguments across selected thinkers |
| **mussar** | Integrates ethical/practical dimensions and action takeaways |
| **history** | ANE parallels, archaeology, historical context |
| **previous** | Learns from your past writings — avoids repetition, detects patterns |
| **setup** | Configuration and readiness wizard |

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
  dvar-torah-plugin/          ← canonical plugin root (v4.2)
    .claude-plugin/plugin.json  canonical plugin manifest
    skills/                     9 skills
    commands/                   /dvar-torah command
    agents/                     7 specialized agents
    hooks/                      PostToolUse + Stop validation hooks
    scripts/                    Sefaria REST API helper
    CLAUDE.md                   architecture + routing guide
.claude-plugin/
  marketplace.json            ← marketplace catalog metadata
output/divrei-torah/          ← generated content
scripts/                      ← repository maintenance scripts
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
