/*
 * Kundomdömen som visas under "Omdömen" på startsidan.
 *
 * Inga publika omdömen om företaget hittades när sidan byggdes (se research/foretagsinfo.md),
 * så listan är tom och sidan visar i stället en uppmaning att lämna omdöme.
 *
 * Lägg bara in riktiga omdömen som kunden godkänt att publicera. Exempel på format:
 *
 *   {
 *     namn: "Anna S.",
 *     ort: "Lindås",
 *     betyg: 5,                 // 1–5, valfritt
 *     datum: "2026-05",         // valfritt
 *     projekt: "Tillbyggnad",   // valfritt
 *     text: "Kundens egna ord här.",
 *     kalla: "Hitta.se"         // valfritt – var omdömet ursprungligen lämnades
 *   },
 */
window.OMDOMEN = [];
