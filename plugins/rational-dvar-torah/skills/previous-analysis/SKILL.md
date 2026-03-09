---
name: previous-analysis
license: MIT
compatibility: "Claude Code 2.1.59+."
author: yodem
description: ניתוח דברי תורה קודמים לזיהוי דפוסים, סגנון, ומניעת חזרות. Use when starting a new dvar torah to learn from previous outputs.
version: 1.0.0
tags: [analysis, patterns, history, style]
user-invocable: false
disable-model-invocation: false
context: fork
complexity: medium
metadata:
  category: analysis
allowed-tools:
  - Read
  - Glob
  - Grep
  - mcp__memory__*
---

# ניתוח כתיבות קודמות — Previous Analysis

## תיאור

מיומנות שמנתחת דברי תורה ופוסטים שנכתבו בעבר כדי ללמוד את הסגנון, לזהות דפוסים, ולהמליץ על כיוונים חדשים.

## מיקום הקבצים

דברי תורה קודמים נשמרים ב:
```
output/divrei-torah/
  ├── dvar-torah/       ← דברי תורה מלאים
  │   ├── YYYY-MM-DD-parsha-name.md
  │   └── ...
  ├── posts/            ← פוסטים
  │   ├── YYYY-MM-DD-topic.md
  │   └── ...
  └── shiurim/          ← שיעורים
      ├── YYYY-MM-DD-topic.md
      └── ...
```

## תהליך ניתוח

### 1. סריקת קבצים קיימים
```
Glob("output/divrei-torah/**/*.md")
```

### 2. ניתוח כל קובץ
לכל דבר תורה קודם, חלץ:

```yaml
metadata:
  date: "2024-01-15"
  format: "dvar-torah"
  parsha: "בראשית"
  topic: "צלם אלהים"
  thinkers_used: ["רמב״ם", "רס״ג", "רלב״ג"]
  length: "medium"

style:
  structure: "dialectical"          # dialectical / analytical / narrative / comparative
  opening_pattern: "question"       # question / quote / story / statement
  closing_pattern: "practical"      # practical / philosophical / open-ended

content:
  main_argument: "..."
  sources_count: 5
  philosophical_depth: "deep"       # surface / moderate / deep
```

### 3. זיהוי דפוסים
מתוך כל הקבצים, חלץ:

- **הוגים מועדפים**: מי מופיע הכי הרבה?
- **נושאים שכוסו**: מה כבר נכתב?
- **סגנון דומיננטי**: מה המבנה החוזר?
- **פורמט מועדף**: יותר דברי תורה? פוסטים? שיעורים?
- **דפוס פתיחה**: איך בדרך כלל נפתח?
- **דפוס סיום**: איך בדרך כלל נסגר?

### 4. המלצות

בהתבסס על הניתוח:

```yaml
recommendations:
  avoid_topics: ["צלם אלהים"]              # כבר נכתב
  suggested_topics: ["ידיעה ובחירה"]        # עוד לא נכתב
  underused_thinkers: ["קרשקש", "אלבו"]    # שימוש נמוך
  style_consistency:
    keep: ["opening with question"]          # שמור — עובד טוב
    try: ["narrative opening"]               # נסה — לגיוון
  format_suggestion: "post"                  # אם כל הקודמים דברי תורה — נסה פוסט
```

### 5. דפוסי כתיבה לפי פורמט

כשיוצרים תוכן חדש, התאם לדפוסים שזוהו:

#### דבר תורה — דפוס טיפוסי שזוהה:
- פתיחה: שאלה פילוסופית מהפסוק
- גוף: 2-3 הוגים בדיאלוג
- סיום: תובנה מעשית

#### פוסט — דפוס טיפוסי שזוהה:
- פתיחה: hook קצר וחד
- גוף: רעיון אחד ממוקד עם מקור אחד
- סיום: שאלה פתוחה או תובנה קצרה

#### שיעור — דפוס טיפוסי שזוהה:
- פתיחה: הצגת הבעיה
- גוף: מקורות לחילוק, שאלות לתלמידים
- סיום: סיכום + מקורות להרחבה

## שמירה ב-Memory MCP

שמור את הדפוסים שזוהו ב-Memory MCP לשימוש עתידי:
```
mcp__memory__create_entity("writing_patterns", {
  preferred_thinkers: [...],
  covered_topics: [...],
  dominant_style: "...",
  format_distribution: { dvar_torah: 5, post: 2, shiur: 1 }
})
```

## פלט

```yaml
analysis:
  total_previous: 8
  format_distribution:
    dvar_torah: 5
    post: 2
    shiur: 1
  top_thinkers: ["רמב״ם (7)", "רלב״ג (4)", "רס״ג (3)"]
  covered_topics: ["צלם אלהים", "בחירה חופשית", "טעמי המצוות"]
  dominant_style: "dialectical"

recommendations:
  avoid: ["צלם אלהים — נכתב ב-2024-01-15"]
  suggest: ["ידיעה ובחירה", "נבואה", "השגחה"]
  try_thinkers: ["קרשקש", "אלבו"]
  try_format: "post — רוב הקודמים דברי תורה"
```
