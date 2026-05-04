# AI Brain Fry — The Engineering Diagnosis

## Quick Summary

A rapid-fire 60-second self-assessment for engineers to determine if they're experiencing "AI brain fry" — the cognitive exhaustion specific to AI-assisted work. Created as a companion to Harvard Business Review's March 2026 "AI brain fry" research, framed for the engineering-specific experience.

**Target users:** HN visitors, Reddit visitors, Twitter visitors who want to know "is this me?"
**Conversion goal:** Quiz taker → Newsletter subscriber → Share the badge

---

## Page: `ai-brain-fry.html`

### Concept
The Harvard Business Review coined "AI brain fry" in March 2026 — mental fatigue from excessive use or oversight of AI tools beyond cognitive capacity. Most coverage is in business/management media. This page is The Clearing's engineering-specific version: named, framed, quantified, actionable.

This is NOT another full-page essay. It's a:
1. **Recognition tool** — "do you have this?" (4 quick questions)
2. **Explanatory framework** — why AI creates this specific cognitive pattern
3. **Severity classifier** — mild / moderate / severe / critical
4. **Action pathway** — what to do based on severity

Format: fast-scanning, mobile-friendly, low-word-count, high-utility. Designed for the engineer who lands from HN and has 60 seconds.

---

## Content Sections

### Section 1: Hero — "AI Brain Fry: The Engineering Diagnosis"

**Subtitle:** "Harvard named it. We mapped it for engineers."

**Hook paragraph (2-3 sentences):**
Harvard Business Review just published research on "AI brain fry" — mental fatigue specific to AI-assisted work. If you've been trying to explain why you feel cognitively depleted despite shipping more code, this is the framework you've been looking for. This is the engineering-specific version.

**4-question quick assessment** (radio buttons, JS-scored):
1. **After a full weekend, how do you feel about Monday morning?**
   - Rested but still dread it → 1 point
   - Somewhat better but not fully recovered → 2 points
   - Just as tired as before the weekend → 3 points

2. **Can you explain your system's architecture without looking at anything?**
   - Yes, completely → 0 points
   - Mostly, with some gaps → 1 point
   - Significant gaps — I know what it does, not how it works → 2 points
   - I couldn't walk someone through it at all → 3 points

3. **When you solve a problem with AI, how much do you retain?**
   - I understand it fully after → 0 points
   - I understand it partially → 1 point
   - I can use it but couldn't explain why it works → 2 points
   - I forget it immediately after accepting → 3 points

4. **How does your output compare to 18 months ago?**
   - More output, same or better understanding → 0 points
   - More output, less understanding → 1 point
   - Same output, less understanding → 2 points
   - I genuinely can't tell anymore → 3 points

**Scoring display:**
- 0-4: Mild — "You have some AI fatigue signals. Worth watching."
- 5-7: Moderate — "You're in the AI brain fry zone. This is real."
- 8-10: Severe — "Classic AI brain fry pattern. Recovery work needed."
- 11-12: Critical — "Please read the recovery section. Today."

### Section 2: What AI Brain Fry Actually Is

**The short version:**
The exhaustion isn't from working too hard. It's from the specific cognitive mode AI forces — rapid context-switching between generation and evaluation, without the deep processing periods that make work feel complete.

**The engineering-specific mechanics:**
- You write code, then mentally evaluate whether the AI's suggestion was right
- Then decide whether to accept it
- Then model what the AI was thinking when it produced it
- That's two cognitive processes simultaneously, every few minutes
- The work looks the same from the outside
- It costs twice as much from the inside

**Key insight box:**
Standard rest doesn't fix AI brain fry. Only pattern change does. Taking a vacation helps temporarily. Structuring your work differently fixes it structurally.

### Section 3: Why Engineers Feel It Most

**Three structural reasons (cards):**
1. **Rapid evaluation loop** — AI generates fast. You evaluate fast. The loop never stops. No natural completion point.
2. **Expertise Reversal Effect** — The more you know, the more cognitive load AI creates for you. Senior engineers often feel it worse than juniors.
3. **Ghost authorship** — Shipping code you didn't fully author creates a specific identity dissonance. It costs something even when it looks productive.

### Section 4: Severity Guide

| Score | Severity | What it means | What to do |
|-------|----------|---------------|-----------|
| 0-4 | Mild | Early stage. Mostly normal. | Watch it. Try Explanation Requirement. |
| 5-7 | Moderate | Clear AI brain fry signals. | No-AI mornings. Quarterly rebuilds. |
| 8-10 | Severe | Pattern is established. Recovery needed. | Full 30-day plan. Consider talking to your manager. |
| 11-12 | Critical | Significant cognitive erosion. | Prioritize recovery immediately. See the crisis section. |

### Section 5: What Actually Helps

**5 evidence-based practices:**
1. **Explanation Requirement** — After accepting any significant AI solution, write out why it works (from memory). The gaps are what didn't transfer.
2. **No-AI mornings** — 90 minutes of first-draft work without AI. Let your brain remember that cognitive mode.
3. **Quarterly rebuilds** — Once per quarter, build something significant without AI. The struggle is where the skill lives.
4. **Batch AI use** — Don't use AI throughout. Do all the thinking first, then use AI to execute. Fewer context switches = less cognitive overhead.
5. **Weekly calibration** — Can you explain your system architecture from memory? If not, that's the skill gap. Rebuild it.

### Section 6: The Crisis Signal

**When to take this seriously:**
If any of these are true, this is beyond "try some boundaries":
- You've considered leaving tech in the last 6 months
- You can't remember the last time you felt proud of code you wrote
- You couldn't explain your system's architecture to a junior engineer right now
- The idea of a no-AI debugging session makes you anxious (not motivated — anxious)

**Crisis resources:**
If you're in a bad place: 988 (Suicide & Crisis Lifeline) | 741741 (Crisis Text Line) | findahelpline.com

### Section 7: Continue Exploring

**Cards linking to:**
- The full AI Fatigue Quiz → quiz.html
- 30-Day Recovery Plan → ai-detox-plan.html
- The Science of AI Fatigue → research.html
- Skill Atrophy Framework → skill-atrophy.html

---

## Schema

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "AI Brain Fry: The Engineering Diagnosis",
  "description": "4-question self-assessment for engineers experiencing cognitive exhaustion from AI-assisted work. Companion to Harvard Business Review March 2026 AI brain fry research.",
  "url": "https://clearing-ai.com/ai-brain-fry.html",
  "isPartOf": {
    "@type": "WebSite",
    "name": "The Clearing"
  }
}
```

Plus FAQPage schema with 4 Q&As:
1. What is AI brain fry? (150 words)
2. How is AI brain fry different from burnout? (120 words)
3. Does this only affect engineers who use AI too much? (100 words)
4. I'm a senior engineer and I feel this worse than juniors — why? (100 words)

---

## Design Notes

- **Format:** Single-column, fast-scanning, mobile-first. Short paragraphs. Cards for lists.
- **Visual:** Simple. Dark mode. Green/amber/red severity color coding.
- **Interactive:** 4-question JS quiz with instant score display and severity tier.
- **Word count:** ~1,800 words. Designed to be read in 60 seconds.
- **CTAs:** Quiz link, Recovery plan link, Newsletter signup.
- **Internal links:** 5 cards linking to existing high-authority pages.
- **External citation:** HBR "When Using AI Leads to Brain Fry" (March 2026) — link to article.

---

## Filename
`ai-brain-fry.html`

## Site updates needed
1. Nav: Add to "Tools" or "Recover" dropdown (after quiz.html or ai-fatigue-checklist.html)
2. Footer: Add link across all 181 pages
3. sitemap.xml: Add ai-brain-fry.html (priority 0.85)
4. sitemap.html: Add to Tools section
5. index.html: Feature card added
6. Git commit
7. Discord DM to user 1479253933909348413

## Launch relevance
- Perfect HN companion: "Harvard named it. We mapped it for engineers."
- Reddit AI brain fry pack: ai-brain-fry.html is the destination URL for the "more at clearing-ai.com" signal
- Twitter: New branded term we now own in engineering space
- Newsletter Day-14: Can reference "AI Brain Fry: The Engineering Diagnosis" as new content

## Commit message
"Hour F4509cba: ai-brain-fry.html — 4-question engineering diagnosis, HBR companion, ~1.8k words"
