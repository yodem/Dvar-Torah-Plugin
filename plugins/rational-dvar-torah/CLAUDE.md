# דבר תורה רציונלי — Rational Dvar Torah Plugin v2.0

## Agent Routing Index

| בקשה | סוכן | מיומנות |
|------|------|---------|
| כתוב דבר תורה / Write a dvar torah | torah-philosopher | interactive-cli → dvar-torah-writer |
| כתוב פוסט / Write a post | torah-philosopher | interactive-cli → dvar-torah-writer |
| הכן שיעור / Prepare a shiur | torah-philosopher | interactive-cli → dvar-torah-writer |
| חפש מקורות / Find sources | source-researcher | source-research |
| נתח פילוסופית / Analyze philosophically | torah-philosopher | philosophical-analysis |
| הוסף מוסר / Add mussar | torah-philosopher | mussar-ethics |
| חקור הקשר היסטורי / Historical context | torah-philosopher | historical-research |
| אמת מקורות / Verify sources | source-researcher | source-references |
| נתח כתיבות קודמות / Analyze previous | torah-philosopher | previous-analysis |

## Quick Start

```
/dvar-torah                                          ← אשף אינטראקטיבי
/dvar-torah פרשת בראשית                               ← פרשה ספציפית
/dvar-torah פורמט: פוסט, נושא: השגחה                   ← פוסט קצר
/dvar-torah פורמט: שיעור, אורך: שיעור, נושא: נבואה     ← שיעור 45 דק
/dvar-torah סוג: מחקרי, נושא: חוקי חמורבי בפרשת משפטים  ← מחקרי
```

## פורמטים ואורכים

| פורמט | אורכים זמינים | תיאור |
|-------|--------------|-------|
| **דבר תורה** | קצר (5 דק) · בינוני (10-15 דק) · ארוך (30 דק) | מובנה עם ניתוח פילוסופי |
| **פוסט** | קצר (5 דק) | נגיש, ממוקד, לרשתות/בלוג |
| **שיעור** | שיעור (45 דק) | מערך שיעור עם מקורות לחילוק ושאלות |

## סוגי נושאים

| סוג | תת-נושאים | skills |
|-----|-----------|--------|
| **פרשת השבוע** | אוטומטי מ-Sefaria calendar | source-research, philosophical-analysis |
| **פילוסופי** | תיאולוגיה · אתיקה · אפיסטמולוגיה · מטאפיזיקה | philosophical-analysis |
| **מחקרי** | הקשר היסטורי · מחקר המקרא · המזרח הקדום · ארכאולוגיה | historical-research |

## MCP Dependencies

- **claude_ai_Sefaria** (required): 15 tools for texts, search, links, calendar. Connect via Claude Account Connectors (claude.ai/settings/integrations) or `claude mcp add-oauth Sefaria`
- **sequential-thinking** (recommended): חשיבה מורכבת לניתוח פילוסופי
- **memory** (optional): זיכרון — דפוסי כתיבה, נושאים חוזרים

## Core Principles

> 1. העדף מחקר מקורות (retrieval) על ידע מוקדם (pre-training). תמיד חפש ב-Sefaria לפני שמצטט.
> 2. אף ציטוט בלי אימות. כל מראה מקום חייב לעבור אימות ב-Sefaria MCP.
> 3. למד מכתיבות קודמות. נתח דפוסים, הימנע מחזרות, שמור על עקביות סגנונית.

## Skills (8)

| # | Skill | תיאור |
|---|-------|-------|
| 1 | **interactive-cli** | אשף אינטראקטיבי — בחירת פורמט, אורך, נושא, הוגים |
| 2 | **dvar-torah-writer** | כותב ראשי — מתזמן את כל התהליך, תבניות לכל פורמט ואורך |
| 3 | **source-research** | מחקר מקורות דרך Sefaria MCP |
| 4 | **source-references** | מראי מקומות מדויקים — אימות, פורמט אחיד, ביבליוגרפיה |
| 5 | **philosophical-analysis** | ניתוח פילוסופי מעמיק |
| 6 | **mussar-ethics** | שילוב ממד מוסרי-מעשי |
| 7 | **historical-research** | מחקר היסטורי — המזרח הקדום, ארכאולוגיה, ביקורת המקרא |
| 8 | **previous-analysis** | ניתוח כתיבות קודמות — דפוסים, סגנון, המלצות |

## Agents & Model Routing

| Agent / Skill | Model | Role |
|-------|-------|------|
| **interactive-cli** | Haiku | אשף אינטראקטיבי — בחירות מהירות |
| **source-researcher** | Sonnet | מחקר מקורות מהיר, אימות מראי מקומות |
| **torah-philosopher** | Opus | סוכן ראשי — כתיבה, ניתוח, שילוב |

> Haiku handles the wizard for instant responsiveness. Sonnet does research. Opus writes.

## הוגים

### פילוסופיה רציונלית
רמב״ם · רס״ג · רלב״ג · קרשקש · אלבו · אבן עזרא · ר״י הלוי · אבן פקודה

### מוסר
רמח״ל · רבינו יונה · ר׳ ישראל סלנטר · חזון אי״ש

### מחקר מודרני
פינס · אלטמן · הרווי · קלנר · הלברטל · לורברבוים · קאופמן · גרינברג

## Output Directory

```
output/divrei-torah/
  ├── dvar-torah/YYYY-MM-DD-<topic>.md
  ├── posts/YYYY-MM-DD-<topic>.md
  └── shiurim/YYYY-MM-DD-<topic>.md
```
