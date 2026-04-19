#!/usr/bin/env python3
"""Add ai-fatigue-quick-start.html to nav and footer on all pages with full nav."""
import os
import re

exclude = {'index-hn.html', 'hn-quick-start.html', 'hn-subscribe.html'}

# Pages that have the full multi-link header/footer (exclude HN-only stubs)
pages = [f for f in os.listdir('.') if f.endswith('.html') and f not in exclude]

added_nav = []
added_footer = []

for fname in pages:
    with open(fname, 'r') as f:
        content = f.read()

    # Skip pages that don't have the full nav (look for dropdown-menu)
    if 'dropdown-menu' not in content:
        continue

    # Add to nav if not already there
    if 'ai-fatigue-quick-start' not in content:
        # Add after the "Quick-Start" entry in a dropdown, or after index-hn.html link
        # Find a suitable dropdown section — try Stories first (junior/senior archetypes)
        # Pattern: add after a related entry in Stories dropdown
        patterns_to_try = [
            (r'(<li><a href="stories\.html">)', r'\1\n            <li><a href="ai-fatigue-quick-start.html">Quick-Start Guide</a></li>'),
            (r'(<li><a href="index\.html")', r'<li><a href="ai-fatigue-quick-start.html">Quick-Start Guide</a></li>\1'),
        ]
        inserted = False
        for pattern, replacement in patterns_to_try:
            new_content = re.sub(pattern, replacement, content, count=1)
            if new_content != content:
                content = new_content
                inserted = True
                added_nav.append(fname)
                break

        if not inserted:
            print(f"  [NAV] Could not insert in {fname}")

    # Add to footer if not already there
    if 'ai-fatigue-quick-start' not in content:
        # Add before sitemap.html link in footer
        new_content = re.sub(
            r'(<li><a href="sitemap\.html")',
            r'<li><a href="ai-fatigue-quick-start.html">Quick-Start Guide</a></li>\n      \1',
            content,
            count=1
        )
        if new_content != content:
            content = new_content
            added_footer.append(fname)
        # else: footer may not have sitemap link

    with open(fname, 'w') as f:
        f.write(content)

print(f"Nav updated: {len(added_nav)} pages")
for p in added_nav:
    print(f"  +NAV: {p}")
print(f"Footer updated: {len(added_footer)} pages")
for p in added_footer:
    print(f"  +FOOTER: {p}")
if not added_nav and not added_footer:
    print("No updates needed — ai-fatigue-quick-start.html already in nav/footer on all full-nav pages.")
