# História balíka EA-040

## 2026-07-22 — DRAFT_NOT_DELIVERED

- nový immutable package ID; EA-039 zostáva nezmenený;
- scope je statický T1 audit constraint-first mapy a screenov B0–B2;
- `15` single-copy položiek, `7` controls a response `1`, spolu `23 < 40`;
- primárny formula dokument a AR66.2 checklist sú iba v `EVIDENCE/`;
  `REPRO/` nemá žiadny súbor a runtime mapa je preto header-only;
- všeobecný R6 preflight bol opravený tak, aby header-only runtime mapu
  akceptoval iba pri presne nulovom počte fyzických `REPRO` súborov; ak je
  `REPRO` neprázdne, aspoň jeden runtime riadok zostáva povinný;
- balík neobsahuje Python, raw výsledok ani generated JSON;
- kurátor `/root` a fresh externý auditor `/root/ea040_external_audit` sú
  odlišné kanonické task identity; auditor pred sealom nečítal live projekt
  ani package a iba potvrdil `READY_FOR_SEALED_PACKAGE`;
- read-only curatorial review `/root/ea038_external_audit` vyžiadal presun
  primárneho Markdownu mimo `REPRO/` a doplnenie exact AR66.2 checklistu;
  obe korekcie boli zapracované bez vedeckej zmeny;
- prvý R6 preflight prešiel `96/96`, exit code `0`; lokálny wall time
  `2.4 s`;
- finálny read-only curatorial review overil `15/15` parity, `7` controls,
  package `22` + response `1`, nulové duplicity, prázdny `REPRO`, header-only
  runtime mapu a fail-closed preflight patch;
- review zablokoval seal do doplnenia reálnej auditor identity, exact
  `AUDITOR_RULESET_PATHS_AND_SHA256` a preflight záznamu; všetky tri
  podmienky sú teraz splnené;
- stav prechádza na `PREFLIGHT_PASSED`; po opravnom preflighte možno package
  zapečatiť bez ďalšej obsahovej zmeny.

## 2026-07-22 — SEALED_READY_FOR_AUDIT

- opravný R6 preflight po reálnej auditor identity a ruleset markerov prešiel
  `96/96`, exit code `0`, wall time `1182 ms`;
- source/copy parita `15/15`, package files `22`, response `1`, spolu `23`;
- `REPRO` files `0`, runtime map rows `0`, duplicate hash groups `0`;
- external auditor `/root/ea040_external_audit` je fresh, odlišný od kurátora
  aj curatorial reviewera a pred sealom nečítal obsah;
- Python nebol spustený, nevznikol raw výsledok ani nový vedecký verdikt;
- po finálnom kontrolnom preflighte je package immutable.
