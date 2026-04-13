#!/usr/bin/env python3
"""Fix LCP by updating outdated woff2 font preloads on all HTML pages."""
import os
import re

BASE = "/Users/nightcoder/Desktop/TheClearing"

# Old (wrong) preloads to remove
OLD_INTER_V18 = "v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEBrLy9d1UZF5p7lk.woff2"
OLD_LORA_V36 = "v36/8IQJvFuJd87V_IYq_mvhDd-2XwWj2R38lLa4hZk.woff2"

# Correction: Preload should match what Google Fonts actually serves (v20 woff2)
# But actually, better approach: remove wrong preloads, let CSS handle it
# OR preload the CORRECT v20 URLs

CORRECT_INTER_V20 = "v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7W0Q5nw.woff2"
CORRECT_LORA_V37_1 = "v37/0QIvMX1D_JOuMwr7I_FMl_E.woff2"
CORRECT_LORA_V37_2 = "v37/0QI8MX1D_JOuMw_hLdO6T2wV9KnW-MoFoq92nPWa3Zw.woff2"

html_files = [f for f in os.listdir(BASE) if f.endswith(".html")]
fixed = 0

for fname in html_files:
    path = os.path.join(BASE, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    changed = False
    
    # Check if this file has the old preloads
    if OLD_INTER_V18 in content or OLD_LORA_V36 in content:
        # Remove the old wrong preloads
        # Pattern: <link rel="preload" as="font" ... v18/v36 URL />
        content = re.sub(
            r'\s*<link[^>]+rel="preload"[^>]+as="font"[^>]+' + re.escape(OLD_INTER_V18) + r'[^>]*/?>\n?',
            '',
            content
        )
        content = re.sub(
            r'\s*<link[^>]+rel="preload"[^>]+as="font"[^>]+' + re.escape(OLD_LORA_V36) + r'[^>]*/?>\n?',
            '',
            content
        )
        changed = True
    
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        fixed += 1
        print(f"Fixed: {fname}")

print(f"\nTotal fixed: {fixed}/{len(html_files)}")