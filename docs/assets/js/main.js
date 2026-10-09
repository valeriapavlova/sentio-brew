/* Sentio Brew · interacciones comunes */
(function () {
  'use strict';

  /* ---------- Menú móvil ---------- */
  var toggle = document.querySelector('.menu-toggle');
  var menu = document.getElementById('mobile-menu');
  function setMenu(open) {
    if (!menu) return;
    menu.hidden = !open;
    menu.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    if (open) { var first = menu.querySelector('nav a'); if (first) first.focus(); } else { toggle.focus(); }
  }
  if (toggle && menu) {
    toggle.addEventListener('click', function () { setMenu(true); });
    menu.querySelector('.mobile-menu__close').addEventListener('click', function () { setMenu(false); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) setMenu(false); });
  }

  /* ---------- Vista previa del test (chips) ---------- */
  document.querySelectorAll('[data-test-preview]').forEach(function (box) {
    var chips = box.querySelectorAll('[data-preview]');
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c === chip)); });
        box.querySelector('[data-preview-eyebrow]').textContent = chip.dataset.eyebrow;
        box.querySelector('[data-preview-name]').textContent = chip.dataset.name;
        box.querySelector('[data-preview-text]').textContent = chip.dataset.text;
        box.querySelector('[data-preview-img]').src = chip.dataset.img;
      });
    });
  });

  /* ---------- Carrusel del blog ---------- */
  document.querySelectorAll('[data-carousel]').forEach(function (wrap) {
    var track = wrap.querySelector('[data-carousel-track]');
    var prev = wrap.querySelector('[data-carousel-prev]');
    var next = wrap.querySelector('[data-carousel-next]');
    function step() { var card = track.firstElementChild; return card ? card.getBoundingClientRect().width + 32 : 400; }
    function update() {
      var max = track.scrollWidth - track.clientWidth - 2;
      prev.disabled = track.scrollLeft <= 2;
      next.disabled = track.scrollLeft >= max;
    }
    prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
    next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: 'smooth' }); });
    track.addEventListener('scroll', function () { window.requestAnimationFrame(update); }, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  /* ---------- Filtros (blog, ingredientes) ---------- */
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var name = group.dataset.filterGroup;
    var target = document.querySelector('[data-filter-target="' + name + '"]');
    if (!target) return;
    var buttons = group.querySelectorAll('[data-filter]');
    var empty = target.parentElement.querySelector('[data-filter-empty]');
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var value = btn.dataset.filter;
        buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
        var visible = 0;
        target.querySelectorAll('[data-tone]').forEach(function (item) {
          var show = value === 'all' || item.dataset.tone === value;
          item.hidden = !show;
          if (show) visible++;
        });
        if (empty) empty.hidden = visible > 0;
      });
    });
  });

  /* ---------- Índice activo (artículo, fichas, legal) ---------- */
  var toc = document.querySelector('[data-toc]');
  if (toc && 'IntersectionObserver' in window) {
    var links = Array.prototype.slice.call(toc.querySelectorAll('a[href^="#"]'));
    var map = {};
    links.forEach(function (a) { var el = document.querySelector(a.getAttribute('href')); if (el) map[el.id] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && map[en.target.id]) {
          links.forEach(function (a) { a.classList.remove('is-active'); });
          map[en.target.id].classList.add('is-active');
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });
    Object.keys(map).forEach(function (id) { io.observe(document.getElementById(id)); });
    if (links[0]) links[0].classList.add('is-active');
  }

  /* ---------- Newsletter (demo) ---------- */
  document.querySelectorAll('[data-newsletter]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = form.querySelector('input[type="email"]');
      if (!input.checkValidity()) { input.reportValidity(); return; }
      form.querySelector('[data-newsletter-note]').hidden = false;
      input.value = '';
    });
  });

  /* ---------- Suscripción: selección de caja + resumen ---------- */
  var subForm = document.querySelector('[data-sub-form]');
  if (subForm) {
    var PLANS = {
      degustacion: { title: 'Caja Degustación', line: 'Caja Degustación · 3 × 50 g', price: '19,00 €', total: '19 €' },
      ritual: { title: 'Caja Ritual', line: 'Caja Ritual · 450 g', price: '36,00 €', total: '36 €' },
      regalo: { title: 'Pack Regalo', line: 'Pack Regalo · 3 cajas', price: '99,00 €', total: '99 €' }
    };
    var after = 'ritual';
    var afterBox = document.querySelector('[data-after]');
    var order = document.querySelector('[data-order]');
    function render() {
      var checked = subForm.querySelector('input[name="plan"]:checked');
      var key = checked ? checked.value : 'degustacion';
      var p = PLANS[key];
      order.querySelector('#order-title').textContent = p.title;
      order.querySelector('[data-order-line]').textContent = p.line;
      order.querySelector('[data-order-line-price]').textContent = p.price;
      order.querySelector('[data-order-total]').textContent = p.total;
      var afterRow = order.querySelector('[data-order-after-row]');
      afterBox.hidden = key !== 'degustacion';
      if (key === 'degustacion') {
        afterRow.hidden = false;
        order.querySelector('[data-order-after]').textContent = after === 'ritual' ? 'Caja Ritual · 36 €/mes' : 'Nada más';
      } else if (key === 'ritual') {
        afterRow.hidden = false;
        order.querySelector('[data-order-after]').textContent = '36 €/mes · cancela cuando quieras';
      } else {
        afterRow.hidden = false;
        order.querySelector('[data-order-after]').textContent = 'Sin renovación automática';
      }
      subForm.querySelectorAll('label.plan-card').forEach(function (l) {
        var on = l.querySelector('input').checked;
        var b = l.querySelector('.btn');
        b.textContent = on ? 'Elegida ✓' : 'Elegir';
        b.classList.toggle('btn--solid', on);
        b.classList.toggle('btn--outline', !on);
      });
    }
    subForm.addEventListener('change', render);
    document.querySelectorAll('[data-after-option]').forEach(function (b, _, all) {
      b.addEventListener('click', function () {
        after = b.dataset.afterOption;
        all.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        render();
      });
    });
    var pay = document.querySelector('[data-pay]');
    pay.addEventListener('click', function () { document.querySelector('[data-pay-note]').hidden = false; });
    // Resultado del test guardado en esta sesión
    try {
      var saved = JSON.parse(sessionStorage.getItem('sb_test') || 'null');
      if (saved && saved.grams) {
        ['focus', 'euphoria', 'serenity'].forEach(function (k) {
          var el = document.querySelector('[data-g="' + k + '"]');
          var name = k.charAt(0).toUpperCase() + k.slice(1);
          if (el) el.textContent = name + ' ' + saved.grams[k] + ' g';
          if (el && saved.grams[k] === 0) el.parentElement.hidden = true;
        });
      } else {
        var lbl = document.querySelector('[data-sub-result-label]');
        if (lbl) lbl.textContent = 'Ejemplo de resultado del test';
        var edit = document.querySelector('[data-sub-edit]');
        if (edit) edit.textContent = 'Hacer el test';
      }
    } catch (e) { /* sin almacenamiento: se queda el ejemplo */ }
    render();
  }

  /* ---------- Pack Regalo: vista previa de la tarjeta ---------- */
  var gift = document.querySelector('[data-gift-form]');
  if (gift) {
    var to = gift.querySelector('#g-to'), from = gift.querySelector('#g-from'), msg = gift.querySelector('#g-msg');
    var count = gift.querySelector('[data-count]');
    function upd() {
      document.querySelector('[data-preview-to]').textContent = to.value.trim() || '…';
      document.querySelector('[data-preview-from]').textContent = from.value.trim() || '…';
      document.querySelector('[data-preview-msg]').textContent = msg.value.trim() || 'Tu mensaje aparecerá aquí.';
      count.textContent = msg.value.length + ' / 200';
    }
    [to, from, msg].forEach(function (el) { el.addEventListener('input', upd); });
    gift.addEventListener('submit', function (e) { e.preventDefault(); gift.querySelector('[data-gift-note]').hidden = false; });
    upd();
  }

  /* ---------- Cookies (Guía AEPD: rechazar tan fácil como aceptar) ---------- */
  var GA_ID = ''; // p. ej. 'G-XXXXXXX'. Vacío = no se carga ningún script de analítica.
  var COOKIE = 'sb_consent';
  var banner = document.getElementById('cookie-banner');
  var modal = document.getElementById('cookie-modal');
  var analyticsSwitch = document.getElementById('cookie-analytics');
  var lastFocus = null;

  function readConsent() {
    var m = document.cookie.match(new RegExp('(?:^|; )' + COOKIE + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }
  function writeConsent(value) {
    var maxAge = 60 * 60 * 24 * 365; // 12 meses
    document.cookie = COOKIE + '=' + encodeURIComponent(value) + '; max-age=' + maxAge + '; path=/; SameSite=Lax' + (location.protocol === 'https:' ? '; Secure' : '');
  }
  function loadAnalytics() {
    if (!GA_ID || window.__sbGA) return;
    window.__sbGA = true;
    var s = document.createElement('script');
    s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { anonymize_ip: true });
  }
  function apply(value) {
    writeConsent(value);
    if (banner) banner.hidden = true;
    closeModal();
    if (value === 'analytics') loadAnalytics();
  }
  function openModal() {
    lastFocus = document.activeElement;
    analyticsSwitch.checked = readConsent() === 'analytics';
    modal.hidden = false;
    modal.querySelector('.cookie-modal__close').focus();
  }
  function closeModal() {
    if (!modal || modal.hidden) return;
    modal.hidden = true;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  if (banner && modal) {
    var current = readConsent();
    if (!current) banner.hidden = false;
    else if (current === 'analytics') loadAnalytics();
    document.querySelectorAll('[data-cookie]').forEach(function (b) {
      b.addEventListener('click', function () {
        var a = b.dataset.cookie;
        if (a === 'accept') apply('analytics');
        else if (a === 'reject') apply('necessary');
        else apply(analyticsSwitch.checked ? 'analytics' : 'necessary');
      });
    });
    document.querySelectorAll('[data-cookie-settings]').forEach(function (b) { b.addEventListener('click', openModal); });
    document.querySelectorAll('[data-cookie-close]').forEach(function (b) { b.addEventListener('click', closeModal); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeModal(); });
  }
})();
