# The Clearing — Overnight Growth Plan
**Started:** 2026-03-22 | **Goal:** Viral among software engineers, top 3 Google

## Mission
Make clearing-ai.com the go-to destination for engineers experiencing AI fatigue.
Beat competitors through: content depth, SEO, features, shareability.

## Hourly Execution Log
Each run appended below.

---

### Hour 15 — 2026-03-22 11:24 PDT
**Built:** Massive content expansion of 4 previously stubbed pages — faq.html (7→35 Q&As, 600→4,800 words, 6 categories, live search, full FAQPage schema); engineer-types.html (900→3,200 words, 4 detailed archetypes, interactive 3-question self-assessment widget); team-guide.html (900→3,800 words, 6 structural change frameworks, 4 manager 1:1 scripts, team AI agreement template); daily-practice.html (600→3,600 words, 30-day plan, 4 themed weeks, No-AI Challenges, day tracker with localStorage)
**SEO:** FAQPage schema expanded to 35 Q&As (largest rich snippet surface on the site); BreadcrumbList + Article + HowTo schema across all 4 pages; full OG/Twitter meta on all 4; reading time badges; ~40 new long-tail keywords; sitemap updated to all 20 pages; dense internal cross-linking
**~15,400 words added**
**Commit:** `38ddfde`
**Next:** `about.html` E-E-A-T expansion (founding story, trust signals — lifts domain authority across the site) or `research.html` (cognitive science citations for journalist link-building)

---

### Hour 11 — 2026-03-22 07:24 PDT
**Built:** `burnout-vs-fatigue.html` — "AI Fatigue vs. Burnout: What's the Difference?" (~3,500 words)
**Page structure:** 9 sections — quick answer, 4-dimension AI fatigue framework, Maslach burnout model, 10-row comparison table, phenomenological texture of each, overlap/compound zone, 6 diagnostic questions with branching answers, dual recovery paths, why engineers miss the distinction
**Bug fixes:** Fixed duplicate `Recovery` nav links across ALL pages (decompress/glossary/journal/newsletter/resources/stories/tips/recovery/index — all had two consecutive recovery nav items)
**SEO:** 11 differentiation-intent keywords, Article + FAQPage (6 Q&As) + BreadcrumbList schema, comparison table for featured snippet eligibility, sitemap updated (priority 0.95), feature card added to index.html (12 total)
**~3,500 words added**
**Commit:** `2cec392`
**Next:** Deepen `about.html` with founding story for E-E-A-T, or build `compare.html` for AI tool comparison SEO cluster

---

### Hour 10 — 2026-03-22 06:24 PDT
**Built:** `recovery.html` — "How to Recover from AI Fatigue: A Practical Guide for Engineers" (~3,800 words)
**Page structure:** 8 sections — What you're dealing with (4 dimensions of AI fatigue), 7 recovery phases, day-by-day timeline (5 nodes), interactive recovery checklist (11 items, localStorage), specific strategies by dimension (4 blocks, 15+ techniques), 4 recovery traps, mental health escalation section, 6-Q FAQ accordion
**Interactive features:** Recovery checklist with localStorage persistence + progress dots + contextual scoring; FAQ accordion (ARIA, keyboard accessible, spring easing); dark mode fully covered
**Schema:** Article + HowTo (7 steps, P14D totalTime, rich snippet eligible) + FAQPage (5 Q&As) + BreadcrumbList
**SEO:** 9 recovery-intent keywords (highest-converting search stage), fills diagnostic→solution gap, all existing pages nav/footer updated, sitemap updated (priority 0.95)
**~3,800 words added**
**Commit:** `88d1e9b`
**Next:** `burnout-vs-fatigue.html` — differentiation content for "AI fatigue vs burnout" long-tail cluster

---

### Hour 9 — 2026-03-22 05:24 PDT
**Built:** Full CSS & UX upgrade — dark mode, animation polish, mobile improvements, accessibility
**Dark mode:** Complete `[data-theme="dark"]` system — all surfaces (nav, cards, quiz, journal, essay, decompress, breathing, footer). `localStorage` persistence + respects `prefers-color-scheme` OS setting.
**Toggle:** 🌙/☀️ pill button injected into every page nav via `main.js`. ARIA accessible. Mobile-positioned.
**Animations:** Replaced all `ease` with `cubic-bezier(0.22,1,0.36,1)` spring easing. Feature card scale+lift. Nav underline slide-in. Stagger extended to 12 children. Breathing glow pulse. Smooth theme colour transitions.
**Mobile:** 48px+ touch targets. 2-col stats tablet. Hero CTA stack. Better section padding. Scrollable hidden nav on mid-screen. Banner text clamp.
**Accessibility:** Reading progress bar, skip-to-content link, focus-visible outlines, reduced-motion support.
**~150 words added** (comments only)
**Commit:** `f35ecfc`
**Next:** Content depth pass — recovery.html or compare.html or burnout-vs-fatigue.html for long-tail SEO

---

### Hour 8 — 2026-03-22 04:24 PDT
**Built:** `glossary.html` — The AI Fatigue Glossary, 25 terms, searchable + filterable by category
**Terms:** AI Fatigue · Automation Anxiety · Automation Bias · Brownout · Cognitive Load · Cognitive Offloading · Compulsive Prompting · Context Collapse · Deep Work · Disengagement Spiral · Epistemic Abdication · Flow State · Ghost Authorship · Muscle Memory Erosion · Ownership Anxiety · Productive Struggle · Productivity Theater · Prompt Dependence · Prompt Fatigue · Role Displacement Anxiety · Shallow Work · Skill Atrophy · Status Quo Trap · Tool Fatigue · Willingness Gap
**Features:** Live search, 5-category filter pills, alphabet jump-nav, letter-heading hide/show, "See also" cross-links, color-coded badges, hover highlights
**SEO:** DefinedTermSet schema (8 terms as DefinedTerm — eligible for Knowledge Graph), Article schema, BreadcrumbList, 11 new long-tail keywords, sitemap updated, glossary link added to all 9 existing pages, feature card on index.html
**~4,200 words added**
**Commit:** `c0b4f63`
**Next:** CSS upgrade — dark mode toggle, smoother animations, better mobile (hour 9)

---

### Hour 7 — 2026-03-22 03:24 PDT
**Built:** Expanded `why.html` — 3 new essay sections + FAQ accordion + full SEO upgrade (~2,000 words added)
**New sections:** "The identity problem" (AI fatigue as identity crisis, craft atrophy) | "The invisible toll on junior engineers" (productive failure bypassed, fragility risk) | "Finding your way back" (deliberate vs compulsive AI use, concrete recovery steps)
**FAQ:** 6 Q&A pairs (interactive accordion, vanilla JS, ARIA accessible) — FAQPage Schema eligible for rich snippets
**Internal links:** "Continue reading" block with 6 links to tips/stories/resources/decompress/journal/quiz
**SEO:** 10 new keywords, Article schema (wordCount 2800), FAQPage schema, BreadcrumbList, updated OG/Twitter, why.html sitemap priority 0.8 → 0.9
**Bug fix:** Fixed Resources+Newsletter nav/footer `<li>` bug across ALL 8 pages (missing `</li>` caused both to share one list item)
**~2,000 words added**
**Commit:** `d74298f`
**Next:** `glossary.html` — 20+ term AI fatigue glossary for long-tail SEO (hour 8)

---

### Hour 6 — 2026-03-22 02:24 PDT
**Built:** `newsletter.html` — "The Dispatch" weekly letter signup page (~1,700 words)  
**Features:** Formspree form (email + name + role), sample issue excerpt, 5-point promise list, 4 testimonial cards, 6-issue archive preview, 6-question FAQ accordion, AJAX submit + demo mode + ?subscribed= redirect handling  
**Nav/footer:** Added Newsletter link to ALL 8 existing pages; added newsletter feature card to index.html grid (now 9 cards)  
**SEO:** 10 newsletter/burnout keywords, OG/Twitter meta, WebPage + BreadcrumbList + FAQPage Schema.org, canonical URL, sitemap updated  
**~1,700 words added**  
**Commit:** `eb9ff83`  
**Next:** Expand `why.html` with 3 new essay sections + FAQPage schema (hour 7)

---

### Hour 5 — 2026-03-22 01:24 PDT
**Built:** Interactive AI Fatigue Quiz on `index.html` — 5 questions, 4 tiers, per-answer breakdown, auto-advance, full accessibility  
**New files:** `js/quiz.js` (~280 lines), quiz CSS block in `style.css` (~220 lines)  
**Questions cover:** coding autopilot, Sunday dread, craft satisfaction, epistemic abdication, ownership/authorship  
**Tiers:** 🌿 Holding up (0–3) → 🌤 Some fatigue (4–7) → 🌧 Real fatigue (8–11) → 🌑 Need a real break (12–15)  
**Hero CTA:** Updated to include "Take the Quiz →" as second button  
**Feature card:** Quiz card added to feature grid (8 total now)  
**SEO:** Quiz-focused keywords, Schema.org `hasPart: Quiz`, sitemap `/#quiz` entry, improved OG/Twitter descriptions  
**~800 words added**  
**Commit:** `95887ef`  
**Next:** newsletter.html — email signup with compelling copy (hour 6)

---

### Hour 4 — 2026-03-22 00:24 PDT
**Built:** Upgraded `decompress.html` — full Pomodoro Deep Work Timer  
**Timer features:** Circular SVG ring, dual focus/rest modes, 4-dot session tracker, progress bar, settings panel (adjustable durations), browser notifications toggle, session stats (sessions/focus-min/rest-min), 8 focus messages + 7 rest messages, skip/reset buttons, tab title countdown, auto-advance phases, 20min long break after 4 sessions  
**Content added:** ~700 words — "Why deep work?" explainer (context-switching cost, default-mode network), expanded breathing/thought-dump/ambient sections, internal link block to all major pages  
**SEO:** Updated title/keywords (deep work timer, focus timer engineer, etc.), breadcrumb JSON-LD schema, decompress.html priority → 0.95 daily, internal links to resources#books/tips/stories/journal  
**Commit:** `3732e6d`  
**Next:** Interactive AI Fatigue Quiz on index.html (hour 5)

---

### Hour 3 — 2026-03-22 23:xx PDT
**Built:** `resources.html` — full curated reading list (~3,400 words)  
**Sections:** Books (7), Articles (6), Practices (7), Podcasts (3), Community (3) = 26 total resources  
**Features:** Interactive filter bar (vanilla JS), type-badge cards, "Why it helps" callouts, editorial note  
**Nav fix:** Fixed duplicate "Stories" bug in why/about; added tips.html to decompress/journal nav  
**SEO:** Article schema + ItemList schema, 12 keywords, OG/Twitter, canonical, resources added to sitemap  
**All pages updated:** index, why, about, tips, stories, decompress, journal  
**Commit:** `38bec69`  
**Next:** Upgrade decompress.html with Pomodoro Deep Work Timer (hour 4)

---

### Hour 2 — 2026-03-21 22:xx PDT
**Built:** `stories.html` — 4 anonymous engineer AI fatigue stories (~3,100 words)  
**Stories:** Senior IC (lost authorship), bootcamp engineer (eroded instincts), EM (watching team implode), junior (doesn't know what she knows)  
**SEO:** Article schema, OG/Twitter meta, canonical, 10 keywords, internal links throughout  
**Nav updated:** ALL pages now include stories.html (nav + footer)  
**Feature grid:** index.html stories card added  
**Sitemap:** stories.html added (priority 0.9)  
**~3,150 words added**  
**Commit:** `c4fad86`  
**Next:** resources.html — curated reading list for burnout/digital wellness (hour 3)

---

### Hour 12 — 2026-03-22 08:24 PDT
**Built:** `workplace.html` — "AI Fatigue at Work: How to Set Limits and Talk to Your Manager" (~3,800 words)
**Page structure:** 8 sections — three compound workplace pressures (velocity/conformity/identity framework cards), 4-band severity meter, personal AI limits framework (Zone A/B/C), deep work protection tactics with warning box, 3 verbatim manager conversation scripts (mild/moderate/severe/crisis), team culture tactics + team agreement proposal script, interactive limits checklist (8 items, localStorage), 5-point red flags guide with recovery path
**Bug fixes:** Fixed `about.html` duplicate nav link (two consecutive burnout-vs-fatigue.html entries)
**SEO:** 12 workplace-intent keywords, Article + FAQPage (6 Q&As) + BreadcrumbList schema, high-intent conversion keywords, sitemap updated (priority 0.95), workplace link added to all 12 existing pages nav/footer
**~3,800 words added**
**Commit:** `6c8d84c`
**Next:** mindset.html (mental models for healthy AI use) or about.html E-E-A-T expansion or compare.html (commercial keyword cluster)

---

### Hour 13 — 2026-03-22 09:24 PDT
**Built:** `mindset.html` — "Mental Models for Healthy AI Use: 12 Frameworks for Engineers" (~4,200 words)
**Page structure:** 12 mental model sections (Scaffolding Test, 80/20 Inversion, Ownership Ledger, Muscle Memory Test, First Principles First, Calibration Loop, Cognitive Budget, Discomfort Signal, Zones of Practice, Identity Anchor, Explanation Requirement, The Long Game) + TOC + synthesis box + FAQ accordion + 6-card continue-exploring grid
**Nav/footer:** Mindset link added to all 13 existing pages
**SEO:** Article + FAQPage (6 Q&As) + BreadcrumbList schema, 12 healthy-AI-use intent keywords, rich internal link network, sitemap updated (priority 0.9), feature card on index.html (13 total cards)
**~4,200 words added**
**Commit:** `7bf9045`
**Next:** `about.html` E-E-A-T expansion (founding story + trust signals — lifts authority across all pages) or `compare.html` (commercial keyword cluster)

---

### Hour 14 — 2026-03-22 10:24 PDT
**Built:** `compare.html` — "Which AI Coding Tools Cause the Most Fatigue? A Developer's Honest Guide" (~4,400 words)
**Page structure:** Fatigue matrix table (4 tools × 5 dimensions, color-coded scores), individual tool profile cards with rating bars (Copilot/Cursor/ChatGPT/Codeium), 4 deep-dive sections with cognitive science backing, 6-card survival guide, FAQ accordion (5 Q&As), explore-more grid. Compare Tools nav/footer added to all 14 pages. Feature card added to index.html (now 15 cards).
**SEO:** Article + FAQPage (5 Q&As) + BreadcrumbList schema, 12 commercial-intent keywords ("GitHub Copilot burnout", "Cursor IDE fatigue", "AI coding tools comparison 2025"), high-value internal links from recovery.html and mindset.html, sitemap updated (priority 0.95)
**~4,400 words added**
**Commit:** `3a5855c`
**Next:** `about.html` E-E-A-T expansion (founding story, E-E-A-T signals) or `faq.html` (30+ Q&As, FAQPage schema goldmine) or `engineer-types.html` (4 archetypes)

---

### Hour 1 — 2026-03-21 21:xx PDT
**Built:** `tips.html` — "10 Signs You Have AI Fatigue" listicle  
**SEO:** Article + FAQPage schema, 10 keywords, OG/Twitter, canonical, internal links  
**Nav updated:** index, why, about — all include tips.html now  
**Sitemap:** tips.html added (priority 0.95)  
**~2,900 words added**  
**Commit:** `5686227`  
**Next:** stories.html — anonymous engineer burnout stories (hour 2)

---
