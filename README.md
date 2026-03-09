# דבר תורה רציונלי — Rational Dvar Torah Plugin

Claude Code plugin for writing philosophical/rationalist Dvar Torah, drawing from Jewish philosophical thinkers and powered by Sefaria MCP.

## הוגים מרכזיים | Featured Thinkers

### פילוסופיה רציונלית
- **רמב״ם** — מורה נבוכים, משנה תורה
- **רס״ג** — אמונות ודעות
- **רלב״ג** — מלחמות ה׳
- **קרשקש** — אור ה׳
- **אלבו** — ספר העיקרים
- **אבן עזרא** — פירושים על התנ״ך
- **ר״י הלוי** — הכוזרי

### מוסר
- **רמח״ל** — מסילת ישרים, דרך ה׳
- **חובות הלבבות** — רבי בחיי אבן פקודה
- **שערי תשובה** — רבינו יונה

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

The `.mcp.json` in this repo is pre-configured to connect to `http://localhost:8089/sse`.

## Usage

```
/dvar-torah פרשת בראשית
/dvar-torah נושא: השגחה פרטית
/dvar-torah חג: פסח, הוגים: רמב״ם, קרשקש
/dvar-torah                    # פרשת השבוע הנוכחית
```

## Skills

| Skill | Description |
|-------|-------------|
| `dvar-torah-writer` | כותב ראשי — מתזמן את כל תהליך הכתיבה |
| `source-research` | מחקר מקורות דרך Sefaria MCP |
| `philosophical-analysis` | ניתוח פילוסופי מעמיק |
| `mussar-ethics` | שילוב ממד מוסרי-מעשי |

## Agents

| Agent | Model | Role |
|-------|-------|------|
| `torah-philosopher` | Opus | סוכן ראשי — כתיבה וניתוח |
| `source-researcher` | Sonnet | מחקר מקורות מהיר |

## Structure

```
src/
  skills/           ← Edit here
    dvar-torah-writer/
    source-research/
    philosophical-analysis/
    mussar-ethics/
  agents/
  settings/
plugins/
  rational-dvar-torah/  ← Generated output
manifests/
scripts/
```

## Build

```bash
npm run build
```

## License

MIT
