# What 100 Issues Teaches You About Knowing Things
### Issue #103 — May 25, 2026

---

Two things happened after last week's Issue #100.

First: a lot of you wrote back. Not the usual "thanks, forwarded to a friend" emails — longer ones. Detailed ones. Ones that started with "you described something I've been feeling for six months and couldn't name." That part was worth the two years.

Second: several of you asked the same question in different ways. It went something like:

> How do I actually know if I'm on the acceleration track or the understanding track? Is there a test I can run?

That question is worth answering properly. Because the answer reveals something about what this newsletter is actually for.

---

## The Test Nobody Runs

Here's the simplest version of the test:

Think about the last time you solved a hard problem — one where you understood the system deeply, where you could explain not just what you did but why you did it that way and not another way.

How long ago was that?

For many engineers reading this, the honest answer is uncomfortable. It was months ago. Maybe longer. Not because you stopped having hard problems. Because the hard problems started getting solved by AI before you had to sit with them.

The test isn't about whether you use AI. It's about whether you're still building the understanding underneath the assistance.

Here's the more specific version:

**Take one feature you've shipped in the last two weeks.** Any feature. Now close all AI tabs and answer these four questions without looking at anything:

1. Could you explain why the architecture takes the shape it does — not just what it does, but why that approach was chosen over alternatives?
2. Could you debug a failure in this feature at 2am without AI assistance — not just find the symptom, but understand the root cause?
3. If you had to estimate how long it would take to build this feature again from scratch with no AI, no reference code, no Stack Overflow — what would you say?
4. When you review code in this area now, do you feel like you're evaluating something you understand, or evaluating output you're trusting?

If you can answer all four confidently — you are on the understanding track. Keep doing exactly what you're doing.

If you hesitated on two or more — you're on the acceleration track, whether you knew it or not. That is not a failing. It's information. And it's reversible.

---

## The Three Shapes of Erosion

Two years of reading your emails and quiz responses has taught us something: AI fatigue doesn't show up the same way for everyone. But it has three consistent shapes.

**Shape 1: The Debugging Fade.**
You used to be the person who could trace anything. Now when something breaks in an area you haven't touched directly, you prompt-storm until something works. You're getting the fix. You're losing the model.

**Shape 2: The Estimation Gap.**
Your estimates used to be built on felt sense — you knew how long things took because you'd built them. Now AI assists so much of the implementation that your estimates come from watching AI work, not from doing the work yourself. You notice it when something takes twice as long as you estimated — without AI.

**Shape 3: The Review Confidence Erosion.**
You used to review PRs with genuine judgment. Now you mostly confirm that the AI-generated code looks reasonable. You're not sure you'd have the same confidence if you had to evaluate the approach without AI having already suggested it.

These aren't character flaws. They're structural. They happen because the feedback loop that used to build understanding has been interrupted.

---

## The Practice That Scales

One question comes up repeatedly from engineers who've been working the recovery path for a while:

> Is there a minimum viable practice? Something that moves the needle without requiring an hour a day of deliberate no-AI work?

Yes. And it's smaller than you'd expect.

**Once a week: before you open any AI tool, spend 20 minutes working on something at the edge of your ability.**

Not something hard for the sake of hard. Something real — a bug in a system you care about, a feature in a personal project, a piece of code you've been meaning to understand better.

The goal isn't to prove you can do it without AI. The goal is to feel the difference between your unaided thinking and AI-assisted thinking. That feeling — the slight friction, the slower path, the part where you have to remember — is the signal that learning is happening.

20 minutes. Once a week. It compounds.

The engineers who write to us after three months of this practice all describe the same thing: the feeling comes back before the speed does. You start noticing that you understand more than you thought, and that the gaps are smaller than you feared.

---

## What Two Years Teaches

When I look back at 103 issues, here's what I notice:

The problems haven't changed. The names have gotten more precise. Two years ago we were calling it burnout-adjacent exhaustion. Now we have a vocabulary that actually fits — middleman problem, fluency illusion, the two tracks, the comprehension gap.

That's meaningful. Getting the diagnosis right is the first step toward doing something about it.

What's also changed: the community. Engineers who found this early, who've been reading since Issue #1, have become the people who send the detailed emails after Issue #100. They were the ones who first described the Sunday reckoning, the debugger drift, the explanation requirement in their own words before we had names for any of it.

That exchange — your experiences shaping the vocabulary, the vocabulary helping you understand your experiences — that's the part that makes this worth doing.

---

## What's Next

We're going to keep writing this. The format changes — some weeks a single practice, some weeks a data point, some weeks a longer essay. The through-line stays the same: honest, specific, useful content for engineers who care about what they're doing and notice that something has quietly changed.

If you've been meaning to share your own AI fatigue story — what it feels like, what you've tried, what works — the door is still open at share-your-story.html.

If you're not sure what track you're on, the quiz takes three minutes and will tell you your profile. Some people find that more useful than any article we've written.

And if Issue #100 landed for you, forward it to someone who's been quieter than usual in the last six months. They probably needed it.

See you next week.

— Sunny + The Clearing team

---

**Further reading from this week:**

- [The Distance Between Knowing and Understanding](/newsletter-issues/dispatch-100.html) — Issue #100, the milestone that prompted this one
- [The Competence Illusion](/newsletter-issues/dispatch-41.html) — the fluency illusion and surface comprehension, from Issue #41
- [The Debugger Drift](/debugger-drift.html) — what the debugging fade actually costs you over time
- [Take the AI Fatigue Quiz](/index.html#quiz) — find out where you stand in 3 minutes
