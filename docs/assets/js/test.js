/* Sentio Brew · Test de bienestar
   Reparte 450 g al mes entre Focus, Euphoria y Serenity según las respuestas.
   No se envía nada: el resultado solo se guarda en esta pestaña (sessionStorage). */
(function () {
  'use strict';
  var root = document.querySelector('[data-quiz]');
  if (!root) return;

  var intro = root.querySelector('[data-step="intro"]');
  var form = root.querySelector('[data-quiz-form]');
  var steps = Array.prototype.slice.call(form.querySelectorAll('.quiz__col[data-step]'));
  var result = root.querySelector('[data-step="result"]');
  var current = -1;
  var MONTHS = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
  var TOTAL = 450, STEP = 50;

  function show(index) {
    intro.hidden = index !== -1;
    form.hidden = index < 0 || index >= steps.length;
    result.hidden = index !== steps.length;
    steps.forEach(function (s, i) { s.hidden = i !== index; });
    current = index;
    window.scrollTo({ top: 0, behavior: 'auto' });
    var focusTarget = index === -1 ? intro.querySelector('h1') : index === steps.length ? result : steps[index].querySelector('h2');
    if (focusTarget) { focusTarget.setAttribute('tabindex', '-1'); focusTarget.focus({ preventScroll: true }); }
  }

  function answered(fs) { return !!fs.querySelector('input:checked'); }
  function syncNext(fs) { var next = fs.querySelector('[data-quiz-next]'); if (next) next.disabled = !answered(fs); }

  steps.forEach(function (fs, i) {
    fs.addEventListener('change', function (e) {
      // Última pregunta: «Nada de esto» es excluyente
      if (e.target.name === 'q8') {
        var boxes = fs.querySelectorAll('input[name="q8"]');
        if (e.target.value === 'nada' && e.target.checked) boxes.forEach(function (b) { if (b !== e.target) b.checked = false; });
        if (e.target.value !== 'nada' && e.target.checked) fs.querySelector('input[value="nada"]').checked = false;
        updateNotice(fs);
      }
      syncNext(fs);
    });
    var back = fs.querySelector('[data-quiz-back]');
    back.addEventListener('click', function () { show(i - 1); });
    var next = fs.querySelector('[data-quiz-next]');
    if (next.type === 'button') next.addEventListener('click', function () { if (answered(fs)) show(i + 1); });
  });

  function updateNotice(fs) {
    var notice = fs.querySelector('[data-quiz-notice]');
    var labels = { embarazo: 'Embarazo o lactancia', medicacion: 'Tomo medicación', cafeina: 'Soy sensible a la cafeína' };
    var picked = Array.prototype.slice.call(fs.querySelectorAll('input[name="q8"]:checked')).map(function (b) { return b.value; }).filter(function (v) { return v !== 'nada'; });
    notice.hidden = picked.length === 0;
    if (picked.length) notice.querySelector('[data-quiz-notice-title]').textContent = 'Has marcado «' + picked.map(function (v) { return labels[v]; }).join('», «') + '»';
  }

  function compute() {
    var score = { focus: 1, euphoria: 1, serenity: 1 };
    form.querySelectorAll('input[type="radio"]:checked').forEach(function (input) {
      var s = JSON.parse(input.dataset.score || '{}');
      Object.keys(s).forEach(function (k) { score[k] += s[k]; });
    });
    var flags = Array.prototype.slice.call(form.querySelectorAll('input[name="q8"]:checked')).map(function (b) { return b.value; });
    var noSerenity = flags.indexOf('embarazo') > -1 || flags.indexOf('medicacion') > -1;
    if (noSerenity) score.serenity = 0;
    var keys = ['focus', 'euphoria', 'serenity'].filter(function (k) { return score[k] > 0; });
    var sum = keys.reduce(function (a, k) { return a + score[k]; }, 0);
    var grams = { focus: 0, euphoria: 0, serenity: 0 };
    // mínimo 50 g por blend incluido y el resto proporcional, en pasos de 50 g
    var rest = TOTAL - STEP * keys.length;
    keys.forEach(function (k) { grams[k] = STEP + Math.floor((rest * score[k] / sum) / STEP) * STEP; });
    var used = keys.reduce(function (a, k) { return a + grams[k]; }, 0);
    var order = keys.slice().sort(function (a, b) { return score[b] - score[a]; });
    var j = 0;
    while (used < TOTAL) { grams[order[j % order.length]] += STEP; used += STEP; j++; }
    return { grams: grams, flags: flags, noSerenity: noSerenity, top: order[0] };
  }

  var REASONS = {
    focus: ['Mañana · concentración · Te cuesta arrancar a primera hora.', 'Mañana · concentración · Un café para empezar el día.'],
    euphoria: ['Mediodía · energía · Bajón después de comer, sin otro café.', 'Mediodía · energía · Para la segunda mitad del día.'],
    serenity: ['Noche · desconexión · Te cuesta desconectar de la pantalla.', 'Noche · desconexión · Una pausa sin teína para cerrar el día.']
  };
  var SUMMARY = {
    focus: 'Tu día pide más foco por la mañana. Así reparte tu caja los tres blends.',
    euphoria: 'Tu día pide energía a mediodía, sin sumar otro café. Así reparte tu caja los tres blends.',
    serenity: 'Tu día pide una pausa sin cafeína por la noche. Así reparte tu caja los tres blends.'
  };

  function renderResult(r) {
    var now = new Date();
    var month = MONTHS[(now.getMonth() + 1) % 12];
    result.querySelector('#result-title').textContent = 'Tu caja de ' + month;
    var summary = SUMMARY[r.top];
    if (r.noSerenity) summary = 'Como has marcado embarazo, lactancia o medicación, tu caja no lleva Serenity (ashwagandha y valeriana). Así se reparten los otros dos blends.';
    if (r.flags.indexOf('cafeina') > -1) summary += ' Toma Focus antes de las 14:00 y Euphoria antes de las 17:00.';
    result.querySelector('[data-result-summary]').textContent = summary;
    ['focus', 'euphoria', 'serenity'].forEach(function (k) {
      var row = result.querySelector('[data-result-row="' + k + '"]');
      var g = r.grams[k];
      row.querySelector('[data-grams]').textContent = g ? g + ' g' : 'No incluido';
      row.querySelector('[data-meter]').style.width = Math.min(100, Math.round(g / 270 * 100)) + '%';
      row.querySelector('[data-reason]').textContent = g ? REASONS[k][k === r.top ? 0 : 1] : 'No lo incluimos por lo que has marcado en la última pregunta.';
      row.style.opacity = g ? '' : '0.5';
    });
    try { sessionStorage.setItem('sb_test', JSON.stringify({ grams: r.grams })); } catch (e) { /* sin almacenamiento */ }
  }

  root.querySelector('[data-quiz-start]').addEventListener('click', function () { show(0); });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!answered(steps[steps.length - 1])) return;
    renderResult(compute());
    show(steps.length);
  });
  root.querySelector('[data-quiz-restart]').addEventListener('click', function () {
    form.reset();
    steps.forEach(syncNext);
    steps[steps.length - 1].querySelector('[data-quiz-notice]').hidden = true;
    show(0);
  });
  steps.forEach(syncNext);
})();
