# The Comprehension Gap
### Issue #105 — May 31, 2026

---

Last week we talked about the fluency illusion — the difference between understanding an explanation and actually understanding something.

This week: what the gap costs you, and one way to measure whether you're growing or just moving faster.

---

## The Gap Nobody Talks About

There's a specific moment that shows up in debugging sessions, architecture reviews, and 2am incidents.

You open a system you worked on six months ago. The AI built most of it. You approved the work. You shipped it.

And now — without AI in the room — you realize you can't explain it. Not fully. Not from first principles. Not without reaching for the output you don't have access to right now.

This isn't a moral failure. It's not about being a bad engineer.

It's what happens when the work of understanding gets outsourced to the same system that did the building.

---

## Three Places the Gap Shows Up

**In incidents.**

When something breaks at 2am and your AI tab is closed, you're the one in the room. If your understanding is explanation-based rather than model-based, you spend the first twenty minutes reconstructing what you thought you understood. The incident clock is running. The fluency illusion becomes very expensive, very fast.

**In architecture decisions.**

When you're asked to extend a system or choose between approaches, the judgment you need is different from the judgment you can gain from reading explanations of how others made those decisions. Explanations are after-the-fact reconstructions. Architecture is prospective. The skills don't transfer cleanly.

**In the quiet moments.**

Friday afternoon. You shipped six features this week. Everything passed review. You close your laptop and there's a feeling — not exhaustion exactly, more like uncertainty about what you actually learned. Not what you processed. What you learned.

---

## The Asymmetry Worth Tracking

Here's what nobody measures:

Most engineering teams track velocity. PRs per sprint. Cycle time. Throughput.

Almost no teams track the gap between what you could explain and what you could generate without assistance.

That gap is the truest signal of whether you're accelerating professionally or just accelerating output. Not the number of features shipped. The number of systems you could design, from scratch, without AI, if you had to.

The engineers who figured this out early have started measuring one number: confidence unaided.

---

## What Actually Helps

There's one practice that shows up consistently in the recovery stories we collect:

**Explaining things out loud.**

Not reviewing code. Not testing it. Explaining — to a colleague, to a rubber duck, to yourself — why the system works the way it does, why those design decisions were made, what would break under different assumptions.

The act of trying to explain reveals gaps instantly. Things you thought you understood turn out to be things you'd merely recognized. The friction is useful. It's information.

What makes this different from most productivity advice: it doesn't require anyone else to participate. You can do it alone, in thirty minutes, at the end of any week. No team buy-in. No process change. Just a different relationship with what you just built.

---

## A Question Worth Sitting With

If you've been feeling the gap — if you've shipped more in the last six months than ever before and somehow feel less certain about your skills — here's the honest question:

Have you been measuring what's actually changing?

Or just what's increasing?

The AI Fatigue Quiz gives you a baseline on where the gap stands right now. Some engineers find it useful for the honest look in the mirror. Some find it confronting.

Either is more useful than the uncertainty.

See you next week.

— Sunny + The Clearing team

---

**Further reading from this week:**

- [The Explanation Requirement](/the-explanation-requirement.html) — The one practice that keeps the reasoning loop intact
- [The Competence Illusion](/skill-atrophy.html) — how AI makes it easy to feel capable while capability quietly erodes
- [The Fluency Illusion](/newsletter-issues/dispatch-104.html) — Issue #104, where this week's letter starts
- [Take the AI Fatigue Quiz](/index.html#quiz) — three minutes, honest look at where you stand