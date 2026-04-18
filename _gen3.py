#!/usr/bin/env python3
"""Generator for testimonials-campaign.html - Part 3 (submit + JS + footer)"""

BASE = "/Users/nightcoder/Desktop/TheClearing/testimonials-campaign.html"

with open(BASE, "a", encoding="utf-8") as f:
    # Submit section
    f.write('<hr class="divider"/>\n')
    f.write('<section class="section" id="submit" aria-labelledby="submit-title">\n')
    f.write('<h2 id="submit-title">Share Your Story</h2>\n')
    f.write('<p class="section-intro">Your recovery story is someone else\'s proof they\'re not broken. Every story submitted (with your permission) gets added to this page to help engineers who are still struggling feel less alone.</p>\n')
    f.write('<div class="incentive-box">\n')
    f.write("<h3>Why share your story?</h3>\n")
    f.write("<p>Most engineers who reach out to us say the same thing: they thought they were the only one. Your story -- even a few sentences -- can change that for someone. It takes 5 minutes to write, and we make it completely anonymous.</p>\n")
    f.write("</div>\n")
    f.write('<div class="form-section">\n')
    f.write('<form id="story-form" action="mailto:hello@clearing-ai.com" method="POST" enctype="text/plain" onsubmit="return handleSubmit(event)">\n')
    f.write('<div class="form-grid">\n')
    f.write('<div class="form-field"><label for="submit-name">Your name or anonymous</label><input type="text" id="submit-name" name="name" placeholder="Anonymous" required/></div>\n')
    f.write('<div class="form-field"><label for="submit-email">Your email (private, never shared)</label><input type="email" id="submit-email" name="email" placeholder="you@example.com"/></div>\n')
    f.write('<div class="form-field"><label for="submit-role">Your role</label><input type="text" id="submit-role" name="role" placeholder="Senior Engineer, Engineering Manager, etc." required/></div>\n')
    f.write('<div class="form-field"><label for="submit-tier">How would you rate your AI fatigue?</label><select id="submit-tier" name="tier"><option value="">Select a tier (optional)</option><option value="Tier 1 - Mild">Tier 1 - Mild (occasional tiredness)</option><option value="Tier 2 - Some Fatigue">Tier 2 - Some Fatigue</option><option value="Tier 3 - Real Fatigue">Tier 3 - Real Fatigue</option><option value="Tier 4 - Severe">Tier 4 - Severe / Burnout</option></select></div>\n')
    f.write("</div>\n")
    f.write('<div class="form-field full"><label for="submit-situation">What was your situation? How did AI fatigue show up for you?</label><textarea id="submit-situation" name="situation" placeholder="What were you experiencing? What was the situation at work?" required></textarea></div>\n')
    f.write('<div class="form-field full"><label for="submit-helped">What helped you recover? (If applicable)</label><textarea id="submit-helped" name="helped" placeholder="What strategies, changes, or realizations helped you? (Optional)"></textarea></div>\n')
    f.write('<div class="form-field full"><label for="submit-share">Anything else you want to share?</label><textarea id="submit-share" name="share" placeholder="Any other thoughts or experiences you want to share."></textarea></div>\n')
    f.write('<button type="submit" class="btn-submit">Submit My Story</button>\n')
    f.write('<p class="form-note">Your story will be reviewed and may be added to this page (with your permission). We remove all identifying details.</p>\n')
    f.write("</form>\n")
    f.write('<div class="success-msg" id="success-state">\n')
    f.write("<p>Thank you for sharing your story!</p>\n")
    f.write("<span>Your submission has been sent. If you'd like to share more or follow up, email us at hello@clearing-ai.com.</span>\n")
    f.write("</div>\n")
    f.write("</div>\n")
    f.write("</section>\n")
    f.write("</div>\n")  # close content-wrap

    # Main JS
    f.write('<script>\n')
    f.write("""
(function() {
  // Reading progress bar
  var progress = document.getElementById('progress');
  function updateProgress() {
    var scrollTop = window.scrollY;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    var pct = docHeight > 0 ? Math.round((scrollTop / docHeight) * 100) : 0;
    progress.style.width = pct + '%';
    progress.setAttribute('aria-valuenow', pct);
  }
  window.addEventListener('scroll', updateProgress, { passive: true });

  // Theme toggle
  var toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function() {
      var html = document.documentElement;
      var current = html.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      toggle.textContent = next === 'dark' ? '🌙' : '☀️';
    });
    // Restore saved theme
    var saved = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', saved);
    toggle.textContent = saved === 'dark' ? '🌙' : '☀️';
  }

  // Copy link
  window.copyLink = function() {
    navigator.clipboard.writeText('https://clearing-ai.com/testimonials-campaign.html').then(function() {
      var btn = document.getElementById('copy-link-btn');
      if (btn) { btn.textContent = 'Copied!'; setTimeout(function() { btn.textContent = 'Copy Link'; }, 2000); }
    });
  };

  // Share story (Twitter/LinkedIn)
  window.shareStory = function(platform, role, quote) {
    var text = quote + ' -- ' + role + ', via The Clearing: https://clearing-ai.com/testimonials-campaign.html';
    if (platform === 'twitter') {
      window.open('https://twitter.com/intent/tweet?text=' + encodeURIComponent(text), '_blank', 'noopener');
    } else if (platform === 'linkedin') {
      window.open('https://www.linkedin.com/shareArticle?mini=true&url=' + encodeURIComponent('https://clearing-ai.com/testimonials-campaign.html') + '&title=' + encodeURIComponent(quote) + '&summary=' + encodeURIComponent(role), '_blank', 'noopener');
    }
  };

  // Copy pre-written share text
  window.copyShareText = function(platform) {
    var texts = {
      twitter: "I just read 10 real engineers' AI fatigue recovery stories. If you've felt the same, you're not alone. https://clearing-ai.com/testimonials-campaign.html",
      linkedin: "10 engineers shared their AI fatigue recovery stories on The Clearing. If you've been feeling behind, overwhelmed, or like you're not keeping up -- you're not lazy. You're experiencing something real. https://clearing-ai.com/testimonials-campaign.html",
      hn: "I came across The Clearing's AI Fatigue Quiz and was surprised how accurately it named something I've been feeling. 10 engineers share their stories. https://clearing-ai.com/testimonials-campaign.html"
    };
    var t = texts[platform] || '';
    navigator.clipboard.writeText(t).then(function() {
      // Visual feedback handled by click event
    });
  };

  // Copy email template
  var templateBodies = {
    A: "Hey [Name],\\n\\nI wanted to check in with you directly. You have seemed a bit off lately -- not yourself in meetings, less engaged than usual, or maybe just more tired than usual. I am not saying anything is wrong, but I noticed and I care.\\n\\nI came across something last week that might speak to what you are going through: The Clearing (clearing-ai.com). It is a free resource for engineers dealing with AI fatigue -- the sense that everything is moving too fast, that you cannot keep up, that you are falling behind no matter how hard you try.\\n\\nI found it useful. Thought you might too. No pressure to look at it -- just wanted you to know you are not alone if that is where you are right now.\\n\\nLet me know if you want to talk about it -- or anything else.\\n\\n[Your name]",
    B: "Hi [Name],\\n\\nI want to check in with you about something that is not in any performance review: how you are actually doing with the pace of things right now.\\n\\nNo agenda here. I just know that a lot of engineers are dealing with something the industry is calling AI fatigue -- the feeling that you are always behind, always catching up, always learning new tools without feeling like you are getting better at the things that matter.\\n\\nIf that resonates, The Clearing (clearing-ai.com) has some useful framing and a short quiz that might help you name what you are feeling.\\n\\nIf not, no worries at all. Just wanted you to know the door is open if you want to talk.\\n\\n[Your name]",
    C: "Hey [Name],\\n\\nRemember when you mentioned [specific thing they said about AI tools / feeling behind / being tired of learning new things]? I thought about that.\\n\\nI found something that might help you name what you were describing: The Clearing has an AI Fatigue Quiz (clearing-ai.com/quiz.html) that you might find surprisingly accurate.\\n\\nIt is free, takes 2 minutes, and the person who showed it to me said it helped them realize they were not just lazy or bad at their job -- they were experiencing something with a name and a path forward.\\n\\nWanted to pass it along.\\n\\n[Your name]",
    D: "I have been reading real engineer stories about AI fatigue on The Clearing (clearing-ai.com) -- people describing something that is not burnout exactly, but feels like the ground moving under your feet.\\n\\nOne quote that stuck with me: 'I could see it happening and I did not have the language for it.'\\n\\nIf you have been feeling the same way, you are not alone. The site has a free 5-question quiz that helps you name what you are experiencing and points toward what actually helps.\\n\\nWorth 2 minutes if any of this lands: clearing-ai.com"
  };

  window.copyTemplate = function(btn, type) {
    var body = templateBodies[type] || '';
    var subject = '';
    if (type === 'A') subject = 'Subject: Something I wanted to check in about';
    else if (type === 'B') subject = 'Subject: How are you doing, really?';
    else if (type === 'C') subject = 'Subject: That thing you mentioned about AI tools';
    else if (type === 'D') subject = 'Subject: [Shareable text for public post]';
    navigator.clipboard.writeText(subject + '\\n\\n' + body).then(function() {
      var orig = btn.textContent;
      btn.textContent = 'Copied!';
      btn.classList.add('copied');
      setTimeout(function() {
        btn.textContent = orig;
        btn.classList.remove('copied');
      }, 2000);
    });
  };

  // Form submission
  window.handleSubmit = function(e) {
    e.preventDefault();
    var form = document.getElementById('story-form');
    var success = document.getElementById('success-state');
    if (form && success) {
      form.style.display = 'none';
      success.classList.add('show');
      success.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    // Also open mailto as fallback
    var name = document.getElementById('submit-name');
    var email = document.getElementById('submit-email');
    var role = document.getElementById('submit-role');
    var tier = document.getElementById('submit-tier');
    var situation = document.getElementById('submit-situation');
    var helped = document.getElementById('submit-helped');
    var share = document.getElementById('submit-share');
    var body = 'Story Submission\\n\\n';
    body += 'Name: ' + (name ? name.value : '') + '\\n';
    body += 'Email: ' + (email ? email.value : '') + '\\n';
    body += 'Role: ' + (role ? role.value : '') + '\\n';
    body += 'Tier: ' + (tier ? tier.value : '') + '\\n\\n';
    body += 'Situation:\\n' + (situation ? situation.value : '') + '\\n\\n';
    body += 'What helped:\\n' + (helped ? helped.value : '') + '\\n\\n';
    body += 'Additional thoughts:\\n' + (share ? share.value : '');
    var mailto = 'mailto:hello@clearing-ai.com?subject=AI Fatigue Story Submission&body=' + encodeURIComponent(body);
    window.location.href = mailto;
    return false;
  };
})();
""")
    f.write("</script>\n")

    # Footer
    f.write("</main>\n")
    f.write("<footer>\n")
    f.write("<p>&copy; 2026 The Clearing. An independent resource for engineers navigating AI fatigue.</p>\n")
    f.write("<div class=\"footer-links\">\n")
    f.write('<a href="/">Home</a><a href="/quiz.html">Quiz</a><a href="/recovery.html">Recovery</a><a href="/testimonials.html">Testimonials</a><a href="/community.html">Community</a><a href="/newsletter.html">Newsletter</a>\n")
    f.write("</div>\n")
    f.write("</footer>\n")
    f.write("</body>\n")
    f.write("</html>\n")

print("Part 3 written OK")
