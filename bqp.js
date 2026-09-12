(function () {
  'use strict';

  // Sticky header shadow
  var header = document.getElementById('siteHeader');
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 8) header.classList.add('is-stuck');
    else header.classList.remove('is-stuck');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile navigation
  var toggle = document.getElementById('navToggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.textContent = open ? 'Close' : 'Menu';
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.nav-pill').forEach(function (p) {
      p.addEventListener('click', function () {
        document.body.classList.remove('nav-open');
        toggle.textContent = 'Menu';
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Contact form - mailto handoff
  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = document.getElementById('cf-name').value.trim();
      var email = document.getElementById('cf-email').value.trim();
      var company = document.getElementById('cf-company').value.trim();
      var message = document.getElementById('cf-message').value.trim();
      var status = document.getElementById('formStatus');
      if (!name || !email || !message) {
        status.textContent = 'Please complete all required fields.';
        status.style.color = '#C2312A';
        return;
      }
      var subject = encodeURIComponent('Advisory Enquiry - ' + name + (company ? ' (' + company + ')' : ''));
      var body = encodeURIComponent(
        'Dear Team Bharat Quantum Prospera,\n\n' + message + '\n\nWarm regards,\n' + name +
        (company ? '\n' + company : '') + '\n' + email
      );
      window.location.href = 'mailto:durgesh@bqpartners.in?subject=' + subject + '&body=' + body;
      status.textContent = 'Mail client opening. Thank you.';
      status.style.color = '#4A5157';
    });
  }
})();
