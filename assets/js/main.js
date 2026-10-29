(function () {
  "use strict";

  // Om företaget skaffar en e-postadress: fyll i den här, så skickas formuläret som e-post i stället för sms.
  var KONTAKT_EPOST = "";
  var KONTAKT_SMS = "+46702682250";

  // Helskärmsmeny
  var toggle = document.querySelector(".menu-toggle");
  var menu = document.getElementById("menu");
  var setMenu = function (open) {
    toggle.setAttribute("aria-expanded", String(open));
    menu.classList.toggle("is-open", open);
    document.body.classList.toggle("menu-open", open);
  };
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      setMenu(toggle.getAttribute("aria-expanded") !== "true");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setMenu(false);
    });
  }

  // Headern ligger transparent över toppbilden och blir ljus när man scrollat förbi den
  var header = document.querySelector(".site-header");
  var hero = document.querySelector(".hero");
  var onScroll = function () {
    header.classList.toggle("is-solid", window.scrollY > hero.offsetHeight - header.offsetHeight);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Årtal som räknas fram automatiskt
  var now = new Date().getFullYear();
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = now;
  });
  document.querySelectorAll("[data-years-since]").forEach(function (el) {
    el.textContent = now - Number(el.getAttribute("data-years-since"));
  });

  // Omdömen – sektionen visas bara när det finns omdömen i omdomen.js
  var list = document.querySelector("[data-reviews]");
  var reviews = Array.isArray(window.OMDOMEN) ? window.OMDOMEN : [];
  if (list && reviews.length > 0) {
    reviews.forEach(function (r) {
      list.appendChild(renderReview(r));
    });
    document.getElementById("omdomen").hidden = false;
  }

  function renderReview(r) {
    var card = document.createElement("figure");
    card.className = "review";

    if (r.betyg) {
      var stars = document.createElement("div");
      var n = Math.max(0, Math.min(5, Math.round(r.betyg)));
      stars.className = "review-stars";
      stars.setAttribute("aria-label", n + " av 5 i betyg");
      stars.textContent = "★★★★★".slice(0, n) + "☆☆☆☆☆".slice(0, 5 - n);
      card.appendChild(stars);
    }

    var quote = document.createElement("blockquote");
    quote.textContent = r.text;
    card.appendChild(quote);

    var meta = [r.projekt, r.ort, r.datum].filter(Boolean).join(" · ");
    var cap = document.createElement("figcaption");
    var name = document.createElement("strong");
    name.textContent = r.namn || "Kund";
    cap.appendChild(name);
    if (meta) cap.appendChild(document.createTextNode(" – " + meta));
    if (r.kalla) {
      var src = document.createElement("span");
      src.className = "review-source";
      src.textContent = "via " + r.kalla;
      cap.appendChild(src);
    }
    card.appendChild(cap);
    return card;
  }

  // Offertformulär → sms (eller e-post om KONTAKT_EPOST är ifyllt)
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    var note = form.querySelector("[data-form-note]");
    var error = form.querySelector("[data-form-error]");
    if (KONTAKT_EPOST && note) {
      note.textContent = "Ditt e-postprogram öppnas med meddelandet ifyllt.";
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var namn = (d.get("namn") || "").trim();
      var telefon = (d.get("telefon") || "").trim();
      var text = (d.get("meddelande") || "").trim();
      if (!namn || !telefon || !text) {
        error.hidden = false;
        return;
      }
      error.hidden = true;

      var ort = (d.get("ort") || "").trim();
      var body =
        "Offertförfrågan: " + d.get("typ") + "\n" +
        text + "\n\n" +
        namn + ", " + telefon + (ort ? ", " + ort : "");

      if (KONTAKT_EPOST) {
        window.location.href =
          "mailto:" + KONTAKT_EPOST +
          "?subject=" + encodeURIComponent("Offertförfrågan – " + d.get("typ")) +
          "&body=" + encodeURIComponent(body);
      } else {
        window.location.href = "sms:" + KONTAKT_SMS + "?&body=" + encodeURIComponent(body);
      }
    });
  }
})();
