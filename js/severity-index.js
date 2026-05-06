// AI Fatigue Severity Index — Interactive Diagnostic Tool
// The Clearing — clearing-ai.com

(function() {
  'use strict';

  // ─── State ────────────────────────────────────────────────────────────────
  var currentAxis = 0;
  var answers = {};  // { axisId: score }
  var axisScores = {};  // { axisId: [score, maxScore] }

  var AXES = [
    {
      id: 'cognitive',
      name: 'Cognitive Load',
      icon: '🧠',
      description: 'How overwhelmed your working memory is by constant AI context-switching',
      color: '#c07050',
      maxScore: 12,
      questions: [
        {
          text: 'At the end of a typical workday using AI tools, how clear is your thinking about what you actually built?',
          options: [
            { label: 'Crystal clear — I understand every piece', value: 0 },
            { label: 'Mostly clear, with a few fuzzy areas', value: 1 },
            { label: 'Vague — I know it works but couldn\'t explain it precisely', value: 2 },
            { label: 'Completely fuzzy — it runs but I don\'t fully understand it', value: 3 }
          ]
        },
        {
          text: 'How many AI tools or AI-assisted workflows do you use in a typical workday?',
          options: [
            { label: '1–2 focused tools', value: 0 },
            { label: '3–4 tools across different contexts', value: 1 },
            { label: '5–7 tools, often simultaneously', value: 2 },
            { label: '8+ tools, juggling constantly', value: 3 }
          ]
        },
        {
          text: 'When you\'re in a flow state of deep work and an AI suggestion comes in, what happens?',
          options: [
            { label: 'I ignore it until my natural break point', value: 0 },
            { label: 'I glance at it briefly, then return to focus', value: 1 },
            { label: 'I check it and often follow up — losing my place', value: 2 },
            { label: 'I immediately engage and lose 10–20 minutes of focus', value: 3 }
          ]
        },
        {
          text: 'How would you rate the overall complexity of what you\'re managing cognitively at work right now?',
          options: [
            { label: 'Manageable — I can hold the whole system in my head', value: 0 },
            { label: 'Moderate — I rely on docs and notes more than before', value: 1 },
            { label: 'High — I feel like I\'m constantly context-switching', value: 2 },
            { label: 'Overwhelming — I can\'t see the whole picture anymore', value: 3 }
          ]
        }
      ],
      findings: [
        { threshold: 1, cls: 'find-low', label: 'Cognitive load is well-managed.', desc: 'You\'re protecting your working memory effectively. Keep monitoring — it\'s easy to drift into overload gradually.', link: 'cognitive-load.html', linkText: 'Learn about cognitive load theory →' },
        { threshold: 5, cls: 'find-mild', label: 'Moderate cognitive overload accumulating.', desc: 'You\'re managing, but the load is building. The risk is it becoming normalized before you notice the cost.', link: 'cognitive-load.html', linkText: 'See the science and strategies →' },
        { threshold: 9, cls: 'find-moderate', label: 'Significant cognitive overload — decision quality is degrading.', desc: 'Research shows degraded working memory leads to more bugs, worse architecture decisions, and slower debugging. This is fixable.', link: 'cognitive-load.html', linkText: 'Cognitive load recovery strategies →' },
        { threshold: 13, cls: 'find-significant', label: 'Critical cognitive overload — your brain is in survival mode.', desc: 'This level of cognitive load correlates with anxiety, insomnia, and professional regret. Please prioritize recovery.', link: 'mental-health.html', linkText: 'Mental health resources →' }
      ]
    },
    {
      id: 'skill',
      name: 'Skill Erosion',
      icon: '💪',
      description: 'Whether your core coding abilities are shrinking from disuse',
      color: '#8a9a5a',
      maxScore: 12,
      questions: [
        {
          text: 'Think about a complex debugging problem you solved recently. How confident are you that you could solve it without AI tools?',
          options: [
            { label: 'Completely confident — I understand the full stack', value: 0 },
            { label: 'Reasonably confident for most cases', value: 1 },
            { label: 'Somewhat — I\'d struggle with the harder cases', value: 2 },
            { label: 'Not really — I\'d be completely lost', value: 3 }
          ]
        },
        {
          text: 'How often do you write code completely without AI assistance?',
          options: [
            { label: 'Daily — I protect deliberate practice time', value: 0 },
            { label: 'A few times a week', value: 1 },
            { label: 'Once a week or less', value: 2 },
            { label: 'Almost never', value: 3 }
          ]
        },
        {
          text: 'When you look at code you wrote 6 months ago (without AI), how does it compare to code you write today?',
          options: [
            { label: 'Today\'s code is stronger — I\'ve grown', value: 0 },
            { label: 'About the same', value: 1 },
            { label: 'My older code showed deeper understanding', value: 2 },
            { label: 'I can\'t tell the difference, which concerns me', value: 3 }
          ]
        },
        {
          text: 'When AI generates a solution, how often do you fully understand why it works before you use it?',
          options: [
            { label: 'Always or almost always', value: 0 },
            { label: 'Usually, for the parts I care about', value: 1 },
            { label: 'Sometimes — I check if it works, not why', value: 2 },
            { label: 'Rarely — I just test and ship', value: 3 }
          ]
        }
      ],
      findings: [
        { threshold: 1, cls: 'find-low', label: 'Your skills are actively maintained.', desc: 'You\'re protecting deliberate practice and staying sharp. This is the right approach.', link: 'skill-atrophy.html', linkText: 'Research on skill maintenance →' },
        { threshold: 5, cls: 'find-mild', label: 'Early-stage skill erosion detected.', desc: 'The erosion is subtle at this stage — that\'s what makes it dangerous. Small no-AI sessions can reverse it quickly.', link: 'skill-atrophy.html', linkText: 'See the rebuild practices →' },
        { threshold: 9, cls: 'find-moderate', label: 'Documented skill atrophy in core areas.', desc: 'The research on automation atrophy (Bainbridge, 1983) is clear: without active use, skills degrade. But the window to rebuild is still open.', link: 'skill-atrophy.html', linkText: 'Skill rebuild protocol →' },
        { threshold: 13, cls: 'find-significant', label: 'Significant skill erosion — professional confidence is at risk.', desc: 'At this level, the gap between your perceived ability and actual ability has widened. This is recoverable but requires intentional practice.', link: 'skill-atrophy.html', linkText: 'Rebuilding your skills →' }
      ]
    },
    {
      id: 'decision',
      name: 'Decision Fatigue',
      icon: '⚡',
      description: 'How depleted your judgment is from too many AI-mediated choices',
      color: '#d4a040',
      maxScore: 12,
      questions: [
        {
          text: 'At the end of a workday, how confident are you in the technical decisions you made that day?',
          options: [
            { label: 'Confident — I weighed options carefully', value: 0 },
            { label: 'Mostly okay — some decisions I\'d revisit', value: 1 },
            { label: 'Uncertain — I made calls without full analysis', value: 2 },
            { label: 'I can\'t articulate why I made most of my choices', value: 3 }
          ]
        },
        {
          text: 'How many times do you evaluate and choose between AI suggestions in a typical workday?',
          options: [
            { label: 'Rarely — I usually already know what I want', value: 0 },
            { label: '5–10 times — focused use', value: 1 },
            { label: '15–25 times — significant AI involvement', value: 2 },
            { label: '30+ times — constant choice loops', value: 3 }
          ]
        },
        {
          text: 'When faced with a significant technical decision now, how does it compare to before AI tools?',
          options: [
            { label: 'I think through it the same way, AI is one input', value: 0 },
            { label: 'I tend to go with AI recommendations more than before', value: 1 },
            { label: 'I often ask AI first and use that as my starting point', value: 2 },
            { label: 'I defer to AI recommendations more than my own judgment', value: 3 }
          ]
        },
        {
          text: 'How do you feel about making architectural or design decisions without AI assistance?',
          options: [
            { label: 'Confident — I have strong instincts and frameworks', value: 0 },
            { label: 'Capable, but AI helps me consider more options', value: 1 },
            { label: 'Uncertain — I\'d want AI\'s take before committing', value: 2 },
            { label: 'Reluctant — I don\'t trust my judgment without AI validation', value: 3 }
          ]
        }
      ],
      findings: [
        { threshold: 1, cls: 'find-low', label: 'Decision-making remains sharp.', desc: 'Your judgment is intact and you\'re using AI as a tool, not a crutch. Keep the ratio healthy.', link: 'decision-fatigue-ai.html', linkText: 'Decision fatigue research →' },
        { threshold: 5, cls: 'find-mild', label: 'Mild decision fatigue creeping in.', desc: 'More AI-mediated choices are accumulating. Consider batching AI consultations to reduce the decision tax.', link: 'decision-fatigue-ai.html', linkText: 'Decision batching strategies →' },
        { threshold: 9, cls: 'find-moderate', label: 'Significant decision fatigue — judgment is compromised.', desc: 'Decision fatigue is insidious: you don\'t notice it degrading. But code review quality, architecture choices, and problem framing all suffer.', link: 'decision-fatigue-ai.html', linkText: 'Recovery and calibration →' },
        { threshold: 13, cls: 'find-significant', label: 'Critical decision fatigue — professional judgment is eroded.', desc: 'You may be relying on AI validation without realizing it. This affects your career trajectory and technical credibility.', link: 'decision-fatigue-ai.html', linkText: 'Rebuilding technical judgment →' }
      ]
    },
    {
      id: 'attention',
      name: 'Attention Residue',
      icon: '🔁',
      description: 'Whether your focus is permanently fractured by task-switching',
      color: '#6a8aaa',
      maxScore: 12,
      questions: [
        {
          text: 'After you check or respond to an AI-assisted task, how long does it take to get back to full focus on what you were doing?',
          options: [
            { label: 'Under 5 minutes — I\'m back quickly', value: 0 },
            { label: '5–15 minutes to get back into flow', value: 1 },
            { label: '15–30 minutes — significant ramp-up time', value: 2 },
            { label: '30+ minutes, or I don\'t fully get back', value: 3 }
          ]
        },
        {
          text: 'How often do you find yourself thinking about an AI query or suggestion when you should be focused on something else?',
          options: [
            { label: 'Rarely — I can set it down', value: 0 },
            { label: 'Sometimes — it lingers in the background', value: 1 },
            { label: 'Often — I\'m mentally half-in multiple things', value: 2 },
            { label: 'Constantly — my mind won\'t settle', value: 3 }
          ]
        },
        {
          text: 'When you\'re in a meeting or offline, how much mental residue from your AI work is still running in the background?',
          options: [
            { label: 'Very little — I can be fully present', value: 0 },
            { label: 'Some — there\'s an open loop or two', value: 1 },
            { label: 'A lot — I\'m mentally back at my desk', value: 2 },
            { label: 'I can\'t stop thinking about AI problems even when offline', value: 3 }
          ]
        },
        {
          text: 'How would you rate your ability to sustain focused work for 60–90 minutes without switching tasks?',
          options: [
            { label: 'Strong — I do this regularly', value: 0 },
            { label: 'Moderate — I manage 30–60 minute blocks', value: 1 },
            { label: 'Weak — 15–30 minutes before I break', value: 2 },
            { label: 'Very weak — I switch every few minutes', value: 3 }
          ]
        }
      ],
      findings: [
        { threshold: 1, cls: 'find-low', label: 'Attention integrity is strong.', desc: 'You\'re protecting deep focus and managing task-switching well. Your flow states are intact.', link: 'attention-residue.html', linkText: 'Attention residue research →' },
        { threshold: 5, cls: 'find-mild', label: 'Mild attention residue accumulating.', desc: 'The Gloria Mark research (23-minute recovery) applies to your situation. Small changes in batching AI work could prevent compounding.', link: 'attention-residue.html', linkText: 'Flow state protection strategies →' },
        { threshold: 9, cls: 'find-moderate', label: 'Significant attention residue — deep work is compromised.', desc: 'Your ability to think through hard problems is degraded. The compounding nature of attention residue means it gets worse without intervention.', link: 'attention-residue.html', linkText: 'Recovery and recalibration →' },
        { threshold: 13, cls: 'find-significant', label: 'Critical attention fragmentation — cognitive baseline is elevated.', desc: 'Your nervous system may be in chronic low-level alert. This affects sleep, relationships, and long-term cognitive health.', link: 'attention-residue.html', linkText: 'Attention restoration practices →' }
      ]
    },
    {
      id: 'identity',
      name: 'Identity Health',
      icon: '🪪',
      description: 'How solid your sense of professional self is in the AI era',
      color: '#9a6a8a',
      maxScore: 12,
      questions: [
        {
          text: 'How confident are you in your professional identity as a software engineer right now?',
          options: [
            { label: 'Very confident — I know what I bring to the table', value: 0 },
            { label: 'Reasonably confident, with occasional doubt', value: 1 },
            { label: 'Somewhat — I question my value at times', value: 2 },
            { label: 'Uncertain — I don\'t know what being a developer means anymore', value: 3 }
          ]
        },
        {
          text: 'When you introduce yourself as a software engineer, how does that statement feel?',
          options: [
            { label: 'Accurate and solid — that\'s who I am', value: 0 },
            { label: 'Mostly accurate — with some ambiguity', value: 1 },
            { label: 'Uncertain — I\'m not sure the title still fits', value: 2 },
            { label: 'Inaccurate — I don\'t know what to call myself', value: 3 }
          ]
        },
        {
          text: 'How much of your professional self-worth is tied to what you personally create vs. what AI helps you ship?',
          options: [
            { label: 'Mostly tied to my own contributions — AI is a tool', value: 0 },
            { label: 'Somewhat — I value both my judgment and the output', value: 1 },
            { label: 'Increasingly tied to shipped features regardless of authorship', value: 2 },
            { label: 'I\'m not sure what my professional worth comes from anymore', value: 3 }
          ]
        },
        {
          text: 'If you had to explain to a junior engineer what makes a great senior developer in the AI era, how confident are you in your answer?',
          options: [
            { label: 'Very confident — I have a clear framework', value: 0 },
            { label: 'Somewhat confident — I have ideas but they\'re evolving', value: 1 },
            { label: 'Uncertain — I\'m rethinking everything', value: 2 },
            { label: 'I genuinely don\'t know right now', value: 3 }
          ]
        }
      ],
      findings: [
        { threshold: 1, cls: 'find-low', label: 'Identity integrity is solid.', desc: 'You have a stable professional self-concept that incorporates AI as a tool. This is a strong position.', link: 'developer-identity.html', linkText: 'Developer identity in the AI era →' },
        { threshold: 5, cls: 'find-mild', label: 'Mild identity questioning — the ground is shifting.', desc: 'This is normal and even healthy at this stage. The key is staying in the question rather than rushing to a false certainty.', link: 'developer-identity.html', linkText: 'What AI cannot take from you →' },
        { threshold: 9, cls: 'find-moderate', label: 'Significant identity erosion — professional purpose is unclear.', desc: 'Identity loss affects motivation, relationships, and career direction. This is the most important axis to address.', link: 'developer-identity.html', linkText: 'Reconstruction framework →' },
        { threshold: 13, cls: 'find-significant', label: 'Critical identity disruption — professional grief is present.', desc: 'You may be experiencing genuine grief for a professional identity that feels lost. This is real and valid, and it can be reconstructed.', link: 'mental-health.html', linkText: 'Mental health support →' }
      ]
    }
  ];

  // ─── Tier definitions ──────────────────────────────────────────────────────
  var TIERS = [
    { max: 15, cls: 'tier-low', label: 'Managing Well', color: '#6a9a6a',
      title: 'Low AI Fatigue', desc: 'Your AI tool usage is well-calibrated. You\'re maintaining cognitive integrity, skill sharpness, and professional identity. Keep monitoring — these things can shift gradually.' },
    { max: 30, cls: 'tier-mild', label: 'Mild Fatigue', color: '#8a9a5a',
      title: 'Mild AI Fatigue', desc: 'You\'re functional but showing early signs across one or two axes. The damage is subtle and reversible. Now is the time to be deliberate about AI usage patterns.' },
    { max: 45, cls: 'tier-moderate', label: 'Moderate Fatigue', color: '#c09050',
      title: 'Moderate AI Fatigue', desc: 'Multiple axes are strained. Your cognitive quality, skill confidence, or professional identity is measurably affected. Structured recovery practices would significantly help.' },
    { max: 60, cls: 'tier-significant', label: 'Significant Fatigue', color: '#c07050',
      title: 'Significant AI Fatigue', desc: 'You\'re operating with meaningful impairment in several areas. This is affecting your work quality, career trajectory, and wellbeing. Prioritizing recovery is not optional at this stage.' },
    { max: 100, cls: 'tier-severe', label: 'Severe Fatigue', color: '#c05040',
      title: 'Severe AI Fatigue', desc: 'Multiple axes are critically degraded. You may be experiencing anxiety, insomnia, professional disillusionment, or a sense of meaning loss. Please treat this as a serious health concern and seek support.' }
  ];

  // ─── DOM helpers ───────────────────────────────────────────────────────────
  function el(id) { return document.getElementById(id); }

  function show(el) { el.style.display = ''; }
  function hide(el) { el.style.display = 'none'; }

  function setHTML(el, html) { el.innerHTML = html; }

  // ─── Quiz logic ───────────────────────────────────────────────────────────
  function startQuiz() {
    hide(el('introScreen'));
    show(el('quizScreen'));
    show(el('progressContainer'));
    answers = {};
    axisScores = {};
    currentAxis = 0;
    renderAxis();
  }

  function renderAxis() {
    var axis = AXES[currentAxis];
    var totalAxes = AXES.length;
    var progress = Math.round((currentAxis / totalAxes) * 100);
    var pct = ((currentAxis / totalAxes) * 100).toFixed(0);

    el('axisNum').textContent = currentAxis + 1;
    el('progressPct').textContent = pct + '%';
    el('progressFill').style.width = pct + '%';
    el('progressContainer').setAttribute('aria-valuenow', pct);

    var saved = answers[axis.id];
    var q = axis.questions[saved !== undefined ? 0 : 0];

    var optionsHTML = axis.questions.map(function(question, qi) {
      var opts = question.options.map(function(opt, oi) {
        var checked = (answers[axis.id + '_q' + qi] === opt.value) ? 'selected' : '';
        return '<button class="option-btn ' + checked + '" data-q="' + qi + '" data-val="' + opt.value + '" onclick="SI.selectOption(\'' + axis.id + '\', ' + qi + ', ' + opt.value + ', event)">' +
          '<span class="option-radio"></span>' +
          '<span class="option-text">' +
          '<span class="option-label">' + opt.label + '</span>' +
          '</span></button>';
      }).join('');
      return '<div class="axis-section" data-axis-q="' + qi + '" ' + (qi > 0 ? 'style="display:none;"' : '') + '>' +
        '<div class="axis-header"><span class="axis-num">AXIS ' + (currentAxis + 1) + ' / ' + totalAxes + '</span><span class="axis-name">' + axis.icon + ' ' + axis.name + '</span></div>' +
        '<p class="axis-question">' + question.text + '</p>' +
        '<div class="options">' + opts + '</div></div>';
    }).join('');

    setHTML(el('questionBlock'), '<div id="qWrap">' + optionsHTML + '</div>');

    // Show navigation state
    el('prevBtn').style.display = currentAxis > 0 ? '' : 'none';

    // Restore saved answers
    if (saved !== undefined) {
      var qBtns = el('questionBlock').querySelectorAll('.option-btn');
      qBtns.forEach(function(btn) {
        var qIdx = parseInt(btn.getAttribute('data-q'));
        var val = parseInt(btn.getAttribute('data-val'));
        if (answers[axis.id + '_q' + qIdx] === val) {
          btn.classList.add('selected');
        }
      });
    }

    updateNextBtn();
  }

  window.SI = {
    selectOption: function(axisId, qIdx, val, e) {
      var btn = e.currentTarget;
      // Deselect siblings in same question
      var siblings = btn.parentElement.querySelectorAll('.option-btn');
      siblings.forEach(function(s) { s.classList.remove('selected'); });
      btn.classList.add('selected');
      answers[axisId + '_q' + qIdx] = val;

      // Show next question or update button
      var axis = AXES.find(function(a) { return a.id === axisId; });
      var nextQ = qIdx + 1;
      var qSections = el('questionBlock').querySelectorAll('.axis-section');
      if (nextQ < axis.questions.length) {
        qSections[qIdx].style.display = 'none';
        qSections[nextQ].style.display = '';
      }
      updateNextBtn();
    }
  };

  function updateNextBtn() {
    var axis = AXES[currentAxis];
    var answered = 0;
    for (var i = 0; i < axis.questions.length; i++) {
      if (answers[axis.id + '_q' + i] !== undefined) answered++;
    }
    var allAnswered = answered === axis.questions.length;
    el('nextBtn').disabled = !allAnswered;
    if (currentAxis === AXES.length - 1) {
      el('nextBtn').textContent = allAnswered ? 'See My Results →' : 'Next →';
    } else {
      el('nextBtn').textContent = allAnswered ? 'Next →' : 'Next →';
    }
  }

  function nextAxis() {
    var axis = AXES[currentAxis];
    var score = 0;
    for (var i = 0; i < axis.questions.length; i++) {
      score += answers[axis.id + '_q' + i] || 0;
    }
    answers[axis.id] = score;
    axisScores[axis.id] = [score, axis.maxScore];

    if (currentAxis < AXES.length - 1) {
      currentAxis++;
      renderAxis();
    } else {
      showResults();
    }
  }

  function prevAxis() {
    if (currentAxis > 0) {
      currentAxis--;
      renderAxis();
    }
  }

  function skipAxis() {
    if (currentAxis < AXES.length - 1) {
      answers[AXES[currentAxis].id] = null;
      axisScores[AXES[currentAxis].id] = [null, AXES[currentAxis].maxScore];
      currentAxis++;
      renderAxis();
    } else {
      showResults();
    }
  }

  // ─── Results ───────────────────────────────────────────────────────────────
  function showResults() {
    hide(el('quizScreen'));
    hide(el('progressContainer'));
    show(el('resultsScreen'));

    var totalScore = 0;
    var totalMax = 0;
    Object.keys(axisScores).forEach(function(k) {
      if (axisScores[k][0] !== null) {
        totalScore += axisScores[k][0];
        totalMax += axisScores[k][1];
      }
    });

    var pct = totalMax > 0 ? Math.round((totalScore / totalMax) * 100) : 0;

    // Animate score ring
    setTimeout(function() {
      var ring = el('scoreRingFill');
      var circumference = 2 * Math.PI * 80; // r=80
      var offset = circumference - (pct / 100) * circumference;
      ring.style.strokeDashoffset = offset;
      ring.style.strokeDasharray = circumference;
      // Color based on tier
      var tier = getTier(pct);
      ring.style.stroke = tier.color;
    }, 100);

    el('overallScore').textContent = pct;

    // Tier
    var tier = getTier(pct);
    el('severityTier').className = 'severity-tier ' + tier.cls;
    setHTML(el('severityLabel'), tier.label);
    setHTML(el('severityTitle'), tier.title);
    setHTML(el('severityDesc'), tier.desc);

    // Date
    var now = new Date();
    el('completedDate').textContent = now.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });

    // Axis bars
    var barsHTML = AXES.map(function(axis) {
      var score = answers[axis.id];
      if (score === null) return '';
      var pctA = Math.round((score / axis.maxScore) * 100);
      var fillClass = score <= 2 ? 'fill-low' : score <= 5 ? 'fill-mild' : score <= 9 ? 'fill-moderate' : score <= 11 ? 'fill-significant' : 'fill-severe';
      return '<div class="axis-bar-group">' +
        '<div class="axis-bar-label"><span class="axis-bar-name">' + axis.icon + ' ' + axis.name + '</span><span class="axis-bar-score">' + score + ' / ' + axis.maxScore + '</span></div>' +
        '<div class="axis-bar-track"><div class="axis-bar-fill ' + fillClass + '" style="width:0%;background:' + axis.color + ';" data-width="' + pctA + '%"></div></div>' +
        '</div>';
    }).join('');
    setHTML(el('axisBars'), barsHTML);

    // Animate bars
    setTimeout(function() {
      el('axisBars').querySelectorAll('.axis-bar-fill').forEach(function(bar) {
        bar.style.width = bar.getAttribute('data-width');
      });
    }, 200);

    // Findings
    var findingsHTML = AXES.map(function(axis) {
      var score = answers[axis.id];
      if (score === null) return '';
      var finding = axis.findings.slice().reverse().find(function(f) { return score >= f.threshold; });
      if (!finding) return '';
      return '<div class="finding-card ' + finding.cls + '">' +
        '<div class="finding-title">' + axis.icon + ' ' + axis.name + ': ' + finding.label + '</div>' +
        '<div class="finding-desc">' + finding.desc + '</div>' +
        '<a href="' + finding.link + '" class="finding-link">' + finding.linkText + '</a>' +
        '</div>';
    }).filter(function(f) { return f; }).join('');
    setHTML(el('findingCards'), findingsHTML);

    // Save to localStorage
    try {
      localStorage.setItem('clearing_severity_index', JSON.stringify({
        answers: answers,
        axisScores: axisScores,
        totalScore: totalScore,
        totalMax: totalMax,
        pct: pct,
        tier: tier.label,
        savedAt: new Date().toISOString()
      }));
    } catch(e) {}

    // Scroll to results
    el('resultsScreen').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function getTier(pct) {
    for (var i = 0; i < TIERS.length; i++) {
      if (pct <= TIERS[i].max) return TIERS[i];
    }
    return TIERS[TIERS.length - 1];
  }

  // ─── Share ─────────────────────────────────────────────────────────────────
  window.shareTwitter = function() {
    var data;
    try { data = JSON.parse(localStorage.getItem('clearing_severity_index') || '{}'); } catch(e) { data = {}; }
    var tier = data.tier || 'assessed';
    var text = 'I just took the AI Fatigue Severity Index on @TheClearing. Result: ' + tier + '. If you work with AI tools, take it — it\'s honest. → clearing-ai.com/ai-fatigue-severity-index.html';
    window.open('https://twitter.com/intent/tweet?text=' + encodeURIComponent(text), '_blank', 'width=600,height=400');
  };

  window.shareLinkedIn = function() {
    window.open('https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent('https://clearing-ai.com/ai-fatigue-severity-index.html'), '_blank', 'width=600,height=500');
  };

  window.copyLink = function() {
    var url = 'https://clearing-ai.com/ai-fatigue-severity-index.html';
    if (navigator.clipboard) {
      navigator.clipboard.writeText(url).then(function() {
        alert('Link copied! Share it with a teammate who needs this.');
      });
    } else {
      prompt('Copy this link:', url);
    }
  };

  window.retake = function() {
    hide(el('resultsScreen'));
    show(el('introScreen'));
    currentAxis = 0;
    answers = {};
    axisScores = {};
    el('scoreRingFill').style.strokeDashoffset = 502.65;
  };

  // ─── FAQ ───────────────────────────────────────────────────────────────────
  window.toggleFaq = function(btn) {
    var answer = btn.nextElementSibling;
    var arrow = btn.querySelector('.faq-arrow');
    var expanded = btn.getAttribute('aria-expanded') === 'true';
    if (expanded) {
      answer.style.display = 'none';
      arrow.textContent = '+';
      btn.setAttribute('aria-expanded', 'false');
    } else {
      answer.style.display = '';
      arrow.textContent = '−';
      btn.setAttribute('aria-expanded', 'true');
    }
  };

  // ─── Theme toggle ──────────────────────────────────────────────────────────
  var toggleBtn = document.querySelector('.theme-toggle');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      var html = document.documentElement;
      var current = html.dataset.theme || 'dark';
      html.dataset.theme = current === 'dark' ? 'light' : 'dark';
    });
  }

  // ─── Restore from localStorage ────────────────────────────────────────────
  try {
    var saved = JSON.parse(localStorage.getItem('clearing_severity_index') || 'null');
    if (saved && saved.pct !== undefined) {
      // Auto-show results if they exist
      // Don't auto-show — let them start fresh
    }
  } catch(e) {}

})();
