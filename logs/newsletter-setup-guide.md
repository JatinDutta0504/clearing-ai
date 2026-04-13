# Newsletter Setup Guide — The Clearing
**Status:** URGENT — newsletter is live but broken
**Fix time:** 5 minutes
**Last updated:** 2026-04-13 (Hour 308)

---

## The Problem

The newsletter form at `clearing-ai.com/newsletter.html` uses Formspree but the form ID
is still the placeholder `YOUR_FORM_ID`. Every time someone tries to subscribe, their
submission goes to `https://formspree.io/f/YOUR_FORM_ID` which doesn't exist.

**Impact:** ~0 newsletter subscribers despite weeks of traffic.

**What users see:** Nothing visible — the form silently fails in the background.
(We added a mailto fallback that now points to hello@clearing-ai.com, so at least
some subscriptions get through as emails.)

---

## The Fix — Option A: Formspree (Recommended)

Formspree is free for up to 50 submissions/month. Takes 5 minutes.

### Step 1: Create Formspree account
1. Go to https://formspree.io — click "Get Started"
2. Sign up with GitHub (fastest) or email + password
3. Verify your email address

### Step 2: Create a new form
1. Click "New Form" in your Formspree dashboard
2. Name it: "The Clearing — Newsletter Subscribers"
3. Copy the form endpoint — it looks like:
   `https://formspree.io/f/xyzABC123`
4. The `xyzABC123` part is your **form ID**

### Step 3: Update the site files

**In `newsletter.html`:**
```bash
# Replace YOUR_FORM_ID with your actual form ID
YOUR_FORM_ID → xyzABC123
```

The form action line (around line 822):
```html
action="https://formspree.io/f/YOUR_FORM_ID"
                           ↑ replace this
```

**In `ai-fatigue-checklist.html`:**
```bash
# Two forms — checklist-form-top (line 227) and checklist-form-bottom (line 277)
# Replace YOUR_FORM_ID in both
```

### Step 4: Test it
1. Go to clearing-ai.com/newsletter.html
2. Fill out the form with a real email
3. Submit — you should see "You're in. See you Sunday."
4. Check your Formspree dashboard — the submission should appear

### What Formspree gives you:
- Automatic storage of all subscribers
- Email notification on each submission
- Integrates with Zapier/Notion/Google Sheets for automation
- Free tier: 50 submissions/month (plenty to start)

---

## The Fix — Option B: Direct Email (Immediate, No Signup)

If you can't do Formspree right now, change the form action to use a direct mailto:

**In `newsletter.html` (line ~822), change:**
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" novalidate>
```
to:
```html
<form action="mailto:hello@clearing-ai.com?subject=Newsletter%20Subscribe" method="POST" enctype="text/plain">
```

**Downside:** Subscribers go to your email inbox instead of a dashboard. You'd need to manually add them to your email service (Mailchimp/ConvertKit/etc.) to send the weekly Dispatch.

**Upside:** Works immediately. Zero setup.

---

## Newsletter Stats to Track

Once Formspree is running, track these weekly:
- Subscribers added per week
- Open rate (Formspree doesn't give this — need ConvertKit/Mailchimp for advanced stats)
- Referral traffic from newsletter links
- Unsubscribes

---

## The Dispatch — Sending the Newsletter

The Dispatch email template is at:
- `logs/hour-258-2026-04-11-2251-dispatch-13.md`
- `logs/hour-271-2026-04-12-0551-dispatch-14.md`
- `logs/hour-287-2026-04-13-0243-dispatch-15.md`
- `logs/hour-292-2026-04-13-0443-dispatch-16.md`

Each log has the full plain-text + HTML email ready to send.
Send cadence: Sundays 9 AM PDT (or Mondays 9 AM PDT).

**To send manually:**
1. Copy the email content from one of the dispatch logs
2. Paste into your email service (Gmail/ConvertKit/Mailchimp)
3. Send to your subscriber list

---

## Subscriber Count Goal

Current: 0 subscribers
Month 1 goal: 50-100 subscribers
Month 2 goal: 200-500 subscribers
Month 3 goal: 1,000+ subscribers (from HN/Reddit viral moments + organic)

Each subscriber is a guaranteed weekly visit — the highest-quality SEO signal you can buy.

---

## Related Files

- `newsletter.html` — live signup page (form currently broken)
- `ai-fatigue-checklist.html` — lead magnet + email capture (form currently broken)
- `newsletter-thank-you.html` — post-signup landing page (working)
- `logs/dispatch-*.md` — ready-to-send email templates (16 issues ready)
- `sitemap.html` — newsletter listed under "Connect"
