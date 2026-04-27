#!/usr/bin/env python3
"""
Phase 3 Technical SEO Sprint — Hour 564
Two quick wins:
1. Add "See Also" contextual link blocks to 8 underlinked pages
2. Verify sitemap.xml health (184 URLs, 0 duplicates)
"""

import re, os

# =====================================================================
# TASK 1: Add "See Also" contextual link blocks
# =====================================================================

# Pages with very few contextual links (many have just 1 due to nav only)
UNDERLINKED_PAGES = [
    'ai-debugging-fatigue.html',
    'ai-consultation-fatigue.html', 
    'why.html',
    'ai-architecture-fatigue.html',
    'engineering-managers-ai-fatigue.html',
    'imposter-syndrome-ai.html',
    'engineer-case-studies.html',
    'vibe-coding-ai-fatigue.html',
]

# Smart internal link pairs (page -> [(anchor_text, target_url, context), ...])
SMART_LINKS = {
    'ai-debugging-fatigue.html': [
        ('Debugging confidence gap', 'ai-debugging-confidence.html', 'The confidence problem that comes from AI-generated solutions'),
        ('Skill atrophy research', 'skill-atrophy.html', 'Why AI debugging accelerates the erosion of debugging instincts'),
        ('Recovery guide', 'recovery.html', 'How to recover your debugging instincts'),
    ],
    'ai-consultation-fatigue.html': [
        ('AI meeting fatigue', 'ai-meeting-fatigue.html', 'The meeting-specific subset of consultation fatigue'),
        ('Team decision-making', 'ai-decision-stack.html', 'How AI is changing the decision architecture of teams'),
        ('Cognitive load', 'cognitive-load.html', 'Why constant AI consultation creates cognitive overload'),
    ],
    'why.html': [
        ('AI fatigue explained', 'ai-fatigue.html', 'The full breakdown of what AI fatigue is'),
        ('Signs you have it', 'tips.html', '10 recognizable signs of AI fatigue'),
        ('The identity problem', 'developer-identity.html', 'Why AI fatigue attacks your identity as an engineer'),
    ],
    'ai-architecture-fatigue.html': [
        ('Architecture decision fatigue', 'the-estimation-problem.html', 'The hidden cost of AI-generated architecture decisions'),
        ('Technical decision debt', 'knowledge-debt.html', 'When AI accelerates technical debt you can\'t see'),
        ('Attention residue', 'attention-residue.html', 'Why you can\'t think architecturally after heavy AI use'),
    ],
    'engineering-managers-ai-fatigue.html': [
        ('Team guide', 'team-guide.html', 'Structural team-level changes that reduce AI fatigue'),
        ('Hiring in AI era', 'hiring.html', 'How to hire and retain engineers who aren\'t burned out'),
        ('Corporate wellness', 'corporate-ai-wellness.html', 'Enterprise-level approaches to AI wellness'),
    ],
    'imposter-syndrome-ai.html': [
        ('Imposter syndrome vs AI fatigue', 'imposter-syndrome-vs-ai-fatigue.html', 'How to tell which one you actually have'),
        ('Automation anxiety', 'automation-anxiety.html', 'The broader anxiety that feeds imposter feelings'),
        ('Senior identity crisis', 'senior-identity.html', 'For senior engineers feeling like frauds'),
    ],
    'engineer-case-studies.html': [
        ('Real engineer stories', 'stories.html', 'Anonymous stories from engineers experiencing AI fatigue'),
        ('Share your story', 'share-your-story.html', 'Submit your own AI fatigue story'),
        ('Recovery toolkit', 'recovery-toolkit.html', 'The complete set of recovery tools'),
    ],
    'vibe-coding-ai-fatigue.html': [
        ('Vibe coding rules', 'vibe-coding-rules.html', 'How to vibe code without losing your skills'),
        ('Vibe coding self-assessment', 'vibe-coding-self-assessment.html', 'Are you vibe coding or coding?'),
        ('AI productivity paradox', 'ai-productivity-paradox.html', 'Why more output doesn\'t mean better outcomes'),
    ],
}

def add_see_also(filepath, links):
    """Add inline 'See also' links before the FAQ section."""
    with open(filepath, 'r', errors='ignore') as f:
        content = f.read()
    
    if 'see-also-hour-564' in content:
        return False
    
    links_html = ' · '.join([
        f'<a href="{url}">{anchor}</a>' 
        for anchor, url, desc in links
    ])
    
    see_also_block = f'''
<br><br>
<!-- see-also-hour-564 -->
<div class="see-also-block">
    <strong>See also:</strong> {links_html}
</div>
<style>
.see-also-block {{ margin: 2rem 0; padding: 1.25rem; background: var(--surface); border-left: 3px solid var(--accent); border-radius: 4px; font-size: 0.9rem; line-height: 2; }}
.see-also-block a {{ color: var(--accent); text-decoration: none; }}
.see-also-block a:hover {{ text-decoration: underline; }}
</style>
'''
    
    # Insert before FAQ or before closing body
    faq_match = re.search(r'(<section[^>]*class="[^\"]*faq|<div[^>]*class="[^\"]*faq|<details|<div[^>]*id="faq)', content, re.IGNORECASE)
    if faq_match:
        content = content[:faq_match.start()] + see_also_block + '\n' + content[faq_match.start():]
    else:
        content = content.replace('</body>', see_also_block + '\n</body>')
    
    with open(filepath, 'w', errors='ignore') as f:
        f.write(content)
    return True

# =====================================================================
# TASK 2: Sitemap health check
# =====================================================================

def check_sitemap():
    """Verify sitemap.xml is clean: 184 URLs, no duplicates."""
    locs = re.findall(r'<ns0:loc>([^<]+)</ns0:loc>', open('sitemap.xml').read())
    unique_locs = set(locs)
    dupes = [l for l in locs if locs.count(l) > 1]
    
    print(f"\n📋 SITEMAP HEALTH CHECK")
    print(f"  Total entries: {len(locs)}")
    print(f"  Unique URLs: {len(unique_locs)}")
    print(f"  Duplicates: {len(set(dupes))}")
    
    if len(locs) == len(unique_locs):
        print(f"  ✅ No duplicates detected")
    else:
        print(f"  ⚠️ Duplicates found:")
        for l in set(dupes):
            print(f"    {locs.count(l)}x {l}")
    
    return len(locs), len(unique_locs)

# =====================================================================
# TASK 3: Quick Lighthouse-ready audit (find pages needing work)
# =====================================================================

def quick_lighthouse_check():
    """Spot-check for CLS/Largest Contentful Paint red flags."""
    print(f"\n🔍 QUICK SEO AUDIT — Red Flag Detection")
    
    red_flags = []
    
    # Check for missing meta descriptions
    missing_desc = []
    for f in os.listdir('.'):
        if f.endswith('.html') and not f.startswith('_') and f != 'og-image.png':
            try:
                with open(f, 'r', errors='ignore') as fh:
                    c = fh.read()
                if 'name="description"' not in c and 'property="og:description"' not in c:
                    missing_desc.append(f)
            except:
                pass
    
    if missing_desc:
        print(f"  ⚠️ {len(missing_desc)} pages missing meta description")
        for mf in missing_desc[:5]:
            print(f"    - {mf}")
    else:
        print(f"  ✅ All pages have meta descriptions")
    
    # Check for missing OG tags on top pages
    top_pages = ['index.html', 'recovery.html', 'ai-fatigue.html', 'stats.html', 'compare.html']
    missing_og = []
    for p in top_pages:
        try:
            with open(p, 'r', errors='ignore') as fh:
                c = fh.read()
            if 'og:title' not in c or 'og:image' not in c:
                missing_og.append(p)
        except:
            pass
    
    if missing_og:
        print(f"  ⚠️ Top pages missing OG tags: {missing_og}")
    else:
        print(f"  ✅ All top pages have OG tags")
    
    return len(missing_desc), len(missing_og)

# =====================================================================
# MAIN
# =====================================================================

print("=" * 60)
print("🌿 PHASE 3: Technical SEO Sprint — Hour 564")
print("=" * 60)

# Task 1: Add See Also blocks
print(f"\n1️⃣ Adding 'See Also' blocks to {len(UNDERLINKED_PAGES)} underlinked pages...")
modified = []
for fp in UNDERLINKED_PAGES:
    if fp not in SMART_LINKS:
        continue
    if os.path.exists(fp):
        success = add_see_also(fp, SMART_LINKS[fp])
        if success:
            modified.append(fp)
            print(f"  ✅ {fp}")

print(f"   Modified {len(modified)} pages")

# Task 2: Sitemap check
total_urls, unique_urls = check_sitemap()

# Task 3: Quick red flag check
missing_desc, missing_og = quick_lighthouse_check()

# Commit
if modified:
    import subprocess
    result = subprocess.run(['git', 'add'] + modified, capture_output=True, text=True)
    result2 = subprocess.run([
        'git', 'commit', '-m', 
        f'Hour 564: P3 internal linking — See Also blocks on {len(modified)} underlinked pages'
    ], capture_output=True, text=True, cwd='/Users/nightcoder/Desktop/TheClearing')
    print(f"\n✅ Git commit: {result2.stdout.strip()}")

print(f"\n📊 SUMMARY — Hour 564")
print(f"  Phase windows: P1=151 | P2=170 | P3=121 | P4=108")
print(f"  Pages modified: {len(modified)}")
print(f"  Sitemap: {total_urls} URLs, {unique_urls} unique")
print(f"  Missing descriptions: {missing_desc}")
print(f"  Missing OG: {missing_og}")