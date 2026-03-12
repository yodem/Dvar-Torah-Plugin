---
name: analyze
license: MIT
compatibility: "Claude Code 2.1.59+."
author: yodem
description: Philosophical analysis of Jewish thought. Use when comparing positions of Jewish thinkers, analyzing theological questions, or building dialectical arguments.
version: 4.2.0
tags: [philosophy, theology, analysis, jewish-thought, dialectics]
user-invocable: true
disable-model-invocation: false
context: fork
complexity: high
metadata:
  category: analysis
allowed-tools:
  - Read
  - Glob
  - Grep
  - mcp__claude_ai_Sefaria__*
  - mcp__sequential-thinking__*
---

# ניתוח פילוסופי — Philosophical Analysis

## תיאור

מיומנות לביצוע ניתוח פילוסופי מעמיק של סוגיות במחשבת ישראל. מזהה שאלות פילוסופיות, ממפה עמדות של הוגים שונים, ובונה דיאלוג ביקורתי בין השיטות.

## נושאי ליבה

### תיאולוגיה
- תארי האל (שלילה/חיוב) — רמב״ם vs. קרשקש
- ידיעה ובחירה — רמב״ם, רלב״ג, קרשקש
- השגחה פרטית — רמב״ם (מו״נ ג:יז-יח), רלב״ג
- בריאה — חידוש vs. קדמות העולם
- נבואה — רמב״ם (מו״נ ב:לב-מח), רלב״ג

### אפיסטמולוגיה
- גבולות השכל האנושי — רמב״ם (מו״נ א:לא-לב)
- יחס תורה ופילוסופיה — רס״ג, רמב״ם, ר״י הלוי
- מקור הידיעה — שכל, מסורת, התגלות

### אתיקה
- טעמי המצוות — רמב״ם (מו״נ ג), רלב״ג, אלבו
- מידות ודרך האמצע — רמב״ם (שמונה פרקים, הל׳ דעות)
- תיקון המידות — רמח״ל (מסילת ישרים)
- תכלית האדם — רמב״ם, רלב״ג, קרשקש

### מטאפיזיקה
- צורה וחומר — רמב״ם, רלב״ג
- השכל הפועל — רמב״ם, רלב״ג
- הנפש ועולם הבא — רמב״ם (הל׳ תשובה ח), רס״ג, קרשקש

## מתודולוגיה

### 1. זיהוי הסוגיה
הגדר את השאלה הפילוסופית בבירור:
- מה בדיוק השאלה?
- מדוע היא בעייתית?
- מה ההנחות שעומדות בבסיסה?

### 2. מיפוי עמדות
לכל הוגה:
- **טענה מרכזית**: מה עמדתו?
- **הנמקה**: מה הטיעון שלו?
- **מקור טקסטואלי**: היכן הוא כותב זאת?
- **הקשר היסטורי**: מול מי הוא כותב? מה ההקשר?

### 3. דיאלוג ביקורתי
- זהה נקודות הסכמה ומחלוקת
- בחן כיצד הוגה מאוחר מגיב לקודם לו
- הצבע על חוזקות וחולשות בכל עמדה

### 4. סינתזה
- מה עולה מהדיון?
- האם ניתן ליישב בין השיטות?
- מה הרלוונטיות העכשווית?

<use_parallel_tool_calls>
If you intend to call multiple tools and there are no dependencies between
the tool calls, make all of the independent tool calls in parallel. Prioritize
calling tools simultaneously whenever the actions can be done in parallel
rather than sequentially. For example, when searching for sources on multiple
thinkers, run all searches at once. Maximize use of parallel tool calls where
possible to increase speed and efficiency.
However, if some tool calls depend on previous calls to inform dependent
values, do NOT call these tools in parallel.
</use_parallel_tool_calls>

## כלים

### Sequential Thinking MCP
כשהניתוח מורכב, `sequential-thinking` יכול לסייע:
- פירוק טיעונים פילוסופיים לצעדים
- בחינת תוקף לוגי של הנמקות
- השוואה שיטתית בין עמדות

### Sefaria MCP (עדיפויות)
1. `english_semantic_search` — גילוי ראשוני
2. `get_links_between_texts` — קשרים בין הוגים
3. `get_text` — שליפת מקור מדויק
4. `get_topic_details` — רקע על נושאים פילוסופיים

## פורמט פלט

```markdown
## ניתוח פילוסופי: [שם הסוגיה]

### השאלה
[ניסוח ברור של השאלה הפילוסופית]

### עמדות

#### [הוגה א׳] — [תיאור קצר של עמדתו]
**טענה**: ...
**הנמקה**: ...
**מקור**: ...

#### [הוגה ב׳] — [תיאור קצר של עמדתו]
**טענה**: ...
**הנמקה**: ...
**מקור**: ...

### דיאלוג
[כיצד השיטות מתייחסות זו לזו]

### סינתזה
[מסקנות מהדיון]
```

## דגשים

1. **דיוק**: אל תייחס להוגה עמדה שלא כתב. תמיד ציין מקור
2. **הוגנות**: הצג כל שיטה בצורה הטובה ביותר שלה (charity principle)
3. **הקשר**: הבן את ההוגה בהקשר ההיסטורי שלו
4. **מורכבות**: אל תפשט יתר על המידה — הפילוסופיה היהודית מורכבת
5. **ענווה**: הכר בגבולות הידע — לפעמים הפרשנות שנויה במחלוקת
