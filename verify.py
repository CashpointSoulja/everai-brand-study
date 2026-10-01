from pathlib import Path
from html.parser import HTMLParser
import hashlib
import json
import re

root = Path(__file__).resolve().parent

class ReferenceCheck(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('src', 'href'):
            value = attrs.get(key, '')
            if value and not value.startswith(('https:', '#')):
                assert (root / value).is_file(), value
        if tag == 'img':
            assert attrs.get('alt'), 'Missing image description'

ReferenceCheck().feed((root / 'visual-guide.html').read_text())
for asset in json.loads((root / 'assets/sources.json').read_text())['assets']:
    data = (root / asset['file']).read_bytes()
    assert len(data) == asset['bytes'], asset['file']
    assert hashlib.sha256(data).hexdigest() == asset['sha256'], asset['file']
for name in ('design.md', 'visual-guide.html'):
    text = (root / name).read_text()
    for fragment in re.findall(r'href="#([^"]+)"', text):
        assert f'id="{fragment}"' in text, fragment
print('Local references, image descriptions, section links and original asset checksums pass.')
