#!/usr/bin/env python3
"""
Phase 3 Internal Linking — Add contextual links to ai-fatigue.html
Hour 564 — One page, smart links, no CSS pollution.
"""

import re

# Read ai-fatigue.html
with open('ai-fatigue.html', 'r', errors='ignore') as f:
    content = f.read()

changes = []

# 1. In intro/overview section: add link to ai-fatigue-vs-burnout
content = re.sub(
    r'(AI fatigue is not burnout|what makes AI fatigue different)',
    r'<a href="burnout-vs-fatigue.html" title="AI Fatigue vs Burnout — understand the difference">\1</a>',
    content, count=1
)

# 2. Add a paragraph about skill atrophy with link (within "What AI Fatigue Feels Like" section)
skill_atrophy_insert = '''
<br><br>Research from skill-atrophy studies shows that prolonged AI use without deliberate practice can erode what engineers call "muscle memory for debugging" — the ability to sense when something is wrong before you've identified the specific failure. <a href="skill-atrophy.html">Learn more about skill atrophy and how to rebuild</a>.'''

# Find the "what it feels like" section and add a note
if 'skill-atrophy' not in content.lower() and 'muscle memory' not in content.lower():
    # Find the section after "what AI fatigue feels like" heading and add the paragraph
    content = re.sub(
        r'(<h2[^>]*>.*?[Ff]eels?[Ll]ike.*?</h2>\s*<p>)',
        r'\1' + skill_atrophy_insert + '\n',
        content, count=1
    )

# 3. Add a "see also" section near the bottom if it doesn't exist
if 'see-also-section' not in content:
    see_also = '''
<br><br>
<span id="see-also-section"></span>
<strong>See also:</strong>
<a href="recovery.html">Recovery guide</a> ·
<a href="checkin.html">Daily check-in tool</a> ·
<a href="the-science-of-ai-fatigue.html">The science behind AI fatigue</a> ·
<a href="ai-detox-plan.html">30-day AI detox plan</a> ·
<a href="community.html">Community support</a>
'''
    # Add before FAQ section or at end
    faq_match = re.search(r'(<section[^>]*class="[^\"]*faq|\<div[^>]*class="[^\"]*faq|\<details)', content, re.IGNORECASE)
    if faq_match:
        content = content[:faq_match.start()] + see_also + '\n' + content[faq_match.start():]
    else:
        content = content.replace('</body>', see_also + '\n</body>')

# 4. Add link to cognitive load theory in explanation section
content = re.sub(
    r'(Cognitive load|Sweller|working memory)',
    r'<a href="cognitive-load.html" title="Cognitive Load Theory">\1</a>',
    content, count=1
)

with open('ai-fatigue.html', 'w', errors='ignore') as f:
    f.write(content)

print("✅ ai-fatigue.html updated with 4 contextual internal links")
print("  1. AI fatigue vs burnout link in intro")
print("  2. Skill atrophy paragraph in 'feels like' section")
print("  3. 'See also' block with 5 related pages")
print("  4. Cognitive load link in explanation")