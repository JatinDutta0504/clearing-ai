#!/usr/bin/env python3
"""Add ai-code-review.html to footer of all HTML pages that already have the nav entry."""
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

    # Only process files that have nav entry for TARGET
    nav_count = content.count(f'href="{TARGET}"')
    if nav_count == 0:
        skipped += 1
        continue
    
    # If TARGET appears 2+ times, it likely has both nav and footer
    if nav_count >= 2:
        skipped += 1
        continue

    if AFTER not in content:
        skipped += 1
        continue

    original = content

    # Find footer section - look for <footer tag
    footer_start = content.find('<footer')
    if footer_start == -1:
        skipped += 1
        continue
    
    footer_content = content[footer_start:]
    
    # Find the AFTER link in footer
    footer_pattern = r'(<li><a href="' + re.escape(AFTER) + r'"[^<]*</a></li>)'
    match = re.search(footer_pattern, footer_content)
    if match:
        insert_pos = footer_start + match.end()
        content = content[:insert_pos] + '\n      <li><a href="' + TARGET + '">AI Code Review</a></li>' + content[insert_pos:]

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
