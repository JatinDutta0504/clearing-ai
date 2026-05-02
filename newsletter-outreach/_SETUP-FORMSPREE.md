# The Clearing — Formspree Setup Guide
**Status:** CRITICAL — 14 files broken, 0 newsletter signups
**Fix time:** ~15 minutes
**Follow this guide exactly — no coding knowledge required**

---

## Why This Matters

Every HTML file with `YOUR_FORM_ID` has a broken newsletter signup form. Engineers can't subscribe. You've built 187 pages and 46 Dispatch issues but are losing subscribers at the form step.

---

## Step 1: Create Formspree Account

1. Go to **https://formspree.io**
2. Click **"Get Started"** → Sign up with **GitHub** (fastest)
3. Free plan = 50 submissions/month — enough for this project
4. Verify your email address

---

## Step 2: Create Your Form

1. In Formspree dashboard → Click **"New Form"**
2. Name it: `The Dispatch Signups`
3. You'll be taken to your form's **Settings** page
4. Look for **"Form ID"** or **"Endpoint"** — it looks like: `https://formspree.io/f/xyzabc123`
5. Copy the part after `/f/` — that's your **FORM_ID** (e.g. `xyzabc123`)

---

## Step 3: Find All Files That Need Updating

Run this command to see exactly which files:
```bash
cd ~/Desktop/TheClearing && grep -rn "YOUR_FORM_ID" *.html
```

**Expected files (14 total):**
```
ai-fatigue-checklist.html
ai-fatigue-quick-start.html
ai-weekly-audit.html
community-hub.html
email-course.html
for-hn-readers.html
freelance-engineer-ai-fatigue.html
hn-visitor-guide.html
linkedin.html
newsletter-outreach-dashboard.html
newsletter.html
recovery-toolkit.html
subscribe.html
testimonials.html
```

Also check:
```
hn-subscribe.html
newsletter.html
ai-fatigue-checklist.html (and 11 others above)
```

---

## Step 4: Replace YOUR_FORM_ID in All Files

**Option A: Find & Replace (Fastest)**

Open VS Code:
1. Press `Cmd + Shift + F` (search across all files)
2. Search for: `YOUR_FORM_ID`
3. Replace all with: `YOUR_ACTUAL_FORM_ID` (e.g. `xpwqblnrg`)
4. Click "Replace All"

**Option B: Terminal command**

```bash
cd ~/Desktop/TheClearing

# Replace YOUR_FORM_ID with your actual ID (example: xpwqblnrg)
# Change 'xpwqblnrg' to whatever your actual Formspree form ID is
find . -name "*.html" -exec sed -i '' 's/YOUR_FORM_ID/xpwqblnrg/g' {} +
```

Then verify:
```bash
grep -rn "YOUR_FORM_ID" *.html
```
Should return nothing.

---

## Step 5: Test It

1. Go to https://clearing-ai.com/newsletter.html
2. Enter a test email
3. Click Subscribe
4. Check your Formspree dashboard — you should see the submission

---

## Step 6: Git Commit After Fixing

```bash
cd ~/Desktop/TheClearing
git add -A
git commit -m "Fix: Formspree newsletter forms — YOUR_FORM_ID replaced with actual form ID"
```

---

## What Formspree Does

- Takes form submissions (email + name)
- Emails them to **hello@clearing-ai.com** (or your configured address)
- No database needed — Formspree handles it
- Free up to 50/month submissions

---

## While You Do This

While you're setting up Formspree, the Day-14 newsletter follow-up emails are ready to send:

**Due: May 4, 2026** (tomorrow)

All 5 final follow-up emails are in:
```
~/Desktop/TheClearing/newsletter-outreach/send-kit/ready-to-post/
```
- `email-bytes-day14.txt`
- `email-tldr-day14.txt`
- `email-swe-weekly-day14.txt`
- `email-cody-day14.txt`
- `email-devweekly-day14.txt`

Copy each into your email client, send from your personal Gmail, and reply to the original thread if one exists.

---

## Need Help?

If you hit a snag, the Formspree docs at https://formspree.io/docs are excellent.