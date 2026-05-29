"""Tests for gemini_writer.py — prompt assembly, env vars, retry logic."""

import json
import os
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))


class TestLoadVoiceProfile(unittest.TestCase):
    def test_loads_yaml_file(self):
        from gemini_writer import load_voice_profile
        voice_dir = os.path.join(os.path.dirname(__file__), '..', 'voices')
        profile = load_voice_profile(os.path.join(voice_dir, 'default.yaml'))
        self.assertEqual(profile['name'], 'default')
        self.assertEqual(profile['language'], 'he')

    def test_missing_file_raises(self):
        from gemini_writer import load_voice_profile
        with self.assertRaises(FileNotFoundError):
            load_voice_profile('/nonexistent/path.yaml')


class TestBuildSystemPrompt(unittest.TestCase):
    def test_includes_voice_register(self):
        from gemini_writer import build_system_prompt
        profile = {
            'name': 'test', 'register': 'casual-linkedin', 'language': 'he',
            'sentence_style': {'avg_length': 'short', 'structure': 'direct'},
            'paragraph_style': {'pattern': 'hook → bridge', 'max_paragraphs': 10},
            'tone': {'personal_anecdotes': True, 'humor': 'light',
                     'self_reference': 'frequent', 'community_address': 'direct'},
            'torah_integration': {'citation_style': 'inline-quoted',
                                  'citation_density': '1-2 per post',
                                  'preferred_thinkers': ['רמב״ם']},
        }
        template = "# [title]\n[content]"
        prompt = build_system_prompt(profile, template)
        self.assertIn('casual-linkedin', prompt)
        self.assertIn('רמב״ם', prompt)
        self.assertIn('hook → bridge', prompt)

    def test_includes_template(self):
        from gemini_writer import build_system_prompt
        profile = {'name': 'x', 'register': 'formal', 'language': 'he',
                   'sentence_style': {}, 'paragraph_style': {},
                   'tone': {}, 'torah_integration': {}}
        template = "## TEMPLATE_MARKER"
        prompt = build_system_prompt(profile, template)
        self.assertIn('TEMPLATE_MARKER', prompt)


class TestBuildUserPrompt(unittest.TestCase):
    def test_includes_research_bundle_fields(self):
        from gemini_writer import build_user_prompt
        bundle = {
            'domain_research': {'concept': 'linters', 'definition': 'static analysis'},
            'sources': [{'ref': 'Sotah 17a', 'quote': 'תכלת'}],
            'bridge_analysis': {'primary': 'linter == tzitzit'},
            'sign_off': 'שבת שלום',
        }
        prompt = build_user_prompt(bundle)
        self.assertIn('linters', prompt)
        self.assertIn('Sotah 17a', prompt)
        self.assertIn('linter == tzitzit', prompt)
        self.assertIn('שבת שלום', prompt)


class TestCallGeminiAPI(unittest.TestCase):
    @patch('gemini_writer.urllib.request.urlopen')
    def test_successful_call(self, mock_urlopen):
        from gemini_writer import call_gemini_api
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            'candidates': [{'content': {'parts': [{'text': '# Post content'}]}}]
        }).encode()
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response
        result = call_gemini_api('system prompt', 'user prompt',
                                 model='gemini-2.5-flash', api_key='test-key',
                                 temperature=0.8, max_tokens=2000)
        self.assertEqual(result, '# Post content')

    def test_missing_api_key_raises(self):
        from gemini_writer import call_gemini_api
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError):
                call_gemini_api('sys', 'usr', model='gemini-2.5-flash',
                                api_key=None, temperature=0.8, max_tokens=2000)

    @patch('gemini_writer.urllib.request.urlopen')
    def test_retry_on_429(self, mock_urlopen):
        from gemini_writer import call_gemini_api
        import urllib.error
        error_429 = urllib.error.HTTPError('url', 429, 'rate limited', {}, None)
        success_response = MagicMock()
        success_response.read.return_value = json.dumps({
            'candidates': [{'content': {'parts': [{'text': 'ok'}]}}]
        }).encode()
        success_response.__enter__ = lambda s: s
        success_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.side_effect = [error_429, success_response]
        result = call_gemini_api('sys', 'usr', model='gemini-2.5-flash',
                                 api_key='key', temperature=0.8, max_tokens=2000)
        self.assertEqual(result, 'ok')
        self.assertEqual(mock_urlopen.call_count, 2)


if __name__ == '__main__':
    unittest.main()
