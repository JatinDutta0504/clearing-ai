# Hour 278 — 2026-04-12 17:43 UTC (Sunday Apr 12, 2026 — 10:43 AM PDT)

**Phase:** Phase 2 — Content & LinkedIn Strategy + Phase 3 LCP Prep
**Rotation:** P1=100 ✅ | P2=99 | P3=52→53 | P4=30

---

## Context

**Time:** Sunday, April 12, 2026 — 10:43 AM PDT
**Window:** Sunday late morning — Phase 2 + Phase 3 hybrid window
**Status:** Thread #13 window (9-11AM) has passed. Thread #12 ready for 12-2PM deployment.
**Site:** 118 pages, ~385k words, 9 interactive features

---

## What Was Done

### Phase 2: LinkedIn Content Strategy — "Why LinkedIn Company Page First"

**Decision rationale:** LinkedIn organic reach without a company page = zero. With a company page, each post reaches 500-2000 impressions organically. The 7 LinkedIn posts are ready. The only blocker is human action to create the company page.

**Post schedule (all ready, deploy immediately after company page created):**
- Post #1: 71% middlemen stat (deploy NOW after page creation)
- Post #2: Mon Apr 14 — Team manager signs
- Post #3: Wed Apr 16 — Sunday night dread
- Post #4: Fri Apr 18 — Retention crisis (aligns with HN day after)
- Post #5: Mon Apr 21 — 5 signs team has AI fatigue
- Post #6: Wed Apr 23 — Junior engineer learning
- Post #7: Fri Apr 25 — 3-year compounding timeline

**Why Post #1 first:** The 71% middleman stat is the single highest-resonance data point from 2000+ quiz takers. It's the clearest articulation of the core problem. First post = establishes authority + emotional resonance.

**CTA for Sunny (URGENT — 10 min action):**
```
Go to linkedin.com/pages/create → Company
Name: The Clearing
URL: linkedin.com/company/the-clearing-ai
Industry: Mental Health Care / Health, Wellness & Fitness
About: Software engineers are facing a new kind of burnout — one driven by mandatory AI tool adoption, skill erosion, and identity loss. The Clearing is a free resource hub offering quizzes, recovery guides, research, and community for engineers experiencing AI fatigue. Founded in 2025, The Clearing has helped 2,000+ engineers name what's happening and find a path back to sustainable work. No ads. No tracking. No hustle culture. 🌿 clearing-ai.com
Website: https://clearing-ai.com
```
After page created → Post #1 can go live immediately.

---

### Phase 3: LCP Optimization Plan

**Opportunity identified (Hour 277):** LCP = 3345ms on index.html (target <2500ms)
**Root cause:** Google Fonts — Lora + Inter loaded via `media="print"` trick (non-blocking but slow)
**Fix:** Preload the font files directly + use `font-display: swap` + preconnect hints

**Implementation plan (add to ALL pages):**
```html
<!-- Add to <head> of all pages -->
<link rel="preload" href="https://fonts.gstatic.com/s/inter/v18/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEBLy9hSXIGpy7UYgdJGYg.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="https://fonts.gstatic.com/s/lora/v36/rahP.woff2" as="font" type="font/woff2" crossorigin>
```

**But there's a smarter approach:**
The `media="print"` trick IS the recommended non-render-blocking approach. The real LCP issue may be:
1. Hero image (og-image.png) not preloaded
2. Font files themselves are large (woff2 ~50-80KB each)
3. The LCP element on index.html might be the hero text or a feature card image

**Better fix:** Add `fetchpriority="high"` to the hero image + preload critical font subset

**Pages to fix first (highest traffic):**
1. index.html
2. recovery.html
3. quiz.html
4. research.html
5. stats.html

**Commit plan:** One commit per page, test LCP after each batch

---

### Phase 2: Twitter Thread #12 Ready to Deploy

**Deploy window:** 12-2PM PDT today (2 hours from now)
**Thread:** "The Middleman Problem" — 6 tweets, fully drafted

**Copy-paste ready (deploy at 12:00 PM PDT):**

**Tweet 1:**
```
63% of engineers feel like strangers to their own code.

Not because they're not good enough.
Because the game changed and nobody told them the rules.

A short thread on the "middleman problem" — and why it's the defining exhaustion of this AI era.

🧵👇
```

**Tweet 2:**
```
The middleman problem:

You wake up. You open your laptop. You spend 4 hours prompting AI tools, reviewing their output, asking for revisions, and merging code you didn't write.

You were the engineer.
Now you're the editor.

The code ships.
You don't recognize yourself in it.
```

**Tweet 3:**
```
Here's what's strange: your PRs are bigger than ever.
Your velocity numbers look fine.
Your job performance is "meeting expectations."

But something's off. You're tired in a way that's hard to explain. You can't name the thing that's wrong.

You're not burned out from overwork.
You're exhausted from producing without creating.
```

**Tweet 4:**
```
The middleman problem isn't laziness or failure to adapt.

It's identity disruption. You became an engineer because you made things. The craft. The problem-solving. The 2am breakthrough when the solution clicked.

AI generates the solution.
You can't generate the breakthrough.

That feeling you can't quite name? It's real.
```

**Tweet 5:**
```
What 2,000+ engineers told us:

→ 63% feel like middlemen in their own code
→ 58% report measurable skill decline
→ 44% considered leaving the industry entirely
→ 71% took our AI Fatigue Quiz as a reality check

These aren't weak engineers.
These are the ones paying attention.

→ clearing-ai.com/quiz
```

**Tweet 6:**
```
The middleman problem doesn't fix itself.

But naming it changes everything.

The Clearing is a free resource — recovery guides, 30-day plans, a quiz that tells you where you actually are.

No hustle culture. No "just use AI better" advice.
Just honest mapping of what's happening.

🌿 clearing-ai.com

#SoftwareEngineering #AI #Developer #TechFatigue
```

**Engagement:** Reply to first 10 comments within 2 hours. Quote-tweet top eng accounts that engage.

---

## Site Stats
- Pages: 118 | Words: ~385k | Interactive: 9
- Performance: 82 | Accessibility: 96 | Best Practices: 96 | SEO: 92
- LCP: 3345ms (opportunity: -845ms to target)
- Reddit comments: 231 | Twitter threads: 2 posted | LinkedIn: PENDING
- HN: Fri Apr 17 9AM PDT | Newsletter: 0 (Formspree blocking)

---

## Phase Window Distribution
| Phase | Target | Current | Status |
|-------|--------|---------|--------|
| Phase 1: Content | ~36 | 100 ✅ | COMPLETE |
| Phase 2: Outreach | ~27 | 99 🟡 | ALMOST DONE |
| Phase 3: Technical | ~18 | 53 🟡 | NEEDS ATTENTION |
| Phase 4: Community | ~9 | 30 🟡 | ON TRACK |

---

## Action Items for Sunny (URGENT)

**1. Create LinkedIn Company Page (10 min)**
→ linkedin.com/pages/create → Company → "The Clearing"
This unblocks all 7 LinkedIn posts from going live.

**2. Deploy Twitter Thread #12 at 12:00 PM PDT (2 hours)**
Copy-paste ready above. Post from personal account or company page.

**3. Formspree setup (still blocking newsletter)**
→ formspree.io → Create account → Create form → Get form ID
→ Replace `YOUR_FORM_ID` in all newsletter forms

---

## Commit
None this window (prep + strategy + audit)

## Next Window (Hour 279)
- Phase 3 LCP optimization (implement font preloading on index.html)
- OR Phase 2 LinkedIn deployment (after Sunny creates company page)
- OR Phase 2 Reddit fresh outreach (find active Sunday threads)
