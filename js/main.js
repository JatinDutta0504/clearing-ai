/* ============================================
   The Clearing — Shared JavaScript
   ============================================ */

// ============================================
// New Dropdown Nav: mobile toggle + dropdowns
// ============================================
(function () {
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  // Mobile hamburger toggle
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', navLinks.classList.contains('open'));
    });
  }

  // Dropdown click for mobile (touch devices)
  document.querySelectorAll('.dropdown-trigger').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const parent = btn.closest('.nav-dropdown');
      if (window.innerWidth <= 900) {
        e.preventDefault();
        parent.classList.toggle('open');
      }
    });
  });

  // Close nav on outside click
  document.addEventListener('click', (e) => {
    if (navLinks && !e.target.closest('.main-nav')) {
      navLinks.classList.remove('open');
      document.querySelectorAll('.nav-dropdown').forEach(d => d.classList.remove('open'));
      if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Mark active nav link
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (href === currentPage || href.split('#')[0] === currentPage || (currentPage === '' && href === 'index.html'))) {
      link.classList.add('active');
      // Also highlight parent dropdown trigger
      const dropdown = link.closest('.nav-dropdown');
      if (dropdown) {
        const trigger = dropdown.querySelector('.dropdown-trigger');
        if (trigger) trigger.classList.add('active');
      }
    }
  });
})();

// ============================================
// Intersection Observer: fade-in animations
// ============================================
(function () {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -48px 0px' });

  document.querySelectorAll('.fade-in, .stagger').forEach(el => {
    observer.observe(el);
  });
})();

// ============================================
// Toast utility
// ============================================
function showToast(message, duration = 3000) {
  let toast = document.querySelector('.toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  requestAnimationFrame(() => {
    toast.classList.add('show');
  });
  setTimeout(() => {
    toast.classList.remove('show');
  }, duration);
}

// ============================================
// Quote rotator
// ============================================
const ambientQuotes = [
  "The best code you ever wrote was the one you took your time with.",
  "Slowness is not inefficiency. It's how humans think.",
  "You are allowed to not know the answer right away.",
  "Rest is not the opposite of productivity. It's the foundation of it.",
  "No model can replicate the way you understand what actually matters.",
  "A thought worth having is worth sitting with for a moment.",
  "Your instincts took years to build. Trust them.",
  "The cursor blinks. You don't have to.",
  "Every great system was designed by someone who paused.",
  "Clarity doesn't come from moving faster. It comes from being still.",
  "There is no PRD for the feeling that something is wrong.",
  "Some of the best debugging happens away from the screen.",
  "Your attention is not a resource to be optimized.",
  "The internet can wait. Your nervous system cannot.",
];

function initQuoteRotator() {
  const el = document.querySelector('.quote-rotator');
  if (!el) return;

  let idx = Math.floor(Math.random() * ambientQuotes.length);

  function showQuote() {
    el.style.opacity = '0';
    setTimeout(() => {
      el.textContent = `"${ambientQuotes[idx]}"`;
      el.style.opacity = '1';
      idx = (idx + 1) % ambientQuotes.length;
    }, 800);
  }

  el.style.transition = 'opacity 0.8s ease';
  showQuote();
  setInterval(showQuote, 7000);
}

document.addEventListener('DOMContentLoaded', initQuoteRotator);

// ============================================
// Hour 9 — Dark Mode Toggle + Reading Progress
// ============================================

// ----- Dark Mode -----
(function () {
  const STORAGE_KEY = 'clearing-theme';

  // Determine initial theme
  function getPreferred() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
    const btn = document.querySelector('.dark-toggle');
    if (!btn) return;
    const icon = btn.querySelector('.toggle-icon');
    const label = btn.querySelector('.toggle-label');
    if (theme === 'dark') {
      if (icon) icon.textContent = '☀️';
      if (label) label.textContent = 'Light';
      btn.setAttribute('aria-label', 'Switch to light mode');
      btn.setAttribute('aria-pressed', 'true');
    } else {
      if (icon) icon.textContent = '🌙';
      if (label) label.textContent = 'Dark';
      btn.setAttribute('aria-label', 'Switch to dark mode');
      btn.setAttribute('aria-pressed', 'false');
    }
  }

  function createToggle() {
    const nav = document.querySelector('.nav');
    if (!nav || document.querySelector('.dark-toggle')) return;

    const btn = document.createElement('button');
    btn.className = 'dark-toggle';
    btn.setAttribute('type', 'button');
    btn.setAttribute('aria-label', 'Switch to dark mode');
    btn.setAttribute('aria-pressed', 'false');
    btn.innerHTML = '<span class="toggle-icon" aria-hidden="true">🌙</span><span class="toggle-label">Dark</span>';

    // Insert before the hamburger (or at end of nav)
    const toggle = nav.querySelector('.nav-toggle');
    if (toggle) {
      nav.insertBefore(btn, toggle);
    } else {
      nav.appendChild(btn);
    }

    btn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      applyTheme(current === 'dark' ? 'light' : 'dark');
    });
  }

  // Apply immediately to avoid FOUC
  applyTheme(getPreferred());

  // Create button after DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createToggle);
  } else {
    createToggle();
  }

  // Respond to system theme changes if no saved preference
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem(STORAGE_KEY)) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });
})();

// ----- Reading Progress Bar -----
(function () {
  const bar = document.createElement('div');
  bar.className = 'reading-progress';
  bar.setAttribute('role', 'progressbar');
  bar.setAttribute('aria-label', 'Reading progress');
  bar.setAttribute('aria-valuemin', '0');
  bar.setAttribute('aria-valuemax', '100');
  document.body.prepend(bar);

  function updateProgress() {
    const doc = document.documentElement;
    const scrollTop = window.scrollY;
    const scrollHeight = doc.scrollHeight - doc.clientHeight;
    if (scrollHeight <= 0) {
      bar.style.width = '0%';
      bar.classList.remove('visible');
      return;
    }
    const pct = Math.min(100, (scrollTop / scrollHeight) * 100);
    bar.style.width = pct + '%';
    bar.setAttribute('aria-valuenow', Math.round(pct));
    if (pct > 2) {
      bar.classList.add('visible');
    } else {
      bar.classList.remove('visible');
    }
  }

  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();
})();

// ----- Skip to content -----
(function () {
  if (document.querySelector('.skip-link')) return;
  const main = document.querySelector('main, [role="main"], #quiz-container, .hero, section');
  if (!main) return;
  if (!main.id) main.id = 'main-content';
  const a = document.createElement('a');
  a.href = '#' + main.id;
  a.className = 'skip-link';
  a.textContent = 'Skip to main content';
  document.body.prepend(a);
})();
