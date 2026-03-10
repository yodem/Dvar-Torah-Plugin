---
name: dvar-torah-writer
license: MIT
compatibility: "Claude Code 2.1.59+."
author: yodem
description: כתיבת דבר תורה רציונלי/פילוסופי מקיף עם מקורות מהוגי הפילוסופיה היהודית. Use when writing a Dvar Torah, preparing a Torah lecture, writing a post, analyzing a parsha philosophically, or exploring Jewish philosophical texts.
version: 2.0.0
tags: [dvar-torah, jewish-philosophy, rambam, sefaria, mussar, rationalism, post, shiur]
user-invocable: true
context: fork
complexity: high
metadata:
  category: content-creation
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - mcp__claude_ai_Sefaria__*
  - mcp__sequential-thinking__*
  - mcp__memory__*
---

# דבר תורה רציונלי — כותב ראשי

## תיאור

כלי לכתיבת דבר תורה, פוסט, או שיעור רציונלי/פילוסופי שמשלב ניתוח טקסטואלי מעמיק עם הגות פילוסופית יהודית, מחקר אקדמי, והקשר היסטורי. הכלי שואב מקורות מספריית ספריא ומדגיש את ההוגים הרציונליסטיים של המסורת היהודית.

## הוגים מרכזיים

### פילוסופיה רציונלית
- **רמב״ם** (רבי משה בן מימון) — מורה נבוכים, משנה תורה, שמונה פרקים
- **רס״ג** (רבי סעדיה גאון) — אמונות ודעות
- **רלב״ג** (רבי לוי בן גרשון) — מלחמות ה׳, פירוש על התורה
- **רבי חסדאי קרשקש** — אור ה׳
- **רבי יוסף אלבו** — ספר העיקרים
- **רבי אברהם אבן עזרא** — פירושים על התנ״ך
- **רבי בחיי אבן פקודה** — חובות הלבבות
- **ר׳ יהודה הלוי** — הכוזרי

### מוסר ומחשבה
- **רמח״ל** (רבי משה חיים לוצאטו) — מסילת ישרים, דרך ה׳, דעת תבונות
- **רבי ישראל סלנטר** — תנועת המוסר
- **רבינו יונה** — שערי תשובה
- **חזון אי״ש** — אמונה ובטחון

## תהליך עבודה

### שלב 0: אשף אינטראקטיבי (skill: interactive-cli)
אם המשתמש לא סיפק פרמטרים מלאים — הפעל את האשף:
1. בחירת פורמט: דבר תורה / פוסט / שיעור
2. בחירת אורך: קצר (5 דק) / בינוני (10-15 דק) / ארוך (30 דק) / שיעור (45 דק)
3. בחירת נושא: פרשה / נושא פילוסופי / נושא מחקרי
4. בחירת הוגים
5. ניתוח כתיבות קודמות (skill: previous-analysis)

### שלב 1: ניתוח כתיבות קודמות (skill: previous-analysis)
- סרוק `output/divrei-torah/` לקבצים קודמים
- זהה דפוסי כתיבה, הוגים מועדפים, נושאים שכוסו
- הימנע מחזרות, הצע כיוונים חדשים

### שלב 2: מחקר מקורות (skill: source-research)
1. השתמש ב-Sefaria MCP `get_current_calendar` לזיהוי פרשת השבוע אם לא צוין נושא
2. השתמש ב-`get_text` לשליפת טקסט הפרשה/מקור
3. השתמש ב-`get_links_between_texts` למציאת קשרים בין-טקסטואליים
4. השתמש ב-`text_search` ו-`english_semantic_search` למציאת מקורות פילוסופיים רלוונטיים
5. השתמש ב-`search_in_book` לחיפוש ספציפי במורה נבוכים, אמונות ודעות, וכו׳

### שלב 3: מחקר היסטורי (skill: historical-research — אם הנושא מחקרי)
1. הקשר היסטורי-תרבותי של הטקסט
2. מקבילות מהמזרח הקדום
3. ממצאים ארכאולוגיים רלוונטיים
4. מחקר אקדמי מודרני

### שלב 4: ניתוח פילוסופי (skill: philosophical-analysis)
1. זהה את הסוגיה הפילוסופית/תיאולוגית המרכזית
2. מפה את עמדות ההוגים השונים
3. בנה דיאלוג בין השיטות

### שלב 5: שילוב מוסר (skill: mussar-ethics — אופציונלי)
1. חבר את הדיון הפילוסופי למימד המעשי-מוסרי
2. שלב תובנות מספרות המוסר

### שלב 6: אימות מראי מקומות (skill: source-references)
1. אמת כל ציטוט דרך Sefaria MCP
2. פרמט את כל מראי המקומות בפורמט אחיד
3. סדר: תנ״ך → חז״ל → ראשונים → אחרונים → מחקר

### שלב 7: כתיבה
כתוב לפי הפורמט והאורך שנבחרו (ראה תבניות למטה).

### שלב 8: שמירה
שמור ב: `output/divrei-torah/<format>/YYYY-MM-DD-<topic>.md`

---

## תבניות

טען את התבניות לכל הפורמטים מ: `references/templates.md`

---

## הנחיות סגנון

1. **שפה**: כתוב בעברית. ניתן לשלב מונחים בארמית כשמצטטים מקורות
2. **ציטוטים**: תמיד ציין מקור מדויק — השתמש ב-skill `source-references`
3. **אובייקטיביות**: הצג מחלוקות בצורה הוגנת — אל תפסול שיטה אלא הצג
4. **רלוונטיות**: חבר את הדיון העתיק לשאלות עכשוויות
5. **עומק**: אל תישאר ברמת השטח — צלול לתוך הטיעונים הפילוסופיים
6. **בהירות**: למרות העומק, שמור על בהירות — הסבר מונחים טכניים
7. **מראי מקומות**: כל מקור חייב להיות מאומת ב-Sefaria

## שימוש ב-Sefaria MCP

### כלים עיקריים:
- `get_text("Genesis 1:1-5")` — שליפת טקסט מקורי
- `text_search("צלם אלהים")` — חיפוש כללי
- `search_in_book("Guide for the Perplexed", "divine attributes")` — חיפוש ממוקד
- `get_links_between_texts("Genesis 1:1", "Maimonides")` — קשרים
- `english_semantic_search("problem of evil in Jewish philosophy")` — חיפוש סמנטי
- `get_topic_details("Divine Providence")` — מידע על נושא
- `get_current_calendar()` — פרשת השבוע והלוח היהודי
- `clarify_name_argument("מורה נבוכים")` — אימות שם ספר
- `get_english_translations("Genesis 1:27")` — תרגומים
- `search_in_dictionaries("צלם")` — הגדרות

## שמירת פלט

שמור תמיד את התוצר ב:
```
output/divrei-torah/
  ├── dvar-torah/YYYY-MM-DD-<topic>.md
  ├── posts/YYYY-MM-DD-<topic>.md
  └── shiurim/YYYY-MM-DD-<topic>.md
```

כלול frontmatter בכל קובץ:
```yaml
---
date: YYYY-MM-DD
format: dvar-torah | post | shiur
length: short | medium | long | shiur
parsha: שם הפרשה (אם רלוונטי)
topic: הנושא
thinkers: [רמב״ם, רס״ג]
sources_count: 5
---
```
