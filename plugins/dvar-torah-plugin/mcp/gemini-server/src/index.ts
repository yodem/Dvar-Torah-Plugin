/**
 * dvar-torah-plugin Gemini MCP server.
 *
 * Routes the plugin's prose phases (writing dvar torah / posts / shiurim,
 * synthesis, edits, calibration samples) to Gemini. Claude Code spawns this
 * server via the plugin manifest; subagents inherit access to its tools.
 * Sefaria source verification is NOT routed here — it stays on Claude
 * (source-verifier agent) via the Sefaria MCP.
 *
 * Five tools:
 *   - gemini_write_section
 *   - gemini_synthesize
 *   - gemini_edit
 *   - gemini_calibrate_sample
 *   - gemini_raw
 *
 * Auth, retry, calibration-bundle caching, and thinking-API split are handled
 * inside the bundled modules; the server itself is a thin adapter.
 */
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

import { runWriteSection, WriteSectionInput } from './tools/write_section.js';
import { runSynthesize, SynthesizeInput } from './tools/synthesize.js';
import { runEdit, EditInput } from './tools/edit.js';
import { runCalibrateSample, CalibrateSampleInput } from './tools/calibrate_sample.js';
import { runRaw, RawInput } from './tools/raw.js';
import { isStructuredError } from './bundle.js';
import { resolveApiKey } from './gemini-client.js';
import { noCredentials, toToolResult, type StructuredError } from './errors.js';

/**
 * Wraps a tool handler:
 *   - checks credentials and returns no_credentials structured error if absent
 *   - catches StructuredError (no_credentials / api_error / transient / validation)
 *     and returns it as an isError MCP result
 *   - unexpected errors are mapped to api_error
 */
function wrap<T>(
  run: (input: unknown) => Promise<T>,
): (input: unknown) => Promise<{
  content: Array<{ type: 'text'; text: string }>;
  isError?: boolean;
}> {
  return async (input: unknown) => {
    const key = await resolveApiKey();
    if (!key) return toToolResult(noCredentials());
    try {
      const result = await run(input);
      return {
        content: [
          { type: 'text', text: JSON.stringify(result) },
        ],
      };
    } catch (err) {
      if (isStructuredError(err)) return toToolResult(err);
      const fallback: StructuredError = {
        code: 'api_error',
        message: err instanceof Error ? err.message : String(err),
      };
      return toToolResult(fallback);
    }
  };
}

async function main(): Promise<void> {
  const server = new McpServer({
    name: 'dvar-torah-gemini',
    version: '0.1.0',
  });

  server.registerTool(
    'gemini_write_section',
    {
      description:
        'Draft a complete dvar torah / post / shiur section (all paragraphs) via Gemini with built-in self-review against style fingerprint, register, anti-AI patterns, and repetition. Returns paragraphs with citation source_ids and self-review scores. Caller (torah-writer) then runs the Claude source-verifier as a hard gate against Sefaria.',
      inputSchema: WriteSectionInput.shape,
    },
    wrap(runWriteSection),
  );

  server.registerTool(
    'gemini_synthesize',
    {
      description:
        'Cross-section polish pass over a full dvar torah draft. Improves transitions, removes repetition, smooths voice drift. Never touches Sefaria citation strings, verse references, or footnote markers.',
      inputSchema: SynthesizeInput.shape,
    },
    wrap(runSynthesize),
  );

  server.registerTool(
    'gemini_edit',
    {
      description:
        "Apply a single edit instruction to an existing passage in the writer's voice. Preserves Sefaria citations, verse references, and quoted Torah / rabbinic material verbatim.",
      inputSchema: EditInput.shape,
    },
    wrap(runEdit),
  );

  server.registerTool(
    'gemini_calibrate_sample',
    {
      description:
        "Produce one calibration paragraph from a topic brief for side-by-side voice comparison. Used during /dvar-torah:setup to approve Gemini for this plugin install.",
      inputSchema: CalibrateSampleInput.shape,
    },
    wrap(runCalibrateSample),
  );

  server.registerTool(
    'gemini_raw',
    {
      description:
        'Escape-hatch tool: send an arbitrary system+prompt to Gemini. Bypasses the calibration bundle. Intended for one-off pings (e.g. /dvar-torah:setup key test).',
      inputSchema: RawInput.shape,
    },
    wrap(runRaw),
  );

  const transport = new StdioServerTransport();
  await server.connect(transport);
}

// keep TS happy with unused z import for downstream extensions
void z;

main().catch((err: unknown) => {
  const msg = err instanceof Error ? err.message : String(err);
  // MCP stdio uses stdout for protocol; emit fatal-startup errors to stderr.
  process.stderr.write(`[gemini-mcp] fatal: ${msg}\n`);
  process.exit(1);
});
