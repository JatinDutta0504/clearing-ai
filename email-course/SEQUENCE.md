# 5-Day AI Fatigue Reset — Email Sequence

## Overview
Automated email sequence sent to new subscribers who sign up via email-course.html.
**Send cadence:** One email per day for 5 days, starting immediately.
**Platform:** Formspree (when configured) or manual send via email service.

---

## Email 1: The Sunday Night Reckoning
**File:** `ai-fatigue-reset-email-1.html`
**Subject:** The Sunday Night Reckoning
**Day:** 1 (send immediately on signup)

### Purpose
Name what they're feeling. Establish the four dimensions of AI fatigue.

### Key Content
- The Sunday night reckoning phenomenon
- 4 engineers anonymous survey quotes
- 4 dimensions of AI fatigue: cognitive load without closure / skill atrophy / identity erosion / ghost authorship
- Day 1 assignment: list 3 things you now reach for AI that you used to know

### CTA
- Primary: Take the full AI Fatigue Quiz
- Secondary: clearing-ai.com/ai-fatigue.html

---

## Email 2: Why Resting Doesn't Fix It
**File:** `ai-fatigue-reset-email-2.html`
**Subject:** Why a vacation won't fix your AI fatigue
**Day:** 2 (send 24 hours after Email 1)

### Purpose
Dispel the "just rest more" misdiagnosis. Introduce the structural problem.

### Key Content
- Three misdiagnoses: burnout / boundaries / overwhelm
- Gloria Mark's 23-minute recovery finding
- Sunday night = cognitive debt finally noticed
- Day 2 assignment: track AI interruptions for one day

### CTA
- Primary: clearing-ai.com/why-resting-doesnt-fix-ai-fatigue.html

---

## Email 3: The 23-Minute Rule
**File:** `ai-fatigue-reset-email-3.html`
**Subject:** The 23-minute rule that changes everything
**Day:** 3 (send 48 hours after Email 1)

### Purpose
Use the science to explain why batching is the structural fix.

### Key Content
- Sophie Leroy's attention residue research
- The compounding cost math (interruptions × 23-min recovery)
- 90-minute deep work blocks + 15-minute AI batch windows
- Day 3 assignment: set a 90-minute no-AI timer

### CTA
- Primary: clearing-ai.com/attention-residue.html

---

## Email 4: The No-AI Hour
**File:** `ai-fatigue-reset-email-4.html`
**Subject:** The one practice that rebuilds what AI erodes
**Day:** 4 (send 72 hours after Email 1)

### Purpose
The skill preservation core — desirable difficulties, Bainbridge's ironies.

### Key Content
- Robert Bjork's desirable difficulty research
- Lisanne Bainbridge's Ironies of Automation (1983)
- The No-AI Hour rules (30/45/60/90 min options)
- Day 4 assignment: schedule the no-AI hour on calendar

### CTA
- Primary: clearing-ai.com/no-ai-block.html

---

## Email 5: The System, Not the Sprint
**File:** `ai-fatigue-reset-email-5.html`
**Subject:** Day 5: Building the system that outlasts the reset
**Day:** 5 (send 96 hours after Email 1)

### Purpose
Convert from reset to system. Anchor into long-term practice.

### Key Content
- 4 Anchors: calendar protection / batch AI / Explanation Requirement / Sunday recalibration
- The Dispatch newsletter signup
- clearing-ai.com full resource guide
- Personal closing

### CTA
- Primary: clearing-ai.com/newsletter.html (The Dispatch weekly)
- Secondary: clearing-ai.com (full site)

---

## Setup Notes

### Formspree Integration
When Formspree is configured:
1. Add form ID to email-course.html signup form
2. Set up Formspree email routing to trigger the 5-email sequence
3. Configure day-interval emails (e.g., using Zapier + Formspree)

### Manual Send Option
Before Formspree/setup:
- Export subscriber list from Formspree dashboard
- Import to email service (Mailchimp, ConvertKit, etc.)
- Use these HTML files as email templates
- Set up 5-email drip sequence with 1-day intervals

### Mailchimp / ConvertKit Setup
- Create a "5-Day Reset" tag/segment
- Import HTML files as individual emails
- Set send interval: immediately, +1 day, +2 days, +3 days, +4 days
- Enable click tracking and open tracking

### Subject Line Testing
Test subject lines with 2-3 variants per email for open rate optimization.

---

## Metrics to Track
- Open rate (target: 40%+)
- Click-through rate (target: 15%+)
- Unsubscribe rate (max acceptable: 0.5%)
- Quiz referral traffic from email sequence
- Newsletter Dispatch signup conversion from Day 5 email

---

## Compliance
- All emails include `*|UNSUB|*` placeholder (Mailchimp) or List-Unsubscribe header
- Physical address: [To be added when site has one]
- Privacy policy: clearing-ai.com/privacy.html
- GDPR: Add checkbox consent field to signup form before EU subscriber acquisition
