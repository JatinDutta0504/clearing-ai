#!/usr/bin/env python3
"""Fix missing SEO metadata on 5 remaining content pages. Insert in proper order."""
import re, os

pages = {
    'community.html': {
        'title': 'Communities for AI-Fatigued Engineers: You\'re Not Alone | The Clearing',
        'desc': 'The best communities for engineers dealing with AI fatigue — online and in-person. Find your people, share what you\'re going through, recover together.',
        'url': 'https://clearing-ai.com/community.html'
    },
    'imposter-syndrome-ai.html': {
        'title': 'Imposter Syndrome vs AI Fatigue: How to Tell the Difference | The Clearing',
        'desc': 'Can\'t tell if you\'re experiencing imposter syndrome or AI fatigue? This guide breaks down the difference and what to do about each one.',
        'url': 'https://clearing-ai.com/imposter-syndrome-ai.html'
    },
    'ml-engineer-ai-fatigue.html': {
        'title': 'ML Engineer AI Fatigue: When You\'re Building the Thing That\'s Changing Everything | The Clearing',
        'desc': 'AI fatigue hits ML engineers differently — you\'re building the tools that are reshaping your own job. Here\'s how to navigate it without losing yourself.',
        'url': 'https://clearing-ai.com/ml-engineer-ai-fatigue.html'
    },
    'hn-ai-fatigue-may7.html': {
        'title': 'We Mapped AI Fatigue Across 2,000+ Engineers — Here\'s What We Found | The Clearing',
        'desc': 'The Clearing\'s 2026 AI Fatigue Report: what 2,000+ quiz takers revealed about skill decline, identity crisis, and what actually helps recovery.',
        'url': 'https://clearing-ai.com/hn-ai-fatigue-may7.html'
    }
}

for fname, meta in pages.items():
    if not os.path.exists(fname):
        print(f'SKIP: {fname} not found')
        continue
    
    with open(fname, 'r') as f:
        content = f.read()
    
    original = content
    
    # Build all meta tags in proper order (title first, then desc, then canonical, then og)
    # Since canonical may already exist, we'll replace/insert properly
    
    # Remove existing canonical if it's the only SEO tag (it was inserted incorrectly before title/desc)
    # Check if canonical exists BEFORE title in current file
    canon_pos = content.find('canonical')
    title_pos = content.find('<title>')
    if canon_pos >= 0 and title_pos >= 0 and canon_pos < title_pos:
        # Canonical is before title - remove it and re-add in correct position
        content = re.sub(r'\s*<link rel="canonical" href="[^"]+">\n', '', content)
    
    # Now build the proper head block
    head_block = f'''  <title>{meta["title"]}</title>
  <meta name="description" content="{meta["desc"]}">
  <link rel="canonical" href="{meta["url"]}">
  <meta property="og:title" content="{meta["title"]}">
  <meta property="og:description" content="{meta["desc"]}">
  <meta property="og:image" content="https://clearing-ai.com/og-image.png">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{meta["url"]}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{meta["title"]}">
  <meta name="twitter:description" content="{meta["desc"]}">
  <meta name="twitter:image" content="https://clearing-ai.com/og-image.png">
'''
    
    # Find where to insert: after <head> tag line, before any existing style/meta
    head_match = re.search(r'(<head[^>]*>\n)', content)
    if head_match:
        insert_pos = head_match.end()
        content = content[:insert_pos] + head_block + content[insert_pos:]
    
    if content != original:
        with open(fname, 'w') as f:
            f.write(content)
        print(f'FIXED: {fname}')
    else:
        print(f'NO CHANGE: {fname}')

print('\nDone.')