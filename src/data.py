# -*- coding: utf-8 -*-
"""Contenido del sitio Sentio Brew (textos copiados del diseño en Figma)."""

NAV = [
    ("Blends", "#blends"),          # ancla en la Home
    ("Ingredientes", "ingredientes/"),
    ("Suscripción", "suscripcion/"),
    ("Pack Regalo", "pack-regalo/"),
    ("Blog", "blog/"),
]

FOOTER_COLS = [
    ("Tienda", [("Suscripción", "suscripcion/"), ("Caja Degustación", "suscripcion/#planes"), ("Pack Regalo", "pack-regalo/")]),
    ("Blends", [("Para concentrarse", "para-concentrarse/"), ("Energizantes", "energizantes/"), ("Para dormir", "para-dormir/"), ("Test de bienestar", "test/")]),
    ("Descubre", [("Ingredientes", "ingredientes/"), ("Nuestro café", "nuestro-cafe/"), ("Blog", "blog/")]),
]

PLANS = [
    dict(key="degustacion", featured=True, tag="Primer mes", title="Caja Degustación", price="19 €", period="envío incluido",
         features=["3 minis de 50 g: Focus, Euphoria y Serenity", "Test de bienestar incluido", "Envío incluido"],
         cta="Pide tu caja →", href="suscripcion/#planes"),
    dict(key="ritual", featured=False, tag="Suscripción", title="Caja Ritual", price="36 €", period="/ mes",
         features=["450 g al mes, repartidos según tu test", "Ajustada cada mes por tu test", "Cancela cuando quieras"],
         cta="Suscríbete", href="suscripcion/#planes"),
    dict(key="regalo", featured=False, tag="Navidad", title="Pack Regalo", price="99 €", period="3 meses",
         features=["3 Cajas Ritual, una al mes", "Tarjeta para quien lo recibe", "Ahorras 9 €"],
         cta="Regálalo", href="pack-regalo/"),
]

# ------------------------------------------------------------------ blends
BLENDS = {
    "focus": dict(
        key="focus", name="Focus", num="01", time="08:00", moment="Mañana · concentración", moment_short="mañana",
        tagline="Para las horas en que no puedes permitirte una distracción.",
        ingredients="café de especialidad · melena de león", prep="15 g · 93 °C · 4 min",
        url="para-concentrarse/", page_name="Para concentrarse", img="pouch-focus.webp",
        preview="Café de especialidad con melena de león para tus horas de trabajo profundo.",
        chip="Con foco",
    ),
    "euphoria": dict(
        key="euphoria", name="Euphoria", num="02", time="13:00", moment="Mediodía · energía", moment_short="mediodía",
        tagline="Para el punto medio del día, cuando todo pesa un poco más.",
        ingredients="yerba mate · guaraná", prep="3 g · 80 °C · 4 min",
        url="energizantes/", page_name="Energizantes", img="pouch-euphoria.webp",
        preview="Yerba mate y guaraná para el punto medio del día.",
        chip="Con energía",
    ),
    "serenity": dict(
        key="serenity", name="Serenity", num="03", time="21:00", moment="Noche · desconexión", moment_short="noche",
        tagline="Para cuando el cuerpo sigue trabajando y tú ya no.",
        ingredients="rooibos · manzanilla · ashwagandha · valeriana", prep="2 g · 95 °C · 6 min",
        url="para-dormir/", page_name="Para dormir", img="pouch-serenity.webp",
        preview="Rooibos, manzanilla, ashwagandha y valeriana, sin teína, para tu pausa de la noche.",
        chip="En calma",
    ),
}
BLEND_ORDER = ["focus", "euphoria", "serenity"]

BLEND_PAGES = {
    "focus": dict(
        title="Café para estudiar y concentrarte · Focus",
        meta="Focus: café de especialidad con melena de león para tus horas de concentración. Preparación, ingredientes y precauciones, sin letra pequeña.",
        eyebrow="Blend 01 · Mañana · Con cafeína", h1="Café para estudiar y concentrarte",
        lead="Focus es nuestro blend de mañana: café de especialidad con un toque de melena de león. Para las horas en que no puedes permitirte una distracción.",
        pills=["15 g · 93 °C · 4 min", "Cantidad según tu test", "Envío incluido"],
        what_title="Qué lleva Focus",
        what_text="Dos ingredientes y nada de relleno. Las proporciones están en el envase y aquí, sin letra pequeña.",
        tiles=[
            dict(fig="95 %", name="Café de especialidad", text="La base del blend. Arábica de especialidad tostado para filtro: tu primera taza del día, sin amargor de más.", link=("Nuestro café →", "nuestro-cafe/"), strip="#3b6cf6"),
            dict(fig="5 %", name="Melena de león", text="Hongo (Hericium erinaceus) en polvo, de sabor suave y terroso. Te contamos qué es y de dónde viene en su ficha.", link=("Ficha próximamente", None), strip="#4793f1"),
            dict(fig="100 %", name="Arábica", text="Sin robusta ni mezclas de relleno. El origen de cada lote está en «Nuestro café».", link=("Origen del lote →", "nuestro-cafe/#lote"), strip="#53b9eb"),
            dict(fig="250 g", name="Molido para filtro", text="Molienda media, pensada para filtro o prensa francesa: la que encaja con el ritual de 4 minutos.", link=("Cómo prepararlo →", "#ritual"), strip="#5fe0e6"),
        ],
        ritual=dict(eyebrow_card="Mañana · concentración",
                    rows=[("Dosis", "15 g por taza"), ("Agua", "93 °C"), ("Tiempo", "4 minutos"), ("Cafeína", "Sí · café")],
                    title="Tu ritual de las 08:00",
                    text="Prepáralo antes de abrir el portátil. Cuatro minutos para ti antes del primer correo.",
                    steps=[("Calienta el agua a 93 °C", "Si no tienes termómetro: deja reposar 1–2 minutos tras hervir."),
                           ("15 g por taza · 4 minutos", "Dos cucharadas colmadas, en filtro o prensa francesa."),
                           ("Antes de abrir el portátil", "Tómalo con calma antes de la primera tarea, no mientras respondes correos.")]),
        prec=dict(title="Antes de tomarlo",
                  intro="Lo mismo que pone en el dorso de la bolsa, sin letra pequeña. Focus lleva cafeína: léelo antes de tu primera taza.",
                  label_sub="Mañana · horas de concentración",
                  ingredients="Café de especialidad 100 % arábica (95 %), melena de león (Hericium erinaceus) en polvo (5 %).",
                  prep=[("15 g", "dosis"), ("250 ml", "agua"), ("93 °C", "temp."), ("4 min", "filtro")],
                  warnings=["Contiene cafeína.", "No recomendado para niños.", "No recomendado durante el embarazo ni la lactancia.", "Si eres sensible a la cafeína, mejor antes de las 14:00."],
                  foot_strong="Café, no un complemento.",
                  foot_small="Peso neto: 250 g · molido para filtro<br>Mezclado y envasado en Valencia (España)"),
        plans_title="Dónde encontrar Focus",
        plans_text="Focus viene en las tres cajas; la cantidad depende de tu test. Empieza por la Degustación y decide después.",
        cta_eyebrow="¿No sabes si Focus es para ti?",
        faq_link=("¿Quieres energía para la tarde sin otro café? ", "Ver Euphoria →", "energizantes/"),
        faqs=[("¿Cuánta cafeína tiene Focus?", "La de una taza de café de filtro. La melena de león no añade cafeína: el 95 % del blend es café de especialidad."),
              ("¿Cuándo es mejor tomarlo?", "Por la mañana, antes de empezar a trabajar o estudiar. Si eres sensible a la cafeína, evita tomarlo después de las 14:00."),
              ("¿Puedo prepararlo en cafetera italiana?", "Focus viene molido para filtro o prensa francesa. En italiana funciona, pero la molienda es más gruesa de lo ideal."),
              ("¿Qué es la melena de león?", "Un hongo comestible (Hericium erinaceus) que se usa en polvo. Aporta un fondo suave y terroso. No hacemos promesas de salud: te contamos qué es en su ficha.")],
        others_text="Focus abre el día. Euphoria lo sostiene y Serenity lo cierra.",
    ),
    "euphoria": dict(
        title="Tu alternativa al café · Euphoria, blend energizante",
        meta="Euphoria: yerba mate y guaraná, sin café, para el punto medio del día. Preparación, ingredientes y precauciones.",
        eyebrow="Blend 02 · Mediodía · Con cafeína", h1="Tu alternativa al café",
        lead="Euphoria es nuestro blend de mediodía: yerba mate y guaraná, sin café. Para el punto medio del día, cuando todo pesa un poco más.",
        pills=["3 g · 80 °C · 4 min", "Cantidad según tu test", "Envío incluido"],
        what_title="Qué lleva Euphoria",
        what_text="Dos plantas y ni un grano de café. Las proporciones están en el envase y aquí, sin letra pequeña.",
        tiles=[
            dict(fig="85 %", name="Yerba mate", text="La base del blend. Hoja de Ilex paraguariensis, de sabor herbal y un punto amargo: la pausa de la tarde en Sudamérica.", link=("Ficha próximamente", None), strip="#ff8a5b"),
            dict(fig="15 %", name="Guaraná", text="Semilla amazónica (Paullinia cupana) en polvo, con un fondo tostado. Te contamos qué es y de dónde viene en su ficha.", link=("Ficha próximamente", None), strip="#ffa45e"),
            dict(fig="0 %", name="Café", text="Ni un grano: la cafeína viene de la yerba mate y del guaraná. Una alternativa si ya llevas dos cafés.", link=("¿Prefieres café? Ver Focus →", "para-concentrarse/"), strip="#ffc262"),
            dict(fig="100 g", name="Hoja suelta", text="Para infusionar en taza, en tetera o en mate con bombilla. Unas 30 tazas por bolsa.", link=("Cómo prepararla →", "#ritual"), strip="#ffe066"),
        ],
        ritual=dict(eyebrow_card="Mediodía · energía",
                    rows=[("Dosis", "3 g por taza"), ("Agua", "80 °C"), ("Tiempo", "4 minutos"), ("Cafeína", "Sí · mate y guaraná")],
                    title="Tu ritual de las 13:00",
                    text="Prepárala al volver de comer. Cuatro minutos de pie, lejos de la pantalla, antes de la segunda mitad del día.",
                    steps=[("Calienta el agua a 80 °C", "Sin que llegue a hervir: con el agua demasiado caliente, la yerba amarga."),
                           ("3 g por taza · 4 minutos", "Una cucharadita colmada. Cuela y sirve, o rellena el mate."),
                           ("Al volver de comer", "Prepárala de pie y sin el móvil: cinco minutos lejos de la pantalla.")]),
        prec=dict(title="Antes de tomarla",
                  intro="Lo mismo que pone en el dorso de la bolsa, sin letra pequeña. Euphoria lleva cafeína: léelo antes de tu primera taza.",
                  label_sub="Mediodía · energía para la tarde",
                  ingredients="Yerba mate (85 %), guaraná (Paullinia cupana) en polvo (15 %).",
                  prep=[("3 g", "dosis"), ("250 ml", "agua"), ("80 °C", "temp."), ("4 min", "infusión")],
                  warnings=["Contiene cafeína.", "No recomendado para niños.", "No recomendado durante el embarazo ni la lactancia.", "Si eres sensible a la cafeína, mejor antes de las 17:00."],
                  foot_strong="Infusión, no un complemento.",
                  foot_small="Peso neto: 100 g · hoja suelta<br>Mezclado y envasado en Valencia (España)"),
        plans_title="Dónde encontrar Euphoria",
        plans_text="Euphoria viene en las tres cajas; la cantidad depende de tu test. Empieza por la Degustación y decide después.",
        cta_eyebrow="¿No sabes si Euphoria es para ti?",
        faq_link=("¿Buscas algo para la noche, sin teína? ", "Ver Serenity →", "para-dormir/"),
        faqs=[("¿Euphoria lleva café?", "No. Su cafeína viene de la yerba mate y del guaraná. Si lo que te apetece es café, tu blend es Focus."),
              ("¿Cuándo es mejor tomarla?", "A mediodía o al volver de comer. Si eres sensible a la cafeína, evita tomarla después de las 17:00."),
              ("¿Puedo tomarla en mate?", "Sí. Euphoria es hoja suelta: funciona en taza, en tetera o en mate con bombilla."),
              ("¿Qué es el guaraná?", "La semilla de una planta amazónica (Paullinia cupana), molida en polvo. Contiene cafeína de forma natural. No hacemos promesas de salud: te contamos qué es en su ficha.")],
        others_text="Euphoria sostiene el día. Focus lo abre y Serenity lo cierra.",
    ),
    "serenity": dict(
        title="Infusiones y hierbas para dormir bien · Serenity",
        meta="Serenity: rooibos, manzanilla, ashwagandha y valeriana, sin teína, para tu pausa de la noche. Preparación, ingredientes y precauciones.",
        eyebrow="Blend 03 · Noche · Sin teína", h1="Infusiones y hierbas para dormir bien",
        lead="Serenity es nuestro blend de noche: rooibos, manzanilla, ashwagandha y valeriana, sin teína. Una taza tranquila para cerrar el día lejos de la pantalla.",
        pills=["2 g · 95 °C · 6 min", "Cantidad según tu test", "Envío incluido"],
        what_title="Qué lleva Serenity",
        what_text="Cuatro plantas y ni rastro de teína. Las proporciones están en el envase y aquí, sin letra pequeña.",
        tiles=[
            dict(fig="50 %", name="Rooibos", text="La base del blend. Infusión roja sudafricana, sin teína de forma natural, de sabor suave y un punto dulce.", link=("Ficha próximamente", None), strip="#9a8cf2"),
            dict(fig="30 %", name="Manzanilla", text="Flor de sabor floral y redondo. La infusión de noche de toda la vida, en su versión de especialidad.", link=("Ficha próximamente", None), strip="#b296e2"),
            dict(fig="10 %", name="Ashwagandha", text="Raíz de la tradición ayurvédica, de notas terrosas. Te contamos qué es y sus precauciones en su ficha.", link=("Ficha del ingrediente →", "ingredientes/ashwagandha/"), strip="#d29ed4"),
            dict(fig="10 %", name="Valeriana", text="Raíz de aroma intenso. En pequeña proporción, da profundidad al blend. Fuente: monografía de la EMA.", link=("Ficha próximamente", None), strip="#f2a7c8"),
        ],
        ritual=dict(eyebrow_card="Noche · desconexión",
                    rows=[("Dosis", "2 g por taza"), ("Agua", "95 °C"), ("Tiempo", "6 minutos"), ("Teína", "0 · sin teína")],
                    title="Tu ritual de las 21:00",
                    text="Prepárala sin prisa y tómala lejos del móvil. El ritual es la mitad de la pausa.",
                    steps=[("Calienta el agua a 95 °C", "Si no tienes termómetro: deja reposar 1 minuto tras hervir."),
                           ("2 g por taza · 6 minutos", "Una cucharadita rasa. Tapa la taza mientras reposa para conservar el aroma."),
                           ("Entre 30 y 60 min antes de dormir", "Apaga pantallas, baja la luz y date esos minutos para ti.")]),
        prec=dict(title="Antes de tomarla",
                  intro="Lo mismo que pone en el dorso de la bolsa, sin letra pequeña. Serenity lleva ashwagandha y valeriana: léelo antes de tu primera taza.",
                  label_sub="Noche · desconectar y descansar",
                  ingredients="Rooibos (50 %), manzanilla (30 %), raíz de ashwagandha (Withania somnifera) (10 %), raíz de valeriana (10 %). Sin teína.",
                  prep=[("2 g", "dosis"), ("250 ml", "agua"), ("95 °C", "temp."), ("6 min", "infusión")],
                  warnings=["No recomendado durante el embarazo ni la lactancia.", "No recomendado con trastornos de tiroides.", "Si tomas medicación, consulta con un profesional.", "Puede producir somnolencia: evita conducir después de tomarla."],
                  foot_strong="Es una infusión, no un medicamento.",
                  foot_small="Peso neto: 100 g · hoja suelta<br>Mezclado y envasado en Valencia (España)"),
        plans_title="Dónde encontrar Serenity",
        plans_text="Serenity viene en las tres cajas. Empieza por la Degustación y decide después.",
        cta_eyebrow="¿No sabes si Serenity es para ti?",
        faq_link=("¿Buscas algo para la tarde? ", "Ver Euphoria →", "energizantes/"),
        faqs=[("¿Serenity lleva teína o cafeína?", "No. Rooibos, manzanilla, ashwagandha y valeriana no tienen teína. Puedes tomarla por la noche sin problema."),
              ("¿Cuándo es mejor tomarla?", "Entre 30 y 60 minutos antes de acostarte, como parte de tu rutina de desconexión."),
              ("¿Puedo comprar solo Serenity?", "Serenity viene en la Caja Ritual y en la Caja Degustación. La cantidad depende de tu test: si te recomienda más calma por la noche, tu caja llevará más Serenity."),
              ("¿Por qué lleva ashwagandha?", "Por su sabor terroso y por la tradición de uso en infusiones de noche. No hacemos promesas de salud: te contamos qué es y sus precauciones en su ficha.")],
        others_text="Serenity cierra el día. Focus y Euphoria lo empiezan y lo sostienen.",
    ),
}

# ------------------------------------------------------------------ blog
POSTS = [
    dict(slug="beneficios-te-verde", tone="euphoria", cat="Mediodía", date="27 oct", title="Beneficios del té verde: qué aporta y cuándo tomarlo", img="blog-te-verde.webp", live=True),
    dict(slug="bienestar-digital", tone="serenity", cat="Noche", date="3 nov", title="Bienestar digital: 7 hábitos para desconectar al terminar la jornada", img="blog-bienestar-digital.webp"),
    dict(slug="cafe-de-especialidad", tone="focus", cat="Mañana", date="10 nov", title="¿Qué es el café de especialidad y cómo reconocerlo?", img="blog-cafe-de-especialidad.webp"),
    dict(slug="tipos-de-infusiones", tone="serenity", cat="Noche", date="17 nov", title="Tipos de infusiones: cuál tomar en cada momento del día", img="blog-tipos-de-infusiones.webp"),
    dict(slug="cafeina-mate", tone="euphoria", cat="Mediodía", date="1 dic", title="¿Cuánta cafeína tiene el mate?", img="blog-cafeina-mate.webp"),
    dict(slug="como-preparar-matcha", tone="focus", cat="Mañana", date="8 dic", title="Cómo se hace el té matcha paso a paso", img="blog-matcha.webp"),
    dict(slug="te-verde-sin-teina", tone="serenity", cat="Noche", date="15 dic", title="Té verde sin teína: opciones para la tarde y la noche", img="blog-te-verde-sin-teina.webp"),
]
POST_BY_SLUG = {p["slug"]: p for p in POSTS}

# ------------------------------------------------------------------ ingredientes
INGREDIENTS = {
    "focus": [
        dict(name="Café de especialidad", latin="Coffea arabica", desc="100 % arábica, tostado para filtro. La base de Focus.", link=("Nuestro café →", "nuestro-cafe/")),
        dict(name="Melena de león", latin="Hericium erinaceus", desc="Hongo comestible en polvo, de sabor suave y terroso.", link=None),
    ],
    "euphoria": [
        dict(name="Yerba mate", latin="Ilex paraguariensis", desc="Hoja herbal con un punto amargo. Lleva cafeína natural.", link=None),
        dict(name="Guaraná", latin="Paullinia cupana", desc="Semilla amazónica en polvo, con fondo tostado y cafeína.", link=None),
    ],
    "serenity": [
        dict(name="Rooibos", latin="Aspalathus linearis", desc="Infusión roja sudafricana, sin teína de forma natural.", link=None),
        dict(name="Manzanilla", latin="Matricaria chamomilla", desc="Flor de sabor floral y redondo, la infusión de noche clásica.", link=None),
        dict(name="Ashwagandha", latin="Withania somnifera", desc="Raíz de la tradición ayurvédica, de notas terrosas.", link=("Ver ficha →", "ingredientes/ashwagandha/")),
        dict(name="Valeriana", latin="Valeriana officinalis", desc="Raíz de aroma intenso; en pequeña proporción en Serenity.", link=None),
    ],
}
OTHER_INGREDIENTS = ["Té verde", "Matcha", "Lavanda", "Menta", "Tila", "Jengibre", "Cúrcuma", "Canela", "Melisa", "Cacao", "Hibisco", "Pasiflora", "Hinojo", "Regaliz"]

# ------------------------------------------------------------------ test
QUESTIONS = [
    dict(cat="Ritmo", q="¿A qué hora empieza tu día?", hint="Piensa en un día normal entre semana.", time="≈ 2 min",
         options=[("Antes de las 7:00", "Madrugas: el día empieza con la casa en silencio.", {"focus": 1}),
                  ("Entre las 7:00 y las 9:00", "El horario de casi todo el mundo.", {"focus": 1}),
                  ("Después de las 9:00", "Te organizas tú y empiezas más tarde.", {"euphoria": 1}),
                  ("Depende del día", "Turnos, clases o semanas muy distintas.", {"euphoria": 1, "serenity": 1})]),
    dict(cat="Pantallas", q="¿Cuántas horas pasas frente a una pantalla?", hint="Suma trabajo, estudio y tiempo libre.", time="≈ 1,5 min",
         options=[("Menos de 4 horas", "Tu día tiene bastante vida fuera de la pantalla.", {}),
                  ("Entre 4 y 8 horas", "Una jornada de oficina o de clases.", {"focus": 1}),
                  ("Entre 8 y 10 horas", "Trabajo en remoto y alguna serie por la noche.", {"focus": 1, "serenity": 1}),
                  ("Más de 10 horas", "La pantalla es tu oficina, tu aula y tu sofá.", {"focus": 1, "serenity": 2})]),
    dict(cat="Concentración", q="¿Cuándo te cuesta más concentrarte?", hint="Elige el momento que más se parece a un día normal.", time="≈ 1,3 min",
         options=[("A primera hora", "Hasta las 10:00 me cuesta arrancar.", {"focus": 2}),
                  ("A media mañana", "Entre reuniones y correos pierdo el hilo.", {"focus": 1}),
                  ("Después de comer", "Entre las 14:00 y las 16:00, cuando todo pesa un poco más.", {"euphoria": 2}),
                  ("Por la noche", "Cuando estudio o trabajo hasta tarde.", {"serenity": 1})]),
    dict(cat="Mediodía", q="¿Cómo es tu bajón de la tarde?", hint="Ese momento después de comer en que todo cuesta un poco más.", time="≈ 1 min",
         options=[("No tengo bajón", "Llego a la tarde con la misma energía.", {}),
                  ("Pequeño", "Un rato flojo que se pasa solo.", {"euphoria": 1}),
                  ("Fuerte", "Necesito algo para seguir hasta el final del día.", {"euphoria": 2}),
                  ("Lo tapo con otro café", "Y luego me cuesta dormir.", {"euphoria": 2, "serenity": 1})]),
    dict(cat="Cafeína", q="¿Cuántos cafés tomas al día?", hint="Cuenta también el té y las bebidas energéticas.", time="≈ 45 s",
         options=[("Ninguno", "Prefieres infusiones o nada.", {"serenity": 1}),
                  ("Uno", "El de la mañana y listo.", {"focus": 1}),
                  ("Dos o tres", "Uno para arrancar y otro para aguantar.", {"focus": 1, "euphoria": 1}),
                  ("Más de tres", "Uno detrás de otro, casi sin pensarlo.", {"euphoria": 1, "serenity": 1})]),
    dict(cat="Noche", q="¿Cómo desconectas por la noche?", hint="Piensa en la última hora antes de dormir.", time="≈ 30 s",
         options=[("Me cuesta desconectar", "Sigo pensando en el trabajo o en las entregas.", {"serenity": 2}),
                  ("Con el móvil en la mano", "Redes o series hasta que me entra el sueño.", {"serenity": 2}),
                  ("Leo o escucho algo", "Ya tengo una rutina sin pantallas.", {"serenity": 1}),
                  ("Me duermo enseguida", "Desconectar no es mi problema.", {})]),
    dict(cat="Sabor", q="¿Qué te apetece más?", hint="Sin pensar en efectos: solo en lo que te gusta tomar.", time="≈ 15 s",
         options=[("Café", "Me gusta su sabor y su ritual.", {"focus": 2}),
                  ("Mate", "Herbal, un punto amargo, para compartir.", {"euphoria": 2}),
                  ("Infusión", "Algo suave y caliente, sin cafeína.", {"serenity": 2}),
                  ("Un poco de todo", "Me gusta cambiar según el momento.", {})]),
]
LAST_QUESTION = dict(cat="Antes de recomendarte", q="¿Hay algo que debamos tener en cuenta?",
                     hint="Puedes marcar varias. Solo lo usamos para ajustar tu caja y no lo guardamos.", time="Última pregunta",
                     options=[("embarazo", "Embarazo o lactancia"), ("medicacion", "Tomo medicación"),
                              ("cafeina", "Soy sensible a la cafeína"), ("nada", "Nada de esto")])

for _p in POSTS:
    _p.setdefault("live", False)
