# Formspree Setup Guide — UNBLOCK NEWSLETTER CAPTURES
**Fri Apr 3, 2026 — 10 min setup — CRITICAL FOR HN TRAFFIC**

## Why This Matters
Without Formspree configured, EVERY visitor from HN/Reddit/Twitter who tries to subscribe hits a broken form.
With Formspree: 20–40% of high-intent visitors subscribe → becomes owned audience.

---

## Step 1: Create Formspree Account (Free Tier = 50 subs/month)
1. Go to: https://formspree.io
2. Click "Get Started" → Sign up with GitHub or Email
3. Verify your email
4. Click "New Form" → Name it "clearing-ai-newsletter"

## Step 2: Get Your Form ID
1. In formspree.io dashboard, click your new form
2. Copy the Form ID (looks like: xpzgldjk)
3. Your endpoint will be: https://formspree.io/f/xpzgldjk

## Step 3: Replace YOUR_FORM_ID in 4 Files

### File 1: newsletter.html
```bash
open /Users/nightcoder/Desktop/TheClearing/newsletter.html
```
Search for: `YOUR_FORM_ID`
Replace with: `xpzgldjk` (your actual ID)

### File 2: ai-fatigue-checklist.html
```bash
open /Users/nightcoder/Desktop/TheClearing/ai-fatigue-checklist.html
```
Search for: `YOUR_FORM_ID`
Replace with: `xpzgldjk` (your actual ID)

### File 3: index-hn.html
```bash
open /Users/nightcoder/Desktop/TheClearing/index-hn.html
```
Search for: `YOUR_FORM_ID`
Replace with: `xpzgldjk` (your actual ID)

### File 4: testimonials.html
```bash
open /Users/nightcoder/Desktop/TheClearing/testimonials.html
```
Search for: `YOUR_FORM_ID`
Replace with: `xpzgldjk` (your actual ID)

## Step 4: Commit and Push
```bash
cd /Users/nightcoder/Desktop/TheClearing
git add -A
git commit -m "Hour 137: Formspree configured — newsletter captures UNBLOCKED"
git push
```

## Step 5: Test It
1. Go to https://clearing-ai.com/newsletter.html
2. Enter a test email + name
3. Submit — should see "Thanks! Please check your email."
4. Check your Formspree dashboard → should show 1 submission

## Step 6: Verify All 4 Forms
Test each page:
- https://clearing-ai.com/ai-fatigue-checklist.html (scroll to email capture)
- https://clearing-ai.com/index-hn.html (email capture section)
- https://clearing-ai.com/testimonials.html (email capture section)

---

## What Happens After
- Formspree free tier: 50 subscribers/month
- At 50 subscribers: upgrade to $9/month for unlimited
- Each submission goes to: your formspree.io dashboard AND (optionally) your email
- To get emails forwarded to your inbox: Formspree dashboard → form → Settings → Email notifications

## Timeline
- Setup: 10 minutes
- Test: 2 minutes
- Total: 12 minutes
- Impact: Unblocks ALL newsletter captures from HN/Reddit/Twitter traffic

---

## Sunny's Action Items (Right Now)
1. ☐ Go to formspree.io → create account → new form
2. ☐ Copy Form ID
3. ☐ Replace YOUR_FORM_ID in 4 files above
4. ☐ Commit + push
5. ☐ Test all 4 forms
6. ☐ Send the 4 newsletter partnership emails (from logs/hour-137-2026-04-03-newsletter-outreach-refresh.md)
7. ☐ Submit to HN: news.ycombinator.com/submit
   - Title: "I built a free AI fatigue recovery tool for burnt-out engineers — here's what 2,000+ quiz takers revealed"
   - URL: https://clearing-ai.com/index-hn.html
