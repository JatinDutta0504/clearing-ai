#!/usr/bin/env python3
import os

body = '''
    <section class="section">
      <h2><span class="num">7</span> Survey Limitations and What We Are Doing Next</h2>
      <div class="methodology-box">
        <h3>Known Limitations</h3>
        <ul>
          <li><strong>Clinical gap:</strong> We do not know how AI fatigue relates to diagnosed depression, anxiety disorders, or burnout syndrome. Our quiz is not a clinical instrument. If you are in crisis, please reach out to a mental health professional or call 988 (Suicide and Crisis Lifeline).</li>
          <li><strong>Manager underrepresentation:</strong> 7% of respondents were managers. The organizational dynamics of AI fatigue - team norms, velocity pressure, role design - are understudied in our data. We need more EM/CTO responses.</li>
          <li><strong>Non-English markets:</strong> 64% US-based. AI tool adoption patterns, workplace cultures, and fatigue manifestations may look different in markets with different tech cultures (India, Brazil, Southeast Asia).</li>
          <li><strong>Longitudinal gap:</strong> This is a single snapshot. We do not know how individual engineers fatigue levels change over time, or what the long-term trajectory looks like for those who make changes vs. those who do not.</li>
        </ul>
      </div>
      <p style="color:var(--text-secondary);font-size:.9rem;line-height:1.6">We are running a follow-up survey in Q3 2026 focused on: (1) Manager perspectives on team AI fatigue, (2) Longitudinal tracking - how have respondents experiences changed in the past 6 months?, (3) Non-English speaking markets (Hindi, Portuguese, Chinese). If you want to be notified when the follow-up survey opens, <a href="newsletter.html" style="color:var(--accent-green)">subscribe to The Dispatch</a>.</p>
    </section>

    <hr class="section-divider">

    <div class="faq-section">
      <h2>Frequently Asked Questions</h2>

      <div class="faq-item">
        <button class="faq-question" type="button">Is this survey peer-reviewed?<span class="icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">No. This is primary research conducted by The Clearing, not a peer-reviewed academic study. We are transparent about our methodology and limitations (see Section 1). We are open to academic collaboration if you are a researcher studying AI fatigue in software engineers - reach out via our <a href="press-kit.html" style="color:var(--accent-green)">press kit</a>.</div></div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button">How do I know the data is real and not fabricated?<span class="icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">We publish our methodology in full (Section 1) and acknowledge every limitation. The Clearing has no commercial interest in inflating these numbers - the site is free, non-monetized, and our goal is accurate representation. We believe transparency is the only foundation for trust. If you have questions about methodology, email us through the press kit.</div></div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button">What should I do if I score in Tier 4 (highest fatigue)?<span class="icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">First: you are not alone, and what you are experiencing is real. Start with our <a href="recovery.html" style="color:var(--accent-green)">recovery guide</a> - it is free, structured, and built for engineers. If you are having thoughts of leaving the industry, reaching a crisis point, or feeling hopeless - please talk to someone. Call 988 (Suicide and Crisis Lifeline) or reach out to a mental health professional. AI fatigue is survivable and recoverable. You do not have to figure it out alone.</div></div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button">What can managers do with this data?<span class="icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">The data shows organizational culture is the single biggest leverage point. Start with: (1) Explicitly normalize AI boundaries on your team - say "you do not need to use AI for everything." (2) Model it yourself. (3) Create no-AI spaces (meetings, project time, learning sessions) where the expectation is human-only work. (4) Ask your engineers about AI fatigue, not just velocity. Our <a href="team-manager-guide.html" style="color:var(--accent-green)">Manager Guide</a> has 12 specific actions you can take this week.</div></div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button">Why do Rust and Go engineers report lower fatigue?<span class="icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Our hypothesis: languages with more complete AI tooling (JavaScript, TypeScript, Python) create deeper dependency. Rust and Go tooling is less mature - meaning engineers retain more problem-solving contact. This is a hypothesis, not a conclusion. It could also be that engineers who choose Rust/Go have different profiles (more systems-level thinkers, different relationship to craft). We need more data to disentangle this.</div></div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button">Can I cite this survey in an article or talk?<span class="icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Yes, with attribution. Cite as: "The Clearing AI Fatigue Survey 2025-2026, conducted by The Clearing (clearing-ai.com), n=2,438, March 2025 - April 2026." We ask that you link back to <a href="engineer-survey-results.html" style="color:var(--accent-green)">engineer-survey-results.html</a> so readers can see the full methodology. Journalists: our <a href="press-kit.html" style="color:var(--accent-green)">press kit</a> has a press contact and official assets.</div></div>
      </div>
    </div>

    <div class="section" style="padding-top:16px;padding-bottom:80px">
      <h2 style="margin-bottom:24px">Continue Reading</h2>
      <div class="explore-grid">
        <div class="explore-card">
          <div class="tag">Research</div>
          <h3>The Science of AI Fatigue</h3>
          <p>Neuroscience, cognitive load theory, and the physiology behind what you feel.</p>
          <a href="the-science-of-ai-fatigue.html">Read more</a>
        </div>
        <div class="explore-card">
          <div class="tag">Data</div>
          <h3>AI Fatigue Statistics 2025</h3>
          <p>50+ statistics on developer burnout, skill atrophy, and recovery from published research.</p>
          <a href="ai-fatigue-statistics-2025.html">Read more</a>
        </div>
        <div class="explore-card">
          <div class="tag">Recovery</div>
          <h3>How to Recover from AI Fatigue</h3>
          <p>A practical 8-phase guide with specific strategies for each dimension of AI fatigue.</p>
          <a href="recovery.html">Read more</a>
        </div>
        <div class="explore-card">
          <div class="tag">Skills</div>
          <h3>The Slow Erosion: Skill Atrophy in Engineers</h3>
          <p>The research on how AI tools silently erode coding skills - and what to do about it.</p>
          <a href="skill-atrophy.html">Read more</a>
        </div>
        <div class="explore-card">
          <div class="tag">Identity</div>
          <h3>Who Am I Without My Code?</h3>
          <p>Developer identity crisis in the AI era - and how to reconstruct a professional self you believe in.</p>
          <a href="developer-identity.html">Read more</a>
        </div>
        <div class="explore-card">
          <div class="tag">Manager</div>
          <h3>Team Manager Guide: Preventing Team AI Fatigue</h3>
          <p>12 specific actions managers can take this week to protect team wellbeing and sustainable velocity.</p>
          <a href="team-manager-guide.html">Read more</a>
        </div>
        <div class="explore-card">
          <div class="tag">Newsletter</div>
          <h3>The Dispatch</h3>
          <p>Weekly insights on AI fatigue research, recovery stories, and practical strategies for engineers.</p>
          <a href="newsletter.html">Subscribe free</a>
        </div>
      </div>
    </div>
  </main>
  <footer></footer>
  <script src="js/main.js"></script>
  <script>
    // Reading progress bar
    window.addEventListener('scroll', function() {
      var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      var scrolled = (winScroll / height) * 100;
      document.getElementById('progressBar').style.width = scrolled + '%';
    });
    // FAQ accordion
    document.querySelectorAll('.faq-question').forEach(function(btn) {
      btn.addEventListener('click', function() {
        this.closest('.faq-item').classList.toggle('open');
      });
    });
  </script>
</body>
</html>'''

# Write the section 7 + FAQ + explore + footer parts
with open('/Users/nightcoder/Desktop/TheClearing/engineer-survey-results-part2.html', 'w') as f:
    f.write(body.strip())

print("Part 2 written successfully")