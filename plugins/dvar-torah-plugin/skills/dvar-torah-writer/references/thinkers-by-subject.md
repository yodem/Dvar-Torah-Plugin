# מדריך הוגים לפי נושא / Thinkers by Subject

מפה מלאה של חמש אוריינטציות עם הוגים, יצירות, ומזהי Sefaria.

---

## 1. פילוסופיה יהודית (philosophy)
*רציונליזם — לא קבלה*

| הוגה | Thinker | יצירות מרכזיות | Sefaria Ref |
|------|---------|----------------|-------------|
| **רס״ג** | Saadia Gaon (882–942) | אמונות ודעות | "Emunot veDeot" |
| **רמב״ם** | Maimonides (1138–1204) | מורה נבוכים, משנה תורה, שמונה פרקים | "Guide for the Perplexed", "Mishneh Torah", "Shemonah Perakim" |
| **רלב״ג** | Gersonides (1288–1344) | מלחמות ה׳, פירוש על התורה | "Milhamot HaShem", "Ralbag on Torah" |
| **קרשקש** | Hasdai Crescas (1340–1410) | אור ה׳ | "Or Hashem" |
| **אלבו** | Joseph Albo (1380–1444) | ספר העיקרים | "Sefer HaIkkarim" |
| **ר״י הלוי** | Judah HaLevi (1075–1141) | הכוזרי | "Kuzari" |
| **אבן עזרא** | Abraham Ibn Ezra (1089–1167) | פירושים על התורה | "Ibn Ezra on Torah" |
| **אבן פקודה** | Bahya Ibn Paquda (11th c.) | חובות הלבבות | "Chovot HaLevavot" |

**נושאים מרכזיים**: תארי האל, נבואה, השגחה, בחירה חופשית, ידיעה, בריאה, טעמי המצוות, נפש האדם

**הנחיות Sefaria**:
```
search_in_book("Guide for the Perplexed", query)
search_in_book("Emunot veDeot", query)
search_in_book("Or Hashem", query)
get_text("Guide for the Perplexed 1:1")
```

---

## 2. קבלה (kabbalah)

| הוגה | Thinker | יצירות מרכזיות | Sefaria Ref |
|------|---------|----------------|-------------|
| **זוהר** | Zohar (ר״ש בר יוחאי / ר״מ דה ליאון) | ספר הזוהר | "Zohar" |
| **רמ״ק** | Ramak — Moses Cordovero (1522–1570) | פרדס רמונים | "Pardes Rimonim" |
| **האר״י** | Ari — Isaac Luria (1534–1572) | עץ חיים, פרי עץ חיים | "Etz Chaim" |
| **רמח״ל** | Ramchal — Moses Luzzatto (1707–1746) | דעת תבונות, כלח פתחי חכמה | "Daat Tevunot", "Klach Pitchei Chochmah" |

**נושאים מרכזיים**: עשר ספירות, צמצום, שבירת הכלים, תיקון, ניצוצות, עולמות אצי-בריא-יצ-עשי, אין סוף

**הנחיות Sefaria**:
```
get_text_or_category_shape(path="Kabbalah")
search_in_book("Zohar", query)
get_text("Zohar 1:1a")
```

---

## 3. חסידות (hasidut)

| הוגה | Thinker | יצירות מרכזיות | Sefaria Ref |
|------|---------|----------------|-------------|
| **הבעש״ט** | Baal Shem Tov (1698–1760) | כתר שם טוב, בן פורת יוסף | "Keter Shem Tov" |
| **המגיד ממזריץ׳** | Maggid of Mezeritch (1704–1772) | מגיד דבריו ליעקב | "Maggid Devarav LeYaakov" |
| **אדמו״ר הזקן** | Shneur Zalman of Liadi (1745–1812) | תניא, שו״ע הרב | "Tanya" |
| **ר׳ נחמן מברסלב** | Nachman of Breslov (1772–1810) | ליקוטי מוהר״ן, ליקוטי תפילות | "Likkutei Moharan" |
| **ר׳ לוי יצחק מברדיטשוב** | Levi Yitzchak of Berditchev (1740–1810) | קדושת לוי | "Kedushat Levi" |

**נושאים מרכזיים**: דבקות, בטול, שמחה, צדיק, עבודת השם, תפילה, אמונה, התעלות

**הנחיות Sefaria**:
```
get_text_or_category_shape(path="Chasidut")
search_in_book("Tanya", query)
search_in_book("Likkutei Moharan", query)
get_text("Tanya, Likutei Amarim 1")
```

---

## 4. חז״ל (hazal)

| מקור | Source | כינוי | Sefaria Ref |
|------|--------|-------|-------------|
| **תנאים** | Tannaim (1st–3rd c.) | משנה, מדרש הלכה | "Mishnah", "Mekhilta", "Sifra", "Sifre" |
| **אמוראים** | Amoraim (3rd–6th c.) | תלמוד בבלי, ירושלמי | "Talmud Bavli", "Jerusalem Talmud" |
| **מדרש אגדה** | Aggadic Midrash | בראשית רבה, תנחומא, ויקרא רבה | "Bereishit Rabbah", "Midrash Tanchuma" |
| **תנאים בודדים** | Individual sages | ר״ע, ר״י הנשיא, בית שמאי/הלל | varies |

**נושאים מרכזיים**: אגדה ופרשנות, מחלוקת לשם שמים, הלכה ומחשבה, דרשת הפסוק, עולמות הבא, גאולה

**הנחיות Sefaria**:
```
get_text("Mishnah Avot 2:1")
search_in_book("Bereishit Rabbah", query)
get_links_between_texts("Genesis 1:1")
text_search(query, categories=["Talmud"])
```

---

## 5. חוקרים מודרניים (modern)
*Wissenschaft des Judentums + ANE + Biblical Criticism*

### חוקרים יהודיים (נגד/ביקורת/אחר)

| חוקר | Scholar | תחום | הערות |
|------|---------|------|-------|
| **יחזקאל קאופמן** | Y. Kaufmann (1889–1963) | תולדות האמונה הישראלית | נגד תיאוריית תעודות, ייחודיות הדת הישראלית |
| **משה קסוטו** | M. Cassuto (1883–1951) | ביקורת ספר בראשית ושמות | נגד תיאוריית תעודות, עדות ספרותית |
| **שלמה פינס** | S. Pines (1908–1990) | מחקרי רמב״ם, תרגומים | Academic Jewish philosophy |
| **אלכסנדר אלטמן** | A. Altmann (1906–1987) | פילוסופיה יהודית ניאו-אפלטונית, רס״ג | Academic |
| **וורן זאב הרווי** | W. Harvey | קרשקש, רלב״ג | Academic Crescas & Gersonides studies |
| **מנחם קלנר** | M. Kellner | רמב״ם, אמונה | Academic Maimonides |
| **משה הלברטל** | M. Halbertal | רמב״ם, מהפכה ומסורת | Academic |

### תיאוריית התעודות (כרקע/ניגוד)

| חוקר | Scholar | תרומה |
|------|---------|-------|
| **ולהאוזן** | Wellhausen | תיאוריית J, E, D, P |
| **גרף** | Graf | מקדימן לולהאוזן |

### טקסטים מהמזרח הקדום (ANE)

| טקסט | Topic | מקבילה בתורה |
|------|-------|--------------|
| **ענומה אליש** | Enuma Elish (Babylonian) | בריאת העולם — בראשית א |
| **אטרהסיס** | Atrahasis Epic | מבול — נח |
| **גלגמש** | Gilgamesh Epic | מבול — נח |
| **חמורבי** | Code of Hammurabi | חוקי משפטים |
| **חוקי חיתים** | Hittite Laws | חוקים + ברית סיני |
| **אמרנה** | Amarna Letters | הקשר כנען |
| **בריתות חיתיות** | Hittite suzerain-vassal treaties | מבנה ברית סיני |

**הנחיות מחקר**:
```
# ANE + academic — לרוב דרך WebSearch/WebFetch
# Sefaria לטקסטים המקראיים עצמם
get_text("Genesis 1:1-2:3")  # להשוואה עם ענומה אליש
get_text("Exodus 21:1-24:18")  # להשוואה עם חמורבי
```
