# Sentio Brew · contexto para Claude Code

Web estática del proyecto académico Sentio Brew (marca ficticia, CEI Valencia). Autora: Valeriia Pavlova.
Diseño de origen en Figma: archivo `DBPynbVPOYXiH8CcLUsuVA`, páginas «12 · Web · Home» … «21 · Web · Legal» y componentes en «11 · Web · Components».

## Cómo está hecho
- HTML/CSS/JS sin frameworks. Plantillas Jinja2 en `src/templates`, textos en `src/data.py`.
- `python3 build.py` genera `/docs` (lo publica GitHub Pages). Nunca edites `/docs` a mano: edita `src/` o `assets/` y vuelve a generar.
- `assets/css/styles.css` es el sistema de diseño. Usa siempre sus tokens (`--paper`, `--ink`, `--s-24`, `--radius-md`…) y las clases de texto `t-*`; no metas colores ni tamaños sueltos.
- Componentes = macros en `src/templates/macros.html` (blend_card, plan_card, post_card, ing_card, step, test_preview, faq, cta_test). Reutilízalos antes de crear markup nuevo.

## Reglas del proyecto
- Idioma del sitio: español de España. Tono cercano y directo, sin promesas de salud (Reglamento CE 1924/2006): «se le atribuye», «uso tradicional», nunca «cura», «mejora el sueño», etc.
- Cantidades honestas: la Caja Ritual son 450 g al mes repartidos según el test; no inventes gramos fijos.
- Tipografía: mínimo 16 px (14 px solo en el footer y eyebrows); line-height múltiplo de 4.
- Accesibilidad AA: contraste, foco visible, teclado, `alt` en imágenes con contenido.
- Evita `!important`; resuelve con especificidad.
- Es un proyecto académico: los formularios no envían datos y no hay pagos. Mantén los avisos.
- Cookies: rechazar debe ser tan fácil como aceptar (Guía AEPD). Analítica solo con consentimiento y si `GA_ID` tiene valor.

## Comprobar antes de terminar
1. `python3 build.py` sin errores.
2. `python3 -m http.server -d docs 8000` y revisar en 1440 px y 390 px.
3. Que no haya enlaces rotos ni textos en inglés.
