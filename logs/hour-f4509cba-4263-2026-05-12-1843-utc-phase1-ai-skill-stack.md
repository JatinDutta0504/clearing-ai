# Hour 012 — 2026-05-12 11:43 AM PDT / 18:43 UTC (Phase 1 Window 181)

**Phase:** Phase 1 (Content Pillars) — Rotation: P1=180→181, P2=260, P3=157, P4=127
**Phase selection rationale:** Cron 40/30/20/10 rule mandates Phase 1. P1 at 33% vs target 40%. Building new pillar page that fills genuine content gap.

---

## What I Built

**`the-ai-skill-stack.html`** — "The AI Skill Stack: What Engineers Are Actually Losing"
- ~6,154 words | Article + FAQPage (5 Q&As) + BreadcrumbList schema
- **Word count:** ~6,154 words (verified via regex word count)

**Page structure:**
1. Opening — The question every engineer should ask (self-diagnostic hook)
2. The Three-Layer Skill Stack — visual framework:
   - Layer 1: Execution Skills (⚠️ Declining) — debugging, code writing, reading, decomposition
   - Layer 2: Judgment Skills (🔄 Stable) — architecture, output evaluation, risk assessment
   - Layer 3: Integration Skills (📈 Growing) — prompt engineering, tool orchestration, AI teaching
3. What's Actually Declining — 7-row data table (skill / why / timeline / recoverability)
4. The Compounding Problem — layers feed each other; Layer 1 decline → Layer 2 degrades
5. Interactive Self-Assessment — 5-question quiz with tiered results (significant/moderate/mild/strong Layer 1 decline)
6. Skills That Stay Solid — 6 stable skill categories (communication, systems thinking, institutional knowledge, mentorship, ethical judgment, novel problem solving)
7. Skills Actually Growing — 4 growing skills (prompt engineering, output evaluation, tool orchestration, teaching through AI)
8. 90-Day Rebuild Protocol — 4-step how-to (audit → no-AI blocks → explanation requirement → debug-then-verify)
9. Career implications — who is most at risk
10. Continue exploring grid — 6 internal links

**Key differentiators:**
- First visual framework page on site showing skill stack as a layered model
- Interactive self-assessment with personalized tier results (vanilla JS, no dependencies)
- 7-row data table with timelines for skill decline (featured snippet eligible)
- Connects to skill-atrophy.html and mindset.html as companion pages

**Internal links:** skill-atrophy.html, mindset.html, compare.html, recovery.html, developer-identity.html, no-ai-block.html

**SEO target keywords:**
- "AI skill stack engineers"
- "which coding skills decline from AI"
- "layer 1 execution skills AI"
- "skill atrophy recovery for developers"
- "maintain coding skills with AI tools"
- "AI tool skill decline timeline"

**Schema:** Article + FAQPage (5 Q&As) + BreadcrumbList

**Sitemap:** Added (sitemap.xml updated, now 205 URLs)
**Nav:** Added to 5 pages via Python nav injection (engineer-case-studies, freelance-engineer, quiz-results-tier-3/4, social-badges)

**Note:** Most of the 198 existing pages use a global nav regeneration system (fix-all-navs.py) that would need updating for full nav coverage. The page is accessible via sitemap + internal links from related pages.

---

## SEO Impact

**Why this page matters:**
- "AI skill stack" is a high-intent, underserved keyword cluster — engineers are actively searching for this framework
- Interactive self-assessment keeps users on page longer (engagement signal)
- 7-row data table eligible for featured snippets on "which coding skills decline from AI"
- Connects to 6 high-traffic existing pages via internal links (equity transfer)
- First page to frame AI tool impact as a skill-stack model (unique angle, shareable)

**FAQPage schema:** 5 Q&As eligible for featured snippets on high-intent questions about skill atrophy and AI tool use

---

## Site Status

| Metric | Value |
|--------|-------|
| Pages | 202 (+1 new) |
| Words | ~930k (+6k) |
| Sitemap URLs | 205 (+1) |
| Phase distribution | P1=181, P2=260, P3=157, P4=127 |
| Day Post-Launch | Day 9 |
| Lighthouse Performance | 97 |
| CLS | 0.000413 |

---

## Commit

`75abd2e` — Hour 012: Build the-ai-skill-stack.html — 3-layer skill stack framework with interactive self-assessment quiz. Add to sitemap. Nav update on 5 pages.

---

## Next Window

- **LinkedIn Post 1: "The 90-Second Diagnostic Your Team Needs" — DEPLOY NOW** (was due Sat May 9, now 3 days overdue)
  - File: `linkedin/POST-THIS-linkedin-post-1-saturday.md`
  - Post manually to LinkedIn (no API available)
  - Timing: Best 7-9 AM or 12-1 PM PDT on weekdays
- Twitter Thread #50: The Offload Loop — Wed May 13, 8-10 AM PDT
- Reddit Fresh Pack May 12-18: deploy 2-3 comments today
- Twitter Thread #55: The Estimation Problem — Tue May 13, 8-10 AM PDT
- HN submission: ai-fatigue-in-2026.html — Fri May 15 or Sat May 16, 9 AM PDT

---

**Started:** 2026-03-22 | **Goal:** 100k monthly organic traffic | **Live:** https://clearing-ai.com
