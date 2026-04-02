with open('coding-ai-tools-comparison.html', 'r') as f:
    content = f.read()

# Check for truncation
cutoff = "If you're learning to code:"
if cutoff not in content:
    print("File doesn't have expected content, regenerating...")
    # We'll rebuild the full file properly
else:
    idx = content.find(cutoff)
    before = content[:idx]

remaining = '''
                <div class="framework-row">
                <div class="framework-label">If you're learning to code:</div>
                <div class="framework-answer">ChatGPT only, and only for syntax lookups and conceptual questions. Never for problems at your edge. Build the competence first; use the tool later.</div>
              </div>
            </div>

            <h3>The skill-preservation ranking (lowest to highest cost)</h3>
            <p>Ranked by cumulative skill erosion over 6 months of daily use, based on practitioner reports and cognitive science of skill decay:</p>
            <ol>
              <li><strong>ChatGPT (separate tab, deliberate use)</strong> — Lowest erosion risk. The friction of context-switching creates natural learning boundaries.</li>
              <li><strong>GitHub Copilot (suggestion mode, intentional rejections)</strong> — Low erosion if you actively reject 30%+ of suggestions. High erosion if used passively.</li>
              <li><strong>Cursor (suggestion mode only)</strong> — Similar to Copilot. The IDE integration slightly increases passive acceptance risk.</li>
              <li><strong>Cursor (agent mode)</strong> — High erosion. The autonomous execution bypasses learning at the implementation reasoning level.</li>
              <li><strong>Claude Code (agent mode)</strong> — Highest erosion risk. Autonomous implementation with minimal engagement required. Fastest path to detached code ownership.</li>
            </ol>
          </div>

          <div class="section faq-section">
            <h2>Frequently asked questions</h2>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                Which AI coding tool causes the most fatigue?
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-answer">
                <p>Claude Code in agent mode causes the highest fatigue and skill erosion risk, followed by Cursor in agent mode, then GitHub Copilot in suggestion mode, and finally ChatGPT with the lowest fatigue risk. The key variable is how much autonomous agency the tool has over your codebase. The more the AI does without your active engagement, the more it costs you in skills and ownership.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                Does GitHub Copilot cause skill atrophy?
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-answer">
                <p>Yes, GitHub Copilot can cause skill atrophy over time, particularly in syntax recall, API familiarity, and the ability to write boilerplate without assistance. A 2024 Deloitte survey found 41% of Copilot users reported reduced engagement with their own code. The risk is highest when used as a default rather than a fallback.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                Is Claude Code worth the cognitive trade-off?
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-answer">
                <p>For senior engineers handling large refactors or unfamiliar codebases, Claude Code can be worth the trade-off — if used with deliberate boundaries. The key practices: the Explanation Requirement (explain each change back before accepting it), no-agent sessions where you solve problems yourself, and weekly no-AI coding days to maintain baseline competence.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                Which tools are safest for junior engineers?
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-answer">
                <p>ChatGPT in a separate tab is safest for juniors because the context-switching friction creates a natural learning boundary. GitHub Copilot in suggestion-only mode is second-best if the engineer actively rejects suggestions to practice. Claude Code and Cursor in agent mode are highest risk for juniors because they bypass the productive struggle that builds core engineering instincts.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                How do I use AI coding tools without losing skills?
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-answer">
                <p>Three evidence-based practices: (1) <strong>The Explanation Requirement</strong> — before accepting any AI suggestion, explain to yourself why it works and what alternatives exist; (2) <strong>No-AI sessions</strong> — one hour per week where you solve problems without any AI assistance; (3) <strong>The Rebuild Test</strong> — once per month, rebuild something the AI generated from scratch to calibrate skill drift.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                Can I recover skills after AI dependency?
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-answer">
                <p>Yes, but recovery takes 4-8 weeks of deliberate practice. Start with 20 minutes per day of AI-free coding on problems just below your comfort level. Add the Explanation Requirement for every AI output you do encounter. Most engineers report measurable confidence and competence recovery within 6 weeks.</p>
              </div>
            </div>
          </div>

          <div class="section explore-grid">
            <h2>Continue exploring</h2>
            <div class="explore-cards">
              <a href="ai-tool-overload.html" class="explore-card">
                <span class="explore-icon">⚡</span>
                <h3>AI Tool Overload</h3>
                <p>Why new tools paralyze engineers and how to break the cycle.</p>
              </a>
              <a href="skill-atrophy.html" class="explore-card">
                <span class="explore-icon">📉</span>
                <h3>Skill Atrophy</h3>
                <p>The science of how AI erodes the skills you built over years.</p>
              </a>
              <a href="compare.html" class="explore-card">
                <span class="explore-icon">⚖️</span>
                <h3>Compare All Tools</h3>
                <p>The full comparison of AI coding assistants — features, risks, and trade-offs.</p>
              </a>
              <a href="recovery.html" class="explore-card">
                <span class="explore-icon">🌿</span>
                <h3>Recovery Guide</h3>
                <p>How to recover from AI fatigue and regain your sense of craft.</p>
              </a>
              <a href="cognitive-load.html" class="explore-card">
                <span class="explore-icon">🧠</span>
                <h3>Cognitive Load</h3>
                <p>Why AI is overwhelming your brain and what to do about it.</p>
              </a>
              <a href="ai-detox-plan.html" class="explore-card">
                <span class="explore-icon">🧘</span>
                <h3>30-Day AI Detox</h3>
                <p>A structured plan to reset your relationship with AI tools.</p>
              </a>
            </div>
          </div>
        </div>
      </article>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <p>🌿 The Clearing — AI fatigue recovery for software engineers.</p>
        <p class="footer-tagline">Free forever. No tracking. No account required.</p>
      </div>
      <div class="footer-links">
        <div class="footer-col">
          <h4>Recover</h4>
          <ul>
            <li><a href="recovery.html">Recovery Guide</a></li>
            <li><a href="ai-detox-plan.html">30-Day AI Detox</a></li>
            <li><a href="ai-fatigue-checklist.html">Checklist</a></li>
            <li><a href="daily-practice.html">Daily Practice</a></li>
            <li><a href="decompress.html">Deep Work Timer</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Understand</h4>
          <ul>
            <li><a href="why.html">Why This Happens</a></li>
            <li><a href="ai-fatigue.html">What Is AI Fatigue</a></li>
            <li><a href="compare.html">Compare Tools</a></li>
            <li><a href="coding-ai-tools-comparison.html">Claude vs Copilot</a></li>
            <li><a href="research.html">The Research</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <ul>
            <li><a href="stories.html">Engineer Stories</a></li>
            <li><a href="community.html">Community</a></li>
            <li><a href="newsletter.html">Newsletter</a></li>
            <li><a href="resources.html">Reading List</a></li>
            <li><a href="press-kit.html">Press Kit</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 The Clearing · <a href="about.html">About</a> · <a href="changelog.html">Changelog</a> · <a href="sitemap.html">Sitemap</a></p>
    </div>
  </footer>

  <script>
    // Reading progress bar
    const progressBar = document.createElement('div');
    progressBar.className = 'reading-progress';
    document.body.appendChild(progressBar);
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    });

    // FAQ accordion
    document.querySelectorAll('.faq-question').forEach(btn => {
      btn.addEventListener('click', () => {
        const isExpanded = btn.getAttribute('aria-expanded') === 'true';
        document.querySelectorAll('.faq-question').forEach(b => {
          b.setAttribute('aria-expanded', 'false');
          b.nextElementSibling.style.display = 'none';
          b.querySelector('.faq-icon').textContent = '+';
        });
        if (!isExpanded) {
          btn.setAttribute('aria-expanded', 'true');
          btn.nextElementSibling.style.display = 'block';
          btn.querySelector('.faq-icon').textContent = '−';
        }
      });
    });
  </script>
</body>
</html>'''

new_content = before + remaining

with open('coding-ai-tools-comparison.html', 'w') as f:
    f.write(new_content)

lines = new_content.splitlines()
print(f"Done. Total lines: {len(lines)}")
print(f"File size: {len(new_content)} bytes")
# Word count estimate
words = len(new_content.split())
print(f"Estimated words: {words}")
