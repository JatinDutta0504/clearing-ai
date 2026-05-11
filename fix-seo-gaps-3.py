#!/usr/bin/env python3
"""Fix remaining SEO gaps: 3 pages missing title/desc/og, 1 page missing og."""
import re, os

fixes = [
    {
        'file': 'community.html',
        'has_canonical': True, 'has_title': False, 'has_desc': False, 'has_og': False,
        'title': 'Communities for AI-Fatigued Engineers: You\'re Not Alone | The Clearing',
        'desc': 'The best communities for engineers dealing with AI fatigue — online and in-person. Find your people, share what you\'re going through, recover together.',
        'url': 'https://clearing-ai.com/community.html'
    },
    {
        'file': 'imposter-syndrome-ai.html',
        'has_canonical': True, 'has_title': False, 'has_desc': False, 'has_og': False,
        'title': 'Imposter Syndrome vs AI Fatigue: How to Tell the Difference | The Clearing',
        'desc': 'Can\'t tell if you\'re experiencing imposter syndrome or AI fatigue? This guide breaks down the difference and what to do about each one.',
        'url': 'https://clearing-ai.com/imposter-syndrome-ai.html'
    },
    {
        'file': 'ml-engineer-ai-fatigue.html',
        'has_canonical': True, 'has_title': False, 'has_desc': False, 'has_og': False,
        'title': 'ML Engineer AI Fatigue: When You\'re Building the Thing That\'s Changing Everything | The Clearing',
        'desc': 'AI fatigue hits ML engineers differently — you\'re building the tools that are reshaping your own job. Here\'s how to navigate it without losing yourself.',
        'url': 'https://clearing-ai.com/ml-engineer-ai-fatigue.html'
    },
    {
        'file': 'hn-ai-fatigue-may7.html',
        'has_canonical': True, 'has_title': True, 'has_desc': True, 'has_og': False,
        'title': 'We Mapped AI Fatigue Across 2,000+ Engineers — Here\'s What We Found | The Clearing',
        'desc': 'The Clearing\'s 2026 AI Fatigue Report: what 2,000+ quiz takers revealed about skill decline, identity crisis, and what actually helps recovery.',
        'url': 'https://clearing-ai.com/hn-ai-fatigue-may7.html'
    }
]

for fix in fixes:
    fname = fix['file']
    with open(fname, 'r') as f:
        content = f.read()
    
    original = content
    
    # For all pages: add OG/Twitter tags after existing meta viewport or charset
    if not fix['has_og']:
        og_block = f'''  <meta property="og:title" content="{fix['title']}">
  <meta property="og:description" content="{fix['desc']}">
  <meta property="og:image" content="https://clearing-ai.com/og-image.png">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{fix['url']}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{fix['title']}">
  <meta name="twitter:description" content="{fix['desc']}">
  <meta name="twitter:image" content="https://clearing-ai.com/og-image.png">
'''
        
        # Insert after <meta charset> or <meta name="viewport">
        vp_match = re.search(r'(<meta (?:charset|viewport)[^>]+>\n)', content)
        if vp_match:
            pos = vp_match.end()
            content = content[:pos] + og_block + content[pos:]

    # For pages missing title AND desc: add them before canonical
    if not fix['has_title'] or not fix['has_desc']:
        title_tag = f'  <title>{fix["title"]}</title>\n'
        desc_tag = f'  <meta name="description" content="{fix["desc"]}">\n'
        
        # Find canonical and insert title+desc before it
        canon_match = re.search(r'(\s*<link rel="canonical" href="[^"]+">\n)', content)
        if canon_match:
            pos = canon_match.start()
            content = content[:pos] + title_tag + desc_tag + content[pos:]
    
    if content != original:
        with open(fname, 'w') as f:
            f.write(content)
        print(f'FIXED: {fname}')
    else:
        print(f'NO CHANGE: {fname}')

print('\nDone.')