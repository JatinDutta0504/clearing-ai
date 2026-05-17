# 🚨 FORM SCRIPT READY — RUN THIS NOW

## STATUS: READY TO ACTIVATE

Sunny — the script is ready. You just need to do 3 things:

---

## STEP 1: Get Your Formspree Form ID (2 minutes)

1. Go to **[formspree.io](https://formspree.io)** → Sign in
2. Click **"+ New Form"** → Name it "The Dispatch"
3. Confirm your email (Formspree sends confirmation email — click it)
4. Your form URL is: `https://formspree.io/f/YOUR_FORM_ID`
5. Copy the form ID (the part after `/f/` — e.g., `xyzabc123`)

---

## STEP 2: Edit the Script (30 seconds)

Open: `_activate-formspree.py`

Change line 15:
```python
FORM_ID = "YOUR_FORM_ID"  # <-- REPLACE THIS
```

To:
```python
FORM_ID = "xyzabc123"  # <-- YOUR actual ID from step above
```

---

## STEP 3: Run the Script (10 seconds)

```bash
cd ~/Desktop/TheClearing
python _activate-formspree.py
```

The script will:
- ✅ Replace YOUR_FORM_ID with your real ID in all 73 files
- ✅ Verify the activation worked
- ✅ Show you exactly which files were updated

---

## STEP 4: Verify It Works (1 minute)

1. Open: `https://clearing-ai.com/subscribe.html`
2. Enter a test email (use a real one you can check)
3. Click Subscribe
4. You should see "You're in." success message
5. Check your inbox — you should receive a Formspree submission email

---

## WHAT THIS FIXES

After activation, all newsletter forms across the site will capture real email addresses:

| Page | Current | After |
|------|---------|-------|
| subscribe.html | ❌ broken | ✅ working |
| newsletter.html | ❌ broken | ✅ working |
| email-course.html | ❌ broken | ✅ working |
| ai-fatigue-checklist.html | ❌ broken | ✅ working |
| testimonials.html | ❌ broken | ✅ working |
| community-hub.html | ❌ broken | ✅ working |
| share-your-story.html | ❌ broken | ✅ working |
| **Total** | **73 pages** | **All working** |

---

## WHY THIS MATTERS

- Newsletter subscribers = owned audience (not borrowed from Twitter/Reddit)
- Email capture from high-intent visitors (quiz completers, recovery page visitors)
- The Dispatch (weekly email) is ready to send — 50+ issues written
- Email course (5-day) is ready to deliver — content exists
- **Right now: 0 subscribers captured. This fixes that.**

---

## QUICK COMMAND REFERENCE

```bash
# Edit the form ID
nano ~/Desktop/TheClearing/_activate-formspree.py

# Run activation
python ~/Desktop/TheClearing/_activate-formspree.py

# Test subscribe page
open https://clearing-ai.com/subscribe.html

# Check formspree submissions
open https://formspree.io/dashboard
```

---

## IF YOU RUN INTO ISSUES

**"Formspree account doesn't exist"**
→ Create one at formspree.io (free, 3 min)

**"I already have a form but don't know the ID"**
→ Log in to formspree.io → Click your form → URL ends in /f/XXXXX

**"The script failed"**
→ Run manually:
```bash
grep -rl "YOUR_FORM_ID" ~/Desktop/TheClearing/*.html | wc -l
```
If it returns a number > 0, the placeholder is still there. Edit each file manually or re-run the script.

---

*Last updated: 2026-05-17 8:46 AM PDT*
*Script by: Jeez 🤙 for The Clearing*