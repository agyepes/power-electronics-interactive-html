# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Alejandro Gómez Yepes
# Full terms: collection/LICENSE-CODE.txt
"""Verify the exact released collection before publishing unchanged files."""
from pathlib import Path
import hashlib
from html.parser import HTMLParser
import json

root = Path(__file__).resolve().parent.parent / 'collection'
manifest = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8-sig'))
expected = manifest['package']['expected_filenames']
assert len(expected) == len(set(expected)) == manifest['package']['expected_file_count'] == 27
assert all(Path(name).name == name and '/' not in name and '\\' not in name for name in expected)
assert sorted(path.name for path in root.iterdir()) == sorted(expected), 'Unexpected or missing package entries'
assert all((root / name).is_file() and not (root / name).is_symlink() for name in expected)
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
covered = set()
for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    checksum, name = line.split('  ', 1)
    assert name in expected and name not in covered and name != 'SHA256SUMS.txt'
    assert len(checksum) == 64 and all(c in '0123456789abcdef' for c in checksum)
    assert sha(root / name) == checksum, 'Checksum mismatch: ' + name
    covered.add(name)
assert covered == set(expected) - {'SHA256SUMS.txt'}
payload = manifest['files']
assert {item['name'] for item in payload} == set(expected) - {'MANIFEST.json','SHA256SUMS.txt'}
assert len(payload) == 25
for item in payload:
    path = root / item['name']
    assert path.stat().st_size == item['bytes'] and sha(path) == item['sha256'], path.name
class Meta(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = {}
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name'):
            self.values.setdefault(attrs['name'], []).append(attrs.get('content'))
labs = [name for name in expected if name[:2].isdigit() and name.endswith('.html')]
assert len(labs) == manifest['package']['interactive_laboratory_count'] == 13
assert [name[:2] for name in labs] == [str(i).zfill(2) for i in range(1,14)]
for name in [*labs, 'index.html', 'DOCUMENTATION.html']:
    parser = Meta()
    parser.feed((root / name).read_text(encoding='utf-8'))
    assert parser.values.get('collection-version') == [manifest['collection']['version']], name
    assert parser.values.get('collection-title') == [manifest['collection']['title']], name
print('Verified 27 package files, all SHA-256 checksums, 13 laboratories and collection metadata.')
