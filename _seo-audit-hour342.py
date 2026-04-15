#!/usr/bin/env python3
"""
Phase 3 Technical SEO Audit — Hour 342
HN submission in ~52 hours. Pre-HN validation sweep.
"""
import os
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/Users/nightcoder/Desktop/TheClearing")
HTML_FILES = sorted([f for f in ROOT.glob("*.html")])
SITEMAP = ROOT / "sitemap.xml"

issues = []
warnings = []
pages_checked = 0

# --- 1. Basic HTML validity: check all pages have closing tags ---
print("=== 1. HTML STRUCTURE VALIDATION ===")
for f in HTML_FILES:
    content = f.read_text()
    pages_checked += 1
    
    # Basic structure checks
    if not content.strip().endswith('</html>'):
        issues.append(f"BROKEN_HTML: {f.name} — does not end with </html>")
    
    # Check for duplicate </head> or </body>
    heads = len(re.findall(r'</head>', content))
    bodies = len(re.findall(r'</body>', content))
    if heads > 1:
        issues.append(f"EXTRA_HEAD: {f.name} — {heads} </head> tags")
    if bodies > 1:
        issues.append(f"EXTRA_BODY: {f.name} — {bodies} </body> tags")
    
    # Check no double <html> tags at root level
    html_opens = re.findall(r'<html[^>]*>', content)
    if len(html_opens) > 1:
        issues.append(f"MULTIPLE_HTML: {f.name} — {len(html_opens)} <html> tags")

print(f"  Checked: {pages_checked} pages")
print(f"  Issues found: {len(issues)}")
for i in issues[:20]:
    print(f"    ❌ {i}")
if len(issues) > 20:
    print(f"    ... and {len(issues)-20} more")

# --- 2. Sitemap coverage check ---
print("\n=== 2. SITEMAP COVERAGE ===")
sitemap_content = SITEMAP.read_text()
sitemap_urls = re.findall(r'<loc>(.*?)</loc>', sitemap_content)
sitemap_count = len(sitemap_urls)
print(f"  Sitemap URLs: {sitemap_count}")
print(f"  HTML files at root: {len(HTML_FILES)}")

# Find HTML files NOT in sitemap
sitemap_base_urls = [u.rstrip('/').split('/')[-1] if 'clearing-ai' in u or 'localhost' in u else u for u in sitemap_urls]
missing_from_sitemap = []
for f in HTML_FILES:
    # Skip utility pages
    if f.name in ['404.html', 'sitemap.html', 'privacy.html']:
        continue
    # Check if this file is represented in sitemap
    found = False
    for url in sitemap_urls:
        if f.name in url or url.endswith(f.name):
            found = True
            break
    if not found:
        missing_from_sitemap.append(f.name)

if missing_from_sitemap:
    print(f"  ⚠️  Pages missing from sitemap: {missing_from_sitemap}")
    warnings.append(f"Missing from sitemap: {missing_from_sitemap}")
else:
    print(f"  ✅ All pages in sitemap")

# --- 3. Schema.org validation (spot check on newest pages) ---
print("\n=== 3. SCHEMA VALIDATION (newest pages) ===")
newest_pages = [
    'ai-architecture-fatigue.html',
    'ai-code-review-fatigue.html', 
    'ai-debugging-fatigue.html',
    'the-middleman-problem.html',
    'ai-fatigue-in-2026.html',
    'press-release-2026.html',
    'community-hub.html',
    'linkedin.html',
]
for fname in newest_pages:
    f = ROOT / fname
    if not f.exists():
        issues.append(f"MISSING_FILE: {fname}")
        continue
    content = f.read_text()
    
    # Check schema types present
    schemas = re.findall(r'"@type"\s*:\s*"([^"]+)"', content)
    has_article = '"Article"' in content or '"WebPage"' in content or '"HowTo"' in content
    has_breadcrumb = '"BreadcrumbList"' in content
    has_faq = '"FAQPage"' in content
    
    status = "✅" if has_article and has_breadcrumb else "⚠️"
    schema_str = ", ".join(schemas[:3])
    print(f"  {status} {fname}: Article={has_article}, Breadcrumb={has_breadcrumb}, FAQ={has_faq}")
    if not has_article:
        warnings.append(f"Schema: {fname} missing Article/WebPage/HowTo")

# --- 4. OG tags validation (spot check newest pages) ---
print("\n=== 4. OG/TWITTER META VALIDATION (newest pages) ===")
for fname in newest_pages:
    f = ROOT / fname
    if not f.exists():
        continue
    content = f.read_text()
    
    has_og_title = 'property="og:title"' in content or "property='og:title'" in content
    has_og_desc = 'property="og:description"' in content or "property='og:description'" in content
    has_og_image = 'property="og:image"' in content or "property='og:image'" in content
    has_twitter_card = 'name="twitter:card"' in content
    
    ok = has_og_title and has_og_desc and has_og_image and has_twitter_card
    status = "✅" if ok else "⚠️"
    print(f"  {status} {fname}: og:title={has_og_title}, og:desc={has_og_desc}, og:image={has_og_image}, twitter:card={has_twitter_card}")
    if not ok:
        warnings.append(f"OG/Twitter: {fname} missing meta tags")

# --- 5. Check index-hn.html is HN-ready ---
print("\n=== 5. HN PILLAR PAGE VALIDATION ===")
hn_page = ROOT / "index-hn.html"
if hn_page.exists():
    content = hn_page.read_text()
    has_hn_title = 'clearing-ai.com' in content.lower()
    has_faq_schema = '"FAQPage"' in content
    has_article = '"Article"' in content
    has_twitter = 'twitter:card' in content
    print(f"  index-hn.html: clearing-ai.com refs={has_hn_title}, FAQPage={has_faq_schema}, Article={has_article}, Twitter={has_twitter}")
    
    # Check it has links back to main site
    has_link_to_index = 'href="index.html"' in content or "href='index.html'" in content
    has_link_to_quiz = 'quiz' in content.lower() and ('href=' in content)
    print(f"    Links to index.html: {has_link_to_index}, Has quiz links: {has_link_to_quiz}")
else:
    print("  ❌ index-hn.html NOT FOUND")

# --- 6. Internal link health (spot check recently built pages) ---
print("\n=== 6. INTERNAL LINKING SPOT CHECK ===")
for fname in ['ai-architecture-fatigue.html', 'ai-debugging-fatigue.html', 'the-middleman-problem.html', 'community-hub.html']:
    f = ROOT / fname
    if not f.exists():
        continue
    content = f.read_text()
    
    # Count internal .html links
    internal_links = re.findall(r'href="([^"]+\.html)"', content)
    unique_internal = set(internal_links)
    
    # Check for strategic internal links
    has_recovery = any('recovery.html' in l for l in internal_links)
    has_research = any('research.html' in l for l in internal_links)
    has_glossary = any('glossary.html' in l for l in internal_links)
    
    print(f"  {fname}: {len(unique_internal)} unique internal links, recovery={has_recovery}, research={has_research}, glossary={has_glossary}")

# --- 7. Newsletter subscribe link validation ---
print("\n=== 7. NEWSLETTER CTA VALIDATION ===")
newsletter_pages = ['index.html', 'index-hn.html', 'newsletter.html', 'ai-fatigue-checklist.html', 'community-hub.html']
for fname in newsletter_pages:
    f = ROOT / fname
    if not f.exists():
        continue
    content = f.read_text()
    # Check for mailto subscribe link
    has_mailto = 'mailto:hello@clearing-ai.com' in content or 'mailto:subscribe@clearing-ai.com' in content
    has_formspree = 'formspree.io' in content
    has_action = 'action=' in content and 'form' in content.lower()
    print(f"  {'✅' if (has_mailto or has_formspree) else '⚠️'} {fname}: mailto={has_mailto}, formspree={has_formspree}, form={has_action}")

# --- 8. Sitemap priority signals check ---
print("\n=== 8. SITEMAP PRIORITY AUDIT ===")
priority_high = re.findall(r'<priority>(0\.(?:9[0-9]|[5-9][0-9]))</priority>', sitemap_content)
priority_daily = re.findall(r'<changefreq>daily</changefreq>', sitemap_content)
print(f"  High priority (0.8+) pages: {len(priority_high)}")
print(f"  Daily changefreq pages: {len(priority_daily)}")
print(f"  Sitemap stats: {sitemap_count} URLs, {len(priority_high)} priority 0.8+, {len(priority_daily)} daily")

# --- Summary ---
print("\n" + "="*50)
print("=== AUDIT SUMMARY ===")
print(f"  Pages checked: {pages_checked}")
print(f"  ❌ Critical issues: {len(issues)}")
print(f"  ⚠️  Warnings: {len(warnings)}")
if issues:
    print(f"\n  CRITICAL ISSUES:")
    for i in issues[:10]:
        print(f"    • {i}")
if warnings:
    print(f"\n  WARNINGS:")
    for w in warnings[:10]:
        print(f"    • {w}")
print("="*50)
