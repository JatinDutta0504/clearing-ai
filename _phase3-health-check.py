#!/usr/bin/env python3
"""Phase 3 Technical SEO Health Check — Hour 392"""
import os
import re
import json
from html.parser import HTMLParser

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_elements = {'area','base','br','col','embed','hr','img','input',
                              'link','meta','param','source','track','wbr'}
    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_elements:
            self.stack.append(tag.lower())
    def handle_endtag(self, tag):
        if tag.lower() in self.void_elements:
            return
        if self.stack and self.stack[-1] == tag.lower():
            self.stack.pop()
        elif tag.lower() in self.stack:
            idx = self.stack.index(tag.lower())
            self.errors.append(f"Unexpected </{tag}> at depth {idx}")
            self.stack = self.stack[:idx]
        else:
            self.errors.append(f"Unexpected closing tag </{tag}> (no matching open)")

def check_page(path):
    issues = []
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return ['FILE_READ_ERROR']
    
    issues = []
    
    # Check for essential meta
    if 'canonical' not in content:
        issues.append('MISSING: canonical')
    if 'og:image' not in content:
        issues.append('MISSING: og:image')
    if 'data-theme' not in content:
        issues.append('MISSING: data-theme (dark mode SSR)')
    
    # Check for broken internal links to .html (excluding external)
    html_links = re.findall(r'href="([^"#?/][^"]*\.html)"', content)
    for link in html_links:
        if not os.path.exists(link):
            issues.append(f'BROKEN_LINK: {link}')
    
    # Check for quiz.html (old broken link pattern)
    if 'href="/quiz.html"' in content or 'href="quiz.html"' in content:
        issues.append('OLD_LINK: quiz.html (should be index.html#/quiz or #quiz)')
    
    # Check for mailto:YOUR_FORM_ID or Formspree placeholder
    if 'YOUR_FORM_ID' in content:
        issues.append('FORMSPREE: YOUR_FORM_ID placeholder still present')
    
    # Check title length
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', content)
    if title_match:
        title_len = len(title_match.group(1).strip())
        if title_len > 60:
            issues.append(f'TITLE_TOO_LONG: {title_len} chars')
        elif title_len < 30:
            issues.append(f'TITLE_TOO_SHORT: {title_len} chars')
    
    # Check description length
    desc_match = re.search(r'<meta name="description" content="([^"]{10,})"', content)
    if desc_match:
        desc_len = len(desc_match.group(1))
        if desc_len > 160:
            issues.append(f'DESC_TOO_LONG: {desc_len} chars')
        elif desc_len < 120:
            issues.append(f'DESC_TOO_SHORT: {desc_len} chars')
    
    # Check HTML balance
    parser = HTMLValidator()
    try:
        parser.feed(content)
        if parser.stack:
            issues.append(f'UNCLOSED_TAGS: {parser.stack[-3:]}')
        if parser.errors:
            issues.extend(parser.errors[:3])
    except:
        issues.append('HTML_PARSE_ERROR')
    
    # Check for schema
    if 'schema.org' not in content and 'Schema.org' not in content:
        issues.append('NO_SCHEMA')
    
    # Check for BreadcrumbList
    if 'BreadcrumbList' not in content:
        issues.append('NO_BREADCRUMB')
    
    return issues

# Run on all HTML files
results = {}
html_files = sorted([f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')])

critical_issues = []
for f in html_files:
    issues = check_page(f)
    if issues:
        results[f] = issues
        for iss in issues:
            if any(x in iss for x in ['BROKEN_LINK', 'FORMSPREE', 'MISSING: canonical', 'MISSING: og:image', 'UNCLOSED', 'html_parse']):
                critical_issues.append((f, iss))

print(f"=== SITE HEALTH CHECK: {len(html_files)} pages ===")
print(f"\nCritical issues: {len(critical_issues)}")
for f, iss in critical_issues[:20]:
    print(f"  [{f}] {iss}")

print(f"\nTotal pages with issues: {len(results)}")
if len(results) <= 20:
    for f, issues in results.items():
        print(f"\n{f}:")
        for iss in issues:
            print(f"  - {iss}")

# Summary stats
issue_types = {}
for issues in results.values():
    for iss in issues:
        t = iss.split(':')[0]
        issue_types[t] = issue_types.get(t, 0) + 1

print("\n=== Issue Type Summary ===")
for k, v in sorted(issue_types.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
