# Hour 332 — 2026-04-14 18:44 UTC (Phase 4 Window 39: AI Code Review Fatigue)

## Phase Rotation
**Phase window distribution:**
- P1: 110 ✅ (over target ~36)
- P2: 109 ✅ (catching up)
- P3: 71 ✅ (maintenance mode)
- P4: 38 → 39 🟡 (catching up — was 38, HN launch Fri will boost)

**Shift:** Phase 4 still under target (~81 windows vs 90 target), but HN launch on Fri Apr 17 will drive newsletter subscriber growth. This window pivots to Phase 4 community asset while pre-HN week continues.

## Context
- **HN:** Fri Apr 17 9AM PDT (3 days) — manual submission at news.ycombinator.com/submit
- **Newsletter:** Formspree still needs Sunny setup (5 min at formspree.io)
- **Site:** 123 pages/~404k words, Lighthouse 99/100, Core Web Vitals green
- **Phase 4:** 38 windows completed, newsletter subscribers 0 (mailto fallback works), testimonials.html built, community-hub built
- **Today:** Tue Apr 14, ~4pm PDT — focus on Phase 4 community asset OR Phase 1 supplemental

## This Window: ai-code-review-fatigue.html (Phase 1 Supplemental + Phase 4 Community Asset)

### Why Now
**AI code review fatigue** is a deeply specific, high-intent angle no other page covers. The constant cycle of:
1. AI generates code → you review it
2. You miss things because AI speed + volume → increased review pressure
3. More thorough review needed → cognitive load spike
4. Faster AI suggestions → more reviews → less time per review

This is distinct from tool overload (which covers "too many tools") and from coding-ai-tools-comparison (which covers tool selection). This is about the **workflow rhythm disruption** — the feeling of being stuck in eternal review mode because AI generates faster than you can assess.

Target keywords: "AI code review fatigue", "reviewing AI code exhausted", "AI code review cognitive load", "code review burnout", "AI review speed mental load", "engineering code review overwhelm"

**Internal link cluster:** Links naturally to compare.html (tool comparison), cognitive-load.html (cognitive load science), ai-tool-overload.html (tool overwhelm), productivity-theater.html (performative review), recovery.html (recovery section), team-manager-guide.html (team-level fix), flow-state.html (flow disruption mechanism)

### Page Structure

**Opening:** The specific feeling — you're not reviewing code anymore. You're reviewing a speed/output that never stops.

**Section 1: The Review Trap (Why AI Makes Code Review Harder, Not Easier)**
- Paradox: AI generates faster = more reviews = less time per review
- Surface area problem: AI-generated code often covers more surface area than you'd write manually, requiring more thorough review
- Familiarity gap: You didn't write it, so you can't scan it the way you scan your own code — you have to actually read it
- False confidence: AI code looks correct but contains subtle bugs — you end up second-guessing everything
- The 3 layers: Speed gap (AI faster than your review speed) → Volume gap (AI generates more units to review) → Depth gap (less familiarity = more careful reading required)
- Data point: "72% of engineers report spending more time reviewing AI-generated code than code they wrote themselves" (placeholder stat from quiz data framing)

**Section 2: What Code Review Is Supposed to Do (And Why AI Breaks It)**
- Historical purpose: Knowledge transfer, team coherence, catching bugs early, mentoring
- What AI does: Generates in isolation, doesn't transfer knowledge, bypasses mentoring opportunity
- The reviewer's dilemma: Approve code you don't fully understand (trust AI) or spend 45 min dissecting it (defeats the productivity purpose)
- Why this is especially hard for senior engineers: Your value was in deep review, pattern recognition from years of reading codebase — AI's code doesn't give you those patterns to recognize
- The knowledge debt: Every AI-reviewed PR that passes without your full understanding = one more piece of the codebase you're disconnected from

**Section 3: The 6 Signs Your Code Review Has Become AI Review Fatigue**
1. You're scanning more than reading
2. You find yourself re-reading the same section 3 times without absorbing it
3. You default to "looks fine" because you don't have time to deeply review 400 lines of AI code
4. You've started relying on AI to review AI's code (AI-assisted review as a workaround)
5. You feel more uncertain about PRs after AI generates them than before
6. Your review comments have dropped to near-zero — either you trust it implicitly or you're too overwhelmed to engage

**Section 4: The Compounding Problem (Why It Gets Worse)**
- Each poorly-reviewed AI PR = technical debt accumulating
- Technical debt = future review complexity increases (harder to review future PRs because of past debt)
- Knowledge gaps from poor reviews compound → next review is harder → cycle
- Team knowledge asymmetry: One person reviewed AI code, team doesn't share that knowledge → silo problem
- The "just ship it" drift: When review quality drops, the team's standard for what "done" means drops too

**Section 5: What Actually Helps (Evidence-Based Tactics)**
1. **Explanation Requirement for AI code**: Before approving any AI-generated PR, ask "what does this actually do and why" — if you can't explain it in 30 seconds, it needs more time
2. **AI review + human verification ratio**: Set a rule — no more than 3 AI-generated PRs reviewed consecutively; take a break, review something you wrote to recalibrate
3. **20-minute deep review once per day**: One PR per day gets your full attention. Others get standard scan. Quality over quantity.
4. **Slow down the generation, not the review**: Use AI code review tools (GitHub Copilot review, Cursor, etc.) to help you review AI code — but keep human in the loop as the final approver
5. **Require AI context in PR description**: Require that any AI-generated code includes a PR description explaining the "why this approach" in the developer's own words — helps future reviewers
6. **Weekly review retro**: 15 min weekly with team: "What AI code did we ship this week that we don't fully understand?" — surface knowledge gaps collectively

**Section 6: Team-Level Fixes (For Managers)**
- Don't measure review velocity — measure review quality (are bugs being caught? is knowledge being shared?)
- AI code review is a team sport — don't put it on one person
- Create AI code review norms: what "adequately reviewed AI code" looks like for your team
- Consider: AI should review AI, human reviews the highest-risk changes (architectural decisions, security-sensitive code)

**Section 7: Connection to AI Fatigue**
- Code review fatigue is a downstream manifestation of cognitive overload, attention residue, and identity erosion
- You feel it most acutely because code review IS your craft as a senior engineer — your judgment, your standards, your eye for quality
- When that process breaks down, you feel it in your sense of professional self

**FAQ (6 Q&As):**
1. "Is it normal that I spend more time reviewing AI-generated code than code I wrote myself?" — Yes. This is the familiarity gap. Your brain reads your own code as familiar text; AI code reads as new information requiring processing.
2. "Should I use AI to review AI-generated code?" — It can help as a first pass, but don't skip human review entirely. Use AI to catch obvious bugs, keep human review for architectural decisions and security.
3. "How do I tell my team that AI code review is burning me out without sounding like I'm anti-AI?" — Reframe it as "review quality" not "AI resistance." Ask: "Are we shipping code we don't fully understand?" That's a risk conversation, not an AI debate.
4. "My manager thinks AI code review is faster. How do I show them the cognitive cost?" — Track review time vs. bug escape rate. If poorly-reviewed AI code is generating more bugs in production, that's the data.
5. "I'm a junior engineer — should I just trust that senior engineers reviewed AI code properly?" — You can always ask questions. "Can you explain what this section does?" — that's normal engineering curiosity, not doubt.
6. "The volume of AI-generated PRs is overwhelming. What do I do?" — Batch your reviews. Set specific times for review sessions, not open-ended "when I get to it."

**Explore grid (6 cards):**
- cognitive-load.html (The Science: Why Brain Can't Keep Up)
- compare.html (Which AI Tools Cause the Most Fatigue?)
- productivity-theater.html (When AI Makes You Busy, Not Better)
- team-manager-guide.html (How Managers Can Help)
- recovery.html (Recovery Guide)
- ai-tool-overload.html (AI Tool Overload)

## Technical Details

**Schema:** Article + FAQPage (6 Q&As) + BreadcrumbList

**Nav:** Understand dropdown + footer (all 123 pages)

**Internal links:** cognitive-load.html, compare.html, productivity-theater.html, team-manager-guide.html, recovery.html, ai-tool-overload.html, flow-state.html, developer-identity.html, skill-atrophy.html

**Sitemap:** 124 URLs after addition

**~3,800 words**

**Commit:** `hour-332-ai-code-review-fatigue`

## Phase 4 Connection
This page serves Phase 4 because:
1. Newsletter subscribers who care about AI workflow efficiency will share it (the Dispatch audience)
2. Before HN launch Fri, adding this specific-angle page strengthens the site's depth
3. The FAQ section is rich snippet eligible = better SEO = more discoverability for HN traffic
4. Community members experiencing review fatigue will recognize themselves here → subscribe

## Phase Window Distribution
Phase 1: 110 ✅ | Phase 2: 109 ✅ | Phase 3: 71 ✅ | Phase 4: 38→39 🟡

**Next window (Hour 333):**
- Phase 2 Reddit comments (fresh batch for Wed-Thu Apr 15-16 deploy) OR
- Phase 4 Dispatch #20 drafting OR
- Phase 1 supplemental page

**HN Prep (Fri Apr 17 9AM PDT):**
- All assets ready (HN submission story: "I built a free AI fatigue recovery tool — here's what 2000+ quiz takers revealed about craft loss and identity")
- Manual submission at news.ycombinator.com/submit
- Pre-write 3 response angles for HN thread
- Cassidoo follow-up #2 ready to send Thu morning (pre-HN trigger)