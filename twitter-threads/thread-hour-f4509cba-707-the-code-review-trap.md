# Twitter Thread #73 — The Code Review Trap
# Hour f4509cba-707 — Fresh thread
# Theme: AI code review makes you faster at approving and slower at catching — the reviewer's paradox
# Target: Senior engineers, tech leads, anyone who reviews code
# Deploy: Mon May 19, 9am PST (follow-up to Estimation Paradox on Thu May 15)

---

## TWEET 1 (Hook)

You review 50 PRs a week now.

You're not reviewing better. You're reviewing faster.

There's a difference, and it's costing you.

---

## TWEET 2 (What's Changed)

Before AI code review:

You read the diff carefully. You built a mental model of what this change was trying to do. You caught the logic error because you were actually thinking about the system.

Time per review: 15 minutes. Depth: high.

After AI code review:

AI flags the obvious issues. You scan the remaining diff. You approve. Your brain is on autopilot.

Time per review: 5 minutes. Depth: surface.

---

## TWEET 3 (The Specific Problem)

When AI reviews code, it tells you where to look.

You go there. You look. You approve.

You never had to build the full-system picture. AI already did it for you. You just verified its work.

What you lost: the act of building the mental model yourself. That act is where review skill lives.

---

## TWEET 4 (Why This Shows Up Late)

Code review skill decline is silent.

The bugs that get through don't feel like "I missed this because AI made me shallow."

They feel like "huh, that was a tricky one, how did we miss it."

You're not aware it's happening. The output looks fine. Your reviews still pass. The degradation is invisible.

---

## TWEET 5 (The Expertise Reversal Problem)

Kalyuga's Expertise Reversal Effect explains this precisely:

Your code review skill was highest when you were doing the hardest reviews — where you had to really think.

AI removes the hard part. You review fewer hard problems. Your skill at the hardest reviews declines.

You get better at the easy reviews (which AI handles) and worse at the hard ones (which AI can't fully handle).

The result: you can catch simple bugs. The complex ones that need genuine judgment? You're slower at catching those than you used to be.

---

## TWEET 6 (What To Do)

The fix isn't to reject AI review.

It's to review AI's review before you approve:

→ Read what AI flagged and ask: "Would I have flagged that?"
→ Scan the diff without AI flags: "Is there anything I notice that AI missed?"
→ The cognitive practice is in the asking, not the answer

You're protecting the skill by keeping the mental model active, even when AI helps.

---

## TWEET 7 (The Deep Fix)

Once a week: do a "deep review" of a complex PR without AI running first.

Not to catch more bugs. To practice building the full-system mental model.

The skill that matters in complex code review isn't "can you spot the bug." It's "can you hold the whole system in your head and see where this change doesn't fit."

That skill only survives if you practice it.

---

## TWEET 8 (CTA)

The "AI Code Review Fatigue" guide at clearing-ai.com goes deeper: why AI review erodes the reviewer's skill, the Expertise Reversal Effect, and the specific weekly practice that keeps your review judgment sharp.

Not "stop using AI review." Just "know what you're losing when you let AI do the thinking."

---

## Posting notes:
- **Best time:** Mon May 19, 9am PST (start of week — strong for senior engineers planning their week)
- **Alternative:** Wed May 20, 8am PST
- **Hook:** "50 PRs a week, not reviewing better" — specific quantity that resonates with anyone who reviews code daily
- **Target:** Senior engineers, tech leads, staff engineers, anyone who reviews code frequently
- **Complementary to:** Thread #72 (Estimation Paradox, Thu May 15) — same theme (AI optimizes review/estimation, erodes underlying skill)
- **Tag possibility:** None — keep it clean for broad reach
- **Hashtags:** #SoftwareEngineering #CodeReview #AIFatigue (2 max)

## Thread metadata:
```
thread_number: 73
theme: The Code Review Trap
scheduled: Mon May 19, 9am PST
status: READY
link: clearing-ai.com/ai-code-review-fatigue
chars: ~3,300
tweets: 8
pipeline_position: Thread #73
previous_thread: Thread #72 (Estimation Paradox, Thu May 15 9am)
next_thread_needed: Thread #74 (for May 22-26 window)
```

## SEO notes:
- Links to: ai-code-review-fatigue.html (pillar page, ~3,400 words)
- Theme: "AI code review fatigue", "code review skill erosion", "senior engineer code review AI", "software engineering review quality"
- Related threads: Estimation Paradox (#72), Debugging Paradox (#49), Competence Illusion (#63) — all share the "AI optimizes X, erodes the skill behind X" pattern
- Shareable by: engineering Twitter, tech leads, senior IC communities, code review tooling discussions (GitHub, Linear)