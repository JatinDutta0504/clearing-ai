# DISPATCH-126-THE-PHANTOM-COMPETENCIES.md

## Newsletter Issue #126 · June 2026

**Word count:** ~1,900 words  
**Theme:** AI tools create a portfolio of completed work while quietly hollowing out the underlying competencies that built it  
**Tone:** Direct, slightly wry, genuinely empathetic  
**CTA:** Take the AI Fatigue Quiz →

---

## The Phantom Competencies

There is a specific kind of anxiety that has no name in most engineering cultures.

It looks like this: You are looking at a project you shipped three months ago. The features are working. The code is in production. Your manager highlighted it in the all-hands. Other engineers have referenced it as an example of good work.

And you cannot remember how it works.

Not in the vague, "it's been a while" sense. In the specific sense: you would not be able to independently reproduce it. You would not pass a whiteboard interview on its core architecture. You are not sure you could debug it without AI assistance — and in fact, when issues come up, you reach for AI immediately, not because you tried first and failed, but because trying first doesn't occur to you anymore.

This is not burnout. This is not impostor syndrome in the classical sense. This is something more specific and more insidious: you have a body of work that does not belong to your competencies.

The work exists. The competencies do not.

---

### What the Phantom Competencies actually are

Phantom competencies are skills that appear in your output, your track record, your project history — but have quietly evacuated from your actual capabilities. They are real in the same way a mirage is real: they have a location, they look solid, they seem to indicate something about the landscape ahead, but they dissolve when you try to touch them.

The most common ones in AI-assisted engineering:

**Debugging.** Your projects are mostly bug-free. Your track record shows fast resolution times. But try to debug something without AI, cold, on a codebase you wrote six months ago — and the feeling is different. The trace doesn't connect. The mental model has gaps.

**Architecture.** You can describe why a system was designed the way it was — because you asked AI to explain it to you and you internalized the explanation. But you did not form those intuitions through the friction of making the decisions. You can narrate the architecture. You could not have invented it independently.

**Testing.** Tests exist in your projects. Test coverage looks good. But when was the last time you designed a test case that surprised you — that caught something the implementation hadn't anticipated? Or are the tests mostly AI-generated paraphrases of the implementation?

**Code review.** You can approve PRs. You can identify obvious issues. But deep architectural concerns, subtle performance implications, the kind of review that makes a senior engineer valuable — does that still come from you, or from AI surfacing patterns you would have caught before AI existed?

**API design.** Your services have clean interfaces. They were probably designed with heavy AI input — sometimes explicitly ("design me a REST API for X"). The result looks professional. But the intuition that says "this interface will cause problems at scale" or "this naming will confuse future developers" — is that yours, or is it AI's pattern-matching reflected back?

Each of these looks like competency. Each of these shows up in performance reviews, in shipped features, in codebases. And each of these is, at least partially, a phantom — present in the artifact, absent in the person.

---

### Why this is different from normal skill decay

Normal skill decay happens when you stop practicing. You don't write Python for six months, you get rusty. This is understood. It has a clear cause and a clear cure: practice, gradually, and the skill returns.

Phantom competencies are different. They persist even while you are actively working — often *because* you are actively working. You are shipping more code than ever. You are more productive than ever. You are building a track record that looks exceptional.

And underneath all of that, the skills are quietly evacuating.

The mechanism is specific: AI tools bypass the cognitive processes that build competency. You get the output without the process. The destination without the journey. And it is the journey — the struggle, the debugging, the wrong turns, the moments of genuine confusion followed by genuine understanding — that actually builds the skill.

This is not a moral failure. It is an architectural property of how these tools work. AI tools are not designed to build your competencies. They are designed to produce outputs. Those are different goals, and optimizing for one at scale produces the other as a side effect.

---

### The competency audit

The problem with phantom competencies is that they are hard to detect from the inside. The artifacts look real. The track record looks solid. Your confidence, looking at what you shipped, might even be high — because you can see the work, and the work looks like yours.

Here is a simple diagnostic. For each of the skills below, answer honestly:

**Can you do it without AI?** Not "will you reach for AI" — actually: could you produce a good result if AI were unavailable for the next week?

- Debug a production issue in a service you wrote six months ago
- Design a non-trivial feature from scratch (requirements to implementation)
- Explain the full architecture of your primary codebase to a mid-level engineer
- Write a meaningful test suite without AI assistance
- Perform a code review that catches architectural concerns, not just style issues

If you hesitated on any of these — if the honest answer is "probably not, not as well" — you have phantom competencies in that area. The work exists. The skill is partially phantom.

This is not a judgment. This is information.

---

### The compounding problem

Phantom competencies compound in a specific direction: they make you more dependent on AI, which further evacuates the underlying competencies, which makes you more dependent on AI.

The mechanism is self-reinforcing. The less confident you are in your ability to debug something without AI, the more automatically you reach for AI to debug it. The more you use AI to debug, the less you practice debugging, the less you build the skill, the less confident you are — and around it goes.

The same is true for architecture, testing, code review, API design. Each use of AI to bypass the cognitive effort bypasses the effort that would have built the underlying competency. And each step down makes the next step more likely.

There is also a second compounding layer: the people around you. When everyone on the team uses AI for the same tasks, the team-level competency for those tasks starts to atrophy. The institutional memory of how things work — distributed across people who have struggled with them — starts to thin. The team's capacity to catch AI-generated errors decreases as the team's baseline of non-AI competency decreases.

This is not hypothetical. It is already happening in organizations where this hasn't been monitored.

---

### The re-phantomization protocol

The cure for phantom competencies is not to stop using AI. That is not a realistic prescription and it is not the point.

The cure is deliberate interleaving: regular, structured periods where you work without AI on the skills that are becoming phantom. Not as a purity test, not as a rejection of the tools — but as maintenance on your own cognitive infrastructure.

A practical version:

**The 90-minute rule.** Once a week, spend 90 minutes working on something you would normally use AI for — from scratch, without AI assistance. It does not need to be production code. It needs to be the cognitive effort: the decomposition, the debugging, the architecture, the testing. The part that AI normally takes from you.

**The explain-it-first protocol.** Before asking AI anything about your own codebase, write what you think the answer is first. Not as a test — as a calibration. Write the explanation, then see how it compares to what AI says. The gap between your explanation and AI's explanation is a map of your phantom competencies.

**The monthly audit.** Once a month, take one of the five areas above and honestly assess: can I do this without AI? Not "will I" — "can I." If the answer is no, that is the area to focus on in your 90-minute rule that week.

**The pairing change.** Pair-program with a specific focus on who is thinking. When you are watching AI write code, you are not thinking architecturally — you are verifying. Change the dynamic: you think, AI executes. You explain, AI elaborates. The cognitive load needs to stay with you, even when the execution load goes to the tool.

---

### What this means for your career

Phantom competencies are not a personal failing. They are a structural consequence of tools that are very good at producing outputs and not designed to build competencies.

But they are real, and they matter — not because AI is bad, but because your confidence and your capability need to be anchored to something. When the competencies are phantom, you are one significant event away from a very uncomfortable reckoning: a production incident at 2 AM, an architectural decision that goes wrong, a situation where AI is unavailable or produces wrong output, and suddenly the gap between what you can do and what you have shipped becomes visible.

You want to know what is in that gap before the gap becomes an emergency.

The work you shipped is real. The competencies underneath need to be, too.

---

**This week's challenge:** Audit one skill from the list above — honestly, without AI. Can you do it without AI? If not, that is where to start.

— The Clearing

---

*Previously in The Dispatch: ["The Imposter in the Machine" — AI tooling's new species of imposter syndrome](https://clearing-ai.com/dispatch-125.html)*

*Forwarded this? [Subscribe for The Dispatch every Thursday](https://clearing-ai.com/newsletter.html)*
