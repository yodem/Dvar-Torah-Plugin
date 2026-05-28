# Dvar Torah Plugin — Developer & Contributor Reference

This file is for contributors, maintainers, and Claude Code itself.
For user-facing docs, see `README.md`.

---

## Repo Structure

```
Dvar-Torah-Plugin/
├── CLAUDE.md                          ← you are here
├── README.md                          ← user-facing docs
├── .claude-plugin/
│   └── marketplace.json               ← marketplace catalog (name: yodem)
├── .mcp.json                          ← Sefaria MCP config for local dev
├── plugins/
│   └── dvar-torah-plugin/             ← canonical plugin root
│       ├── .claude-plugin/plugin.json ← plugin manifest
│       ├── CLAUDE.md                  ← full architecture + agent routing
│       ├── skills/                    ← 9 SKILL.md files
│       ├── agents/                    ← 7 agent definitions
│       ├── hooks/                     ← PostToolUse + Stop hooks
│       ├── commands/
│       │   └── dvar-torah.md          ← /dvar-torah entry point
│       └── scripts/
│           └── sefaria_api.py         ← direct REST fallback
└── scripts/
    └── build-plugin.sh                ← packaging helper
```

---

## Plugin Pipeline

```
User: /dvar-torah [params]
         │
         ▼
  commands/dvar-torah.md          ← resolves params or launches wizard
         │
    ┌────┴────┐
    │  params? │
    └────┬────┘
     no  │  yes ──────────────────────────────────┐
         ▼                                         │
  skills/wizard  (haiku, ~5s)                      │
  8-step interactive intake                         │
  language → orientation → format →                │
  length → topic → thinkers → context → previous   │
         │                                         │
         └──────────────────┬──────────────────────┘
                            ▼
                  skills/compose  (sonnet, orchestrator)
                  launches Phase 1 agents in parallel:
                  ┌──────────────────────────────┐
                  │ source-researcher  (haiku)    │
                  │ previous-analyzer  (haiku)    │
                  │ historical-researcher (haiku) │ ← conditional
                  │ mussar agent       (haiku)    │ ← conditional
                  └──────────────────────────────┘
                            │
                  Phase 2 agents in parallel:
                  ┌──────────────────────────────┐
                  │ philosophical-analyzer (sonnet)│
                  │ source-verifier        (haiku) │
                  └──────────────────────────────┘
                            │
                  Phase 3:
                  ┌──────────────────────────────┐
                  │ torah-writer           (opus)  │ ← final output
                  └──────────────────────────────┘
                            │
                            ▼
               output written to user's project at:
               output/divrei-torah/{format}/YYYY-MM-DD-{topic}.md
```

---

## Skills Reference

| Skill | Model | Context | Invocable | Purpose |
|-------|-------|---------|-----------|---------|
| `wizard` | haiku | fork | no (called by compose) | 8-step interactive intake |
| `compose` | sonnet | fork | yes | orchestrator — dispatches all agents in parallel |
| `research` | haiku | fork | yes | Sefaria source search + bibliography |
| `analyze` | sonnet | fork | yes | philosophical analysis across thinkers |
| `verify` | haiku | fork | yes | citation verification + standard formatting |
| `mussar` | haiku | fork | no | ethical/practical dimensions from Mussar texts |
| `history` | haiku | fork | yes | ANE parallels, archaeology, biblical criticism |
| `previous` | haiku | fork | yes | pattern analysis from user's past writings |
| `setup` | — | inherit | yes | initial setup — language, Sefaria check, readiness score |
| `profile` | — | inherit | yes | (optional) orientation, thinkers, writing style |

**Model rationale:** Haiku for high-volume retrieval (fast, cheap). Sonnet for deep reasoning. Opus for final writing only (most capable, slowest, used once per run).

**`context: fork`** means the skill runs in an isolated subagent with its own context window — no bleed from the parent conversation. `context: inherit` (setup only) shares the parent's context, needed to read user preferences.

---

## Agents Reference

| Agent file | Called by | Model | Phase | Role |
|-----------|-----------|-------|-------|------|
| `source-researcher.md` | compose | haiku | 1 | Sefaria lookups — texts, links, search |
| `previous-analyzer.md` | compose | haiku | 1 | Scan output/ for patterns, avoid repetition |
| `historical-researcher.md` | compose | haiku | 1 | ANE parallels, Kaufmann, Cassuto (conditional) |
| `mussar agent` | compose | haiku | 1 | Mesillat Yesharim, Sha'arei Teshuvah (conditional) |
| `philosophical-analyzer.md` | compose | sonnet | 2 | Multi-thinker dialectical analysis |
| `source-verifier.md` | compose | haiku | 2 | Confirm every citation exists in Sefaria |
| `torah-writer.md` | compose | opus | 3 | Compose final piece (never called for non-writing tasks) |

**Conditional agents** (historical-researcher, mussar) are only spawned when the selected orientation or topic warrants it. This keeps the pipeline lean for simple use cases.

---

## Allowed-Tools per Skill

Each skill declares only the tools it needs. This is enforced in the frontmatter.

| Skill | Key tools |
|-------|-----------|
| wizard | `AskUserQuestion`, `mcp__claude_ai_Sefaria__*`, `mcp__memory__*` |
| compose | `Agent`, `Read`, `Write`, `Glob` |
| research | `mcp__claude_ai_Sefaria__*`, `Bash` (sefaria_api.py fallback) |
| analyze | `mcp__claude_ai_Sefaria__*`, `Read` |
| verify | `mcp__claude_ai_Sefaria__*`, `Read`, `Edit` |
| history | `mcp__claude_ai_Sefaria__*`, `WebSearch`, `Bash` |
| mussar | `mcp__claude_ai_Sefaria__*`, `Read` |
| previous | `Glob`, `Read` |
| setup | `Read`, `Grep`, `Glob`, `Bash`, `Write`, `AskUserQuestion`, `mcp__claude_ai_Sefaria__get_current_calendar` |

---

## Sefaria MCP — Two Access Patterns

```python
# Pattern 1 — MCP tools (preferred for discovery and semantic search)
mcp__claude_ai_Sefaria__english_semantic_search("divine providence Rambam")
mcp__claude_ai_Sefaria__get_text("Guide for the Perplexed 3:17")

# Pattern 2 — REST API fallback (faster for known references)
python scripts/sefaria_api.py get-text "Genesis 1:1"
python scripts/sefaria_api.py get-calendar          # current parasha
python scripts/sefaria_api.py get-links "Berakhot 5a"
```

Use MCP for exploration. Use the API script when you already have the exact reference.

---

## Core Invariant

**Every citation must pass Sefaria verification before appearing in output.**

The `source-verifier` agent runs in parallel with analysis (Phase 2) and rejects any citation that Sefaria cannot confirm. The `torah-writer` only receives verified sources. This is non-negotiable — no fabricated references, ever.

---

## Adding a New Orientation

1. Add an entry to `skills/wizard/SKILL.md` → Step 0.5 options
2. Add thinker list to `skills/wizard/SKILL.md` → Step 4 (filtered by orientation)
3. Add thinker details to `skills/compose/references/thinkers-by-subject.md`
4. Add thinker profiles to `skills/compose/references/thinkers-guide.md`
5. Update the orientation routing table in `plugins/dvar-torah-plugin/CLAUDE.md`
6. Bump `version` in `plugin.json` and `marketplace.json`

## Adding a New Thinker to an Existing Orientation

1. Add to `skills/wizard/SKILL.md` → thinker list for that orientation
2. Add profile to `skills/compose/references/thinkers-guide.md`
3. Add to `skills/compose/references/thinkers-by-subject.md`

---

## Publishing a New Version

1. Update `version` in:
   - `plugins/dvar-torah-plugin/.claude-plugin/plugin.json`
   - `.claude-plugin/marketplace.json`
2. Commit + push to `main`
3. Tag the release: `git tag v{version} && git push origin v{version}`

Users will get the new version on next `/plugin install dvar-torah-plugin@yodem`.
