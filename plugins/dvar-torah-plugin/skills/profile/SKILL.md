---
name: profile
license: MIT
compatibility: "Claude Code 2.1.59+."
description: "Optional profiling wizard — configure default orientation, preferred thinkers, and writing style for personalized dvar torah output."
context: inherit
version: 1.0.0
author: yodem
tags: [profile, preferences, orientation, thinkers, style, personalization]
user-invocable: true
disable-model-invocation: false
allowed-tools: [Read, Grep, Glob, Bash, Write, AskUserQuestion]
metadata:
  category: configuration
---

# Dvar Torah Plugin — Profile

Optional personalization wizard. Configure your default orientation, preferred thinkers, and writing style so `/dvar-torah` tailors output to your preferences.

You don't need to run this — the `/dvar-torah` wizard asks these questions each time. But if you want consistent defaults, this saves them.

## Quick Start

```bash
/dvar-torah:profile              # Full profile wizard
```

## Phases

| Phase | What | Output |
|-------|------|--------|
| 1. Orientation | Which Jewish thought stream(s) to default to | Orientation saved |
| 2. Thinkers | Choose default thinkers (filtered by orientation) | Preferences saved |
| 3. Style | Describe your writing style in your own words | Style saved |

---

## Phase 1: Orientation Preference

Which Jewish thought stream(s) to default to? This determines which thinkers appear in the `/dvar-torah` wizard.

```python
AskUserQuestion(questions=[{
  "question": "באיזה זרם מחשבה תרצה להתמקד בדרך כלל? / Which Jewish thought stream(s)?",
  "header": "אוריינטציה / Orientation",
  "options": [
    {
      "label": "פילוסופיה יהודית — Rationalists",
      "description": "רמב״ם, רס״ג, רלב״ג, קרשקש, אלבו, ר״י הלוי",
      "markdown": "```\nRationalist Philosophy\n──────────────────────\nRambam, Rasag, Ralbag, Crescas, Albo, Kuzari\nCore: Aristotelian rationalism, harmony of Torah & reason\n```"
    },
    {
      "label": "קבלה — Kabbalah",
      "description": "זוהר, האר״י, רמ״ק, רמח״ל",
      "markdown": "```\nKabbalah\n────────\nZohar, Pardes Rimonim, Etz Chaim, Daat Tevunot\nCore: Sefirot, Ein Sof, tzimtzum, tikkun\n```"
    },
    {
      "label": "חסידות — Hasidut",
      "description": "בעש״ט, תניא, ברסלב, קדושת לוי",
      "markdown": "```\nHasidut\n───────\nKeter Shem Tov, Maggid, Tanya, Likkutei Moharan\nCore: Devekut, simcha, Tzaddik, avodah\n```"
    },
    {
      "label": "חז״ל — Talmudic Sages",
      "description": "משנה, גמרא, מדרש",
      "markdown": "```\nHazal\n─────\nMishnah, Talmud Bavli, Bereishit Rabbah, Midrash Tanchuma\nCore: Halakha, Aggadah, rabbinic thought\n```"
    },
    {
      "label": "חוקרים מודרניים — Modern Scholars",
      "description": "Wissenschaft, ANE, ביקורת המקרא",
      "markdown": "```\nModern Scholarship\n──────────────────\nKaufmann, Cassuto, Pines, Wellhausen (contrast), ANE texts\nCore: Historical context, documentary hypothesis\n```"
    }
  ],
  "multiSelect": true
}])
```

Persist as env var:
```
DVAR_TORAH_ORIENTATION="philosophy"  # philosophy | kabbalah | hasidut | hazal | modern (comma-separated for multiple)
```

---

## Phase 2: Thinker Preferences

Ask which thinkers to feature by default. These become the pre-selected defaults in the `/dvar-torah` wizard.
**Filter thinker list based on orientation(s) selected in Phase 1.**

```python
AskUserQuestion(questions=[{
  "question": "אילו הוגים להגדיר כברירת מחדל? / Which thinkers as defaults?",
  "header": "הוגים / Default Thinkers",
  # Show only thinkers from selected orientation(s):
  # philosophy → Rambam, Rasag, Ralbag, Crescas, Albo, Ibn Ezra, Kuzari, Ibn Paquda
  # kabbalah   → Zohar, Ramak, Ari, Ramchal
  # hasidut    → Besht, Maggid, Admur HaZaken, Nachman, Levi Yitzchak
  # hazal      → Tannaim, Amoraim, Midrash, individual sages
  # modern     → Kaufmann, Cassuto, Pines, Altmann, Harvey, Wellhausen (contrast)
  "multiSelect": true
}])
```

Save the selection:
```python
DVAR_TORAH_DEFAULT_THINKERS="רמב״ם,קרשקש"   # comma-separated
```

---

## Phase 3: Writing Style

Instead of picking from presets, let the user describe their own style. This makes the profile truly personal.

```python
AskUserQuestion(questions=[{
  "question": "תאר את סגנון הכתיבה שלך / Describe your writing style",
  "header": "סגנון כתיבה / Writing Style",
  "options": [
    {
      "label": "אקדמי-פילוסופי",
      "description": "מבני, מדויק, מקורות ראשוניים"
    },
    {
      "label": "שיחתי-נגיש",
      "description": "חם, אישי, מתאים לשולחן שבת"
    },
    {
      "label": "דרשני-רטורי",
      "description": "רטורי, מרתק, לקהל רחב"
    },
    {
      "label": "אחר — אתאר בעצמי",
      "description": "כתוב תיאור חופשי של הסגנון שלך"
    }
  ],
  "multiSelect": false
}])
```

If the user selects "אחר", ask them to describe their style in free text.

Persist:
```
DVAR_TORAH_STYLE_DESCRIPTION="..."  # free-text style description
```

---

## Done

```
Profile saved! Your defaults:
  Orientation: פילוסופיה
  Thinkers:    רמב״ם, קרשקש
  Style:       אקדמי-פילוסופי

These will be pre-selected in /dvar-torah. You can always override per session.
To update: /dvar-torah:profile
```
