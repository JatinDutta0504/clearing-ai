/* ============================================
   The Clearing — AI Fatigue Quiz
   Hour 5: Interactive self-assessment for engineers
   Vanilla JS, no libraries, accessible
   ============================================ */

(function () {
  'use strict';

  // ============================================
  // Quiz Data — 5 questions, 4 options each
  // Each answer maps to a "fatigue score" 0–3
  // ============================================
  const quizData = [
    {
      id: 'q1',
      icon: '🧠',
      question: 'When you sit down to write code, what happens first?',
      answers: [
        { text: 'I think through the problem, then start typing.', score: 0 },
        { text: 'I open a tab and sketch it out, then code.', score: 1 },
        { text: 'I ask an AI to generate a starting point, then edit it.', score: 2 },
        { text: 'I paste the prompt in before I\'ve even really thought about it.', score: 3 },
      ]
    },
    {
      id: 'q2',
      icon: '😮‍💨',
      question: 'How do you feel on Sunday evening before a work week starts?',
      answers: [
        { text: 'Generally fine — maybe a little sleepy.', score: 0 },
        { text: 'Mild dread, nothing unusual for a professional.', score: 1 },
        { text: 'A persistent heaviness that\'s hard to shake.', score: 2 },
        { text: 'A specific anxiety about keeping up with the AI pace.', score: 3 },
      ]
    },
    {
      id: 'q3',
      icon: '🤔',
      question: 'When you solve a hard problem, where does the satisfaction come from?',
      answers: [
        { text: 'From the struggle and the moment it clicked in my head.', score: 0 },
        { text: 'Mostly from the outcome — I\'m fine using AI to get there.', score: 1 },
        { text: 'I\'m not sure I feel satisfaction the way I used to.', score: 2 },
        { text: 'I can\'t remember the last time I felt real satisfaction at work.', score: 3 },
      ]
    },
    {
      id: 'q4',
      icon: '🔁',
      question: 'How often do you review AI-generated code without fully understanding it?',
      answers: [
        { text: 'Rarely — I read and verify everything carefully.', score: 0 },
        { text: 'Sometimes, when I\'m under deadline pressure.', score: 1 },
        { text: 'Often — there\'s too much volume to digest it all.', score: 2 },
        { text: 'I\'ve mostly stopped questioning it if the tests pass.', score: 3 },
      ]
    },
    {
      id: 'q5',
      icon: '💬',
      question: 'If a junior engineer asked you to explain a system you built this year, you\'d say:',
      answers: [
        { text: '"Sure, let me walk you through my thinking…"', score: 0 },
        { text: '"Happy to — give me a moment to put it in words."', score: 1 },
        { text: '"Honestly, the AI wrote parts of it, so… let me check the docs."', score: 2 },
        { text: '"I\'m not sure I could fully explain it myself anymore."', score: 3 },
      ]
    },
  ];

  // ============================================
  // Scoring tiers
  // ============================================
  const tiers = [
    {
      min: 0, max: 3,
      label: 'You\'re holding up well',
      emoji: '🌿',
      color: 'var(--forest-light)',
      description: 'You\'re staying grounded. You still feel connected to your work, think before you act, and trust your own instincts. The pressures are real, but they haven\'t overwhelmed your sense of craft. Keep doing what you\'re doing — and keep checking in with yourself.',
      cta: { text: 'Read the essay on AI fatigue →', href: 'why.html' },
    },
    {
      min: 4, max: 7,
      label: 'Some fatigue is showing',
      emoji: '🌤',
      color: 'var(--earth-light)',
      description: 'You\'re in the grey zone — not burnt out, but not quite yourself either. The pace has gotten to you in places. Maybe you notice you accept AI output a little too quickly, or Sunday evenings have gotten heavier. Small resets matter here. This is a good time to pay attention.',
      cta: { text: 'Check out our 10 signs of AI fatigue →', href: 'tips.html' },
    },
    {
      min: 8, max: 11,
      label: 'Real AI fatigue is present',
      emoji: '🌧',
      color: 'var(--earth)',
      description: 'You\'re carrying more than you should have to. The volume, the pace, the constant context-switching — it\'s taken a toll. You may have noticed your relationship with your own work changing. The good news: naming this is step one. There are real ways through.',
      cta: { text: 'Read stories from engineers who feel this too →', href: 'stories.html' },
    },
    {
      min: 12, max: 15,
      label: 'You need a real break',
      emoji: '🌑',
      color: 'var(--bark)',
      description: 'This isn\'t a mild slump — you\'re describing significant depletion. The markers you\'re hitting are the ones engineers describe just before burning out completely: disconnection from your own work, inability to explain what you\'ve built, anxiety about keeping pace. Please take this seriously. You matter more than your velocity.',
      cta: { text: 'Start with the resources that helped others →', href: 'resources.html' },
    },
  ];

  // ============================================
  // State
  // ============================================
  let currentQuestion = 0;
  let answers = new Array(quizData.length).fill(null);
  let quizStarted = false;

  // ============================================
  // DOM references (lazily resolved)
  // ============================================
  function getEl(id) { return document.getElementById(id); }

  // ============================================
  // Render: intro screen
  // ============================================
  function renderIntro() {
    const container = getEl('quiz-container');
    if (!container) return;

    container.innerHTML = `
      <div class="quiz-intro fade-in visible">
        <div class="quiz-intro-icon">🔍</div>
        <h3 class="quiz-intro-title">Do you have AI fatigue?</h3>
        <p class="quiz-intro-desc">
          5 questions. 2 minutes. An honest read on where you actually are right now —
          not where you think you should be.
        </p>
        <div class="quiz-intro-note">
          Anonymous. Nothing is stored. This runs entirely in your browser.
        </div>
        <button class="btn btn-primary quiz-start-btn" id="quiz-start">
          Take the assessment →
        </button>
      </div>
    `;

    const startBtn = getEl('quiz-start');
    if (startBtn) {
      startBtn.addEventListener('click', startQuiz);
    }
  }

  // ============================================
  // Start quiz
  // ============================================
  function startQuiz() {
    quizStarted = true;
    currentQuestion = 0;
    answers = new Array(quizData.length).fill(null);
    renderQuestion();
  }

  // ============================================
  // Render: question
  // ============================================
  function renderQuestion() {
    const container = getEl('quiz-container');
    if (!container) return;

    const q = quizData[currentQuestion];
    const progress = ((currentQuestion) / quizData.length) * 100;
    const selectedAnswer = answers[currentQuestion];

    container.innerHTML = `
      <div class="quiz-question-wrapper">
        <div class="quiz-progress-bar">
          <div class="quiz-progress-fill" style="width: ${progress}%"></div>
        </div>
        <div class="quiz-counter">Question ${currentQuestion + 1} of ${quizData.length}</div>

        <div class="quiz-question-card">
          <div class="quiz-q-icon">${q.icon}</div>
          <h3 class="quiz-q-text">${q.question}</h3>

          <ul class="quiz-answers" role="list">
            ${q.answers.map((a, i) => `
              <li>
                <button
                  class="quiz-answer-btn ${selectedAnswer === i ? 'selected' : ''}"
                  data-index="${i}"
                  data-score="${a.score}"
                  aria-pressed="${selectedAnswer === i}"
                >
                  <span class="quiz-answer-letter">${String.fromCharCode(65 + i)}</span>
                  <span class="quiz-answer-text">${a.text}</span>
                </button>
              </li>
            `).join('')}
          </ul>
        </div>

        <div class="quiz-nav">
          ${currentQuestion > 0
            ? `<button class="btn btn-secondary quiz-nav-btn" id="quiz-prev">← Back</button>`
            : `<span></span>`
          }
          <button
            class="btn btn-primary quiz-nav-btn ${selectedAnswer === null ? 'disabled' : ''}"
            id="quiz-next"
            ${selectedAnswer === null ? 'disabled' : ''}
          >
            ${currentQuestion < quizData.length - 1 ? 'Next →' : 'See my results →'}
          </button>
        </div>
      </div>
    `;

    // Answer button listeners
    container.querySelectorAll('.quiz-answer-btn').forEach(btn => {
      btn.addEventListener('click', function () {
        const idx = parseInt(this.dataset.index);
        selectAnswer(idx);
      });
    });

    // Nav listeners
    const nextBtn = getEl('quiz-next');
    const prevBtn = getEl('quiz-prev');

    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        if (answers[currentQuestion] !== null) {
          if (currentQuestion < quizData.length - 1) {
            currentQuestion++;
            renderQuestion();
          } else {
            renderResults();
          }
        }
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function () {
        if (currentQuestion > 0) {
          currentQuestion--;
          renderQuestion();
        }
      });
    }
  }

  // ============================================
  // Select an answer
  // ============================================
  function selectAnswer(idx) {
    answers[currentQuestion] = idx;

    // Update UI
    document.querySelectorAll('.quiz-answer-btn').forEach((btn, i) => {
      btn.classList.toggle('selected', i === idx);
      btn.setAttribute('aria-pressed', i === idx);
    });

    const nextBtn = getEl('quiz-next');
    if (nextBtn) {
      nextBtn.disabled = false;
      nextBtn.classList.remove('disabled');
    }

    // Auto-advance after short delay on desktop (not mobile to avoid scroll issues)
    if (window.innerWidth > 600) {
      setTimeout(() => {
        if (currentQuestion < quizData.length - 1) {
          currentQuestion++;
          renderQuestion();
        } else {
          renderResults();
        }
      }, 600);
    }
  }

  // ============================================
  // Build Twitter share URL from tier + score
  // ============================================
  function buildTwitterUrl(tier, score) {
    const messages = {
      0: `I took The Clearing's AI Fatigue Quiz and I'm holding up well (${score}/15). Are you?`,
      1: `I scored ${score}/15 on The Clearing's AI Fatigue Quiz — some fatigue is showing. Sound familiar?`,
      2: `I scored ${score}/15 on The Clearing's AI Fatigue Quiz. Real AI fatigue is present. If you're a software engineer, this quiz is worth taking.`,
      3: `I scored ${score}/15 on The Clearing's AI Fatigue Quiz. I need a real break. Sharing this in case someone else recognises themselves in it.`,
    };
    const tierIdx = [0, 1, 2, 3].find(i => score >= tiers[i].min && score <= tiers[i].max) ?? 3;
    const text = messages[tierIdx];
    return `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent('https://clearing-ai.com/#quiz')}&via=clearingai`;
  }

  // ============================================
  // Render: results
  // ============================================
  function renderResults() {
    const container = getEl('quiz-container');
    if (!container) return;

    // Calculate total score
    const totalScore = answers.reduce((sum, ansIdx, qIdx) => {
      if (ansIdx === null) return sum;
      return sum + quizData[qIdx].answers[ansIdx].score;
    }, 0);

    const tier = tiers.find(t => totalScore >= t.min && totalScore <= t.max) || tiers[tiers.length - 1];

    // Per-question breakdown
    const breakdown = quizData.map((q, i) => {
      const ansIdx = answers[i];
      if (ansIdx === null) return '';
      const ans = q.answers[ansIdx];
      const barWidth = (ans.score / 3) * 100;
      const barColor = ans.score === 0 ? 'var(--forest-light)' : ans.score === 1 ? 'var(--forest-pale)' : ans.score === 2 ? 'var(--earth-light)' : 'var(--bark)';
      return `
        <div class="quiz-breakdown-item">
          <div class="quiz-breakdown-q">${q.icon} ${q.question}</div>
          <div class="quiz-breakdown-a">${ans.text}</div>
          <div class="quiz-breakdown-bar">
            <div class="quiz-breakdown-fill" style="width: ${barWidth}%; background: ${barColor}"></div>
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="quiz-results fade-in visible">

        <div class="quiz-score-ring" style="--tier-color: ${tier.color}">
          <div class="quiz-score-emoji">${tier.emoji}</div>
          <div class="quiz-score-num">${totalScore}<span>/15</span></div>
        </div>

        <div class="quiz-tier-label" style="color: ${tier.color}">${tier.label}</div>

        <p class="quiz-tier-desc">${tier.description}</p>

        <a href="${tier.cta.href}" class="btn btn-primary quiz-result-cta">${tier.cta.text}</a>

        <div class="quiz-breakdown">
          <h4 class="quiz-breakdown-title">Your answers</h4>
          ${breakdown}
        </div>

        <div class="quiz-retake">
          <button class="btn btn-secondary" id="quiz-retake">Retake the quiz</button>
          <p class="quiz-retake-note">Results are not stored. This entire quiz lives in your browser.</p>
        </div>

        <div class="quiz-share-prompt">
          <p class="quiz-share-title">Know someone who might need this?</p>
          <div class="quiz-share-buttons">
            <a
              class="quiz-share-btn quiz-share-twitter"
              href="${buildTwitterUrl(tier, totalScore)}"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Share your result on Twitter/X"
            >𝕏 Share on X</a>
            <a
              class="quiz-share-btn quiz-share-linkedin"
              href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fclearing-ai.com%2F%23quiz"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Share on LinkedIn"
            >in Share on LinkedIn</a>
            <button
              class="quiz-share-btn quiz-share-copy"
              id="quiz-copy-link"
              aria-label="Copy link to quiz"
            >🔗 Copy link</button>
          </div>
          <p class="quiz-share-note">No score is shared — just the link to the quiz.</p>
        </div>

      </div>
    `;

    const retakeBtn = getEl('quiz-retake');
    if (retakeBtn) {
      retakeBtn.addEventListener('click', function () {
        quizStarted = false;
        renderIntro();
      });
    }

    // Copy link button
    const copyBtn = getEl('quiz-copy-link');
    if (copyBtn) {
      copyBtn.addEventListener('click', function () {
        navigator.clipboard.writeText('https://clearing-ai.com/#quiz').then(() => {
          this.textContent = '✓ Copied!';
          setTimeout(() => { this.textContent = '🔗 Copy link'; }, 2200);
        }).catch(() => {
          // fallback for older browsers
          this.textContent = 'clearing-ai.com/#quiz';
          setTimeout(() => { this.textContent = '🔗 Copy link'; }, 3000);
        });
      });
    }

    // Animate score bar fills after DOM is ready
    requestAnimationFrame(() => {
      container.querySelectorAll('.quiz-breakdown-fill').forEach(el => {
        const target = el.style.width;
        el.style.width = '0';
        requestAnimationFrame(() => {
          el.style.transition = 'width 0.8s ease';
          el.style.width = target;
        });
      });
    });
  }

  // ============================================
  // Init
  // ============================================
  function init() {
    const container = getEl('quiz-container');
    if (!container) return;
    renderIntro();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
