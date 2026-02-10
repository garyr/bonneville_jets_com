(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', open);
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });
})();

(function () {
  // Build email from parts so it isn’t in the HTML (reduces scraping/spam)
  var user = 'Bonnevillejets';
  var domain = 'gmail.com';
  var email = user + '\u0040' + domain;
  var links = document.querySelectorAll('.js-email');
  for (var i = 0; i < links.length; i++) {
    var a = links[i];
    a.href = 'mailto:' + email;
    a.textContent = email;
  }
})();
