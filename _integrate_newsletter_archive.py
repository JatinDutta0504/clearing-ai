#!/usr/bin/env python3
"""Integrate newsletter-archive.html into nav + footer of all pages + sitemap.xml"""

import os
import re

SITE = "/Users/nightcoder/Desktop/TheClearing"
ARCHIVE_LINK = '<li><a href="newsletter-archive.html">Archive</a></li>'

def add_archive_to_file(filepath):
    with open(filepath) as f:
        content = f.read()
    
    if 'newsletter-archive.html' in content:
        return False  # already integrated
    
    # Add after newsletter-thank-you.html in nav (Newsletter dropdown)
    # Pattern: </li>\n<li><a href="newsletter-thank-you.html">
    # We add archive after thank-you
    old = '<li><a href="newsletter-thank-you.html">Thank You</a></li>'
    new = old + '\n            ' + ARCHIVE_LINK
    
    if old in content:
        content = content.replace(old, new)
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    
    # Fallback: add after newsletter.html link if no thank-you page
    old2 = '<li><a href="newsletter.html">Newsletter</a></li>'
    if old2 in content:
        new2 = old2 + '\n            ' + ARCHIVE_LINK
        content = content.replace(old2, new2)
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    
    return False

def update_sitemap():
    sitemap = os.path.join(SITE, "sitemap.xml")
    with open(sitemap) as f:
        content = f.read()
    
    if 'newsletter-archive.html' in content:
        return False
    
    # Add after newsletter-thank-you entry or before </urlset>
    archive_entry = '  <url>\n    <loc>https://clearing-ai.com/newsletter-archive.html</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n</urlset>'
    archive_line = '  <url>\n    <loc>https://clearing-ai.com/newsletter-archive.html</loc>'
    
    if archive_line in content:
        return False
    
    # Add before closing </urlset>
    content = content.replace('</urlset>', archive_entry)
    with open(sitemap, 'w') as f:
        f.write(content)
    return True

# Main
html_files = [f for f in os.listdir(SITE) if f.endswith('.html')]
updated = 0
for fname in html_files:
    fpath = os.path.join(SITE, fname)
    if add_archive_to_file(fpath):
        print(f"  Updated: {fname}")
        updated += 1

print(f"\nUpdated {updated} files")

sitemap_updated = update_sitemap()
if sitemap_updated:
    print("Updated sitemap.xml")
else:
    print("sitemap.xml already has newsletter-archive or no change needed")
