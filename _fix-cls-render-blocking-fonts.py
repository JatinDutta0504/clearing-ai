#!/usr/bin/env python3
"""
Fix render-blocking Google Fonts across all HTML pages.
Convert: <link rel="stylesheet" href="https://fonts.googleapis.com/css2?...">
To:     <link rel="stylesheet" href="https://fonts.googleapis.com/css2?..." media="print" onload="this.media='all'" />
Plus add preconnect and noscript fallback.
"""
import os
import re
import shutil
import datetime

TARGET_DIR = '.'
BACKUP_DIR = '_cls-fix-backup'
os.makedirs(BACKUP_DIR, exist_ok=True)

# Regex to find render-blocking Google Fonts <link> tags
# Pattern: <link rel="stylesheet" href="https://fonts.googleapis.com/css2...">
GFONTS_BLOCKING = re.compile(
    r'<link\s+rel="stylesheet"\s+href="https://fonts\.googleapis\.com/css2[^"]+"\s*/?>(?:\s*<noscript>.*?</noscript>)?',
    re.DOTALL
)

# Regex for preconnect
PRECONNECT = re.compile(r'<link\s+rel="preconnect"\s+href="https://fonts\.googleapis\.com"\s*/>')

count_pages = 0
count_fixes = 0

for fname in sorted(os.listdir(TARGET_DIR)):
    if not fname.endswith('.html') or fname.startswith('_'):
        continue
    if fname.startswith('cls-fix') or fname == 'fix-render-blocking-fonts.py':
        continue
    
    fpath = os.path.join(TARGET_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all render-blocking Google Fonts links
    matches = GFONTS_BLOCKING.findall(content)
    if not matches:
        continue
    
    # Backup
    shutil.copy2(fpath, os.path.join(BACKUP_DIR, fname))
    count_pages += 1
    
    for m in matches:
        # Check if already non-blocking
        if 'media="print"' in m or "media='print'" in m:
            continue
        
        count_fixes += 1
        # Convert to non-blocking pattern
        # Extract href
        href_match = re.search(r'href="(https://fonts\.googleapis\.com/css2[^"]+)"', m)
        if not href_match:
            continue
        href = href_match.group(1)
        
        # Check for noscript fallback
        has_noscript = '<noscript>' in m
        
        # Build new link
        new_link = f'<link rel="stylesheet" href="{href}" media="print" onload="this.media=\'all\'" />'
        
        if has_noscript:
            # Extract noscript content and append
            ns_match = re.search(r'<noscript>.*?</noscript>', m, re.DOTALL)
            noscript = ns_match.group(0) if ns_match else ''
            new_link += f'\n  {noscript}'
        
        content = content.replace(m, new_link)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed {count_fixes} render-blocking Google Fonts links across {count_pages} pages.")
print(f"Backup saved in ./{BACKUP_DIR}/")
print("\nTop fixed pages:")
import glob
fixed = []
for fname in sorted(os.listdir(BACKUP_DIR)):
    fixed.append(fname)
for f in fixed[:10]:
    print(f"  {f}")
if len(fixed) > 10:
    print(f"  ...+{len(fixed)-10} more")