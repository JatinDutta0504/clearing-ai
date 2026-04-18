# Formspree Setup Guide — The Clearing

## Overview
Formspree handles all email collection on clearing-ai.com. This guide walks through getting a free Formspree account, creating forms, and replacing `YOUR_FORM_ID` placeholders.

**Time needed:** ~15 minutes
**Cost:** Free (up to 50 submissions/month)
**Account:** formspree.io

---

## Step 1: Create a Formspree Account

1. Go to [formspree.io](https://formspree.io) and sign up (GitHub or Google SSO is fastest)
2. Verify your email address
3. You're in the free tier — no credit card needed

---

## Step 2: Create Forms for Each Signup Location

You need **one form per signup location** on the site. Create them in the Formspree dashboard:

### Form A: Newsletter (subscribe.html + newsletter.html)
- **Name:** `The Dispatch — Newsletter Signup`
- **Redirect URL:** `https://clearing-ai.com/confirmed.html`
- **Email notification:** Add `hello@clearing-ai.com` as notification email
- After creating, note the **Form ID** (e.g., `xpwzgklb` → URL becomes `https://formspree.io/f/xpwzgklb`)

### Form B: Email Course (email-course.html)
- **Name:** `5-Day AI Fatigue Reset — Email Course Signup`
- **Redirect URL:** `https://clearing-ai.com/confirmed.html`
- **Email notification:** `hello@clearing-ai.com`
- After creating, note the Form ID

### Form C: Testimonials (testimonials-campaign.html)
- **Name:** `Engineer Testimonial Submission`
- **Redirect URL:** `https://clearing-ai.com/testimonials-campaign.html?submitted=1`
- **Email notification:** `hello@clearing-ai.com`
- Note: This form has more fields — add them in the Formspree dashboard

### Form D: Share Your Story (share-your-story.html)
- **Name:** `Share Your Story — Anonymous Submission`
- **Redirect URL:** `https://clearing-ai.com/share-your-story.html?submitted=1`
- **Email notification:** `hello@clearing-ai.com`

### Form E: AI Fatigue Checklist (ai-fatigue-checklist.html)
- **Name:** `AI Fatigue Recovery Checklist — PDF Download`
- **Redirect URL:** `https://clearing-ai.com/ai-fatigue-checklist.html?subscribed=1`
- **Email notification:** `hello@clearing-ai.com`

---

## Step 3: Replace YOUR_FORM_ID Placeholders

Find all occurrences across the site:

```bash
cd /Users/nightcoder/Desktop/TheClearing
grep -r "YOUR_FORM_ID" --include="*.html" -l
```

Replace `YOUR_FORM_ID` with your actual Form ID for each file:

| File | Form ID to Use |
|------|---------------|
| subscribe.html | Form A ID |
| newsletter.html | Form A ID |
| email-course.html | Form B ID |
| testimonials-campaign.html | Form C ID |
| share-your-story.html | Form D ID |
| ai-fatigue-checklist.html | Form E ID |

### Example replacement

```html
<!-- BEFORE -->
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">

<!-- AFTER (Form A = xpwzgklb) -->
<form action="https://formspree.io/f/xpwzgklb" method="POST">
```

In JavaScript `fetch()` calls:
```javascript
// BEFORE
fetch('https://formspree.io/f/YOUR_FORM_ID', ...)

// AFTER
fetch('https://formspree.io/f/xpwzgklb', ...)
```

---

## Step 4: Verify Forms Work

1. Open each page in browser
2. Fill in test data (use `test@example.com`)
3. Submit — should redirect to confirmed.html (or show success)
4. Check Formspree dashboard — submission should appear
5. Check email — should receive notification

---

## Step 5: Upgrade to Pro (Optional — When Ready)

Free tier: 50 submissions/month
Pro tier: $9/month — unlimited submissions, password protection, analytics, file uploads

**When to upgrade:** When newsletter growth hits ~40 signups/month (so you have room for spikes)

---

## Step 6: Set Up Email Sequence (Automated)

Formspree free tier does NOT include automated email sequences. For the 5-day email course, you need either:

### Option A: Formspree + Zapier (Free tier)
1. Formspree submission → Zapier webhook trigger
2. Zapier → email service (Gmail, SendGrid) → sends Day 1 email
3. Zapier delay → sends Day 2, Day 3, etc.

### Option B: ConvertKit (Recommended — Free up to 300 subscribers)
1. Export Formspree submissions to CSV
2. Import to ConvertKit
3. Create 5-email sequence with ConvertKit's visual automation
4. Embed ConvertKit form instead of Formspree on email-course.html

### Option C: Mailchimp (Free up to 500 subscribers)
1. Export Formspree submissions
2. Import to Mailchimp audience
3. Create 5-email "Customer Journey" automation
4. Replace Formspree embed with Mailchimp form

---

## Quick Reference

| Page | File | Current placeholder | Replace with |
|------|------|---------------------|--------------|
| Subscribe | subscribe.html | YOUR_FORM_ID | Form A ID |
| Newsletter | newsletter.html | YOUR_FORM_ID | Form A ID |
| Email Course | email-course.html | YOUR_FORM_ID | Form B ID |
| Testimonials | testimonials-campaign.html | YOUR_FORM_ID | Form C ID |
| Share Story | share-your-story.html | YOUR_FORM_ID | Form D ID |
| Checklist | ai-fatigue-checklist.html | YOUR_FORM_ID | Form E ID |

**Git commit after setup:**
```bash
cd /Users/nightcoder/Desktop/TheClearing
git add -A
git commit -m "feat: configure Formspree forms (live IDs)"
git push
```

---

## Troubleshooting

**Form redirects to Formspree instead of confirmed.html?**
→ Check the redirect URL in Formspree dashboard matches `https://clearing-ai.com/confirmed.html`

**Not receiving email notifications?**
→ Check spam folder. Add notifications@formspree.io to contacts.

**Form submissions not appearing in dashboard?**
→ Check the form's spam folder in Formspree dashboard.

**"Server error" on submission?**
→ The Form ID is wrong. Double-check the ID in the Formspree dashboard.

---

*Last updated: Hour 406 — 2026-04-18*
