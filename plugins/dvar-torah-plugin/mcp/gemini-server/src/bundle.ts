/**
 * Calibration bundle loader for the dvar-torah-plugin.
 *
 * Reads AUTHOR_VOICE / style fingerprint / anti-AI patterns from the project
 * and plugin dirs. ALL files are optional — the loader silently skips anything
 * absent. The plugin ships greenfield; users may have nothing yet.
 *
 * Cache lifetime == server process lifetime (~ Claude Code session).
 */
import { readFile } from 'node:fs/promises';
import * as path from 'node:path';
import { bundleLoadFailed, type StructuredError } from './errors.js';

export interface CalibrationBundle {
  voice: string;
  fingerprint: string;
  antiAi: string;
  targetLanguage: string;
}

const cache = new Map<string, CalibrationBundle>();

function projectDir(): string {
  return process.env.CLAUDE_PROJECT_DIR ?? process.cwd();
}

function pluginRoot(): string {
  const fromEnv = process.env.CLAUDE_PLUGIN_ROOT;
  if (fromEnv) return fromEnv;
  // dist/index.js lives at <plugin>/mcp/gemini-server/dist/index.js — plugin root is three up.
  return path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..', '..');
}

async function readOptional(filePath: string): Promise<string> {
  try {
    return await readFile(filePath, 'utf8');
  } catch {
    return '';
  }
}

/**
 * Pull the JSON block beneath `## Style Fingerprint` from profile.md.
 * Returns the JSON-string body, or '' if absent.
 */
function extractStyleFingerprint(profileMd: string): string {
  const header = /^##\s+Style Fingerprint\s*$/im;
  const m = header.exec(profileMd);
  if (!m) return '';
  const after = profileMd.slice(m.index + m[0].length);
  const fence = /```(?:json|JSON)?\s*\n([\s\S]*?)\n```/.exec(after);
  return fence ? fence[1].trim() : '';
}

function lang(t: string): string {
  return (t || 'hebrew').toLowerCase().trim();
}

async function loadAntiAi(plugin: string, targetLanguage: string): Promise<string> {
  const lc = lang(targetLanguage);
  // Primary location: compose skill references.
  const primary = path.join(
    plugin,
    'skills',
    'compose',
    'references',
    `anti-ai-patterns-${lc}.md`,
  );
  const got = await readOptional(primary);
  if (got) return got;
  // Fallback to Hebrew when targeting any other language and Hebrew exists.
  if (lc !== 'hebrew') {
    const fallback = path.join(
      plugin,
      'skills',
      'compose',
      'references',
      'anti-ai-patterns-hebrew.md',
    );
    return await readOptional(fallback);
  }
  return '';
}

export async function getBundle(targetLanguage: string): Promise<CalibrationBundle> {
  const key = lang(targetLanguage);
  const hit = cache.get(key);
  if (hit) return hit;

  const project = projectDir();
  const plugin = pluginRoot();

  try {
    const [voice, profileMd, antiAi] = await Promise.all([
      readOptional(path.join(project, 'AUTHOR_VOICE.md')),
      readOptional(path.join(project, '.dvar-torah', 'profile.md')),
      loadAntiAi(plugin, key),
    ]);

    const fingerprint = extractStyleFingerprint(profileMd);

    const bundle: CalibrationBundle = {
      voice,
      fingerprint,
      antiAi,
      targetLanguage: key,
    };
    cache.set(key, bundle);
    return bundle;
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    throw bundleLoadFailed(`Failed to load calibration bundle for ${key}: ${message}`) as unknown as Error;
  }
}

/**
 * Render the calibration bundle into a single markdown block to inject into
 * the system prompt template. Each section is conditional — absent inputs do
 * not produce empty headings.
 */
export function renderBundleMarkdown(b: CalibrationBundle): string {
  const sections: string[] = [];
  sections.push(`<!-- target_language: ${b.targetLanguage} -->`);
  if (b.voice) sections.push('## AUTHOR VOICE\n\n' + b.voice);
  if (b.fingerprint)
    sections.push('## STYLE FINGERPRINT (JSON)\n\n```json\n' + b.fingerprint + '\n```');
  if (b.antiAi) sections.push('## ANTI-AI PATTERNS\n\n' + b.antiAi);
  if (sections.length === 1) {
    // Only the language comment — give the model a defensible default.
    sections.push(
      '## CALIBRATION\n\n' +
        '(No author voice profile or style fingerprint configured yet. Write in a clear, traditional Jewish-thought register suitable for a dvar torah / post / shiur. Default to the target language above. Avoid AI tells: avoid empty hedges, listicle structures, and generic moralizing.)',
    );
  }
  return sections.join('\n\n---\n\n');
}

/** Test/escape-hatch: forget cached bundles. */
export function clearBundleCache(): void {
  cache.clear();
}

export function isStructuredError(e: unknown): e is StructuredError {
  return (
    typeof e === 'object' &&
    e !== null &&
    'code' in e &&
    typeof (e as { code: unknown }).code === 'string'
  );
}
