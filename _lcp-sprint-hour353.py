#!/usr/bin/env python3
"""Phase 3 pre-HN LCP sprint: Fix comment-only woff2 blocks + audit CLS on index-hn"""

import os
import re

BASE = "/Users/nightcoder/Desktop/TheClearing"

# Pages with the woff2 comment but no actual preload tags (stale comment blocks)
STALE_COMMENT_FILES = [
    "index-hn.html",  # critical - HN landing page, LCP 3.1s mobile
    "ai-fatigue-checklist.html",
    "engineering-managers-ai-fatigue.html",
    "engineer-energy-management.html",
    "imposter-syndrome-ai.html",
    "engineer-case-studies.html",
]

# Real woff2 preload URLs for Inter (v20) and JetBrains Mono (v20)
# These match what Google Fonts actually serves
INTER_WOFF2 = "v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7W0Q5nw.woff2"
MONO_WOFF2 = "v20/IuliatdzThPrusWB9_V_FX1ebc5iU7Q.woff2"

# The non-render-blocking font pattern used on site
NONBLOCKING_FONT = """<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>"""

def fix_stale_woff2_comment(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # Remove the stale comment + add real woff2 preloads BEFORE the preconnect/font links
    stale_pattern = r"<!-- woff2 font preloads for LCP optimization -->\n?"
    
    real_preload_block = f"""<!-- woff2 font preloads for LCP optimization -->
  <link rel="preload" as="font" type="font/woff2" crossorigin
       href="https://fonts.gstatic.com/s/inter/{INTER_WOFF2}"
       data-fn="woff2-inter">
  <link rel="preload" as="font" type="font/woff2" crossorigin
       href="https://fonts.gstatic.com/s/jetbrains-mono/{MONO_WOFF2}"
       data-fn="woff2-mono">
"""
    
    content = re.sub(stale_pattern, real_preload_block, content)
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def fix_all_stale():
    fixed = []
    for fname in STALE_COMMENT_FILES:
        path = os.path.join(BASE, fname)
        if os.path.exists(path):
            ok = fix_stale_woff2_comment(path)
            if ok:
                fixed.append(fname)
    return fixed

def audit_cls_on_indexhn():
    """Quick audit: does index-hn.html have any CLS-causing patterns?"""
    path = os.path.join(BASE, "index-hn.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    issues = []
    
    # Check for images without dimensions
    img_without_dims = re.findall(r'<img(?![^>]*\s(width|height)=)[^>]*>', content)
    if img_without_dims:
        issues.append(f"{len(img_without_dims)} images without width/height attributes")
    
    # Check for font-size changes that could cause CLS
    if re.search(r'font-size:\s*clamp\s*\(', content):
        issues.append("Uses clamp() for font sizes (potential CLS if font loads late)")
    
    # Check if there's a fallback font stack
    if not re.search(r'font-family.*Inter.*sans-serif', content):
        issues.append("No Inter as primary font in CSS")
    
    return issues

if __name__ == "__main__":
    print("=== Phase 3 Pre-HN LCP Sprint ===\n")
    
    fixed = fix_all_stale()
    print(f"Fixed stale woff2 comments: {len(fixed)} pages")
    for f in fixed:
        print(f"  ✅ {f}")
    
    print()
    cls_issues = audit_cls_on_indexhn()
    if cls_issues:
        print("CLS audit on index-hn.html:")
        for i in cls_issues:
            print(f"  ⚠️  {i}")
    else:
        print("CLS audit: no issues found on index-hn.html")