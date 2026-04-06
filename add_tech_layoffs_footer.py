#!/usr/bin/env python3
"""Add tech-layoffs-ai-era.html to footer of all HTML pages, after developer-burnout-2025.html."""
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

    # Skip if already in footer
    if content.count(TARGET) >= 2:  # already has nav + footer
        skipped += 1
        continue

    if AFTER not in content:
        skipped += 1
        continue

    original = content

    # Find footer section with developer-burnout-2025 and insert after
    # Footer pattern: <li><a href="developer-burnout-2025.html">...
    pattern = r'(<li><a href="' + re.escape(AFTER) + r'"[^<]*</a></li>)'
    # We want to add to footer specifically - find second occurrence (footer)
    matches = list(re.finditer(pattern, content))
    if len(matches) >= 2:
        # Add after second occurrence (footer)
        match = matches[1]
        insert_pos = match.end()
        content = content[:insert_pos] + '\n      <li><a href="' + TARGET + '">Tech Layoffs &amp; AI</a></li>' + content[insert_pos:]
    elif len(matches) == 1:
        # Only one occurrence - might be in footer only or nav+footer same element
        # Try to find footer section by looking for <footer
        footer_match = re.search(r'<footer', content)
        after_match = re.search(pattern, content)
        if footer_match and after_match:
            # Insert after the footer occurrence
            insert_pos = after_match.end()
            content = content[:insert_pos] + '\n      <li><a href="' + TARGET + '">Tech Layoffs &amp; AI</a></li>' + content[insert_pos:]

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
