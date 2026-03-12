# מדריך הקשרים — Contexts Guide

הנחיות טון, נושאים, ופתיחות לפי הקשר / אירוע.

---

## contexts:

### id: birth
**Hebrew**: לידה / שלום זכר / שמחת בת
**tone**: joyful, hopeful, welcoming
**themes**: ברית, ברכה, פוטנציאל החיים החדשים, סיפורי רחל/חנה, פוריות
**opening_suggestion**: פתח בהודיה על החיים החדשים, חבר לפסוקים על לידה וברכה
**sources**:
- "וַיִּפְקֹד ה׳ אֶת שָׂרָה" (Gen. 21:1) — ה׳ זוכר וברכה מגיעה בזמן
- "אֵשֶׁת חַיִל מִי יִמְצָא" (Proverbs 31)
- "שְׂאוּ שְׁעָרִים רָאשֵׁיכֶם" (Ps. 24) — אם שלום זכר
- Talmud: Niddah 31b — על השמחה בלידה
**sefaria_search**: `text_search("ולד", filter_by="Torah")`, `search_in_book("Bereishit Rabbah", "לידה")`
**closing_suggestion**: ברכה לילד/ה ולמשפחה, תקווה לעתיד

---

### id: brit_milah
**Hebrew**: ברית מילה
**tone**: covenantal, serious, joyful
**themes**: ברית אברהם, כניסה לעם ישראל, אות הברית, הגוף כנשא של הברית
**opening_suggestion**: "וַיִּתֶּן לוֹ אֱלֹהִים בְּרִית הַמִּילָה" — הברית כקשר יסודי בין האל לישראל
**sources**:
- Gen. 17:9-14 — מצוות הברית לאברהם
- "ומלתם את ערלת לבבכם" (Deut. 10:16) — ברית פנימית
- Rambam, Guide 3:49 — טעם המילה פילוסופית
- Tanya ch. 2 — ברית כחקיקה בנשמה
**sefaria_search**: `search_in_book("Guide for the Perplexed", "circumcision")`, `get_text("Genesis 17")`
**closing_suggestion**: ברכה לנימול, חיבור לברית אברהם ולמסורת הדורות

---

### id: bar_bat_mitzvah
**Hebrew**: בר/בת מצווה
**tone**: celebratory, encouraging, educational
**themes**: אחריות, מעבר לבגרות, מצוות כמשמעות, בחירה חופשית, זהות יהודית
**opening_suggestion**: "הנה לא ינום ולא יישן שומר ישראל" — כל שלב בחיים הוא התחדשות
**sources**:
- Mishnah Avot 5:21 — "בן שלוש עשרה למצוות"
- Rambam, Shemonah Perakim ch. 4 — בחירה חופשית כיסוד המוסרי
- Etz Chaim — כל עלייה דורשת הכנה פנימית (אם קבלה)
- Likkutei Moharan — "כל אחד יש לו עולם בפני עצמו" (אם חסידות)
**sefaria_search**: `search_in_book("Shemonah Perakim", "choice")`, `get_text("Mishnah Avot 5:21")`
**closing_suggestion**: עידוד אישי לבר/בת המצווה, מסר על אחריות כחירות

---

### id: wedding
**Hebrew**: נישואין / אופרוף
**tone**: joyful, poetic, romantic-spiritual
**themes**: שותפות, שכינה שרויה ביניהם, אהבה בשיר השירים, בית נאמן בישראל, גוף ונשמה
**opening_suggestion**: "אִישׁ וְאִשָּׁה שָׁכִינָה שְׁרוּיָה בֵינֵיהֶם" (Sotah 17a)
**sources**:
- Shir HaShirim — אהבה כמטאפורה לקשר עם האל
- Gen. 2:18 — "לא טוב היות האדם לבדו" — שלמות דרך שותפות
- Rambam, Mishneh Torah, Ishut — נישואין כהתחייבות מוסרית
- Tanya, Likutei Amarim — אחדות נשמות ונשמה כללית (אם חסידות)
- Zohar — זווג עליון, שכינה ותפארת (אם קבלה)
**sefaria_search**: `search_in_book("Shir HaShirim Rabbah", "love")`, `get_text("Shir HaShirim 1:1")`
**closing_suggestion**: ברכת מזל טוב, ברכת בית נאמן בישראל

---

### id: shabbat
**Hebrew**: שבת
**tone**: reflective, restful, elevated
**themes**: מנוחה כרוחניות, קדושת הזמן, שבת כיצירה, חידוש שבועי, נשמה יתרה
**opening_suggestion**: "וַיְכַל אֱלֹהִים בַּיּוֹם הַשְּׁבִיעִי" — המנוחה היא פסגת הבריאה
**sources**:
- Gen. 2:1-3 — קידוש השבת בבריאה
- Rambam, Guide 2:31 — טעם השבת — זכירת הבריאה
- Etz Chaim — שבת כנקודת האין סוף בתוך הבריאה (אם קבלה)
- Tanya — נשמה יתרה בשבת (אם חסידות)
**sefaria_search**: `search_in_book("Guide for the Perplexed", "Sabbath")`, `get_text("Genesis 2:1-3")`
**special**: הצמד לפרשת השבוע אם רלוונטי
**closing_suggestion**: שבת שלום, מסר על קדושת הזמן

---

### id: holiday
**Hebrew**: חג
**tone**: festive, themed by specific holiday
**themes_by_holiday**:
  - פסח: חירות, יציאת מצרים, גאולה
  - שבועות: מתן תורה, תורה שבכתב ושבעל פה, קבלת עול מלכות שמים
  - ראש השנה: תשובה, מלכות, זיכרון
  - יום כיפור: סליחה, כפרה, חזרה לעצמי
  - סוכות: ארעיות, אושפיזין, שמחה
  - חנוכה: נס, אור, ייצוג במחשכים
  - פורים: נסתרות, אסתר, הפוך הוא
**opening_suggestion**: פתח בנושא המרכזי של החג הספציפי
**sefaria_search**: `get_current_calendar()` — לזיהוי החג הנוכחי
**closing_suggestion**: חג שמח / מועדים לשמחה

---

### id: shiva
**Hebrew**: שבעה / שלושים / אבל
**tone**: comforting, gentle, grounded, honest about pain
**themes**: משמעות האובדן, זיכרון והמשכיות, "אנא ה׳ כי עבדך", איוב, קהלת, עולם הבא
**opening_suggestion**: התחל בשתיקה — הודאה בכאב לפני כל רעיון. פתח לאט ובעדינות
**sources**:
- Job 1:21 — "ה׳ נתן וה׳ לקח"
- Kohelet 3:1-8 — "לכל זמן ועת לכל חפץ"
- Talmud Berakhot 5b — "כל שמיתו אוהבו... יתחזק"
- Rambam, Mishneh Torah, Evel — כבוד המת ונחמת האבלים
- Or Hashem / Zohar — נשמה אחרי המוות (אם רלוונטי)
**sefaria_search**: `search_in_book("Job", "death")`, `get_text("Kohelet 3")`
**closing_suggestion**: "המקום ינחם אתכם בתוך שאר אבלי ציון וירושלים"
**special**: אל תכביד. שמור על פשטות ואמפתיה. אין פילוסופיה כבדה בשבעה.

---

### id: yahrzeit
**Hebrew**: יארצייט / אזכרה
**tone**: memorial, personal, contemplative
**themes**: זיכרון, ירושה, נשמה ועלייתה, השפעת הנפטר על החיים, "אֵין אֱלֹהִים כִּי אִם ה׳"
**opening_suggestion**: "לא מתו הצדיקים, שמעשיהם הם זכרם" — פתח בחיבור האישי לנפטר
**sources**:
- Mishnah Avot — "ואל תאמר דבר שאי אפשר לשמוע שסופו להישמע"
- Kaddish — זיכרון דרך קידוש שם שמים
- Talmud — iluy neshama, study in memory
- Zohar — נשמה עולה ביארצייט
**sefaria_search**: `text_search("memory soul", filter_by="Kabbalah")`, `search_in_book("Zohar", "soul")`
**closing_suggestion**: "תהא נשמתו/ה צרורה בצרור החיים"

---

### id: general
**Hebrew**: כללי — ללא הקשר ספציפי
**tone**: neutral — follow chosen orientation
**themes**: any topic — determined by orientation and thinker selection
**opening_suggestion**: עקוב אחרי הנושא שנבחר ללא הגבלות הקשר
**special**: אין הנחיות טון ספציפיות — כל ההחלטות נובעות מהאוריינטציה והנושא
