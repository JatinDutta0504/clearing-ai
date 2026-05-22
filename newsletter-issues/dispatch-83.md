# The Dispatch #83 — The Competence Illusion

*Issue #83 — May 22, 2026 — For engineers who suspect they're getting worse at the things that matter most*

---

There's a phenomenon happening in software engineering right now that nobody is talking about directly.

It's the gap between what you can do with AI and what you can do without it. And the scary part isn't that the gap exists — it's that the gap is invisible to the person standing in it.

Let me explain with something that happened to me.

I used to be genuinely good at reading maps. Not GPS — actual paper maps, city layouts, the kind of navigation where you build a mental model of where things are relative to each other. I used to take road trips with a folded atlas in the passenger seat and navigate from memory.

Then GPS became ubiquitous. And after a few years of relying on it, I noticed something: when I tried to navigate without it, my spatial memory had degraded. Not dramatically — but noticeably. I could still figure out where I was, but it took more effort, and my confidence was lower.

I hadn't gotten worse at driving. I'd gotten worse at the specific skill of wayfinding.

This is the competence illusion. And it's happening to software engineers at scale.

## The Competence Illusion

Here's how it works: when AI helps you solve a problem, your brain registers the problem as solved. The solution enters the codebase. Tests pass. PR merges. The task is complete.

But your brain doesn't separately register "I solved this with AI" and "I understand this." It just registers "solved." Over time, this creates an accumulated sense of capability that doesn't match your actual unaided ability.

You feel competent. You are competent — with AI. Without AI, you're not sure what you are.

This isn't imposter syndrome. Imposter syndrome is the fear that you're not as good as people think you are. The competence illusion is different: it's the belief that you're still as good as you used to be, when you're not. You look in the mirror and see an engineer. The mirror is showing you an AI-assisted engineer.

## Five Signs You're Inside the Illusion

**1. You can explain the solution, but you couldn't have generated it.**

This is the most reliable signal. You can follow the AI's reasoning, understand why it made the choices it made, and even modify the output intelligently. But if you had to produce that output from scratch — without AI — you'd be lost.

The explanation is not the same as the ability. Understanding why a solution works is fundamentally different from being able to construct it. You can understand every word of a proof in a mathematics textbook and still be unable to generate the proof yourself.

When AI is doing the generating, your explanation skills can remain sharp while your generative skills atrophy.

**2. You pass technical interviews but struggle with real work without AI.**

Technical interviews are, by design, bounded problems. Given enough time and a clean specification, you can probably work through most of them. But the work that actually pays the bills — debugging a gnarly production issue at 11 PM, architecting a system under constraints, understanding a legacy codebase well enough to safely change it — that work is different. It's ambiguous. It requires the kind of deep, embodied knowledge that doesn't transfer from watching AI solve problems.

If you can pass an interview with AI but you'd struggle in a real work environment without it, you're inside the illusion.

**3. Your estimation is confident but consistently wrong.**

Here's a specific one. When you're working with AI, do you find yourself saying things like "that should take an hour" and then it takes six hours? The AI makes the architecture obvious, but the implementation still has to come from somewhere — and the gap between "I see how this works" and "I can build this efficiently" is where estimation breaks down.

AI accelerates the visible parts of a task and hides the invisible parts. The result is systematically optimistic estimates that feel justified in the moment but collapse in execution.

**4. You can work in unfamiliar codebases with AI, but you'd be lost without it.**

This one cuts deep. You used to be the person who could drop into any codebase and figure out what was going on. You were proud of that — your ability to navigate unfamiliar systems was a core part of your identity as an engineer.

Now, with AI, you can do that navigation with a lot less friction. You can ask AI to explain sections, generate modifications, map out the architecture. And this feels like the same ability. But it isn't.

The old ability was a mental model you built from reading code, tracing execution paths, holding the system's state in your head. The new version is a skill at prompting AI to explain things. Those are different skills. They both let you "figure out" a codebase, but they leave you in different places when the AI isn't available.

**5. When AI is unavailable, your first instinct is to wait.**

This is the behavioral tell. When Copilot is down, or Claude is rate-limited, or Cursor is throwing errors — what do you do? If your instinct is to wait until it comes back, rather than to just start working without it, that's a signal.

Healthy AI usage means AI is a power tool. Unhealthy usage means AI is a dependency — and the test for dependency is whether you can do the work without it.

## Why This Illusion Is So Compelling

The competence illusion is particularly insidious because it exploits a specific feature of how human metacognition works: we are very good at recognizing that we don't know something, but we are poor at recognizing when our knowledge is shallow.

This is called the Dunning-Kruger effect, but it's not exactly what Dunning and Kruger described. The classic Dunning-Kruger finding is that incompetent people overestimate their competence because they lack the expertise to recognize their own mistakes.

The competence illusion is different. You are not incompetent. You are genuinely helpful to your team, you ship value, your code reviews are useful. But the specific skills that make you effective — the ones that will matter most in five years when AI is even more capable and the marginal value of "just using AI" is lower — those skills are eroding while you watch.

Here's what makes it worse: AI makes the erosion feel like progress.

When you solve a problem with AI, you experience the satisfaction of completion. Your brain releases the dopamine it associates with solving hard problems. You feel the positive emotions of mastery without doing the work that produces actual mastery.

This is the mechanism. Not malicious, not intentional — just the natural consequence of getting problem-solving feedback without problem-solving effort.

## The Dangerous Part

The danger isn't the gap itself. The danger is that the gap compounds.

Here's what I mean. If your unaided skill in an area is at 70% and you're not practicing it, you're gradually declining. But because you're still getting results — with AI — you don't feel the decline in real time. You feel effective.

Then something happens. Maybe you change jobs. Maybe the team's AI tooling changes. Maybe there's a production incident at 2 AM and the tooling is down and you have to understand what's happening in a system you don't know well. And the gap becomes visible — not gradually, but all at once.

The competence illusion compounds into a capability cliff. And the cliff is steepest for the engineers who are currently most confident.

## What Closes the Gap

The solution isn't to use AI less. It's to be more deliberate about what you practice without it.

This is the framework I've come to believe in:

**Every week, do one thing from scratch.**

Not a whole project. Not a hero effort. One task — a function, a debugging session, an architecture sketch — that you complete without any AI assistance. You can use AI to explore and understand, but the actual building has to be yours.

This sounds small. It isn't. The maintenance of generative skill requires generative practice. Reading about swimming doesn't make you a better swimmer. Watching AI solve problems doesn't make you a better problem-solver.

**Measure confidence unaided.**

Once a quarter, give yourself a real test. Not a quiz — an actual coding task, something you'd encounter in your work, done without AI. Then honestly assess: how did that go? What was I confident about that I shouldn't have been? What did I know that I couldn't have articulated before?

The goal isn't to prove you're still good. The goal is to get an accurate reading of where you actually are.

**Distinguish between "I understand this" and "AI explained this to me."**

This one is a discipline, not a technique. After every AI-assisted solution, pause and ask: could I have generated this? Not "do I understand it" — that question is almost always yes. The question is "could I have produced this from scratch, without being shown?"

If the answer is no, note it. That's not a failure — that's information. You now know something about the shape of your actual knowledge versus your AI-assisted knowledge.

## The Thing Nobody's Saying

Here's what I keep coming back to.

The engineers who will thrive in an AI-augmented future are not the ones who use AI most effectively. They're the ones who maintain the underlying craft — who can still think, design, debug, and reason about systems without AI assistance, while also being highly effective with AI.

That's a harder balance to strike than it sounds. It requires deliberate practice in the unaided mode, not just efficient use of the aided mode.

The competence illusion doesn't mean you're failing. It means you're in a new situation that requires a new kind of discipline — the discipline of protecting the skills that AI can't replace, even as you're using AI to be more effective in the short term.

The engineers who figure this out won't be the ones who learn to use AI better. They'll be the ones who learn to be honest about what they can still do without it.

— *The Clearing*

---

*This is issue #83 of The Dispatch. Subscribe at [clearing-ai.com/newsletter.html](https://clearing-ai.com/newsletter.html)*