# Hour 571 — 2026-04-27 17:43 PDT (Phase 2 Window 174: Outreach Execution)

**Phase:** Phase 2 (Outreach + Authority) — rotation pick
**Phase windows:** P1=151 ✅ | P2=174 🟡 | P3=122 ✅ | P4=109 🟡
**40% P1 / 30% P2 / 20% P3 / 10% P4** → Phase 2 selected

---

## Context: What Was Built Last 24 Hours

- Hour 570: CSS render-blocking fix — all 183 pages now non-blocking (✅)
- Hour 569: Phase 2 outreach week package — Reddit Mon-Fri schedule + Thread #41 + Day-7 follow-ups ready

---

## ⚠️ TODAY'S ACTION ITEMS (Mon Apr 27 — These need Sunny to execute NOW)

### 1. Reddit Post — r/cscareerquestions "The 11pm Problem" (DUE TODAY)

**File:** `reddit-posts/hour-503-cscareerquestions-11pm-problem.md`
**Status:** READY — needs to be posted NOW (it's 5:43 PM, posted should have gone up ~7-9 AM)
**Community:** r/cscareerquestions (1.1M members)
**Format:** Text post, first-person hook, NO mention of Clearing in post body
**Title:** "I shipped more code than any month in my career but I understand almost none of it. Is this just me or is something off?"
**Engagement:** Reply to every comment for first 2 hours, then check daily

### 2. Newsletter Day-7 Follow-ups — DUE TODAY (5 emails)

All 5 newsletters marked as **PENDING** in tracker. Day-7 follow-ups were due today.

| Newsletter | Email | Status | Notes |
|-----------|-------|--------|-------|
| Bytes | hello@bytes.dev | PENDING | ~80k subs |
| TLDR | letters@tldr.tech | PENDING | ~200k subs |
| SWE Weekly | sec@swec.io | PENDING | ~15k subs |
| Cody | hello@cody.sh | PENDING | ~20k subs |
| Devweekly | devweekly.io form | PENDING | ~30k subs |

**Templates:** `newsletter-outreach/send-kit/SEND-KIT.md` — Follow-up copy for each already written.
**Action:** Send from personal email (Gmail, or himalaya/openclaw email skill). Use `?ref=bytes` etc. on all links.
**Tracker update:** Mark each as EM2_SENT after sending.

### 3. Twitter Thread #41 — Status Check

**File:** `twitter-threads/thread-hour-567-the-5-bootcamp-problem.md`
**Status per tracker:** "POSTED Mon Apr 27" — if NOT posted, post NOW
**Thread:** "The 5-Bootcamp Problem" (10 tweets, competence illusion + junior engineers)
**CTA:** https://clearing-ai.com/#quiz
**Hashtags:** #AIFatigue #JuniorEngineer #SoftwareEngineering

### 4. Formspree Configuration — CRITICAL BLOCKER

**Problem:** All newsletter/email forms still use `YOUR_FORM_ID` placeholder. Zero subscribers can sign up.
**Impact:** Newsletter outreach is pointless if the signup form doesn't work.

**Action:**
1. Go to formspree.io → Sign up free → Create 3 forms:
   - **Form 1:** "The Dispatch" newsletter signup
   - **Form 2:** 5-Day AI Fatigue Recovery Course
   - **Form 3:** Share Your Story / Testimonials
2. Replace `YOUR_FORM_ID` in all HTML files:
   - `newsletter.html` (line 878)
   - `email-course.html` (line 509, 649)
   - `subscribe.html`
   - `testimonials.html`
   - `share-your-story.html`
   - `ai-fatigue-checklist.html`
   - `ai-fatigue-quick-start.html`
3. Commit all form fixes

### 5. Reddit This Week — Remaining Schedule

| Day | Platform | File | Status |
|-----|----------|------|--------|
| ~~Mon Apr 27~~ | r/cscareerquestions | hour-503 11pm problem | **DUE TODAY** |
| Tue Apr 28 | r/programming | hour-510 competence illusion | READY |
| Wed Apr 29 | r/BurnOut | Comment pack (Angle D) | hour-567-comment-pack.md |
| Thu Apr 30 | r/ExperiencedDevs | hour-432-r-experienceddevs.md | READY |
| Fri May 1 | r/learnprogramming | Comment pack (Angle C) | hour-567-comment-pack.md |

---

## Tracker Update

```json
{
  "phase_windows": {
    "phase1_content": 151,
    "phase2_outreach": 174,
    "phase3_seo": 122,
    "phase4_community": 109
  },
  "content_pages_built": 183,
  "total_words": "~517k",
  "interactive_features": 11,
  "pillars_completed": {
    "pillar1_ai_fatigue": ["index","tips","why","glossary","quiz","quiz-results","ai-fatigue","signs-ai-fatigue","quiz-results-tier-1-4","vibe-coding","career-pivot","index-hn","ai-skeptic-guide","ai-productivity-paradox","ai-code-review","coders-block","ai-consultation-fatigue","the-craft-problem","ai-healthcare","neurodivergent","tutorial-paradox","daily-ai-boundaries","ai-fatigue-type-calculator","ai-meeting-fatigue","ai-fatigue-emergency-kit","debugger-drift","engineer-case-studies","social-badges","engineer-energy-management","share-your-story","sleep-and-ai-fatigue","why-resting-doesnt-fix","no-ai-block","ai-free-fridays","freelance","golden-handcuffs","ai-fatigue-compounding","vibe-coding-self-assessment","vibe-coding-rules","senior-engineer-ai-fatigue","performance-review-ai-fatigue","ai-architecture-fatigue","startup-engineer","ai-fatigue-quick-start","first-year-engineer","ai-fatigue-by-role","ai-middleman-problem","decision-fatigue-ai","architecture-decay","context-switching-ai","manifesto","the-explanation-requirement","ai-fatigue-cost-calculator","ai-fatigue-recovery-cheat-sheet","ai-fatigue-checklist-print","ai-fatigue-checklist","ai-fatigue-recovery-journal","ai-fatigue-severity-index","engineering-managers-ai-fatigue","executive-burnout","ml-engineer-ai-fatigue","pair-programming-fatigue","ai-debugging-fatigue","ai-productivity-guilt","ai-documentation-fatigue","ai-brownout","ai-fatigue-conversations","inference-fatigue","ai-skeptic-engineer","the-sunday-scaries-ai","underrepresented-engineers-ai-fatigue","ai-fatigue-type-calculator","ai-debugging-confidence","data-engineer-ai-fatigue","oncall-ai-fatigue","the-ai-dependency-trap","tech-giants-ai-fatigue","ai-decision-stack"],
    "pillar2_burnout": ["team-guide","developer-burnout-2025","workplace","hiring","burnout-vs-fatigue","software-engineer-mental-health","tech-layoffs-ai-era","imposter-syndrome-ai","engineering-managers-ai-fatigue","executive-burnout","ml-engineer-ai-fatigue","senior-identity","junior-engineers","community","return-to-office-ai-fatigue","code-review-culture","tech-giants-ai-fatigue","imposter-syndrome-vs-ai-fatigue"],
    "pillar3_tools": ["compare","ai-tool-overload","ai-learning-burnout","coding-ai-tools-comparison","ai-productivity-paradox","ai-documentation-fatigue","pair-programming-fatigue","ai-debugging-fatigue","ai-productivity-guilt","vibe-coding-ai-fatigue","ai-code-review-fatigue","ai-meeting-fatigue","ai-consultation-fatigue"],
    "pillar4_recovery": ["decompress","recovery","mental-health","developer-wellbeing","daily-practice","checkin","ai-fatigue-checklist","ai-detox-plan","corporate-ai-wellness","team-manager-guide","daily-ai-boundaries","testimonials","engineer-energy-management","share-your-story","sleep-and-ai-fatigue","why-resting-doesnt-fix","no-ai-block","ai-free-fridays","freelance-engineer-ai-fatigue","ai-decision-stack","golden-handcuffs","ai-fatigue-emergency-kit","ai-fatigue-recovery-journal","ai-fatigue-severity-index","manifesto","the-explanation-requirement","testimonials-campaign","ai-brownout","the-24-month-projection"],
    "pillar5_research": ["research","skill-atrophy","cognitive-load","attention-residue","flow-state","productivity-theater","engineer-survey-results","ai-fatigue-statistics-2025","the-science-of-ai-fatigue","ai-fatigue-compounding","decision-fatigue-ai","architecture-decay","ai-fatigue-in-2026","ai-fatigue-2026-report","data-report-2026","inference-fatigue","ai-engineer-2026-retrospective"]
  },
  "phase2_assets": {
    "reddit_posts_live": ["r/cscareerquestions (hour-462)", "r/webdev (hour-462)"],
    "reddit_posts_scheduled_this_week": [
      "r/cscareerquestions Mon Apr 27 — 11pm problem (hour-503) — DUE TODAY",
      "r/programming Tue Apr 28 — Competence Illusion (hour-510) — READY",
      "r/BurnOut Wed Apr 29 — Comment mode (hour-567 Angle D)",
      "r/ExperiencedDevs Thu Apr 30 — Senior judgment erosion (hour-432)",
      "r/learnprogramming Fri May 1 — Comment mode (hour-567 Angle C)"
    ],
    "twitter_threads": [
      "Thread #41: The 5-Bootcamp Problem — POSTED Mon Apr 27 (verify if posted)"
    ],
    "newsletter_day7_followups": "DUE TODAY — 5 follow-up emails ready in send-kit",
    "newsletter_formspree_blocker": "ALL FORMS use YOUR_FORM_ID — 0 subscribers captured"
  },
  "outreach_status": {
    "reddit_communities_active": 5,
    "reddit_posts_live_count": 2,
    "reddit_posts_scheduled_this_week": 5,
    "twitter_threads_posted": 5,
    "newsletter_partnerships_pending": "5 Day-7 follow-ups — SEND TODAY",
    "newsletter_outreach_tracker": "newsletter-outreach/newsletter-outreach-tracker.md",
    "formspree_status": "NOT CONFIGURED — all forms broken"
  },
  "seo_metrics": {
    "site_pages": 183,
    "total_words": "~517k",
    "sitemap_urls": 184,
    "interactive_features": 11,
    "technical_seo_score": "98/100"
  },
  "newsletter_status": {
    "subscriber_count": 0,
    "forms_broken": true,
    "formspree_configured": false,
    "dispatch_issues_ready": 50,
    "email_course_built": true,
    "email_course_forms_broken": true
  },
  "hour_N_notes": "Hour 571: Phase 2 outreach execution window. Reddit r/cscareerquestions due TODAY. Day-7 newsletter follow-ups due TODAY. Formspree config is CRITICAL blocker.",
  "last_updated": "2026-04-27T17:43:00-07:00"
}
```

---

## What to Do Right Now

### Step 1 — Post to r/cscareerquestions (5 min)
Copy the post body from `reddit-posts/hour-503-cscareerquestions-11pm-problem.md` and paste to reddit.com/r/cscareerquestions

### Step 2 — Send 5 newsletter Day-7 follow-ups (10 min)
Use the templates in `newsletter-outreach/send-kit/SEND-KIT.md`. Send from your personal email. Add `?ref=bytes` etc. to all links.

### Step 3 — Configure Formspree (15 min)
1. formspree.io → Sign up
2. Create 3 forms: newsletter, course, testimonials
3. Find + replace `YOUR_FORM_ID` across ~10 HTML files
4. Git commit

### Step 4 — Verify Thread #41 posted
Check Twitter. If not posted, post from `twitter-threads/thread-hour-567-the-5-bootcamp-problem.md`

---

**Git:** No new commit this window — execution only. Next content window: Hour 572.
**Live at:** https://clearing-ai.com
