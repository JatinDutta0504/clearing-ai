#!/usr/bin/env python3
"""Add FAQ sections to 8 pages that have FAQPage JSON-LD but no visible FAQ content."""

import re

# FAQ data for each page: (filename, questions_list_of_tuples)
FAQ_DATA = {
    "senior-engineer-ai-fatigue.html": [
        ("Why is AI fatigue different for senior engineers than junior engineers?",
         "Senior engineers experience a deeper identity threat because they have more to lose. Years of hard-won expertise, architectural judgment, and craft identity are directly challenged by AI tools that produce outputs comparable to senior-level work. Juniors face skill atrophy risk; seniors face existential identity crisis."),
        ("Is this imposter syndrome or something else?",
         "It's neither imposter syndrome nor ordinary burnout — it's role displacement anxiety compounded by industry gaslighting. Imposter syndrome is a cognitive distortion about your own abilities. This is a functional, measurable shift: the code you're shipping isn't the code you're authoring, and the learning loop that made you senior is now broken."),
        ("How does AI affect architectural thinking specifically?",
         "Architectural thinking requires sitting with ambiguity long enough to see the shape of a solution. AI offers that shape immediately. Taking it means you stop sitting with the ambiguity — and that muscle atrophies. Senior engineers who use AI heavily report decreased confidence in their ability to design systems from scratch, not because their intelligence changed, but because they stopped doing the deliberate practice that built that skill."),
        ("What does 'ghost authorship' feel like?",
         "Ghost authorship is the psychological experience of shipping code you couldn't reproduce. Senior engineers describe it as a form of impostorhood that feels more justified than classic imposter syndrome — because they're right. They genuinely don't fully own the code. The feeling compounds over months as the gap between 'what I ship' and 'what I understand' grows invisibly."),
        ("Are my concerns about AI replacing senior engineers justified?",
         "Partially. The job market for senior engineers is shifting, not collapsing. The engineers most at risk are those who haven't differentiated their value beyond 'shipping features with AI help.' Senior engineers who can do the hard parts AI can't — navigate ambiguity, teach effectively, read a room, make judgment calls in undefined territory — remain genuinely valuable. The risk is real but concentrated among engineers who haven't built those skills."),
        ("How do I talk to my manager about this without sounding afraid of AI?",
         "Frame it around sustainable performance, not AI rejection. Specific script: 'I've noticed I'm learning less on the job than I was two years ago, and I think it's affecting my long-term value to the team. Can we talk about building in some structured time for learning and deep work without AI assistance?' This is a performance concern, not a technology rejection — managers respond to it very differently."),
    ],

    "developer-burnout-recovery.html": [
        ("What's the difference between developer burnout and regular tiredness?",
         "Tiredness resolves with a good night's sleep. Burnout is a systemic depletion that sleep alone cannot fix. Burnout includes emotional exhaustion, cynicism about your work, and feeling professionally ineffective — not just physically tired. If you take a weekend off and feel worse instead of better, that's burnout, not tiredness."),
        ("How long does developer burnout recovery take?",
         "Minimum 4–6 weeks for acute symptoms to ease, 3–6 months for meaningful recovery, and 12–18 months for full reconstruction of sustainable work patterns. Most engineers underestimate this timeline and return to work too soon, triggering relapse. The recovery curve is not linear — expect two steps forward, one step back."),
        ("Should I quit my job if I'm burned out as a developer?",
         "Quitting can help if the job itself is the cause and you're in a financial position to take a break. But quitting without a plan often trades burnout for anxiety about income. The better question: 'Can I recover within this job with different boundaries?' If yes, try that first. If the job is structurally broken — impossible expectations, chronic understaffing, values mismatch — leaving may be the right call."),
        ("Do I need therapy or coaching for developer burnout?",
         "If you're experiencing intrusive thoughts, emotional numbness lasting more than 2 weeks, physical symptoms (sleep, appetite, motivation completely disrupted), or thoughts of self-harm — yes, seek professional support. A therapist or psychiatrist can help with clinical burnout or depression. A coach can help with career redesign and boundary-setting. Both have value; they're different tools."),
        ("Can AI tools help or worsen developer burnout recovery?",
         "AI tools can worsen burnout by creating productivity pressure and skill dependency. They can help during recovery by reducing the cognitive load of routine tasks — but only if used intentionally, not compulsively. The worst pattern: using AI to stay productive while burned out, which masks the problem and deepens the depletion. AI during recovery should reduce load, not extend capacity."),
        ("What's the first thing I should do when I realize I'm burned out?",
         "Stop adding to the pile. That means: no new commitments, no side projects, no 'just one more thing' until the acute phase passes. Second: tell someone — a manager, a colleague, a friend. Burnout thrives in isolation. Naming it breaks the shame loop. Third: protect sleep, nutrition, and one activity you enjoy purely for its own sake. Recovery starts with these three, before any bigger interventions."),
    ],

    "engineering-managers-ai-fatigue.html": [
        ("Why are engineering managers especially vulnerable to AI fatigue?",
         "Managers carry a dual burden: they're pressured to adopt AI tools for productivity while being responsible for their team's wellbeing and output. They feel the productivity pressure themselves while simultaneously worrying about what AI means for their reports. Plus, many managers are former ICs — they're watching their own craft erode while trying to lead others through the same disruption."),
        ("How does AI fatigue show up differently for managers than individual contributors?",
         "For ICs, AI fatigue shows as skill atrophy, loss of craft satisfaction, or learning pressure. For managers, it's subtler: dread of technical conversations you can't follow, anxiety about making architecture decisions you used to make confidently, guilt about not staying hands-on, and exhaustion from mediating everyone else's AI fatigue while managing your own."),
        ("How do I talk to my team about AI fatigue without sounding dismissive?",
         "Start with genuine acknowledgment: 'I've noticed a particular kind of exhaustion that seems different from normal tiredness. I want to name it and talk about it openly.' Frame it as a team-level concern, not an individual failure. Ask: 'How is everyone experiencing the increased pace of AI-assisted work? What would help?' This creates permission to be honest without making anyone feel broken."),
        ("What structural changes actually help teams dealing with AI fatigue?",
         "Three changes have highest impact: (1) Protected no-AI time blocks for craft protection — calendar-blocked, team-wide. (2) Explicit norms about AI use in code review and architecture decisions. (3) Learning time built into the schedule — not 'use AI to learn faster' but actual time to build without AI assistance. These require manager advocacy and willingness to accept slower short-term velocity."),
        ("My manager is pressuring me to adopt more AI tools. My team is already stretched. What do I do?",
         "Document actual productivity impact. Have an honest 1:1: 'I want to adopt AI tools that genuinely help us. I also want to flag that my team is at capacity and adding new tooling will require decommissioning something else or accepting quality risk. Can we agree on which tools and set expectations together?' This reframes the conversation from resistance to prioritization."),
        ("How do I know if my team has an AI fatigue problem versus normal tiredness?",
         "Normal tiredness resolves with rest. AI fatigue has a specific texture: people describe work as 'not feeling like work anymore,' they can't articulate what they built last week with confidence, junior engineers aren't progressing despite shipping more, and there are more bugs reaching production. Watch for withdrawal from technical discussions, reluctance to go deep on problems, and increased reliance on AI to explain code rather than understanding it directly."),
    ],

    "freelance-engineer-ai-fatigue.html": [
        ("How is freelance AI fatigue different from employee engineer AI fatigue?",
         "Employee engineers with AI fatigue can lean on teammates, bring it up in 1:1s with managers, or share the mental load of craft erosion with colleagues. Freelance engineers have none of that. You carry the productivity pressure alone, the income precarity alone, the skill anxiety alone. There's no HR department, no team culture, no one to notice if you're quietly falling apart. The isolation is a force multiplier."),
        ("How do I tell a client I won't use AI for their project?",
         "Start with the framing that serves the project, not your fatigue. Say: 'I work in a deliberate, low-AI workflow because it produces more maintainable, well-understood code. My clients own what I build, not what an AI generates.' This is a quality argument, not a technology rejection. Most clients who care about long-term code quality will respect it — and the ones who don't aren't your clients."),
        ("How do freelance engineers maintain skills without a team or peer code review?",
         "The skill maintenance challenge for freelancers is real: no one is reviewing your code, no one is pushing back on your architectural decisions, no one notices when you accept AI suggestions you don't fully understand. Combat this with deliberate practice: weekly no-AI coding sessions, contributing to open source for external review, explaining your code aloud as if teaching someone, and periodic code archaeology — going back to old projects to verify you still understand them."),
        ("Is AI fatigue worse when your income depends on being productive?",
         "Yes. Income precarity is a compounding stressor that makes AI fatigue significantly worse. When a freelancer's productivity drops, the response is often to work more hours and use more AI to compensate — which deepens the fatigue. The trap: using AI to stay productive while burned out, which masks the problem until the skill erosion becomes irreversible. The income pressure makes it harder to take the breaks that recovery requires."),
        ("How do I handle the isolation that makes freelance AI fatigue worse?",
         "Isolation is a force multiplier for AI fatigue. When you're alone with your work, there's no one to notice you're struggling, no one to give you honest feedback on your skills, no one to tell you to stop. Actively build what employment gives you for free: join developer communities (online and in-person), find accountability partners, get a therapist or coach who specializes in tech, and schedule regular 'state of your skills' check-ins with yourself every quarter."),
        ("Should I disclose AI fatigue to clients?",
         "Almost never in raw form. 'I'm experiencing AI fatigue' means nothing to most clients and may make you seem less reliable. What you can say: 'I'm being deliberate about my workflow to ensure quality, which means my turnaround on complex tasks is 2–3 days rather than same-day. This produces better outcomes for your project.' Frame around process and quality, not internal states."),
    ],

    "the-craft-problem.html": [
        ("Is the craft problem the same as burnout?",
         "No. Burnout is exhaustion — you can't do more. The craft problem is worse: you can still ship, still work, still be productive — but you feel the hollow quality of what you're producing. The craft problem is about meaning, not energy. Engineers with the craft problem can still do their jobs; they just feel like they're doing them from inside a shell."),
        ("Does this only affect senior engineers?",
         "It's most visible in senior engineers because they have the sharpest contrast — they remember what the craft used to feel like. But junior engineers are experiencing it too, just differently. Juniors who learned primarily with AI assistance never built the craft foundation that makes the loss feel acute. They may not feel the loss yet — but they're building on sand."),
        ("Isn't this just imposter syndrome?",
         "No. Imposter syndrome is a cognitive distortion — you think you're not capable when you actually are. The craft problem is different: you are genuinely less capable than you used to be, not because you changed, but because the practice that built your capability was disrupted. You have legitimate reasons for the uncertainty. The feeling isn't distorted — it's accurate signal."),
        ("Will using AI less damage my career prospects?",
         "The evidence suggests the opposite. The engineers most in demand right now are the ones who understand what AI can't do — and that understanding only comes from doing the hard parts yourself. AI-assisted engineers are a commodity. Engineers who know when AI is wrong are invaluable. The short-term velocity gain from using AI everywhere is offset by long-term deskilling."),
        ("How do I start recovering my craft?",
         "The most consistently effective starting point we've seen in our data is what we call the Explanation Requirement: before you accept any AI suggestion, close the AI and complete the sentence 'I added this because...' If you can finish it, the authorship loop is intact. If you can't, that's your signal — the gap is where the learning is. Start there. Everything else builds from that one practice."),
        ("Is the craft problem solvable, or is it too late?",
         "It's solvable. Skill atrophy from disuse is not permanent — it's reversible. The research on desirable difficulties (Bjork) shows that skills lost to disuse can be rebuilt with deliberate practice. It takes 4–8 weeks of consistent no-AI practice to see measurable recovery. The craft isn't gone. It's dormant. And it's recoverable, if you're willing to protect the time and tolerate the initial discomfort of rebuilding."),
    ],

    "vibe-coding-vs-traditional.html": [
        ("Is vibe coding bad for your career?",
         "Not categorically — but using it exclusively without deliberate traditional coding practice erodes the foundation your career is built on. Vibe coding is excellent for prototyping, exploration, and tasks where the goal is a working solution, not deep understanding. The risk is when vibe coding becomes the only mode — then you're outsourcing the thinking that makes you valuable."),
        ("Do I need to choose one approach permanently?",
         "No. The best engineers in 2025 are context-sensitive: they vibe code when speed matters and the stakes are low, and they go traditional when understanding, quality, and long-term maintainability matter. The skill is knowing which mode serves which situation — not picking a side."),
        ("How do I know if I've tipped too far toward vibe coding?",
         "Three honest signals: you can't debug a recent feature without AI, you couldn't write a core algorithm from memory in your language of choice, and you don't feel proud of what you ship — you just feel relieved it's done. If those three are true, the balance has tipped. The fix isn't to stop vibe coding; it's to add deliberate traditional practice back in."),
        ("Does vibe coding produce lower quality code?",
         "It produces faster code, but the quality distribution is wider. Vibe-coded solutions can be brilliant or deeply flawed — and you often can't tell the difference without deep understanding of what was generated. Traditional coding produces more consistent quality, slower. The honest answer is: it depends on what you're building, what quality means for that context, and whether you can evaluate the output critically."),
        ("Can you build a career on vibe coding alone?",
         "Possibly short-term, but with real risks: technical interviews become harder, architecture decisions become brittle, and debugging unfamiliar code becomes a constant dependency. The engineers who thrive long-term are the ones who can do both — who can vibe when speed matters and go deep when quality or understanding matters. The career on vibe coding alone gets harder as the field matures."),
        ("What does traditional coding mean in 2025?",
         "Writing code from your own understanding — using an editor, your knowledge, debugging from your mental model, building something you could explain from scratch. Traditional coding isn't a rejection of AI; it's the practice of maintaining the skills that make AI useful rather than replacing them. In 2025, traditional coding is a deliberate practice, not the only way to work."),
    ],

    "working-parent-burnout.html": [
        ("How does AI fatigue affect working parent engineers differently?",
         "Working parent engineers face a compounding problem: AI tools remove natural time boundaries — you can now work in every pocket of time that used to be protected (naptime, evening, weekends). The exhaustion of parenting plus the exhaustion of AI-assisted work compounds into something neither alone would cause. Plus, there's the guilt of using AI to compensate for time with kids, which adds an emotional layer that pure work exhaustion doesn't have."),
        ("Is it okay to use AI to save time as a working parent?",
         "Sometimes, yes — but the key distinction is between using AI to do something you could do yourself (legitimate efficiency) versus using AI to avoid doing something you're no longer capable of doing (compensation that deepens skill erosion). The first is fine. The second is a trap. Track which mode you're in. If most AI use is the second kind, that's a signal worth paying attention to."),
        ("How do I talk to my manager about AI workload pressure as a parent?",
         "Three frameworks that work: (1) Name the structural problem, not your personal limitation — 'the volume of AI-assisted work has created a pace that's hard to sustain alongside my other responsibilities.' (2) Propose a specific structural change — protected focus hours, reduced meeting load, a modified sprint commitment. (3) Frame around sustainable output: 'I'd rather deliver 80% with full attention than 100% with divided attention.'"),
        ("What are the signs that AI is hurting my career as a parent engineer?",
         "Five warning signs specific to parent engineers: (1) You can't remember the last time you debugged something yourself. (2) You feel relief rather than pride when features ship. (3) Your technical conversations at work feel like you're performing rather than contributing. (4) Your manager's 1:1s have become the only time you think about your craft. (5) You've stopped reading technical content outside work because 'there's no time' — but the time went to AI-assisted work, not family."),
        ("How can I protect my skills without sacrificing family time?",
         "Three approaches that actually work for parents: (1) Saturday morning sessions — 90 minutes when kids are occupied, no AI, building something small from scratch. Treat it like a gym appointment. (2) Family-visible work on craft — let kids see you writing code the slow way sometimes. It models that mastery takes time. (3) Strategic AI use: when AI saves you 3 hours, use 1 of those hours for deliberate practice. The other 2 are family time. This is sustainable, honest, and actually works."),
        ("Should I tell my team I'm struggling with AI fatigue?",
         "That depends on your team culture, but naming it specifically — 'I'm experiencing AI fatigue, which means I'm learning less at work and feeling detached from what I build' — is almost always better than suffering quietly. Most managers who care about retention will respond to this. The engineers who don't name it often end up leaving — which is a worse outcome for everyone. Frame around sustainable performance and learning, not exhaustion."),
    ],
}


def build_faq_html(questions):
    """Build HTML for FAQ section given list of (question, answer) tuples."""
    items = []
    for q, a in questions:
        # Strip trailing ellipsis if present
        a = a.rstrip('…').rstrip('.') + '.'
        # Handle HTML entities and special chars
        q_escaped = q.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        a_escaped = a.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        items.append(f'''            <details>
              <summary>{q_escaped}</summary>
              <div>
                <p>{a_escaped}</p>
              </div>
            </details>''')
    
    html = '''        <!-- FAQ Section -->
        <section class="faq-section">
          <h2>Frequently Asked Questions</h2>
          <div class="faq-accordion" role="region" aria-label="Frequently asked questions">

''' + ',\n'.join(items).replace(',', '') + '''

          </div>
        </section>

'''
    return html


def add_faq_to_file(filepath, questions):
    """Add FAQ section to a file before </article>."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if FAQ section already exists
    if 'class="faq-section"' in content:
        print(f"SKIP {filepath}: FAQ section already exists")
        return False
    
    faq_html = build_faq_html(questions)
    
    # Find the last </div> before </article> to insert before
    # We want to find </article> and insert before it
    article_end = content.rfind('</article>')
    if article_end == -1:
        print(f"ERROR {filepath}: No </article> found")
        return False
    
    # Insert FAQ before </article>
    new_content = content[:article_end] + faq_html + content[article_end:]
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"ADDED FAQ to {filepath}")
    return True


def main():
    for filename, questions in FAQ_DATA.items():
        add_faq_to_file(filename, questions)
    
    # Check quiz-results-tier-4 separately
    f4 = "quiz-results-tier-4.html"
    content = open(f4).read()
    if 'class="faq-section"' in content:
        print(f"SKIP {f4}: FAQ section already exists")
    elif '"@type": "FAQPage"' in content:
        print(f"NOTE {f4}: Has FAQPage JSON-LD but no visible FAQ - needs manual check")
    else:
        print(f"NOTE {f4}: No FAQPage JSON-LD found - may not need FAQ section")


if __name__ == "__main__":
    main()
