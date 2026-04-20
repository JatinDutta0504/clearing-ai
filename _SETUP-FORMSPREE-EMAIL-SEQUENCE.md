# The Clearing — Email Funnel Setup Guide
## Formspree + 5-Day Email Sequence Activation

**Status:** Ready to activate. All files are built. This guide walks through the 3 steps to get the newsletter funnel live.

**Last updated:** Hour 437 — 2026-04-19

---

## What Gets Activated

When this is set up, the following flow works automatically:

```
Visitor lands on email-course.html
        ↓
Signs up with name + email
        ↓
Formspree captures the submission
        ↓
SendGrid (or Formspree's email forwarding) sends:
  → Welcome email (immediately, HTML inline)
  → Day 1 email (24h later)
  → Day 2 email (48h later)
  → Day 3 email (72h later)
  → Day 4 email (96h later)
  → Day 5 email (120h later)
        ↓
New subscriber receives The Dispatch (weekly newsletter) every Sunday
```

---

## Step 1: Create Formspree Account

**URL:** https://formspree.io

1. Go to formspree.io and sign up (free tier: 50 submissions/month)
2. Click **New Form** → name it: `AI Fatigue Reset Course`
3. Form endpoint will look like: `https://formspree.io/f/xyzabcde`
4. Copy the form ID (`xyzabcde` part) — you need it for Step 2

---

## Step 2: Add Form ID to Landing Page

Open `email-course.html` and find the `<form>` element (around line 290).

Replace `YOUR_FORM_ID` with your actual form ID:

```html
<!-- OLD (line ~290) -->
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">

<!-- NEW -->
<form action="https://formspree.io/f/xyzabcde" method="POST">
```

Also update these other pages that have the same placeholder:
```bash
grep -rl "YOUR_FORM_ID" /Users/nightcoder/Desktop/TheClearing/
```

Pages that need the form ID:
- `subscribe.html`
- `community-hub.html`
- `newsletter.html`
- `linkedin.html`
- `email-course.html`
- `hn-subscribe.html`

---

## Step 3: Set Up the Email Sequence (SendGrid or Formspree Pro)

### Option A: SendGrid (Recommended — supports automated sequences)

**Why SendGrid:** Formspree free tier doesn't support automated email sequences. SendGrid does (via Twilio SendGrid Marketing Campaigns).

1. Sign up at https://sendgrid.com (free tier: 100 emails/day)
2. Create a **Marketing Campaign** called "5-Day AI Fatigue Reset"
3. Add all 6 emails as individual campaigns:
   - `email-course/welcome-email.html` (send: immediately)
   - `email-course/ai-fatigue-reset-email-1.html` (send: 1 day after)
   - `email-course/ai-fatigue-reset-email-2.html` (send: 2 days after)
   - `email-course/ai-fatigue-reset-email-3.html` (send: 3 days after)
   - `email-course/ai-fatigue-reset-email-4.html` (send: 4 days after)
   - `email-course/ai-fatigue-reset-email-5.html` (send: 5 days after)

4. Copy the **HTML body** from each file (everything between the `<body>` tags, stripped of `<!DOCTYPE>` and `<html>` elements)
5. Create a **Contact List** called "AI Fatigue Reset" 
6. Set up **Automations** → **Welcome Series**:
   - Trigger: new contact added to list
   - Step 1: Send Welcome Email (immediate)
   - Step 2: Send Day 1 (1 day)
   - Step 3: Send Day 2 (2 days)
   - Step 4: Send Day 3 (3 days)
   - Step 5: Send Day 4 (4 days)
   - Step 6: Send Day 5 (5 days)

7. In Formspree form settings → **Notifications** → **Add Email Notification**:
   - Forward form submissions to: your SendGrid-created list
   - Or use a Zapier integration (Formspree → Zapier → SendGrid)

### Option B: Zapier (connects Formspree + SendGrid/Mailchimp)

1. Create Zap at https://zapier.com
2. **Trigger:** Formspree — New Form Submission
3. **Action:** Add to SendGrid/Mailchimp contact list
4. **Action:** SendGrid/Mailchimp automation starts

### Option C: Mailchimp (free tier works for small lists)

1. Sign up at https://mailchimp.com (free: 500 contacts)
2. Create **Audience** called "AI Fatigue Reset"
3. Create **Customer Journey** → **Joining a group** trigger:
   ```
   When contact joins "5-Day Reset" group:
     → Send Welcome email (immediately)
     → Send Day 1 (1 day)
     → Send Day 2 (2 days)
     → Send Day 3 (3 days)
     → Send Day 4 (4 days)
     → Send Day 5 (5 days)
   ```
4. In Formspree → **Forms → your form → Integrations** → Add to Mailchimp audience
5. Tag new subscribers with "5-Day Reset" group

---

## Email Files Reference

| File | Subject Line | Send Timing |
|------|-------------|-------------|
| `welcome-email.html` | "Welcome to the 5-Day AI Fatigue Reset. Here is where to start." | Immediately |
| `ai-fatigue-reset-email-1.html` | "The Sunday Night Reckoning" | Day 1 |
| `ai-fatigue-reset-email-2.html` | "Why a vacation won't fix your AI fatigue" | Day 2 |
| `ai-fatigue-reset-email-3.html` | "The 23-minute rule that changes everything" | Day 3 |
| `ai-fatigue-reset-email-4.html` | "The one practice that rebuilds what AI erodes" | Day 4 |
| `ai-fatigue-reset-email-5.html` | "Day 5: Building the system that outlasts the reset" | Day 5 |

---

## Testing the Sequence

### Test Formspree submission:
```bash
curl -X POST https://formspree.io/f/YOUR_FORM_ID \
  -H "Content-Type: application/json" \
  -d '{"name": "Test User", "email": "test@example.com"}'
```

### Test email rendering:
Open each `.html` file in browser (File → Open) and check:
- [ ] Logo/header renders correctly
- [ ] Fonts look right (Georgia serif body, Inter sans-serif accents)
- [ ] Links work
- [ ] CTA button is visible and styled
- [ ] Mobile width looks good (test at 375px wide)
- [ ] No horizontal overflow

---

## Tracking Setup

### What to track:
1. **Form submission rate** — email-course.html conversion rate
2. **Email open rate** (SendGrid/Mailchimp built-in)
3. **Click-through rate** — which links get clicked in emails
4. **Quiz completion rate** — how many email subscribers take the AI Fatigue Quiz
5. **Newsletter Dispatch conversion** — how many 5-day completers subscribe to The Dispatch

### UTM parameters to add to email links:
```
https://clearing-ai.com/index.html#quiz?utm_source=email&utm_medium=5day&utm_campaign=day1
https://clearing-ai.com/recovery.html?utm_source=email&utm_medium=5day&utm_campaign=day1
https://clearing-ai.com/research.html?utm_source=email&utm_medium=5day&utm_campaign=day1
```

Add these UTM params to all CTA links in the 6 email files.

---

## Subscriber List Management

### Adding UTM to email links in all 6 files:

Use this search/replace to add UTM params to all links pointing to clearing-ai.com:

```python
# Run this from TheClearing directory:
import re, os

utms = "?utm_source=email&utm_medium=5day&utm_campaign=day1"  # change day per email
base_dir = "email-course"

for fname in os.listdir(base_dir):
    if not fname.endswith(".html"):
        continue
    path = os.path.join(base_dir, fname)
    with open(path) as f:
        content = f.read()
    
    # Add UTM to internal clearing-ai.com links
    def add_utm(url):
        if "utm_source" in url:
            return url  # already has UTM
        sep = "&" if "?" in url else "?"
        return url + sep + utms
    
    # Replace href="https://clearing-ai.com/... without existing UTM
    new_content = re.sub(
        r'href="(https://clearing-ai\.com/[^"]+)"(?![^"]*utm_source)',
        lambda m: f'href="{add_utm(m.group(1))}"',
        content
    )
    
    with open(path, "w") as f:
        f.write(new_content)
    
    print(f"Updated {fname}")
```

---

## Weekly Newsletter (The Dispatch) — Separate Flow

After completing the 5-day sequence, subscribers should be invited to **The Dispatch** (weekly Sunday email):

Add this to Day 5 email (or create an automation trigger "completed 5-day course"):
- Subject: "One more thing: The Dispatch goes out every Sunday"
- Body: Brief description of The Dispatch + subscribe link with UTM
- CTA: "Yes, send me The Dispatch every Sunday →"

Link: `https://clearing-ai.com/newsletter.html?utm_source=email&utm_medium=5day&utm_campaign=day5-dispatch`

---

## Compliance Notes

- [ ] All emails include `*|UNSUB|*` placeholder (Mailchimp) or List-Unsubscribe header
- [ ] Privacy policy page exists: `clearing-ai.com/privacy.html`
- [ ] Physical address: [Add when site has one]
- [ ] GDPR: Add checkbox consent field to signup form before EU subscriber acquisition

---

## Quick Checklist

- [ ] Create Formspree account
- [ ] Create SendGrid/Mailchimp account  
- [ ] Add form ID to `email-course.html` and 5 other pages
- [ ] Upload 6 HTML emails to email service
- [ ] Set up welcome automation (immediately)
- [ ] Set up 5-day drip sequence (1 per day)
- [ ] Add UTM parameters to all CTA links
- [ ] Test full submission → email flow
- [ ] Verify *|UNSUB|* works in all emails
- [ ] Set up weekly Dispatch automation for completers
