# Email Sequence Setup Guide — The Clearing

## Status
- ✅ Landing page built: `email-course.html` (Formspree form ID: `xpwqqvln`)
- ✅ Email course hub: `email-course-hub.html`
- ✅ 5 HTML email templates ready: `email-course/ai-fatigue-reset-email-1.html` through `-5.html`
- ✅ 5 plain-text versions ready: `email-course/day-1.md` through `day-5.md`
- ❌ Email sequence delivery: NOT CONFIGURED
- ❌ Formspree not connected to email service

---

## How the Stack Fits Together

```
User signs up at email-course.html
    → Formspree receives submission (form ID: xpwqqvln)
    → Formspree forwards to your email service via webhook
    → Email service sends D1 immediately, D2 in 24h, D3 in 48h, D4 in 72h, D5 in 96h
```

**Two options to make this work:**

1. **Option A: Formspree + Zapier + Email Service** (free tier friendly, ~2hr setup)
2. **Option B: Email service captures directly** (simpler, recommended)

---

## Option A: Formspree → Zapier → Email Service

### Step 1: Choose an Email Service

| Service | Free Tier | Best For | Setup Complexity |
|---------|-----------|----------|-----------------|
| **Loops.so** | 1,000 subscribers, 5,000 emails/mo | Developer-friendly, modern UI | Easy |
| **ConvertKit** | 300 subscribers, unlimited emails | Creators, course builders | Medium |
| **Mailchimp** | 500 subscribers, 1,000 emails/mo | Large ecosystem, reports | Medium |
| **Buttondown** | Simple, cheap ($5/mo) | Minimalists | Easy |

**Recommendation: Loops.so** — it has a generous free tier, clean API, and is designed for drip sequences. Also has a Formspree integration built in.

### Step 2: Set Up Your Email Service

#### Loops.so Setup (Recommended)

1. Go to [loops.so](https://loops.so) and create a free account
2. Create a list called "AI Fatigue Reset" or "5-Day Reset"
3. Go to **Contacts → Add a subscriber** to manually add a test contact
4. Create your 5-email sequence:
   - Click **Campaigns → Create Campaign → Drip Sequence**
   - Set trigger: "Subscribed to list"
   - Add 5 emails with delays:
     - Email 1: Send immediately
     - Email 2: Send 24 hours after Email 1
     - Email 3: Send 24 hours after Email 2 (48h total)
     - Email 4: Send 24 hours after Email 3 (72h total)
     - Email 5: Send 24 hours after Email 4 (96h total)
5. Copy your **API Key** from Settings → API

#### Importing the Emails into Loops

For each of the 5 emails, copy the content from:
- `email-course/ai-fatigue-reset-email-1.html` (D1)
- `email-course/ai-fatigue-reset-email-2.html` (D2)
- `email-course/ai-fatigue-reset-email-3.html` (D3)
- `email-course/ai-fatigue-reset-email-4.html` (D4)
- `email-course/ai-fatigue-reset-email-5.html` (D5)

In Loops email editor, switch to **HTML mode** (code icon) and paste the full HTML. Review the visual preview before saving each email.

**Plain text versions** (for email clients that block HTML) are in:
- `email-course/day-1.md` through `day-5.md`
- In Loops, paste the plain text in the "Plain text version" field

### Step 3: Connect Formspree to Loops via Zapier

1. Create a free [Zapier](https://zapier.com) account
2. Create a new Zap:
   - **Trigger:** Formspree — "New Form Submission"
     - Connect your Formspree account
     - Form ID: `xpwqqvln`
   - **Action:** Loops.so — "Add Subscriber to List"
     - Connect your Loops account (paste API key)
     - List ID: from your Loops list URL (e.g., `ls_lxxxxx`)
     - Email field: map from Formspree `email` field
     - First name (optional): map from Formspree `firstName` if available
3. Test the Zap with a real email submission
4. Enable the Zap

**Test this immediately:**
1. Submit the form at `email-course.html` using your own email
2. Check Loops to see if you appear in the list
3. Check your inbox for D1 email (usually arrives in 1-2 minutes)
4. If D1 arrives, the chain is working

### Step 4: Verify Drip Delays

Wait 25 hours and verify you receive D2. If you don't:
- Check Zapier for errors (Zaps can have 25-min delays on free tier)
- Check Loops sequence timing settings

---

## Option B: Replace Formspree with Native Email Capture

Some email services (Loops, ConvertKit, Mailchimp) can host the signup form directly, bypassing Formspree entirely.

### Loops.so Form Embed

1. In Loops, go to **Forms → Create Form → Inline Form**
2. Design your form (or paste in minimal HTML)
3. Copy the generated **form embed snippet**
4. Replace the `<form>` block in `email-course.html` with the Loops embed

**Current form code to replace** (around line 229 in `email-course.html`):
```html
<form class="signup-form" id="email-course-signup" action="https://formspree.io/f/xpwqqvln" method="POST">
```

**New Loops form embed** (replace with actual snippet from your Loops form):
```html
<div id="loops-form-id-XXXXX"></div>
<script src="https://app.loops.so/forms/embed.js"></script>
```

**Pros:** No Zapier dependency. Direct. 
**Cons:** Need to update the form ID in the site.

---

## Mailchimp Setup (Alternative)

If using Mailchimp instead:

### Step 1: Create a "5-Day Reset" Audience

1. Mailchimp → **Audience → Create Audience**
2. Name: "AI Fatigue Reset"
3. Set up the signup form (or embed existing)

### Step 2: Create the Drip Sequence (Customer Journey)

1. Go to **Automations → Customer Journeys → Create Journey**
2. Name: "5-Day AI Fatigue Reset"
3. Starting point: "Subscribes to audience"
4. Add emails at these intervals:
   - D1: Immediate
   - D2: +24 hours
   - D3: +48 hours
   - D4: +72 hours
   - D5: +96 hours

### Step 3: Import HTML Emails

For each step in the journey, paste the HTML from:
- `email-course/ai-fatigue-reset-email-1.html` through `-5.html`

Mailchimp's editor supports HTML paste. Use the **Code Block** or **Plain Text** block in the custom content option.

### Step 4: Replace Formspree with Mailchimp Embed

Find the form in `email-course.html` and replace the Formspree action with your Mailchimp embed URL.

---

## Subscriber Management

### Where to See Subscribers

| Service | Where |
|---------|-------|
| Loops.so | **Contacts** tab |
| ConvertKit | **Subscribers** tab |
| Mailchimp | **Audience** tab |
| Formspree | **Submissions** (formspree.io/dashboard) — no sequence |

### Metrics to Track

- **Open rate** (target: 40%+)
- **Click-through rate** (target: 15%+)
- **Unsubscribe rate** (max acceptable: 0.5%)
- **D1 → D2 completion rate** (shows real engagement)
- **Quiz referral traffic** from email sequence

Check these weekly for the first month, then monthly once stable.

### Tagging in Loops/ConvertKit

Add a tag "5-day-reset" to all sequence subscribers so you can:
- See them separately from newsletter subscribers
- Re-market to them after they complete the sequence (via The Dispatch)
- See conversion rate from reset → Dispatch sign-up

---

## Testing the Full Sequence

**Do this before announcing the course anywhere:**

1. **Sign up with test email** (use a personal email, not a work email — deliverability is different)
2. **Note the exact time** of signup
3. **Check D1 arrives** within 5 minutes
4. **Set calendar reminder for +25 hours** to check D2
5. **Set calendar reminder for +49 hours** to check D3
6. **Set calendar reminder for +73 hours** to check D4
7. **Set calendar reminder for +97 hours** to check D5

If any email doesn't arrive:
- Check spam folder
- Check the email service for delivery errors (often in the campaign log)
- Verify Zap/workflow ran correctly

---

## What to Do After Setup

1. **Announce the email course** from the main newsletter (The Dispatch #123+)
2. **Share on Reddit** — in r/webdev, r/learnprogramming, r/ExperiencedDevs comments
3. **Add to site footer** — link from every page ("Free 5-Day Email Course")
4. **Add to Dispatch CTAs** — each Dispatch issue should mention the email course at the bottom
5. **Track quiz referrals** — add `?ref=email-course` UTM to email links, check in GSC

---

## Quick-Start Summary (Loops + Zapier)

```
1. Sign up at loops.so → create list → create drip with 5 emails → copy API key
2. Set up Zap: Formspree trigger → Loops add subscriber action
3. Replace <form> in email-course.html with a note (keep Formspree for now)
4. Test with your personal email
5. Verify D1-D5 arrive at correct intervals
6. Add UTM params to email links for tracking
7. Done
```

Expected setup time: 60-90 minutes.
Expected cost: $0/month (Loops free tier: 1k subscribers, 5k emails/month).
At 1,001 subscribers, Loops costs $20/month.

---

## Files Reference

```
email-course.html              ← Landing page (Formspree form active)
email-course-hub.html         ← Management dashboard (internal)
email-course/                 ← Email templates (HTML + plain text)
  ai-fatigue-reset-email-1.html  ← Day 1 HTML
  ai-fatigue-reset-email-2.html  ← Day 2 HTML
  ai-fatigue-reset-email-3.html  ← Day 3 HTML
  ai-fatigue-reset-email-4.html  ← Day 4 HTML
  ai-fatigue-reset-email-5.html  ← Day 5 HTML
  day-1.md  ← Day 1 plain text (for email clients that block HTML)
  day-2.md  ← Day 2 plain text
  day-3.md  ← Day 3 plain text
  day-4.md  ← Day 4 plain text
  day-5.md  ← Day 5 plain text
```

Formspree form ID: `xpwqqvln`
Formspree submissions: https://formspree.io/dashboard/forms/xpwqqvln/submissions