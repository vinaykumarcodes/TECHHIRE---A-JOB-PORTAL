/* careers.js
 * Adds animations and smooth scrolling for Careers page
 */

document.addEventListener('DOMContentLoaded', () => {

  // ============= Scroll Reveal Animation =============
  const fadeElems = document.querySelectorAll('.fade-in');

  if (!('IntersectionObserver' in window)) {
    // fallback if browser doesn’t support IO
    fadeElems.forEach(el => el.classList.add('visible'));
  } else {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    fadeElems.forEach(el => observer.observe(el));
  }

  // ============= Smooth Scroll for CTA buttons =============
  const ctaButtons = document.querySelectorAll('.btn-cta');

  ctaButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const targetId = button.getAttribute('href');
      if (targetId && targetId.startsWith('#')) {
        e.preventDefault();
        document.querySelector(targetId).scrollIntoView({
          behavior: 'smooth'
        });
      }
    });
  });

  // ============= Floating Shapes (optional) =============
  // If you later add floating elements with class .floating-shape
  const floatingShapes = document.querySelectorAll('.floating-shape');
  floatingShapes.forEach(shape => {
    shape.style.animationDelay = `${Math.random() * 4}s`;
  });

});
// static/js/careers.js
document.addEventListener("DOMContentLoaded", () => {
  const fadeElems = document.querySelectorAll('.fade-in');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
      }
    });
  }, { threshold: 0.1 });

  fadeElems.forEach(el => observer.observe(el));
});
// ✅ Fade-in on scroll for Careers hero section
document.addEventListener("DOMContentLoaded", () => {
  const hero = document.querySelector(".careers-hero");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          hero.classList.add("active");
        }
      });
    },
    { threshold: 0.2 }
  );

  if (hero) observer.observe(hero);
});
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("applicationModal");
  const closeBtn = document.querySelector("#applicationModal .close");
  const applyButtons = document.querySelectorAll(".btn-apply");

  applyButtons.forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      modal.style.display = "block";
    });
  });

  // Close modal when close button is clicked
  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      modal.style.display = "none";
    });
  }

  // Close modal when clicking outside modal content
  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });
});
