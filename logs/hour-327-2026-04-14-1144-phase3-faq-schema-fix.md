# Hour 327 — 2026-04-14T11:44:00Z (Phase 3 Window 70)

## Phase Rotation
P1=108 ✅ | P2=108 ✅ | P3=69→70 🟡 (underindexed — this window corrects) | P4=37 🔴

## Context
- **HN submission:** Fri Apr 17 9AM PDT (3 days away)
- **Site:** 121 pages, ~396k words, 9 interactive features
- **Phase balance:** P3 most underindexed (69 vs P1/P2=108). This window focused on P3.

## This Window: Phase 3 Technical SEO — FAQ Schema Hidden-Content Fix

### The Problem Discovered
During an audit of recent pages, discovered that `golden-handcuffs-ai-engineers.html` and `why-resting-doesnt-fix-ai-fatigue.html` both had FAQPage JSON-LD schema in their `<head>` but **zero visible FAQ content** in the HTML body.

Google's rich snippet guidelines require that FAQ content marked up with FAQPage schema be **visible to users**. Pages with FAQ schema but no visible FAQ HTML are at risk of:
- Rich snippet demotion (Google ignores the schema)
- Manual action in severe cases (structured data abuse)
- Loss of SERP real estate (FAQ featured snippets)

### Fix Applied

**`why-resting-doesnt-fix-ai-fatigue.html` (~2,975 words):**
- Added 6-question FAQ accordion section before "Continue Exploring"
- Questions: rest vs reconstruction / burnout vs AI fatigue / skill recovery timeline / quitting AI tools / guilt after rest / manager conversation
- FAQPage JSON-LD already existed — now matched with visible content
- Natural fit: conceptual article raises these exact questions

**`golden-handcuffs-ai-engineers.html` (~3,767 words):**
- Added 6-question FAQ accordion section before "Continue Exploring" 
- Questions: why high-paid engineers feel trapped / selfish to quit high-pay / golden handcuffs vs friction / manager solutions / fixing without quitting / freelance trap
- FAQPage JSON-LD already existed with 6 questions — now matched with visible content
- Structural fix: `<details>/<summary>` with main.js accordion (same pattern as ai-code-review-fatigue.html)

### Schema-Content Matching
| Page | Before | After |
|------|--------|-------|
| why-resting-doesnt-fix-ai-fatigue.html | FAQPage JSON-LD ✅, 0 visible FAQs ❌ | FAQPage JSON-LD ✅, 6 visible FAQs ✅ |
| golden-handcuffs-ai-engineers.html | FAQPage JSON-LD ✅, 0 visible FAQs ❌ | FAQPage JSON-LD ✅, 6 visible FAQs ✅ |

### Technical SEO Impact
- **Rich snippet eligibility:** Both pages now properly eligible (not just schema-declared)
- **Google compliance:** Fixes potential structured data abuse flag
- **CTR improvement:** FAQ snippets in SERPs = more real estate, higher click-through
- **Estimated lift:** +5-10% CTR on these pages from FAQ snippet display

### Git
- Commit `e57617d`: FAQ section additions to both pages
- Commit `426a494`: TRACKER.json update — P3=70

## Phase Distribution
- P1: 108 ✅ (target ~36)
- P2: 108 ✅ (target ~27)
- P3: 69 → 70 🟡 (target ~18 — still needs ~5-8 more windows)
- P4: 37 🔴 (target ~9 — most underindexed, Formspree blocking)

## Site Status
- Pages: 121 | Words: ~396k | Interactive: 9
- Rich snippet eligible: 43+ pages (2 more fixed this window)
- Technical SEO: 99/100
- Sitemap: 121 URLs, 0 duplicates, 0 missing files
- HN: Fri Apr 17 9AM PDT (3 days)

## Blocking Issues
- **Formspree newsletter setup:** Sunny action needed (5-min setup, blocks automated email capture)
- **LinkedIn company page:** Sunny action needed at linkedin.com/pages/create

## Next Window (Hour 328)
- Phase 2: HN final pre-flight + Twitter Thread #15 deploy package ready
- OR Phase 4: Newsletter growth push (Dispatch #17 ready to send to first subscribers once Formspree active)
- OR Phase 3: Continue technical audit (WCAG accessibility deep-dive on newest pages)

**Started:** 2026-04-14T11:44:00Z
**Phase:** Phase 3 (Technical SEO — underindexed correction)
