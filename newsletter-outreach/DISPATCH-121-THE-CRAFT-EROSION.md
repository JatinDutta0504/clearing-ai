# DISPATCH-121: The Craft Erosion
**Theme:** The quiet dissolution of the identity that took years to build
**Subject line:** The craft erosion is invisible until it isn't
**Preview:** You used to be an engineer who cared about the craft. Now you're not sure what you are. Here's what that means.
**Date:** July 19, 2026

---

## The Craft Erosion

There's a version of you that used to care about things.

Not just whether the code worked — whether it was elegant. Whether the abstraction was right. Whether the function did one thing and did it cleanly. Whether you could make a complex system understandable to the next person who touched it.

You didn't learn to care about this from a manager. You learned it from the craft itself — from the experience of writing something good, of feeling what good felt like, of wanting more of that feeling.

That version of you is eroding. Not dramatically. Not with a moment you can point to. Slowly, quietly, the craft part of the job has been removing itself from your work while the production part accelerates.

This is craft erosion. And it's the most overlooked cost of AI-assisted development.

---

## What Craft Actually Was

"Having craft" doesn't mean writing clever code. It means having standards informed by experience — knowing what good looks like because you've built enough things to recognize the difference, caring about the gap between "works" and "right," and taking the gap seriously even when no one is watching.

The craft dimension of software engineering is what makes engineers valuable beyond their output. A craftsperson brings judgment: which approach is better, even if both "work"; what the code will cost downstream; where the brittleness lives. That judgment comes from years of making mistakes and feeling the consequences.

AI tooling is eroding this specific faculty. Because AI generates code that works, and works quickly, and the pressure to ship is constant — the feedback loop that used to reward craft attention is broken. There's no penalty for accepting an AI solution that solves the problem in a ugly way. The problem gets solved. That's what gets measured.

The craft engineer's internal standard — the voice that says "this works but it's not right" — has nothing to push against anymore. It gets overridden by velocity metrics and the quiet knowledge that AI will handle the next iteration anyway.

---

## What the Erosion Looks Like

You've noticed it already. You just haven't named it.

**The naming drift.** You used to name variables descriptively, in ways that encoded what the thing was and why it existed. Now the names are whatever AI chose, or close enough that you don't bother changing them. The name drift is a proxy for the care drift.

**The pattern recognition fade.** You used to look at a piece of code and immediately see the patterns — this is a repository pattern, this is a middleware chain, this is a factory abstraction. Now you sometimes can't see the structure until AI explains it to you. The pattern recognition that used to be automatic requires external narration.

**The "good enough" tolerance shift.** You used to have a specific, personal feel for when something was done well. That feel — that calibrated standard — has been settling lower, one AI-assisted delivery at a time.

**The design conversations avoidance.** You used to engage deeply with design questions: Is this the right abstraction? Should this be a separate service? Are we solving the right problem? Now you tend to implement whatever approach gets framed in the ticket, because AI makes implementation feel approachable regardless of whether the approach is correct. Design is where craft lives. If you've stopped having design conversations, the craft erosion has reached your architecture layer.

---

## The Identity Problem Nobody Talks About

Craft isn't just a quality standard. It's an identity anchor. Many engineers define themselves partly through the craft relationship — "I'm the person who cares about getting this right," "I'm the engineer who understands why this approach is better," "I'm someone who takes pride in the work."

That identity anchor is loosening. Not because the engineer stopped caring — because the conditions that expressed care became structurally unrewarded.

You can care about craft and still ship AI-generated code that doesn't meet your standard. The velocity pressure doesn't negotiation. The ticket is due. The AI makes it possible to ship without the craft work. So the craft work doesn't happen.

And every week you ship without the craft dimension, the identity anchor loosens a little more. And at some point, you look at yourself and think: I'm not sure I know what I am anymore. I'm producing. I'm not building. I don't know what to call myself.

This is the identity erosion version of craft erosion. It's less visible than the capability erosion, and it may be more consequential.

---

## Why It's Not Recovering Automatically

You might expect that caring about craft is enough to preserve it. That if you just cared more, you'd maintain the standards.

The research doesn't support this. Bjork's desirable difficulties framework tells us that effortful struggle against appropriate challenge is what builds durable capability. If AI removes the struggle, the capability doesn't get built. Caring doesn't substitute for the mechanism.

Similarly, Dweck's growth mindset research tells us that believing your abilities can grow requires feedback that confirms they are growing. If AI-assisted output shows external improvement but internal stagnation, the signal being sent to your brain is contradictory: things are getting better and worse simultaneously. The brain resolves the contradiction by updating on the visible signal (things shipped, velocity up) and discounting the invisible one (understanding flat). Your growth mindset gets distorted — you believe you're growing because the metrics say so, while the underlying capability erodes.

The craft erosion doesn't self-correct because the rewards structure doesn't support craft. Shipping is rewarded. Care is not. Until the individual engineer deliberately reintroduces the craft feedback loop, the erosion continues regardless of internal motivation.

---

## What Does and Doesn't Work

**What doesn't work:** More caring without structural change. Telling yourself to "just care more" or "pay better attention" doesn't introduce the struggle that the craft development requires. The difficulty isn't attention — it's the absence of friction that learning from mistakes requires.

**What works:** Deliberate retrieval practice that reintroduces the friction AI removes. Specifically:

- Once per week: solve a small design problem from scratch, no AI, 30 minutes. Feel the friction. Notice what you reach for before AI would.
- After every AI-assisted implementation: write one paragraph in your own words about why this approach was taken, without consulting code or AI. If you can't, the understanding gap is live.
- Monthly: review a piece of your own AI-assisted code from 2-3 months ago and ask: could I have written this? Would I have chosen this approach?

**The specific habit that helps most:** Write a craft note on every significant implementation. Brief — 2-3 sentences. What approach did you choose and why? What did you reject? What would you do differently? This forces the reflection that craft requires. Without the record, the reflection doesn't survive the velocity.

---

## The Question Worth Asking

Take a piece of code you've shipped in the last month. Look at it. Can you say, in your own words, why the implementation is structured the way it is?

If yes — the craft is intact. Keep watering it.

If no — there's your map. That's the gap. And closing it starts with one honest paragraph: what this code does and why it does it that way, without AI, without code reference, without guessing. Write it until you can.

---

**This week on The Clearing:**

New article: **[The Staff Engineer's Dilemma](https://clearing-ai.com/the-staff-engineer-dilemma.html)**

The identity problem nobody talks about at the senior IC level — when everyone expects you to be fine.

---

Until next week.

— *The Clearing*

*Free. No ads. No tracking. Just help.*
