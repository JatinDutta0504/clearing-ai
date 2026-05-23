# The Competence by Proxy
### Issue #98 — July 13, 2026

---

There's a moment that happens quietly, and then all at once.

It starts as a feeling. Not imposter syndrome — something more specific. You're looking at code you approved, code you shipped, code that's in production — and you can't tell if it's right. Not from the surface. You need to run it. You need to test it. You need someone else to tell you.

And the part that makes it distinct from ordinary uncertainty is this: you used to know. Not sometimes. Not most of the time. You used to have a direct line between your judgment and your work, and that line is now uncertain in a way it wasn't before.

You didn't get worse at coding. Your code is fine. But you can't feel fine about it anymore — because the validation has moved.

---

## How Trust Worked Before AI

Before AI tools became constant in your workflow, trust in code worked in a specific way.

You wrote something. You felt whether it was right — not just whether it compiled, but whether the approach made sense, whether the edge cases were handled, whether the logic held. That feeling was built from thousands of hours of debugging your own mistakes. You knew what wrong looked like. You could feel it before you proved it.

When you reviewed someone else's code, your gut caught things the tests didn't catch. When you saw a bug in production, your first instinct was usually right about where to look. When something felt off in a PR, it was off.

That gut feeling was not superstition. It was calibration — a model of how your systems work, built from failures you personally witnessed.

The model was the point. Not the code. The model.

---

## The Third Party

AI tools introduced a third party between you and your work.

Before, you wrote code and knew whether it was right. Now: you describe what you want to an AI, the AI generates it, you evaluate whether it looks right. The validation step is no longer between you and the code — it's between you, the code, and the AI's explanation of the code.

And over time, your calibration starts to drift toward the AI.

Not because AI is wrong. Because the AI becomes the reference point. When you look at AI-generated code, you judge it by whether it looks like what AI would write — not by whether it feels like what you would write. The standard shifts. The internal reference changes.

The gut feeling that used to be calibrated to your work is now calibrated to AI output. And when that happens, you start to lose the ability to judge code on your own terms.

---

## The Three Failure Modes

Once the calibration has drifted, three specific things start happening. They're easy to miss individually — they're most visible as a pattern.

**1. Trusting AI Over Your Gut (Even When You're Right)**

You look at something. Your gut says it's wrong. The AI says it's fine. You trust the AI — not because you have a reason to, but because the AI is the reference point now. You override your own judgment with the AI's explanation, even when your gut was correct. After a few of these, you stop trusting the gut. The gut was right. The calibration was wrong.

**2. Taking Credit You Don't Feel**

You solved a hard problem this week. You feel pleased — but when you try to locate the specific thinking that solved it, you can't quite find it. The solution is yours because you're the one who shipped it. But the thinking came in the form of evaluating AI-generated output, not generating it yourself. You feel competent but not confident. There's a difference.

**3. Validating Through AI Instead of Through Understanding**

When something feels uncertain — a complex piece of logic, a tricky edge case — your first move is to ask AI to explain it. Not to think it through yourself. To let AI hold the uncertainty for you. Over time, this becomes the primary way uncertainty gets resolved. Not through your own reasoning, but through AI's explanation. The reasoning path atrophies. The uncertainty tolerance drops. You need the explanation to feel okay about the code.

---

## The Double-Bind

The hardest part of the competence-by-proxy problem is the double-bind at the center of it.

The fear of trusting only AI is real. You see the outputs. You know the gaps. You know that shipping code you don't fully understand is a risk — for the system, for the team, for you as the engineer who has to maintain it.

But the fear of trusting only yourself is also real. Your calibration has drifted. The gut feeling is no longer as reliable as it used to be — not because you're less capable, but because it hasn't been maintained against your actual work. When you trust your gut alone, you might be right, or you might be working from an outdated model.

So you end up in a loop: AI validates your gut, your gut validates the AI, and neither is anchored to direct contact with the code itself.

This is the part that feels like madness. You're not incompetent. The work is not bad. But you can't trust either your judgment or the AI's — and you can't trust yourself to trust either of them.

> **The uncomfortable truth:** the answer is not to trust yourself more, and it's not to trust AI less. The answer is to rebuild the calibration — which requires direct contact with code written without AI assistance, enough times that your internal model starts updating again.

---

## The Path Back

The path back is slower and less dramatic than it sounds.

It starts with one thing: code written without AI assistance, small enough to not feel consequential.

Not to prove you can still do it. Not to rebuild your confidence. Just to get your calibration back in contact with the actual work of building something — the friction, the debugging, the moments where you don't know and you have to figure it out.

That contact rebuilds the model. Slowly. The gut starts to mean something again. Not something perfect — but something that belongs to you, that reflects your actual understanding, not the residue of expertise left over from before the drift.

---

## The Test

This week's question — and it's one you have to answer honestly to get anything from it:

Think about the last time something you shipped broke in production. Did you see it coming before it happened?

If yes — if your gut said something was off and you overrode it — that's data.

If no — if it surprised you — that's also data. Different data.

The question worth sitting with is not whether you made a mistake. It's whether you had access to the information that would have prevented it before the mistake was made. And whether you trusted that information when you had it.

---

*This week's Dispatch goes to 97 issues — six months of weekly letters for engineers navigating AI fatigue. Thank you for being here.*

*🌿 The Clearing — Resources for engineers navigating AI fatigue*