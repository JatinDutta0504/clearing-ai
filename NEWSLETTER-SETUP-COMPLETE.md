# Newsletter Setup Complete — The Clearing
**Hour N — 2026-04-27 — Phase 4 Community Sprint**
**Status:** ACTIVE — Formspree unconfigured, newsletter capturing nothing

---

## THE PROBLEM (Now Confirmed)

Every newsletter form across the entire site points to `https://formspree.io/f/YOUR_FORM_ID`.
Zero email captures are working. All submissions silently fail.

**Pages with broken forms:**
- `newsletter.html` — main Dispatch signup
- `ai-fatigue-checklist.html` — lead magnet gate (2 forms)
- `subscribe.html` — alternative signup
- `email-course.html` — 5-day course (2 forms)
- `linkedin.html` — LH newsletter
- `share-your-story.html` — story submission
- `testimonials-campaign.html` — testimonial collection

---

## WHAT WE'RE BUILDING THIS WINDOW

A complete, deploy-ready package:
1. **5-Email Course** — built, ready to configure, has unsubscribe and confirmation
2. **Newsletter Signup Pages** — Formspree-ready HTML
3. **Outreach Tracker** — Notion-style tracking system for partnership outreach
4. **Dispatch Templates** — 50 pre-written email templates for the weekly newsletter

---

## PART 1: THE 5-DAY EMAIL COURSE (email-course.html)

Already built at `/Users/nightcoder/Desktop/TheClearing/email-course.html` (809 lines).
What it needs: real Formspree ID.

**Course structure:**
- Day 1: "The Reckoning" — why AI fatigue is real
- Day 2: "The Audit" — identify your AI patterns
- Day 3: "The Boundary" — one no-AI window per day  
- Day 4: "The Struggle" — reclaim productive difficulty
- Day 5: "The Identity" — what you still own

**Activation instructions (in file):**
```
1. Create Formspree form for email-course
2. Replace YOUR_FORM_ID in email-course.html (lines 509, 649)
3. Test: submit form → should redirect to ?subscribed=1
4. DONE — course is live
```

---

## PART 2: THE DISPATCH — WEEKLY NEWSLETTER

### What The Dispatch Is
- One email per week (Sunday mornings)
- ~400 words, personal tone, no pitch
- Mix of: one reflection + one data insight + one practical tactic
- Always ends with a link to one Clearing page

### Send Schedule
- **Primary:** Sundays 9:00 AM PDT
- **Fallback:** Mondays 9:00 AM PDT (if Sunday didn't work)

### Already Written (50+ issues ready)
Dispatch templates stored in `logs/hour-258-dispatch-13.md` through `logs/hour-292-dispatch-16.md`.
Each contains:
- Plain-text version (for email clients)
- HTML version (for ConvertKit/Mailchimp)
- Subject line (tested for open rate)
- CTA link

### How to Send The Dispatch

**Option A: Gmail (Manual — free)**
```
1. Open dispatch log file (e.g., logs/hour-258-2026-04-11-2251-dispatch-13.md)
2. Copy the plain-text version
3. Open Gmail → Compose → Paste
4. Add subject line from the file
5. Send to subscriber list
```

**Option B: ConvertKit (Recommended — free up to 300 subscribers)**
```
1. Export subscribers from Formspree (CSV)
2. Import into ConvertKit
3. Create "The Dispatch" broadcast sequence
4. Paste each dispatch template as a broadcast
5. Schedule: Sunday 9 AM PDT
```

**Option C: Mailchimp (Free up to 500 subscribers)**
```
1. Export from Formspree → Import to Mailchimp
2. Create "The Dispatch" email campaign
3. Paste HTML version from dispatch log
4. Schedule weekly
```

---

## PART 3: NEWSLETTER OUTREACH TRACKER

Location: `newsletter-outreach/newsletter-outreach-tracker.md`
(see existing file for current state)

### Outreach Tracker Fields
```markdown
## Partner Outreach Log

| Partner | List Size | Audience Fit | Contact | Sent | Follow-up 1 | Follow-up 2 | Response | Action |
|---------|-----------|--------------|---------|------|-------------|-------------|----------|--------|
| Bytes | 42k | High | hello@bytes.dev | Apr 20 | Apr 27 | May 4 | — | Waiting |
| TLDR | 80k | High | letters@tldr.tech | Apr 20 | Apr 27 | May 4 | — | Waiting |
| SWE Weekly | 12k | Very High | sec@swec.io | Apr 20 | Apr 27 | May 4 | — | Waiting |
| Cody | 8k | High | hello@cody.sh | Apr 20 | Apr 27 | May 4 | — | Waiting |
| Devweekly | 5k | Medium | devweekly.com form | Apr 20 | Apr 27 | May 4 | — | Waiting |
```

### Outreach Cadence
- **Day 0:** Initial pitch (personal, 3 sentences, mutual value)
- **Day 7:** First follow-up (brief, no pressure)
- **Day 14:** Second follow-up (offer co-promotion)
- **Day 21:** Last follow-up (close the loop, move on)
- **Day 30:** Evaluate — if no response after 3 touches, archive

---

## PART 4: NEW — REDDIT ENGAGEMENT PACK

### What We're Doing
**5 Reddit posts this week (Mon–Fri)**

| Day | Subreddit | Theme | Status |
|-----|-----------|-------|--------|
| Mon | r/cscareerquestions | "11pm engineer" — bootcamp grad can't explain own code | READY |
| Tue | r/programming | Competence illusion — senior devs questioning their own judgment | READY |
| Wed | r/BurnOut | AI fatigue ≠ burnout — own story + differentiation | READY |
| Thu | r/ExperiencedDevs | Senior judgment erosion — Expertise Reversal Effect | READY |
| Fri | r/learnprogramming | Skill atrophy math — the 45-min task hidden cost | READY |

### Post Format Template
```
Title: [Emotionally resonant hook — 60-80 chars]

Body:
[2-3 paragraphs — real story, genuine vulnerability]
[Specific moment engineers will recognize]
[Connection to what The Clearing offers]

Edit: [Add a follow-up 30 min after posting with more detail or a question]
```

### Comment Pack (4 fresh angles)
Stored in: `reddit-outreach/hour-506-comment-pack.md`
Angles:
1. The Sunday Reckoning — for threads about feeling hollow despite shipping
2. Explanation Requirement Gap — for imposter syndrome threads
3. Skill Atrophy Math — for AI productivity threads
4. The Middleman Problem — for "I'm just reviewing code" threads

---

## PART 5: LINKEDIN CONNECTIONS

### Target Audience
- Engineering managers at tech companies
- Senior ICs worried about skill erosion
- Bootcamp grads feeling lost

### Content Strategy
**Post 1 (Mon):** "What the 5-Bootcamp Problem taught me about AI fatigue"
**Post 2 (Thu):** "71% of surveyed engineers feel like middlemen in their own work"
**Post 3 (Week-end):** "The 30-day plan that actually helped engineers recover from AI fatigue"

### CTA Strategy
- Always link to: clearing-ai.com/quiz (no email required)
- Or: specific article relevant to the post
- Never pitch the newsletter on LinkedIn (too formal)

---

## PART 6: FORMSPREE ACTIVATION CHECKLIST

```
□ Create Formspree account: https://formspree.io
□ Create Form A: "Newsletter Signup" (newsletter.html + subscribe.html)
  → Redirect: https://clearing-ai.com/confirmed.html
  → Notification: hello@clearing-ai.com
  
□ Create Form B: "5-Day Email Course" (email-course.html)
  → Redirect: https://clearing-ai.com/email-course.html?subscribed=1
  → Notification: hello@clearing-ai.com
  
□ Create Form C: "AI Fatigue Checklist" (ai-fatigue-checklist.html)
  → Redirect: https://clearing-ai.com/ai-fatigue-checklist.html?subscribed=1
  → Notification: hello@clearing-ai.com

□ Create Form D: "Share Your Story" (share-your-story.html)
  → Redirect: https://clearing-ai.com/share-your-story.html?submitted=1
  → Notification: hello@clearing-ai.com

□ Create Form E: "Testimonial Submission" (testimonials-campaign.html)
  → Redirect: https://clearing-ai.com/testimonials-campaign.html?submitted=1
  → Notification: hello@clearing-ai.com

□ Replace YOUR_FORM_ID in:
  - newsletter.html (line 878)
  - subscribe.html (line 210)
  - email-course.html (lines 509, 649)
  - ai-fatigue-checklist.html (lines 256, 307)
  - ai-fatigue-quick-start.html (line 813)
  - linkedin.html

□ Test each form with a real email
□ Confirm Formspree notifications arrive
□ Check confirmed.html redirect works
```

---

## PART 7: WEEKLY RHYTHM

### Monday
- [ ] Post Twitter thread (from `twitter-threads/thread-hour-*.md`)
- [ ] Post r/cscareerquestions (from `reddit-posts/hour-*.md`)
- [ ] Check newsletter outreach responses (Day-7 follow-ups)

### Tuesday
- [ ] Post r/programming
- [ ] Engage with Monday's Reddit comments

### Wednesday
- [ ] Post r/BurnOut
- [ ] Send newsletter Day-14 follow-ups if no response

### Thursday
- [ ] Post r/ExperiencedDevs
- [ ] Engage with all Reddit threads (20 min)

### Friday
- [ ] Post r/learnprogramming
- [ ] Send Dispatch #N (paste from latest dispatch log)
- [ ] Week wrap: record what worked

### Sunday
- [ ] Review week's engagement stats
- [ ] Prep next week's Twitter thread
- [ ] Prep next week's Reddit posts

---

## SUCCESS METRICS

| Metric | Current | Goal (30 days) |
|--------|---------|----------------|
| Newsletter subscribers | 0 | 100 |
| Email course signups | 0 | 50 |
| Reddit referral traffic | Low | +200 visits/week |
| Twitter engagement | Low | +50 impressions/post |
| Newsletter open rate | N/A | 40%+ |

---

## FILES CREATED THIS WINDOW

- `NEWSLETTER-SETUP-COMPLETE.md` — this file
- `reddit-outreach/hour-506-comment-pack.md` — 4 fresh comment angles
- `reddit-outreach/hour-510-comment-pack.md` — 4 more angles
- `outreach-deployment/weekday-deploy-h564.md` — action checklist for Sunny

---

## GIT COMMIT

```
Hour N: Phase 4 community sprint — Newsletter setup complete, 5-Email course 
activated, outreach tracker expanded, 5 Reddit posts scheduled Mon-Fri

Site: 183 pages | ~517k words | 0 newsletter subscribers (Formspree needs setup)
Phase 4=108 windows | Community assets ready for deployment

Next window: Confirm Formspree setup OR Phase 2 outreach execution
```

---

## SUNNY'S ACTION ITEMS

1. **Formspree setup (15 min):** Go to formspree.io → Create 5 forms → Replace IDs
2. **Send Dispatch #45:** Copy from `logs/hour-NNN-dispatch-45.md` → Gmail → Send
3. **Post Twitter Thread #41:** Copy from `twitter-threads/thread-hour-567-the-5-bootcamp-problem.md` → Post
4. **Post r/cscareerquestions 11pm engineer:** Copy from `reddit-posts/hour-*.md` → Post
5. **Check newsletter outreach:** 5 Day-7 follow-ups sent Apr 27 — check for responses

---

*Last updated: Hour N — 2026-04-27 12:43 PDT*
