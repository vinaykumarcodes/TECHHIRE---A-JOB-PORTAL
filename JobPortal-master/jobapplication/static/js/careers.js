// Careers Page Script – clean unified version
document.addEventListener("DOMContentLoaded", () => {
  // Fade-in animation for sections
  const fadeElems = document.querySelectorAll(".fade-in");
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    },
    { threshold: 0.2 }
  );

  fadeElems.forEach((el) => observer.observe(el));

  // Smooth scroll for CTA (Call To Action) buttons
  document.querySelectorAll(".btn-cta[href^='#']").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const target = document.querySelector(btn.getAttribute("href"));
      if (target) {
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // (Optional) You can trigger modal open/close automatically if needed,
  // but Bootstrap handles modals with data attributes, so no JS is required.
});
document.addEventListener("DOMContentLoaded", () => {
  const modals = document.querySelectorAll(".modal");
  modals.forEach(modal => {
    modal.addEventListener("shown.bs.modal", () => {
      document.body.classList.add("modal-open-custom");
    });
    modal.addEventListener("hidden.bs.modal", () => {
      document.body.classList.remove("modal-open-custom");
    });
  });
});
// Auto-hide alerts
setTimeout(() => {
    document.querySelectorAll('.alert').forEach(el => el.classList.remove('show'));
}, 4000);
document.addEventListener("DOMContentLoaded", function() {
  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
      }
    });
  });
});