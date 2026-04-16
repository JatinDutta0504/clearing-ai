#!/usr/bin/env python3
"""Hour 358: Fix broken woff2 font preloads in ai-learning-burnout.html
   - Inter woff2 URL was 404 (wrong hash) -> replace with correct URL
   - JetBrains Mono woff2 URL 404 -> remove (not available in woff2)
   Also scan all 129 pages for any other font 404s
"""

import os
import re

BASE = "/Users/nightcoder/Desktop/TheClearing"

# Correct Inter woff2 URL (verified 200 OK)
CORRECT_INTER_WOFF2 = "https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7W0Q5nw.woff2"

# Broken URLs (404)
BROKEN_INTER = "UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7"
BROKEN_JETBRAINS = "jfR2FeNeShRy0hXVq1_7aA.woff2"

def fix_ai_learning_burnout():
    filepath = os.path.join(BASE, "ai-learning-burnout.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # Fix broken Inter woff2 URL
    content = content.replace(
        "https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7.woff2",
        CORRECT_INTER_WOFF2
    )
    
    # Remove JetBrains Mono woff2 preload (404s - JetBrains Mono no longer available as woff2)
    # Replace the JetBrains Mono preload line with nothing
    jb_pattern = r'\s*<link rel="preload" as="font" type="font/woff2" crossorigin href="https://fonts\.gstatic\.com/s/jetbrains-mono/v20/jfR2FeNeShRy0hXVq1_7aA\.woff2" />\n?'
    content = re.sub(jb_pattern, '\n', content)
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Fixed: {filepath}")
        return True
    else:
        print(f"⚠️  No changes: {filepath}")
        return False

def scan_all_pages_for_broken_fonts():
    """Scan all HTML files for any other broken font preloads"""
    print("\n🔍 Scanning all pages for broken font preloads...")
    
    broken_pages = []
    all_preload_files = []
    
    for filename in os.listdir(BASE):
        if not filename.endswith(".html"):
            continue
        filepath = os.path.join(BASE, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Find all font preloads
        preload_pattern = r'<link rel="preload" as="font"[^>]+href="(https://fonts\.gstatic\.com[^"]+)"'
        matches = re.findall(preload_pattern, content)
        
        for url in matches:
            if "jetbrains" in url.lower():
                print(f"  ⚠️  {filename}: JetBrains Mono preload: {url}")
                broken_pages.append(filename)
            elif "UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7" in url:
                print(f"  ❌ {filename}: Broken Inter URL: {url}")
                broken_pages.append(filename)
    
    if not broken_pages:
        print("  ✅ No other broken font preloads found")
    return list(set(broken_pages))

if __name__ == "__main__":
    fixed = fix_ai_learning_burnout()
    broken = scan_all_pages_for_broken_fonts()
    print(f"\n📊 Summary: Fixed={fixed}, Other broken pages={len(broken)}")
