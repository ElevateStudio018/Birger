# BA Bygg Emmaboda – webbplats

Webbplats för **Byggnadsfirman Birger Andersson Emmaboda AB** (BA Bygg Emmaboda), org.nr 556337-1490.

Byggd i samma designsystem som S-Bygg-sajten: samma sidstruktur, typografi (Plus Jakarta Sans), mörkt sidhuvud och
sidfot, piller-knappar och runda ”Ring”-knappar, stora foton med rundade hörn och enkla staplade sektioner som växlar
mellan vitt och ljusgrått. Färgerna är BA Byggs egna: grafit och falurött.

## Logga

Loggan är ritad som vektorbanor ur Plus Jakarta Sans, så den ser likadan ut överallt:

- `docs/img/ba-bygg-logo.svg` – vit text, används i sidhuvud och sidfot
- `assets-src/ba-bygg-logo-morkt.svg` – mörk text, för ljus bakgrund
- `docs/img/favicon.svg` – BA-märket

## Sidor

Allt ligger i [`docs/`](docs/) och kräver inga verktyg – öppna `docs/index.html` i en webbläsare.

- `index.html` – startsidan: hero, introduktion, tjänster, företaget i korthet, om oss med arbetsgång, kontakt med
  offertformulär, vanliga frågor, SEO-text med interna länkar och karta
- sex tjänstesidor: `tjanst-nybyggnation.html`, `tjanst-tillbyggnad.html`, `tjanst-renovering.html`,
  `tjanst-badrum.html`, `tjanst-kok.html`, `tjanst-underhall.html`
- `404.html`, `sitemap.xml`, `robots.txt`

## Ändra text

Sidorna genereras av `scripts/build.py`, där all text, alla tjänster, omdömen och kontaktuppgifter finns. Ändra där och kör:

```bash
python3 scripts/build.py docs
```

## Fakta och förslag – gå igenom före lansering

Alla uppgifter och källor finns i [`research/foretagsinfo.md`](research/foretagsinfo.md).

**Verifierat** (Allabolag, Hitta.se, årsredovisning 2024): firmanamn, bifirman BA Bygg Emmaboda, org.nr,
momsreg.nr, registrerat 1988, säte och adress Vegagatan 6 i Emmaboda, F-skatt, verksamhet (nybyggnation,
tillbyggnad och renovering av hus och andra byggnader samt fastighetsförvaltning).

**Bör bekräftas:**

- Telefonnumren. Källorna anger olika nummer; sidan använder 0471-104 91 (Hitta, Yelp) och 070-268 22 50 (Eniro).
- Tjänsterna *Badrumsrenovering*, *Köksrenovering* och *Fastighetsunderhåll* (`confirmed=False` i `SERVICES`).
  De visas som knappar under ”Vi tar också förfrågningar om”.
- Listorna ”Det kan ingå” på tjänstesidorna, arbetsgången och svaren i Vanliga frågor.
- `EMAIL` är tom tills adressen är känd; då visas den inte alls.

Inga certifieringar, försäkringar, garantier eller antal anställda anges.

## Omdömen

Inga publika omdömen hittades (Hitta.se: 0). Lägg in riktiga omdömen ordagrant i `REVIEWS` i `scripts/build.py`.
Tills dess visar sidan en uppmaning att lämna omdöme på Hitta.se.

## Offertformuläret

Formuläret skickar e-post via [FormSubmit](https://formsubmit.co) (gratis) och visar ett tackmeddelande när det
gått fram. Under förhandsvisningen går förfrågningarna till Elevate Studio; byt `FORM_EMAIL` i `scripts/build.py`
till BA Byggs adress vid lansering. Första förfrågan till en ny adress skickar bara ett aktiveringsmejl.
En tjänstesidas ”Begär offert” fyller i projekttypen automatiskt (`index.html?typ=…#offert`).

## Bilder

Inga egna bilder från företaget finns publicerade. Fotona i `docs/img/` är stockbilder från
[Unsplash](https://unsplash.com/license) och märks på sidan som illustrationsbilder. Undantaget är
`emmaboda.jpg` (Ersjön i Emmaboda) av Bernt Fransson, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Emmaboda_Ersj%C3%B6n_002.jpg),
CC BY-SA 4.0 – fotografens namn och licensen måste stå kvar. Byt mot egna bilder genom att ersätta filerna med samma
namn (både `namn.jpg`, ca 1800 px, och `namn-s.jpg`, ca 800 px).

## Publicera

GitHub Pages publicerar mappen `docs/` från grenen `claude/awesome-einstein-sboy64`. Byt `SITE_URL` i
`scripts/build.py` om sidan får en egen domän.
