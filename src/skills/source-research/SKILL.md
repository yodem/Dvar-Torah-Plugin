---
name: source-research
license: MIT
compatibility: "Claude Code 2.1.59+."
author: yodem
description: מחקר מקורות מעמיק בספריית ספריא עבור דבר תורה פילוסופי. Use when searching Jewish texts, finding sources in Sefaria, or building a source bibliography.
version: 1.0.0
tags: [sefaria, source-research, jewish-texts, bibliography]
user-invocable: false
disable-model-invocation: false
context: fork
complexity: medium
metadata:
  category: research
allowed-tools:
  - Read
  - Glob
  - Grep
  - mcp__sefaria__*
  - mcp__memory__*
---

# מחקר מקורות — Source Research

## תיאור

מיומנות לביצוע מחקר מקורות מעמיק דרך Sefaria MCP. מוצאת מקורות רלוונטיים מהספרות הפילוסופית היהודית, מזהה קשרים בין טקסטים, ובונה רשת מקורות מקיפה.

## תהליך עבודה

### 1. זיהוי טקסט המוצא
- קבל פסוק, סוגיה, או נושא
- השתמש ב-`clarify_name_argument` לאימות שמות ספרים
- השתמש ב-`get_text` לשליפת הטקסט המקורי

### 2. חיפוש מקורות פילוסופיים
בצע חיפושים ממוקדים בספרים הבאים:

#### רמב״ם
- `search_in_book("Guide for the Perplexed", <query>)`
- `search_in_book("Mishneh Torah", <query>)`
- `search_in_book("Commentary on the Mishnah", <query>)`

#### רס״ג
- `search_in_book("Emunot veDeot", <query>)`

#### רלב״ג
- `search_in_book("Milhamot HaShem", <query>)`
- `search_in_book("Ralbag on Torah", <query>)`

#### קרשקש
- `search_in_book("Or Hashem", <query>)`

#### אלבו
- `search_in_book("Sefer HaIkkarim", <query>)`

#### רמח״ל
- `search_in_book("Mesillat Yesharim", <query>)`
- `search_in_book("Derech Hashem", <query>)`

### 3. מציאת קשרים
- השתמש ב-`get_links_between_texts` לזיהוי קישורים בין מקורות
- השתמש ב-`english_semantic_search` למציאת טקסטים דומים תימטית

### 4. העשרה
- `get_topic_details(<topic>)` — מידע רקע על נושאים פילוסופיים
- `search_in_dictionaries(<term>)` — הגדרות מונחים

## כללי חיפוש

1. **רוחב**: חפש תמיד בלפחות 3 מקורות שונים
2. **עומק**: אם מצאת מקור רלוונטי, חפש גם את ההקשר הרחב שלו
3. **קשרים**: תמיד בדוק קישורים בין המקורות שמצאת
4. **אימות**: אמת שמות ספרים עם `clarify_name_argument` לפני חיפוש
5. **שפה**: נסה חיפושים גם בעברית וגם באנגלית

## פורמט פלט

```yaml
מקורות:
  - מקור: "רמב״ם, מורה נבוכים א:א"
    ציטוט: "..."
    רלוונטיות: "הגדרת צלם אלהים כשכל"
    sefaria_ref: "Guide for the Perplexed 1:1"

  - מקור: "רס״ג, אמונות ודעות ו:א"
    ציטוט: "..."
    רלוונטיות: "הגדרת הנפש"
    sefaria_ref: "Emunot veDeot 6:1"

קשרים:
  - בין: ["מו״נ א:א", "אמו״ד ו:א"]
    סוג: "מחלוקת"
    תיאור: "..."
```
