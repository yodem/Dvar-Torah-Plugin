#!/usr/bin/env python3
"""
Gemini API writer for dvar-torah plugin bridge-post format.

Usage:
  python scripts/gemini_writer.py \
    --voice voices/yahadotech.yaml \
    --template references/bridge-post-template.md \
    --bundle /tmp/research-bundle.json

Reads $GEMINI_API_KEY from environment.
Uses only stdlib (urllib, json) — zero pip dependencies.
"""

import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from typing import Optional


GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"
TIMEOUT = 60
MAX_RETRIES = 3


def load_voice_profile(path: str) -> dict:
    """Load a YAML voice profile using a minimal stdlib parser."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Voice profile not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return _parse_simple_yaml(content)


def _parse_simple_yaml(text: str) -> dict:
    """Minimal YAML parser for voice profiles — handles scalars, lists, nested maps."""
    result = {}
    stack = [(result, -1)]
    lines = text.split('\n')
    for line in lines:
        stripped = line.rstrip()
        if not stripped or stripped.startswith('#'):
            continue
        indent = len(line) - len(line.lstrip())
        content = stripped.lstrip()
        while len(stack) > 1 and indent <= stack[-1][1]:
            stack.pop()
        current = stack[-1][0]
        if content.startswith('- '):
            value = content[2:].strip().strip('"').strip("'")
            if isinstance(current, dict):
                last_key = list(current.keys())[-1] if current else None
                if last_key and isinstance(current[last_key], list):
                    current[last_key].append(value)
            elif isinstance(current, list):
                current.append(value)
        elif ':' in content:
            key, _, val = content.partition(':')
            key = key.strip().strip('"').strip("'")
            val = val.strip()
            if val == '' or val == '|':
                next_line_idx = lines.index(line) + 1 if line in lines else -1
                if next_line_idx < len(lines):
                    next_stripped = lines[next_line_idx].lstrip()
                    if next_stripped.startswith('- '):
                        current[key] = []
                        stack.append((current, indent))
                    else:
                        current[key] = {}
                        stack.append((current[key], indent))
                else:
                    current[key] = {}
                    stack.append((current[key], indent))
            else:
                val = val.strip('"').strip("'")
                if val.lower() == 'true':
                    val = True
                elif val.lower() == 'false':
                    val = False
                elif val.isdigit():
                    val = int(val)
                current[key] = val
    return result


def build_system_prompt(profile: dict, template: str) -> str:
    """Build a system prompt from voice profile + template."""
    parts = []
    parts.append("You are a blog post writer. Write in the following voice and style:")
    parts.append("")
    parts.append(f"Register: {profile.get('register', 'formal')}")
    parts.append(f"Language: {profile.get('language', 'he')}")
    ss = profile.get('sentence_style', {})
    if ss:
        parts.append(f"Sentence style: {ss.get('avg_length', '')}, {ss.get('structure', '')}")
    ps = profile.get('paragraph_style', {})
    if ps:
        parts.append(f"Paragraph pattern: {ps.get('pattern', '')}")
        parts.append(f"Max paragraphs: {ps.get('max_paragraphs', 10)}")
    tone = profile.get('tone', {})
    if tone:
        parts.append(f"Personal anecdotes: {'yes' if tone.get('personal_anecdotes') else 'no'}")
        parts.append(f"Humor: {tone.get('humor', 'none')}")
        parts.append(f"Self-reference: {tone.get('self_reference', 'rare')}")
        parts.append(f"Community address: {tone.get('community_address', 'formal')}")
    ti = profile.get('torah_integration', {})
    if ti:
        parts.append(f"Citation style: {ti.get('citation_style', 'inline')}")
        parts.append(f"Citation density: {ti.get('citation_density', '1-2')}")
        thinkers = ti.get('preferred_thinkers', [])
        if thinkers:
            parts.append(f"Preferred thinkers: {', '.join(thinkers)}")
    parts.append("")
    parts.append("Follow this template structure:")
    parts.append(template)
    return '\n'.join(parts)


def build_user_prompt(bundle: dict) -> str:
    """Build a user prompt from the research bundle."""
    parts = []
    parts.append("Write a bridge-post based on the following research:\n")
    dr = bundle.get('domain_research', {})
    if dr:
        parts.append("## Tech Concept")
        parts.append(f"Concept: {dr.get('concept', '')}")
        parts.append(f"Definition: {dr.get('definition', '')}")
        if dr.get('key_points'):
            parts.append(f"Key points: {json.dumps(dr['key_points'], ensure_ascii=False)}")
        parts.append("")
    sources = bundle.get('sources', [])
    if sources:
        parts.append("## Torah Sources")
        for s in sources:
            parts.append(f"- {s.get('ref', '')}: \"{s.get('quote', '')}\"")
        parts.append("")
    ba = bundle.get('bridge_analysis', {})
    if ba:
        parts.append("## Bridge Analysis")
        parts.append(f"Primary analogy: {ba.get('primary', '')}")
        if ba.get('secondary_points'):
            for p in ba['secondary_points']:
                parts.append(f"- {p}")
        parts.append("")
    sign_off = bundle.get('sign_off', '')
    if sign_off:
        parts.append("## Sign-off")
        parts.append(sign_off)
    return '\n'.join(parts)


def call_gemini_api(system_prompt: str, user_prompt: str, *,
                    model: str, api_key: Optional[str],
                    temperature: float, max_tokens: int) -> str:
    """Call Gemini REST API and return generated text."""
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Export it in your shell profile.")
    url = f"{GEMINI_API_BASE}/{model}:generateContent?key={api_key}"
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"parts": [{"text": user_prompt}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens,
        }
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data,
                                 headers={"Content-Type": "application/json"})
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                body = json.loads(r.read().decode())
                return body['candidates'][0]['content']['parts'][0]['text']
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < MAX_RETRIES - 1:
                wait = 2 ** attempt
                print(f"Rate limited, retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise


def main():
    parser = argparse.ArgumentParser(description="Gemini writer for dvar-torah bridge-posts")
    parser.add_argument('--voice', required=True, help='Path to voice profile YAML')
    parser.add_argument('--template', required=True, help='Path to template markdown')
    parser.add_argument('--bundle', required=True, help='Path to research bundle JSON')
    args = parser.parse_args()
    profile = load_voice_profile(args.voice)
    with open(args.template, 'r', encoding='utf-8') as f:
        template = f.read()
    with open(args.bundle, 'r', encoding='utf-8') as f:
        bundle = json.load(f)
    writer_cfg = profile.get('writer', {})
    model = writer_cfg.get('model', 'gemini-2.5-flash')
    temperature = writer_cfg.get('temperature', 0.8)
    max_tokens = writer_cfg.get('max_tokens', 2000)
    api_key = os.environ.get('GEMINI_API_KEY')
    system_prompt = build_system_prompt(profile, template)
    user_prompt = build_user_prompt(bundle)
    result = call_gemini_api(system_prompt, user_prompt,
                             model=model, api_key=api_key,
                             temperature=temperature, max_tokens=max_tokens)
    print(result)


if __name__ == '__main__':
    main()
