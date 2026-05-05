#!/usr/bin/env python3
"""Fix CSS/JS asset paths for minified files across all HTML pages."""
import os, re

BASE = '/Users/nightcoder/Desktop/TheClearing'

replacements = [
    # CSS
    (r'href="style\.css"', 'href="css/style.min.css"'),
    (r'href="css/style\.css"', 'href="css/style.min.css"'),
    (r'href="css/style\.min\.css"', 'href="css/style.min.css"'),
    # JS
    (r'src="main\.js"', 'src="js/main.min.js"'),
    (r'src="js/main\.js"', 'src="js/main.min.js"'),
    (r'src="js/main\.min\.js"', 'src="js/main.min.js"'),
    # Versioned (strip v= query params from old files)
    (r'href="style\.css\?v=[^"]*"', 'href="css/style.min.css"'),
    (r'src="main\.js\?v=[^"]*"', 'src="js/main.min.js"'),
    (r'src="js/main\.js\?v=[^"]*"', 'src="js/main.min.js"'),
]

html_files = [f for f in os.listdir(BASE) if f.endswith('.html')]
changed = 0

for fname in html_files:
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        changed += 1
        print(f"  Fixed: {fname}")

print(f"\nDone — {changed}/{len(html_files)} files updated.")