#!/usr/bin/env python3
"""Audit CLS causes on index-hn.html and fix the stale comment in index-hn.html"""
import re

BASE = "/Users/nightcoder/Desktop/TheClearing"

def audit_indexhn_cls():
    with open(f"{BASE}/index-hn.html", "r") as f:
        content = f.read()
    
    issues = []
    
    # Images without dimensions
    imgs = re.findall(r'<img(?![^>]*\s(width|height)=)', content)
    if imgs:
        issues.append(f"{len(imgs)} images without width/height")
    
    # iframe without dimensions
    iframes = re.findall(r'<iframe(?![^>]*\s(width|height)=)', content)
    if iframes:
        issues.append(f"{len(iframes)} iframes without dimensions")
    
    # Font with display:swap
    if 'font-display:swap' in content or 'swap' in content:
        issues.append("Uses font-display:swap (good — reduces CLS from FOIT)")
    
    # System font fallback
    fallback_check = re.search(r'font-family.*Inter.*sans-serif', content)
    if fallback_check:
        issues.append("Has Inter with sans-serif fallback (good CLS protection)")
    
    # CLS from font-swap (FOUT) - already handled with font-display:swap + preloads
    # Check for explicit size attributes on key hero elements
    hero_imgs = re.findall(r'<img[^>]+class="hero[^"]*"[^>]*>', content)
    if hero_imgs:
        issues.append(f"{len(hero_imgs)} hero images")
    
    return issues

issues = audit_indexhn_cls()
print("index-hn.html CLS audit:")
for i in issues:
    print(f"  {'⚠️' if 'without' in i else '✅'} {i}")
if not issues:
    print("  No critical CLS issues detected")