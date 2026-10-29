"""Builds docs/*.html for Byggnadsfirman Birger Andersson Emmaboda AB (BA Bygg Emmaboda).

Run:  python3 scripts/build.py docs

All text, services and contact details live in this file. Services with confirmed=False and the FAQ answers are
suggestions that the company should confirm or edit before launch. Sources for the facts: research/foretagsinfo.md.
"""
import html
import json
import pathlib
import sys
from urllib.parse import quote_plus

# Elevate Studio's credit under every footer: the mark and the name, the whole of it one link to elevatestudio.nu.
ELEVATE_CREDIT = '''<!-- elevate-credit -->
<style>.elevate-credit{max-width:1240px;margin:24px auto 0;padding:20px 16px 0;border-top:1px solid rgba(128,128,128,.25);display:flex;justify-content:center;box-sizing:border-box}.elevate-credit a{display:inline-flex;align-items:center;gap:10px;padding:8px 0;font:inherit;font-size:15px;line-height:1;color:inherit;opacity:.55;text-decoration:none;transition:opacity .2s}.elevate-credit a:hover,.elevate-credit a:focus-visible{opacity:1}.elevate-credit svg{width:20px;height:20px;flex:none;display:block}@media(min-width:1024px){.elevate-credit a{font-size:16px}}</style>
<div class="elevate-credit"><a href="https://elevatestudio.nu" target="_blank" rel="noopener"><svg viewBox="0 0 1884.3 1353.9" aria-hidden="true"><path d="M0.0 1353.9 L1218.7 0.0 L1218.7 329.1 L479.7 1136.4 L786.7 1132.4 L1215.5 687.4 L1884.3 1349.9 L1590.1 1349.9 L1218.6 994.7 L865.4 1349.9Z" fill="currentColor"/></svg>Byggd av Elevate Studio</a></div>
'''


OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")

# --- Verified company details (Allabolag, Hitta.se, Eniro, annual report 2024) -------------------------------------
NAME = "BA Bygg Emmaboda"
LEGAL = "Byggnadsfirman Birger Andersson Emmaboda AB"
PHONE, TEL = "0471-104 91", "+4647110491"
MOBILE, MOBILE_TEL = "070-268 22 50", "+46702682250"
STREET, POSTAL, CITY = "Vegagatan 6", "361 31", "Emmaboda"
ADDR = f"{STREET}, {POSTAL} {CITY}"
ORG_NR = "556337-1490"
VAT_NR = "SE556337149001"
FOUNDED = 1988
GEO = (56.62496, 15.54453)
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + quote_plus(f"{LEGAL}, {ADDR}")
MAP_EMBED = "https://www.google.com/maps?q=" + quote_plus(ADDR) + "&z=14&hl=sv&output=embed"
HITTA_LINK = "https://www.hitta.se/verksamhet/byggnadsfirman-birger-andersson-emmaboda-ab-csddjppq"

# Not known yet: left empty, and then not shown anywhere.
EMAIL = ""

# The quote form e-mails through FormSubmit. Elevate Studio receives the requests during the preview; at launch this
# becomes the company's own address. The first request to a new address only sends an activation e-mail.
FORM_EMAIL = "elevate.studio018@gmail.com"

SITE_URL = "https://elevatestudio018.github.io/Birger/"

# --- Services -------------------------------------------------------------------------------------------------------
# confirmed=True: in the company's registered business (bifirman BA Bygg Emmaboda: new builds, extensions and
# renovation of houses and other buildings). confirmed=False: from directory listings or the articles of association,
# shown as "Vi tar också förfrågningar om" until the company confirms them.
SERVICES = [
    dict(
        slug="nybyggnation", title="Nybyggnation", confirmed=True,
        photo="nybyggnation", pos="50% 50%", alt="Nybyggt hus med träfasad",
        short="Villor, fritidshus, garage och andra byggnader.",
        body=[
            "Vi bygger nya bostadshus och andra byggnader i Emmaboda med omnejd – villor, fritidshus, garage, förråd och ekonomibyggnader.",
            "Innan något arbete börjar går vi igenom ritningar, bygglov och tidplan med dig, så att det är klart vad som ska byggas och vem som gör vad.",
        ],
        items=["Villor och fritidshus", "Garage, carport och förråd", "Ekonomibyggnader", "Grund, stomme och tak",
               "Samordning med el, VVS och mark"],
    ),
    dict(
        slug="tillbyggnad", title="Tillbyggnad", confirmed=True,
        photo="tillbyggnad", pos="50% 50%", alt="Hantverkare isolerar en regelvägg",
        short="Ett nytt rum, ett uterum eller en större entré.",
        body=[
            "Behöver huset ett sovrum till, ett uterum eller en större hall bygger vi till så att det nya ansluter till huset du redan har.",
            "Krävs bygglov eller anmälan ska det vara klart innan arbetet börjar. Vi går igenom vad som gäller för ditt projekt.",
        ],
        items=["Nytt rum", "Uterum", "Entré och vindfång", "Påbyggnad", "Anslutning mot befintligt tak och fasad"],
    ),
    dict(
        slug="renovering", title="Renovering och ombyggnad", confirmed=True,
        photo="renovering", pos="50% 50%", alt="Hus under ombyggnad med uppstöttat bjälklag",
        short="Ny planlösning, nya väggar eller renovering i etapper.",
        body=[
            "Ett rum som ska delas, en planlösning som ska öppnas upp eller ett äldre hus som ska renoveras i omgångar. Vi bygger om och renoverar hus och andra byggnader.",
            "Vi tittar på huset tillsammans med dig och går igenom vad som ska göras och i vilken ordning, innan något arbete börjar.",
        ],
        items=["Ändrad planlösning", "Nya och rivna innerväggar", "Isolering och fönsterbyten", "Golv, väggar och innertak",
               "Renovering i etapper"],
    ),
    dict(
        slug="badrum", title="Badrumsrenovering", confirmed=False,
        photo="badrum", pos="50% 50%", alt="Nyrenoverat badrum med glasvägg",
        short="Rivning och uppbyggnad av badrum.",
        body=[
            "Vi tar emot förfrågningar om badrumsrenoveringar – från rivning till färdigt rum.",
            "Tätskikt, VVS och el utförs av behöriga hantverkare. Vi går igenom upplägget med dig innan start.",
        ],
        items=["Rivning", "Nya väggar och golv", "Samordning med VVS, el och plattsättning"],
    ),
    dict(
        slug="kok", title="Köksrenovering", confirmed=False,
        photo="kok", pos="50% 55%", alt="Ljust kök med vita luckor",
        short="Nytt kök eller ändrad planlösning runt köket.",
        body=[
            "Vi tar emot förfrågningar om köksrenoveringar, från rivning av det gamla köket till montering av det nya.",
        ],
        items=["Rivning av gammalt kök", "Nya väggar och ytskikt", "Montering av stommar och luckor", "Öppning mot angränsande rum"],
    ),
    dict(
        slug="underhall", title="Fastighetsunderhåll", confirmed=False,
        photo="underhall", pos="50% 50%", alt="Målarverktyg och färgtråg",
        short="Fasad, tak, fönster och reparationer.",
        body=[
            "Vi tar emot förfrågningar om underhåll och reparationer av bostäder och fastigheter – för villaägare och fastighetsägare.",
        ],
        items=["Fasadrenovering", "Takarbeten", "Fönster och dörrar", "Löpande reparationer"],
    ),
]
DONE = [s for s in SERVICES if s["confirmed"]]
ASK = [s for s in SERVICES if not s["confirmed"]]
WORK_TYPES = [s["title"] for s in SERVICES] + ["Annat"]

# --- Reviews --------------------------------------------------------------------------------------------------------
# No public reviews were found (Hitta.se: 0). Add real reviews only, word for word, with the customer's consent:
#   dict(name="Förnamn E.", stars=5, text="…", source="Google")
REVIEWS = []

FACTS = [
    ("Grundat", str(FOUNDED)),
    ("Säte", "Emmaboda"),
    ("Organisationsnummer", ORG_NR),
    ("F-skatt", "Godkänd"),
]

FAQ = [
    ("Vilka jobb tar ni?",
     "Nybyggnation, tillbyggnader och renovering av hus och andra byggnader. Fråga gärna om badrum, kök och underhåll också."),
    ("Kan jag få en offert?",
     f"Ja. Fyll i <a href=\"#offert\">formuläret</a> eller ring <a href=\"tel:{TEL}\">{PHONE}</a>. Oftast behöver vi se huset eller tomten innan vi kan ge ett pris som håller."),
    ("Var jobbar ni?",
     "Vi utgår från Emmaboda och tar jobb i kommunen – Lindås, Vissefjärda, Långasjö, Eriksmåla, Algutsboda, Boda och Johansfors. Ligger jobbet utanför, säg var, så svarar vi om vi kan ta det."),
    ("Gäller ROT-avdrag?",
     "ROT-avdraget gäller arbetskostnaden för många renoveringar, ombyggnader och tillbyggnader i bostäder. Vi går igenom vad som gäller för ditt jobb i offerten."),
    ("Har ni F-skatt?",
     f"Ja. {LEGAL} är godkänt för F-skatt, org.nr {ORG_NR}."),
]

STEPS = [
    ("Du ringer eller skriver", "Berätta kort vad du vill göra."),
    ("Vi tittar på jobbet", "Gärna på plats, så att vi ser förutsättningarna."),
    ("Du får en offert", "Med vad som ingår och vad det kostar."),
    ("Vi bygger", "Enligt det vi har kommit överens om."),
]

# --- Markup helpers -------------------------------------------------------------------------------------------------
E = html.escape
PHONE_ICON = ('<svg class="pi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
              '<path d="M21 16.5v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 1.1 3.8 2 2 0 0 1 3.1 1.6h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L7.1 9.5a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'
              '<path d="M15 2.5a6.5 6.5 0 0 1 6.5 6.5M15 6a3 3 0 0 1 3 3"/></svg>')
STAR = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="m10 1.6 2.6 5.4 5.9.8-4.3 4.1 1 5.9L10 15l-5.2 2.8 1-5.9L1.5 7.8l5.9-.8z"/></svg>'

# Ersjön is a real photo from Emmaboda (Wikimedia Commons, CC BY-SA 4.0): the credit replaces "Illustrationsbild".
CREDITS = {
    "emmaboda": 'Ersjön, Emmaboda. Foto: Bernt Fransson, <a href="https://commons.wikimedia.org/wiki/File:Emmaboda_Ersj%C3%B6n_002.jpg" target="_blank" rel="noopener">CC BY-SA 4.0</a>',
}


def stars(n=5):
    return f'<span class="stars" role="img" aria-label="{n} av 5 stjärnor">{STAR * n}</span>'


def img(src, alt="", pos="50% 50%", sizes="100vw", lazy=True):
    return (f'<img src="img/{src}.jpg" srcset="img/{src}-s.jpg 800w, img/{src}.jpg 1800w" sizes="{sizes}" '
            f'alt="{E(alt)}"{" loading=\"lazy\"" if lazy else " fetchpriority=\"high\""} decoding="async" style="object-position:{pos}">')


def photo(src, alt, pos="50% 50%", sizes="(min-width: 960px) 50vw, 100vw"):
    """A rounded photo with a note that it is a stock photo, or the photographer's credit."""
    return f'<figure class="ph">{img(src, alt, pos, sizes)}<figcaption>{CREDITS.get(src, "Illustrationsbild")}</figcaption></figure>'


# The BA Bygg logo, drawn from Plus Jakarta Sans outlines: white text for the dark header and footer.
# assets-src/ba-bygg-logo-morkt.svg has dark text for light backgrounds.
def logo():
    return '<img class="logo-img" src="img/ba-bygg-logo.svg" alt="BA Bygg Emmaboda" width="309" height="100">'


def call_btn(label=None, cls=""):
    return f'<a class="pill pill-accent {cls}" href="tel:{TEL}">{PHONE_ICON}<span>{label or "Ring " + PHONE}</span></a>'


NAV = [("tjanster", "Tjänster"), ("foretaget", "Företaget"), ("om-oss", "Om oss"), ("fragor", "Frågor"), ("kontakt", "Kontakt")]


def header(home):
    pre = "" if home else "index.html"
    links = "".join(f'<a href="{pre}#{a}">{t}</a>' for a, t in NAV)
    rows = "".join(f'<li><a href="{pre}#{a}">{t}</a></li>' for a, t in NAV)
    svc = "".join(f'<li><a href="tjanst-{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES)
    return f'''<a class="skip" href="#main">Hoppa till innehållet</a>
<header class="head">
  <div class="wrap bar">
    <a class="logo" href="{'#top' if home else 'index.html'}" aria-label="{NAME}, till startsidan">{logo()}</a>
    <nav class="nav" aria-label="Huvudmeny">{links}</nav>
    <a class="pill pill-accent head-call" href="tel:{TEL}">{PHONE_ICON}<span>{PHONE}</span></a>
    <a class="round round-accent head-round" href="tel:{TEL}" aria-label="Ring {PHONE}">{PHONE_ICON}</a>
    <button class="burger" id="menuBtn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Meny"><span></span><span></span></button>
  </div>
  <nav class="menu" id="menu" aria-label="Meny" hidden>
    <div class="wrap">
      <ul class="menu-main">{rows}</ul>
      <p class="menu-h">Tjänster</p><ul class="menu-svc">{svc}</ul>
      {call_btn()}
    </div>
  </nav>
</header>'''


def footer(home):
    pre = "" if home else "index.html"
    svc = "".join(f'<li><a href="tjanst-{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES)
    mail = f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>' if EMAIL else ""
    return f'''<footer class="foot">
  <div class="wrap">
    <a class="logo" href="{pre or '#top'}" aria-label="{NAME}, till startsidan">{logo()}</a>
    <div class="foot-grid">
      <div>
        <p class="foot-h">{LEGAL}</p>
        <p><b>Emmaboda</b></p>
        <p>{STREET},<br>{POSTAL} {CITY}</p>
        <p><a href="tel:{TEL}">{PHONE}</a><br><a href="tel:{MOBILE_TEL}">{MOBILE}</a></p>{mail}
        <p class="foot-legal">Org.nr {ORG_NR}<br>Momsreg.nr {VAT_NR}<br>Godkänd för F-skatt</p>
      </div>
      <div><p class="foot-h">Tjänster</p><ul>{svc}</ul></div>
      <div><p class="foot-h">BA Bygg</p><ul>{"".join(f'<li><a href="{pre}#{a}">{t}</a></li>' for a, t in NAV)}<li><a href="{pre}#offert">Begär offert</a></li></ul></div>
    </div>
    <div class="foot-end">
      <span>© <span data-year>2026</span> {LEGAL} · Illustrationsbilder från Unsplash</span>
    </div>
  </div>
{ELEVATE_CREDIT}</footer>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def jsonld():
    data = {
        "@context": "https://schema.org", "@type": "GeneralContractor", "name": NAME, "legalName": LEGAL,
        "alternateName": "Byggnadsfirman Birger Andersson", "url": SITE_URL, "telephone": TEL,
        "image": SITE_URL + "img/hero.jpg", "logo": SITE_URL + "img/ba-bygg-logo.svg",
        "foundingDate": str(FOUNDED), "vatID": VAT_NR, "taxID": ORG_NR,
        "address": {"@type": "PostalAddress", "streetAddress": STREET, "postalCode": POSTAL.replace(" ", ""),
                    "addressLocality": CITY, "addressRegion": "Kalmar län", "addressCountry": "SE"},
        "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
        "areaServed": {"@type": "AdministrativeArea", "name": "Emmaboda kommun"},
    }
    if EMAIL:
        data["email"] = EMAIL
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def page(name, title, desc, main, home=False, image="hero"):
    url = SITE_URL + ("" if name == "index.html" else name)
    doc = f'''<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="sv_SE">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{SITE_URL}img/{image}.jpg">
<meta name="theme-color" content="#1b1f24">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="assets/site.css">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
{jsonld() if home else ''}
</head>
<body>
{header(home)}
<main id="main">
{main}
</main>
{footer(home)}'''
    (OUT / name).write_text(doc, encoding="utf-8")


def card(s):
    return (f'<li class="card"><a href="tjanst-{s["slug"]}.html">{photo(s["photo"], s["alt"], s["pos"], "(min-width: 960px) 33vw, 100vw")}'
            f'<h3>{s["title"]}</h3><p>{s["short"]}</p><span class="more">Läs mer</span></a></li>')


def ask_pills(skip=None):
    return "".join(f'<a class="pill pill-dark" href="tjanst-{s["slug"]}.html">{s["title"]}</a>' for s in ASK if s["slug"] != skip)


def review_block(center=False):
    out = []
    for r in REVIEWS:
        src = f', omdöme på {E(r["source"])}' if r.get("source") else ""
        out.append(f'<figure class="review{" center" if center else ""}">{stars(r["stars"])}<blockquote><p>”{E(r["text"])}”</p></blockquote>'
                   f'<figcaption><b>{E(r["name"])}</b>{src}</figcaption></figure>')
    return "".join(out)


def facts_block():
    rows = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in FACTS)
    return f'<dl class="facts">{rows}</dl>'


def quote_form():
    opts = "".join(f"<option>{E(t)}</option>" for t in WORK_TYPES)
    req = '<span class="req" aria-hidden="true">*</span>'
    return f'''<form class="form" id="qform" novalidate data-endpoint="https://formsubmit.co/ajax/{FORM_EMAIL}">
  <p class="field"><label for="f-typ">Typ av jobb</label><select id="f-typ" name="Typ av byggprojekt"><option value="">– Välj ett alternativ –</option>{opts}</select></p>
  <p class="field"><label for="f-namn">För- och efternamn{req}</label><input id="f-namn" name="Namn" autocomplete="name" required><span class="err" id="e-namn" hidden>Skriv ditt namn.</span></p>
  <p class="field"><label for="f-tel">Telefonnummer{req}</label><input id="f-tel" name="Telefon" type="tel" autocomplete="tel"><span class="err" id="e-tel" hidden>Skriv telefonnummer eller e-post.</span></p>
  <p class="field"><label for="f-epost">E-post</label><input id="f-epost" name="E-post" type="email" autocomplete="email"><span class="err" id="e-epost" hidden>Kontrollera e-postadressen.</span></p>
  <p class="field"><label for="f-ort">Ort</label><input id="f-ort" name="Ort" autocomplete="address-level2" placeholder="t.ex. Emmaboda"></p>
  <p class="field"><label for="f-besk">Beskriv jobbet</label><textarea id="f-besk" name="Beskrivning" rows="5" placeholder="Vad ska göras, var och när?"></textarea></p>
  <p class="hp" aria-hidden="true"><label for="f-web">Lämna tomt</label><input id="f-web" name="_honey" tabindex="-1" autocomplete="off"></p>
  <p class="small">{req} Telefonnummer eller e-post räcker. Uppgifterna används bara för att svara dig.</p>
  <p><button class="pill pill-dark" type="submit">Skicka förfrågan</button></p>
  <p class="send-err" id="send-err" role="alert" hidden>Det gick inte att skicka just nu. Försök igen, eller ring <a href="tel:{TEL}">{PHONE}</a>.</p>
</form>
<div class="done" id="qdone" tabindex="-1" hidden>
  <p class="done-h">Tack! Vi har fått din förfrågan.</p>
  <p>Vi hör av oss så snart vi kan. Brådskar det, ring <a href="tel:{TEL}">{PHONE}</a>.</p>
  <p><button class="link" type="button" id="qagain">Skicka en ny förfrågan</button></p>
</div>'''


# --- Start page -----------------------------------------------------------------------------------------------------
def index():
    cards = "".join(card(s) for s in DONE)
    steps = "".join(f"<li><b>{t}</b> {d}</li>" for t, d in STEPS)
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    done_links = " ".join(f'<a class="pill pill-dark" href="tjanst-{s["slug"]}.html">{s["title"]}</a>' for s in DONE)
    years = 2026 - FOUNDED

    if REVIEWS:
        voices = f'''<h3 class="also-h">Vad kunderna säger</h3>{review_block(center=True)}'''
    else:
        voices = f'<p class="small facts-note">Har vi byggt åt dig? <a href="{HITTA_LINK}" target="_blank" rel="noopener">Lämna gärna ett omdöme på Hitta.se</a>.</p>'

    main = f'''<section class="hero" id="top" aria-labelledby="hero-h">
  <div class="hero-ph">{img("hero", "Trähus i skogsbryn i kvällsljus", "60% 55%", lazy=False)}</div>
  <div class="wrap hero-in">
    <h1 id="hero-h">Byggföretag i Emmaboda sedan {FOUNDED}</h1>
    <p>{NAME} bygger nytt, bygger till och renoverar hus och andra byggnader i Emmaboda med omnejd.</p>
    <div class="btns">{call_btn()}<a class="pill pill-dark" href="#offert">Begär offert</a></div>
  </div>
  <span class="hero-note">Illustrationsbild</span>
</section>

<section class="sec tint" aria-labelledby="intro-h">
  <div class="wrap split">
    {photo("villa", "Modern villa med träfasad i kvällsljus", "50% 60%")}
    <div>
      <h2 id="intro-h">Nybyggnation, tillbyggnad och renovering</h2>
      <p class="lead">Byggnadsfirman Birger Andersson har byggt i Emmaboda sedan {FOUNDED}. I dag heter vi {NAME} och tar uppdrag från privatpersoner, företag och fastighetsägare i hela kommunen.</p>
      <div class="btns">{done_links}</div>
    </div>
  </div>
</section>

<section class="sec" id="tjanster" aria-labelledby="tj-h">
  <div class="wrap">
    <h2 id="tj-h">Våra tjänster</h2>
    <ul class="cards">{cards}</ul>
    <h3 class="also-h">Vi tar också förfrågningar om</h3>
    <div class="btns">{ask_pills()}</div>
  </div>
</section>

<section class="sec tint" id="foretaget" aria-labelledby="ft-h">
  <div class="wrap">
    <h2 id="ft-h">Företaget i korthet</h2>
    <p class="lead facts-lead">{LEGAL} registrerades {FOUNDED} och har sitt säte i Emmaboda. Bolaget bedriver byggmästarrörelse inom husbyggnad och fastighetsförvaltning under namnet {NAME}.</p>
    {facts_block()}
    {voices}
  </div>
</section>

<section class="sec" id="om-oss" aria-labelledby="om-h">
  <div class="wrap split">
    {photo("emmaboda", "Ersjön i Emmaboda en sommardag", "50% 50%")}
    <div>
      <h2 id="om-h">Ett lokalt byggföretag i Emmaboda</h2>
      <p class="lead">Vi har funnits i Emmaboda i {years} år och är fortfarande ett litet företag. Du pratar direkt med dem som bygger, från första besöket till slutbesiktningen.</p>
      <h3>Så går det till</h3>
      <ol class="steps">{steps}</ol>
      <div class="btns">{call_btn()}</div>
    </div>
  </div>
</section>

<section class="sec tint" id="kontakt" aria-labelledby="kt-h">
  <div class="wrap narrow">
    <h2 id="kt-h">Bli kontaktad av BA Bygg</h2>
    <p class="lead">Fyll i formuläret så hör vi av oss. Vill du hellre ringa går det bra – kontoret på {PHONE} eller mobilen på <a href="tel:{MOBILE_TEL}">{MOBILE}</a>.</p>
    <div class="btns">{call_btn()}</div>
    <div id="offert">{quote_form()}</div>
  </div>
</section>

<section class="sec" id="fragor" aria-labelledby="fq-h">
  <div class="wrap narrow">
    <h2 id="fq-h">Vanliga frågor</h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="sec tint seo" aria-labelledby="seo-h">
  <div class="wrap narrow">
    <h2 id="seo-h">Byggfirma i Emmaboda</h2>
    <p>{NAME} är en byggfirma i Emmaboda som bygger och renoverar hus och andra byggnader. Vi tar uppdrag inom <a href="tjanst-nybyggnation.html">nybyggnation</a> av villor, fritidshus och garage, och bygger <a href="tjanst-tillbyggnad.html">tillbyggnader</a> när huset behöver mer plats.</p>
    <p>Ska planlösningen ändras eller ett äldre hus rustas upp gör vi <a href="tjanst-renovering.html">renovering och ombyggnad</a>. Ring {PHONE} eller <a href="#offert">begär en offert</a>, så tittar vi på jobbet.</p>
    <h3>Hitta hit</h3>
    <p>{LEGAL}, {ADDR}.</p>
    <div class="btns"><a class="pill pill-accent" href="{MAPS_LINK}" target="_blank" rel="noopener">Öppna i Google Maps</a></div>
  </div>
</section>

<section class="map" aria-label="Karta">
  <iframe src="{MAP_EMBED}" title="Karta: {ADDR}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>'''
    page("index.html", "Byggfirma i Emmaboda – nybyggnation, tillbyggnad, renovering | BA Bygg",
         f"{NAME} ({LEGAL}) bygger nytt, bygger till och renoverar i Emmaboda med omnejd sedan {FOUNDED}. Ring {PHONE} eller begär offert.",
         main, home=True)


# --- Service pages --------------------------------------------------------------------------------------------------
def service_page(s):
    items = "".join(f"<li>{i}</li>" for i in s["items"])
    body = "".join(f"<p>{p}</p>" for p in s["body"])
    review = f'<h2>Omdöme</h2>{review_block()}' if s["confirmed"] and REVIEWS else ""
    others = "".join(card(o) for o in DONE if o["slug"] != s["slug"])
    main = f'''<section class="hero hero-small" aria-labelledby="ph-h">
  <div class="hero-ph">{img(s["photo"], s["alt"], s["pos"], lazy=False)}</div>
  <div class="wrap hero-in">
    <nav class="crumbs" aria-label="Brödsmulor"><a href="index.html">Start</a> / <a href="index.html#tjanster">Tjänster</a> / <span aria-current="page">{s["title"]}</span></nav>
    <h1 id="ph-h">{s["title"]} i Emmaboda</h1>
    <p>{s["short"]}</p>
    <div class="btns">{call_btn()}<a class="pill pill-dark" href="index.html?typ={quote_plus(s["title"])}#offert">Begär offert</a></div>
  </div>
  <span class="hero-note">Illustrationsbild</span>
</section>
<section class="sec">
  <div class="wrap narrow prose">
    <h2>{s["title"]} med BA Bygg</h2>
    {body}
    <h3>Det kan ingå</h3>
    <ul class="list">{items}</ul>
    {review}
    <div class="btns">{call_btn()}<a class="pill pill-dark" href="index.html?typ={quote_plus(s["title"])}#offert">Begär offert</a></div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <h2>Fler tjänster</h2>
    <ul class="cards">{others}</ul>
    <h3 class="also-h">Vi tar också förfrågningar om</h3>
    <div class="btns">{ask_pills(skip=s["slug"])}</div>
  </div>
</section>'''
    desc = f'{s["title"]} i Emmaboda. {s["short"]} {LEGAL}, telefon {PHONE}.'
    page(f'tjanst-{s["slug"]}.html', f'{s["title"]} i Emmaboda | BA Bygg', desc, main, image=s["photo"])


def not_found():
    main = f'<section class="sec"><div class="wrap narrow"><h1>Sidan finns inte</h1><div class="btns"><a class="pill pill-dark" href="index.html">Till startsidan</a>{call_btn()}</div></div></section>'
    page("404.html", "Sidan finns inte | BA Bygg", "Sidan kunde inte hittas.", main)


def seo_files():
    urls = ["index.html"] + [f'tjanst-{s["slug"]}.html' for s in SERVICES]
    locs = "".join(f"<url><loc>{SITE_URL}{'' if u == 'index.html' else u}</loc></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{locs}</urlset>\n', encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    index()
    for s in SERVICES:
        service_page(s)
    not_found()
    seo_files()
    print("Byggde", len(list(OUT.glob("*.html"))), "sidor i", OUT)
