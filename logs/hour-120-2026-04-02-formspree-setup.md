# 🚨 CRITICAL: Formspree Setup Guide — Do This Before HN Launch
**Created:** Hour 120 — Thu Apr 2, 2026 ~05:50 UTC (~3 hours before HN launch)
**Status:** BLOCKER — 0 newsletter captures without this fix

---

## Why This Matters RIGHT NOW

HN launches in ~3 hours. Every visitor who signs up for the newsletter will be captured IF Formspree is configured. Without it, those emails go nowhere. That's 300-800 potential subscribers lost forever.

**Files that need your Form ID:**
1. `newsletter.html` — line ~787
2. `ai-fatigue-checklist.html` — lines ~167 and ~212
3. `index-hn.html` — line ~702 (HN landing page — MOST CRITICAL)
4. `testimonials.html` — find and replace `YOUR_FORM_ID`

---

## Step-by-Step Setup (10 minutes)

### Step 1: Create Formspree Account
1. Go to **https://formspree.io**
2. Click "Get Started" → Sign up with **GitHub** (fastest) or email
3. Free plan: **250 submissions/month** — more than enough for newsletter growth

### Step 2: Create Your Form
1. Dashboard → "**+ New Form**"
2. Name it: `The Clearing Newsletter`
3. You'll land on your form settings page
4. Your endpoint will look like: `https://formspree.io/f/YOUR_FORM_ID`
5. The `YOUR_FORM_ID` part is what you need (e.g., if URL is `formspree.io/f/xoyqbcd`, your ID is `xoyqbcd`)

### Step 3: Add Form Fields (already done in our HTML)
Our forms send these fields automatically:
- `email` (required)
- `name` (optional)
- `_subject` (for email notifications)
- `_next` (redirect after submit — already set to `/newsletter-thank-you.html`)

### Step 4: Copy Your Form ID and Replace
Find and replace `YOUR_FORM_ID` with your actual form ID in these files:

**Find all occurrences:**
```bash
cd ~/Desktop/TheClearing
grep -r "YOUR_FORM_ID" --include="*.html" -l
```

**Replace in each file:**
- `newsletter.html` line ~787: `action="https://formspree.io/f/YOUR_FORM_ID"` → `action="https://formspree.io/f/xoyqbcd"` (your ID)
- `ai-fatigue-checklist.html` lines ~167, ~212: same replacement
- `index-hn.html` line ~702: same replacement
- `testimonials.html`: same replacement

### Step 5: Test It
1. Open `index-hn.html` in browser
2. Enter a test email
3. Click Subscribe
4. You should be redirected to `/newsletter-thank-you.html`
5. Check your Formspree dashboard — you should see the submission

### Step 6: Git Push
```bash
cd ~/Desktop/TheClearing
git add -A
git commit -m "hour-120-formspree-configured"
git push
```

---

## TEMPORARY WORKAROUND (If You Don't Have Time)

If HN is live before Formspree is set up, add a **mailto fallback** to `index-hn.html`:

Replace the form on line ~702 with:
```html
<div class="nl-form">
  <p style="margin-bottom: 0.75rem;">
    <a href="mailto:hello@clearing-ai.com?subject=Newsletter Signup">Email us to subscribe →</a>
  </p>
</div>
```

This at least captures emails as actual emails, even if not automated.

---

## Alternative: Use Buttondown (Easier Setup)

If Formspree feels complex, **Buttondown** (buttondown.email) is simpler:
1. Create account at buttondown.email
2. Create a "subscriber form"
3. It gives you an HTML snippet
4. Replace the form in `index-hn.html` with their snippet

But Formspree is already coded — just needs the ID swapped.

---

## What Happens After Setup

1. **HN visitors subscribe** → emails go to Formspree dashboard → you export to CSV or connect to email service
2. **Week 1:** Export all Formspree submissions, import to Buttondown or ConvertKit
3. **Week 2:** Send Dispatch #2 to new subscribers
4. **Week 3-4:** Grow to 200+ subscribers from HN traffic

---

## Timeline
- **NOW:** Set up Formspree (10 min)
- **~3h:** HN goes live (9 AM PDT)
- **During HN:** Monitor Formspree submissions dashboard
- **After HN:** Export submissions, import to email service
- **Mon Apr 7:** Send Dispatch #3 to full list

---

## If You Get Stuck
Email: hello@clearing-ai.com (already in the fallback on the page)
