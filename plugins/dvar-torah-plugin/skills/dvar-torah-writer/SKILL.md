---
name: dvar-torah-writer
license: MIT
compatibility: "Claude Code 2.1.59+."
author: yodem
description: כתיבת דבר תורה מקיף בכל זרם מחשבה יהודית — פילוסופיה, קבלה, חסידות, חז״ל, מחקר מודרני. Use when writing a Dvar Torah, preparing a Torah lecture, writing a post, analyzing a parsha, or exploring Jewish thought.
version: 4.1.0
tags: [dvar-torah, jewish-philosophy, kabbalah, hasidut, hazal, rambam, sefaria, mussar, jewish-thought, post, shiur, parallel-agents]
user-invocable: true
context: fork
complexity: high
model: sonnet
metadata:
  category: content-creation
  orchestration: parallel-agents
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Agent
  - AskUserQuestion
  - mcp__claude_ai_Sefaria__get_current_calendar
---

# דבר תורה — Orchestrator (v4.0)

## Architecture

This skill is an **orchestrator** — it dispatches specialized agents in parallel, then feeds results to the writer. It does NOT do research or writing itself.

```
Phase 1 — Research (parallel, haiku)
  ├── previous-analyzer        ← scan output/ for patterns
  ├── source-researcher        ← Sefaria lookups
  ├── historical-researcher    ← if topic.type == "research" or orientation == "modern"
  └── source-researcher        ← mussar sources (if mussar requested)

Phase 2 — Analysis + Verification (parallel)
  ├── philosophical-analyzer   ← sonnet: deep reasoning with Phase 1 sources
  └── source-verifier          ← haiku: verify all Phase 1 citations

Phase 3 — Writing (opus)
  └── torah-writer             ← opus: compose final piece from all results
```

## Config Input

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
    description: "from contexts-guide.md"
  previous_patterns:
    mode: "avoid" | "base_on"
    base_documents: [...]
    template_guidance: {...}
  include_mussar: true | false
```

## Orientation Routing

### philosophy — פילוסופיה יהודית
Thinkers: רמב״ם, רס״ג, רלב״ג, קרשקש, אלבו, ר״י הלוי, אבן עזרא, אבן פקודה
Sefaria: "Guide for the Perplexed", "Emunot veDeot", "Milhamot HaShem", "Or Hashem", "Kuzari"

### kabbalah — קבלה
Thinkers: זוהר, רמ״ק, האר״י, רמח״ל
Sefaria: "Zohar", "Pardes Rimonim", "Etz Chaim", "Daat Tevunot"
Hint: `get_text_or_category_shape(path="Kabbalah")`

### hasidut — חסידות
Thinkers: בעש״ט, מגיד, תניא, ברסלב, קדושת לוי
Sefaria: "Tanya", "Likkutei Moharan", "Keter Shem Tov", "Maggid Devarav LeYaakov"
Hint: `get_text_or_category_shape(path="Chasidut")`

### hazal — חז״ל
Thinkers: תנאים, אמוראים, מדרשים
Sefaria: "Talmud Bavli", "Jerusalem Talmud", "Bereishit Rabbah", "Midrash Tanchuma"

### modern — חוקרים מודרניים
Thinkers: קאופמן, קסוטו, פינס, אלטמן + ANE texts
Default to historical-researcher agent

## Execution

### Step 0: Interactive Wizard (if needed)

If the user did not provide full config — invoke `interactive-cli` skill to collect parameters. Once config is complete, proceed to orchestration.

### Step 1: Resolve topic

If `topic.type == "parsha"` and no specific parsha given:
```
mcp__claude_ai_Sefaria__get_current_calendar()
# or faster: python scripts/sefaria_api.py get-calendar
```
Set `topic.value` from the calendar result.

---

<use_parallel_tool_calls>
If you intend to call multiple tools and there are no dependencies between
the tool calls, make all of the independent tool calls in parallel. Prioritize
calling tools simultaneously whenever the actions can be done in parallel
rather than sequentially. Maximize use of parallel tool calls where possible
to increase speed and efficiency.
However, if some tool calls depend on previous calls to inform dependent
values, do NOT call these tools in parallel.

Agent dispatch pattern:
- Phase 1 agents: launch ALL in a single message with run_in_background: true
- Phase 2 agents: launch BOTH in a single message with run_in_background: true
- Phase 3 (torah-writer): foreground — wait for completion
</use_parallel_tool_calls>

### PHASE 1 — Research (parallel, all background)

Launch ALL of these agents in a **single message** with `run_in_background: true`:

#### Agent 1: previous-analyzer (haiku)
```
Agent(
  subagent_type: "dvar-torah-plugin:previous-analyzer",
  model: "haiku",
  run_in_background: true,
  prompt: """
    MODE: {previous_patterns.mode}
    {if mode == "base_on": "SELECTED_FILES: {previous_patterns.base_documents}"}
    Scan output/divrei-torah/ and return analysis per your instructions.
  """
)
```

#### Agent 2: source-researcher (haiku)
```
Agent(
  subagent_type: "dvar-torah-plugin:source-researcher",
  model: "haiku",
  run_in_background: true,
  prompt: """
    TOPIC: {topic.value} ({topic.type})
    ORIENTATION: {orientation}
    THINKERS: {thinkers}
    CONTEXT: {context.type}

    Search Sefaria for sources relevant to this topic.

    IMPORTANT: When the source is Talmudic or has Steinsaltz commentary available,
    FIRST read Steinsaltz for pshat understanding:
      get_text("Steinsaltz on <reference>")
    This gives you the baseline meaning before philosophical analysis.

    For orientation={orientation}, focus on:
    - philosophy: Guide for the Perplexed, Emunot veDeot, Milhamot HaShem, Or Hashem, Kuzari
    - kabbalah: Zohar, Pardes Rimonim, Etz Chaim, Daat Tevunot
    - hasidut: Tanya, Likkutei Moharan, Keter Shem Tov
    - hazal: Talmud Bavli, Bereishit Rabbah, Midrash Tanchuma
    - modern: academic scholarship + ANE parallels

    Search at least 3 different books. Find connections between sources.
    Return structured YAML with sources, quotes, and sefaria_refs.
  """
)
```

#### Agent 3: historical-researcher (haiku, CONDITIONAL)
Only launch if `topic.type == "research"` OR `orientation == "modern"`:
```
Agent(
  subagent_type: "dvar-torah-plugin:historical-researcher",
  model: "haiku",
  run_in_background: true,
  prompt: """
    TOPIC: {topic.value}
    VERSE/TEXT: {topic.sub_topic or topic.value}

    Research the historical and cultural context of this text.
    Find ANE parallels, archaeological evidence, and classical commentary.
    Return structured YAML.
  """
)
```

#### Agent 4: mussar source-researcher (haiku, CONDITIONAL)
Only launch if `include_mussar == true`:
```
Agent(
  subagent_type: "dvar-torah-plugin:source-researcher",
  model: "haiku",
  run_in_background: true,
  prompt: """
    TOPIC: {topic.value}
    ORIENTATION: mussar
    TASK: Search ONLY mussar literature for sources related to this topic.

    Search in:
    - Mesillat Yesharim
    - Chovot HaLevavot
    - Shaarei Teshuvah
    - Shemonah Perakim

    Identify which middah/virtue is relevant and find 2-3 mussar sources.
    Return structured YAML with sources, quotes, and practical applications.
  """
)
```

**Wait for all Phase 1 agents to complete before proceeding.**

---

### PHASE 2 — Analysis + Verification (parallel)

Launch BOTH agents in a **single message** with `run_in_background: true`:

#### Agent 5: philosophical-analyzer (sonnet)
```
Agent(
  subagent_type: "dvar-torah-plugin:philosophical-analyzer",
  model: "sonnet",
  run_in_background: true,
  prompt: """
    TOPIC: {topic.value}
    ORIENTATION: {orientation}
    THINKERS: {thinkers}
    CONTEXT: {context.type}

    SOURCES FROM PHASE 1:
    {source_researcher_results}

    {if historical: "HISTORICAL CONTEXT: {historical_researcher_results}"}
    {if mussar: "MUSSAR SOURCES: {mussar_researcher_results}"}

    Build a philosophical analysis:
    1. Identify the core philosophical question
    2. Map each thinker's position using the sources provided
    3. Build critical dialogue between positions
    4. Synthesize conclusions

    If sources are insufficient, you may search Sefaria for additional texts.
    Return structured YAML with question, positions, dialogue, synthesis.
  """
)
```

#### Agent 6: source-verifier (haiku)
```
Agent(
  subagent_type: "dvar-torah-plugin:source-verifier",
  model: "haiku",
  run_in_background: true,
  prompt: """
    CITATIONS TO VERIFY:
    {all citations from Phase 1 agents}

    Verify each citation through Sefaria MCP.
    Format all references uniformly.
    Build bibliography: תנ״ך → חז״ל → ראשונים → אחרונים → מחקר
  """
)
```

**Wait for both Phase 2 agents to complete.**

---

### PHASE 3 — Writing (opus)

Launch the writer with ALL collected results:

#### Agent 7: torah-writer (opus)
```
Agent(
  subagent_type: "dvar-torah-plugin:torah-writer",
  model: "opus",
  prompt: """
    WRITE a {format} in {language}.

    CONFIG:
    - Format: {format}
    - Length: {length}
    - Language: {language}
    - Orientation: {orientation}
    - Context: {context.type} — {context.description}
    - Thinkers: {thinkers}

    RESEARCH BUNDLE:
    ================

    PREVIOUS ANALYSIS:
    {previous_analyzer_results}

    SOURCES:
    {source_researcher_results}

    {if historical: "HISTORICAL CONTEXT:\n{historical_researcher_results}"}

    {if mussar: "MUSSAR:\n{mussar_researcher_results}"}

    PHILOSOPHICAL ANALYSIS:
    {philosophical_analyzer_results}

    VERIFIED CITATIONS:
    {source_verifier_results}

    {if base_on: "TEMPLATE GUIDANCE (FOLLOW STRICTLY):\n{template_guidance}"}

    INSTRUCTIONS:
    1. Read references/templates.md for the {format}/{length} template
    2. Read references/contexts-guide.md for {context.type} guidance
    3. Use ONLY verified citations (status: verified or corrected)
    4. Write the complete piece
    5. Save to: output/divrei-torah/{format_dir}/YYYY-MM-DD-{topic_slug}.md
    6. Include frontmatter with all metadata
  """
)
```

**This agent runs in FOREGROUND — wait for it to complete.**

---

## Context Guidance

Read `references/contexts-guide.md` per `context.type`:
- **shiva**: comforting tone, themes of loss and meaning
- **wedding**: joyful and poetic, themes of partnership and Shekhinah
- **bar_bat_mitzvah**: encouraging, themes of responsibility and free choice
- **general**: follow orientation only

## base_on Mode

If `previous_patterns.mode == "base_on"` and `template_guidance` exists:
- Pass `template_guidance.strict_instructions` to torah-writer
- Writer MUST follow: same structure, register, citation density, length (±20%)

## Output

Final output saved by torah-writer to:
```
output/divrei-torah/
  ├── dvar-torah/YYYY-MM-DD-<topic>.md
  ├── posts/YYYY-MM-DD-<topic>.md
  └── shiurim/YYYY-MM-DD-<topic>.md
```

Frontmatter:
```yaml
---
date: YYYY-MM-DD
format: dvar-torah | post | shiur
length: short | medium | long | shiur
language: he | en | bilingual
orientation: philosophy | kabbalah | hasidut | hazal | modern | custom
context: general | wedding | shabbat | shiva | ...
parsha: שם הפרשה (if relevant)
topic: הנושא
thinkers: [רמב״ם, רס״ג]
sources_count: N
agents_used: [source-researcher, philosophical-analyzer, torah-writer, ...]
---
```

## Sefaria MCP Tool Priority (for agents)

Research agents use tools in this order:
1. `english_semantic_search` — primary discovery
2. `get_links_between_texts` — connections & commentary
3. `get_text` — exact text (or: `python scripts/sefaria_api.py get-text "<ref>"`)
4. `get_text_catalogue_info` — metadata
5. `get_text_or_category_shape` — structure
6. `get_topic_details` — topic context
7. `search_in_book` — focused book search
8. `search_in_dictionaries` — term definitions
9. `text_search` — general fallback

This orchestrator uses only `get_current_calendar` (Step 1) or `python scripts/sefaria_api.py get-calendar`.
