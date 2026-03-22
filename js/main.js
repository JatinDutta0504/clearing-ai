/* ============================================
   The Clearing — Shared JavaScript
   ============================================ */

// ============================================
// Navigation: scroll state + mobile toggle
// ============================================
(function () {
  const nav = document.querySelector('.nav');
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (nav) {
    const handleScroll = () => {
      if (window.scrollY > 40) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
  }

  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      toggle.setAttribute('aria-expanded', navLinks.classList.contains('open'));
    });

    // Close on link click
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!nav.contains(e.target)) {
        navLinks.classList.remove('open');
      }
    });
  }

  // Mark active nav link
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
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
