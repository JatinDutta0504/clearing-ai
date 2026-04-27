#!/usr/bin/env python3
import os
files = {
    "ai-decision-stack.html": [
        ("<h3>Code review as a learning vector</h3>", "engineering-managers-ai-fatigue.html", "For Engineering Managers"),
        ("<h3>Cognitive Cost</h3>", "attention-residue.html", "Attention Residue"),
        ("<h3>Skill heterogeneity amplification</h3>", "the-ai-dependency-trap.html", "AI Dependency Trap"),
        ("<h2>Layer 4: Long-Term Sustainability</h2>", "developer-wellbeing.html", "Developer Wellbeing"),
    ],
    "underrepresented-engineers-ai-fatigue.html": [
        ("<h2>Continue Reading</h2>", "ai-fatigue-by-role.html", "AI Fatigue by Role"),
        ("<h2>Continue Reading</h2>", "engineering-managers-ai-fatigue.html", "For Engineering Managers"),
        ("<h2>Continue Reading</h2>", "hiring.html", "Hiring in the AI Era"),
        ("<h2>Continue Reading</h2>", "imposter-syndrome-ai.html", "Imposter Syndrome & AI"),
    ],
    "ai-learning-burnout.html": [
        ("<h2>The Junior Engineer's Special Problem</h2>", "first-year-engineer-ai-fatigue.html", "First-Year Engineer AI Fatigue"),
        ("<h2>The Sustainable Learning Protocol</h2>", "ai-productivity-paradox.html", "AI Productivity Paradox"),
        ("<h2>The Guilt Work</h2>", "mindset.html", "Mental Models for Healthy AI Use"),
        ("<h2>The Acceleration Problem</h2>", "attention-residue.html", "Attention Residue"),
    ],
    "the-ai-dependency-trap.html": [
        ("<h2>The AI Dependency Trap</h2>", "ai-productivity-paradox.html", "AI Productivity Paradox"),
        ("<h2>", "skill-atrophy.html", "Skill Atrophy"),
        ("<h2>", "automation-anxiety.html", "Automation Anxiety"),
        ("<h2>", "attention-residue.html", "Attention Residue"),
    ],
    "ai-skeptic-engineer.html": [
        ("<h2>The AI Skeptic Engineer</h2>", "automation-anxiety.html", "Automation Anxiety"),
        ("<h3>You might be wrong about:</h3>", "imposter-syndrome-ai.html", "Imposter Syndrome vs AI Fatigue"),
        ("<h2>The Skeptics Who Are Thriving</h2>", "mindset.html", "Mental Models for Healthy AI Use"),
        ("<h2>What To Do With Your Skepticism</h2>", "no-ai-block.html", "The No-AI Block"),
    ],
    "daily-ai-boundaries.html": [
        ("<h2>", "recovery.html", "AI Fatigue Recovery Guide"),
        ("<h2>", "ai-detox-plan.html", "30-Day AI Detox Plan"),
        ("<h2>", "mindset.html", "Mental Models for Healthy AI Use"),
        ("<h2>", "decompress.html", "Deep Work Timer"),
    ],
    "data-engineer-ai-fatigue.html": [
        ("<h2>", "ai-tool-overload.html", "AI Tool Overload"),
        ("<h2>", "inference-fatigue.html", "Inference Fatigue"),
        ("<h2>", "flow-state.html", "Flow State & AI"),
        ("<h2>", "attention-residue.html", "Attention Residue"),
    ],
}
for fname, pairs in files.items():
    if not os.path.exists(fname): print(f"SKIP {fname}"); continue
    lines = open(fname).read().splitlines()
    for search, target, kw in pairs:
        for i, line in enumerate(lines):
            if search in line:
                link = f' <a href="{target}">{kw}</a>'
                for j in range(i, min(i+6, len(lines))):
                    if "<p>" in lines[j] and "</p>" in lines[j]:
                        lines[j] = lines[j].replace("</p>", link+"</p>", 1)
                        print(f"ADD {kw} -> {target} in {fname} at line {j+1}")
                        break
                break
    open(fname, "w").write("\n".join(lines))
print("DONE")
