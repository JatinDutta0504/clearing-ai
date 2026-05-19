#!/usr/bin/env python3
"""Add contextual internal links to low-link pages"""

import re, os

# Pages to fix + the links to add
# Format: (filename, [ (link_text, href, insert_phrase), ... ])
PAGE_UPDATES = {
    'engineer-stories.html': [
        # New links to add contextual content
        ('ai-fatigue-checklist.html', 'AI Fatigue Checklist', 'Take our interactive checklist to track your recovery journey'),
        ('community.html', 'Community support', 'Connect with engineers who understand what you\'re experiencing'),
        ('senior-identity.html', 'Senior engineer identity', 'Many senior engineers recognize themselves in these stories'),
        ('automation-anxiety.html', 'Automation anxiety', 'The anxiety underneath many of these stories'),
        ('junior-engineers.html', 'Junior engineer risks', 'Early-career engineers face unique AI fatigue risks'),
        # Update existing link to add context sentence
    ],
    'the-offload-loop.html': [
        ('the-explanation-requirement.html', 'The Explanation Requirement', 'One concrete practice that reverses the loop'),
        ('ai-fatigue-checklist.html', 'AI Fatigue Recovery Checklist', 'Track your offload-loop patterns with our checklist'),
        ('compare.html', 'AI coding tool comparison', 'See how different tools affect the offload loop differently'),
        ('community.html', 'Community stories', 'Engineers share how they broke the offload loop'),
        ('mindset.html', 'Mental models for AI use', 'Reframe your relationship with AI tools'),
    ],
    'the-productivity-gap.html': [
        ('ai-fatigue-checklist.html', 'AI Fatigue Recovery Checklist', 'Identify where your productivity-growth gap is widest'),
        ('the-reward-deferred.html', 'The Reward Deferred', 'Why output keeps growing but satisfaction doesn\'t'),
        ('skill-atrophy.html', 'Skill atrophy research', 'The research showing why more output ≠ more learning'),
        ('compare.html', 'AI tool comparison', 'See which tools widen vs close the productivity gap'),
        ('the-attention-merchants.html', 'Attention and AI', 'How AI tools compete for your cognitive attention'),
    ],
    'ai-fatigue-emergency-kit.html': [
        ('ai-fatigue-checklist.html', 'AI Fatigue Recovery Checklist', 'A longer-term tracking tool for recurring fatigue'),
        ('recovery.html', 'Full recovery guide', 'A structured 8-step path for sustained recovery'),
        ('mental-health.html', 'Mental health support', 'When fatigue intersects with mental health'),
        ('daily-practice.html', 'Daily practice routine', 'Build recovery habits that stick'),
        ('community.html', 'Community support', 'You don\'t have to recover alone'),
        ('checkin.html', 'Daily check-in tool', 'Track your fatigue levels every day'),
    ],
    'refer.html': [
        ('engineer-stories.html', 'Engineer stories', 'See how others talked about their fatigue'),
        ('quiz.html', 'AI Fatigue Quiz', 'Send them the quiz to self-assess'),
        ('ai-fatigue-checklist.html', 'Recovery checklist', 'A shareable resource they can use today'),
        ('community.html', 'Community', 'Point them to peer support'),
    ],
}

def add_contextual_links_to_page(filepath, new_links):
    """Add contextual in-content links + expand explore grid"""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # 1. Add 2-3 contextual link sentences in the body (before Continue Exploring)
    # Find the last </p> or </li> or </h3> before "Continue Exploring"
    insert_point = content.find('Continue Exploring')
    if insert_point == -1:
        # Find </section> before footer
        insert_point = content.rfind('</section>', 0, content.find('<footer'))
    if insert_point == -1:
        insert_point = content.find('<footer')

    link_html_parts = []
    for href, link_text, context in new_links:
        # Make relative path clean
        if href.startswith('/'):
            href_clean = href.lstrip('/')
        else:
            href_clean = href
        link_html_parts.append(
            f'<a href="{href}" class="context-link">{link_text}</a>'
        )

    # Build 2 contextual paragraphs to inject
    contextual_block = f'''
    <section style="padding: 1.5rem 2rem; max-width: 900px; margin: 0 auto;">
      <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
        Also helpful: {' · '.join(link_html_parts[:3])} — curated resources for engineers working through this.
      </p>
    </section>
    '''

    content = content[:insert_point] + contextual_block + content[insert_point:]

    # 2. Expand explore grid with 2 more links
    explore_grid_end = content.find('</div>', content.find('explore-grid'))
    if explore_grid_end != -1:
        more_cards = ''
        for href, link_text, context in new_links[3:5]:
            if href.startswith('/'):
                href_clean = href.lstrip('/')
            else:
                href_clean = href
            icon_map = {
                'community.html': '👥', 'quiz.html': '📋', 'ai-fatigue-checklist.html': '✅',
                'recovery.html': '🌱', 'mental-health.html': '🧠', 'checkin.html': '📊',
                'daily-practice.html': '📅', 'senior-identity.html': '👴', 'junior-engineers.html': '📈',
                'automation-anxiety.html': '😰', 'compare.html': '⚖️', 'skill-atrophy.html': '📉',
                'the-reward-deferred.html': '⏳', 'the-attention-merchants.html': '🎯',
                'the-explanation-requirement.html': '💡', 'mindset.html': '🧭',
                'ai-fatigue.html': '🔍', 'resources.html': '📚', 'about.html': '🏠',
                'engineer-stories.html': '💬',
            }
            icon = icon_map.get(href_clean, '➡️')
            more_cards += f'''
        <a href="{href_clean}" class="explore-card">
          <span style="font-size:1.5rem;">{icon}</span>
          <h3>{link_text}</h3>
          <p>{context}</p>
        </a>'''
        # Find the explore grid div and add more cards before its closing div
        grid_start = content.find('class="explore-grid"')
        if grid_start != -1:
            grid_end = content.find('</div>', grid_start)
            content = content[:grid_end] + more_cards + content[grid_end:]

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {filepath}")
    else:
        print(f"⚠️  No changes to {filepath}")

for fname, links in PAGE_UPDATES.items():
    path = os.path.join(os.path.dirname(__file__), fname) if __name__ != '__main__' else fname
    if os.path.exists(path):
        add_contextual_links_to_page(path, links)
    else:
        print(f"❌ Not found: {path}")