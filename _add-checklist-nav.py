#!/usr/bin/env python3
"""Add checklist PDF link to nav on all pages."""
import os, re

files_to_update = []
for f in os.listdir('.'):
    if f.endswith('.html') and f not in ['ai-fatigue-recovery-checklist-pdf.html', '404.html', 'index-hn.html', 'hn-visitor-guide.html', 'launch-command-center.html']:
        files_to_update.append(f)

added = 0
for filename in sorted(files_to_update):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the nav-cta link and add checklist before it
    # Pattern: <a href="...quiz..." class="nav-cta">Take Quiz →</a>
    old = r'(<a href="[^"]*ai-fatigue-checklist[^"]*" class="nav-cta">[^<]*</a>\s*</div>)'
    # Check if already added
    if 'ai-fatigue-recovery-checklist-pdf.html' in content and 'nav-cta' in content:
        print(f'SKIP {filename} — already has checklist nav')
        continue

    # Add before the quiz nav-cta
    new_nav_entry = '<a href="ai-fatigue-recovery-checklist-pdf.html" class="nav-cta">📄 Checklists</a>\n    '
    # Find the first nav-cta and insert before it
    match = re.search(r'(<a href="[^"]*#quiz[^"]*" class="nav-cta">)', content)
    if match:
        content = content[:match.start()] + new_nav_entry + content[match.start():]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'ADDED {filename}')
        added += 1
    else:
        # Check if nav exists and add at end of nav-links
        old_pattern = r'(<div class="nav-links">[\s\S]*?)(</div>\s*</nav>)'
        m = re.search(old_pattern, content)
        if m:
            nav_content = m.group(1)
            # append before </div>
            content = content[:m.start(1)] + nav_content + new_nav_entry + content[m.start(2):]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'ADDED (append) {filename}')
            added += 1
        else:
            print(f'WARN could not find nav in {filename}')

print(f'\nTotal updated: {added}/{len(files_to_update)}')