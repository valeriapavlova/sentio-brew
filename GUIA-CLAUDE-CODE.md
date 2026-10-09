# Інструкція: як викласти сайт на GitHub і доробляти його в Claude Code

## 1. Викласти сайт на GitHub Pages (≈10 хв, без терміналу)

1. Розпакуй `sentio-brew.zip`.
2. На github.com натисни **New repository**:
   - назва `sentio-brew`;
   - **Public** (безкоштовний GitHub Pages працює з публічними репозиторіями);
   - README не додавай.
3. На сторінці порожнього репозиторію натисни **uploading an existing file**. Перетягни **весь вміст** розпакованої папки (`assets`, `docs`, `src`, `build.py`, `README.md`, `CLAUDE.md`, цей файл, `.gitignore`) → **Commit changes**.
   Якщо GitHub не прийме все одразу, завантаж спочатку `docs`, потім решту.
4. Відкрий **Settings → Pages**:
   - Source: **Deploy from a branch**;
   - Branch: **main**, папка **/docs** → **Save**.
5. За 1–2 хвилини сайт буде тут: `https://valeriapavlova.github.io/sentio-brew/`

**Власний домен** (наприклад `sentiobrew.va-pavlova.com`):

- у Settings → Pages впиши домен у **Custom domain**;
- у DNS свого хостингу додай запис `CNAME sentiobrew → valeriapavlova.github.io`;
- у `build.py` зміни `SITE_PATH = "/"` і перегенеруй сайт.

## 2. Доробляти сайт у Claude Code

1. Встанови Claude Code: https://docs.claude.com/en/docs/claude-code (потрібні Node.js 18+ і Python 3).
2. Клонуй репозиторій і відкрий його:
   ```bash
   git clone https://github.com/valeriapavlova/sentio-brew.git
   cd sentio-brew
   pip install jinja2
   claude
   ```
3. Claude Code сам прочитає `CLAUDE.md`, де описано правила проєкту: дизайн-система, без health claims, мінімум 16 px, без `!important`.
4. Після змін: `python3 build.py` → `git add -A && git commit -m "..." && git push`. Pages оновиться сам.

## 3. Готові промти для Claude Code

**Перевірити, що все працює**

```
Genera el sitio con python3 build.py, levanta un servidor local y revisa todas las páginas en 1440 px y 390 px con Playwright. Busca enlaces rotos, textos cortados, solapamientos y errores en la consola. Arregla lo que encuentres en src/ o assets/, no en docs/.
```

**Додати нову статтю в блог** (текст бери з WordPress або з Notion)

```
Añade el artículo «<título>» al blog. Copia la estructura de src/templates/articulo-te-verde.html: índice lateral, secciones con h2/h3, bloque CTA al test y artículos relacionados. El texto es este: <pega el texto>. Marca el post como live=True en src/data.py, pon una meta description de máx. 155 caracteres y no añadas promesas de salud.
```

**Додати фічу інгредієнта** (як Ashwagandha)

```
Crea la ficha de ingrediente de <Rooibos> copiando src/templates/ficha-ashwagandha.html. Contenido: <texto>. Enlázala desde las tarjetas de ingrediente (src/data.py → INGREDIENTS y las tiles de BLEND_PAGES) en lugar de «Ficha próximamente».
```

**Підключити справжню Google Analytics**

```
Activa Google Analytics 4 con el ID G-XXXXXXX en assets/js/main.js (GA_ID). Comprueba que solo se carga después de aceptar las cookies y que al rechazar no se crea ninguna cookie _ga.
```

**Перевірка доступності**

```
Haz una auditoría WCAG 2.1 AA de todo el sitio con axe-core y Playwright. Corrige contraste, etiquetas, orden de encabezados y foco. Respeta los tokens de assets/css/styles.css.
```

**Узгодити з Figma після змін у дизайні** (потрібен Figma MCP у Claude Code)

```
Compara la página <Home> de Figma (archivo DBPynbVPOYXiH8CcLUsuVA) con docs/index.html. Lista las diferencias de espaciado, tipografía y contenido, y aplica solo las que yo confirme.
```

## 4. Що варто знати

- `docs/` генерується автоматично. Редагуй `src/` і `assets/`, потім запускай `build.py`.
- Тексти лежать у `src/data.py` (бленди, плани, пости, питання тесту) і в шаблонах сторінок.
- Тест рахує 450 г на місяць між трьома блендами (`assets/js/test.js`). Якщо відмічено вагітність або ліки, Serenity не включається.
- Cookie-банер працює, але GA не завантажується, поки `GA_ID` порожній. Юридичні тексти описують варіант «з GA».
