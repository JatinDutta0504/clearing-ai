#!/usr/bin/env python3
"""Fix missing SEO metadata on 9 content pages."""
import re, os

pages = {
    'community.html': {
        'title': 'Communities for AI-Fatigued Engineers: You\'re Not Alone',
        'desc': 'The best communities for engineers dealing with AI fatigue — online and in-person. Find your people, share what you\'re going through, recover together.',
        'url': 'https://clearing-ai.com/community.html'
    },
    'workplace.html': {
        'title': 'AI Fatigue at Work: How to Set Limits and Talk to Your Manager',
        'desc': 'Practical strategies for setting AI limits at work, conversation scripts for your manager, and how to protect your energy when AI is mandatory.',
        'url': 'https://clearing-ai.com/workplace.html'
    },
    'imposter-syndrome-ai.html': {
        'title': 'Imposter Syndrome vs AI Fatigue: How to Tell the Difference',
        'desc': 'Can\'t tell if you\'re experiencing imposter syndrome or AI fatigue? This guide breaks down the difference and what to do about each one.',
        'url': 'https://clearing-ai.com/imposter-syndrome-ai.html'
    },
    'ml-engineer-ai-fatigue.html': {
        'title': 'ML Engineer AI Fatigue: When You\'re Building the Thing That\'s Changing Everything',
        'desc': 'AI fatigue hits ML engineers differently — you\'re building the tools that are reshaping your own job. Here\'s how to navigate it without losing yourself.',
        'url': 'https://clearing-ai.com/ml-engineer-ai-fatigue.html'
    },
    'quiz-results-tier-1.html': {
        'title': 'Some Fatigue Is Showing — AI Fatigue Tier 1 | The Clearing',
        'desc': 'Your quiz results: Some Fatigue Is Showing. You\'re functional but something\'s off. Here\'s what tier 1 AI fatigue means and how to address it.',
        'url': 'https://clearing-ai.com/quiz-results-tier-1.html'
    },
    'quiz-results-tier-2.html': {
        'title': 'Real Fatigue Is Setting In — AI Fatigue Tier 2 | The Clearing',
        'desc': 'Your quiz results: Real Fatigue Is Setting In. The signs are compounding. Here\'s what tier 2 AI fatigue means and how to start recovering.',
        'url': 'https://clearing-ai.com/quiz-results-tier-2.html'
    },
    'ai-fatigue-checklist-print.html': {
        'title': 'AI Fatigue Recovery Checklist — 30 Days to Reclaim Your Energy',
        'desc': 'The 30-day AI fatigue recovery checklist — print-friendly. Concrete daily actions to reclaim your energy, focus, and sense of craft as an engineer.',
        'url': 'https://clearing-ai.com/ai-fatigue-checklist-print.html'
    },
    'hn-ai-fatigue-may7.html': {
        'title': 'The Clearing — HN Launch Post',
        'desc': 'We mapped AI fatigue across 2,000+ engineers. Here\'s what we found — and what\'s actually working for recovery.',
        'url': 'https://clearing-ai.com/hn-ai-fatigue-may7.html'
    },
    'newsletter-outreach-dashboard.html': {
        'title': 'Newsletter Outreach Dashboard — The Clearing',
        'desc': 'Internal newsletter partnership tracking dashboard for The Clearing team.',
        'url': 'https://clearing-ai.com/newsletter-outreach-dashboard.html'
    }
}

for fname, meta in pages.items():
    if not os.path.exists(fname):
        print(f'SKIP: {fname} not found')
        continue
    
    with open(fname, 'r') as f:
        content = f.read()
    
    original = content
    
    # 1. Add canonical if missing
    if 'canonical' not in content:
        # Add after any existing link tags in head
        canonical_tag = f'  <link rel="canonical" href="{meta["url"]}">\n'
        # Find position: after charset meta or after existing meta tags
        insert_after = re.search(r'(<meta charset[^>]+>\n)', content)
        if insert_after:
            pos = insert_after.end()
            content = content[:pos] + canonical_tag + content[pos:]
        else:
            # After <head> tag
            head_match = re.search(r'(<head[^>]*>\n)', content)
            if head_match:
                pos = head_match.end()
                content = content[:pos] + '  ' + canonical_tag.strip() + '\n' + content[pos:]
    
    # 2. Add title if missing
    if not re.search(r'<title>', content):
        title_tag = f'  <title>{meta["title"]}</title>\n'
        # Insert after description meta tag if it exists, else after charset
        desc_match = re.search(r'(<meta name="description" content="[^"]+">\n)', content)
        if desc_match:
            pos = desc_match.end()
            content = content[:pos] + title_tag + content[pos:]
        else:
            charset_match = re.search(r'(<meta charset[^>]+>\n)', content)
            if charset_match:
                pos = charset_match.end()
                content = content[:pos] + title_tag + content[pos:]
    
    # 3. Add meta description if missing
    if not re.search(r'<meta name="description"', content):
        desc_tag = f'  <meta name="description" content="{meta["desc"]}">\n'
        charset_match = re.search(r'(<meta charset[^>]+>\n)', content)
        if charset_match:
            pos = charset_match.end()
            content = content[:pos] + desc_tag + content[pos:]
    
    # 4. Add OG/Twitter tags if missing (only for content pages, not internal tools)
    if fname not in ['newsletter-outreach-dashboard.html', 'hn-ai-fatigue-may7.html']:
        if 'og:title' not in content:
            og_tags = f'''  <meta property="og:title" content="{meta["title"]}">
  <meta property="og:description" content="{meta["desc"]}">
  <meta property="og:image" content="https://clearing-ai.com/og-image.png">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{meta["url"]}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{meta["title"]}">
  <meta name="twitter:description" content="{meta["desc"]}">
  <meta name="twitter:image" content="https://clearing-ai.com/og-image.png">
'''
            charset_match = re.search(r'(<meta charset[^>]+>\n)', content)
            if charset_match:
                pos = charset_match.end()
                content = content[:pos] + og_tags + content[pos:]
    
    if content != original:
        with open(fname, 'w') as f:
            f.write(content)
        print(f'FIXED: {fname}')
    else:
        print(f'NO CHANGE: {fname}')

print('\nDone.')