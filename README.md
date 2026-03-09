# דבר תורה רציונלי — Rational Dvar Torah Plugin v2.0

Claude Code plugin for writing philosophical/rationalist Dvar Torah, posts, and shiurim. Draws from Jewish philosophical thinkers, academic research, and historical context. Powered by Sefaria MCP.

## Features

- **Interactive CLI** — guided wizard for choosing format, length, topic, and thinkers
- **3 formats** — Dvar Torah, Post, Shiur (lesson plan)
- **4 lengths** — Short (5 min), Medium (10-15 min), Long (30 min), Shiur (45 min)
- **3 topic types** — Parsha, Philosophical, Research/Historical
- **Precise source references** — every citation verified via Sefaria MCP
- **Previous analysis** — learns from your past writings, avoids repetition
- **Academic research** — Ancient Near East parallels, archaeology, biblical criticism

## הוגים מרכזיים | Featured Thinkers

### פילוסופיה רציונלית
רמב״ם · רס״ג · רלב״ג · קרשקש · אלבו · אבן עזרא · ר״י הלוי · אבן פקודה

### מוסר
רמח״ל · רבינו יונה · ר׳ ישראל סלנטר · חזון אי״ש

### מחקר מודרני
פינס · אלטמן · הרווי · קלנר · הלברטל · לורברבוים · קאופמן · גרינברג

## Installation

```bash
/plugin install rational-dvar-torah
```

## Sefaria MCP Setup

This plugin requires the [Sefaria MCP server](https://github.com/Sefaria/sefaria-mcp):

```bash
# Option 1: Docker (recommended)
docker build -t sefaria-mcp https://github.com/Sefaria/sefaria-mcp.git
docker run -d --name sefaria-mcp -p 8089:8088 sefaria-mcp

# Option 2: Local
git clone https://github.com/Sefaria/sefaria-mcp.git
cd sefaria-mcp
pip install -e .
python -m sefaria_mcp.main
```

The `.mcp.json` is pre-configured to connect to `http://localhost:8089/sse`.

## Usage

```bash
/dvar-torah                                            # Interactive wizard
/dvar-torah פרשת בראשית                                 # Specific parsha
/dvar-torah פורמט: פוסט, נושא: השגחה פרטית               # Short post
/dvar-torah פורמט: שיעור, אורך: שיעור, נושא: נבואה       # 45-min lesson plan
/dvar-torah סוג: מחקרי, נושא: חוקי חמורבי בפרשת משפטים   # Academic/historical
/dvar-torah פורמט: דבר-תורה, אורך: ארוך, הוגים: רמב״ם, קרשקש
```

## Formats & Lengths

| Format | Lengths | Description |
|--------|---------|-------------|
| **דבר תורה** | קצר (5 דק) · בינוני (10-15 דק) · ארוך (30 דק) | Structured with philosophical analysis |
| **פוסט** | קצר (5 דק) | Short, accessible, for social/blog |
| **שיעור** | שיעור (45 דק) | Full lesson plan with source sheets and discussion questions |

## Topic Types

| Type | Sub-topics |
|------|-----------|
| **פרשת השבוע** | Auto-detected from Sefaria calendar |
| **פילוסופי** | Theology · Ethics · Epistemology · Metaphysics |
| **מחקרי** | Historical context · Biblical criticism · Ancient Near East · Archaeology |

## Skills (8)

| Skill | Description |
|-------|-------------|
| `interactive-cli` | אשף אינטראקטיבי — בחירת פורמט, אורך, נושא, הוגים |
| `dvar-torah-writer` | כותב ראשי — תבניות לכל פורמט ואורך |
| `source-research` | מחקר מקורות דרך Sefaria MCP |
| `source-references` | מראי מקומות מדויקים — אימות ופורמט אחיד |
| `philosophical-analysis` | ניתוח פילוסופי מעמיק |
| `mussar-ethics` | שילוב ממד מוסרי-מעשי |
| `historical-research` | מחקר היסטורי — המזרח הקדום, ארכאולוגיה |
| `previous-analysis` | ניתוח כתיבות קודמות — דפוסים וסגנון |

## Agents

| Agent | Model | Role |
|-------|-------|------|
| `torah-philosopher` | Opus | Primary — writing, analysis, integration |
| `source-researcher` | Sonnet | Fast source lookup and verification |

## Structure

```
src/
  skills/               ← Edit here
    interactive-cli/        CLI wizard
    dvar-torah-writer/      Main writer
    source-research/        Sefaria search
    source-references/      Citation verification
    philosophical-analysis/ Philosophical analysis
    mussar-ethics/          Mussar integration
    historical-research/    Historical/academic research
    previous-analysis/      Learn from past writings
  agents/
  settings/
plugins/
  rational-dvar-torah/  ← Generated output
output/
  divrei-torah/         ← Written outputs
    dvar-torah/
    posts/
    shiurim/
manifests/
scripts/
```

## Build

```bash
npm run build
```

## License

MIT
