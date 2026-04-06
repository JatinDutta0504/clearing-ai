#!/usr/bin/env python3
"""Add ai-code-review.html to nav of all HTML pages, after ai-learning-burnout.html."""
import re, os

SITE = "/Users/nightcoder/Desktop/TheClearing"
TARGET = "ai-code-review.html"
AFTER = "ai-learning-burnout.html"

html_files = [f for f in os.listdir(SITE) if f.endswith(".html") and f != TARGET]

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

    if TARGET in content:
        skipped += 1
        continue

    if AFTER not in content:
        skipped += 1
        continue

    original = content

    # Find the first nav <li> block for ai-learning-burnout and insert after its </li>
    # Nav links are indented with spaces inside <ul class="nav-links">
    # We want the first occurrence (nav section)
    pattern = r'(<li><a href="' + re.escape(AFTER) + r'"[^<]*</a></li>)'
    match = re.search(pattern, content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + '\n            <li><a href="' + TARGET + '">AI Code Review</a></li>' + content[insert_pos:]

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
