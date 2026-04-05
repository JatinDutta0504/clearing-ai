path = '/Users/nightcoder/Desktop/TheClearing/coding-ai-tools-comparison.html'
with open(path, 'r') as f:
    lines = f.readlines()

# Keep lines up to and including line 440 (index 439), which is the </section> after debugging
# Actually line 440 is the </section> we want to keep - lines are 1-indexed
# So index 439 = line 440
lines = lines[:440]

# Now append the remaining sections
remaining = """
      <section>
        <div class="use-case">
          <div class="use-case-header">
            <div class="use-case-icon">⚡</div>
            <div><h3 style="margin:0">Task 4: Prototyping a New Feature or Project</h3></div>
          </div>
          <p class="task-desc">You're validating an idea. Speed matters. You want to see if something is roughly possible before investing more time. The code may be thrown away.</p>
          <div class="task-ratings">
            <div class="task-rating"><div class="tool">GitHub Copilot</div><div class="verdict">High productivity — low cognitive load upfront</div><div class="rating r-high">Best for fast prototyping</div></div>
            <div class="task-rating"><div class="tool">Cursor</div><div class="verdict">High productivity — AI-native editing accelerates prototyping</div><div class="rating r-high">Best for fast prototyping</div></div>
            <div class="task-rating"><div class="tool">ChatGPT</div><div class="verdict">Moderate — conversations are slower for rapid iteration</div><div class="rating r-mid">Moderate</div></div>
            <div class="task-rating"><div class="tool">Claude Code</div><div class="verdict">Moderate — thorough but slower for pure prototyping</div><div class="rating r-mid">Moderate</div></div>
            <div class="task-rating"><div class="tool">Codeium</div><div class="verdict">Moderate — decent completions, less context than Copilot</div><div class="rating r-mid">Moderate</div></div>
          </div>
          <div class="verdict-box">
            <p><strong>Why this matters:</strong> Prototyping is one of the highest-dependency use cases. When AI generates the scaffold, engineers report feeling unable to start projects without it. The prototype you build with AI becomes the foundation you continue from. The fix: prototype manually for 15-30 minutes before reaching for AI.</p>
          </div>
        </div>
      </section>

      <section>
        <div class="use-case">
          <div class="use-case-header">
            <div class="use-case-icon">📝</div>
            <div><h3 style="margin:0">Task 5: Writing Documentation</h3></div>
          </div>
          <p class="task-desc">You need to document an API, write a README, or explain a system. Documentation is important but often deferred.</p>
          <div class="task-ratings">
            <div class="task-rating"><div class="tool">GitHub Copilot</div><div class="verdict">Moderate — inline doc suggestions are generic</div><div class="rating r-mid">Moderate</div></div>
            <div class="task-rating"><div class="tool">Cursor</div><div class="verdict">Moderate — can generate full docs but often generic</div><div class="rating r-mid">Moderate</div></div>
            <div class="task-rating"><div class="tool">ChatGPT</div><div class="verdict">Low fatigue — conversational drafting preserves your voice</div><div class="rating r-high">Best for documentation</div></div>
            <div class="task-rating"><div class="tool">Claude Code</div><div class="verdict">Moderate — good for API docs, less for narrative</div><div class="rating r-mid">Moderate</div></div>
            <div class="task-rating"><div class="tool">Codeium</div><div class="verdict">Low value — minimal documentation support</div><div class="rating r-low">Not suited</div></div>
          </div>
          <div class="verdict-box">
            <p><strong>Why this matters:</strong> Documentation is one of the few AI use cases where the fatigue cost is genuinely low and productivity gain is real. Since you understand the code, AI helps you articulate what you already know. Best practice: let AI draft, then edit with your specific audience in mind. Never ship AI-generated docs without review.</p>
          </div>
        </div>
      </section>

      <section>
        <div class="use-case">
          <div class="use-case-header">
            <div class="use-case-icon">🏗️</div>
            <div><h3 style="margin:0">Task 6: Architecture and System Design</h3></div>
          </div>
          <p class="task-desc">You're designing a service or evaluating architectural decisions. You need reasoning, not code generation.</p>
          <div class="task-ratings">
            <div class="task-rating"><div class="tool">GitHub Copilot</div><div class="verdict">Low value — not designed for architectural reasoning</div><div class="rating r-low">Not suited</div></div>
            <div class="task-rating"><div class="tool">Cursor</div><div class="verdict">Moderate — can generate architecture code</div><div class="rating r-mid">Moderate</div></div>
            <div class="task-rating"><div class="tool">ChatGPT</div><div class="verdict">Low fatigue — excellent for multi-turn architecture reasoning</div><div class="rating r-high">Best for architecture</div></div>
            <div class="task-rating"><div class="tool">Claude Code</div><div class="verdict">Low fatigue — strong analytical reasoning</div><div class="rating r-high">Very good</div></div>
            <div class="task-rating"><div class="tool">Codeium</div><div class="verdict">Low value — no architectural reasoning support</div><div class="rating r-low">Not suited</div></div>
          </div>
          <div class="verdict-box">
            <p><strong>Why this matters:</strong> Architecture is judgment accumulated through experience. AI can summarize patterns and explain tradeoffs — but it cannot replace the judgment that comes from having made architectural mistakes before. Use AI as a thinking partner, not an authority that makes the decision for you.</p>
          </div>
        </div>
      </section>

      <section>
        <div class="use-case">
          <div class="use-case-header">
            <div class="use-case-icon">🧠</div>
            <div><h3 style="margin:0">Task 7: Understanding Unfamiliar Code</h3></div>
          </div>
          <p class="task-desc">You inherited a codebase or are reading a library's source. You need comprehension, fast.</p>
          <div class="task-ratings">
            <div class="task-rating"><div class="tool">GitHub Copilot</div><div class="verdict">Moderate — inline explanations are shallow</div><div class="rating r-mid">Moderate</div></div>
            <div class="task-rating"><div class="tool">Cursor</div><div class="verdict">Moderate — chat mode can explain code sections</div><div class="rating r-mid">Moderate</div></div>
            <div class="task-rating"><div class="tool">ChatGPT</div><div class="verdict">Low fatigue — excellent for deep code explanation</div><div class="rating r-high">Best for exploration</div></div>
            <div class="task-rating"><div class="tool">Claude Code</div><div class="verdict">Low fatigue — reads full files, explains holistically</div><div class="rating r-high">Very good</div></div>
            <div class="task-rating"><div class="tool">Codeium</div><div class="verdict">Moderate — basic hover explanations</div><div class="rating r-mid">Moderate</div></div>
          </div>
          <div class="verdict-box">
            <p><strong>Why this matters:</strong> Understanding unfamiliar code quickly is a legitimate and low-fatigue use case. AI can read a function and explain it in plain language faster than you can trace through it manually. This is the use case where AI genuinely accelerates comprehension without substituting thinking — because you already have the code, you're just trying to understand it.</p>
          </div>
        </div>
      </section>

      <section>
        <div class="use-case">
          <div class="use-case-header">
            <div class="use-case-icon">✅</div>
            <div><h3 style="margin:0">Task 8: Writing Tests</h3></div>
          </div>
          <p class="task-desc">You have working code. You need tests that cover the behavior, not the implementation.</p>
          <div class="task-ratings">
            <div class="task-rating"><div class="tool">GitHub Copilot</div><div class="verdict">Low fatigue — test completions are generally good</div><div class="rating r-high">Well suited</div></div>
            <div class="task-rating"><div class="tool">Cursor</div><div class="verdict">Low fatigue — can generate comprehensive test suites</div><div class="rating r-high">Well suited</div></div>
            <div class="task-rating"><div class="tool">ChatGPT</div><div class="verdict">Low fatigue — good for edge case identification</div><div class="rating r-high">Well suited</div></div>
            <div class="task-rating"><div class="tool">Claude Code</div><div class="verdict">Low fatigue — thorough test generation with reasoning</div><div class="rating r-high">Well suited</div></div>
            <div class="task-rating"><div class="tool">Codeium</div><div class="verdict">Moderate — basic test completions</div><div class="rating r-mid">Moderate</div></div>
          </div>
          <div class="verdict-box">
            <p><strong>Why this matters:</strong> Test writing is one of the few coding tasks where most AI tools perform well with low fatigue cost. Since you understand the code, AI's role is mostly mechanical translation of behavior into test cases. The risk: AI-generated tests can have gaps. Use AI to generate the scaffold, then audit the coverage. Never treat AI-generated test suites as comprehensive without review.</p>
          </div>
        </div>
      </section>

      <section>
        <h2>The Fatigue Comparison Summary</h2>
        <p>At a glance: which tool to reach for for each task, and at what fatigue cost.</p>
        <div class="table-wrap">
          <table class="summary-table">
            <thead><tr><th>Task</th><th>Best Tool</th><th>Fatigue Cost</th><th>Skill Risk</th></tr></thead>
            <tbody>
              <tr><td>Learning a new language</td><td>ChatGPT <span class="best-badge">BEST</span></td><td style="color: var(--green)">Low</td><td>Minimal if tutoring mode</td></tr>
              <tr><td>Debugging</td><td>ChatGPT / Claude Code <span class="best-badge">BEST</span></td><td style="color: var(--green)">Low</td><td>High — auto-fix erodes debugging skill</td></tr>
              <tr><td>Code review</td><td>Claude Code <span class="best-badge">BEST</span></td><td style="color: #f0a500">Moderate</td><td>Low — judgment, not generation</td></tr>
              <tr><td>Prototyping</td><td>Copilot / Cursor <span class="best-badge">BEST</span></td><td style="color: var(--green)">Low upfront</td><td>Very High — highest dependency risk</td></tr>
              <tr><td>Writing documentation</td><td>ChatGPT <span class="best-badge">BEST</span></td><td style="color: var(--green)">Low</td><td>Minimal</td></tr>
              <tr><td>Architecture discussion</td><td>ChatGPT / Claude Code <span class="best-badge">BEST</span></td><td style="color: var(--green)">Low</td><td>Minimal — AI as thinking partner</td></tr>
              <tr><td>Understanding unfamiliar code</td><td>ChatGPT <span class="best-badge">BEST</span></td><td style="color: var(--green)">Low</td><td>Minimal — comprehension aid</td></tr>
              <tr><td>Writing tests</td><td>All tools <span class="best-badge">BEST</span></td><td style="color: var(--green)">Low</td><td>Low — mechanical translation</td></tr>
            </tbody>
          </table>
        </div>
        <div class="insight-box">
          <strong>The pattern:</strong> Tasks where AI generates new code carry the highest fatigue and skill-erosion cost. Tasks where AI explains, teaches, or reviews existing code carry the lowest cost. The safest rule: reach for AI when you already understand the problem deeply and need translation — not when you're still building that understanding.
        </div>
      </section>

      <section>
        <h2>The Three Rules for Using AI Coding Tools Without the Fatigue</h2>
        <h3>Rule 1: Always use the Explanation Requirement</h3>
        <p>Before accepting any AI code suggestion, say out loud why the suggestion makes sense. Not what the code does — why it's right for this specific context. If you can't explain why it's right, don't accept it yet. This single practice eliminates passive acceptance and transforms AI from a crutch into a second opinion.</p>
        <h3>Rule 2: Never let AI start a project you couldn't start yourself</h3>
        <p>If you can't begin a project without AI generating the scaffold, you're dependent. The test: close the AI tool and try to start. If you can't, you've found a dependency. Rebuild that initiation skill deliberately — start projects manually for the first 15-30 minutes before reaching for AI.</p>
        <h3>Rule 3: Use AI to explain more than to generate</h3>
        <p>The lowest-fatigue use cases — code explanation, architecture discussion, debugging with tutoring — share a common thread: AI is teaching you, not replacing your thinking. Shift your default from "write this for me" to "explain this to me." The skill you preserve is worth far more than the time you save.</p>
      </section>

      <section>
        <h2>Frequently Asked Questions</h2>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq-1">Which AI coding tool causes the least fatigue overall?<span class="icon">+</span></button>
          <div class="faq-answer" id="faq-1" aria-hidden="true"><p>ChatGPT and Claude Code cause the least fatigue overall because they're conversational — you maintain agency. Tab-completion tools like Copilot are lower-effort in the moment but higher-cost over time because they suppress active thinking. The tool that causes the least fatigue is the one that makes you continue thinking, not the one that makes thinking unnecessary.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq-2">Is it okay to use Copilot for debugging?<span class="icon">+</span></button>
          <div class="faq-answer" id="faq-2" aria-hidden="true"><p>Only if you use it correctly. The wrong way: paste an error message and accept the auto-fix without understanding why. The right way: describe the bug in your own words, reason through possible causes yourself, then use AI to confirm your hypothesis. Copilot's auto-fix feature is the highest-risk debugging pattern — it applies the fix before you've diagnosed the problem.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq-3">Should junior engineers avoid AI coding tools entirely?<span class="icon">+</span></button>
          <div class="faq-answer" id="faq-3" aria-hidden="true"><p>Not entirely. The right approach is selective use with deliberate practice. Juniors should use AI for code explanation and exploration (low skill risk, high learning value) and avoid AI for tasks they're still learning. The goal: use AI to accelerate learning without replacing the practice that builds expertise.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq-4">What's the highest-risk AI coding use case for skill atrophy?<span class="icon">+</span></button>
          <div class="faq-answer" id="faq-4" aria-hidden="true"><p>Prototyping. When AI generates the scaffold for a project, engineers form an immediate dependency — they can't start projects without it. The combination of high initial speed and high long-term dependency makes prototyping the most corrosive use case. The solution: always start projects manually for 15-30 minutes before reaching for AI.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq-5">Can I use multiple AI tools simultaneously?<span class="icon">+</span></button>
          <div class="faq-answer" id="faq-5" aria-hidden="true"><p>You can, but be aware of the cognitive cost. Processing two AI outputs in parallel requires evaluating, accepting or rejecting, and integrating each into your mental model. One tool at a time, for a specific purpose, is better than two simultaneously for vague purposes.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq-6">How do I know if I've already lost skills from AI use?<span class="icon">+</span></button>
          <div class="faq-answer" id="faq-6" aria-hidden="true"><p>Three diagnostic questions: (1) Can you start a project without AI generating the first chunk of code? (2) When you see a bug, do you have a hypothesis before reaching for AI? (3) Can you explain your current project's code without AI summarizing it? If you answered no to two or more, skill atrophy is likely. The <a href="ai-detox-plan.html" style="color: var(--green)">30-day AI detox plan</a> is designed to recover these skills.</p></div>
        </div>
      </section>

      <section>
        <h2>Continue Exploring</h2>
        <div class="explore-grid">
          <a href="compare.html" class="explore-card"><div class="card-label">Tool Comparison</div><h4>AI Tools Fatigue Comparison</h4><p>Full breakdown of Copilot vs Cursor vs ChatGPT vs Codeium on skill erosion and cognitive load.</p></a>
          <a href="skill-atrophy.html" class="explore-card"><div class="card-label">Skill Atrophy</div><h4>The Slow Erosion of Coding Skills</h4><p>Research-backed explanation of how AI tools erode specific coding skills over time.</p></a>
          <a href="debugger-drift.html" class="explore-card"><div class="card-label">Debugging</div><h4>Debugging Drift</h4><p>Why AI is making engineers worse at finding bugs — and what to do about it.</p></a>
          <a href="mindset.html" class="explore-card"><div class="card-label">Mental Models</div><h4>12 Frameworks for Healthy AI Use</h4><p>The Explanation Requirement and 11 other mental models for using AI without losing yourself.</p></a>
          <a href="ai-detox-plan.html" class="explore-card"><div class="card-label">Recovery</div><h4>30-Day AI Detox Plan</h4><p>A structured recovery plan for engineers who want to recalibrate their AI relationship.</p></a>
          <a href="cognitive-load.html" class="explore-card"><div class="card-label">Cognitive Science</div><h4>Cognitive Load Theory</h4><p>Why AI is drowning your brain — and research-backed strategies for managing it.</p></a>
        </div>
      </section>

    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-brand">
        <a href="index.html" class="footer-logo">
          <svg width="18" height="18" viewBox="0 0 20 20" fill="none" aria-hidden="true"><circle cx="10" cy="10" r="8" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M10 6C10 6 7 9 7 11C7 13 8.5 14 10 14C11.5 14 13 13 13 11C13 9 10 6 10 6Z" fill="currentColor" opacity="0.6"/><path d="M10 14V16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
          The Clearing
        </a>
        <p>A resource for engineers navigating AI without losing themselves in the process.</p>
      </div>
      <div class="footer-links">
        <div class="footer-col"><h5>Recover</h5><a href="recovery.html">Recovery Guide</a><a href="ai-detox-plan.html">30-Day AI Detox</a><a href="ai-fatigue-checklist.html">Recovery Checklist</a><a href="mental-health.html">Mental Health</a><a href="developer-wellbeing.html">Wellbeing</a></div>
        <div class="footer-col"><h5>Understand</h5><a href="why.html">Why This Happens</a><a href="signs-ai-fatigue.html">Warning Signs</a><a href="compare.html">Tool Comparison</a><a href="coding-ai-tools-comparison.html">Use-Case Comparison</a><a href="mindset.html">Mental Models</a><a href="skill-atrophy.html">Skill Atrophy</a></div>
        <div class="footer-col"><h5>Stories</h5><a href="stories.html">Engineer Stories</a><a href="senior-identity.html">Senior Identity</a><a href="junior-engineers.html">For Juniors</a><a href="testimonials.html">Recovery Stories</a></div>
        <div class="footer-col"><h5>Tools and Research</h5><a href="decompress.html">Deep Work Timer</a><a href="journal.html">Reflection Journal</a><a href="research.html">Science</a><a href="ai-fatigue-statistics-2025.html">Statistics</a><a href="resources.html">Resources</a></div>
      </div>
      <div class="footer-bottom"><p>© 2026 The Clearing · <a href="about.html">About</a> · <a href="privacy.html">Privacy</a> · <a href="about.html#contact">Contact</a></p></div>
    </div>
  </footer>

  <script src="main.js" defer></script>
  <script>
    window.addEventListener('scroll', function() {
      var el = document.getElementById('reading-progress');
      if (el) {
        var scrollTop = window.scrollY;
        var docHeight = document.documentElement.scrollHeight - window.innerHeight;
        el.style.width = (scrollTop / docHeight * 100) + '%';
      }
    }, { passive: true });

    document.querySelectorAll('.faq-question').forEach(function(btn) {
      btn.addEventListener('click', function() {
        var expanded = btn.getAttribute('aria-expanded') === 'true';
        document.querySelectorAll('.faq-question').forEach(function(b) {
          b.setAttribute('aria-expanded', 'false');
          b.nextElementSibling.setAttribute('aria-hidden', 'true');
        });
        if (!expanded) {
          btn.setAttribute('aria-expanded', 'true');
          btn.nextElementSibling.setAttribute('aria-hidden', 'false');
        }
      });
    });
  </script>
</body>
</html>
"""

lines.append(remaining)
with open(path, 'w') as f:
    f.writelines(lines)

print(f"Done. File now has {len(lines)} lines")
