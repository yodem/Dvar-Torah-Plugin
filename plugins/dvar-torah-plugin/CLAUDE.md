# דבר תורה — Dvar Torah Plugin v4.2

## Architecture — Parallel Agent Orchestration

```
Phase 0 — Selection (haiku)                   ~5s
  └── wizard              ← fast wizard, instant responses

Phase 1 — Research (parallel, haiku)          ~15s
  ├── previous-analyzer     ← scan output/ for patterns
  ├── source-researcher     ← Sefaria lookups
  ├── historical-researcher ← ANE, archaeology (conditional)
  └── source-researcher     ← mussar sources (conditional)

Phase 2 — Analysis + Verification (parallel)  ~20s
  ├── philosophical-analyzer ← sonnet: deep reasoning
  └── source-verifier        ← haiku: verify citations

Phase 3 — Writing (opus)                      ~30s
  └── torah-writer           ← compose final piece
```

## Agent Routing Index

| בקשה | סוכן | Model | תפקיד |
|------|------|-------|-------|
| כתוב דבר תורה | torah-writer | **opus** | כתיבה סופית בלבד |
| חפש מקורות | source-researcher | **haiku** | חיפוש ב-Sefaria |
| נתח קודמים | previous-analyzer | **haiku** | סריקת דפוסים |
| חקור היסטורי | historical-researcher | **haiku** | הקשר תרבותי |
| נתח פילוסופית | philosophical-analyzer | **sonnet** | ניתוח ודיאלוג |
| אמת מקורות | source-verifier | **haiku** | אימות ציטוטים |

## Quick Start

```
/dvar-torah                                              ← אשף אינטראקטיבי
/dvar-torah פרשת בראשית                                   ← פרשה ספציפית
/dvar-torah פורמט: פוסט, נושא: השגחה                       ← פוסט קצר
/dvar-torah פורמט: שיעור, אורך: שיעור, נושא: נבואה         ← שיעור 45 דק
/dvar-torah אוריינטציה: קבלה, נושא: ספירות               ← קבלה
/dvar-torah אוריינטציה: חסידות, הקשר: חתונה               ← חסידות + הקשר
/dvar-torah סוג: מחקרי, נושא: חוקי חמורבי בפרשת משפטים    ← מחקרי
```

## Standalone Skills

```
/dvar-torah:compose     ← direct compose (skip wizard)
/dvar-torah:research    ← standalone Sefaria search
/dvar-torah:analyze     ← standalone philosophical analysis
/dvar-torah:history     ← standalone historical context
/dvar-torah:previous    ← analyze previous writings (patterns + recommendations)
/dvar-torah:previous --base  ← extract writing template from selected pieces
/dvar-torah:setup       ← configuration wizard
```

## Formats & Lengths

| פורמט | אורכים | תיאור |
|-------|--------|-------|
| **דבר תורה** | קצר (5 דק) · בינוני (10-15 דק) · ארוך (30 דק) | מובנה עם ניתוח |
| **פוסט** | קצר (5 דק) | נגיש, ממוקד, לרשתות/בלוג |
| **שיעור** | שיעור (45 דק) | מערך שיעור עם מקורות ושאלות |

## Orientations (5)

| אוריינטציה | הוגים מרכזיים | Sefaria |
|-----------|--------------|---------|
| **פילוסופיה** | רמב״ם, רס״ג, רלב״ג, קרשקש, אלבו, ריה״ל, אבן פקודה, הר״ן | Guide for the Perplexed, HaEmunot veHaDeot, Kuzari |
| **קבלה** | זוהר, רמ״ק, האר״י, רמח״ל, אבולעפיה, בעל הסולם | Zohar, Etz Chaim, Pardes Rimonim, Talmud Eser HaSefirot |
| **חסידות** | בעש״ט, מגיד, תניא, ברסלב, קדושת לוי, איזביצא, ר׳ צדוק, שפת אמת | Tanya, Likutei Moharan, Kedushat Levi, Mei HaShiloach |
| **חז״ל** | משנה/תוספתא, בבלי/ירושלמי, מדרשי הלכה ואגדה | Mishnah, Talmud Bavli, Jerusalem Talmud, Midrash Rabbah |
| **מודרני** | הרב קוק, הרב זקס, ברקוביץ, ליבוביץ (+ קאופמן/קסוטו כרקע מחקרי) | Orot, Rabbi Lord Jonathan Sacks corpus, thematic search |

## Contexts (9)

לידה · ברית מילה · בר/בת מצווה · נישואין · שבת · חג · שבעה · יארצייט · כללי

## MCP Dependencies

- **claude_ai_Sefaria** (bundled): Sefaria MCP is configured via `.mcp.json` in this plugin directory — no manual setup required. 15 tools for texts, search, links, calendar.
- **sequential-thinking** (recommended): חשיבה מורכבת לניתוח פילוסופי
- **memory** (optional): דפוסי כתיבה

## API Script (v4.1)

`scripts/sefaria_api.py` — direct REST calls, faster than MCP for known references:
```
python scripts/sefaria_api.py get-text "Genesis 1:1"
python scripts/sefaria_api.py get-calendar
python scripts/sefaria_api.py get-links "Berakhot 5a"
```
Use MCP `english_semantic_search` for discovery; API script for targeted lookups.

## Core Principles

> 1. העדף מחקר מקורות (retrieval) על ידע מוקדם (pre-training)
> 2. אף ציטוט בלי אימות ב-Sefaria MCP
> 3. **שטיינזלץ לפשט**: קרא שטיינזלץ להבנת הפשט לפני ניתוח — `get_text("Steinsaltz on ...")`
> 4. למד מכתיבות קודמות — הימנע מחזרות
> 5. הכבד כל זרם מחשבה — ללא דחייה פסקנית
> 6. **חכמת מודלים**: haiku לבחירות ומחקר, sonnet לניתוח, opus לכתיבה בלבד

## Skills (9)

| # | Skill | Displays as | תיאור |
|---|-------|-------------|-------|
| 1 | **wizard** | `dvar-torah:wizard` | אשף אינטראקטיבי — שפה, אוריינטציה, פורמט, אורך, נושא, הוגים, הקשר |
| 2 | **compose** | `dvar-torah:compose` | **Orchestrator** — מתזמן סוכנים במקביל, מרכיב תוצאות |
| 3 | **research** | `dvar-torah:research` | מחקר מקורות דרך Sefaria MCP |
| 4 | **verify** | `dvar-torah:verify` | אימות מראי מקומות ופורמט אחיד |
| 5 | **analyze** | `dvar-torah:analyze` | ניתוח פילוסופי מעמיק |
| 6 | **mussar** | `dvar-torah:mussar` | שילוב ממד מוסרי-מעשי |
| 7 | **history** | `dvar-torah:history` | מחקר היסטורי — המזרח הקדום, ארכאולוגיה |
| 8 | **previous** | `dvar-torah:previous` | ניתוח כתיבות קודמות — דפוסים, סגנון |
| 9 | **setup** | `dvar-torah:setup` | אשף הגדרות |

## Agents (7)

| Agent | Skill | Model | Role | Phase |
|-------|-------|-------|------|-------|
| — | **wizard** | haiku | אשף אינטראקטיבי — בחירות מהירות | 0 |
| **source-researcher** | research | haiku | חיפוש מקורות ב-Sefaria | 1 |
| **previous-analyzer** | previous | haiku | סריקת דפוסים מכתיבות קודמות | 1 |
| **historical-researcher** | history | haiku | הקשר היסטורי ותרבותי | 1 |
| **source-verifier** | verify | haiku | אימות ציטוטים ופורמט | 2 |
| **philosophical-analyzer** | analyze | sonnet | ניתוח פילוסופי ודיאלוג | 2 |
| **torah-writer** | compose | opus | כתיבה סופית בלבד | 3 |

## Output Directory

```
output/divrei-torah/
  ├── dvar-torah/YYYY-MM-DD-<topic>.md
  ├── posts/YYYY-MM-DD-<topic>.md
  └── shiurim/YYYY-MM-DD-<topic>.md
```
