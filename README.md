# BA Bygg Emmaboda – hemsida

Hemsida för **Byggnadsfirman Birger Andersson Emmaboda AB** (BA Bygg Emmaboda), org.nr 556337-1490.

En statisk sida (HTML, CSS och lite JavaScript) utan byggsteg. Den kan läggas upp på valfritt webbhotell,
GitHub Pages, Netlify eller liknande.

## Visa sidan lokalt

```bash
python3 -m http.server 8000
```

Öppna sedan <http://localhost:8000>. Det går också att öppna `index.html` direkt i webbläsaren.

## Struktur

```
index.html              Hela sidan (tjänster, om oss, så går det till, omdömen, område, kontakt)
assets/css/style.css    Stilmall
assets/js/main.js       Mobilmeny, omdömen, offertformulär
assets/js/omdomen.js    Kundomdömen – lägg in riktiga omdömen här
assets/img/             Bilder och logotyp
research/foretagsinfo.md  All insamlad information om företaget, med källor
```

## Innan sidan publiceras

Uppgifterna kommer från offentliga register och kataloger (se `research/foretagsinfo.md`). Stäm av med företaget:

1. **Telefonnummer** – källorna anger olika nummer. Sidan använder 0471-104 91 (Hitta, Yelp) och 070-268 22 50 (Eniro).
2. **Texterna** – tjänstebeskrivningar och arbetssätt bygger på företagets registrerade verksamhet och katalogtexter.
   Justera så att de stämmer med hur företaget faktiskt jobbar.
3. **Bilder** – inga egna bilder från företaget fanns publicerade. Toppbilden och tjänstebilderna är
   illustrationsbilder från Unsplash. Byt gärna mot riktiga projektbilder (samma filnamn i `assets/img/` räcker).
4. **Omdömen** – inga publika omdömen hittades. Lägg in riktiga kundomdömen i `assets/js/omdomen.js`;
   tills dess visar sidan en uppmaning att lämna omdöme på Hitta.se.
5. **E-post** – ingen e-postadress hittades. Offertformuläret öppnar därför ett sms till mobilnumret.
   Fyll i `KONTAKT_EPOST` överst i `assets/js/main.js` för att i stället skicka formuläret som e-post.

## Bildkällor

- Illustrationsbilder: [Unsplash](https://unsplash.com/license) (fri användning, erkännande krävs inte).
- *Emmaboda Ersjön 002* – Bernt Fransson, Lindås,
  [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Emmaboda_Ersj%C3%B6n_002.jpg),
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Fotografens namn och licensen
  måste stå kvar bredvid bilden och i sidfoten.
