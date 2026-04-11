#!/bin/bash
# Formspree Setup Guide for The Clearing Newsletter
# Run AFTER creating a Formspree account and form

# ============================================================
# STEP 1: Create Formspree Account
# ============================================================
# 1. Go to https://formspree.io
# 2. Click "Get Started" — sign up with GitHub or email
# 3. Create a new form named "Newsletter Subscribers"
# 4. Formspree will give you a form ID like: https://formspree.io/f/xpwqgvln
# 5. Your form ID is the part AFTER /f/ — e.g. "xpwqgvln"
#
# FREE PLAN: 50 submissions/month
# If we need more, upgrade to Pro at formspree.io/pricing
#
# ============================================================
# STEP 2: Replace YOUR_FORM_ID in all files
# ============================================================
# Replace YOUR_FORM_ID with your actual form ID
# The form ID looks like: xpwqgvln (letters+numbers)

# Files that need updating:
FILES=(
  "newsletter.html"
  "newsletter-thank-you.html"
  "ai-fatigue-checklist.html"
  "community-hub.html"
  "index-hn.html"
  "testimonials.html"
  "share-your-story.html"
)

# Run this sed command AFTER you have your form ID:
# Replace YOUR_FORM_ID with your actual ID, e.g.:
# sed -i '' 's/YOUR_FORM_ID/xpwqgvln/g' newsletter.html
# etc.

# Or use Python for all files at once (see below)
# ============================================================
# STEP 3: Verify Setup
# ============================================================
# 1. Go to https://clearing-ai.com/newsletter.html
# 2. Fill out the form and submit
# 3. Check your Formspree dashboard — should see the submission
# 4. Check email — should receive notification of new subscriber

# ============================================================
# AUTOMATED REPLACEMENT (run after getting your form ID)
# ============================================================
# Save this as a Python script and run it:

# --- cut here ---
'''
#!/usr/bin/env python3
import os
import re

FORM_ID = "YOUR_FORM_ID"  # <-- PUT YOUR FORM ID HERE

files_to_update = [
    "newsletter.html",
    "newsletter-thank-you.html", 
    "ai-fatigue-checklist.html",
    "community-hub.html",
    "index-hn.html",
    "testimonials.html",
    "share-your-story.html",
]

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"SKIP: {filename} not found")
        continue
    with open(filename, 'r') as f:
        content = f.read()
    if 'YOUR_FORM_ID' in content:
        new_content = content.replace('YOUR_FORM_ID', FORM_ID)
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"UPDATED: {filename}")
    else:
        print(f"OK: {filename} (no placeholder found)")

print("\nAll done! Test the form at newsletter.html")
'''
# --- cut here ---

# ============================================================
# FORM ENDPOINT DETAILS
# ============================================================
# Newsletter form endpoint:
# https://formspree.io/f/{FORM_ID}
# Method: POST
# Content-Type: application/json (Formspree JSON submissions)
#
# Hidden fields used:
# _subject: "New Dispatch subscriber 🌿"
# _next: https://clearing-ai.com/newsletter-thank-you
# _format: json
#
# Formspree dashboard: https://formspree.io/dashboard
# ============================================================

echo "Formspree Setup Guide"
echo "====================="
echo ""
echo "1. Create account: https://formspree.io"
echo "2. Get your form ID (e.g. xpwqgvln)"
echo "3. Edit the FORM_ID variable in this script"
echo "4. Run: python3 _setup-formspree.py"
echo ""
echo "Once set up, test at: https://clearing-ai.com/newsletter.html"
