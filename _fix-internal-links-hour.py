#!/usr/bin/env python3
"""
Hour f4509cba Window — Phase 3: Internal Linking Fix
Add strategic internal links to orphan/underlinked pages
"""
import re, os

SITE = '/Users/nightcoder/Desktop/TheClearing'
os.chdir(SITE)

PAGES = {
    'ai-fatigue-compounding.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('burnout-vs-fatigue.html', 'AI Fatigue vs Burnout'),
            ('recovery.html', 'Recovery Guide'),
            ('mental-health.html', 'Mental Health'),
            ('daily-practice.html', 'Daily Practice'),
            ('skill-atrophy.html', 'Skill Atrophy'),
            ('cognitive-load.html', 'Cognitive Load'),
        ]
    },
    'tutorial-paradox.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('ai-learning-burnout.html', 'AI Learning Burnout'),
            ('ai-tool-overload.html', 'AI Tool Overload'),
            ('mindset.html', 'Mental Models'),
            ('compare.html', 'Tool Comparison'),
            ('resources.html', 'Resources'),
            ('community.html', 'Community'),
        ]
    },
    'ai-engineer-red-flags.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('burnout-vs-fatigue.html', 'AI Fatigue vs Burnout'),
            ('signs-ai-fatigue.html', 'Signs of AI Fatigue'),
            ('tips.html', '10 Signs'),
            ('workplace.html', 'Workplace Guide'),
            ('team-guide.html', 'Team Guide'),
            ('community.html', 'Community'),
        ]
    },
    'the-reward-deferred.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('burnout-vs-fatigue.html', 'AI Fatigue vs Burnout'),
            ('recovery.html', 'Recovery Guide'),
            ('mindset.html', 'Mental Models'),
            ('flow-state.html', 'Flow State'),
            ('productivity-theater.html', 'Productivity Theater'),
            ('community.html', 'Community'),
        ]
    },
    'the-attention-merchants.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('attention-residue.html', 'Attention Residue'),
            ('flow-state.html', 'Flow State'),
            ('cognitive-load.html', 'Cognitive Load'),
            ('decompress.html', 'Decompress'),
            ('daily-practice.html', 'Daily Practice'),
            ('skill-atrophy.html', 'Skill Atrophy'),
        ]
    },
    'the-pattern-erosion.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('skill-atrophy.html', 'Skill Atrophy'),
            ('cognitive-load.html', 'Cognitive Load'),
            ('developer-identity.html', 'Developer Identity'),
            ('senior-identity.html', 'Senior Identity'),
            ('mindset.html', 'Mental Models'),
            ('research.html', 'Research'),
        ]
    },
    'ai-fatigue-2026-numbers.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('stats.html', 'Statistics'),
            ('engineer-survey-results.html', 'Survey Results'),
            ('ai-fatigue-statistics-2025.html', '2025 Stats'),
            ('research.html', 'Research'),
            ('press-kit.html', 'Press Kit'),
            ('about.html', 'About'),
        ]
    },
    'ai-fatigue-by-language.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('compare.html', 'Tool Comparison'),
            ('ai-tool-overload.html', 'AI Tool Overload'),
            ('coding-ai-tools-comparison.html', 'Coding Tools Compare'),
            ('resources.html', 'Resources'),
            ('community.html', 'Community'),
            ('about.html', 'About'),
        ]
    },
    'platform-devops-ai-fatigue.html': {
        'heading': 'Continue Exploring',
        'links': [
            ('workplace.html', 'Workplace Guide'),
            ('team-guide.html', 'Team Guide'),
            ('hiring.html', 'Hiring Guide'),
            ('burnout-vs-fatigue.html', 'AI Fatigue vs Burnout'),
            ('community.html', 'Community'),
            ('recovery.html', 'Recovery'),
        ]
    },
}

def get_explore_html(title, links):
    cards_html = ''
    for url, label in links:
        cards_html += f'''          <a href="{url}" class="explore-card">
            <h4>{label}</h4>
            <span class="explore-arrow">→</span>
          </a>
'''
    return f'''
  <section class="continue-exploring">
    <div class="container">
      <h2>{title}</h2>
      <div class="explore-grid">
{cards_html}
      </div>
    </div>
  </section>
'''

def inject_links(html_file, page_data):
    with open(html_file, 'r') as f:
        content = f.read()
    
    links_html = get_explore_html(page_data['heading'], page_data['links'])
    
    # Find insertion point: before closing </main> or before last section
    if '</main>' in content:
        # Insert before </main>
        new_content = content.replace('</main>', links_html + '\n  </main>', 1)
    elif '</body>' in content:
        # Insert before </body>
        new_content = content.replace('</body>', links_html + '\n</body>', 1)
    else:
        print(f'  WARNING: No </main> or </body> in {html_file}')
        return content
    
    return new_content

def main():
    total_changes = 0
    for fname, data in PAGES.items():
        if not os.path.exists(fname):
            print(f'SKIP: {fname} not found')
            continue
        
        original = open(fname).read()
        updated = inject_links(fname, data)
        
        if updated == original:
            print(f'NO CHANGE: {fname}')
            continue
        
        with open(fname, 'w') as f:
            f.write(updated)
        
        # Count links added
        added = len(data['links'])
        print(f'✓ {fname}: added {added} links')
        total_changes += added
    
    print(f'\nTotal links added: {total_changes} across {len(PAGES)} pages')
    return total_changes

if __name__ == '__main__':
    main()