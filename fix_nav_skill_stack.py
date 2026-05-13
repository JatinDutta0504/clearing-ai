#!/usr/bin/env python3
"""Add the-ai-skill-stack.html to Understand nav dropdown in all pages that have cognitive-load but not skill-stack."""

import os
import re

SITE_DIR = "/Users/nightcoder/Desktop/TheClearing"
NEW_LINK = '            <li><a href="the-ai-skill-stack.html">AI Skill Stack</a></li>'
TARGET_FILE = "the-ai-skill-stack.html"
ANCHOR = "cognitive-load.html"

count = 0
updated = []

for filename in os.listdir(SITE_DIR):
    if not filename.endswith(".html"):
        continue
    filepath = os.path.join(SITE_DIR, filename)
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Skip if already has the link
    if TARGET_FILE in content:
        continue
    
    # Find the cognitive-load.html line
    lines = content.split("\n")
    anchor_idx = None
    for i, line in enumerate(lines):
        if ANCHOR in line and "<li>" in line:
            anchor_idx = i
            break
    
    if anchor_idx is None:
        continue
    
    # Insert right after the anchor line, preserving same indentation as the anchor line
    indent_match = re.match(r"(\s*)", lines[anchor_idx])
    indent = indent_match.group(1) if indent_match else "            "
    new_item = f'{indent}<li><a href="{TARGET_FILE}">AI Skill Stack</a></li>'
    new_lines = lines[:anchor_idx+1] + [new_item] + lines[anchor_idx+1:]
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
    
    count += 1
    updated.append(filename)
    print(f"Updated: {filename} (inserted after line {anchor_idx+1})")

print(f"\nTotal files updated: {count}")
