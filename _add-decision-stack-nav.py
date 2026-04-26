#!/usr/bin/env python3
"""Add ai-decision-stack.html to nav on all HTML pages."""
import os
import re

TARGET = "ai-decision-stack.html"
NAV_LINK = f'            <li><a href="{TARGET}">AI Decision Stack</a></li>'

pages_updated = 0
already_have = 0
skipped = 0

skip_patterns = [
    "newsletter-issues/",
    "_",
    "backup",
    "test",
    "404",
    "badge",
    "dispatch-",
    "og-",
]

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Insert after team-guide.html (engineering manager content)
insert_after = '<li><a href="team-guide.html">For Managers</a></li>'

for fname in html_files:
    skip = any(p in fname for p in skip_patterns)
    if skip:
        skipped += 1
        continue

    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {fname}: {e}")
        continue

    if TARGET in content:
        already_have += 1
        continue

    if 'team-guide.html' not in content:
        # Try alternate insertion points
        if 'corporate-ai-wellness.html' in content:
            insert_after = '<li><a href="corporate-ai-wellness.html">Corporate Wellness</a></li>'
        elif 'hiring.html' in content:
            insert_after = '<li><a href="hiring.html">Hiring &amp; Retention</a></li>'
        else:
            continue

    new_content = content.replace(
        insert_after,
        insert_after + '\n' + NAV_LINK
    )

    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        pages_updated += 1
        print(f"Updated: {fname}")
    else:
        print(f"Could not insert in: {fname}")

print(f"\nTotal pages updated: {pages_updated}")
print(f"Already have link: {already_have}")
print(f"Skipped: {skipped}")
