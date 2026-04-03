#!/usr/bin/env python3
"""Integrate 4 missing pages into sitemap.xml + nav/footer on all HTML pages."""

import re, os,glob

SITE = "/Users/nightcoder/Desktop/TheClearing"
NEW_PAGES = [
    {"file": "ai-skeptic-guide.html", "priority": "0.85", "changefreq": "monthly",
     "nav_dropdown": "Why",
     "nav_after": "ai-productivity-paradox.html",
     "nav_text": "AI Skeptic's Guide"},
    {"file": "share-your-story.html", "priority": "0.75", "changefreq": "monthly",
     "nav_dropdown": "Stories",
     "nav_after": "testimonials.html",
     "nav_text": "Share Your Story"},
    {"file": "sleep-and-ai-fatigue.html", "priority": "0.85", "changefreq": "monthly",
     "nav_dropdown": "Heal",
     "nav_after": "recovery.html",
     "nav_text": "Sleep & AI Fatigue"},
    {"file": "developer-burnout-recovery.html", "priority": "0.90", "changefreq": "weekly",
     "nav_dropdown": "Heal",
     "nav_after": "executive-burnout.html",
     "nav_text": "Burnout Recovery Guide"},
]

def add_to_sitemap():
    """Add missing pages to sitemap.xml."""
    sitemap_path = os.path.join(SITE, "sitemap.xml")
    with open(sitemap_path) as f:
        content = f.read()
    
    today = "2026-04-03"
    insertions = 0
    
    for page in NEW_PAGES:
        url_block = f"""
  <url>
    <loc>https://clearing-ai.com/{page['file']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>
"""
        # Insert before </urlset>
        if f"<loc>https://clearing-ai.com/{page['file']}</loc>" not in content:
            content = content.replace("</urlset>", url_block + "</urlset>")
            insertions += 1
            print(f"  + {page['file']} added to sitemap")
        else:
            print(f"  ~ {page['file']} already in sitemap")
    
    with open(sitemap_path, "w") as f:
        f.write(content)
    
    # Update lastmod for ai-productivity-paradox if it exists (needs lastmod)
    if 'lastmod' not in open(sitemap_path).read():
        pass  # already has it
    
    print(f"  Sitemap updated: {insertions} pages added")
    return insertions

def add_to_nav_dropdown(html_content, dropdown_name, after_file, new_file, nav_text):
    """Add a nav link to the specified dropdown after the given file."""
    
    # Find the Stories dropdown and add after testimonials
    if dropdown_name == "Stories":
        pattern = r'(<li><a href="testimonials\.html">[^<]+</a></li>)'
        replacement = r'\1\n            <li><a href="' + new_file + '">' + nav_text + r'</a></li>'
    elif dropdown_name == "Heal":
        if "sleep" in new_file:
            pattern = r'(<li><a href="recovery\.html">[^<]+</a></li>)'
            replacement = r'\1\n            <li><a href="' + new_file + '">' + nav_text + r'</a></li>'
        elif "burnout-recovery" in new_file:
            pattern = r'(<li><a href="executive-burnout\.html">[^<]+</a></li>)'
            replacement = r'\1\n            <li><a href="' + new_file + '">' + nav_text + r'</a></li>'
        else:
            return html_content
    elif dropdown_name == "Why":
        pattern = r'(<li><a href="ai-productivity-paradox\.html">[^<]+</a></li>)'
        replacement = r'\1\n            <li><a href="' + new_file + '">' + nav_text + r'</a></li>'
    else:
        return html_content
    
    new_content = re.sub(pattern, replacement, html_content, count=1)
    if new_content != html_content:
        print(f"    + {new_file} added to {dropdown_name} dropdown")
    else:
        print(f"    ! {new_file} NOT added to {dropdown_name} dropdown (pattern not found)")
    return new_content

def add_to_footer(html_content, new_file, nav_text):
    """Add link to footer resources section."""
    # Add after testimonials in footer if present
    if 'testimonials.html' in html_content:
        # Find testimonials footer link and add new link after it
        pattern = r'(<li><a href="testimonials\.html">[^<]+</a></li>)'
        replacement = r'\1\n        <li><a href="' + new_file + '">' + nav_text + '</a></li>'
        new_content = re.sub(pattern, replacement, html_content, count=1)
        if new_content != html_content:
            print(f"    + {new_file} added to footer")
            return new_content
    return html_content

def process_all_pages():
    """Add new pages to nav and footer on all HTML files."""
    html_files = glob.glob(os.path.join(SITE, "*.html"))
    # Exclude partial files
    html_files = [f for f in html_files if not os.path.basename(f).startswith("_")]
    
    updated = 0
    for html_path in html_files:
        filename = os.path.basename(html_path)
        
        # Check which new pages are missing from this file
        for page in NEW_PAGES:
            new_file = page["file"]
            nav_text = page["nav_text"]
            dropdown = page["nav_dropdown"]
            after_file = page.get("nav_after", "")
            
            with open(html_path) as f:
                content = f.read()
            
            modified = False
            
            # Add to nav dropdown if not already there
            if new_file not in content:
                if dropdown == "Stories" and "Stories" in content:
                    content = add_to_nav_dropdown(content, dropdown, after_file, new_file, nav_text)
                    modified = True
                elif dropdown == "Heal" and "Heal" in content:
                    content = add_to_nav_dropdown(content, dropdown, after_file, new_file, nav_text)
                    modified = True
                elif dropdown == "Why" and "Why" in content:
                    content = add_to_nav_dropdown(content, dropdown, after_file, new_file, nav_text)
                    modified = True
            
            # Add to footer if not already there
            if new_file not in content:
                content = add_to_footer(content, new_file, nav_text)
                modified = True
            
            if modified:
                with open(html_path, "w") as f:
                    f.write(content)
                updated += 1
    
    print(f"\n  Updated {updated} files")
    return updated

if __name__ == "__main__":
    print("=== SITEMAP UPDATE ===")
    add_to_sitemap()
    print("\n=== NAV/FOOTER UPDATE ===")
    process_all_pages()
    print("\nDone!")
