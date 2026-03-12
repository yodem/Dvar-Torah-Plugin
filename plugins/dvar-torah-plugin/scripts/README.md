# Sefaria API Script

Direct REST API access to Sefaria — faster than MCP for targeted lookups of known references.

## When to use

| Use case | Recommended tool |
|----------|-----------------|
| Semantic discovery ("find texts about providence") | MCP `english_semantic_search` |
| Fetch a known reference exactly | This script (`get-text`) |
| Get commentary on a specific verse | This script (`get-links`) |
| Resolve a book/author name | This script (`lookup-name`) |
| Current parsha / daf yomi | This script (`get-calendar`) |

## Commands

```bash
# Fetch text by reference
python scripts/sefaria_api.py get-text "Genesis 1:1"
python scripts/sefaria_api.py get-text "Guide for the Perplexed 1:1"
python scripts/sefaria_api.py get-text "Berakhot 5a"

# Commentary and cross-references for a verse
python scripts/sefaria_api.py get-links "Genesis 1:1"

# Topic metadata
python scripts/sefaria_api.py get-topic "providence"
python scripts/sefaria_api.py get-topic "free-will"

# Resolve a name (book or person)
python scripts/sefaria_api.py lookup-name "Rambam"
python scripts/sefaria_api.py lookup-name "Or Hashem"

# Current calendar (parsha, daf yomi, etc.)
python scripts/sefaria_api.py get-calendar

# Book structure and metadata
python scripts/sefaria_api.py get-catalogue "Mishneh Torah"
python scripts/sefaria_api.py get-catalogue "Guide for the Perplexed"

# Full-text search (fallback when MCP unavailable)
python scripts/sefaria_api.py search "human intellect" --size 5
python scripts/sefaria_api.py search "tzelem elohim" --size 10
```

## Output

All commands return clean JSON to stdout. Errors go to stderr with exit code 1.

## Requirements

Python 3.7+ (standard library only — no pip install needed).
No authentication required for Sefaria's public API.
