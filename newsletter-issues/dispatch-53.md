---
title: "The Velocity Regression"
number: 53
date: 2026-06-20
description: "Why shipping more code with AI can make your team look faster while making them actually slower — and the measurement trap nobody's naming."
---

# The Velocity Regression

*A letter about what happens when your velocity metrics optimize for output while your capability metrics quietly decline.*

---

A team ships 40% more features this quarter than they did last year.

The AI tools are working. The sprint retrospectives are glowing. The roadmap is ahead of schedule.

And then something breaks — something that used to be straightforward — and the team that could rebuild it in a day now takes a week. Not because the problem is harder. Because the capability to solve it without AI has quietly contracted.

This is the velocity regression. And it's one of the most insidious dynamics in software engineering right now.

---

## What the Regression Looks Like

The velocity regression happens in three stages.

**Stage 1: Apparent acceleration.** AI tools let your team ship more. Features land faster. Velocity metrics go up. Everyone feels good.

**Stage 2: Capability substitution.** The team learns to rely on AI for the hard parts — architecture decisions, debugging, complex refactors. Each sprint ships more, but each sprint also requires more AI assistance to achieve the same output. The team is effectively outsourcing its problem-solving capacity.

**Stage 3: Hidden deceleration.** A system issue surfaces. The team's mental model of their own code is incomplete — they've been operating on AI's understanding, not their own. The recovery time is longer than it would have been a year ago. Velocity drops. Nobody knows why.

The features shipped faster. The capability to handle what those features require has quietly atrophied.

---

## The Measurement Trap

Here's why this is hard to see: **we measure what AI makes faster, not what it makes slower.**

Sprint velocity, story points, features shipped — these all improve with AI. They're easy to measure. They're visible on dashboards.

The things that get worse — debugging depth, architectural judgment, the ability to work without AI assistance — aren't measured. They're invisible on the metrics board.

The result is a team that looks like it's accelerating on every metric that gets reported, while slowly losing the capability that those features depend on.

---

## The Specific Mechanism

The velocity regression is a form of technical debt — but it's debt in the team's knowledge, not in the codebase.

When a senior engineer uses AI to ship a feature, they're choosing between two paths:

**Path A:** Use AI, ship faster, and let the understanding of what they just built stay partially in the AI's model rather than theirs.

**Path B:** Use AI to accelerate, but take the time to understand what they just built — complete the cognitive loop, maintain the mental model.

Path A is easier. Path B is what's required to prevent the regression.

Most teams are doing Path A by default. The metrics reward Path A. The sprint schedule rewards Path A.

---

## The Question Worth Asking

If you lead a team: when something goes wrong with a feature shipped in the last six months — something that requires genuine debugging or architectural repair — how long does it take?

If the answer is "longer than it used to" or "I don't know, we'd have to check" — that's the regression happening in real time.

The fix isn't to use AI less. It's to be honest about what AI is optimizing for and to protect the capabilities it's quietly eroding.

The practice that helps: quarterly calibration. Pick three features shipped with heavy AI assistance. Can your team explain, design, and debug them without AI? If not, that's the gap. That's where the coaching time goes.

---

*Next week: Dispatch #54 — more from the archive.*

**The Clearing** | clearing-ai.com | For engineers navigating AI without losing themselves