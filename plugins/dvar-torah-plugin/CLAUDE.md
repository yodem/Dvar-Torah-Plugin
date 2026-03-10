# דבר תורה — Dvar Torah Plugin v3.0

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
/dvar-torah                                              ← אשף אינטראקטיבי (שפה + אוריינטציה + נושא)
/dvar-torah פרשת בראשית                                   ← פרשה ספציפית
/dvar-torah פורמט: פוסט, נושא: השגחה                       ← פוסט קצר
/dvar-torah פורמט: שיעור, אורך: שיעור, נושא: נבואה         ← שיעור 45 דק
/dvar-torah אוריינטציה: קבלה, נושא: ספירות               ← קבלה
/dvar-torah אוריינטציה: חסידות, הקשר: חתונה               ← חסידות + הקשר
/dvar-torah סוג: מחקרי, נושא: חוקי חמורבי בפרשת משפטים    ← מחקרי
```

## פורמטים ואורכים

| פורמט | אורכים זמינים | תיאור |
|-------|--------------|-------|
| **דבר תורה** | קצר (5 דק) · בינוני (10-15 דק) · ארוך (30 דק) | מובנה עם ניתוח |
| **פוסט** | קצר (5 דק) | נגיש, ממוקד, לרשתות/בלוג |
| **שיעור** | שיעור (45 דק) | מערך שיעור עם מקורות לחילוק ושאלות |

## אוריינטציות (v3.0)

| אוריינטציה | הוגים מרכזיים | Sefaria |
|-----------|--------------|---------|
| **פילוסופיה יהודית** | רמב״ם, רס״ג, רלב״ג, קרשקש, אלבו, הלוי | Guide for the Perplexed, Kuzari |
| **קבלה** | זוהר, רמ״ק, האר״י, רמח״ל | Zohar, Etz Chaim, Pardes Rimonim |
| **חסידות** | בעש״ט, מגיד, תניא, ברסלב | Tanya, Likkutei Moharan |
| **חז״ל** | תנאים, אמוראים, מדרשים | Talmud Bavli, Bereishit Rabbah |
| **חוקרים מודרניים** | קאופמן, קסוטו, פינס, אלטמן | + ANE texts |

## סוגי נושאים

| סוג | תת-נושאים | skills |
|-----|-----------|--------|
| **פרשת השבוע** | אוטומטי מ-Sefaria calendar | source-research, philosophical-analysis |
| **פילוסופי** | תיאולוגיה · אתיקה · אפיסטמולוגיה · מטאפיזיקה | philosophical-analysis |
| **מחקרי** | הקשר היסטורי · מחקר המקרא · המזרח הקדום · ארכאולוגיה | historical-research |

## הקשרים (v3.0)

לידה · ברית מילה · בר/בת מצווה · נישואין · שבת · חג · שבעה · יארצייט · כללי

## MCP Dependencies

- **claude_ai_Sefaria** (required, via Claude connector): ספריית ספריא — 15 כלים לטקסטים, חיפוש, קשרים, לוח, כתבי יד
- **sequential-thinking** (recommended): חשיבה מורכבת לניתוח פילוסופי
- **memory** (optional): זיכרון — דפוסי כתיבה, נושאים חוזרים

## Core Principles

> 1. העדף מחקר מקורות (retrieval) על ידע מוקדם (pre-training). תמיד חפש ב-Sefaria לפני שמצטט.
> 2. אף ציטוט בלי אימות. כל מראה מקום חייב לעבור אימות ב-Sefaria MCP.
> 3. למד מכתיבות קודמות. נתח דפוסים, הימנע מחזרות, שמור על עקביות סגנונית.
> 4. הכבד כל זרם מחשבה — הצג בנאמנות ובכבוד, ללא דחייה פסקנית.

## Skills (8)

| # | Skill | תיאור |
|---|-------|-------|
| 1 | **interactive-cli** | אשף אינטראקטיבי — שפה, אוריינטציה, פורמט, אורך, נושא, הוגים, הקשר |
| 2 | **dvar-torah-writer** | כותב ראשי — מתזמן את כל התהליך, תבניות לכל פורמט ואורך |
| 3 | **source-research** | מחקר מקורות דרך Sefaria MCP |
| 4 | **source-references** | מראי מקומות מדויקים — אימות, פורמט אחיד, ביבליוגרפיה |
| 5 | **philosophical-analysis** | ניתוח פילוסופי מעמיק |
| 6 | **mussar-ethics** | שילוב ממד מוסרי-מעשי |
| 7 | **historical-research** | מחקר היסטורי — המזרח הקדום, ארכאולוגיה, ביקורת המקרא |
| 8 | **previous-analysis** | ניתוח כתיבות קודמות — דפוסים, סגנון, כתיבה על בסיס קודמים |

## Agents (2)

| Agent | Model | Role |
|-------|-------|------|
| **torah-philosopher** | Opus | סוכן ראשי — כתיבה, ניתוח, שילוב |
| **source-researcher** | Sonnet | מחקר מקורות מהיר, אימות מראי מקומות |

## הוגים לפי אוריינטציה

### פילוסופיה יהודית
רמב״ם · רס״ג · רלב״ג · קרשקש · אלבו · אבן עזרא · ר״י הלוי · אבן פקודה

### קבלה
זוהר (ר״ש בר יוחאי / ר״מ דה ליאון) · רמ״ק · האר״י · רמח״ל

### חסידות
בעש״ט · המגיד ממזריץ׳ · אדמו״ר הזקן (תניא) · ר׳ נחמן מברסלב · ר׳ לוי יצחק מברדיטשוב

### חז״ל
תנאים (משנה) · אמוראים (גמרא) · מדרשים (בראשית רבה, תנחומא)

### חוקרים מודרניים
קאופמן · קסוטו · פינס · אלטמן · הרווי · קלנר · הלברטל + ANE texts

## Output Directory

```
output/divrei-torah/
  ├── dvar-torah/YYYY-MM-DD-<topic>.md
  ├── posts/YYYY-MM-DD-<topic>.md
  └── shiurim/YYYY-MM-DD-<topic>.md
```
