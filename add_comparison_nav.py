#!/usr/bin/env python3
"""
Add coding-ai-tools-comparison.html to nav after ai-tool-overload.html.
Minimal surgical fix — only touches the nav section.
"""
import re, os

SITE = "/Users/nightcoder/Desktop/TheClearing"
TARGET = "coding-ai-tools-comparison.html"
AFTER = "ai-tool-overload.html"

html_files = [f for f in os.listdir(SITE) if f.endswith(".html") and f != TARGET]

# Pattern: find the nav <li> for ai-tool-overload and add our page after
# Match: <li><a href="ai-tool-overload.html">...</a></li>
# Then insert new <li>after it

before = f'<li><a href="{AFTER}"'
after_insert = f'</li>\\n            <li><a href="{TARGET}">Coding Tools Comparison</a></li>'

updated = 0
skipped = 0
errors = []

for fname in html_files:
    fpath = os.path.join(SITE, fname)
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        errors.append(f"{fname}: {e}")
        continue

    if TARGET in content:  # already integrated
        skipped += 1
        continue

    if AFTER not in content:  # doesn't have the reference page
        skipped += 1
        continue

    original = content

    # Find the nav <li> block for ai-tool-overload and insert after its </li>
    # Use a pattern that matches the specific nav entry
    pattern = r'(<li><a href="' + re.escape(AFTER) + r'"[^<]*</a></li>)'
    match = re.search(pattern, content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + '\n            <li><a href="' + TARGET + '">Coding Tools Comparison</a></li>' + content[insert_pos:]

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1
    else:
        skipped += 1

print(f"Updated: {updated} | Skipped: {skipped} | Errors: {len(errors)}")
if errors:
    for e in errors[:5]:
        print(" ", e)
