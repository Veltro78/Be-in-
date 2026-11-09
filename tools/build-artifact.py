#!/usr/bin/env python3
"""Build the claude.ai Artifact version of the game from index.html.

The artifact host wraps the page in its own <html>/<head>/<body>, so we keep only the
marked head and body fragments, and load Three.js from jsDelivr instead of lib/.
Usage: python3 tools/build-artifact.py <output.html>
"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'index.html').read_text()
head = re.search(r'<!-- HEAD:START -->(.*?)<!-- HEAD:END -->', src, re.S).group(1)
body = re.search(r'<!-- BODY:START -->(.*?)<!-- BODY:END -->', src, re.S).group(1)
head = re.sub(r'<meta name="viewport"[^>]*>\n', '', head)
body = body.replace('<script src="lib/three.min.js"></script>',
                    '<script src="https://cdn.jsdelivr.net/npm/three@0.158.0/build/three.min.js"></script>')
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'artifact.html')
out.write_text(head.strip() + '\n' + body.strip() + '\n')
print('wrote', out, len(head) + len(body), 'bytes')
