# Dispatch #92 — The Calibration Gap

**Week of June 1, 2026**
**Theme: Why you can no longer accurately judge your own skills — and the test that proves it**

---

## The Opening

Last month, a lead engineer at a mid-size startup reached out with a specific problem.

His team had been using AI coding tools for about 18 months. Velocity was up. Deployment frequency was up. Code review looked clean.

And yet: something had quietly gone wrong.

The specific thing he noticed: when his engineers encountered problems that required genuine debugging — not prompt-debugging, actual diagnosis — they took much longer than they used to. Not because they were slower. Because they had lost the intuitive sense of where to look.

His phrase: "It's like they've been flying with autopilot so long they've forgotten how to read the instruments."

The instruments are still there. The ability to read them has atrophied.

This is the calibration gap.

---

## What Calibration Actually Means

Calibration in engineering is the relationship between your internal model and reality.

You know how long something will take because you've done it before. You know where to look when something breaks because you've seen similar failures. You know what "good enough" looks like in a code review because you've built up a felt sense of quality through hundreds of decisions.

This calibration is not just intuition. It's accumulated evidence encoded as judgment. It lives in the gap between what you know and what you can immediately articulate — the same gap that lets a senior engineer look at a piece of code and immediately sense something is off before they can explain why.

AI tools are very good at filling this gap. Too good.

When you hit a bug and AI generates a fix in 20 seconds, the gap between "something feels wrong" and "I found the problem" collapses. You never have to develop the sense of where to look, because AI already knows.

Over time: the calibration doesn't just fade. It reverses.

You start thinking you're better than you are, because AI output looks correct and you're the one who approved it. The feedback loop that used to correct your calibration — the system breaks and you debug it and you learn — has been broken. You're flying blind and you don't realize it because the instruments look like they're working.

---

## The Specific Version That Shows Up Most

It usually surfaces as one of these:

**The estimation reversal.** You used to estimate in days and be within a factor of two. Now you estimate in hours and you're off by 3x — but in the wrong direction. You think you're faster. You've actually lost the calibration that made your estimates accurate.

**The review confidence gap.** You review AI code and it looks correct. You approve it. Three weeks later it breaks in production and you have no idea why. Your confidence in your review ability is higher than your actual review ability — AI has been doing the deep review you used to do, and you didn't notice the difference.

**The interview gap.** You get to a system design interview and you can describe the high-level approach. You can't build it. You can't debug it. You can talk about architecture fluently but you can't generate the implementation. This shows up most painfully in take-home technical assessments done without AI.

**The "I'll know it when I see it" gap.** This one is subtle. You used to have a sense for when code was right before you ran it — a kind of pre-conscious pattern recognition built from thousands of hours of reading and writing code. Now that sense is gone. You wait for the AI to tell you something is wrong, and you're not sure you could have caught it yourself.

---

## Why This Is Different From Imposter Syndrome

Imposter syndrome is: you are capable but you feel like a fraud.

The calibration gap is: you have measurably lost capability and you haven't noticed.

The important distinction: imposter syndrome makes you feel bad about something that isn't real. The calibration gap makes you feel fine about something that is very real.

Engineers in the calibration gap often feel confident. They're shipping, they're reviewing, they're estimating. The outputs look fine. They don't feel like they're struggling.

Until they try to do something — debug something real, build something from scratch, solve something without AI — and the gap becomes impossible to ignore.

And by then it's been 18 months.

---

## The Test You Can Run Right Now

This is not a self-assessment. This is a measurement.

**The unaided estimation test:**

Take your last 10 completed tickets. For each one, ask:

1. Could I have estimated this without AI assistance? (Not: should I have. Could I have.)
2. What would my unaided estimate have been vs. what actually happened?
3. If you had to estimate it today without AI, what would you say?

Most engineers who run this test find something specific: their AI-assisted estimates are 30-50% shorter than their unaided estimates would be. Not because they got faster. Because they lost the parts of the problem that used to make estimation hard.

**The Explanation Test:**

Pick a feature you shipped in the last two weeks. Not a trivial one — something with real logic. Now answer these three questions without looking at the code:

1. Why was this approach right instead of another one?
2. What would break if you removed this part?
3. What edge cases does this handle that might not be obvious?

If you can't answer all three in 60 seconds, that's your calibration gap.

---

## What Actually Closes the Gap

The obvious answer: use AI less.

That's not wrong. It's also incomplete.

The calibration gap doesn't close by using AI less. It closes by rebuilding the feedback loop that AI interrupted.

The feedback loop: you do something hard, you get feedback on whether it worked, you update your model. Repeat.

What AI does: it completes the loop for you. You do the hard part (describe the problem), AI does the execution, you get the output. The loop is closed — but not by you.

The key insight: the loop has to close with you in it. The learning happens in the gap between what you attempted and what happened, not in the output itself.

Three practices that do this:

**The 20-minute buffer.** Before you open any AI tool for a problem: spend 20 minutes thinking about it. Not to solve it without AI. Just to have a hypothesis. Then open AI, compare what you expected to what it produced. The comparison is the learning.

**Weekly unaided estimation.** Once a week, estimate one ticket by hand. Not to prove you can — to measure your calibration. Track the ratio of unaided estimate to actual. Watch whether it improves or degrades.

**The explanation requirement.** Before you accept any AI code: complete this sentence out loud. "I added this because..." Not the AI added this because. You. If you can't finish the sentence in 30 seconds, that 30 seconds is the gap.

---

## The Uncomfortable Part

The engineers who are navigating this best share one trait: they've stopped measuring themselves by their outputs and started measuring themselves by their unaided capability.

That's a harder number to track. It doesn't show up in velocity dashboards. It doesn't show up in sprint metrics. It's invisible to everyone except you.

It's also the number that matters for whether you're still the engineer you were, or whether you're a high-output middleman with excellent metrics and a growing gap in your actual capability.

There's no shame in being in the gap. It's the natural consequence of 18 months of heavy AI use. The question is what you do about it.

The first step: measure it.

---

## One Thing This Week

Find one problem you've been meaning to solve — something you haven't touched yet, something in your backlog. Don't open AI. Don't search for the answer. Spend 20 minutes thinking about it before you do anything else.

Write down your approach before you look at anything.

Then: open AI, build it, ship it.

Compare what you expected to what happened. If the gap surprises you, that's data. The data is the beginning of calibration.

---

## What to Read This Week

**The Estimation Problem** — why estimation accuracy degrades with AI tooling and the practice that rebuilds it.

**The Debugger Drift** — the specific way debugging skill erodes and why senior engineers feel it most acutely.

**The 30-Day Recovery Plan** — structured practice for engineers who are ready to rebuild rather than just cope.

---

*The Clearing is built by engineers who got tired of naming problems without offering solutions. Start with the quiz.*