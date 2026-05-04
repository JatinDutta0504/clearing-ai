#!/usr/bin/env python3
"""Phase 3 Internal Linking Sprint — Hour 687
Fix internal links on pages with <10 internal links + general linking audit
"""
import re, os

SITE = "/Users/nightcoder/Desktop/TheClearing"

# Pages needing internal link fixes (fewest first)
WEAK_PAGES = {
    "newsletter-outreach-dashboard.html": {
        "current_links": ["ai-fatigue-quick-start.html", "quiz.html", "recovery.html"],
        "needed": ["why.html", "tips.html", "compare.html", "stories.html", "mental-health.html", "newsletter.html", "resources.html", "glossary.html"],
        "context": "before closing </section> or before explore grid"
    },
    "hn-subscribe.html": {
        "current_links": ["ai-fatigue-quick-start.html", "quiz.html", "recovery.html"],
        "needed": ["why.html", "tips.html", "compare.html", "stories.html", "mental-health.html", "newsletter.html", "resources.html", "manifesto.html"],
        "context": "before closing </section> or explore section"
    },
    "r-programming-llm-ban-what-it-means-for-engineers.html": {
        "current_links": ["/r-programming-llm-ban-what-it-means-for-engineers.html", "ai-skeptic-engineer.html", "ai-skeptic-guide.html", "first-year-engineer-ai-fatigue.html", "skill-atrophy.html", "the-ai-dependency-trap.html"],
        "needed": ["ai-productivity-paradox.html", "compare.html", "recovery.html", "research.html", "cognitive-load.html", "manifesto.html"],
        "context": "after first paragraph or before FAQ"
    },
    "ai-learning-burnout.html": {
        "current_links": ["ai-productivity-paradox.html", "ai-tool-overload.html", "cognitive-load.html", "first-year-engineer-ai-fatigue.html", "imposter-syndrome-ai.html", "recovery.html", "skill-atrophy.html", "tutorial-paradox.html"],
        "needed": ["tips.html", "compare.html", "mindset.html", "glossary.html", "no-ai-block.html", "daily-ai-boundaries.html", "ai-detox-plan.html", "manifesto.html"],
        "context": "before the FAQ section"
    },
    "ai-skeptic-engineer.html": {
        "current_links": ["ai-productivity-paradox.html", "compare.html", "first-year-engineer-ai-fatigue.html", "manifesto.html", "no-ai-block.html", "recovery.html", "research.html", "skill-atrophy.html"],
        "needed": ["tips.html", "glossary.html", "mindset.html", "why.html", "stories.html", "community.html", "hiring.html"],
        "context": "before FAQ accordion"
    },
    "daily-ai-boundaries.html": {
        "current_links": ["ai-detox-plan.html", "attention-residue.html", "cognitive-load.html", "decompress.html", "mindset.html", "recovery.html", "skill-atrophy.html", "team-guide.html", "the-explanation-requirement.html"],
        "needed": ["tips.html", "why.html", "compare.html", "stories.html", "mental-health.html", "manifesto.html", "no-ai-block.html"],
        "context": "before closing section or checklist"
    },
    "tech-layoffs-ai-era.html": {
        "current_links": ["developer-burnout-2025.html", "developer-identity.html", "imposter-syndrome-vs-ai-fatigue.html", "quiz.html", "recovery.html", "skill-atrophy.html", "software-engineer-mental-health.html", "tech-layoffs-ai-era.html"],
        "needed": ["hiring.html", "workplace.html", "mental-health.html", "community.html", "why.html", "tips.html", "stories.html"],
        "context": "before FAQ or conclusion section"
    },
    "the-productivity-gap.html": {
        "current_links": ["ai-productivity-paradox.html", "daily-practice.html", "quiz.html", "recovery.html", "research.html", "skill-atrophy.html", "tips.html", "vibe-coding-rules.html"],
        "needed": ["compare.html", "mindset.html", "glossary.html", "why.html", "stories.html", "manifesto.html", "attention-residue.html", "flow-state.html"],
        "context": "before FAQ section"
    },
}

print("=== Phase 3 Internal Linking Sprint — Hour 687 ===")
print()

changes = []
for filename, info in WEAK_PAGES.items():
    filepath = os.path.join(SITE, filename)
    if not os.path.exists(filepath):
        print(f"❌ {filename}: FILE NOT FOUND")
        continue
    
    with open(filepath) as f:
        content = f.read()
    
    # Find explore/continue/footer sections to inject links
    # Strategy: add links before the FAQ accordion or in a "Continue reading" block
    needed = info["needed"]
    current = info["current_links"]
    
    # Find where to inject — look for explore grid, FAQ, or end of article body
    explore_pattern = r'(<div class="explore-grid".*?</div>\s*</section>)'
    faq_pattern = r'(<div class="faq-accordion".*?</div>\s*</section>)'
    
    # Build link injection HTML
    links_html = ""
    for link in needed[:6]:  # Add max 6 new links
        if link not in content:  # Only add if not already there
            label = link.replace(".html", "").replace("-", " ").title()
            links_html += f'          <a href="{link}" class="explore-card">Explore: {label}</a>\n'
    
    if links_html:
        # Try to inject before FAQ or explore section
        faq_match = re.search(faq_pattern, content, re.DOTALL)
        explore_match = re.search(explore_pattern, content, re.DOTALL)
        
        if faq_match:
            injection_point = faq_match.start()
            new_content = content[:injection_point] + f'''
          <section class="article-section">
            <h2>Continue Reading</h2>
            <div class="grid-3col">
{links_html}            </div>
          </section>

''' + content[injection_point:]
        elif explore_match:
            injection_point = explore_match.start()
            new_content = content[:injection_point] + f'''
          <section class="article-section">
            <h2>Continue Reading</h2>
            <div class="grid-3col">
{links_html}            </div>
          </section>

''' + content[injection_point:]
        else:
            # Just inject before closing article-body
            new_content = content.replace("</div>\n</div>\n</article>", 
                f'''<div class="explore-grid">
{links_html}            </div>
          </div>
        </div>
        </article>''')
        
        if new_content != content:
            with open(filepath, "w") as f:
                f.write(new_content)
            changes.append(filename)
            print(f"✅ {filename}: Added {len(needed[:6])} links")
        else:
            print(f"⚠️  {filename}: No injection point found")
    else:
        print(f"⏭️  {filename}: All needed links already present")

print()
print(f"=== Summary: {len(changes)} pages updated ===")
for c in changes:
    print(f"  ✅ {c}")
