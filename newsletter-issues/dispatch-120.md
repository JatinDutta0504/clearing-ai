# The Input-to-Output Ratio
### Issue #120 — July 22, 2026

---

Here's an exercise worth doing right now, before you read any further:

Think about the last month of your engineering work. Count the number of commits you shipped. Now count the number of those commits where you genuinely struggled with the problem — 15+ minutes where you weren't on the verge of reaching for an AI tool, where you sat with not-knowing and pushed through yourself.

If you're like most AI-assisted engineers, the second number is dramatically smaller than the first.

This is the input-to-output ratio problem — and it's quietly rewriting what your engineering career looks like from the inside.

---

## What the Ratio Used to Mean

In pre-AI engineering, input and output were tightly coupled. The time you spent wrestling with something was the input. The code you shipped was the output. The ratio was roughly 1:1 — or more accurately, 2:1 or 3:1 if you count the debugging and the failures along with the struggling.

The struggling was the input. It wasn't a tax on your productivity. It was the work itself.

This produced an engineer who came out of an intensive period with something to show for it and something learned from it. The output was visible. The input survived as skill/capability.

---

## What AI Changed

AI decoupled input from output.

You can now produce significant engineering output with minimal input of your own cognitive effort. The ratio goes from something like 2:1 to something like 0.2:1 — you're putting in less genuine struggle per unit of production than you used to.

On a velocity metric, this looks like a miracle. On a capability metric, this looks like atrophy.

The dangerous part: your brain doesn't update your internal bookkeeping correctly. It sees high output and assumes the input somehow happened anyway, even when it didn't. You shipped a complex feature — the struggle must have been there somewhere. The implication is that you earned the output.

You didn't. You earned the velocity. The struggle was outsourced to AI, and the skill formation that typically accompanies productive struggle went with it.

---

## Why Metrics Miss the Ratio Problem

Standard velocity metrics measure output. They don't measure input in any meaningful way — they certainly don't measure the type of input that builds capability.

Sprint velocity is up. PR throughput is up. Tasks closed per day is up. All of this tells you the output side of the equation is healthier. None of it tells you whether the input side is building or eroding the engineer who produces it.

Engineers often don't notice this internally either, at least not until the gap between what they can do and what they could do before AI becomes significant enough to feel.

Here's the specific experience that signals the ratio has inverted for you: you can produce but you can't explain. You can ship but you can't debug. You can deliver but you couldn't have gotten there without AI. The output is dissociated from the input that used to produce it.

---

## The Compounding Problem

The ratio problem compounds in two ways:

**On the negative side**: When you produce output without genuine input, you're not just failing to build skill — you're actively un-building it. The circuits that handle reasoning, debugging, and independent problem-solving are idle in the same way muscles are idle during disuse. And like muscles, they don't maintain themselves. They erode.

**On the metric side**: As you erode, your output quality increasingly depends on AI correctness. Your ability to catch AI errors degrades. Your reference points for "this code is right" shift toward AI output as your baseline, which is an unstable foundation. The ratio keeps inverting until you can't produce without AI and can barely evaluate what AI produces.

---

## The Ratio Table

Here's a rough framework for understanding where you stand:

**Healthy ratio (pre-AI)**: 2-3 hours of genuine struggle per day in peak engineering work, producing code that reflects the struggling. Confidence in code matched by genuine understanding. Input and output stay coupled.

**Warning ratio**: 1-2 hours of genuine struggle per day, with AI handling the rest. Output quality is fine; personal capability is slightly eroding. The gap between what you ship and what you understand is widening.

**Compromised ratio**: 30-60 minutes per day of genuine struggle, AI handling the rest. Output looks healthy; internal experience is vague dissatisfaction you can't quite name. The engineer you were is eroding faster than you notice.

**Atrophied ratio**: Almost no genuine struggle per day. You're essentially supervising AI output. You can approve what AI generates but your ability to independently produce or evaluate it is significantly degraded. The original engineer is largely gone; you're running on AI capability now.

---

## How to Restore the Ratio

The goal isn't to use less AI. The goal is to maintain the input side of the ratio — the part that builds capability — that used to be automatic in pre-AI engineering.

**The weekly practice protocol**: Once per week, identify one meaningful technical problem and solve it with zero AI assistance for 30-45 minutes. Not for production. Not for speed. Deliberate practice. The struggling is the point, and it has to be genuine.

**The explanation audit**: Before you approve AI-generated code, write three sentences about why this approach was chosen, without consulting code or AI. If you can't, the ratio has inverted on this specific decision and you need to engage more deeply before approving.

**The metric worth tracking**: Add a personal metric alongside sprint velocity — a count of the number of decisions you made this week that required genuine judgment, not just AI approval. If that number is trending down, the ratio is working against you.

---

## The Internal Experience of a Working Engineer

Before AI tooling, you probably had a specific internal experience of doing engineering work: the feeling of sitting with a hard problem, not knowing, pushing through, and coming out the other side with something you built and understood. This was the experience that produced the satisfaction of engineering. The struggle was part of the reward.

The ratio problem means that experience is getting harder to have. Not because the work is getting harder — because the work is getting easier and the satisfaction of genuine completion is consequently harder to find.

If you're months into intensive AI-assisted work and you can't quite remember the last time you finished something that felt like you really finished it, the ratio has inverted. Your output metric looks great. Your development metric is running negative.

The goal is to get the ratio healthy again — not by rejecting AI, but by being deliberate about which problems you engage without it, and making sure at least some of your output reflects your genuine input.

---

*This week: audit your ratio. How many genuine struggling hours did you put in this week? How many would you estimate you used to put in? The gap is the problem.*

<div class="dispatch-cta">
<p><strong>The AI Fatigue Quiz</strong> measures your severity across all known AI fatigue dimensions. Takes 90 seconds. Free.</p>
<a href="../#quiz" class="cta-btn">Take the Quiz →</a>
</div>
