#!/usr/bin/env python3
"""
Sefaria REST API CLI — faster than MCP for targeted lookups.

Usage:
  python scripts/sefaria_api.py get-text "Genesis 1:1"
  python scripts/sefaria_api.py get-links "Genesis 1:1"
  python scripts/sefaria_api.py get-topic "providence"
  python scripts/sefaria_api.py lookup-name "Rambam"
  python scripts/sefaria_api.py get-calendar
  python scripts/sefaria_api.py get-catalogue "Mishneh Torah"
  python scripts/sefaria_api.py search "human intellect" --size 5

Use MCP english_semantic_search for semantic discovery.
Use this script for targeted lookups of known references.
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request


BASE = "https://www.sefaria.org/api"


def _get(path: str) -> dict:
    url = f"{BASE}{path}"
    with urllib.request.urlopen(url, timeout=15) as r:
        return json.loads(r.read().decode())


def _post(path: str, data: dict) -> dict:
    url = f"{BASE}{path}"
    payload = json.dumps(data).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode())


def cmd_get_text(ref: str) -> dict:
    """GET /api/v3/texts/{ref} — fetch text and translations."""
    encoded = urllib.parse.quote(ref, safe="")
    return _get(f"/v3/texts/{encoded}")


def cmd_get_links(ref: str) -> dict:
    """GET /api/links/{ref}?with_text=1 — commentaries and parallels."""
    encoded = urllib.parse.quote(ref, safe="")
    return _get(f"/links/{encoded}?with_text=1")


def cmd_get_topic(slug: str) -> dict:
    """GET /api/v2/topics/{slug} — topic metadata and related texts."""
    encoded = urllib.parse.quote(slug, safe="")
    return _get(f"/v2/topics/{encoded}")


def cmd_lookup_name(name: str) -> dict:
    """GET /api/name/{name} — resolve a book or person name."""
    encoded = urllib.parse.quote(name, safe="")
    return _get(f"/name/{encoded}")


def cmd_get_calendar() -> dict:
    """GET /api/calendars — current parsha, daf yomi, etc."""
    return _get("/calendars")


def cmd_get_catalogue(title: str) -> dict:
    """GET /api/v2/raw/index/{title} — book metadata and structure."""
    encoded = urllib.parse.quote(title, safe="")
    return _get(f"/v2/raw/index/{encoded}")


def cmd_search(query: str, size: int = 10) -> dict:
    """POST /api/search-wrapper — full-text search across Sefaria."""
    payload = {
        "query": query,
        "size": size,
        "type": "text",
        "field": "exact",
        "sort_type": "_score",
    }
    return _post("/search-wrapper", payload)


def main():
    parser = argparse.ArgumentParser(description="Sefaria REST API CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("get-text", help="Fetch a text by reference")
    p.add_argument("ref", help='e.g. "Genesis 1:1"')

    p = sub.add_parser("get-links", help="Get links/commentary for a reference")
    p.add_argument("ref")

    p = sub.add_parser("get-topic", help="Get topic details by slug")
    p.add_argument("slug", help='e.g. "providence"')

    p = sub.add_parser("lookup-name", help="Resolve a book or author name")
    p.add_argument("name", help='e.g. "Rambam"')

    sub.add_parser("get-calendar", help="Current parsha and daf yomi")

    p = sub.add_parser("get-catalogue", help="Book structure and metadata")
    p.add_argument("title", help='e.g. "Mishneh Torah"')

    p = sub.add_parser("search", help="Full-text search")
    p.add_argument("query")
    p.add_argument("--size", type=int, default=10, help="Number of results (default 10)")

    args = parser.parse_args()

    try:
        if args.command == "get-text":
            result = cmd_get_text(args.ref)
        elif args.command == "get-links":
            result = cmd_get_links(args.ref)
        elif args.command == "get-topic":
            result = cmd_get_topic(args.slug)
        elif args.command == "lookup-name":
            result = cmd_lookup_name(args.name)
        elif args.command == "get-calendar":
            result = cmd_get_calendar()
        elif args.command == "get-catalogue":
            result = cmd_get_catalogue(args.title)
        elif args.command == "search":
            result = cmd_search(args.query, args.size)
        else:
            parser.print_help()
            sys.exit(1)

        print(json.dumps(result, ensure_ascii=False, indent=2))

    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        print(json.dumps({"error": f"HTTP {e.code}", "detail": body}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
