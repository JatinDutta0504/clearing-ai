#!/usr/bin/env python3
"""Add refer.html to nav and footer on all pages."""
import os, re

files_to_update = []
skip = ['404.html', 'index-hn.html', 'hn-visitor-guide.html', 'launch-command-center.html',
        'confirmed.html', 'refer.html']
for f in os.listdir('.'):
    if f.endswith('.html') and f not in skip:
        files_to_update.append(f)

added_nav = 0
added_footer = 0

for filename in sorted(files_to_update):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Skip if already has refer.html
    if 'refer.html' in content:
        print(f'SKIP {filename} — already has refer')
        continue

    # Add to nav — add before The Dispatch nav-cta
    # Pattern: <a href="newsletter.html" class="nav-cta">The Dispatch</a>
    new_nav_entry = '<a href="refer.html" class="nav-cta">📤 Share</a>\n        '
    m = re.search(r'(<a href="newsletter\.html" class="nav-cta">)', content)
    if m:
        content = content[:m.start()] + new_nav_entry + content[m.start():]
        changed = True
        added_nav += 1

    # Add to footer — before newsletter.html footer link
    new_footer_entry = '<a href="refer.html">Share</a></li>\n        '
    mf = re.search(r'(<a href="newsletter\.html">The Dispatch</a></li>)', content)
    if mf:
        content = content[:mf.start()] + new_footer_entry + content[mf.start():]
        changed = True
        added_footer += 1

    if changed:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'ADDED {filename}')

print(f'\nDone. Nav: {added_nav}, Footer: {added_footer}')
