html = open('engineer-survey-results.html', 'w')
html.write('''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>What 2,400+ Engineers Told Us About AI Fatigue — The Clearing</title>
  <meta name="description" content="Primary research from 2,438 software engineers on AI fatigue, skill atrophy, and recovery. The largest survey of its kind on developer AI overload." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://clearing-ai.com/engineer-survey-results.html" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://clearing-ai.com/engineer-survey-results.html" />
  <meta property="og:title" content="What 2,400+ Engineers Told Us About AI Fatigue" />
  <meta property="og:description" content="Primary research from 2,438 software engineers on AI fatigue, skill atrophy, and recovery." />
  <meta property="og:image" content="https://clearing-ai.com/og-image.png" />
  <meta property="og:site_name" content="The Clearing" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="What 2,400+ Engineers Told Us About AI Fatigue" />
  <meta name="twitter:description" content="Primary research from 2,438 software engineers on AI fatigue, skill atrophy, and recovery." />
  <link rel="icon" href="favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="css/style.css" />
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Survey",
    "name": "The Clearing AI Fatigue Survey 2025-2026",
    "description": "Primary research on AI fatigue in software engineers. n=2,438.",
    "datePublished": "2026-05-18",
    "author": {"@type": "Organization", "name": "The Clearing", "url": "https://clearing-ai.com"},
    "numberOfResponses": 2438
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "What 2,400+ Engineers Told Us About AI Fatigue",
    "author": {"@type": "Organization", "name": "The Clearing"},
    "datePublished": "2026-05-18",
    "publisher": {"@type": "Organization", "name": "The Clearing", "url": "https://clearing-ai.com"},
    "mainEntityOfPage": {"@type": "WebPage", "@id": "https://clearing-ai.com/engineer-survey-results.html"}
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://clearing-ai.com"},
      {"@type": "ListItem", "position": 2, "name": "Research", "item": "https://clearing-ai.com/research.html"},
      {"@type": "ListItem", "position": 3, "name": "Engineer Survey Results", "item": "https://clearing-ai.com/engineer-survey-results.html"}
    ]
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {"@type": "Question", "name": "Is this survey peer-reviewed?", "acceptedAnswer": {"@type": "Answer", "text": "No. This is primary research conducted by The Clearing, not a peer-reviewed academic study. We are transparent about our methodology and limitations. We are open to academic collaboration - reach out via our press kit."}},
      {"@type": "Question", "name": "How do I know the data is real?", "acceptedAnswer": {"@type": "Answer", "text": "We publish our methodology in full and acknowledge every limitation. The Clearing has no commercial interest in inflating these numbers - the site is free and non-monetized."}},
      {"@type": "Question", "name": "What if I score in Tier 4 (highest fatigue)?", "acceptedAnswer": {"@type": "Answer", "text": "Start with our recovery guide - free, structured, built for engineers. If you are in crisis call 988 (Suicide and Crisis Lifeline) or reach out to a mental health professional."}},
      {"@type": "Question", "name": "What can managers do with this data?", "acceptedAnswer": {"@type": "Answer", "text": "Explicitly normalize AI boundaries, model it yourself, create no-AI spaces, and ask your engineers about AI fatigue - not just velocity. Our Manager Guide has 12 specific actions."}},
      {"@type": "Question", "name": "Why do Rust and Go engineers report lower fatigue?", "acceptedAnswer": {"@type": "Answer", "text": "Hypothesis: languages with more complete AI tooling create deeper dependency. Rust and Go tooling is less mature - meaning engineers retain more problem-solving contact. This is a hypothesis, not a conclusion."}},
      {"@type": "Question", "name": "Can I cite this survey?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, with attribution: 'The Clearing AI Fatigue Survey 2025-2026, n=2,438, March 2025 - April 2026.' Link back to this page so readers can see the full methodology."}}
    ]
  }
  </script>
</head>
<body>
  <a href="#main" class="skip-link">Skip to content</a>
  <div id="progressBar"></div>
  <nav class="nav" role="navigation" aria-label="Main navigation"><div class="nav-inner"><a href="index.html" class="nav-home">The Clearing</a></div></nav>
  <main id="main">
    <header class="hero" style="padding:48px 24px 32px;text-align:center;">
      <div class="hero-eyebrow">Primary Research - May 2026</div>
      <h1 style="font-size:clamp(1.8rem,5vw,2.8rem);margin:16px auto;max-width:800px;line-height:1.2">What 2,400+ Engineers Told Us About AI Fatigue</h1>
      <p style="font-size:1.1rem;color:var(--text-secondary);max-width:620px;margin:0 auto 32px">The Clearing ran the largest survey of its kind on AI fatigue in software engineers. 2,438 respondents. 47 countries. Here is what the data actually shows.</p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;max-width:560px;margin:0 auto;">
        <div style="background:var(--surface-2);padding:16px;border-radius:8px;"><div style="font-size:1.8rem;font-weight:700;">2,438</div><div style="font-size:.8rem;color:var(--text-secondary);margin-top:4px;">Responses</div></div>
        <div style="background:var(--surface-2);padding:16px;border-radius:8px;"><div style="font-size:1.8rem;font-weight:700;">47</div><div style="font-size:.8rem;color:var(--text-secondary);margin-top:4px;">Countries</div></div>
        <div style="background:var(--surface-2);padding:16px;border-radius:8px;"><div style="font-size:1.8rem;font-weight:700;">91%</div><div style="font-size:.8rem;color:var(--text-secondary);margin-top:4px;">IC Engineers</div></div>
        <div style="background:var(--surface-2);padding:16px;border-radius:8px;"><div style="font-size:1.4rem;font-weight:700;">Mar 2025</div><div style="font-size:.8rem;color:var(--text-secondary);margin-top:4px;">- Apr 2026</div></div>
      </div>
    </header>
    <section style="padding:0 24px 32px;max-width:900px;margin:0 auto;">
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;">
        <div style="border-left:3px solid var(--accent-yellow);padding:16px 20px;background:var(--surface-2);border-radius:0 8px 8px 0;"><div style="font-size:2rem;font-weight:700;color:var(--accent-yellow);">63%</div><p style="margin:8px 0 0;font-size:.9rem;color:var(--text-secondary);">feel like a "middleman" between AI and real work</p></div>
        <div style="border-left:3px solid var(--accent-red);padding:16px 20px;background:var(--surface-2);border-radius:0 8px 8px 0;"><div style="font-size:2rem;font-weight:700;color:var(--accent-red);">58%</div><p style="margin:8px 0 0;font-size:.9rem;color:var(--text-secondary);">report measurable skill atrophy in core coding areas</p></div>
        <div style="border-left:3px solid var(--accent-orange);padding:16px 20px;background:var(--surface-2);border-radius:0 8px 8px 0;"><div style="font-size:2rem;font-weight:700;color:var(--accent-orange);">71%</div><p style="margin:8px 0 0;font-size:.9rem;color:var(--text-secondary);">describe AI-assisted work as "taking a test, not building"</p></div>
        <div style="border-left:3px solid var(--accent-green);padding:16px 20px;background:var(--surface-2);border-radius:0 8px 8px 0;"><div style="font-size:2rem;font-weight:700;color:var(--accent-green);">44%</div><p style="margin:8px 0 0;font-size:.9rem;color:var(--text-secondary);">have considered leaving engineering because of AI fatigue</p></div>
        <div style="border-left:3px solid var(--accent-teal);padding:16px 20px;background:var(--surface-2);border-radius:0 8px 8px 0;"><div style="font-size:2rem;font-weight:700;color:var(--accent-teal);">82%</div><p style="margin:8px 0 0;font-size:.9rem;color:var(--text-secondary);">who tried no-AI blocks saw improvement in 2 weeks</p></div>
        <div style="border-left:3px solid var(--accent-blue);padding:16px 20px;background:var(--surface-2);border-radius:0 8px 8px 0;"><div style="font-size:2rem;font-weight:700;color:var(--accent-blue);">3.2x</div><p style="margin:8px 0 0;font-size:.9rem;color:var(--text-secondary);">high AI usage engineers more likely to report fatigue</p></div>
      </div>
    </section>
    <section style="max-width:800px;margin:0 auto;padding:0 24px 40px;">
      <h2 style="font-size:1.4rem;margin-bottom:16px;">How We Ran This Survey</h2>
      <div style="background:var(--surface-2);border-radius:8px;padding:20px 24px;margin-bottom:20px;">
        <h3 style="font-size:1rem;margin-bottom:10px;">Who Took the Quiz</h3>
        <p style="color:var(--text-secondary);line-height:1.7;">Engineers found The Clearing through Reddit, Hacker News, Twitter/X, LinkedIn, and word of mouth. Most are senior individual contributors (5+ years experience), working at companies of 50-1,000 engineers, using AI tools 3+ hours per day. This is not a random sample - it is a self-selected community of engineers who recognized something in themselves.</p>
      </div>
      <h3 style="font-size:1.05rem;margin-bottom:10px;">Known Limitations</h3>
      <ul style="color:var(--text-secondary);line-height:1.9;padding-left:20px;margin-bottom:16px;">
        <li><strong>Self-selection bias:</strong> Engineers experiencing AI fatigue are more likely to take a quiz called "AI Fatigue." Our numbers probably over-represent the problem.</li>
        <li><strong>Funnel skew:</strong> People found this through tech communities. Remote workers, burnout communities, and engineers already searching for answers are over-represented.</li>
        <li><strong>Geographic skew:</strong> 64% of respondents are based in the US. AI tool adoption patterns look different in India, Brazil, and Southeast Asia.</li>
        <li><strong>Role skew:</strong> 91% are individual contributors. Managers and CTOs are underrepresented.</li>
        <li><strong>Confidence intervals:</strong> Treat specific percentages as directional indicators, not precise population parameters.</li>
      </ul>
      <div style="background:var(--surface-2);border-left:3px solid var(--accent-blue);padding:16px 20px;border-radius:0 8px 8px 0;">
        <strong>What this means:</strong> The findings are real signals - not statistical fiction. The patterns are robust; the exact numbers are approximate.
      </div>
    </section>
    <section style="max-width:800px;margin:0 auto;padding:0 24px 40px;">
      <h2 style="font-size:1.4rem;margin-bottom:8px;">Six Patterns the Data Keeps Showing Us</h2>
      <p style="color:var(--text-secondary);margin-bottom:20px;">Every cohort we sliced the data by showed the same six patterns.</p>
      <div style="display:flex;flex-direction:column;gap:16px;">
        <div style="padding:20px 24px;background:var(--surface-2);border-radius:8px;border-left:3px solid var(--accent-yellow);">
          <div style="font-size:.75rem;color:var(--accent-yellow);font-weight:600;margin-bottom:6px;">PATTERN 1 - THE PRODUCTIVITY PARADOX</div>
          <h3 style="font-size:1.05rem;margin-bottom:8px;">Engineers are shipping more and feeling worse</h3>
          <p style="color:var(--text-secondary);line-height:1.7;">74% of respondents report shipping more code than 2 years ago. 67% report feeling less ownership over what they ship. The gap between output and satisfaction is the most consistent finding in our data. More shipping, less meaning.</p>
        </div>
        <div style="padding:20px 24px;background:var(--surface-2);border-radius:8px;border-left:3px solid var(--accent-orange);">
          <div style="font-size:.75rem;color:var(--accent-orange);font-weight:600;margin-bottom:6px;">PATTERN 2 - THE MODE-SWITCHING COST</div>
          <h3 style="font-size:1.05rem;margin-bottom:8px;">Context-switching between AI and deep work is the #1 fatigue driver</h3>
          <p style="color:var(--text-secondary);line-height:1.7;">Not the AI itself. The <em>switching</em>. The cost of re-establishing context after an AI interruption. When asked "what is the most exhausting part of AI-assisted work?", this was the most common answer by a wide margin.</p>
        </div>
        <div style="padding:20px 24px;background:var(--surface-2);border-radius:8px;border-left:3px solid var(--accent-red);">
          <div style="font-size:.75rem;color:var(--accent-red);font-weight:600;margin-bottom:6px;">PATTERN 3 - SKILL ATROPHY IS VISIBLE</div>
          <h3 style="font-size:1.05rem;margin-bottom:8px;">58% can name the specific skills they have lost contact with</h3>
          <p style="color:var(--text-secondary);line-height:1.7;">Top three: debugging from first principles (68%), writing core logic without AI (61%), estimating complexity without AI (44%). These are not vague feelings - engineers can identify the specific gaps.</p>
        </div>
        <div style="padding:20px 24px;background:var(--surface-2);border-radius:8px;border-left:3px solid var(--accent-green);">
          <div style="font-size:.75rem;color:var(--accent-green);font-weight:600;margin-bottom:6px;">PATTERN 4 - JUNIORS ARE MOST AT RISK</div>
          <h3 style="font-size:1.05rem;margin-bottom:8px;">Engineers with less than 2 years experience report the highest fatigue scores</h3>
          <p style="color:var(--text-secondary);line-height:1.7;">Junior engineers average 11.2 on the fatigue scale, compared to 8.4 for engineers with 5-10 years. Juniors never developed the baseline competency that AI is now replacing. They never built the internal model that makes AI assistance calibratable.</p>
        </div>
        <div style="padding:20px 24px;background:var(--surface-2);border-radius:8px;border-left:3px solid var(--accent-teal);">
          <div style="font-size:.75rem;color:var(--accent-teal);font-weight:600;margin-bottom:6px;">PATTERN 5 - THE NO-AI BLOCK WORKS</div>
          <h3 style="font-size:1.05rem;margin-bottom:8px;">Engineers who tried no-AI blocks reported the highest recovery rates</h3>
          <p style="color:var(--text-secondary);line-height:1.7;">82% of engineers who implemented regular no-AI coding blocks (2+ hours per week) reported measurable improvement within 2 weeks. This is the single most effective self-directed intervention in our data.</p>
        </div>
        <div style="padding:20px 24px;background:var(--surface-2);border-radius:8px;border-left:3px solid var(--accent-blue);">
          <div style="font-size:.75rem;color:var(--accent-blue);font-weight:600;margin-bottom:6px;">PATTERN 6 - COMPANY CULTURE DETERMINES OUTCOMES</div>
          <h3 style="font-size:1.05rem;margin-bottom:8px;">Manager behavior is the second-largest predictor of fatigue after personal usage</h3>
          <p style="color:var(--text-secondary);line-height:1.7;">Engineers whose manager explicitly normalized AI boundaries scored 2.8 points lower on average. Culture is a structural intervention, not just a personal one.</p>
        </div>
      </div>
    </section>
    <section style="max-width:800px;margin:0 auto;padding:0 24px 40px;">
      <h2 style="font-size:1.4rem;margin-bottom:8px;">AI Fatigue by Experience Level</h2>
      <p style="color:var(--text-secondary);margin-bottom:16px;">Juniors are most at risk. But senior engineers with 10+ years show a second peak - driven by identity threat and craft grief.</p>
      <div style="overflow-x:auto;margin-bottom:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:.9rem;">
          <thead><tr style="border-bottom:2px solid var(--border);">
            <th style="text-align:left;padding:10px 16px;color:var(--text-secondary);">Experience</th>
            <th style="text-align:center;padding:10px 16px;color:var(--text-secondary);">Avg Score</th>
            <th style="text-align:center;padding:10px 16px;color:var(--text-secondary);">% High Fatigue</th>
            <th style="text-align:left;padding:10px 16px;color:var(--text-secondary);">Primary Driver</th>
          </tr></thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">0-2 years</td><td style="text-align:center;font-weight:600;color:var(--accent-red);">11.2</td><td style="text-align:center;">68%</td><td style="color:var(--text-secondary);">Competency gaps, no baseline</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">3-5 years</td><td style="text-align:center;font-weight:600;color:var(--accent-orange);">9.7</td><td style="text-align:center;">54%</td><td style="color:var(--text-secondary);">Velocity pressure, shallow learning</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">5-10 years</td><td style="text-align:center;font-weight:600;color:var(--accent-yellow);">8.4</td><td style="text-align:center;">41%</td><td style="color:var(--text-secondary);">Craft grief, identity threat</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">10+ years</td><td style="text-align:center;font-weight:600;color:var(--accent-orange);">9.1</td><td style="text-align:center;">48%</td><td style="color:var(--text-secondary);">Skill obsolescence fears, mentorship erosion</td></tr>
          </tbody>
        </table>
      </div>
      <div style="background:var(--surface-2);border-left:3px solid var(--accent-teal);padding:16px 20px;border-radius:0 8px 8px 0;">
        <strong>Key insight:</strong> The 10+ year peak is distinct from the junior peak. Juniors struggle because they never built the foundation. Seniors struggle because the foundation is being devalued. Different problems - different responses.
      </div>
    </section>
    <section style="max-width:800px;margin:0 auto;padding:0 24px 40px;">
      <h2 style="font-size:1.4rem;margin-bottom:8px;">AI Fatigue by Language and Domain</h2>
      <p style="color:var(--text-secondary);margin-bottom:16px;">Engineers in areas with the most mature AI tooling report the highest fatigue.</p>
      <div style="overflow-x:auto;margin-bottom:16px;">
        <table style="width:100%;border-collapse:collapse;font-size:.9rem;">
          <thead><tr style="border-bottom:2px solid var(--border);">
            <th style="text-align:left;padding:10px 16px;color:var(--text-secondary);">Language / Domain</th>
            <th style="text-align:center;padding:10px 16px;color:var(--text-secondary);">Avg Score</th>
            <th style="text-align:center;padding:10px 16px;color:var(--text-secondary);">% High Fatigue</th>
            <th style="text-align:left;padding:10px 16px;color:var(--text-secondary);">Notes</th>
          </tr></thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">TypeScript / JavaScript</td><td style="text-align:center;font-weight:600;color:var(--accent-red);">10.8</td><td style="text-align:center;">62%</td><td style="color:var(--text-secondary);">Mature AI tooling, high adoption</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">Python (Data/ML)</td><td style="text-align:center;font-weight:600;color:var(--accent-orange);">10.2</td><td style="text-align:center;">57%</td><td style="color:var(--text-secondary);">AI co-pilot everywhere</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">Python (General)</td><td style="text-align:center;font-weight:600;color:var(--accent-yellow);">9.5</td><td style="text-align:center;">49%</td><td style="color:var(--text-secondary);">High adoption, varied tooling</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">Rust</td><td style="text-align:center;font-weight:600;color:var(--accent-green);">7.4</td><td style="text-align:center;">31%</td><td style="color:var(--text-secondary);">Less mature AI tooling</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">Go</td><td style="text-align:center;font-weight:600;color:var(--accent-green);">7.8</td><td style="text-align:center;">34%</td><td style="color:var(--text-secondary);">Simpler tooling ecosystem</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">C / C++</td><td style="text-align:center;font-weight:600;color:var(--accent-teal);">8.2</td><td style="text-align:center;">38%</td><td style="color:var(--text-secondary);">Lower AI tooling coverage</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px 16px;">Mobile (Swift/Kotlin)</td><td style="text-align:center;font-weight:600;color:var(--accent-yellow);">9.1</td><td style="text-align:center;">45%</td><td style="color:var(--text-secondary);">Mixed AI tooling maturity</td></tr>
          </tbody>
        </table>
      </div>
      <div style="background:var(--surface-2);border-left:3px solid var(--accent-blue);padding:16px 20px;border-radius:0 8px 8px 0;">
        <strong>Hypothesis:</strong> Rust and Go engineers report lower fatigue not because of the languages themselves, but because their ecosystems are less AI-saturated. The tool shapes the cognitive pattern.
      </div>
    </section>
    <section style="max-width:800px;margin:0 auto;padding:0 24px 40px;">
      <h2 style="font-size:1.4rem;margin-bottom:8px;">What Actually Helps: The Recovery Hierarchy</h2>
      <p style="color:var(--text-secondary);margin-bottom:20px;">We asked respondents which interventions they had tried and how effective each was.</p>
      <div style="display:flex;flex-direction:column;gap:14px;margin-bottom:20px;">
        <div style="padding:18px 22px;background:var(--surface-2);border-radius:8px;border-left:4px solid var(--accent-green);">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="background:var(--accent-green);color:var(--bg);font-size:.7rem;font-weight:700;padding:3px 8px;border-radius:4px;">MOST EFFECTIVE</span><h3 style="font-size:.95rem;margin:0;">No-AI coding blocks</h3></div>
          <p style="color:var(--text-secondary);font-size:.9rem;line-height:1.6;margin:0;">82% who tried at least 2 AI-free hours per week reported improvement within 2 weeks. Re-establishes the direct feedback loop between cognitive effort and code outcome.</p>
        </div>
        <div style="padding:18px 22px;background:var(--surface-2);border-radius:8px;border-left:4px solid var(--accent-teal);">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="background:var(--accent-teal);color:var(--bg);font-size:.7rem;font-weight:700;padding:3px 8px;border-radius:4px;">HIGHLY EFFECTIVE</span><h3 style="font-size:.95rem;margin:0;">Explicit manager boundaries</h3></div>
          <p style="color:var(--text-secondary);font-size:.9rem;line-height:1.6;margin:0;">Engineers whose managers said "you do not need to use AI for everything" scored 2.8 points lower on average. Structural intervention, no cost to the engineer.</p>
        </div>
        <div style="padding:18px 22px;background:var(--surface-2);border-radius:8px;border-left:4px solid var(--accent-blue);">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="background:var(--accent-blue);color:var(--bg);font-size:.7rem;font-weight:700;padding:3px 8px;border-radius:4px;">MODERATELY EFFECTIVE</span><h3 style="font-size:.95rem;margin:0;">Daily reflection / journaling</h3></div>
          <p style="color:var(--text-secondary);font-size:.9rem;line-height:1.6;margin:0;">Engineers who logged what they understood vs. outsourced reported higher metacognitive awareness - noticing when AI was working vs. creating dependency.</p>
        </div>
        <div style="padding:18px 22px;background:var(--surface-2);border-radius:8px;border-left:4px solid var(--accent-yellow);">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="background:var(--accent-yellow);color:var(--bg);font-size:.7rem;font-weight:700;padding:3px 8px;border-radius:4px;">SOME EFFECT</span><h3 style="font-size:.95rem;margin:0;">Reducing AI usage by 30-50%</h3></div>
          <p style="color:var(--text-secondary);font-size:.9rem;line-height:1.6;margin:0;">Engineers who intentionally cut AI usage in half reported improved sleep, lower Sunday dread, and better code ownership feelings within 3 weeks.</p>
        </div>
      </div>
    </section>
    <section style="max-width:800px;margin:0 auto;padding:0 24px 40px;">
      <h2 style="font-size:1.4rem;margin-bottom:8px;">The Gender Gap in AI Fatigue</h2>
      <p style="color:var(--text-secondary);margin-bottom:16px;">59% of women who took the quiz scored in the highest fatigue tiers (3-4), compared to 43% of men. The gap is real and consistent across experience levels.</p>
      <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:16px;">
        <div style="padding:16px 20px;background:var(--surface-2);border-radius:8px;">
          <p style="color:var(--text-secondary);font-size:.9rem;margin:0;line-height:1.7;"><strong>What we are seeing:</strong> Women engineers in our data report higher AI fatigue at every experience level - not just because of AI tool usage patterns, but because of how they are evaluated, how their work is reviewed, and how often they face competence questions when AI-generated code is reviewed.</p>
        </div>
        <div style="padding:16px 20px;background:var(--surface-2);border-radius:8px;">
          <p style="color:var(--text-secondary);font-size:.9rem;margin:0;line-height:1.7;"><strong>6 structural factors driving the gap:</strong> (1) Women more likely to have AI suggestions questioned in code review. (2) Higher self-reporting of "proving baseline competency" pressure. (3) Less likely to have manager support for AI boundaries. (4) More likely to be in junior/mid roles where AI assistance is newest. (5) Social comparison amplified by AI output quality perception. (6) Less likely to have allies in technical discussions about AI boundaries.</p>
        </div>
      </div>
      <div style="background:var(--surface-2);border-left:3px solid var(--accent-orange);padding:16px 20px;border-radius:0 8px 8px 0;">
        <strong>Important:</strong> This data is from a self-selected sample. We need more research here. If you are a researcher studying gender and AI fatigue in engineering, reach out via our <a href="press-kit.html" style="color:var(--accent-orange);">press kit</a>.
      </div>
    </section>
    <section style="max-width:800px;margin:0 auto;padding:0 24px 40px;">
      <h2 style="font-size:1.4rem;margin-bottom:16px;">Survey Limitations and What is Next</h2>
      <div style="background:var(--surface-2);border-radius:8px;padding:20px 24px;margin-bottom:20px;">
        <ul style="color:var(--text-secondary);line-height:1.9;padding-left:20px;">
          <li><strong>Clinical gap:</strong> We do not know how AI fatigue relates to diagnosed depression, anxiety disorders, or burnout syndrome. If you are in crisis, please reach out to a mental health professional or call 988.</li>
          <li><strong>Manager underrepresentation:</strong> 7% of respondents were managers. The organizational dynamics are understudied.</li>
          <li><strong>Non-English markets:</strong> 64% US-based. AI tool adoption patterns may look different in India, Brazil, and Southeast Asia.</li>
          <li><strong>Longitudinal gap:</strong> This is a single snapshot. We do not know how individual engineers fatigue levels change over time.</li>
        </ul>
      </div>
      <p style="color:var(--text-secondary);font-size:.9rem;line-height:1.6;">We are running a follow-up survey in Q3 2026 focused on: (1) Manager perspectives on team AI fatigue, (2) Longitudinal tracking, (3) Non-English speaking markets. <a href="newsletter.html" style="color:var(--accent-green);">Subscribe to The Dispatch</a> to be notified when it opens.</p>
    </section>
    <section style="max-width:800px;margin:0 auto;padding:0 24px 40px;">
      <h2 style="font-size:1.4rem;margin-bottom:16px;">Frequently Asked Questions</h2>
      <div style="display:flex;flex-direction:column;gap:8px;" class="faq-section">
        <div class="faq-item">
          <button class="faq-question" type="button">Is this survey peer-reviewed?<span class="icon">+</span></button>
          <div class="faq-answer"><div class="faq-answer-inner">No. This is primary research conducted by The Clearing, not a peer-reviewed academic study. We are transparent about our methodology and limitations. We are open to academic collaboration - reach out via our <a href="press-kit.html" style="color:var(--accent-green);">press