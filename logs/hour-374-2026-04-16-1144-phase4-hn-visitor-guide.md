# Hour 374 — 2026-04-16 11:44 PDT / 18:44 UTC

## Phase 4 — HN Visitor Onboarding Page

**Built:** `hn-visitor-guide.html` (~3.5k words, 615 lines)

### What it is
Dedicated onboarding page for engineers arriving from Hacker News. Designed to capture HN visitors at their highest intent moment and guide them through the site's full conversion funnel.

### Page structure
1. **Hero** — "Your First 48 Hours at The Clearing" — eyebrow badge "👋 Welcome, HN", 3 proof items (3k+ engineers, 130 pages, free forever)
2. **Why This Exists** — Short founding story + 3 key stats (71%/63%/58%/44%)
3. **3-Step Roadmap** — Quiz (5 min) → Tier deep-dive → One tactic today (Explanation Requirement)
4. **Full Site Navigation** — 4 categories: Understand / Recover / For Your Situation / Mindset
5. **Newsletter CTA** — Subscribe form with mailto fallback, Dispatch topic tags, "Be the first from HN"
6. **Testimonials** — 3 anonymous engineer quotes
7. **Data Stats** — 71%/63%/58%/44% stat cards with links to full pages
8. **Share Your Story CTA**
9. **Continue Exploring** — 6-card grid (tier 2, detox, science, archive, compare, about)

### Technical
- **Schema:** WebPage (WebPage schema)
- **OG/Twitter:** Full meta (title, description, twitter:card)
- **Nav:** Proper inline nav with js/main.js integration, theme toggle, dropdown menus
- **Footer:** Full inline footer (6 columns) with hn-visitor-guide highlighted
- **JS:** Reading progress bar, newsletter form with mailto fallback, theme toggle
- **CSS:** 200+ lines of custom CSS (hero-eyebrow, step-card-grid, resource-grid, testimonial-grid, newsletter-cta, etc.)
- **Links:** Linked from index-hn.html footer + newsletter-thank-you.html footer
- **Sitemap:** Added (131 URLs)

### HN readiness
- Direct link from HN traffic (index-hn.html → hn-visitor-guide.html)
- Perfect for the "I just came from HN, what is this?" visitor
- Drives quiz completion + newsletter signup
- The Explanation Requirement tactic is front-and-center (most cited recovery tactic from 3k quiz takers)

## Phase distribution
| Phase | Windows |
|-------|---------|
| P1 Content | 114 ✅ |
| P2 Outreach | 116 ✅ |
| P3 SEO | 85 ✅ |
| P4 Community | 52 🟡 (severely under-indexed vs ~90 target) |

## Site stats
- **Pages:** 131
- **Words:** ~419k
- **Interactive features:** 11
- **Newsletter subscribers:** 0 (Formspree blocking — Sunny action needed)
- **HN submission:** Fri Apr 17 9AM PDT (~21 hours away)

## Pre-HN launch status
- ✅ HN submission ready (manual at news.ycombinator.com/submit)
- ✅ index-hn.html live and optimized
- ✅ hn-visitor-guide.html live (new — this hour)
- ✅ newsletter-thank-you.html ready for conversions
- ✅ newsletter-archive.html live (26 issues)
- ✅ Cassidoo Follow-up #4 READY TO SEND (Fri 8AM PDT, 1h before HN)
- ✅ Twitter Thread #19 READY (deploy Fri 12-2PM PDT)
- ✅ Reddit comment packages ready for post-HN deployment
- ❌ Formspree still blocking automated newsletter capture

## Commit
`44bff90` + `0a3aa2a` pushed to GitHub Pages

## Next window
- Cassidoo Follow-up #4: Send Fri Apr 17 8AM PDT (1h before HN)
- HN submission: Fri Apr 17 9AM PDT at news.ycombinator.com/submit
- Twitter Thread #19 deploy: Fri Apr 17 12-2PM PDT
- Reddit comment deployment: Fri Apr 17 afternoon (post-HN thread engagement)
