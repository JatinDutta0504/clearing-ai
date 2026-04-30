# The Clearing — Email Course: "5-Day AI Fatigue Reset"

## Overview

Complete 5-email sequence with HTML versions of each day + archive page.

**Purpose:** Transform newsletter subscribers into engaged readers through a 5-day email arc.

**Sequence logic:**
- Day 1: Welcome + identity framing (you're in the right place)
- Day 2: The real problem (what AI fatigue actually is)
- Day 3: Your first action (no-AI block or Explanation Requirement)
- Day 4: The community angle (you're not alone, here's a story)
- Day 5: The offer (continue with The Dispatch OR try the quiz)

## Files

| File | Purpose |
|------|---------|
| `email-course.html` | Main landing page (already existed) |
| `email-course/index.html` | Archive page — all 5 days linked |
| `email-course/day-1.html` | Day 1: Your Brain Is Not a Bug |
| `email-course/day-2.html` | Day 2: The Thing Nobody Names |
| `email-course/day-3.html` | Day 3: Your First No-AI Block |
| `email-course/day-4.html` | Day 4: You're Not Alone |
| `email-course/day-5.html` | Day 5: Keep Going |
| `email-course/day-1.md` | Day 1 — plain text source |
| `email-course/day-2.md` | Day 2 — plain text source |
| `email-course/day-3.md` | Day 3 — plain text source |
| `email-course/day-4.md` | Day 4 — plain text source |
| `email-course/day-5.md` | Day 5 — plain text source |

## Usage

The HTML pages are for:
1. Subscribers who can't receive email (web-based reading)
2. Debugging email rendering issues
3. Sharing specific days with people

The MD files are plain-text source — use these when sending via himalaya/gog.

## Technical Notes

- No tracking pixels (zero tracking policy)
- Plain text primary (works everywhere)
- HTML backup (renders beautifully)
- Unsubscribe link in every email (legal requirement)
- From: The Clearing <hello@clearing-ai.com>
- Archive link in email-course.html and newsletter-archive.html

## Formspree Status

All forms have `YOUR_FORM_ID` placeholder. Sunny needs to configure Formspree.
See: `_FORMSPREE_SETUP.md`

## Day Sequence (for sending)

**Day 1:** Send immediately on signup
**Day 2:** Send 1 day after Day 1
**Day 3:** Send 1 day after Day 2
**Day 4:** Send 1 day after Day 3
**Day 5:** Send 1 day after Day 4

Use `day-N.md` files as email body when sending via himalaya.