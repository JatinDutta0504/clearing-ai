#!/usr/bin/env python3
"""Phase 3: Internal Linking Optimization
Add 3-5 contextual internal links to each of 7 pages with fewest internal links.
Target pages: ai-decision-stack, underrepresented-engineers, ai-learning-burnout,
              the-ai-dependency-trap, ai-skeptic-engineer, daily-ai-boundaries, data-engineer-ai-fatigue
"""

import re, os

# Define additions for each page:
# Each entry: (search_fragment, link_page, link_keyword)
ADDITIONS = {
    "ai-decision-stack.html": [
        # Layer 1: Cognitive Cost — link to attention-residue for context-switching
        ('<h3>Code review as a learning vector</h3>',
         'engineering-managers-ai-fatigue.html', 'For Engineering Managers'),
        # In the cognitive cost section, add attention-residue link
        ('<h3>Cognitive Cost</h3>',
         'attention-residue.html', 'Attention Residue'),
        # After "skill heterogeneity amplification" section
        ('<h3>Skill heterogeneity amplification</h3>',
         'the-ai-dependency-trap.html', 'AI Dependency Trap'),
        # In sustainability section
        ('<h2>Layer 4: Long-Term Sustainability</h2>',
         'developer-wellbeing.html', 'Developer Wellbeing'),
    ],
    "underrepresented-engineers-ai-fatigue.html": [
        # Add role-based link in intro/context section
        ('<h2>Continue Reading</h2>',
         'ai-fatigue-by-role.html', 'AI Fatigue by Role'),
        # Add engineering managers link
        ('<h2>Continue Reading</h2>',
         'engineering-managers-ai-fatigue.html', 'For Engineering Managers'),
        # Add hiring context
        ('<h2>Continue Reading</h2>',
         'hiring.html', 'Hiring in the AI Era'),
        # Add imposter syndrome link in relevant section
        ('<h2>Continue Reading</h2>',
         'imposter-syndrome-ai.html', 'Imposter Syndrome & AI'),
        # Add neurodivergent link — already in list, add hn-launch
        ('<h2>Continue Reading</h2>',
         'hn-launch.html', 'About The Clearing'),
    ],
    "ai-learning-burnout.html": [
        # In the learning burnout section, add first-year link
        ('<h2>The Junior Engineer\'s Special Problem</h2>',
         'first-year-engineer-ai-fatigue.html', 'First-Year Engineer AI Fatigue'),
        # In the sustainable learning protocol
        ('<h2>The Sustainable Learning Protocol</h2>',
         'ai-productivity-paradox.html', 'AI Productivity Paradox'),
        # In the learning guilt section
        ('<h2>The Guilt Work</h2>',
         'mindset.html', 'Mental Models for Healthy AI Use'),
        # In the acceleration section
        ('<h2>The Acceleration Problem</h2>',
         'attention-residue.html', 'Attention Residue'),
    ],
    "the-ai-dependency-trap.html": [
        # In the trap description section
        ('<h2>The AI Dependency Trap</h2>',
         'ai-productivity-paradox.html', 'AI Productivity Paradox'),
        # In skill erosion section
        ('<h2>',
         'skill-atrophy.html', 'Skill Atrophy Research'),
        # In the automation section
        ('<h2>',
         'automation-anxiety.html', 'Automation Anxiety'),
        # In the recovery section
        ('<h2>',
         'attention-residue.html', 'Attention Residue'),
    ],
    "ai-skeptic-engineer.html": [
        # In the intro section
        ('<h2>The AI Skeptic Engineer</h2>',
         'automation-anxiety.html', 'Automation Anxiety'),
        # In "what you might be wrong about"
         ('<h3>You might be wrong about:</h3>',
         'imposter-syndrome-ai.html', 'Imposter Syndrome vs AI Fatigue'),
        # In the skeptic who thrive section
        ('<h2>The Skeptics Who Are Thriving</h2>',
         'mindset.html', 'Mental Models for Healthy AI Use'),
        # In the "what to do with your skepticism" section
         ('<h2>What To Do With Your Skepticism</h2>',
         'no-ai-block.html', 'The No-AI Block'),
    ],
    "daily-ai-boundaries.html": [
        # In intro/context section
        ('<h2>',
         'recovery.html', 'AI Fatigue Recovery Guide'),
        # In practical section
        ('<h2>',
         'ai-detox-plan.html', '30-Day AI Detox Plan'),
        # Add mindset link
        ('<h2>',
         'mindset.html', 'Mental Models for Healthy AI Use'),
        # Add decompress
        ('<h2>',
         'decompress.html', 'Deep Work Timer'),
    ],
    "data-engineer-ai-fatigue.html": [
        # Add ai-tool-overload link
        ('<h2>',
         'ai-tool-overload.html', 'AI Tool Overload'),
        # Add inference-fatigue
        ('<h2>',
         'inference-fatigue.html', 'Inference Fatigue'),
        # Add flow-state
        ('<h2>',
         'flow-state.html', 'Flow State & AI'),
        # Add attention-residue
        ('<h2>',
         'attention-residue.html', 'Attention Residue'),
    ],
}

def make_link(html_page, link_target, keyword):
    return f'<a href="{link_target}">{keyword}</a>'

def add_links_to_page(fname, additions):
    filepath = fname
    content = open(filepath).read()
    lines = content.split('\n')
    additions_made = []
    
    for search_fragment, link_target, keyword in additions:
        # Find the line containing the search fragment
        idx = None
        for i, line in enumerate(lines):
            if search_fragment in line:
                idx = i
                break
        
        if idx is None:
            print(f"  WARNING: Could not find '{search_fragment[:50]}' in {fname}")
            continue
        
        # Find the paragraph after this heading to insert a link into
        # Look for the next <p> or <ul> after the heading index
        insert_after = None
        for i in range(idx, min(idx + 8, len(lines))):
            line = lines[i]
            # Skip the heading itself, empty lines, and divs
            if line.strip().startswith('<h') or line.strip().startswith('</div') or line.strip() == '' or line.strip().startswith('<!--'):
                continue
            if '<p>' in line or '<ul>' in line:
                insert_after = i
                break
        
        if insert_after is None:
            insert_after = idx + 1
        
        # Build the link text
        link_html = f' <a href="{link_target}">{keyword}</a>'
        
        # Insert into the paragraph line
        line = lines[insert_after]
        if '</p>' in line:
            # Insert before closing </p>
            new_line = line.replace('</p>', f'{link_html}</p>', 1)
        elif '</ul>' in line:
            new_line = line.replace('</ul>', f'{link_html}</ul>', 1)
        else:
            # Append at end of line
            new_line = line.rstrip() + link_html
        
        lines[insert_after] = new_line
        additions_made.append(f"  Added '{keyword}' -> {link_target} after line {insert_after+1}")
    
    new_content = '\n'.join(lines)
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return additions_made

def main():
    print("Phase 3: Internal Linking Optimization")
    print("=" * 50)
    
    for fname, additions in ADDITIONS.items():
        if not os.path.exists(fname):
            print(f"\nSKIPPING {fname} — file not found")
            continue
        
        print(f"\n>>> {fname}")
        results = add_links_to_page(fname, additions)
        for r in results:
            print(r)
        print(f"  Saved: {fname}")
    
    print("\n" + "=" * 50)
    print("Done.")

if __name__ == '__main__':
    main()
