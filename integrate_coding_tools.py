#!/usr/bin/env python3
"""Integrate coding-ai-tools-comparison.html into nav and footer of all HTML pages."""
import os
import re

SITE = "/Users/nightcoder/Desktop/TheClearing"
TARGET = "coding-ai-tools-comparison.html"
INSERT_AFTER = "ai-tool-overload.html"
FOOTER_AFTER = "ai-tool-overload"

files_updated = 0
errors = []

html_files = [f for f in os.listdir(SITE) if f.endswith(".html") and f != TARGET]

for filename in html_files:
    filepath = os.path.join(SITE, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        errors.append(f"{filename}: read error {e}")
        continue

    original = content

    # Skip if already has this link
    if TARGET in content and f'href="{TARGET}"' in content:
        continue

    # Add to nav dropdown after ai-tool-overload
    if INSERT_AFTER in content:
        # Nav: find the li containing ai-tool-overload and add our page after it
        pattern = r'(<li><a href="' + re.escape(INSERT_AFTER) + r'"[^>]*>.*?</a>)'
        replacement = r'\1\n        <li><a href="' + TARGET + r'">Compare Tools</a></li>'
        content, n = re.subn(pattern, replacement, content, flags=re.DOTALL)
        if n == 0:
            # Try simpler pattern
            pattern2 = r'(href="' + re.escape(INSERT_AFTER) + r'")'
            if TARGET not in content and pattern2.search(content):
                pass

    # Add to footer after ai-tool-overload
    if FOOTER_AFTER in content and f'href="{TARGET}"' not in content:
        footer_pattern = r'(<a href="' + FOOTER_AFTER + r'\.html"[^>]*>.*?</a>)'
        footer_repl = r'\1</li>\n    <li><a href="' + TARGET + r'">Compare AI Tools</a></li>'
        content, n2 = re.subn(footer_pattern, footer_repl, content, flags=re.DOTALL)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        files_updated += 1

print(f"Updated {files_updated} files")
if errors:
    print("Errors:", errors[:5])
