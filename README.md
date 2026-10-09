# Sentio Brew · web

Web del proyecto final **Sentio Brew** (Máster en Diseño Web, UX/UI y Marketing Digital · CEI Valencia).
Marca ficticia: los productos no están a la venta y no se realiza ningún pago.

Diseño de origen: Figma, páginas 11–22 («Web · …»).

## Estructura

```
assets/          CSS, JS, fuentes e imágenes (fuente de verdad)
  css/styles.css   sistema de diseño: tokens, tipografía, componentes
  js/main.js       menú, filtros, carrusel, FAQ, suscripción, regalo, cookies
  js/test.js       lógica del test de bienestar (reparte 450 g entre los 3 blends)
src/
  data.py          textos y datos (blends, planes, posts, preguntas del test…)
  templates/       plantillas Jinja2 (base, macros = componentes, una por página)
build.py         genera el sitio estático en /docs
docs/            sitio generado → lo publica GitHub Pages (no editar a mano)
```

## Cómo editar

1. Cambia textos en `src/data.py` o en `src/templates/*.html`, estilos en `assets/css/styles.css`.
2. Genera el sitio: `pip install jinja2` (solo la primera vez) y `python3 build.py`.
3. Prueba en local: `python3 -m http.server -d docs 8000` → http://localhost:8000
4. Sube los cambios (`git add -A && git commit -m "…" && git push`). GitHub Pages se actualiza solo.

## Páginas

| Ruta | Página |
|---|---|
| `/` | Home |
| `/para-concentrarse/` `/energizantes/` `/para-dormir/` | Blends Focus, Euphoria, Serenity |
| `/test/` | Test de bienestar (intro, 8 preguntas, resultado) |
| `/suscripcion/` | Elige tu caja + pedido |
| `/pack-regalo/` | Pack Regalo con tarjeta personalizable |
| `/blog/` y `/blog/beneficios-te-verde/` | Blog y artículo (el resto, «en preparación») |
| `/ingredientes/` y `/ingredientes/ashwagandha/` | Hub de ingredientes y ficha |
| `/nuestro-cafe/` | Nuestro café |
| `/aviso-legal/` `/privacidad/` `/cookies/` | Páginas legales |

## Notas

- **Sistema de diseño**: los tokens de `styles.css` son las variables de Figma (Web · Color, Web · Layout) y las clases `t-*` son los estilos de texto (Desktop / Mobile a partir de 900 px).
- **Cookies**: banner de primera capa con «Rechazar» y «Aceptar» al mismo nivel (Guía AEPD 2023) y panel de preferencias. La elección se guarda en la cookie `sb_consent` (12 meses).
  Google Analytics solo se carga si aceptas **y** si pones un ID en `GA_ID` (`assets/js/main.js`). Por defecto está vacío, así que no se carga nada.
- **Fuentes**: Archivo Black e Inter autoalojadas (SIL Open Font License), sin llamadas a Google Fonts.
- **Datos**: los formularios no envían nada. El resultado del test se guarda solo en `sessionStorage` para mostrarlo en Suscripción.
- **Accesibilidad**: contraste AA, foco visible, navegación con teclado, `prefers-reduced-motion`, textos mínimos de 16 px (14 px en el footer).
- Si cambias el nombre del repositorio o usas dominio propio, actualiza `SITE_PATH` en `build.py` (solo afecta a la página 404).
