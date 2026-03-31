# Dvar Torah Plugin — Claude Code Context

## What This Repo Is

A Claude Code plugin that writes divrei Torah, posts, and shiurim grounded in real Sefaria sources.
The canonical plugin lives in `plugins/dvar-torah-plugin/`.

## Key Files

| Path | Purpose |
|------|---------|
| `plugins/dvar-torah-plugin/CLAUDE.md` | Full architecture, agent routing, model strategy |
| `plugins/dvar-torah-plugin/skills/` | 9 skills (wizard, compose, research, analyze, verify, mussar, history, previous, setup) |
| `plugins/dvar-torah-plugin/agents/` | 7 specialized agent definitions |
| `plugins/dvar-torah-plugin/.mcp.json` | Sefaria MCP configuration (bundled) |
| `output/divrei-torah/` | Generated content (dvar-torah/, posts/, shiurim/) |
| `scripts/sefaria_api.py` | Direct REST fallback for targeted Sefaria lookups |

## Quick Commands

```
/dvar-torah              # interactive wizard → full pipeline
/dvar-torah:setup        # first-time setup + Sefaria check
/dvar-torah:research     # standalone Sefaria source search
/dvar-torah:analyze      # standalone philosophical analysis
```

## Model Strategy

- **Haiku** — wizard, research, verification (fast + cheap)
- **Sonnet** — philosophical analysis (deep reasoning)
- **Opus** — final writing only (quality output)

## Core Rule

Every citation must be retrieved and verified via Sefaria MCP. No fabricated sources.

## Development

See `plugins/dvar-torah-plugin/CLAUDE.md` for full architecture.
See `README.md` for user-facing installation and usage docs.
