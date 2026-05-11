#!/usr/bin/env python3
"""Fix nav/footer on pages that lost them during rebase/overwrite."""
import os
import re
import shutil

# Pages that need nav/footer restoration
pages_to_fix = [
    'first-year-engineer-ai-fatigue.html',
]

# Pages that should receive full nav
all_pages = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f)]

for target in pages_to_fix:
    if target not in all_pages:
        print(f"SKIP {target} — not found")
        continue
    
    with open(target) as f:
        content = f.read()
    
    original = content
    
    # Check if it already has proper nav structure
    has_nav = '<nav' in content or 'dropdown-menu' in content
    has_footer = '<footer>' in content
    
    if has_nav and has_footer:
        print(f"OK   {target} — already has nav + footer")
        continue
    
    print(f"FIX  {target} — adding nav/footer (nav={has_nav}, footer={has_footer})")
    
    # Get a reference page with proper nav (recovery.html)
    ref = 'recovery.html'
    if not os.path.exists(ref):
        # Find another reference
        for p in ['index.html', 'why.html', 'ai-fatigue.html']:
            if os.path.exists(p):
                ref = p
                break
    
    with open(ref) as f:
        ref_content = f.read()
    
    # Find the nav block in reference
    nav_match = re.search(r'(<!-- nav start -->.*?<!-- nav end -->)', ref_content, re.DOTALL)
    footer_match = re.search(r'(<!-- footer start -->.*?<!-- footer end -->)', ref_content, re.DOTALL)
    
    if not nav_match or not footer_match:
        # Try simpler approach — find the nav tag block
        nav_match = re.search(r'(<nav.*?</nav>)', ref_content, re.DOTALL)
        footer_match = re.search(r'(<footer.*?</footer>)', ref_content, re.DOTALL)
    
    # Extract critical CSS/style links
    css_links = re.findall(r'<link rel="stylesheet" href="([^"]+)"', ref_content)
    script_links = re.findall(r'<script src="([^"]+)"', ref_content)
    preconnects = re.findall(r'<link rel="preconnect"[^>]+>', ref_content)
    
    # Build new content
    # 1. Add missing CSS/preconnect to head
    for css in css_links:
        if css not in content:
            content = content.replace('</title>', f'\n  <link rel="stylesheet" href="{css}">\n</title>')
    
    for pc in preconnects[:3]:  # Limit
        if pc not in content:
            content = content.replace('</title>', f'\n  {pc}\n</title>')
    
    # 2. Add missing scripts before </body>
    for scr in script_links:
        if scr not in content and 'main.js' in scr:
            content = content.replace('</body>', f'  <script src="{scr}"></script>\n</body>')
    
    # 3. Add nav before <main> if missing
    if not has_nav and nav_match:
        nav_block = '\n' + nav_match.group(1) + '\n'
        content = content.replace('<main', nav_block + '<main')
    
    # 4. Add footer if missing
    if not has_footer and footer_match:
        footer_block = '\n' + footer_match.group(1) + '\n'
        content = content.replace('</body>', footer_block + '</body>')
    
    # Also add theme toggle script
    if 'main.js' in content and 'theme-toggle' not in content:
        content = content.replace('</body>', '<script src="js/main.js"></script>\n</body>')
    
    with open(target, 'w') as f:
        f.write(content)
    
    print(f"     → Fixed {target}")