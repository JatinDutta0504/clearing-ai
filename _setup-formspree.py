#!/usr/bin/env python3
"""
Formspree Setup Script for The Clearing
========================================

INSTRUCTIONS:
1. Create formspree.io account and new form
2. Get your form ID (the part after /f/ in your endpoint URL)
3. Replace YOUR_FORM_ID below with your actual form ID
4. Run: python3 _setup-formspree.py
5. Test at https://clearing-ai.com/newsletter.html

EXAMPLE:
If your Formspree form URL is: https://formspree.io/f/xpwqgvln
Then your FORM_ID = "xpwqgvln"
"""

import os
import re

# ==============================================================================
#  TODO: Replace this with your actual Formspree form ID
# ==============================================================================
FORM_ID = "YOUR_FORM_ID"  # <-- PUT YOUR FORM ID HERE

FILES_TO_UPDATE = [
    "newsletter.html",
    "newsletter-thank-you.html",
    "ai-fatigue-checklist.html",
    "community-hub.html",
    "index-hn.html",
    "testimonials.html",
    "share-your-story.html",
]

def update_formspree_form(filepath, form_id):
    """Replace YOUR_FORM_ID placeholder with actual form ID in a file."""
    if not os.path.exists(filepath):
        print(f"  SKIP: {filepath} (not found)")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'YOUR_FORM_ID' not in content:
        print(f"  OK:   {filepath} (no placeholder found)")
        return False
    
    if form_id == "YOUR_FORM_ID":
        print(f"  BLOCKED: {filepath} — FORM_ID still set to placeholder")
        return False
    
    new_content = content.replace('YOUR_FORM_ID', form_id)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  UPDATED: {filepath}")
    return True

def main():
    if FORM_ID == "YOUR_FORM_ID":
        print("ERROR: FORM_ID is still set to 'YOUR_FORM_ID'")
        print("Edit this script and replace FORM_ID with your actual Formspree form ID.")
        print("Get your form ID at: https://formspree.io/dashboard")
        return
    
    print(f"Replacing YOUR_FORM_ID → '{FORM_ID}' in {len(FILES_TO_UPDATE)} files...\n")
    
    updated = []
    for filepath in FILES_TO_UPDATE:
        if update_formspree_form(filepath, FORM_ID):
            updated.append(filepath)
    
    print(f"\nUpdated {len(updated)} files.")
    
    if updated:
        print("\nTest the form at: https://clearing-ai.com/newsletter.html")
        print("Submit a test email and check your Formspree dashboard.")
    else:
        print("\nNo files needed updating — either already configured or not found.")
    
    # Also update sitemap stats to reflect working form
    print("\nNOTE: After setup, update the 'hero-stats' on community-hub.html")
    print("      to say the newsletter is live (0 subscribers → growing).")

if __name__ == "__main__":
    main()
