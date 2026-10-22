"""Stable release selection and update safety, without network requests."""
import importlib.util
import gzip
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, patch

SPEC = importlib.util.spec_from_file_location(
    'technology_audit', Path(__file__).resolve().parents[1] / 'audit-technology-versions.py')
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class TechnologyVersionsTests(unittest.TestCase):
    def test_gzip_response_is_decoded(self):
        response = MagicMock()
        response.headers = {'Content-Encoding': 'gzip'}
        response.read.return_value = gzip.compress(b'<a>Python 3.14.7</a>')
        response.__enter__.return_value = response
        with patch.object(AUDIT, 'urlopen', return_value=response):
            self.assertEqual(AUDIT.latest('python', 'https://www.python.org/downloads/'), '3.14.7')

    def test_github_token_is_scoped_to_api(self):
        response = MagicMock()
        response.headers = {}
        response.read.return_value = b'{}'
        response.__enter__.return_value = response
        with patch.dict(AUDIT.os.environ, {'GITHUB_TOKEN': 'test-token'}), patch.object(AUDIT, 'urlopen', return_value=response) as opened:
            AUDIT.get_text('https://registry.npmjs.org/mermaid/latest')
            self.assertIsNone(opened.call_args.args[0].get_header('Authorization'))
            AUDIT.get_text('https://api.github.com/repos/actions/checkout/releases/latest')
            self.assertEqual(opened.call_args.args[0].get_header('Authorization'), 'Bearer test-token')

    def test_empty_or_changed_metadata_is_incomplete(self):
        for kind, content in [('python', '<a>Python 3.15.0rc2</a>'), ('pypi', '{"releases": {}}'), ('sqlite', '<html>changed</html>'), ('npm', '{"version":"12.0.0-rc.1"}')]:
            with self.subTest(kind=kind), patch.object(AUDIT, 'get_text', return_value=content):
                row = AUDIT.check(dict(kind=kind, source='unused', current='1.0.0', policy='pin'))
                self.assertEqual(row['status'], 'unknown')
                self.assertEqual(AUDIT.exit_code([row]), 2)

    def test_mermaid_uses_only_stable_project_release_tags(self):
        payload = [
            {'tag_name': 'mermaid@12.2.0', 'draft': False, 'prerelease': False},
            {'tag_name': 'mermaid@12.3.0-rc.1', 'draft': False, 'prerelease': True},
            {'tag_name': 'mermaid@13.0.0', 'draft': True, 'prerelease': False},
            {'tag_name': 'mermaid-cli@12.9.0', 'draft': False, 'prerelease': False},
            {'tag_name': 'mermaid@12.1.0', 'draft': False, 'prerelease': False},
        ]
        with patch.object(AUDIT, 'get_text', return_value=json.dumps(payload)):
            self.assertEqual(AUDIT.latest('github-mermaid', AUDIT.MERMAID_URL), '12.2.0')
        for body in ('{}', '[]', '[{"tag_name":"mermaid@12.3.0-rc.1"}]'):
            with self.subTest(body=body), patch.object(AUDIT, 'get_text', return_value=body):
                row = AUDIT.check(dict(kind='github-mermaid', source=AUDIT.MERMAID_URL,
                                       current='12.2.0', policy='pin'))
                self.assertEqual(row['status'], 'unknown')
                self.assertEqual(AUDIT.exit_code([row]), 2)

    def test_numeric_comparison_detects_patch_minor_major(self):
        for candidate in ['11.17.3', '11.18.0', '12.0.0']:
            self.assertEqual(AUDIT.compare('11.17.2', candidate, 'pin'), 'update available')
        self.assertEqual(AUDIT.compare('11.9.0', '11.17.2', 'pin'), 'update available')
        self.assertEqual(AUDIT.compare('12.0.0', '11.17.2', 'pin'), 'source behind')

    def test_prerelease_and_tag_rejected(self):
        for value in ['12.0.0-rc.1', '3.14.0rc1', 'latest', '11']:
            with self.assertRaises(ValueError):
                AUDIT.version(value)

    def test_pypi_ignores_yanked_and_prerelease(self):
        payload = {'releases': {'1.0.0': [{'yanked': False}],
                                '2.0.0': [{'yanked': True}],
                                '3.0.0rc1': [{'yanked': False}], '4.0.0': []}}
        with patch.object(AUDIT, 'get_text', return_value=json.dumps(payload)):
            self.assertEqual(AUDIT.latest('pypi', 'unused'), '1.0.0')

    def test_node_current_and_lts_are_separate(self):
        payload = [{'version': 'v26.9.0', 'lts': False},
                   {'version': 'v24.21.0', 'lts': 'Krypton'}]
        with patch.object(AUDIT, 'get_text', return_value=json.dumps(payload)):
            self.assertEqual(AUDIT.latest('node', 'unused'), '26.9.0')
            self.assertEqual(AUDIT.latest('node-lts', 'unused'), '24.21.0')

    def test_installed_node_uses_its_actual_release_channel(self):
        payload = [{"version": "v26.9.0", "lts": False},
                   {"version": "v25.0.0", "lts": False},
                   {"version": "v24.21.0", "lts": "Krypton"},
                   {"version": "v22.20.0", "lts": "Jod"}]
        for installed, expected_latest, expected_name, status in [
            ("26.9.0", "26.9.0", "Node.js non-LTS (this host)", "current"),
            ("25.0.0", "26.9.0", "Node.js non-LTS (this host)", "update available"),
            ("24.21.0", "24.21.0", "Node.js LTS (this host)", "current"),
            ("22.20.0", "24.21.0", "Node.js LTS (this host)", "update available"),
        ]:
            with self.subTest(installed=installed), patch.object(AUDIT, "get_text", return_value=json.dumps(payload)):
                row = AUDIT.check(dict(kind="node-host", source="unused", current=installed, policy="host"))
                self.assertEqual((row["latest"], row["name"], row["status"]), (expected_latest, expected_name, status))
                self.assertEqual(AUDIT.exit_code([row]), 0)
                self.assertEqual(AUDIT.exit_code([row], True), int(status == "update available"))
        with patch.object(AUDIT, "get_text", return_value="[]"):
            row = AUDIT.check(dict(kind="node-host", source="unused", current="26.9.0", policy="host"))
            self.assertEqual(AUDIT.exit_code([row]), 2)

    def test_python_excludes_prerelease_and_compares_numerically(self):
        html = '<a>Python 3.14.7</a><a>Python 3.15.0rc2</a><a>Python 3.9.25</a>'
        with patch.object(AUDIT, 'get_text', return_value=html):
            self.assertEqual(AUDIT.latest('python', 'unused'), '3.14.7')

    def test_moving_action_major_is_not_an_exact_pin(self):
        self.assertEqual(AUDIT.compare('v7', '7.0.1', 'action'), 'tracks major')
        self.assertEqual(AUDIT.compare('v7', '8.0.0', 'action'), 'update available')

    def test_network_failure_is_not_current(self):
        with patch.object(AUDIT, 'get_text', side_effect=TimeoutError('unavailable')):
            result = AUDIT.check(dict(kind='npm', source='unused', current='1.0.0', policy='pin'))
        self.assertEqual(result['status'], 'unknown')
        self.assertEqual(AUDIT.exit_code([result]), 2)

    def test_host_drift_is_advisory_by_default(self):
        rows = [dict(status='update available', policy='host')]
        self.assertEqual(AUDIT.exit_code(rows), 0)
        self.assertEqual(AUDIT.exit_code(rows, True), 1)
        self.assertEqual(AUDIT.exit_code([dict(status='update available', policy='pin')]), 1)

    def test_candidate_preserves_bytes_and_requires_major_opt_in(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'web-templates/index.html'
            path.parent.mkdir()
            original = b'<!-- preserve -->\r\nhttps://cdn.jsdelivr.net/npm/mermaid@11.17.2/dist/mermaid.esm.min.mjs\r\n'
            path.write_bytes(original)
            with self.assertRaises(ValueError):
                AUDIT.prepare_mermaid(root, '12.0.0')
            self.assertEqual(path.read_bytes(), original)
            self.assertTrue(AUDIT.prepare_mermaid(root, '11.17.3'))
            self.assertEqual(path.read_bytes(), original.replace(b'11.17.2', b'11.17.3'))
            self.assertFalse(AUDIT.prepare_mermaid(root, '11.17.2'))
            self.assertTrue(AUDIT.prepare_mermaid(root, '12.0.0', True))

    def test_duplicate_or_missing_mermaid_pin_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'web-templates/index.html'
            path.parent.mkdir()
            for content in ['', ('https://cdn.jsdelivr.net/npm/mermaid@11.0.0/dist/mermaid.esm.min.mjs\n' * 2)]:
                path.write_text(content, encoding='utf-8')
                with self.assertRaises(ValueError):
                    AUDIT.prepare_mermaid(root, '11.1.0')
                self.assertEqual(path.read_text(encoding='utf-8'), content)


if __name__ == '__main__':
    unittest.main()
