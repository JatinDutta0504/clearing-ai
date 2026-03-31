#!/usr/bin/env python3
"""Fix nav corruption in newsletter.html — floating li elements, duplicate links, improper nesting."""

path = "/Users/nightcoder/Desktop/TheClearing/newsletter.html"
with open(path) as f:
    content = f.read()

# The nav section we want to rebuild (from line ~470 to ~600 area)
# Let's identify the broken sections and fix them

# FIX 1: The "Why" dropdown has floating li elements between ai-learning-burnout and research
# Lines around 536-543 have broken structure
old_why_dropdown_fragment = '''            <li><a href="ai-tool-overload.html">Tool Overload</a></li>
            <li><a href="ai-learning-burnout.html">AI Learning Burnout</a></li>

                      <li><a href="research.html">The Science</a></li>
            <li><a href="stats.html">Statistics 2025</a></li>
            <li><a href="productivity-theater.html">Productivity Theater</a></li>
      <li><a href="flow-state.html">Flow State &amp; AI</a></li>
            <li><a href="attention-residue.html">Attention Residue</a></li>

            <li><a href="skill-atrophy.html">Skill Atrophy</a></li>
            <li><a href="cognitive-load.html">Cognitive Load</a></li>
            <li><a href="developer-identity.html">Developer Identity</a></li>
            <li><a href="automation-anxiety.html">Automation Anxiety</a></li>
            <li><a href="imposter-syndrome-vs-ai-fatigue.html">Imposter Syndrome</a></li>
            <li><a href="imposter-syndrome-ai.html">Imposter Syndrome & AI</a></li>'''

new_why_dropdown = '''            <li><a href="ai-tool-overload.html">Tool Overload</a></li>
            <li><a href="ai-learning-burnout.html">AI Learning Burnout</a></li>
            <li><a href="research.html">The Science</a></li>
            <li><a href="stats.html">Statistics 2025</a></li>
            <li><a href="productivity-theater.html">Productivity Theater</a></li>
            <li><a href="flow-state.html">Flow State &amp; AI</a></li>
            <li><a href="attention-residue.html">Attention Residue</a></li>
            <li><a href="skill-atrophy.html">Skill Atrophy</a></li>
            <li><a href="cognitive-load.html">Cognitive Load</a></li>
            <li><a href="developer-identity.html">Developer Identity</a></li>
            <li><a href="automation-anxiety.html">Automation Anxiety</a></li>
            <li><a href="imposter-syndrome-vs-ai-fatigue.html">Imposter Syndrome</a></li>
            <li><a href="imposter-syndrome-ai.html">Imposter Syndrome & AI</a></li>'''

content = content.replace(old_why_dropdown_fragment, new_why_dropdown)

# FIX 2: The "Heal" dropdown has </li></li> and duplicate/corrupt entries
old_heal_dropdown_fragment = '''            <li><a href="recovery.html">Recovery Guide</a></li>
            <li><a href="software-engineer-mental-health.html">Mental Health</a></li></li>
<li><a href="mental-health.html">Mental Health</a></li>
            <li><a href="developer-wellbeing.html">Wellbeing</a></li>
      <li><a href="flow-state.html">Flow State &amp; AI</a></li>
            <li><a href="attention-residue.html">Attention Residue</a></li>
            <li><a href="tips.html">Tips</a></li>
            <li><a href="mindset.html">Mindset</a></li>
            <li><a href="daily-practice.html">Daily Practice</a></li>
          <li><a href="ai-fatigue-checklist.html">30-Day Checklist</a></li>
            <li><a href="ai-detox-plan.html">30-Day Detox Plan</a></li>
            <li><a href="team-guide.html">For Managers</a></li>
            <li><a href="hiring.html">Hiring &amp; Retention</a></li>
            <li><a href="corporate-ai-wellness.html">Corporate Wellness</a>
      <a href="daily-ai-boundaries.html">Daily AI Boundaries</a></li>
            <li><a href="team-manager-guide.html">For Managers</a></li>
            <li><a href="workplace.html">Workplace</a></li>'''

new_heal_dropdown = '''            <li><a href="recovery.html">Recovery Guide</a></li>
            <li><a href="mental-health.html">Mental Health</a></li>
            <li><a href="developer-wellbeing.html">Wellbeing</a></li>
            <li><a href="tips.html">Tips</a></li>
            <li><a href="mindset.html">Mindset</a></li>
            <li><a href="daily-practice.html">Daily Practice</a></li>
            <li><a href="ai-fatigue-checklist.html">30-Day Checklist</a></li>
            <li><a href="ai-detox-plan.html">30-Day Detox Plan</a></li>
            <li><a href="team-guide.html">For Managers</a></li>
            <li><a href="hiring.html">Hiring &amp; Retention</a></li>
            <li><a href="corporate-ai-wellness.html">Corporate Wellness</a></li>
            <li><a href="daily-ai-boundaries.html">Daily AI Boundaries</a></li>
            <li><a href="team-manager-guide.html">Team Manager Guide</a></li>
            <li><a href="workplace.html">Workplace</a></li>'''

content = content.replace(old_heal_dropdown_fragment, new_heal_dropdown)

# FIX 3: Stories dropdown duplicate/corrupt entries
old_stories_fragment = '''            <li><a href="stories.html">Engineer Stories</a></li>
            <li><a href="engineer-types.html">Your Type</a></li>
                  <li><a href="junior-engineers.html">For Juniors</a></li>
      <li><a href="senior-identity.html">Senior Identity</a></li>
            
            <li><a href="community.html">Community</a></li><li><a href="senior-identity.html">Senior Identity</a></li>
            
            <li><a href="community.html">Community</a></li><li><a href="glossary.html">Glossary</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="testimonials.html">Testimonials</a></li>'''

new_stories_fragment = '''            <li><a href="stories.html">Engineer Stories</a></li>
            <li><a href="engineer-types.html">Your Type</a></li>
            <li><a href="junior-engineers.html">For Juniors</a></li>
            <li><a href="senior-identity.html">Senior Identity</a></li>
            <li><a href="community.html">Community</a></li>
            <li><a href="testimonials.html">Testimonials</a></li>'''

content = content.replace(old_stories_fragment, new_stories_fragment)

# FIX 4: "Read" dropdown has floating li for quiz results tiers
old_read_fragment = '''            <li><a href="resources.html">Resources</a></li>
            <li><a href="newsletter.html">Newsletter</a></li>
            <li><a href="quiz-results.html">Quiz Results</a></li>          <li><a href="quiz-results-tier-4.html">Tier 4 Results</a></li>
          <li><a href="quiz-results-tier-3.html">Tier 3 Results</a></li>

            <li><a href="press-kit.html">Press Kit</a></li>
            <li><a href="changelog.html">Changelog</a></li>'''

new_read_fragment = '''            <li><a href="resources.html">Resources</a></li>
            <li><a href="newsletter.html">Newsletter</a></li>
            <li><a href="quiz-results.html">Quiz Results</a></li>
            <li><a href="quiz-results-tier-4.html">Tier 4 Results</a></li>
            <li><a href="quiz-results-tier-3.html">Tier 3 Results</a></li>
            <li><a href="press-kit.html">Press Kit</a></li>
            <li><a href="changelog.html">Changelog</a></li>'''

content = content.replace(old_read_fragment, new_read_fragment)

with open(path, "w") as f:
    f.write(content)

print("✅ newsletter.html nav fixed")
