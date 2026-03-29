# SR-PTD - Rational Dvar Torah Plugin Cleanup

**Date**: 2026-03-29 | **Type**: Refactor + Maintenance | **Domain**: Plugin architecture/docs | **Complexity**: High

## Trigger
> "Delete archive, keep one plugin, remove duplicate manifests, expand Sefaria section/writer coverage in markdown, and align with best practices."

## Workflow (numbered steps)
1. Audited repository structure, manifests, docs, and active plugin root.
2. Removed legacy artifacts (`archive`, `src`, old manifests, stale refactor test file).
3. Reworked build flow to treat `plugins/dvar-torah-plugin` as canonical source.
4. Normalized metadata by aligning `package.json` version with canonical plugin manifest.
5. Expanded Sefaria-aligned reference docs (`thinkers-by-subject.md`, `thinkers-guide.md`) across Jewish Thought, Chasidut, Musar, Kabbalah, Midrash/Hazal, and selected Halakhah frameworks.
6. Refreshed docs (`README.md`, `CLAUDE.md`, setup/templates wording) to remove v2 names and reflect current 9-skill architecture.
7. Verified no stale v2 references remain and ran lints + build validation script.

## Key Decisions
- Keep `plugins/dvar-torah-plugin/.claude-plugin/plugin.json` as the single canonical plugin manifest.
- Keep `.claude-plugin/marketplace.json` as catalog metadata only.
- Replace copy-based build logic with validation/sync logic to avoid accidental overwrite from legacy trees.
- Expand references with representative Sefaria corpora and authors (breadth-first) rather than only a short handpicked list.

## Knowledge Used
- **Code patterns**: Claude Code plugin structure, single-source-of-truth repo layout.
- **External taxonomy**: Sefaria category structure for Jewish Thought / Chasidut / Musar / Kabbalah / Midrash / Halakhah.
- **Best-practice context**: CandleKeep plugin/skills/tooling guidance already retrieved in-session.

## Code Written (if reusable)
```bash
# Validation build now checks canonical plugin and syncs package version:
bash scripts/build-plugin.sh
```

## Output Format (if templatable)
```text
Cleanup pattern:
1) Remove legacy trees
2) Set canonical manifest/root
3) Align package metadata
4) Expand domain references from source taxonomy
5) Remove stale names in docs/tests
6) Validate via grep/lint/build
```

## Issues -> Fixes
- Legacy naming references (`previous-analysis`) remained in active docs -> replaced with current `previous`.
- Version drift (`package.json` vs plugin manifest) -> unified to `4.2.0`.

## Skill Potential: High
**Notes**: This is a reusable migration pattern for plugin repos with legacy duplicated trees and stale documentation.

## Tags
Languages: markdown, json, bash | Domain: plugin-maintenance, docs-refactor | Services: Sefaria taxonomy
