---
name: dvar-torah
description: כתוב דבר תורה, פוסט, או שיעור — בכל זרם מחשבה יהודית
user-invocable: true
---

# /dvar-torah

כתוב דבר תורה, פוסט, או שיעור — פילוסופיה, קבלה, חסידות, חז״ל, או מחקר מודרני.

## תהליך

### אם אין פרמטרים — הפעל אשף אינטראקטיבי (skill: wizard):

0. **בחירת שפה**: עברית / English / Bilingual
0.5. **בחירת אוריינטציה**: פילוסופיה / קבלה / חסידות / חז״ל / חוקרים מודרניים / אחר
1. **בחירת פורמט**: דבר תורה / פוסט / שיעור
2. **בחירת אורך**: קצר / בינוני / ארוך / שיעור
3. **בחירת נושא**: קודם שלוף פרשה מ-`get_current_calendar()`, ואז שאל
4. **בחירת הוגים** (מסונן לפי אוריינטציה שנבחרה)
5.5. **הקשר**: לידה / ברית / בר מצווה / חתונה / שבת / חג / שבעה / יארצייט / כללי
5. **ניתוח כתיבות קודמות**: סרוק `output/divrei-torah/` — הימנע מחזרות או כתוב על בסיס קודמים

### אחרי הבחירות:

6. **מחקר מקורות** (skill: research)
7. **מחקר היסטורי** (skill: history) — אם מחקרי
8. **ניתוח פילוסופי** (skill: analyze)
9. **שילוב מוסר** (skill: mussar) — אם רלוונטי
10. **אימות מראי מקומות** (skill: verify)
11. **כתיבה** (skill: compose) — לפי פורמט, אורך, אוריינטציה, הקשר
12. **שמירה** — `output/divrei-torah/<format>/YYYY-MM-DD-<topic>.md`

## פרמטרים (אם ניתנים ישירות — דלג על האשף)

- **שפה**: `עברית` / `English` / `bilingual`
- **אוריינטציה**: `פילוסופיה` / `קבלה` / `חסידות` / `חז״ל` / `מודרני`
- **פורמט**: `דבר-תורה` / `פוסט` / `שיעור`
- **אורך**: `קצר` / `בינוני` / `ארוך` / `שיעור`
- **נושא/פרשה**: הפרשה, החג, או הנושא
- **הוגים**: הוגים ספציפיים להדגיש
- **הקשר**: `לידה` / `ברית` / `בר-מצווה` / `חתונה` / `שבת` / `חג` / `שבעה` / `יארצייט` / `כללי`
- **סוג**: `פילוסופי` / `מחקרי` / `מעורב`
- **`--parasha <name|+N>`**: Parasha planning mode — prepare for a specific upcoming parasha

### `--parasha` Argument

```
/dvar-torah --parasha בראשית          # Specific parasha by name
/dvar-torah --parasha +1              # Next week's parasha
/dvar-torah --parasha +3              # Three weeks from now
/dvar-torah --parasha current         # Current week (same as no argument)
```

**Resolution logic:**
1. If `--parasha current` or no argument: use `get_current_calendar()` to get this week's parsha
2. If `--parasha <name>`: look up the parasha by name — use `python scripts/sefaria_api.py get-calendar` and find the matching week
3. If `--parasha +N`: call `get_current_calendar()`, then advance N weeks in the annual cycle

Once the parasha is resolved, proceed normally with `topic.type = "parsha"` and `topic.value = <resolved parasha name>`.

## דוגמאות

```
/dvar-torah
/dvar-torah פרשת בראשית
/dvar-torah --parasha +1                                     # Next week's parsha
/dvar-torah --parasha נח                                      # Parsha Noach
/dvar-torah פורמט: פוסט, נושא: השגחה פרטית
/dvar-torah אוריינטציה: קבלה, נושא: ספירות, הקשר: שבת
/dvar-torah אוריינטציה: חסידות, נושא: דבקות, הקשר: חתונה
/dvar-torah פורמט: שיעור, אורך: שיעור, נושא: בחירה חופשית, הוגים: רמב״ם, קרשקש
/dvar-torah סוג: מחקרי, נושא: חוקי המזרח הקדום בפרשת משפטים
/dvar-torah פורמט: דבר-תורה, אורך: ארוך, נושא: נבואה, הוגים: רמב״ם, רלב״ג, ר״י הלוי
```

## כללים

- כל מקור מאומת ב-Sefaria MCP — אף ציטוט בלי אימות
- מראי מקומות בפורמט אחיד (skill: verify)
- שמור את התוצר בתיקייה המתאימה
- למד מכתיבות קודמות (skill: previous)
- הכבד כל זרם מחשבה — הצג בנאמנות
