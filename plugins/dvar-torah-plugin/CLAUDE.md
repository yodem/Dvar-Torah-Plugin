# דבר תורה — Dvar Torah Plugin v4.0

## Architecture — Parallel Agent Orchestration

```
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

## Formats & Lengths

| פורמט | אורכים | תיאור |
|-------|--------|-------|
| **דבר תורה** | קצר (5 דק) · בינוני (10-15 דק) · ארוך (30 דק) | מובנה עם ניתוח |
| **פוסט** | קצר (5 דק) | נגיש, ממוקד, לרשתות/בלוג |
| **שיעור** | שיעור (45 דק) | מערך שיעור עם מקורות ושאלות |

## Orientations (5)

| אוריינטציה | הוגים מרכזיים | Sefaria |
|-----------|--------------|---------|
| **פילוסופיה** | רמב״ם, רס״ג, רלב״ג, קרשקש, אלבו, הלוי | Guide for the Perplexed, Kuzari |
| **קבלה** | זוהר, רמ״ק, האר״י, רמח״ל | Zohar, Etz Chaim, Pardes Rimonim |
| **חסידות** | בעש״ט, מגיד, תניא, ברסלב | Tanya, Likkutei Moharan |
| **חז״ל** | תנאים, אמוראים, מדרשים | Talmud Bavli, Bereishit Rabbah |
| **מודרני** | קאופמן, קסוטו, פינס, אלטמן | + ANE texts |

## Contexts (9)

לידה · ברית מילה · בר/בת מצווה · נישואין · שבת · חג · שבעה · יארצייט · כללי

## MCP Dependencies

- **claude_ai_Sefaria** (required): 15 כלים לטקסטים, חיפוש, קשרים
- **sequential-thinking** (recommended): חשיבה מורכבת לניתוח פילוסופי
- **memory** (optional): דפוסי כתיבה

## Core Principles

> 1. העדף מחקר מקורות (retrieval) על ידע מוקדם (pre-training)
> 2. אף ציטוט בלי אימות ב-Sefaria MCP
> 3. למד מכתיבות קודמות — הימנע מחזרות
> 4. הכבד כל זרם מחשבה — ללא דחייה פסקנית
> 5. **חכמת מודלים**: haiku למחקר, sonnet לניתוח, opus לכתיבה בלבד

## Skills (8)

| # | Skill | תיאור |
|---|-------|-------|
| 1 | **interactive-cli** | אשף אינטראקטיבי — שפה, אוריינטציה, פורמט, אורך, נושא, הוגים, הקשר |
| 2 | **dvar-torah-writer** | **Orchestrator** — מתזמן סוכנים במקביל, מרכיב תוצאות |
| 3 | **source-research** | מחקר מקורות דרך Sefaria MCP |
| 4 | **source-references** | אימות מראי מקומות ופורמט אחיד |
| 5 | **philosophical-analysis** | ניתוח פילוסופי מעמיק |
| 6 | **mussar-ethics** | שילוב ממד מוסרי-מעשי |
| 7 | **historical-research** | מחקר היסטורי — המזרח הקדום, ארכאולוגיה |
| 8 | **previous-analysis** | ניתוח כתיבות קודמות — דפוסים, סגנון |

## Agents (6)

| Agent | Model | Role | Phase |
|-------|-------|------|-------|
| **source-researcher** | haiku | חיפוש מקורות ב-Sefaria | 1 |
| **previous-analyzer** | haiku | סריקת דפוסים מכתיבות קודמות | 1 |
| **historical-researcher** | haiku | הקשר היסטורי ותרבותי | 1 |
| **source-verifier** | haiku | אימות ציטוטים ופורמט | 2 |
| **philosophical-analyzer** | sonnet | ניתוח פילוסופי ודיאלוג | 2 |
| **torah-writer** | opus | כתיבה סופית בלבד | 3 |

## Output Directory

```
output/divrei-torah/
  ├── dvar-torah/YYYY-MM-DD-<topic>.md
  ├── posts/YYYY-MM-DD-<topic>.md
  └── shiurim/YYYY-MM-DD-<topic>.md
```
