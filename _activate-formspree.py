#!/usr/bin/env python3
"""
Formspree Activation Script — The Clearing
Replaces YOUR_FORM_ID placeholder with actual Formspree form ID.

HOW TO USE:
1. First, create your form at formspree.io and get your Form ID (the part after /f/)
2. Edit this file: set FORM_ID = "your_actual_form_id" below
3. Run: python _activate-formspree.py
4. Test: open subscribe.html → submit test email → check your inbox

AUTHOR: Jeez 🤙 for The Clearing
DATE: 2026-05-17
"""

import os
import re
import glob

# ============================================================
# STEP 1: SET YOUR FORM ID HERE
# ============================================================
FORM_ID = "YOUR_FORM_ID"  # <-- REPLACE THIS with your actual Formspree form ID
                    # e.g., "xyzabc123" if your form URL is formspree.io/f/xyzabc123

# ============================================================
# STEP 2: VERIFY FORM ID IS SET
# ============================================================
if FORM_ID == "YOUR_FORM_ID":
    print("❌ ERROR: You must set your Form ID first!")
    print("   Edit this file and replace YOUR_FORM_ID with your actual formspree.io form ID.")
    print("   Get it from: https://formspree.io → Forms → Your form → URL ends with /f/XXXXX")
    exit(1)

FORMSPREE_URL = f"https://formspree.io/f/{FORM_ID}"

# ============================================================
# STEP 3: FIND ALL FILES WITH YOUR_FORM_ID
# ============================================================
site_root = os.path.dirname(os.path.abspath(__file__))
html_files = glob.glob(os.path.join(site_root, "*.html"))
files_to_update = []
for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if 'YOUR_FORM_ID' in content:
            files_to_update.append(f)
    except:
        pass

print(f"\n🌿 THE CLEARING — Formspree Activation")
print(f"   Form ID: {FORM_ID}")
print(f"   URL: {FORMSPREE_URL}")
print(f"   Files to update: {len(files_to_update)}\n")

# ============================================================
# STEP 4: REPLACE IN ALL FILES
# ============================================================
for filepath in sorted(files_to_update):
    try:
        with open(filepath, 'r', encoding='utf-8') as fh:
            content = fh.read()
        
        original = content
        content = content.replace('YOUR_FORM_ID', FORM_ID)
        
        # Count replacements
        count = original.count('YOUR_FORM_ID')
        
        with open(filepath, 'w', encoding='utf-8') as fh:
            fh.write(content)
        
        rel_path = os.path.relpath(filepath, site_root)
        print(f"   ✅ {rel_path} — {count} replacement(s)")
    except Exception as e:
        print(f"   ❌ Failed: {filepath} — {e}")

# ============================================================
# STEP 5: VERIFY
# ============================================================
print("\n🔍 Verification...")

# Check subscribe.html
subscribe_path = os.path.join(site_root, "subscribe.html")
if os.path.exists(subscribe_path):
    with open(subscribe_path, 'r', encoding='utf-8') as fh:
        content = fh.read()
    if FORM_ID in content and 'YOUR_FORM_ID' not in content:
        print(f"   ✅ subscribe.html — formspree.io/f/{FORM_ID} active")
    elif 'YOUR_FORM_ID' in content:
        print(f"   ❌ subscribe.html — YOUR_FORM_ID still present")
    else:
        print(f"   ❌ subscribe.html — form not found")

# Check newsletter.html
newsletter_path = os.path.join(site_root, "newsletter.html")
if os.path.exists(newsletter_path):
    with open(newsletter_path, 'r', encoding='utf-8') as fh:
        content = fh.read()
    if FORM_ID in content and 'YOUR_FORM_ID' not in content:
        print(f"   ✅ newsletter.html — formspree.io/f/{FORM_ID} active")
    elif 'YOUR_FORM_ID' in content:
        print(f"   ❌ newsletter.html — YOUR_FORM_ID still present")
    else:
        print(f"   ❌ newsletter.html — form not found")

# Count remaining YOUR_FORM_ID
remaining = 0
for f in glob.glob(os.path.join(site_root, "*.html")):
    with open(f, 'r', encoding='utf-8') as fh:
        if 'YOUR_FORM_ID' in fh.read():
            remaining += 1

if remaining == 0:
    print(f"\n   🎉 All forms activated! {len(files_to_update)} files updated.")
else:
    print(f"\n   ⚠️  {remaining} files still contain YOUR_FORM_ID — run script again or fix manually")

print(f"\n📋 NEXT STEPS:")
print(f"   1. Open https://formspree.io/dashboard → your form → Settings")
print(f"   2. Set redirect URL: https://clearing-ai.com/subscribe.html?subscribed=1")
print(f"   3. Set notification email: your email address")
print(f"   4. Test: visit clearing-ai.com/subscribe.html → submit test email")
print(f"   5. Check your inbox for Formspree confirmation + submission")
print(f"\n   Live at: https://clearing-ai.com")