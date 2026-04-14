#!/usr/bin/env python3
import re, os

issues = []
for f in os.listdir('.'):
    if not f.endswith('.html'):
        continue
    content = open(f).read()
    has_jsonld = '"@type": "FAQPage"' in content
    if not has_jsonld:
        continue

    has_details = '<details>' in content
    has_faq_question = 'faq-question' in content
    # Check for visible FAQ section with heading
    article_end = content.rfind('</article>') if '</article>' in content else len(content) - 500
    end_content = content[max(0, article_end-3000):]
    has_faq_h = bool(re.search(r'<h[23][^>]*>.*?[Ff]req', end_content)) or bool(re.search(r'<h[23][^>]*>.*? [Aa]sk ', end_content))
    has_section_class = 'faq-section' in end_content

    has_real_faq = (has_details or has_faq_question) and has_faq_h

    if has_jsonld and not has_real_faq:
        issues.append(f)

if issues:
    print(f'GENUINE ISSUES ({len(issues)} pages):')
    for f in sorted(issues):
        print(f'  {f}')
else:
    print('All pages with FAQPage JSON-LD have visible FAQ content')
