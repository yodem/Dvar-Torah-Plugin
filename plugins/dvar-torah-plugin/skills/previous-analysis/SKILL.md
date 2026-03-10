---
name: previous-analysis
license: MIT
compatibility: "Claude Code 2.1.59+."
author: yodem
description: ניתוח דברי תורה קודמים לזיהוי דפוסים, סגנון, ומניעת חזרות — או כתיבה על בסיסם. Use when starting a new dvar torah to learn from previous outputs, or to base a new one on selected previous pieces.
version: 3.0.0
tags: [analysis, patterns, history, style, base-on]
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

מיומנות שמנתחת דברי תורה ופוסטים שנכתבו בעבר.

**שני מצבים:**
- `mode: "avoid"` — זיהוי דפוסים, מניעת חזרות, המלצה על כיוונים חדשים (התנהגות קיימת)
- `mode: "base_on"` — חילוץ סגנון ומבנה מדברי תורה נבחרים, שימוש כתבנית לכתיבה חדשה

---

## פרמטר `mode`

```yaml
mode: "avoid"   # ברירת מחדל — זיהוי דפוסים + המלצות
mode: "base_on" # כתיבה על בסיס קבצים נבחרים
selected_files:  # רק ב-base_on — רשימת נתיבים שנבחרו
  - "output/divrei-torah/dvar-torah/2024-01-15-bereshit.md"
```

---

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

## פלט — מצב `avoid`

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

---

## מצב `base_on` — כתיבה על בסיס קבצים נבחרים

### תהליך

1. קרא את כל הקבצים ב-`selected_files`
2. לכל קובץ, חלץ:

```yaml
extracted:
  opening_style: "שאלה פילוסופית" | "ציטוט" | "סיפור" | "טענה"
  argument_structure: "dialectical" | "analytical" | "narrative" | "comparative"
  thinker_usage: "רמב״ם ראשון, קרשקש משיג" | "שני הוגים במקביל" | ...
  paragraph_length: "short" | "medium" | "long"
  closing_style: "תובנה מעשית" | "שאלה פתוחה" | "סינתזה"
  register: "אקדמי" | "שיחתי" | "דרשני"
  avg_word_count: 1500
  citation_density: "heavy" | "moderate" | "light"
```

3. סנתז את הדפוסים המשותפים לכל הקבצים שנבחרו
4. צור `template_guidance` — הנחיות לסגנון ומבנה

### פלט — מצב `base_on`

```yaml
base_on_analysis:
  source_files:
    - path: "output/divrei-torah/dvar-torah/2024-01-15-bereshit.md"
      topic: "צלם אלהים"
      thinkers: ["רמב״ם", "קרשקש"]
    - path: "output/divrei-torah/dvar-torah/2024-02-10-noach.md"
      topic: "בחירה חופשית"
      thinkers: ["רמב״ם", "רלב״ג"]

template_guidance:
  opening:
    style: "שאלה פילוסופית חדה מהפסוק"
    example_pattern: "מדוע [X]? האם [Y]?"
  body:
    structure: "dialectical — שני הוגים בדיאלוג, ניגוד ופתרון"
    thinker_order: "הוגה א׳ מציע → הוגה ב׳ מקשה → סינתזה"
    citation_style: "ציטוט עברי + תרגום"
    paragraph_length: "medium — 3-4 משפטים לפסקה"
  closing:
    style: "תובנה מעשית — שאלה אישית לסיום"
  register: "אקדמי-דרשני, עברית, מינוח פילוסופי"
  avg_length: 1600

  strict_instructions: |
    כתוב את דבר התורה החדש לפי אותו מבנה ומבוסס על הדפוסים שחולצו:
    1. פתח בשאלה פילוסופית חדה
    2. הצג שני הוגים בדיאלוג (ניגוד → פתרון)
    3. צטט בעברית עם תרגום
    4. סגור עם תובנה מעשית ושאלה אישית
    5. אורך: ~1500-1700 מילים
```
