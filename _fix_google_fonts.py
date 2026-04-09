#!/usr/bin/env python3
"""Fix Google Fonts loading across all pages - make it non-render-blocking."""
import os
import re

FONTS_PRECONNECT = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap" /></noscript>"""

# Pages that already have proper font loading (have preconnect)
already_fixed = set()
# Pages that use style.min.css (need fix via CSS)
uses_style_min = set()
# Pages that have Google Fonts direct link but missing preconnect
missing_preconnect = set()

html_dir = "/Users/nightcoder/Desktop/TheClearing"
fixed_count = 0

for fname in os.listdir(html_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(html_dir, fname)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    has_preconnect = 'preconnect' in content and 'fonts.googleapis' in content
    uses_style = 'style.min.css' in content or 'style.css' in content
    has_gfont_link = 'fonts.googleapis.com' in content

    if has_preconnect:
        already_fixed.add(fname)
    if uses_style:
        uses_style_min.add(fname)
    if has_gfont_link and not has_preconnect:
        missing_preconnect.add(fname)

print(f"Pages already fixed (preconnect + async): {len(already_fixed)}")
print(f"Pages using style.min.css (font via @import): {len(uses_style_min)}")
print(f"Pages with Google Fonts link but missing preconnect: {len(missing_preconnect)}")
print(f"\nMissing preconnect: {sorted(missing_preconnect)}")
