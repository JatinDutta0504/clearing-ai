#!/usr/bin/env python3
"""Add keyword-relevant explore sections to 13 pillar pages + fix imposter-syndrome-ai.html."""
import os

# Contextual explore sections keyed by page
EXPLORE_SECTIONS = {
    'ai-brownout.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="burnout-vs-fatigue.html">Burnout vs. Fatigue</a></li>
        <li><a href="ai-fatigue.html">What is AI Fatigue?</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="checkin.html">Daily Check-in</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
    'ai-free-practice.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="daily-practice.html">Daily Practice</a></li>
        <li><a href="skill-atrophy.html">Skill Atrophy</a></li>
        <li><a href="mindset.html">Mental Models</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
    'neurodivergent-engineer-ai-fatigue.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="ai-fatigue.html">What is AI Fatigue?</a></li>
        <li><a href="community.html">Community Support</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="checkin.html">Daily Check-in</a></li>
      </ul>
    </div>
  </section>
''',
    'working-parent-burnout.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="community.html">Community</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="daily-practice.html">Daily Practice</a></li>
        <li><a href="checkin.html">Daily Check-in</a></li>
      </ul>
    </div>
  </section>
''',
    'vibe-coding-deep-dive.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="vibe-coding.html">Vibe Coding Overview</a></li>
        <li><a href="skill-atrophy.html">Skill Atrophy</a></li>
        <li><a href="mindset.html">Mental Models</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
    'imposter-syndrome-ai.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="developer-identity.html">Developer Identity</a></li>
        <li><a href="senior-identity.html">Senior Identity</a></li>
        <li><a href="research.html">Research</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
    'ai-fatigue-checklist.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="checkin.html">Daily Check-in</a></li>
        <li><a href="daily-practice.html">Daily Practice</a></li>
        <li><a href="ai-fatigue-recovery-checklist-pdf.html">Downloadable PDF</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
    'engineering-managers-ai-fatigue.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="team-manager-guide.html">Manager Guide</a></li>
        <li><a href="corporate-ai-wellness.html">Corporate Wellness</a></li>
        <li><a href="hiring.html">Retaining Engineers</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
    'ai-debugging-fatigue.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="skill-atrophy.html">Skill Atrophy</a></li>
        <li><a href="cognitive-load.html">Cognitive Load</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="daily-ai-boundaries.html">Daily AI Boundaries</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
    'ai-architecture-fatigue.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="cognitive-load.html">Cognitive Load</a></li>
        <li><a href="productivity-theater.html">Productivity Theater</a></li>
        <li><a href="flow-state.html">Flow State</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
    'the-consultation-trap.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="ai-fatigue.html">What is AI Fatigue?</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="manifesto.html">The Manifesto</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="daily-ai-boundaries.html">Daily AI Boundaries</a></li>
        <li><a href="mental-health.html">mental-health</a></li>
      </ul>
    </div>
  </section>
''',
    'engineer-energy-management.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
        <li><a href="daily-practice.html">Daily Practice</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="checkin.html">Daily Check-in</a></li>
        <li><a href="community.html">Community</a></li>
      </ul>
    </div>
  </section>
''',
    'engineer-case-studies.html': '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="stories.html">Engineer Stories</a></li>
        <li><a href="community.html">Community</a></li>
        <li><a href="senior-identity.html">Senior Identity</a></li>
        <li><a href="recovery.html">Recovery Guide</a></li>
        <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
''',
}

EXPLORE_CSS = '''
.explore-section { background: var(--surface, #161616); border-top: 1px solid var(--border, #2a2a2a); padding: 48px 0; margin-top: 64px; }
.explore-inner { max-width: 900px; margin: 0 auto; padding: 0 24px; }
.explore-section h2 { font-size: 1.2rem; font-weight: 600; color: var(--text, #e8e6e3); margin-bottom: 20px; letter-spacing: 0.5px; text-transform: uppercase; font-size: 0.85rem; color: var(--muted, #6e7681); }
.explore-links { list-style: none; display: flex; flex-wrap: wrap; gap: 12px; }
.explore-links li { flex: 0 1 auto; }
.explore-links a { display: inline-block; background: var(--surface-2, #1e1e1e); border: 1px solid var(--border, #2a2a2a); color: var(--text, #e8e6e3); padding: 8px 16px; border-radius: 6px; font-size: 0.9rem; text-decoration: none; transition: all 0.2s ease; }
.explore-links a:hover { border-color: var(--accent, #5c8c6e); color: var(--accent, #5c8c6e); transform: translateY(-1px); }
'''

def add_explore_section(fname, section_html):
    with open(fname, 'r') as f:
        content = f.read()
    
    # Remove the generic explore section if it exists (from the generic script)
    if '<section class="explore-section"' in content:
        # Find and replace it with the contextual one
        import re
        # Remove existing explore section
        content = re.sub(r'\s*<section class="explore-section"[^>]*>.*?</section>\s*', '\n', content, flags=re.DOTALL)
    
    # Add CSS if needed
    if '.explore-section' not in content:
        if '</style>' in content:
            content = content.replace('</style>', EXPLORE_CSS + '\n  </style>', 1)
        elif '</head>' in content:
            content = content.replace('</head>', '<style>' + EXPLORE_CSS + '</style>\n</head>', 1)
    
    # Add explore section before </body>
    if '</body>' in content:
        content = content.replace('</body>', section_html + '\n</body>', 1)
    elif '</html>' in content:
        content = content.replace('</html>', section_html + '\n</html>', 1)
    
    with open(fname, 'w') as f:
        f.write(content)

count = 0
for fname, section in EXPLORE_SECTIONS.items():
    if os.path.exists(fname):
        add_explore_section(fname, section)
        print(f'UPDATED: {fname}')
        count += 1
    else:
        print(f'MISSING: {fname}')

print(f'\nDone. Updated {count}/{len(EXPLORE_SECTIONS)} pages with contextual explore sections.')