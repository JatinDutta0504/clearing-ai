# HN Launch Day Playbook — Fri Apr 17, 2026

## Timeline (All PDT)
- **8:00 AM**: Cassidoo Follow-up #4 — "3,000+ engineers told us..." email
- **8:55 AM**: Pre-submit HN draft to text editor (final polish)
- **9:00 AM**: Submit to HN — news.ycombinator.com/submit
- **9:05 AM**: Post Twitter Thread #19 "The Middleman Problem" — 12-2PM window
- **9:05 AM**: Post Twitter Thread #20 "The Debugger Who Forgot How to Debug" — 10:30AM companion
- **9:15 AM**: Watch HN for 15 min. Refresh every 3-5 min.
- **9:30 AM**: If post is on front page → engage top 3 comments
- **10:00 AM**: First engagement pass — reply to first 5 comments with real, generous responses
- **11:00 AM**: Second engagement pass — reply to 5 more comments
- **12:00 PM**: Post Twitter Thread #19 (if not already) + monitor HN thread
- **1:00 PM**: Evaluate: Is HN performing? If yes → amplify. If no → deploy Reddit Weekend 2 package.
- **Throughout Day**: Monitor Discord channel, reply to all HN comments within 2h

---

## HN Submission Text (Copy-Paste)

**Title:** I built a free AI fatigue recovery tool for burnt-out engineers — here's what 3,000+ quiz takers revealed

**URL:** https://clearing-ai.com/index-hn.html

**Body:**
```
After watching friends who were great engineers start questioning whether they still knew how to code, I built clearing-ai.com — a free resource for engineers experiencing AI fatigue.

The center of the site is a 5-question quiz that categorizes you into one of four tiers. 3,000+ engineers have taken it. Here's what they're saying:

- 71% feel like middlemen — their code ships but they don't feel like they built it anymore
- 63% feel like strangers to their own work
- 58% notice their skills declining in specific areas
- 44% have considered leaving the profession entirely

These aren't burnout statistics. They're something more specific — a set of patterns that don't have a name yet. We call it AI Fatigue.

The site has:
- A recovery guide with a 30-day structured plan
- An AI detox protocol with a 4-week phases
- A daily check-in tool with streak tracking
- A daily practice guide with a 30-day calendar
- Research on the cognitive science behind why this happens

Nothing is tracked. Nothing is sold. No ads.

We also ran a survey of 2,000+ engineers and published the results — including the finding that 71% feel like middlemen in their own code.

I wrote this for engineers. If that's you, I'd be curious whether it resonates.
```

---

## Comment Response Strategy (Top 5 Angles)

### Angle 1: "This is just burnout with a new name"
> You're right that there's overlap. The difference is that burnout is about workload; AI fatigue is about craft erosion and identity loss. You can rest and recover from burnout. AI fatigue requires rebuilding relationship with your own skills. They're related but not identical. The burnout-vs-fatigue page goes deeper if you're curious.

### Angle 2: "71% of middlemen — how was this measured?"
> Survey of 3,000+ engineers who took the quiz. The quiz isn't scientifically validated (we're transparent about that), but the patterns are consistent enough that we think there's something real here. The methodology is on the engineer-survey-results page.

### Angle 3: "Why not just use AI less?"
> This is exactly what the recovery plan recommends. The challenge is that "just use AI less" isn't simple in practice — team velocity pressure, code review expectations, learning curve pressure. The site has a framework for having that conversation with your manager: https://clearing-ai.com/workplace.html

### Angle 4: "Another productivity tool..."
> Not a productivity tool. No tracking, no gamification, no streaks leaderboard. The goal is recovery, not optimization. The deepest page on the site is the recovery guide: https://clearing-ai.com/recovery.html — it's about what you do when you realize the problem isn't that you're lazy.

### Angle 5: "Who are you to write about this?"
> Fair question. I'm not a researcher — I'm an engineer who watched friends go through this and couldn't find a name for it. The site cites real research (Gloria Mark, Sophie Leroy, John Sweller, Maslach burnout model) and the quiz data is from real engineers. We try to be honest about what we know and what we're guessing.

---

## If HN Underperforms (Not in Top 10 after 2h)

**Fall back to Reddit Weekend 2 package:**
- 5 Reddit comments ready (logs/hour-378-2026-04-16-1544-phase2-reddit-weekend2-hn.md)
- Deploy to: r/programming, r/cscareerquestions, r/ExperiencedDevs, r/AskProgramming, r/webdev
- Twitter Thread #19 still goes live at 12-2PM
- Cassidoo follow-up already sent at 8AM

---

## Traffic Expectations

| Outcome | Probability | Visits | Newsletter Signups |
|----------|------------|--------|-------------------|
| Top 5 HN | 15% | 5,000-10,000 | 100-300 |
| Top 10 HN | 25% | 2,000-5,000 | 50-150 |
| Top 30 HN | 30% | 500-2,000 | 20-80 |
| Page 2 HN | 20% | 100-500 | 5-20 |
| No HN traction | 10% | <100 | 0-5 |

**Critical path for newsletter capture:**
1. HN visitor → index-hn.html → quiz → newsletter-thank-you.html
2. HN visitor → index-hn.html → hn-visitor-guide.html → newsletter signup
3. All paths should end with newsletter capture

---

## Post-HN Email Sequence (Triggered by Newsletter Signup)

### Email 1 — Welcome (Send immediately)
```
Subject: Welcome to The Clearing — here's where to start

Hey,

You came from Hacker News today. Welcome.

The Clearing is a resource for engineers experiencing AI fatigue — the feeling that your code ships but you don't feel like you built it anymore, your skills are declining, and Sunday night dread is now a weekly pattern.

Here's what to do first:

1. Take the 5-question AI Fatigue Quiz (https://clearing-ai.com/#quiz) — it takes 3 minutes and you'll get a tier and recommended actions

2. Read your tier deep-dive — each tier has its own page with specific recovery steps

3. Try the Explanation Requirement today — before you accept any AI suggestion, write one sentence about why you chose it. It sounds small. It isn't.

We'll send you one email per week — The Dispatch — with something useful: a story, a tactic, a data point, a research finding.

See you Sunday.

— The Clearing
```

### Email 2 — 3 Days Post-Signup
```
Subject: The first thing most people try

Most engineers who sign up tell us they tried the Explanation Requirement first.

The rule: before you accept any AI suggestion, write one sentence about why it's correct. Not what it does — why YOU chose it.

It sounds trivial. Three things happen:

1. You notice when you can't explain it — which means you don't actually understand it
2. You catch yourself before going on autopilot
3. Your learning loop reactivates

There's a full page on it if you want to go deeper:
https://clearing-ai.com/the-explanation-requirement.html

How did it go? Reply and let me know — I read every email.

— The Clearing
```

### Email 3 — 7 Days Post-Signup
```
Subject: What 3,000 engineers told us

We ran a survey of 3,000+ engineers who took the AI Fatigue Quiz. Four numbers kept showing up:

71% feel like middlemen — their code ships but they don't feel like they built it
63% feel like strangers to their own work  
58% notice their skills declining in specific areas
44% have considered leaving the profession entirely

These aren't burnout numbers. Burnout is about workload. This is about craft erosion, identity loss, the feeling that you're watching yourself get worse at something you spent years learning.

The full survey results are here:
https://clearing-ai.com/engineer-survey-results.html

The pattern we hear most: "I thought it was just me."

It's not just you.

— The Clearing
```

### Email 4 — 14 Days Post-Signup
```
Subject: The 30-day plan

If you've been meaning to actually do something about the AI fatigue pattern, here's a structured starting point.

The 30-Day AI Fatigue Recovery Plan:
https://clearing-ai.com/ai-detox-plan.html

It has four phases:
- Week 1: Awareness — what exactly is happening and why
- Week 2: Reduction — cutting back AI use deliberately 
- Week 3: Reconnection — rebuilding relationship with your own skills
- Week 4: Integration — sustainable healthy AI use

It's based on cognitive science (attention residue, cognitive load theory, skill atrophy research) and feedback from thousands of engineers who've gone through it.

Pick one thing from Week 1 and do it today.

— The Clearing
```

### Email 5 — 30 Days Post-Signup (Post-HN Retrospective)
```
Subject: What we learned from 3,000 engineers

A month ago we launched on Hacker News. 3,000+ engineers took the quiz in 24 hours.

The most common response we got: "I thought it was just me."

That response came from senior engineers with 15 years of experience. From bootcamp grads six months into their first job. From Staff engineers who couldn't explain why they felt like beginners again. From managers watching their teams quietly fall apart.

AI fatigue doesn't have a clean solution. But naming it helps. Understanding the mechanisms helps. Knowing you're not alone helps.

The survey results, the recovery plan, the research — it's all still there:
https://clearing-ai.com

If you're still in it, the next Dispatch goes out Sunday.

— The Clearing
```

---

## HN Success Metrics (Track for 48h)

```
 HN URL: https://news.ycombinator.com/item?id=[ID]
 HN Title: "I built a free AI fatigue recovery tool..."
 
 Hour 1: Position? ___ | Points? ___ | Comments? ___
 Hour 2: Position? ___ | Points? ___ | Comments? ___
 Hour 4: Position? ___ | Points? ___ | Comments? ___
 Hour 8: Position? ___ | Points? ___ | Comments? ___
 Hour 24: Position? ___ | Points? ___ | Comments? ___
 Hour 48: FINAL — Position? ___ | Points? ___ | Comments? ___

 Google Analytics:
 - Sessions from HN: ___
 - Newsletter signups: ___
 - Quiz completions: ___
 - Top pages visited: ___
 
 Newsletter:
 - New subscribers: ___
 - Open rate: ___%

 Return visit rate (7 days): ___%
```

---

## Assets Ready to Deploy

| Asset | Status | When |
|-------|--------|------|
| HN submission | READY | 9:00 AM PDT Fri |
| Cassidoo Follow-up #4 | READY | 8:00 AM PDT Fri |
| Twitter Thread #19 (Middleman) | READY | 12-2PM PDT Fri |
| Twitter Thread #20 (Debugger) | READY | 10:30AM PDT Fri |
| Reddit Weekend 2 comments | READY | If HN underperforms |
| Post-HN email sequence | THIS BUILD | Ready to trigger |
| hn-visitor-guide.html | LIVE | HN visitors arrive |
| hn-launch.html | LIVE | Social share hub |

---

## If Top 5 HN — Amplify Actions

1. Immediately tweet stat: "We just hit #4 on HN — 3,000 engineers took the quiz in 24 hours"
2. Send Cassidoo Follow-up #5 (already drafted, send 1h after HN peak)
3. Post Thread #19 + #20 on Twitter with HN position screenshot
4. Update press release with HN moment (drafted in press-kit.html)
5. Send Dispatch #27 to existing subscribers: "What just happened on HN"
6. Monitor r/programming for cross-post (often happens if HN >200 points)

---

Last updated: 2026-04-16 20:44 PDT (9h before HN)
Commit after HN results: Hour 380 — HN Launch Day Results