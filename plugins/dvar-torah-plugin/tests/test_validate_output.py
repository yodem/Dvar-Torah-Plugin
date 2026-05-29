"""Tests for validate-output.sh hook — bridge-post format awareness."""
import json
import os
import subprocess
import tempfile
import unittest

HOOK = os.path.join(os.path.dirname(__file__), '..', 'hooks', 'validate-output.sh')

def run_hook(file_path: str, content: str) -> tuple:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    hook_input = json.dumps({"tool_input": {"file_path": file_path}})
    result = subprocess.run(['bash', HOOK], input=hook_input, capture_output=True, text=True)
    return result.returncode, result.stdout

class TestBridgePostValidation(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.output_dir = os.path.join(self.tmpdir, 'output', 'divrei-torah', 'bridge-posts')

    def test_bridge_post_passes_without_sources_section(self):
        path = os.path.join(self.output_dir, '2026-05-28-linters.md')
        content = '---\nformat: bridge-post\n---\n# יהדוטכנולוגיה #5\nלינט של העליון\n\"תכלת\"(סוטה י״ז א)\nתורה\n'
        code, stdout = run_hook(path, content)
        self.assertEqual(code, 0, f"Hook should pass for bridge-post, got: {stdout}")

    def test_dvar_torah_still_requires_sources_section(self):
        path = os.path.join(self.output_dir, '..', 'dvar-torah', '2026-05-28-test.md')
        content = '---\nformat: dvar-torah\n---\n# Test\nsome text with תורה\n'
        code, stdout = run_hook(path, content)
        self.assertEqual(code, 2, "Hook should block dvar-torah without sources section")

    def test_no_format_defaults_to_strict(self):
        path = os.path.join(self.output_dir, '..', 'posts', '2026-05-28-test.md')
        content = '---\ntopic: test\n---\n# Test\nsome text with תורה\n'
        code, stdout = run_hook(path, content)
        self.assertEqual(code, 2, "Hook should block files without format when missing sources")

if __name__ == '__main__':
    unittest.main()
