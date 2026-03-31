<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/Claude_Code-Plugin-blueviolet" alt="Claude Code Plugin">
  <img src="https://img.shields.io/badge/Sefaria-MCP_Powered-orange" alt="Sefaria MCP">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
</p>

<h1 align="center">דבר תורה<br><sub>Dvar Torah Plugin for Claude Code</sub></h1>

<p align="center">
Write source-verified divrei Torah, posts, and shiurim — powered by <a href="https://www.sefaria.org">Sefaria MCP</a>. No fabricated citations. Ever.
</p>

---

## Setup

### 1. Add the marketplace

```bash
claude plugin marketplace add yodem/Dvar-Torah-Plugin
```

### 2. Install the plugin

```bash
claude plugin install dvar-torah-plugin@yodem
```

### 3. Connect Sefaria

Go to [claude.ai/settings/integrations](https://claude.ai/settings/integrations) → find **Sefaria** → click **Connect**.

Or via CLI:
```
/mcp add-oauth Sefaria
```

### 4. Run setup

```
/dvar-torah:setup
```

---

## Usage

```
/dvar-torah                                    # guided wizard
/dvar-torah פרשת בראשית                         # specific parsha
/dvar-torah format:post, topic:"free will"      # quick post
/dvar-torah orientation:kabbalah, topic:sefirot  # kabbalistic piece
```

| Command | Purpose |
|---------|---------|
| `/dvar-torah` | Write a dvar Torah (wizard or direct params) |
| `/dvar-torah:setup` | First-time setup |
| `/dvar-torah:research <topic>` | Search Sefaria sources |
| `/dvar-torah:analyze <question>` | Philosophical analysis |
| `/dvar-torah:verify` | Verify citations in a draft |

---

## License

MIT — [@yodem](https://github.com/yodem) · [Sefaria](https://www.sefaria.org) + [Claude Code](https://claude.ai/code)
