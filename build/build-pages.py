# -*- coding: utf-8 -*-
"""Generates the whole Dr. Dobby site — five pages × three languages — from one
template. Texts are taken verbatim from doctordobby.com in each language.

    python3 build/build-pages.py

Edit the dictionaries below, never the generated HTML.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPRITE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sprite.html"), encoding="utf-8").read()

KEYS = ("home", "services", "petshop", "installations", "contact")

PATHS = {
    "en": {"home": "index.html", "services": "services/index.html",
           "petshop": "pet-shop/index.html", "installations": "installations/index.html",
           "contact": "contact/index.html"},
    "es": {"home": "es/index.html", "services": "es/servicios/index.html",
           "petshop": "es/tienda-mascota/index.html", "installations": "es/instalaciones/index.html",
           "contact": "es/contacto/index.html"},
    "ru": {"home": "ru/index.html", "services": "ru/servisy/index.html",
           "petshop": "ru/zoomagazin/index.html", "installations": "ru/infrastruktura/index.html",
           "contact": "ru/kontakty/index.html"},
}

FONTS = {
    "latin": "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap",
    "ru": "https://fonts.googleapis.com/css2?family=Unbounded:wght@600;700;800&family=Onest:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap",
}

# --- The one shop, and the two profiles — taken from doctordobby.com ---------
# Address, coordinates and the two social URLs are the live ones; the map link is
# name-anchored so phones hand it to the Maps app instead of the browser.
ADDRESS = "Avd. Nuestro Padre Jes\u00fas Cautivo 15, Edf. Nely, Local 2, 29640 Fuengirola, M\u00e1laga"
GEO = ("36.5516041", "-4.6190035")
MAPS = ("https://www.google.com/maps/search/?api=1&amp;"
        "query=Cl%C3%ADnica+Veterinaria+Doctor+Dobby%2C+Avenida+Nuestro+Padre+Jes%C3%BAs+Cautivo+15"
        "%2C+29640+Fuengirola%2C+M%C3%A1laga")
IG = "https://www.instagram.com/dr.dobby_clinica_veterinaria/"
FB = "https://www.facebook.com/people/Cl%C3%ADnica-Veterinaria-Doctor-Dobby/100063490931078/"
WHATSAPP = "https://wa.me/34622653515"

L = {}

# ================================================================ ENGLISH
L["en"] = {
    "chrome": dict(
        skip="Skip to content", navLabel="Main", langLabel="Language", menuLabel="Menu",
        callLabel="Call 951 566 125", logoAlt="Dr. Dobby, clínica veterinaria",
        markAlt="Dr. Dobby doberman logo mark",
        hoursMain="Mon–Fri 09:00–20:30", hoursSat="Sat 10:30–13:30",
        addressLine="Avd. Nuestro Padre Jesús Cautivo 15, Fuengirola",
        nav=[("services", "Services"), ("petshop", "Pet Shop"),
             ("installations", "Installations"), ("contact", "Contact")],
        home="Home", checking="Checking hours…",
        addrSub="Edf. Nely, Local 2, 29640 Fuengirola, Málaga",
        hoursRow="Monday to Friday 09:00 – 20:30",
        hoursRowSub="Saturdays 10:30 – 13:30 · Sunday closed",
        phoneSub="Call during opening hours", mailSub="We reply within one working day",
        waSub="Message us — appointments and quick questions",
        footBrandText="Dr. Dobby Veterinary Clinic in Fuengirola. Avd. Nuestro Padre Jesús Cautivo 15, Edf. Nely, Local 2.",
        footCols=[("Services", [("services", "Services"), ("petshop", "Pet shop")]),
                  ("Clinic", [("installations", "Installations"), ("contact", "Contact")])],
        socHead="Follow us", socSub="Photos from the clinic, news and opening notices",
        legalHead="Legal", legal=["Privacy Policy", "Cookies Policy", "Legal Notice"],
        copyright="© All rights reserved · Dr. Dobby · Fuengirola, España",
    ),
    "home": dict(
        title="Dr. Dobby — Veterinary Clinic in Fuengirola",
        desc="Consultations, preventive medicine, surgery, diagnostics and a pet shop. Dr. Dobby Clínica Veterinaria, Avd. Nuestro Padre Jesús Cautivo 15, Fuengirola.",
        eyebrow="Clínica Veterinaria · Fuengirola",
        h1=["Veterinary", "Clinic in", "Fuengirola"],
        lede="Consultations, preventive medicine, surgery, our own laboratory and imaging, and a pet shop — all in one clinic on Avenida Nuestro Padre Jesús Cautivo.",
        ctaBook="Book a visit",
        statusMonFri="Mon–Fri", statusMonFriH="09:00–20:30", statusSat="Sat", statusSatH="10:30–13:30",
        ticker=["Veterinary consultation", "Vaccination", "Passports", "Microchips", "Deworming",
                "Surgery", "Diagnostic imaging", "Laboratory research", "Hospital", "Dental care", "Pet shop"],
        teaserEyebrow="What we do",
        teaserH2="A full clinic,<br>not just a consultation",
        teaserNote="Veterinary Consultations and Preventive medicine (Vaccination, Passports, Microchips, Deworming).",
        teasers=[
            ("i-stethoscope", "Veterinary Consultation",
             "Our veterinarian will listen to you, examine your animal, conduct all necessary examinations and prescribe treatment based on the examination and answer all of your questions.",
             "services", "All services"),
            ("i-lamp", "Surgery",
             "The surgeons of our veterinary clinic carry out various surgical interventions both the simplest and most common operations.",
             "services", "All services"),
            ("i-bowl", "Pet Shop",
             "Food, Accessories, Animal Health. Our veterinarian will help you with the selection according to your pet diet and it’s needs.",
             "petshop", "Visit the shop"),
        ],
        servicesCta="See all 10 services",
        instEyebrow="Installations",
        instH2="Five rooms behind<br>the consulting room",
        instNote="From preparation through surgery to recovery — plus our own laboratory and imaging department, so most results come back the same day.",
        instCta="See the installations",
        shopEyebrow="Pet shop",
        shopH2="Food, accessories,<br>animal health",
        shopLede="Our veterinarian will help you with the selection according to your pet diet and it’s needs.",
        shopCta="Visit the pet shop",
        conEyebrow="Contact",
        conH2="Come in, or<br>call us first",
        conNote="Walk-ins are welcome during opening hours. For surgery, dental work and any procedure under anesthesia, please book ahead.",
        conCta="Contact page", conCall="951 566 125",
    ),
    "services": dict(
        title="Services — Dr. Dobby, Fuengirola",
        desc="Consultations, vaccination, passports, microchips, deworming, surgery, diagnostic imaging, laboratory, hospital and dental care.",
        eyebrow="Our services",
        h1="Everything your<br>animal may need",
        lede="Veterinary Consultations and Preventive medicine (Vaccination, Passports, Microchips, Deworming), surgery, diagnostics and aftercare — under one roof.",
        filterLabel="Filter services",
        chips=[("all", "All 10"), ("consultation", "Consultation"), ("prevention", "Prevention"),
               ("surgery", "Surgery"), ("diagnostics", "Diagnostics"), ("care", "Care")],
        rows=[
            ("consultation", "Consultation", "Consultations",
             "Our veterinarian will listen to you, examine your animal, conduct all necessary examinations and prescribe treatment based on the examination and answer all of your questions."),
            ("prevention", "Prevention", "Vaccination",
             "Pets need to be vaccinated early to ensure they stay safe from disease. Young pets are at a much higher risk of catching serious illnesses, and if they do fall ill, these diseases are more likely to be fatal or cause lifelong health issues. This means it’s vital your young pet is vaccinated at the right time and that you follow all of the instructions given by your doctor."),
            ("prevention", "Prevention", "Passports",
             "We provide and register passports. The veterinary passport contains information about your pet (type, breed, nickname, special signs, information about microchipping), contains information about the owner and contains detailed information about vaccinations and examinations of pets."),
            ("prevention", "Prevention", "Microchips",
             "The microchip contains a unique identifying number recorded, along with your contact information and your pet information, in a pet registry database. If your pet goes missing and turns up in an animal shelter, the shelter employees will use an RF scanner to search for this ID and contact the pet owner."),
            ("prevention", "Prevention", "Deworming",
             "We carry out deworming procedures to prevent parasites in animals."),
            ("surgery", "Surgery", "Surgery",
             "The surgeons of our veterinary clinic carry out various surgical interventions both the simplest and most common operations (such as castration of cats, dogs, sterilization of cats, sterilization of dogs), as well as complex surgeries on bones, joints and other organs."),
            ("diagnostics", "Diagnostics", "Diagnostic imaging",
             "Our x-ray machine allows us to get high-quality x-ray images in a short time. Using the digital control panel, we set up settings individually for each animal based on it’s type, size or other characteristics. We also have an ultrasound scanner for investigating tumours, cardiac disease and pregnancy."),
            ("diagnostics", "Diagnostics", "Laboratory research",
             "We do blood tests, we can analyse urine samples, skin samples and cell samples from certain tumours, all allowing for as prompt a diagnosis as possible for your pet."),
            ("care", "Care", "Hospital",
             "We hospitalize patients in the hospital before surgery and in the postoperative period – here the patients, under the supervision of our specialists, wake up after anesthesia."),
            ("care", "Care", "Dental care for your pet",
             "Our Veterinary Technicians will clean each &amp; every tooth (adult dogs have 42 &amp; cats 30!!!) on all sides with a combination of an ultrasonic scaler &amp; hand tools for cleaning plaque and polishing teeth."),
        ],
        outroH="Not sure what your animal needs?",
        outroP="Call us and describe what you are seeing. We will tell you whether it can wait for an appointment.",
        outroCta="Contact us",
    ),
    "installations": dict(
        title="Installations — Dr. Dobby, Fuengirola",
        desc="Pre-operating room, operating room, recovery room, laboratory and diagnostic imaging at Dr. Dobby Veterinary Clinic in Fuengirola.",
        eyebrow="Installations",
        h1="Five rooms behind<br>the consulting room",
        lede="From preparation through surgery to recovery — plus our own laboratory and imaging department, so most results come back the same day.",
        items=[
            ("i-scissors", "Pre-operating room", "Where we carry out shaving and disinfection of pets before entering the operating room."),
            ("i-lamp", "Operating room", "Place for the intervention or procedure that requires general anesthesia. This room always remains in optimal aseptic conditions and has an Inhalation agents for anesthesia just like in human medicine. Throughout the surgical procedure, our patients are monitored, which allows us to control their vital signs."),
            ("i-bed", "Recovery room", "In addition, our clinic has a room for animals in a period of rehabilitation, for those that have undergone any kind of intervention or require hospitalization."),
            ("i-flask", "Laboratory", "At Dr. Dobby Veterinary Clinic we can perform hematologies, biochemistry, cytology, urinalysis, stool tests, and tests for many infectious diseases in both cats and dogs and exotic animals."),
            ("i-scan", "Diagnostic imaging", "The imaging department also has an ultrasound and radiology equipment, where our veterinarians obtain dynamic images of organs and bones."),
        ],
        outroH="Booking a procedure?",
        outroP="Surgery, dental work and anything under anesthesia goes by appointment. Call us and we will find a slot.",
        outroCta="Contact us",
    ),
    "petshop": dict(
        title="Pet Shop — Dr. Dobby, Fuengirola",
        desc="Food, accessories and animal health products, chosen with your veterinarian at Dr. Dobby in Fuengirola.",
        eyebrow="Pet shop",
        h1="Food, accessories,<br>animal health",
        lede="Our veterinarian will help you with the selection according to your pet diet and it’s needs.",
        items=[
            ("i-bowl", "Food", "We have a wide range of special animal food products as well as snacks and treats for your best friend."),
            ("i-ball", "Accessories", "It is important to play with your little friends in order to maintain its’s psychical activity and mental health. We have a wide selection of toys, accessories and other forms of leisure for animals."),
            ("i-heart", "Animal Health", "Products for oral hygiene, different types of antiparasitic and preventive medicine. Prevention is the best remedy to avoid animal diseases!"),
        ],
        outroH="Ask before you buy",
        outroP="Diet and preventive products depend on the animal. Ask our veterinarian and take home the right one.",
        outroCta="Ask about a product",
    ),
    "contact": dict(
        title="Contact — Dr. Dobby, Fuengirola",
        desc="Avd. Nuestro Padre Jesús Cautivo 15, Fuengirola. 951 566 125 · 622 653 515 · info@doctordobby.com",
        eyebrow="Contact",
        h1="Come in, or<br>call us first",
        lede="We have the best team of professionals and the latest technology in all specialties. Veterinary services by appointment.",
        mapName="Dr. Dobby Clínica Veterinaria",
        mapAddr="Av. Nuestro Padre Jesús Cautivo, 15 · Fuengirola",
        mapCta="Open in Maps",
        formH="Contact Dr. Dobby now",
        formSub="Tell us about your animal and we will get back to you with a time.",
        fName="Name", fMail="Email", fTel="Phone", fMsg="Comments",
        consent1="I accept the ", consentLink="Privacy Policy", send="Send",
    ),
}

# ================================================================ SPANISH
L["es"] = {
    "chrome": dict(
        skip="Ir al contenido", navLabel="Principal", langLabel="Idioma", menuLabel="Menú",
        callLabel="Llamar al 951 566 125", logoAlt="Dr. Dobby, clínica veterinaria",
        markAlt="Logotipo de Dr. Dobby, silueta de dóberman",
        hoursMain="Lun–Vie 09:00–20:30", hoursSat="Sáb 10:30–13:30",
        addressLine="Avd. Nuestro Padre Jesús Cautivo 15, Fuengirola",
        nav=[("services", "Servicios"), ("petshop", "Tienda"),
             ("installations", "Instalaciones"), ("contact", "Contacto")],
        home="Inicio", checking="Comprobando el horario…",
        addrSub="Edf. Nely, Local 2, 29640 Fuengirola, Málaga",
        hoursRow="Lunes a Viernes 09:00 – 20:30",
        hoursRowSub="Sábados 10:30 – 13:30 · Domingo cerrado",
        phoneSub="Llámanos dentro del horario", mailSub="Respondemos en un día laborable",
        waSub="Escríbenos — citas y consultas rápidas",
        footBrandText="Clínica Veterinaria Dr. Dobby en Fuengirola. Avd. Nuestro Padre Jesús Cautivo 15, Edf. Nely, Local 2.",
        footCols=[("Servicios", [("services", "Servicios"), ("petshop", "Tienda mascota")]),
                  ("La Clínica", [("installations", "Instalaciones"), ("contact", "Contacto")])],
        socHead="Síguenos", socSub="Fotos de la clínica, novedades y avisos de horario",
        legalHead="Legal", legal=["Política de Privacidad", "Política de Cookies", "Aviso Legal"],
        copyright="© All rights reserved · Dr. Dobby · Fuengirola, España",
    ),
    "home": dict(
        title="Dr. Dobby — Clínica Veterinaria en Fuengirola",
        desc="Consulta, medicina preventiva, cirugía, diagnóstico y tienda para mascotas. Dr. Dobby Clínica Veterinaria, Avd. Nuestro Padre Jesús Cautivo 15, Fuengirola.",
        eyebrow="Clínica Veterinaria · Fuengirola",
        h1=["Clínica", "Veterinaria en", "Fuengirola"],
        lede="Consulta, medicina preventiva, cirugía, laboratorio y diagnóstico por imagen propios, y tienda para mascotas — todo en una clínica en la Avenida Nuestro Padre Jesús Cautivo.",
        ctaBook="Pedir cita",
        statusMonFri="Lun–Vie", statusMonFriH="09:00–20:30", statusSat="Sáb", statusSatH="10:30–13:30",
        ticker=["Consulta veterinaria", "Vacunación", "Pasaportes", "Microchips", "Desparasitaciones",
                "Cirugía general", "Diagnóstico por imagen", "Laboratoriales", "Hospitalizaciones",
                "Limpieza dental", "Tienda mascota"],
        teaserEyebrow="Qué hacemos",
        teaserH2="Una clínica completa,<br>no sólo una consulta",
        teaserNote="Consulta Veterinaria y medicina preventiva (Vacunaciones, Pasaportes, Desparasitaciones).",
        teasers=[
            ("i-stethoscope", "Consulta Veterinaria",
             "En Clínica Veterinaria Dr. Dobby prestamos servicios plenos en la salud veterinaria.",
             "services", "Todos los servicios"),
            ("i-lamp", "Cirugía General",
             "Cirugía general, Diagnóstico por Imagen, Análisis de Sangre y Laboratoriales, Hospitalizaciones, Limpieza Dental por ultrasonidos.",
             "services", "Todos los servicios"),
            ("i-bowl", "Tienda Mascota",
             "Alimentación animal, Complementos para mascotas, Salud y Bienestar Animal.",
             "petshop", "Ver la tienda"),
        ],
        servicesCta="Ver los 10 servicios",
        instEyebrow="Instalaciones",
        instH2="Cinco salas detrás<br>de la consulta",
        instNote="De la preparación al quirófano y a la recuperación — más laboratorio y diagnóstico por imagen propios.",
        instCta="Ver las instalaciones",
        shopEyebrow="Tienda mascota",
        shopH2="Alimentación,<br>complementos,<br>salud animal",
        shopLede="Nuestro veterinario te ayuda a elegir según la dieta y las necesidades de tu mascota.",
        shopCta="Ver la tienda",
        conEyebrow="Contacto",
        conH2="Ven, o<br>llámanos antes",
        conNote="Puedes venir sin cita dentro del horario. Para cirugía, limpieza dental y cualquier procedimiento con anestesia, pide cita antes.",
        conCta="Página de contacto", conCall="951 566 125",
    ),
    "services": dict(
        title="Servicios — Dr. Dobby, Fuengirola",
        desc="Consulta, vacunación, pasaportes, microchips, desparasitaciones, cirugía, diagnóstico por imagen, laboratoriales, hospitalizaciones y limpieza dental.",
        eyebrow="Nuestros servicios",
        h1="Todo lo que tu<br>animal necesita",
        lede="Consulta Veterinaria y medicina preventiva (Vacunaciones, Pasaportes, Desparasitaciones), cirugía general, diagnóstico y hospitalización — bajo un mismo techo.",
        filterLabel="Filtrar servicios",
        chips=[("all", "Los 10"), ("consultation", "Consulta"), ("prevention", "Prevención"),
               ("surgery", "Cirugía"), ("diagnostics", "Diagnóstico"), ("care", "Cuidados")],
        rows=[
            ("consultation", "Consulta", "Consulta",
             "Nuestro veterinario lo escuchará, examinará a su animal, realizará todos los exámenes necesarios, le recetará un tratamiento basado en el examen y responderá a todas sus preguntas."),
            ("prevention", "Prevención", "Vacunación",
             "Las mascotas deben ser vacunadas temprano para asegurarse de que se mantengan a salvo de la enfermedad. Las mascotas jóvenes tienen un riesgo mucho mayor de contraer enfermedades graves y, si se enferman, es más probable que estas enfermedades sean fatales o causen problemas de salud de por vida. Esto significa que es vital que su mascota se vacune en el momento adecuado y que siga todas las instrucciones dadas por su veterinario."),
            ("prevention", "Prevención", "Pasaportes",
             "Proporcionamos y registramos pasaportes. El pasaporte veterinario contiene información sobre su mascota (tipo, raza, apodo, signos especiales, información sobre microchips), contiene información sobre el propietario y contiene información detallada sobre las vacunas y los exámenes preventivos de las mascotas."),
            ("prevention", "Prevención", "Microchips",
             "El microchip contiene un número de identificación único registrado, junto con su información de contacto y la información de su mascota, en una base de datos de registro de mascotas. Si su mascota se pierde y aparece en un refugio para animales, los empleados del refugio usarán un escáner de RF para buscar esta identificación y contactar al dueño de la mascota."),
            ("prevention", "Prevención", "Desparasitaciones",
             "Realizamos procedimientos de desparasitación para prevenir parásitos en animales."),
            ("surgery", "Cirugía", "Cirugía general",
             "Los cirujanos de nuestra clínica veterinaria realizan diversas intervenciones quirúrgicas, tanto las operaciones más simples y comunes (como castración de gatos, perros, esterilización de gatos, esterilización de perros), así como cirugías complejas en huesos y articulaciones."),
            ("diagnostics", "Diagnóstico", "Diagnóstico por imagen",
             "Nuestra máquina de rayos X nos permite obtener imágenes de rayos X de alta calidad en poco tiempo. Usando el panel de control digital, configuramos los ajustes individualmente para cada animal en función de su tipo, tamaño u otras características. También tenemos un ecógrafo para investigar tumores, enfermedades cardíacas y embarazos."),
            ("diagnostics", "Diagnóstico", "Laboratoriales",
             "Hacemos análisis de sangre, podemos analizar muestras de orina, muestras de piel y muestras de células de ciertos tumores, lo que permite un diagnóstico lo más rápido posible para su mascota."),
            ("care", "Cuidados", "Hospitalizaciones",
             "Ingresamos a los pacientes en el hospital antes de la cirugía y en el postoperatorio. Aquí, los pacientes, bajo la supervisión de nuestros especialistas, se despiertan después de la anestesia."),
            ("care", "Cuidados", "Limpieza dental para su mascota",
             "Nuestros técnicos veterinarios limpiarán todos y cada uno de los dientes (¡los perros adultos tienen 42 y los gatos 30!) en todos los lados con una combinación de un raspador ultrasónico y herramientas manuales para limpiar la placa y pulir los dientes."),
        ],
        outroH="¿No sabes qué necesita tu animal?",
        outroP="Llámanos y cuéntanos qué ves. Te decimos si puede esperar a una cita.",
        outroCta="Contacta con nosotros",
    ),
    "installations": dict(
        title="Instalaciones — Dr. Dobby, Fuengirola",
        desc="Sala de prequirófano, quirófano, sala de recuperación, laboratorio y diagnóstico por imagen en la Clínica Veterinaria Dr. Dobby de Fuengirola.",
        eyebrow="Instalaciones",
        h1="Cinco salas detrás<br>de la consulta",
        lede="De la preparación al quirófano y a la recuperación — más laboratorio y diagnóstico por imagen propios.",
        items=[
            ("i-scissors", "Sala de prequirófano", "Donde llevamos a cabo la preparación, rasurado y desinfección de las mascotas antes de entrar a quirófano. Posteriormente, se administrará la anestesia requerida en base al procedimiento o intervención a realizar para asegurar el bienestar de la mascota."),
            ("i-lamp", "Sala de quirófano", "Lugar destinado a la intervención o procedimiento que requiera anestesia general. Dicha sala permanece, siempre, en condiciones óptimas de asepsia y cuenta con un equipo de anestesia inhalatoria, al igual que en medicina humana. Durante todo el procedimiento quirúrgico nuestros pacientes se encuentran monitorizados lo que nos permite controlar sus constantes vitales."),
            ("i-bed", "Sala de recuperación", "Además, nuestra clínica cuenta con una sala para animales en período de convalecencia, para aquéllos que han sufrido cualquier clase de intervención o que requieran hospitalización. La sala está equipada por bloques de jaulas verticales, que permiten una mejor observación de las mascotas y un mejor manejo de las mismas tanto a la hora de la alimentación como de la higiene."),
            ("i-flask", "Diagnóstico de laboratorio", "En la clínica Veterinaria Dr. Dobby podemos realizar hematologías, perfiles bioquímicos, citologías, urianálisis, análisis coprológicos, y pruebas para muchas enfermedades infecciosas tanto en perros y gatos como en animales exóticos."),
            ("i-scan", "Diagnóstico por imagen", "El departamento de imagen también cuenta con un equipo de ecografía abdominal, donde nuestros veterinarios obtendrán imágenes dinámicas de los órganos abdominales y que facilitarán una buena emisión de diagnósticos, complementándose con la radiología."),
        ],
        outroH="¿Vas a programar un procedimiento?",
        outroP="La cirugía, la limpieza dental y todo lo que lleve anestesia va con cita previa. Llámanos y buscamos hueco.",
        outroCta="Contacta con nosotros",
    ),
    "petshop": dict(
        title="Tienda para Mascotas — Dr. Dobby, Fuengirola",
        desc="Alimentación animal, complementos para mascotas y salud y bienestar animal, elegidos con tu veterinario.",
        eyebrow="Tienda mascota",
        h1="Alimentación,<br>complementos,<br>salud animal",
        lede="Nuestro veterinario te ayuda a elegir según la dieta y las necesidades de tu mascota.",
        items=[
            ("i-bowl", "Alimentación Animal", "Tenemos una gran variedad de productos de alimentación para animales."),
            ("i-ball", "Complementos para Mascotas", "Mejora la salud física y psicológica de tu mascota con una amplia selección de juguetes, premios, accesorios y otras formas de ocio para animales. ¡Verás qué divertido!"),
            ("i-heart", "Salud y Bienestar Animal", "Cuidar la higiene bucodental, tratamientos antiparasitarios… ¡Prevenir es el mejor remedio para evitar las enfermedades animales!"),
        ],
        outroH="Pregunta antes de comprar",
        outroP="La dieta y los preventivos dependen del animal. Pregunta a nuestro veterinario y llévate el adecuado.",
        outroCta="Preguntar por un producto",
    ),
    "contact": dict(
        title="Contacto — Dr. Dobby, Fuengirola",
        desc="Avd. Nuestro Padre Jesús Cautivo 15, Fuengirola. 951 566 125 · 622 653 515 · info@doctordobby.com",
        eyebrow="Contacto",
        h1="Ven, o<br>llámanos antes",
        lede="Contamos con el mejor equipo de profesionales y la última tecnología en todas las especialidades. Servicios veterinarios con cita previa.",
        mapName="Dr. Dobby Clínica Veterinaria",
        mapAddr="Av. Nuestro Padre Jesús Cautivo, 15 · Fuengirola",
        mapCta="Abrir en Maps",
        formH="Contacta con nosotros",
        formSub="Déjanos un mensaje: cuéntanos qué le pasa a tu animal y te damos una hora.",
        fName="Nombre", fMail="Email", fTel="Teléfono", fMsg="Comentarios",
        consent1="Aceptar la ", consentLink="política de privacidad", send="Enviar",
    ),
}

# ================================================================ RUSSIAN
L["ru"] = {
    "chrome": dict(
        skip="Перейти к содержимому", navLabel="Основное меню", langLabel="Язык", menuLabel="Меню",
        callLabel="Позвонить 951 566 125", logoAlt="Dr. Dobby, ветеринарная клиника",
        markAlt="Логотип Dr. Dobby, силуэт добермана",
        hoursMain="Пн–Пт 09:00–20:30", hoursSat="Сб 10:30–13:30",
        addressLine="Avd. Nuestro Padre Jesús Cautivo 15, Fuengirola",
        nav=[("services", "Сервисы"), ("petshop", "Зоомагазин"),
             ("installations", "Инфраструктура"), ("contact", "Контакты")],
        home="Главная", checking="Проверяем часы работы…",
        addrSub="Edf. Nely, Local 2, 29640 Fuengirola, Málaga",
        hoursRow="С понедельника по пятницу 09:00 – 20:30",
        hoursRowSub="Суббота 10:30 – 13:30 · Воскресенье выходной",
        phoneSub="Звоните в рабочие часы", mailSub="Отвечаем в течение рабочего дня",
        waSub="Напишите нам — запись и короткие вопросы",
        footBrandText="Ветеринарная клиника Dr. Dobby в Фуэнхироле. Avd. Nuestro Padre Jesús Cautivo 15, Edf. Nely, Local 2.",
        footCols=[("Сервисы", [("services", "Сервисы"), ("petshop", "Зоомагазин")]),
                  ("Клиника", [("installations", "Инфраструктура"), ("contact", "Контакты")])],
        socHead="Мы в соцсетях", socSub="Фото из клиники, новости и изменения в графике",
        legalHead="Legal", legal=["Политика конфиденциальности", "Политика Cookies", "Правовая информация"],
        copyright="© All rights reserved · Dr. Dobby · Fuengirola, España",
    ),
    "home": dict(
        title="Dr. Dobby — ветеринарная клиника в Фуэнхироле",
        desc="Консультации, профилактическая медицина, хирургия, диагностика и зоомагазин. Dr. Dobby Clínica Veterinaria, Avd. Nuestro Padre Jesús Cautivo 15, Фуэнхирола.",
        eyebrow="Clínica Veterinaria · Фуэнхирола",
        h1=["Ветеринарная", "клиника в", "Фуэнхироле"],
        lede="Консультации, профилактическая медицина, хирургия, собственные лаборатория и отдел диагностики, зоомагазин — всё в одной клинике на Avenida Nuestro Padre Jesús Cautivo.",
        ctaBook="Записаться на приём",
        statusMonFri="Пн–Пт", statusMonFriH="09:00–20:30", statusSat="Сб", statusSatH="10:30–13:30",
        ticker=["Консультация", "Вакцинация", "Паспорта", "Чипирование", "Дегельминтизация",
                "Хирургия", "Диагностика", "Лабораторные исследования", "Стационар",
                "Чистка зубов", "Зоомагазин"],
        teaserEyebrow="Что мы делаем",
        teaserH2="Полноценная клиника,<br>а не только приём",
        teaserNote="Консультации и профилактическая медицина (Паспорта, Микрочипы, Дегельминтизация).",
        teasers=[
            ("i-stethoscope", "Консультация",
             "В нашей ветеринарной клинике мы предоставляем полный спектр услуг в области ветеринарии.",
             "services", "Все сервисы"),
            ("i-lamp", "Общая хирургия",
             "Общая хирургия, Рентгенография, УЗИ, Анализ крови и другие лабораторные исследования, Госпитализация, Чистка зубов ультразвуком.",
             "services", "Все сервисы"),
            ("i-bowl", "Зоомагазин",
             "Корма для животных, Аксессуары, Различные виды противопаразитарных и профилактических средств.",
             "petshop", "В зоомагазин"),
        ],
        servicesCta="Все 10 сервисов",
        instEyebrow="Инфраструктура",
        instH2="Пять кабинетов<br>за смотровой",
        instNote="От подготовки через операционную до реабилитации — плюс собственные лаборатория и отдел диагностики.",
        instCta="Смотреть инфраструктуру",
        shopEyebrow="Зоомагазин",
        shopH2="Корма, аксессуары,<br>здоровье животных",
        shopLede="Корма для животных, аксессуары, различные виды противопаразитарных и профилактических средств.",
        shopCta="В зоомагазин",
        conEyebrow="Контакты",
        conH2="Приходите<br>или позвоните",
        conNote="В рабочие часы можно прийти без записи. На операцию, чистку зубов и любые процедуры под наркозом — по предварительной записи.",
        conCta="Страница контактов", conCall="951 566 125",
    ),
    "services": dict(
        title="Сервисы — Dr. Dobby, Фуэнхирола",
        desc="Консультация, вакцинация, паспорта, чипирование, дегельминтизация, хирургия, диагностика, лабораторные исследования, стационар и чистка зубов.",
        eyebrow="Наши сервисы",
        h1="Всё, что нужно<br>вашему животному",
        lede="Консультации и профилактическая медицина (Вакцинация, Паспорта, Чипирование, Дегельминтизация), хирургия, диагностика и стационар — в одной клинике.",
        filterLabel="Фильтр сервисов",
        chips=[("all", "Все 10"), ("consultation", "Консультация"), ("prevention", "Профилактика"),
               ("surgery", "Хирургия"), ("diagnostics", "Диагностика"), ("care", "Уход")],
        rows=[
            ("consultation", "Консультация", "Консультация",
             "Наш ветеринарный врач выслушает Вас, осмотрит Ваше животное, ответит на все Ваши вопросы, проведет все необходимые исследования и на основании обследования назначит лечение."),
            ("prevention", "Профилактика", "Вакцинация",
             "Мы проводим прививки для собак и кошек от всех распространенных инфекционных заболеваний. Прививка – это способ выработать у организма иммунитет к определенным заболеваниям путем «тренировки» клеток иммунной системы. В организм вводятся мертвые или инактивированные частицы возбудителя болезни, и иммунные клетки, уничтожая их, «учатся» бороться с подобными частицами."),
            ("prevention", "Профилактика", "Паспорта",
             "Предоставляем и регистрируем паспорта. Ветеринарный паспорт содержит информацию о вашем питомце (вид, порода, кличка, особые приметы, информация о микрочипировании), содержит данные о владельце и содержит подробную информацию о проведённых вакцинациях и профилактических осмотрах домашних животных."),
            ("prevention", "Профилактика", "Чипирование",
             "Чипирование собаки или кошки – метод идентификации животного путем введения под кожу микрочипа с уникальным и неизменным пятнадцатизначным идентификационным номером. За присвоенным кодовым номером закрепляются данные о животном и его владельцах (кличка, номера контактных телефонов, адреса, особенные отметки). Эти данные заносятся в международную базу данных."),
            ("prevention", "Профилактика", "Дегельминтизация",
             "Проводим дегельминтизацию, это лечебно-профилактическое мероприятие, направленное на оздоровление или профилактику паразитозов у животных. Это неотъемлемая часть забот о вашем питомце, поддерживающая его здоровую жизнедеятельность."),
            ("surgery", "Хирургия", "Хирургия",
             "Хирурги нашей ветеринарной клиники в лечебных и диагностических целях проводят различные плановые оперативные вмешательства – как самые простые и распространенные операции (такие как кастрация котов, кобелей, стерилизация кошек, стерилизация собак), так и сложные реконструктивные операции на костях и суставах."),
            ("diagnostics", "Диагностика", "Клинико-диагностические исследования",
             "Наш аппарат позволяет за короткое время получать высококачественные и максимально информативные рентгеновские снимки. С помощью цифровой панели управления возможно производить настройки индивидуально для каждого животного любого вида, размера и конституции, учитывая исследуемую область."),
            ("diagnostics", "Диагностика", "Лабораторные исследования",
             "Проводим лабораторную диагностику, исследуем биоматериалы (кровь, моча, кал, пробы шерсти и т.д.) с помощью различного специализированного оборудования. Основной целью лабораторной диагностики является уточнение, подтверждение или опровержение диагноза, предполагаемого ветеринарным врачом."),
            ("care", "Уход", "Стационар",
             "В стационар мы госпитализируем пациентов перед проведением оперативного вмешательства и в послеоперационный период – здесь кошки и собаки под присмотром специалистов приходят в себя после анестезии."),
            ("care", "Уход", "Чистка зубов ультразвуком",
             "Ветеринар полностью снимает камень, шлифует пастой каждый зубик, а затем наносит специальное вещество для поддержания максимально длительного эффекта. Камень – серьезная проблема домашних питомцев, которая встречается достаточно часто."),
        ],
        outroH="Не знаете, что нужно вашему животному?",
        outroP="Позвоните и опишите, что видите. Мы скажем, можно ли подождать до записи.",
        outroCta="Связаться с нами",
    ),
    "installations": dict(
        title="Инфраструктура — Dr. Dobby, Фуэнхирола",
        desc="Предоперационная, операционная, комната отдыха, лаборатория и отдел диагностики ветеринарной клиники Dr. Dobby в Фуэнхироле.",
        eyebrow="Инфраструктура",
        h1="Пять кабинетов<br>за смотровой",
        lede="От подготовки через операционную до реабилитации — плюс собственные лаборатория и отдел диагностики.",
        items=[
            ("i-scissors", "Предоперационная комната", "Где мы проводим подготовку и дезинфекцию домашних животных перед операционной."),
            ("i-lamp", "Операционная", "Место для хирургического вмешательства или процедуры, требующей общей анестезии. Эта комната всегда остается в оптимальных асептических условиях и имеет ингаляционные средства для анестезии. На протяжении всей операции наши пациенты находятся под аппаратным наблюдением, что позволяет нам контролировать их жизненные показатели."),
            ("i-bed", "Комната отдыха", "Кроме того, в нашей клинике есть комната для животных в период реабилитации. Комната оборудована вертикальными клетками, которые позволяют наблюдать за домашними животными."),
            ("i-flask", "Лаборатория", "Мы проводим все необходимые анализы такие как: биохимия, цитология, анализ мочи, анализ кала и тесты на многие инфекционные заболевания у кошек и собак, а также у экзотических животных."),
            ("i-scan", "Отдел диагностики", "В отделе диагностики имеется ультразвуковое и рентгенологическое оборудование, где наши ветеринары получают динамические изображения органов и костей."),
        ],
        outroH="Планируете процедуру?",
        outroP="Операция, чистка зубов и всё под наркозом — по записи. Позвоните, подберём время.",
        outroCta="Связаться с нами",
    ),
    "petshop": dict(
        title="Зоомагазин — Dr. Dobby, Фуэнхирола",
        desc="Корма, игрушки и аксессуары, средства для здоровья животных — с подбором от ветеринара.",
        eyebrow="Зоомагазин",
        h1="Корма, аксессуары,<br>здоровье животных",
        lede="Корма для животных, аксессуары, различные виды противопаразитарных и профилактических средств.",
        items=[
            ("i-bowl", "Продукты питания", "Широкий ассортимент специальных продуктов питания для животных, а также различные лакомства и угощения для вашего лучшего друга."),
            ("i-ball", "Игрушки и аксессуары", "Играть с питомцем важно для его физической активности и психического здоровья. У нас большой выбор игрушек, аксессуаров и других развлечений для животных."),
            ("i-heart", "Здоровье животных", "Продукты для гигиены полости рта, различные виды противопаразитарных и профилактических средств."),
        ],
        outroH="Спросите перед покупкой",
        outroP="Рацион и профилактика зависят от животного. Спросите нашего ветеринара — и заберёте то, что нужно.",
        outroCta="Спросить о товаре",
    ),
    "contact": dict(
        title="Контакты — Dr. Dobby, Фуэнхирола",
        desc="Avd. Nuestro Padre Jesús Cautivo 15, Fuengirola. 951 566 125 · 622 653 515 · info@doctordobby.com",
        eyebrow="Контакты",
        h1="Приходите<br>или позвоните",
        lede="У нас лучшая команда специалистов и современное оборудование по всем направлениям. Ветеринарные услуги по предварительной записи.",
        mapName="Dr. Dobby Clínica Veterinaria",
        mapAddr="Av. Nuestro Padre Jesús Cautivo, 15 · Fuengirola",
        mapCta="Открыть в Maps",
        formH="Связаться с нами",
        formSub="Расскажите о вашем животном — мы подберём время.",
        fName="Имя", fMail="Email", fTel="Телефон", fMsg="Комментарий",
        consent1="Я принимаю ", consentLink="политику конфиденциальности", send="Отправить",
    ),
}


# ---------------------------------------------------------------- helpers
def rel(frm, to):
    d = os.path.dirname(frm) or "."
    p = os.path.relpath(to, d).replace(os.sep, "/")
    if p.endswith("/index.html"):
        return p[:-10]
    if p == "index.html":
        return "./"
    return p


def asset(frm, name):
    d = os.path.dirname(frm) or "."
    return os.path.relpath("assets/" + name, d).replace(os.sep, "/")


def chrome(lang, key):
    """Header, utility bar and footer — identical on every page."""
    c = L[lang]["chrome"]
    me = PATHS[lang][key]

    nav = "\n      ".join(
        '<a href="%s"%s>%s</a>' % (rel(me, PATHS[lang][k]), ' aria-current="page"' if k == key else '', t)
        for k, t in c["nav"]
    )
    langs = "".join(
        '<a href="%s" hreflang="%s"%s>%s</a>' % (
            rel(me, PATHS[code][key]), code, ' aria-current="page"' if code == lang else '', code.upper())
        for code in ("en", "es", "ru")
    )
    foot_cols = "\n    ".join(
        '<div>\n      <h4>%s</h4>\n      %s\n    </div>' % (
            head, "\n      ".join('<a href="%s">%s</a>' % (rel(me, PATHS[lang][k]), t) for k, t in items))
        for head, items in c["footCols"]
    )
    legal = "\n      ".join('<a href="#">%s</a>' % t for t in c["legal"])

    head = f'''<div class="util">
  <div class="wrap util__in">
    <div class="util__set">
      <span class="util__i"><svg aria-hidden="true"><use href="#i-clock"/></svg><span><b>{c["hoursMain"]}</b></span></span>
      <span class="util__i util__set--wide">{c["hoursSat"]}</span>
    </div>
    <div class="util__set">
      <span class="util__i"><svg aria-hidden="true"><use href="#i-phone"/></svg><a href="tel:+34951566125"><b>951 566 125</b></a></span>
      <span class="util__i util__set--wide"><svg aria-hidden="true"><use href="#i-wa"/></svg><a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp 622 653 515</a></span>
      <span class="util__i util__set--wide"><svg aria-hidden="true"><use href="#i-mail"/></svg><a href="mailto:info@doctordobby.com">info@doctordobby.com</a></span>
      <span class="util__i util__set--wide"><svg aria-hidden="true"><use href="#i-pin"/></svg>{c["addressLine"]}</span>
    </div>
  </div>
</div>

<header class="hdr" id="hdr">
  <div class="wrap hdr__in">
    <a class="brand" href="{rel(me, PATHS[lang]["home"])}">
      <img class="brand__logo" src="{asset(me, "logo.png")}" width="371" height="156" alt="{c["logoAlt"]}">
    </a>

    <nav class="nav" id="nav" aria-label="{c["navLabel"]}">
      {nav}
      <div class="nav__lang" aria-label="{c["langLabel"]}">
        {langs}
      </div>
    </nav>

    <div class="hdr__end">
      <div class="lang" aria-label="{c["langLabel"]}">
        {langs}
      </div>
      <a class="btn btn--v btn--sm btn--call" href="tel:+34951566125" aria-label="{c["callLabel"]}"><svg aria-hidden="true"><use href="#i-phone"/></svg><span class="btn__label">951 566 125</span></a>
      <button class="burger" id="burger" aria-label="{c["menuLabel"]}" aria-controls="nav" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>'''

    foot = f'''<footer>
  <div class="wrap foot">
    <div>
      <div class="foot__brand">
        <img class="brand__logo" src="{asset(me, "logo.png")}" width="371" height="156" alt="{c["logoAlt"]}">
      </div>
      <p>{c["footBrandText"]}</p>
    </div>
    {foot_cols}
    <div>
      <h4>{c["legalHead"]}</h4>
      {legal}
    </div>
  </div>
  <div class="wrap foot__bot">
    <span>{c["copyright"]}</span>
    <div class="soc">
      <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram"><svg aria-hidden="true"><use href="#i-ig"/></svg></a>
      <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook"><svg aria-hidden="true"><use href="#i-fb"/></svg></a>
    </div>
  </div>
</footer>'''
    return head, foot


def phead(lang, key):
    """The band that opens an inner page."""
    c, d = L[lang]["chrome"], L[lang][key]
    me = PATHS[lang][key]
    return f'''<section class="phead">
  <div class="wrap phead__in">
    <div>
      <p class="mono crumbs" data-rise style="--d:60ms"><a href="{rel(me, PATHS[lang]["home"])}">{c["home"]}</a> · {d["eyebrow"]}</p>
      <h1 data-rise style="--d:140ms">{d["h1"]}</h1>
      <p class="lede" data-rise style="--d:240ms">{d["lede"]}</p>
    </div>
    <div class="phead__mark" aria-hidden="true" data-rise style="--d:200ms">
      <div class="d"></div>
      <svg viewBox="0 0 100 89.43"><use href="#dobby"/></svg>
    </div>
  </div>
</section>'''


def outro(lang, key):
    d = L[lang][key]
    me = PATHS[lang][key]
    return f'''<section class="sec sec--sand">
  <div class="wrap">
    <div class="cstrip" data-reveal>
      <div>
        <h2>{d["outroH"]}</h2>
        <p class="sec__note" style="margin-top:14px">{d["outroP"]}</p>
      </div>
      <div class="cstrip__cta">
        <a class="btn btn--v" href="{rel(me, PATHS[lang]["contact"])}">{d["outroCta"]}</a>
        <a class="btn btn--ghost" href="tel:+34951566125"><svg aria-hidden="true"><use href="#i-phone"/></svg>951 566 125</a>
      </div>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------- page bodies
def body_home(lang):
    c, d = L[lang]["chrome"], L[lang]["home"]
    me = PATHS[lang]["home"]
    h1 = "\n        ".join(
        '<span class="l" data-rise style="--d:%dms"><span>%s</span></span>' % (
            180 + i * 100, f'<em>{line}</em>' if i == 2 else line)
        for i, line in enumerate(d["h1"]))
    ticker = "".join(f'<span>{t}</span><i></i>' for t in d["ticker"])
    teasers = "\n      ".join(
        f'''<a class="teaser" href="{rel(me, PATHS[lang][target])}" data-reveal style="--d:{40 + i * 60}ms">
        <span class="teaser__ic"><svg aria-hidden="true"><use href="#{icon}"/></svg></span>
        <h3>{name}</h3>
        <p>{text}</p>
        <span class="teaser__go">{go} <svg aria-hidden="true"><use href="#i-arrow"/></svg></span>
      </a>'''
        for i, (icon, name, text, target, go) in enumerate(d["teasers"]))
    rooms = "\n        ".join(
        f'<span><svg aria-hidden="true"><use href="#{icon}"/></svg>{name}</span>'
        for icon, name, _ in L[lang]["installations"]["items"])

    return f'''<section class="hero">
  <div class="wrap hero__in">
    <div class="hero__copy">
      <p class="mono eyebrow" data-rise style="--d:80ms">{d["eyebrow"]}</p>
      <h1>
        {h1}
      </h1>
      <p class="lede" data-rise style="--d:500ms">{d["lede"]}</p>
      <div class="hero__cta" data-rise style="--d:600ms">
        <a class="btn btn--v" href="{rel(me, PATHS[lang]["contact"])}">{d["ctaBook"]}</a>
        <a class="btn btn--ghost" href="tel:+34951566125"><svg aria-hidden="true"><use href="#i-phone"/></svg>951 566 125</a>
      </div>
      <div class="status" data-rise style="--d:700ms">
        <span class="dot" data-open aria-live="polite">{c["checking"]}</span>
        <span><b>{d["statusMonFri"]}</b> {d["statusMonFriH"]}</span>
        <span><b>{d["statusSat"]}</b> {d["statusSatH"]}</span>
      </div>
    </div>

    <div class="stage" id="stage" data-rise style="--d:420ms">
      <div class="stage__ring" aria-hidden="true"></div>
      <div class="stage__disc" aria-hidden="true"></div>
      <div class="stage__shadow" aria-hidden="true"></div>
      <canvas class="stage__canvas" id="dobbyCanvas" aria-hidden="true"></canvas>
      <div class="stage__flat" id="stageFlat">
        <svg viewBox="0 0 100 89.43" role="img" aria-label="{c["markAlt"]}"><use href="#dobby"/></svg>
      </div>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker__track">
    <div class="ticker__set">{ticker}</div>
    <div class="ticker__set">{ticker}</div>
  </div>
</div>

<section class="sec">
  <div class="wrap">
    <div class="sec__head" data-reveal>
      <div>
        <p class="mono eyebrow">{d["teaserEyebrow"]}</p>
        <h2>{d["teaserH2"]}</h2>
      </div>
      <p class="sec__note">{d["teaserNote"]}</p>
    </div>
    <div class="teasers">
      {teasers}
    </div>
    <div class="sec__more" data-reveal>
      <a class="btn btn--ghost" href="{rel(me, PATHS[lang]["services"])}">{d["servicesCta"]} <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
    </div>
  </div>
</section>

<section class="sec sec--sand">
  <div class="wrap">
    <div class="shop" data-reveal>
      <svg class="shop__dog" viewBox="0 0 100 89.43" aria-hidden="true"><use href="#dobby"/></svg>
      <div>
        <p class="mono eyebrow">{d["shopEyebrow"]}</p>
        <h2>{d["shopH2"]}</h2>
        <p class="shop__lede">{d["shopLede"]}</p>
        <div class="shop__cta"><a class="btn btn--peach" href="{rel(me, PATHS[lang]["petshop"])}">{d["shopCta"]}</a></div>
      </div>
      <div class="shop__list">
        {"".join(f"""
        <div class="shop__item">
          <svg aria-hidden="true"><use href="#{icon}"/></svg>
          <div><h3>{t}</h3><p>{b}</p></div>
        </div>""" for icon, t, b in L[lang]["petshop"]["items"])}
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split" data-reveal>
      <div>
        <p class="mono eyebrow">{d["instEyebrow"]}</p>
        <h2>{d["instH2"]}</h2>
      </div>
      <div>
        <p class="sec__note">{d["instNote"]}</p>
        <div class="rooms">
          {rooms}
        </div>
        <div class="sec__more">
          <a class="btn btn--ghost" href="{rel(me, PATHS[lang]["installations"])}">{d["instCta"]} <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--sand">
  <div class="wrap">
    <div class="cstrip" data-reveal>
      <div>
        <p class="mono eyebrow">{d["conEyebrow"]}</p>
        <h2>{d["conH2"]}</h2>
        <p class="sec__note" style="margin-top:14px">{d["conNote"]}</p>
        <div class="cstrip__facts">
          <div><svg aria-hidden="true"><use href="#i-pin"/></svg><span><b>Avd. Nuestro Padre Jesús Cautivo 15</b><span>{c["addrSub"]}</span></span></div>
          <div><svg aria-hidden="true"><use href="#i-clock"/></svg><span><b>{c["hoursRow"]}</b><span>{c["hoursRowSub"]}</span></span></div>
          <div><svg aria-hidden="true"><use href="#i-phone"/></svg><span><b><a href="tel:+34951566125">951 566 125</a></b><span>{c["phoneSub"]}</span></span></div>
        </div>
      </div>
      <div class="cstrip__cta">
        <a class="btn btn--v" href="{rel(me, PATHS[lang]["contact"])}">{d["conCta"]}</a>
        <a class="btn btn--ghost" href="tel:+34951566125"><svg aria-hidden="true"><use href="#i-phone"/></svg>{d["conCall"]}</a>
      </div>
    </div>
  </div>
</section>'''


def body_services(lang):
    d = L[lang]["services"]
    chips = "\n      ".join(
        f'<button class="chip" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{t}</button>'
        for k, t in d["chips"])
    rows = "\n\n      ".join(
        f'''<article class="row" data-cat="{cat}" data-reveal style="--d:{40 + i * 30}ms">
        <span class="tag">{tag}</span>
        <h2>{title}</h2>
        <p>{text}</p>
      </article>'''
        for i, (cat, tag, title, text) in enumerate(d["rows"]))
    return f'''{phead(lang, "services")}

<section class="sec">
  <div class="wrap">
    <div class="filters" role="group" aria-label="{d["filterLabel"]}" data-reveal>
      {chips}
    </div>
    <div class="chart" id="chart">
      {rows}
    </div>
  </div>
</section>

{outro(lang, "services")}'''


def body_installations(lang):
    d = L[lang]["installations"]
    items = "\n      ".join(
        f'''<article class="inst__item" data-reveal style="--d:{40 + i * 60}ms">
        <div class="inst__plate"><svg aria-hidden="true"><use href="#{icon}"/></svg></div>
        <div><h2>{t}</h2><p>{b}</p></div>
      </article>'''
        for i, (icon, t, b) in enumerate(d["items"]))
    return f'''{phead(lang, "installations")}

<section class="sec">
  <div class="wrap">
    <div class="inst__list">
      <!-- PHOTO SLOT: replace the <svg> inside .inst__plate with <img src="…" alt="…"> -->
      {items}
    </div>
  </div>
</section>

{outro(lang, "installations")}'''


def body_petshop(lang):
    d = L[lang]["petshop"]
    cards = "\n      ".join(
        f'''<article class="pcard" data-reveal style="--d:{40 + i * 70}ms">
        <span class="pcard__ic"><svg aria-hidden="true"><use href="#{icon}"/></svg></span>
        <h2>{t}</h2>
        <p>{b}</p>
      </article>'''
        for i, (icon, t, b) in enumerate(d["items"]))
    return f'''{phead(lang, "petshop")}

<section class="sec">
  <div class="wrap">
    <div class="pshop">
      {cards}
    </div>
  </div>
</section>

{outro(lang, "petshop")}'''


def body_contact(lang):
    c, d = L[lang]["chrome"], L[lang]["contact"]
    return f'''{phead(lang, "contact")}

<section class="sec">
  <div class="wrap">
    <div class="contact">
      <div data-reveal>
        <div class="info">
          <div class="info__row">
            <svg aria-hidden="true"><use href="#i-pin"/></svg>
            <div><b>Avd. Nuestro Padre Jesús Cautivo 15</b><span>{c["addrSub"]}</span></div>
          </div>
          <div class="info__row">
            <svg aria-hidden="true"><use href="#i-clock"/></svg>
            <div><b>{c["hoursRow"]}</b><span>{c["hoursRowSub"]}</span></div>
          </div>
          <div class="info__row">
            <svg aria-hidden="true"><use href="#i-phone"/></svg>
            <div><b><a href="tel:+34951566125">951 566 125</a></b><span>{c["phoneSub"]}</span></div>
          </div>
          <div class="info__row">
            <svg aria-hidden="true"><use href="#i-wa"/></svg>
            <div><b><a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp 622 653 515</a></b><span>{c["waSub"]}</span></div>
          </div>
          <div class="info__row">
            <svg aria-hidden="true"><use href="#i-mail"/></svg>
            <div><b><a href="mailto:info@doctordobby.com">info@doctordobby.com</a></b><span>{c["mailSub"]}</span></div>
          </div>
          <div class="info__row info__row--soc">
            <svg aria-hidden="true"><use href="#i-ig"/></svg>
            <div>
              <b>{c["socHead"]}</b>
              <span>{c["socSub"]}</span>
              <div class="soc soc--inline">
                <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram"><svg aria-hidden="true"><use href="#i-ig"/></svg></a>
                <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook"><svg aria-hidden="true"><use href="#i-fb"/></svg></a>
              </div>
            </div>
          </div>
        </div>

        <p class="status" style="margin-top:22px"><span class="dot" data-open aria-live="polite">{c["checking"]}</span></p>

        <div class="map">
          <div class="map__vis" aria-hidden="true">
            <div class="map__pin"><svg aria-hidden="true"><use href="#i-pin"/></svg></div>
          </div>
          <div class="map__bar">
            <div><b>{d["mapName"]}</b><span>{d["mapAddr"]}</span></div>
            <a class="btn btn--ghost btn--sm" target="_blank" rel="noopener" href="{MAPS}">{d["mapCta"]}</a>
          </div>
        </div>
      </div>

      <form class="form" id="form" data-reveal style="--d:120ms" novalidate>
        <h2>{d["formH"]}</h2>
        <p>{d["formSub"]}</p>
        <div class="field"><label for="f-name">{d["fName"]}</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="f-mail">{d["fMail"]}</label><input id="f-mail" name="email" type="email" autocomplete="email" spellcheck="false" required></div>
        <div class="field"><label for="f-tel">{d["fTel"]}</label><input id="f-tel" name="phone" type="tel" inputmode="tel" autocomplete="tel" spellcheck="false"></div>
        <div class="field"><label for="f-msg">{d["fMsg"]}</label><textarea id="f-msg" name="comments"></textarea></div>
        <label class="consent"><input type="checkbox" id="f-ok" required><span>{d["consent1"]}<a href="#">{d["consentLink"]}</a></span></label>
        <button class="btn btn--v" type="submit">{d["send"]}</button>
        <p class="form__done" id="formNote" hidden role="status"></p>
      </form>
    </div>
  </div>
</section>'''


BODIES = {"home": body_home, "services": body_services, "petshop": body_petshop,
          "installations": body_installations, "contact": body_contact}


def page(lang, key):
    c, d = L[lang]["chrome"], L[lang][key]
    me = PATHS[lang][key]
    head, foot = chrome(lang, key)
    alts = "\n".join(
        '<link rel="alternate" hreflang="%s" href="%s">' % (code, rel(me, PATHS[code][key]))
        for code in ("en", "es", "ru"))
    importmap = '''
<script type="importmap">
{
  "imports": {
    "three/webgpu": "https://cdn.jsdelivr.net/npm/three@0.185.1/build/three.webgpu.min.js",
    "three/tsl": "https://cdn.jsdelivr.net/npm/three@0.185.1/build/three.tsl.min.js"
  }
}
</script>''' if key == "home" else ""
    preconnect = '\n<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>' if key == "home" else ""

    # One LocalBusiness record on the home and contact pages: the shop's real
    # address and coordinates, and the two social profiles as sameAs.
    jsonld = ""
    if key in ("home", "contact"):
        jsonld = f'''
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "VeterinaryCare",
  "name": "Dr. Dobby",
  "url": "https://doctordobby.com/",
  "telephone": "+34951566125",
  "email": "info@doctordobby.com",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Avd. Nuestro Padre Jes\u00fas Cautivo 15, Edf. Nely, Local 2",
    "addressLocality": "Fuengirola",
    "addressRegion": "M\u00e1laga",
    "postalCode": "29640",
    "addressCountry": "ES"
  }},
  "geo": {{ "@type": "GeoCoordinates", "latitude": {GEO[0]}, "longitude": {GEO[1]} }},
  "openingHoursSpecification": [
    {{ "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "20:30" }},
    {{ "@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "10:30", "closes": "13:30" }}
  ],
  "sameAs": ["{IG}", "{FB}"]
}}
</script>'''

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d["title"]}</title>
<meta name="description" content="{d["desc"]}">
<meta name="theme-color" content="#14101a">
{alts}

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{preconnect}
<link href="{FONTS["ru" if lang == "ru" else "latin"]}" rel="stylesheet">
<link rel="stylesheet" href="{asset(me, "site.css")}">{importmap}{jsonld}
</head>
<body>

<a class="skip" href="#main">{c["skip"]}</a>
<div class="progress" id="progress"></div>

{SPRITE}

{head}

<main id="main">
{BODIES[key](lang)}
</main>

{foot}

<script src="{asset(me, "site.js")}"></script>
</body>
</html>
'''


if __name__ == "__main__":
    for lang in ("en", "es", "ru"):
        for key in KEYS:
            path = os.path.join(ROOT, PATHS[lang][key])
            os.makedirs(os.path.dirname(path), exist_ok=True)
            out = page(lang, key)
            open(path, "w", encoding="utf-8").write(out)
            print("%-34s %6d bytes" % (PATHS[lang][key], len(out)))
