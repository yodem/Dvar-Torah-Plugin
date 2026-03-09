# דבר תורה רציונלי — Rational Dvar Torah Plugin

## Agent Routing Index

כשמשתמש מבקש לכתוב דבר תורה, נתב לסוכן ולמיומנות המתאימים:

| בקשה | סוכן | מיומנות |
|------|------|---------|
| כתוב דבר תורה / Write a dvar torah | torah-philosopher | dvar-torah-writer |
| חפש מקורות / Find sources | source-researcher | source-research |
| נתח פילוסופית / Analyze philosophically | torah-philosopher | philosophical-analysis |
| הוסף מוסר / Add mussar dimension | torah-philosopher | mussar-ethics |

## Quick Start

```
/dvar-torah פרשת בראשית
/dvar-torah נושא: השגחה פרטית
/dvar-torah חג: פסח
```

## MCP Dependencies

- **sefaria** (required): ספריית ספריא — טקסטים, חיפוש, קשרים
- **sequential-thinking** (recommended): חשיבה מורכבת לניתוח פילוסופי
- **memory** (optional): זיכרון עבור נושאים חוזרים

## Core Principle

> העדף מחקר מקורות (retrieval) על ידע מוקדם (pre-training).
> תמיד חפש ב-Sefaria לפני שמצטט מזיכרון.

## Skills

1. **dvar-torah-writer** — כותב ראשי, מתזמן את כל התהליך
2. **source-research** — מחקר מקורות דרך Sefaria MCP
3. **philosophical-analysis** — ניתוח פילוסופי מעמיק
4. **mussar-ethics** — שילוב ממד מוסרי-מעשי

## Agents

1. **torah-philosopher** (Opus) — סוכן ראשי לכתיבת דבר תורה
2. **source-researcher** (Sonnet) — סוכן מחקר מקורות מהיר

## הוגים מרכזיים

### פילוסופיה רציונלית
רמב״ם · רס״ג · רלב״ג · קרשקש · אלבו · אבן עזרא · ר״י הלוי · אבן פקודה

### מוסר
רמח״ל · רבינו יונה · ר׳ ישראל סלנטר · חזון אי״ש
