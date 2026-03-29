# מדריך הוגים — Jewish Thought Guide (v4.2)

> פירוט מורחב לפי זרמים וקורפוסים מרכזיים ב-Sefaria. לטבלה מקצרת ראה `thinkers-by-subject.md`.

---

## 1. פילוסופיה יהודית (philosophy)

### ליבה רציונליסטית (Rishonim)
- **רס״ג** — `HaEmunot veHaDeot`  
  רציונליזם מוקדם, אמונה ושכל, בריאה, אחדות האל.
- **רמב״ם** — `Guide for the Perplexed`, `Mishneh Torah`, `Eight Chapters`  
  תיאולוגיה שלילית, נבואה, השגחה, טעמי המצוות, אתיקה.
- **רלב״ג** — `The Wars of the Lord`  
  פילוסופיה אריסטוטלית יהודית, ידיעת ה׳ והשגחה.
- **קרשקש** — `Ohr Hashem`  
  ביקורת האריסטוטליזם והרחבת שיח הרצון והאהבה.
- **אלבו** — `Sefer HaIkkarim`  
  סינתזה דוגמטית של עיקרי האמונה.
- **ריה״ל** — `Kuzari`  
  הגנה על ההתגלות וההיסטוריה מול רציונליזם מופשט.
- **אבן פקודה** — `Duties of the Heart`  
  מוסר פנימי כתשתית אמונית.
- **אבן עזרא** — `Yesod Mora VeSod HaTorah`, `Ibn Ezra on Torah`  
  פשט לשוני ודיון פילוסופי מרומז.

### הרחבות (Acharonim ומודרני)
- **הר״ן** — `Derashot HaRan` (תיאולוגיה פוליטית וחינוכית).
- **עקידת יצחק** — `Akeidat Yitzchak` (דרשנות פילוסופית).
- **מהר״ל** — `Tiferet Yisrael`, `Netivot Olam` (מטפיזיקה של תורה והיסטוריה).
- **נפש החיים** — `Nefesh HaChayim` (מבנה רוחני-ישיבתי).
- **הירש** — `Nineteen Letters`, `Horeb` (תורה עם מודרנה).

**שאילתות Sefaria מומלצות**
```python
search_in_book("Guide for the Perplexed", query)
search_in_book("HaEmunot veHaDeot", query)
search_in_book("Ohr Hashem", query)
text_search(query, categories=["Jewish Thought"])
```

---

## 2. קבלה (kabbalah)

### ציר קלאסי
- **זוהר** — `Zohar`
- **רמ״ק** — `Pardes Rimonim`
- **האר״י** — `Etz Chaim`, `Sha'ar HaKavanot`
- **רמח״ל** — `Daat Tevunot`, `Klach Pitchei Chochmah`, `Derekh Hashem`

### הרחבות שימושיות לכתיבה
- **אבולעפיה** — `Ohr HaSekhel`, `Gan Naul (Abulafia)` (שפה ונבואה).
- **בעל הסולם** — `Talmud Eser HaSefirot`, `Baal HaSulam's Introduction to Zohar` (שפה שיטתית מאוחרת).

**שאילתות Sefaria מומלצות**
```python
get_text_or_category_shape(path="Kabbalah")
search_in_book("Zohar", query)
search_in_book("Daat Tevunot", query)
```

---

## 3. חסידות (hasidut)

### מוקדמת
- **הבעש״ט ובית מדרשו** — `Keter Shem Tov`, `Toldot Yaakov Yosef`, `Ben Porat Yosef`
- **המגיד ממזריץ׳** — `Maggid Devarav leYaakov`
- **קדושת לוי** — `Kedushat Levi`

### אסכולות
- **חב״ד** — `Tanya`, `Torah Ohr`, `Likkutei Torah`
- **ברסלב** — `Likutei Moharan`, `Likutei Tefilot`, `Sippurei Maasiyot`
- **איזביצא ור׳ צדוק** — `Mei HaShiloach`, `Peri Tzadik`, `Tzidkat HaTzadik`
- **חסידות מאוחרת** — `Sefat Emet`, `Shem MiShmuel`, `Esh Kodesh`

**שאילתות Sefaria מומלצות**
```python
get_text_or_category_shape(path="Chasidut")
search_in_book("Tanya", query)
search_in_book("Likutei Moharan", query)
```

---

## 4. חז״ל, תלמוד, מדרש (hazal)

### קורפוסים מרכזיים
- **משנה ותוספתא** — `Mishnah`, `Tosefta`
- **תלמודים** — `Talmud Bavli`, `Jerusalem Talmud`
- **מדרשי הלכה** — `Mekhilta DeRabbi Yishmael`, `Sifra`, `Sifrei Bamidbar`, `Sifrei Devarim`
- **מדרש רבה** — `Bereshit Rabbah`, `Shemot Rabbah`, `Vayikra Rabbah` ועוד
- **מדרשי אגדה** — `Midrash Tanchuma`, `Pesikta Rabbati`, `Pirkei DeRabbi Eliezer`
- **אוספים** — `Yalkut Shimoni on Torah`, `Ein Yaakov`

**שאילתות Sefaria מומלצות**
```python
text_search(query, categories=["Talmud", "Midrash"])
search_in_book("Bereshit Rabbah", query)
get_links_between_texts("Genesis 1:1")
```

---

## 5. מחשבה יהודית מודרנית (modern)

### הוגים וטקסטים תורניים מודרניים ב-Sefaria
- **הרב קוק** — `Orot`, `Orot HaTeshuvah`, `Orot HaKodesh`
- **ר׳ יונתן זקס** — `Rabbi Lord Jonathan Sacks` (קורפוס רחב)
- **אליעזר ברקוביץ** — `Eliezer Berkovits` (אמונה, הלכה, מודרנה)
- **ישעיהו ליבוביץ** — `Talks of Yeshayahu Leibowitz on the Parasha`

### מחקר אקדמי יהודי (לרוב כהקשר, לא כקורפוס מלא ב-Sefaria)
- קאופמן, קסוטו, פינס, אלטמן, קלנר, הרווי, הלברטל.
- השתמש בטקסטים מקראיים/חז״ל כבסיס, והבא מחקר אקדמי כהארה פרשנית.

---

## 6. מוסר (musar)

### ראשונים
- `Sha'arei Teshuvah`
- `Orchot Tzadikim`
- `Letter from Ramban to his Son`
- `Sefer HaYirah`

### אחרונים
- `Mesillat Yesharim`
- `Pele Yoetz`
- `Shemirat HaLashon`

### מודרני
- `Ohr HaTzafun` וקורפוסים מוסריים נוספים בקטגוריית Musar.

**שאילתות Sefaria מומלצות**
```python
get_text_or_category_shape(path="Musar")
search_in_book("Mesillat Yesharim", query)
search_in_book("Sha'arei Teshuvah", query)
```

---

## 7. מסגרות הלכתיות מסייעות (halakhic-framework)
*למסגור רעיוני; לא לפסיקה הלכתית*

- **משנה תורה** — `Mishneh Torah`
- **שולחן ערוך** — `Shulchan Arukh, Orach Chayim` (ובהתאם נושא)
- **ספרות מצוות** — `Sefer HaChinukh`, `Sefer HaMitzvot`

שימוש מומלץ: לחבר רעיון הגותי למחויבות מעשית, בלי להציג פסיקה מחייבת.
