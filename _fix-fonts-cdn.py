#!/usr/bin/env python3
"""Replace self-hosted fonts.css with Google Fonts CDN across all HTML pages."""

import os
import re

OLD_BLOCK = """  <link rel="preload" as="style" href="fonts/fonts.css" onload="this.onload=null;this.rel='stylesheet'" />
  <noscript><link rel="stylesheet" href="fonts/fonts.css" /></noscript>"""

NEW_BLOCK = """  <!-- Google Fonts CDN — replaces self-hosted 318KB fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Lora:ital,wght@0,400;1,400&display=swap" />"""

HTML_FILES = [f for f in os.listdir('.') if f.endswith('.html')]
updated = 0
errors = 0

for fname in HTML_FILES:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'fonts/fonts.css' in content and OLD_BLOCK in content:
            new_content = content.replace(OLD_BLOCK, NEW_BLOCK)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1
            print(f"  Updated: {fname}")
        elif 'fonts/fonts.css' in content:
            # Try alternate spacing
            alt_old = re.sub(r'fonts/fonts\.css', 'fonts/fonts.css', OLD_BLOCK)
            # Check if it has the preload but different spacing
            if 'fonts/fonts.css' in content:
                print(f"  SKIP (different format): {fname}")
    except Exception as e:
        print(f"  ERROR: {fname}: {e}")
        errors += 1

print(f"\nDone: {updated} files updated, {errors} errors")
