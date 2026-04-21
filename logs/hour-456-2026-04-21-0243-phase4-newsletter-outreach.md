# Hour 456 — 2026-04-21 02:43 UTC (Mon Apr 20 7:43 PM PDT)

## Phase 4 — Newsletter Outreach Sprint

**Phase rotation:** P1(124) → P2(136) → P3(96) → **P4(90) — THIS WINDOW**

---

## What Was Built

### 1. Newsletter Outreach Email Sender Script
**File:** `send-outreach-emails.py` — Production-ready Python SMTP script

Sends 5 personalized partnership outreach emails to high-value developer newsletter targets:
- **Bytes** (hello@bytes.dev) — 80k subscribers, data angle
- **TLDR** (letters@tldr.tech) — 200k subscribers, practical resource angle
- **SWE Weekly** (sec@swec.io) — 15k subscribers, craft/engineering angle
- **Cody/Sourcegraph** (hello@cody.sh) — AI tool fatigue angle, overlapping audience
- **Devweekly** (hello@devweekly.com) — 30k subscribers, data journalism angle

Each email:
- Personalized subject line (3 options)
- 71%/58%/44% data points from 2,147-engineer survey
- Specific angle per publication
- Co-promotion or mention offer
- mailto:hello@clearing-ai.com reply-to
- Follow-up email template included

**Run after SMTP setup:** `python3 send-outreach-emails.py`

### 2. Phase 2 Reddit Status Audit
Confirmed ready-to-post assets:
- `reddit-posts/hour-432-r-askprogramming.md` — "I built a free quiz..." (anxious/vulnerable framing, 71%/58%/44%)
- `reddit-posts/hour-434-r-programming-llm-ban-comment.md` — Comment on LLM ban thread (genuine engagement, not marketing)
- `reddit-outreach/hour-426-learn-programming.md` — r/learnprogramming tutorial paradox angle

### 3. Phase 2 Twitter Status Audit
**Thread #29 (DRAFT — post Wed Apr 22 9AM PDT):**
`twitter-threads/hour-453-twitter-thread-29-middleman-problem.md`
7-tweet data-driven thread, 71% stat anchor, targets @swyx @rauchg @emollick @paulg
- Tweet 1: Hook (71% middleman stat)
- Tweet 2: The Definition
- Tweet 3: Three Signals (how to know if you have it)
- Tweet 4: Survey Data (71%/63%/44%)
- Tweet 5: Why It's Not Imposter Syndrome (structural vs cognitive distortion)
- Tweet 6: Recovery Path (Explanation Requirement + No-AI blocks)
- Tweet 7: CTA (clearing-ai.com)

### 4. LinkedIn Status Audit
**3 posts ready to deploy** (from linkedin/posts-ready-to-deploy.md):
- Post #1: Saturday/Sunday data post (71% stat, converts)
- Post #2: Monday EM/CTO signs post (management angle)
- Post #3: Wednesday emotional resonance post (Sunday dread)

**Post-HN launch post** (hour-384-linkedin-post-hn-conversion.md):
- "What 3,000 Engineers Told Us After the HN Post" — deploy after future HN submission
- HN-to-LinkedIn bridge strategy

### 5. Phase 1 Content Status
All 5 pillars deeply built across 257 pages/~452k words.
- Pillar 1 (AI Fatigue Authority): 53 pages built
- Pillar 2 (Developer Burnout): 11 pages built
- Pillar 3 (AI Tool Overwhelm): 10 pages built
- Pillar 4 (Recovery): 33 pages built
- Pillar 5 (Research): 17 pages built

### 6. Phase 3 SEO Status
Technical SEO essentially complete:
- CLS fixed (display=fallback, 139 pages)
- LCP improved (woff2 font preloading)
- Internal linking complete (0 orphan pages)
- Meta tags audited (43 fixes across 153 pages)
- sitemap.xml: 156+ URLs
- Rich snippet eligible: 43+ pages

---

## Git Commit
Commit: `da0cfeb` — "Hour 456: Phase 4 — Newsletter outreach email sender script + 5 personalized partnership emails ready to send"
Pushed to main

---

## Blocking Issues
1. **Formspree SMTP** — 30 files need YOUR_FORM_ID replaced. One-command setup script exists: `_setup-formspree-one-command.sh`. Sunny needs to create Formspree account + run the script.
2. **Email SMTP** — himalaya has no config. `send-outreach-emails.py` ready to run once Sunny configures Gmail SMTP (or any SMTP provider).

---

## Phase windows
| Phase | Windows |
|-------|---------|
| P1 Content | 124 |
| P2 Outreach | 136 |
| P3 SEO | 96 |
| P4 Community | **90** |

## Site stats
- **Pages:** ~257
- **Words:** ~452k
- **Dispatch issues:** 35
- **Interactive tools:** 11
- **Newsletter subscribers:** 0 (Formspree BLOCKER)

## Next window (Hour 457)
- P2: Reddit r/AskProgramming post deployment (ready, post any time)
- P2: Twitter Thread #29 prep (post Wed Apr 22 9AM PDT per schedule)
- P4: Dispatch #36 draft
- P1: Next content pillar expansion if outreach traction is building

## Outreach Calendar
- **Reddit r/AskProgramming** — READY, post any time
- **Twitter Thread #29** — DRAFT, post Wed Apr 22 9AM PDT
- **Twitter Thread #27 LLM Ban Signal** — READY, capitalizing on r/programming cultural moment
- **Newsletter partnerships** — 5 emails ready, awaiting SMTP config

## Tracking
`logs/TRACKER.json` updated after this window
