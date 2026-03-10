---
name: dvar-torah-writer
license: MIT
compatibility: "Claude Code 2.1.59+."
author: yodem
description: כתיבת דבר תורה מקיף בכל זרם מחשבה יהודית — פילוסופיה, קבלה, חסידות, חז״ל, מחקר מודרני. Use when writing a Dvar Torah, preparing a Torah lecture, writing a post, analyzing a parsha, or exploring Jewish thought.
version: 3.0.0
tags: [dvar-torah, jewish-philosophy, kabbalah, hasidut, hazal, rambam, sefaria, mussar, rationalism, post, shiur]
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

# דבר תורה — כותב ראשי

## תיאור

כלי לכתיבת דבר תורה, פוסט, או שיעור בכל זרם מחשבה יהודית: פילוסופיה, קבלה, חסידות, חז״ל, וחוקרים מודרניים. שואב מקורות מספריית ספריא, תומך בעברית ואנגלית, ומתכוונן להקשר האירוע.

## הגדרות Config קלט

```yaml
config:
  language: "he" | "en" | "bilingual"
  orientation: "philosophy" | "kabbalah" | "hasidut" | "hazal" | "modern" | "custom"
  format: "dvar-torah" | "post" | "shiur"
  length: "short" | "medium" | "long" | "shiur"
  topic:
    type: "parsha" | "philosophical" | "research"
    value: "..."
    sub_topic: "..." | null
  thinkers: [...]
  context:
    type: "birth" | "brit_milah" | "bar_bat_mitzvah" | "wedding" | "shabbat" | "holiday" | "shiva" | "yahrzeit" | "general"
    description: "tone and theme guidance from contexts-guide.md"
  previous_patterns:
    mode: "avoid" | "base_on"
    base_documents: [...]  # only in base_on mode
    template_guidance: {...}  # from previous-analysis base_on output
```

## ניתוב לפי אוריינטציה

### philosophy — פילוסופיה יהודית
הוגים: רמב״ם, רס״ג, רלב״ג, קרשקש, אלבו, ר״י הלוי, אבן עזרא, אבן פקודה
Sefaria: "Guide for the Perplexed", "Emunot veDeot", "Milhamot HaShem", "Or Hashem", "Kuzari"
גישה: ניתוח פילוסופי-רציונלי, דיאלוג בין שיטות, שאלות תיאולוגיות

### kabbalah — קבלה
הוגים: זוהר, רמ״ק, האר״י, רמח״ל
Sefaria: "Zohar", "Pardes Rimonim", "Etz Chaim", "Daat Tevunot"
גישה: ניתוח ספירות ומושגים, חיבור לפסוק, עיון בעולמות עליונים
- השתמש ב-`get_text_or_category_shape(path="Kabbalah")` לגילוי טקסטים זמינים

### hasidut — חסידות
הוגים: בעש״ט, מגיד, תניא, ברסלב, קדושת לוי
Sefaria: "Tanya", "Likkutei Moharan", "Keter Shem Tov", "Maggid Devarav LeYaakov"
גישה: תורות חסידיות, דרשה על הפסוק, רעיון מרכזי + נרטיב
- השתמש ב-`get_text_or_category_shape(path="Chasidut")` לגילוי טקסטים זמינים

### hazal — חז״ל
הוגים: תנאים, אמוראים, מדרשים
Sefaria: "Talmud Bavli", "Jerusalem Talmud", "Bereishit Rabbah", "Midrash Tanchuma"
גישה: אגדה ופרשנות, דרשה מלשון הכתוב, מחלוקת וסינתזה

### modern — חוקרים מודרניים
הוגים: קאופמן, קסוטו, פינס, אלטמן, ולהאוזן (כניגוד), ANE texts
גישה: הקשר היסטורי, מקבילות מהמזרח הקדום, ביקורת המקרא ותגובתה
- השתמש ב-`historical-research` skill כברירת מחדל

## הנחיות הקשר (Context)

קרא `references/contexts-guide.md` לפי `context.type` ויישם:
- **tone**: התאם את הטון הכללי
- **themes**: הגדר את הנושאים המרכזיים
- **opening_suggestion**: עצות לפתיחה מתאימה להקשר
- **sources**: הוסף מקורות ספציפיים להקשר (ראה contexts-guide.md)

### דוגמאות:
- `shiva`: טון נחמה ועדין, נושאים: אובדן ומשמעות, משיב, קהלת, איוב
- `wedding`: טון שמח ופואטי, נושאים: שותפות, שכינה ביניהם, שיר השירים
- `bar_bat_mitzvah`: טון מעודד, נושאים: אחריות, מצוות כמשמעות, מעבר
- `general`: עקוב אחרי האוריינטציה בלבד

## שימוש ב-base_documents

אם `previous_patterns.mode == "base_on"` ו-`template_guidance` קיים:
- **חובה** לעקוב אחר `template_guidance.strict_instructions`
- שמור על אותו מבנה פתיחה/גוף/סיום שחולץ מהקבצים הקודמים
- שמור על אותו register וצפיפות ציטוטים
- **אין** לחרוג מאורך שנקבע ב-`template_guidance.avg_length` ±20%

## הוגים מרכזיים

### פילוסופיה רציונלית
- **רמב״ם** — מורה נבוכים, משנה תורה, שמונה פרקים
- **רס״ג** — אמונות ודעות
- **רלב״ג** — מלחמות ה׳, פירוש על התורה
- **רבי חסדאי קרשקש** — אור ה׳
- **רבי יוסף אלבו** — ספר העיקרים
- **רבי אברהם אבן עזרא** — פירושים על התנ״ך
- **ר׳ יהודה הלוי** — הכוזרי
- **רבי בחיי אבן פקודה** — חובות הלבבות

### קבלה
- **זוהר** (ר״ש בר יוחאי / ר״מ דה ליאון) — ספר הזוהר
- **רמ״ק** (רבי משה קורדובירו) — פרדס רמונים
- **האר״י** (רבי יצחק לוריא) — עץ חיים
- **רמח״ל** (רבי משה חיים לוצאטו) — דעת תבונות, כלח״ב

### חסידות
- **הבעש״ט** — כתר שם טוב
- **המגיד ממזריץ׳** — מגיד דבריו ליעקב
- **אדמו״ר הזקן** (שניאור זלמן מלאדי) — תניא
- **ר׳ נחמן מברסלב** — ליקוטי מוהר״ן
- **ר׳ לוי יצחק מברדיטשוב** — קדושת לוי

### חז״ל
- תנאים — משנה, מדרש הלכה
- אמוראים — תלמוד בבלי, ירושלמי
- מדרש אגדה — בראשית רבה, תנחומא

### חוקרים מודרניים
- **יחזקאל קאופמן** — תולדות האמונה הישראלית
- **משה קסוטו** — ניתוח ספר בראשית ושמות
- **שלמה פינס** — מחקרי רמב״ם, תרגומים
- **אלכסנדר אלטמן** — פילוסופיה יהודית ניאו-אפלטונית

## תהליך עבודה

### שלב 0: אשף אינטראקטיבי (skill: interactive-cli)
אם המשתמש לא סיפק פרמטרים מלאים — הפעל את האשף:
0. בחירת שפה: עברית / English / Bilingual
0.5. בחירת אוריינטציה: פילוסופיה / קבלה / חסידות / חז״ל / מודרני
1. בחירת פורמט: דבר תורה / פוסט / שיעור
2. בחירת אורך: קצר / בינוני / ארוך / שיעור
3. בחירת נושא: פרשה / נושא / מחקרי
4. בחירת הוגים (מסונן לפי אוריינטציה)
5.5. הקשר: לידה / ברית / בר מצווה / חתונה / שבת / חג / שבעה / יארצייט / כללי
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

1. **שפה**: כתוב בשפה שנבחרה (`language`). עברית — מלאה; English — מלאה; bilingual — גוף עברי + סיכום אנגלי
2. **ציטוטים**: תמיד ציין מקור מדויק — השתמש ב-skill `source-references`
3. **אובייקטיביות**: הצג כל זרם מחשבה בנאמנות ובכבוד — אל תפסול שיטה אלא הצג
4. **רלוונטיות**: חבר את הדיון העתיק לשאלות עכשוויות
5. **עומק**: אל תישאר ברמת השטח — צלול לתוך הטיעונים
6. **בהירות**: הסבר מונחים טכניים (ספירות, תצמצום, צדיק וכו׳) בבהירות
7. **מראי מקומות**: כל מקור חייב להיות מאומת ב-Sefaria
8. **הקשר**: אם `context.type != "general"` — הקדם בהתאמה לטון ולנושאים של ההקשר
9. **base_documents**: אם `mode == "base_on"` — עקוב בקפדנות אחרי `template_guidance`

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
language: he | en | bilingual
orientation: philosophy | kabbalah | hasidut | hazal | modern | custom
context: general | wedding | shabbat | shiva | ...
parsha: שם הפרשה (אם רלוונטי)
topic: הנושא
thinkers: [רמב״ם, רס״ג]
sources_count: 5
---
```
