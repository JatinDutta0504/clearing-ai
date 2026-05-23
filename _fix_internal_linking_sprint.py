#!/usr/bin/env python3
"""Add explore-section to content pages missing it."""
import os, re

EXPLORE_SECTION = '''
  <section class="explore-section" aria-label="Continue exploring">
    <div class="explore-inner">
      <h2>Continue Exploring</h2>
      <ul class="explore-links">
        <li><a href="recovery.html">Recovery</a></li>
        <li><a href="ai-detox-plan.html">Ai Detox Plan</a></li>
        <li><a href="daily-practice.html">Daily Practice</a></li>
        <li><a href="daily-ai-boundaries.html">Daily Ai Boundaries</a></li>
        <li><a href="checkin.html">Checkin</a></li>
        <li><a href="mental-health.html">Mental Health</a></li>
      </ul>
    </div>
  </section>
'''

EXPLORE_CSS = '''
.explore-section { background: var(--surface, #161616); border-top: 1px solid var(--border, #2a2a2a); padding: 48px 0; margin-top: 64px; }
.explore-inner { max-width: 900px; margin: 0 auto; padding: 0 24px; }
.explore-section h2 { font-size: 1.2rem; font-weight: 600; color: var(--text, #e8e6e3); margin-bottom: 20px; letter-spacing: 0.5px; text-transform: uppercase; font-size: 0.85rem; color: var(--muted, #6e7681); }
.explore-links { list-style: none; display: flex; flex-wrap: wrap; gap: 12px; }
.explore-links li { flex: 0 1 auto; }
.explore-links a { display: inline-block; background: var(--surface-2, #1e1e1e); border: 1px solid var(--border, #2a2a2a); color: var(--text, #e8e6e3); padding: 8px 16px; border-radius: 6px; font-size: 0.9rem; text-decoration: none; transition: all 0.2s ease; }
.explore-links a:hover { border-color: var(--accent, #5c8c6e); color: var(--accent, #5c8c6e); transform: translateY(-1px); }
'''

PAGES = [
    'ai-brownout.html',
    'ai-free-practice.html',
    'neurodivergent-engineer-ai-fatigue.html',
    'working-parent-burnout.html',
    'vibe-coding-deep-dive.html',
    'imposter-syndrome-ai.html',
    'ai-fatigue-checklist.html',
    'engineering-managers-ai-fatigue.html',
    'ai-debugging-fatigue.html',
    'ai-architecture-fatigue.html',
    'the-consultation-trap.html',
    'engineer-energy-management.html',
    'engineer-case-studies.html',
]

fixed = 0
for fname in PAGES:
    if not os.path.exists(fname):
        print(f'SKIP (not found): {fname}')
        continue
    with open(fname, 'r') as f:
        content = f.read()
    
    if '<section class="explore-section"' in content:
        print(f'OK (already has explore): {fname}')
        continue
    
    # Add CSS for explore-section if not present
    if '.explore-section' not in content:
        # Insert before </style> or before </head>
        if '</style>' in content:
            content = content.replace('</style>', EXPLORE_CSS + '\n  </style>', 1)
        elif '</head>' in content:
            content = content.replace('</head>', '<style>' + EXPLORE_CSS + '</style>\n</head>', 1)
    
    # Add explore-section before </body>
    if '</body>' in content:
        content = content.replace('</body>', EXPLORE_SECTION + '\n</body>', 1)
    elif '</html>' in content:
        content = content.replace('</html>', EXPLORE_SECTION + '\n</html>', 1)
    
    with open(fname, 'w') as f:
        f.write(content)
    
    print(f'FIXED: {fname}')
    fixed += 1

print(f'\nDone. Fixed {fixed}/{len(PAGES)} pages.')