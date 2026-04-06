#!/usr/bin/env python3
"""Add tech-layoffs-ai-era.html to nav of all HTML pages, after developer-burnout-2025.html."""
import re, os

SITE = "/Users/nightcoder/Desktop/TheClearing"
TARGET = "tech-layoffs-ai-era.html"
AFTER = "developer-burnout-2025.html"

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

    # Find the nav <li> block for developer-burnout-2025 and insert our page after its </li>
    pattern = r'(<li><a href="' + re.escape(AFTER) + r'"[^<]*</a></li>)'
    match = re.search(pattern, content)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + '\n            <li><a href="' + TARGET + '">Tech Layoffs & AI</a></li>' + content[insert_pos:]

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
