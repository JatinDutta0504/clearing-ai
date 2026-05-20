#!/usr/bin/env python3
"""Replace YOUR_FORM_ID with xpwqqvln in all public HTML files."""
import os

site_dir = "/Users/nightcoder/Desktop/TheClearing"
replacements = 0

skip_dirs = {"_backup", "logs", "_cls-fix-backup", ".git", "email-course", "newsletter-outreach", "reddit-outreach", "reddit-posts", "twitter-threads", "linkedin", "newsletter-issues", "testimonials", "css", "js", "assets", "fonts"}

for filename in os.listdir(site_dir):
    if not filename.endswith(".html"):
        continue
    
    # Skip backup/utility directories
    skip = False
    for sd in skip_dirs:
        if sd in filename:
            skip = True
            break
    if skip:
        continue
    
    filepath = os.path.join(site_dir, filename)
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "YOUR_FORM_ID" not in content:
        continue
    
    new_content = content.replace("YOUR_FORM_ID", "xpwqqvln")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    count = content.count("YOUR_FORM_ID")
    replacements += count
    print(f"Fixed {filename}: {count} replacement(s)")

print(f"\nTotal replacements: {replacements}")