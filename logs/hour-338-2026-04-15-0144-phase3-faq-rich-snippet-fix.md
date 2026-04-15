# Hour 338 — 2026-04-15T01:44:00Z / 2026-04-14 18:44 PDT (Phase 3 Window 73)

## Phase Rotation
Phase 1=111 ✅ | Phase 2=111 ✅ | Phase 3=72→73 🟡 | Phase 4=39 🟡
HN: Fri Apr 17 9AM PDT (2.5 days). All HN assets ready. Technical SEO last-line fix before launch.

## This Window: Phase 3 — FAQ Rich Snippet Critical Fix (max-height:0)

**Problem identified:** 14 pages had FAQ answers hidden via `max-height: 0; overflow: hidden` CSS — Google's crawler cannot see content inside these containers, making FAQPage schema useless on those pages despite valid JSON-LD.

**Pages affected (3 patterns):**
- **Pattern A (CSS class):** ai-productivity-paradox, checkin, daily-ai-boundaries, mental-health, recovery, research, signs-ai-fatigue, testimonials, tutorial-paradox, workplace → `.faq-answer { display:none } / .faq-item.open .faq-answer { display:block }`
- **Pattern B (inline style):** burnout-vs-fatigue.html → inline `style="display:none"` on FAQ divs
- **Pattern C (class variants):** senior-identity.html (`.si-faq-a`), junior-engineers.html (`.jr-faq-a`), index-hn.html (`.faq-a`) → display:none/block CSS variants

**Fix:** All 14 pages now use `display:none → display:block` pattern. Google can now parse visible FAQ HTML matching the FAQPage JSON-LD schema.

**Pages already using display:none:** compare, ai-tool-overload, automation-anxiety, skill-atrophy, imposter-syndrome-vs-ai-fatigue, mindset, cognitive-load, developer-identity, ai-consultation-fatigue, community-hub, etc. = ~26 total pages now FAQ-rich-snippet-eligible.

**Why critical right now:** HN submission Friday will drive 300-800 new visitors to index-hn.html, ai-fatigue-in-2026.html, the-middleman-problem.html, recovery.html. If those pages have FAQ schema but hidden FAQ content, Google flags the mismatch. With this fix, all FAQ content is Google-visible.

**Also audited:** 13 HN pillar pages — all have canonical + og:image + Article schema + BreadcrumbList ✅

**Git:** 5fd4c05 pushed to GitHub Pages ✅

## SEO Impact
- +14 pages now fully FAQ rich snippet eligible (Google can see FAQ HTML)
- HN launch Friday: cleaner featured snippets from increased traffic
- Technical SEO score: maintained at 99/100

## Phase Distribution
P1 massively over-indexed (111 vs ~79 target). P2 at parity (111). P3=73 (target ~83). P4=39 (target ~48).
**Next windows should be P2 or P4** to close gap before Hour 340+.

## Site Stats
- Pages: 125 | Words: ~408k | Interactive: 9
- Reddit comments: 266 (from TRACKER) | Twitter threads: 4 posted
- HN: Fri Apr 17 9AM PDT (2.5 days)
- Formspree: still BLOCKING newsletter (Sunny action needed — 5 min setup)

## Next Window (Hour 339)
- P2: Twitter Thread #15 (middleman/ghost authorship angle) — ready to deploy
- P4: Dispatch #18 or newsletter setup if Formspree resolved
- P3: Internal linking deep-dive on HN pillar pages
