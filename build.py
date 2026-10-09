#!/usr/bin/env python3
"""Genera el sitio estático de Sentio Brew en /docs (GitHub Pages).

Uso:  python3 build.py
Requisitos: Python 3.9+ y Jinja2  (pip install jinja2)
"""
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT / "docs"
# Ruta pública del sitio en GitHub Pages (usuario.github.io/sentio-brew/). Si usas dominio propio, pon "/".
SITE_PATH = "/sentio-brew/"
sys.path.insert(0, str(SRC))
import data as D  # noqa: E402

env = Environment(loader=FileSystemLoader(SRC / "templates"), undefined=StrictUndefined,
                  trim_blocks=True, lstrip_blocks=True, autoescape=True)

COMMON = dict(nav=D.NAV, footer_cols=D.FOOTER_COLS, plans=D.PLANS, blends=D.BLENDS, blend_order=D.BLEND_ORDER,
              posts=D.POSTS, post_by_slug=D.POST_BY_SLUG, ingredients=D.INGREDIENTS, others=D.OTHER_INGREDIENTS,
              home=False, hide_test_cta=False, current=None)

EMAIL = '<a href="mailto:info@sentiobrew.com">info@sentiobrew.com</a>'
LEGAL = {
    "aviso-legal": dict(
        crumb="Aviso legal", h1="Aviso legal", title="Aviso legal",
        meta="Aviso legal de Sentio Brew, proyecto académico del Máster en Diseño Web, UX/UI y Marketing Digital de CEI Valencia.",
        lead="Según la Ley 34/2002 de servicios de la sociedad de la información (LSSI-CE), te contamos quién está detrás de esta web y en qué condiciones puedes usarla.",
        others=[("Política de privacidad", "privacidad/"), ("Política de cookies", "cookies/")],
        sections=[
            dict(h="Quién está detrás de esta web", short="Titular", blocks=[
                "Sentio Brew es una marca ficticia creada como proyecto final del Máster Profesional en Diseño Web, UX/UI y Marketing Digital de CEI Valencia. La web no tiene actividad comercial: los productos no están a la venta y no se hacen pedidos ni cobros.",
                {"list": ["Titular y autora del proyecto: Valeriia Pavlova.", "Domicilio: Valencia, España.", "Web: sentiobrew.va-pavlova.com.", "Contacto: " + EMAIL + "."]},
                "Al ser un proyecto académico sin actividad económica, no constan NIF ni inscripción en el Registro Mercantil."]),
            dict(h="Uso de la web", short=None, blocks=[
                "Puedes navegar por la web libremente. Al hacerlo, te comprometes a usarla de forma lícita y a no dañar su funcionamiento ni el de los sistemas que la alojan.",
                "El test de bienestar, la suscripción y el pack regalo son prototipos de diseño: puedes probarlos, pero no envían ni guardan los datos que escribas."]),
            dict(h="Contenido informativo", short=None, blocks=[
                "Los textos sobre ingredientes, blends y bienestar son divulgativos. Hablamos de alimentos e infusiones, no de medicamentos: no sustituyen el consejo de un profesional de la salud.",
                "Citamos las fuentes que usamos, como el NCCIH. Los datos de mercado, keywords y competencia del proyecto son reales; los precios, lotes y datos de producto son de ejemplo."]),
            dict(h="Propiedad intelectual", short=None, blocks=[
                "El diseño, los textos, la identidad visual y el código de Sentio Brew son de su autora. Algunas imágenes se han generado con inteligencia artificial y se detallan en el anexo del proyecto.",
                "No está permitido usar estos contenidos con fines comerciales sin permiso. Puedes compartirlos citando la fuente. Las marcas de terceros que aparecen pertenecen a sus titulares."]),
            dict(h="Enlaces a otras webs", short="Enlaces externos", blocks=[
                "Algunos artículos enlazan a webs externas para ampliar información. No controlamos su contenido ni respondemos de él: al pulsar el enlace, sales de Sentio Brew."]),
            dict(h="Responsabilidad", short=None, blocks=[
                "Revisamos la información para que sea correcta y esté al día, pero puede contener errores. No respondemos de los daños causados por un uso de la web contrario a este aviso ni de cortes técnicos ajenos a nosotros."]),
            dict(h="Ley aplicable", short=None, blocks=[
                "Este aviso se rige por la legislación española. Si surge un conflicto, se resolverá ante los juzgados que correspondan por ley; si actúas como consumidor, los de tu domicilio."]),
        ]),
    "privacidad": dict(
        crumb="Privacidad", h1="Política de privacidad", title="Política de privacidad",
        meta="Qué datos trata la web de Sentio Brew, para qué y qué derechos tienes, según el RGPD y la LOPDGDD.",
        lead="Tus datos son tuyos. Aquí te explicamos qué datos trata esta web, para qué y qué derechos tienes, según el RGPD y la Ley Orgánica 3/2018 (LOPDGDD).",
        others=[("Aviso legal", "aviso-legal/"), ("Política de cookies", "cookies/")],
        sections=[
            dict(h="Responsable del tratamiento", short="Responsable", blocks=[
                {"list": ["Responsable: Valeriia Pavlova, autora del proyecto Sentio Brew.", "Domicilio: Valencia, España.", "Contacto para privacidad: " + EMAIL + "."]}]),
            dict(h="Qué datos tratamos", short=None, blocks=[
                "Esta web es un prototipo académico, así que trata los mínimos datos posibles:",
                {"list": ["Formularios (test, suscripción, pack regalo y newsletter): no envían ni guardan tus respuestas. El resultado del test solo se guarda en tu navegador mientras la pestaña está abierta.",
                          "Datos técnicos: el servidor registra datos básicos de conexión, como la IP y el navegador, por seguridad.",
                          "Analítica: solo si aceptas las cookies de analítica, datos de uso seudonimizados (páginas vistas, dispositivo y país)."]}]),
            dict(h="Para qué y con qué base legal", short="Finalidad y base legal", blocks=[
                {"list": ["Mantener la web segura y funcionando: interés legítimo (art. 6.1.f RGPD).",
                          "Saber qué contenidos se leen para mejorar la web: tu consentimiento (art. 6.1.a RGPD), que puedes retirar cuando quieras."]},
                "No tomamos decisiones automatizadas ni creamos perfiles con tus datos."]),
            dict(h="Cuánto tiempo los guardamos", short="Conservación", blocks=[
                "Los registros técnicos, el tiempo mínimo que fija el proveedor de alojamiento por seguridad. Los datos de analítica, 14 meses como máximo. Tu elección sobre cookies, 12 meses."]),
            dict(h="Quién más puede verlos", short="Destinatarios", blocks=[
                "No vendemos ni cedemos tus datos. Solo acceden los proveedores que nos dan servicio, como encargados del tratamiento: el alojamiento web y, si aceptas, Google Analytics.",
                "Google puede tratar datos fuera del Espacio Económico Europeo. Lo hace con las garantías del Marco de Privacidad de Datos UE-EE. UU. y las cláusulas contractuales tipo de la Comisión Europea."]),
            dict(h="Tus derechos", short=None, blocks=[
                "Puedes pedir en cualquier momento acceder a tus datos, corregirlos, borrarlos, oponerte a su uso, limitarlo o llevarlos a otro servicio. Escríbenos a " + EMAIL + " e indica qué derecho quieres ejercer.",
                'Si crees que no hemos tratado bien tus datos, puedes reclamar ante la Agencia Española de Protección de Datos en <a href="https://www.aepd.es" target="_blank" rel="noopener">aepd.es</a>.']),
            dict(h="Cambios en esta política", short="Cambios", blocks=[
                "Si cambiamos algo importante, lo verás aquí con la nueva fecha de actualización."]),
        ]),
    "cookies": dict(
        crumb="Cookies", h1="Política de cookies", title="Política de cookies",
        meta="Qué cookies usa la web de Sentio Brew y cómo aceptarlas, rechazarlas o cambiar de opinión.",
        lead="Usamos las cookies justas. Las necesarias hacen que la web funcione; las de analítica, solo si tú lo aceptas. Puedes cambiar de opinión cuando quieras.",
        others=[("Aviso legal", "aviso-legal/"), ("Política de privacidad", "privacidad/")],
        sections=[
            dict(h="Qué es una cookie", short=None, blocks=[
                "Es un pequeño archivo que la web guarda en tu navegador para recordar información entre visitas, como tu elección sobre las cookies."]),
            dict(h="Qué cookies usamos", short=None, blocks=[
                {"table": {"cols": ["Cookie", "Titular", "Finalidad", "Duración"], "rows": [
                    ["sb_consent", "Sentio Brew", "Necesaria. Guarda si aceptas o rechazas las cookies.", "12 meses"],
                    ["_ga", "Google", "Analítica. Distingue visitas sin identificarte.", "2 años"],
                    ["_ga_<ID>", "Google", "Analítica. Mantiene el estado de la sesión.", "2 años"]]}},
                "Las cookies necesarias no requieren tu consentimiento (art. 22.2 LSSI-CE). Las de analítica solo se activan si las aceptas."]),
            dict(h="Cómo aceptarlas, rechazarlas o cambiar de opinión", short="Gestionar tus cookies", blocks=[
                "En tu primera visita verás un aviso con tres opciones: aceptar, rechazar o configurar. Rechazar es tan fácil como aceptar.",
                {"button": "Configurar cookies"},
                "También puedes cambiar tu elección desde «Configurar cookies», en el pie de página, o borrarlas y bloquearlas desde los ajustes de tu navegador:",
                {"list": ["Chrome: Configuración › Privacidad y seguridad.", "Safari: Ajustes › Privacidad.", "Firefox: Ajustes › Privacidad y seguridad.", "Edge: Configuración › Cookies y permisos del sitio."]}]),
            dict(h="Cambios en esta política", short="Cambios", blocks=[
                "Si añadimos o quitamos cookies, actualizaremos esta tabla y te volveremos a preguntar."]),
        ]),
}


def render(template, path, **ctx):
    depth = path.count("/") if path else 0
    out_file = OUT / path / "index.html" if path else OUT / "index.html"
    base = "../" * depth
    if path.endswith(".html"):
        out_file, base = OUT / path, SITE_PATH
    out_file.parent.mkdir(parents=True, exist_ok=True)
    context = dict(COMMON, base=base, **ctx)
    out_file.write_text(env.get_template(template).render(**context), encoding="utf-8")
    print("  ✓", out_file.relative_to(ROOT))


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("")

    render("home.html", "", home=True, title="Sentio Brew · Café de especialidad e infusiones por suscripción",
           meta="Un blend para cada momento del día: Focus, Euphoria y Serenity. Haz el test de 2 minutos y recibe tu caja ajustada a cómo te sientes.")

    for key in D.BLEND_ORDER:
        b = D.BLENDS[key]
        p = D.BLEND_PAGES[key]
        render("blend.html", b["url"].rstrip("/") + "/", blend=b, page=p, title=p["title"], meta=p["meta"])

    render("test.html", "test/", hide_test_cta=True, questions=D.QUESTIONS, last=D.LAST_QUESTION,
           title="Test de bienestar", meta="Ocho preguntas sobre tu día para ajustar tu caja de Focus, Euphoria y Serenity. 2 minutos, sin registro ni datos biométricos.")
    render("suscripcion.html", "suscripcion/", current="suscripcion/", title="Suscripción · Elige tu caja",
           meta="Caja Degustación, Caja Ritual o Pack Regalo: los tres blends ajustados con tu test. Sin permanencia y con envío incluido.")
    render("regalo.html", "pack-regalo/", current="pack-regalo/", title="Pack Regalo de Navidad",
           meta="Regala tres meses de pausas: tres Cajas Ritual, una al mes, con tarjeta personalizada. 99 €, sin renovación automática.")
    render("blog.html", "blog/", current="blog/", title="Blog · Lo que hay detrás de cada taza",
           meta="Café, infusiones y rutinas para días con muchas pantallas. Sin promesas milagro: con fuentes.")
    for post in D.POSTS:
        if post.get("live"):
            render("articulo-te-verde.html", f"blog/{post['slug']}/", current="blog/",
                   title="Beneficios del té verde: propiedades, cafeína y cómo tomarlo",
                   meta="Qué es el té verde, qué propiedades se le atribuyen, cuánta cafeína tiene, contraindicaciones y cómo prepararlo para que no amargue.")
        else:
            render("articulo-pronto.html", f"blog/{post['slug']}/", current="blog/", post=post,
                   title=post["title"], meta=post["title"] + " · Próximamente en el blog de Sentio Brew.")
    render("ingredientes.html", "ingredientes/", current="ingredientes/", title="Ingredientes · Qué hay en cada taza",
           meta="Las plantas, hojas y raíces de los blends de Sentio Brew: qué son, cómo se toman y sus precauciones. Sin promesas de salud.")
    render("ficha-ashwagandha.html", "ingredientes/ashwagandha/", current="ingredientes/",
           title="Ashwagandha: qué es, propiedades y cómo tomarla",
           meta="Qué es la ashwagandha, sus propiedades, contraindicaciones y cómo tomarla en infusión. Descubre los blends de Sentio Brew que la contienen.")
    render("cafe.html", "nuestro-cafe/", title="Nuestro café · Café de especialidad",
           meta="El café de Focus es 100 % arábica de especialidad, tostado para filtro. Qué significa y cómo lo elegimos.")
    for slug, legal in LEGAL.items():
        render("legal.html", slug + "/", legal=legal, title=legal["title"], meta=legal["meta"])
    render("404.html", "404.html", title="Página no encontrada", meta="Esta página no existe.")
    print("Listo →", OUT)


if __name__ == "__main__":
    main()
