#!/usr/bin/env python3
"""Add context-switching-ai.html to Understand dropdown on all HTML pages."""
import os
import re

TARGET = "context-switching-ai.html"
NAV_LINK = f'            <li><a href="{TARGET}">Context Switching</a></li>'
SITEMAP_LINK = f"https://clearing-ai.com/{TARGET}"

pages_updated = 0
errors = []

# Pages that already have context-switching-ai in nav
already_have = set()

# Pages to skip (newsletter issues, etc.)
skip_patterns = [
    "newsletter-issues/",
    "_",
    "backup",
    "test",
    "404",
    "badge",
]

# Where to insert in Understand dropdown — after attention-residue.html
insert_after = '<li><a href="attention-residue.html">Attention Residue</a></li>'

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for fname in html_files:
    skip = any(p in fname for p in skip_patterns)
    if skip:
        continue

    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        errors.append(f"{fname}: {e}")
        continue

    # Check if already present
    if TARGET in content:
        already_have.add(fname)
        continue

    # Check if this page has Understand dropdown with attention-residue
    if 'attention-residue.html' not in content:
        continue

    # Insert after attention-residue in the Understand dropdown
    new_content = content.replace(
        insert_after,
        insert_after + '\n' + NAV_LINK
    )

    if new_content == content:
        # Try alternate insertion point — after decision-fatigue-ai
        insert_after2 = '<li><a href="decision-fatigue-ai.html">Decision Fatigue</a></li>'
        new_content = content.replace(
            insert_after2,
            insert_after2 + '\n' + NAV_LINK
        )

    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        pages_updated += 1
        print(f"Updated: {fname}")
    else:
        errors.append(f"{fname}: could not find insertion point")

print(f"\nTotal pages updated: {pages_updated}")
print(f"Already have link: {len(already_have)}")
if errors:
    print(f"Errors: {errors[:10]}")
