# História balíka EA-043

## 2026-07-23 — DRAFT_NOT_DELIVERED

- nový package ID; existujúce balíky a responses zostali immutable;
- scope je T1 audit B6b-1 analytic envelopes a B6b-2
  perturbation/search/S8 passportu;
- exact input hash gate prešiel `15/15`; register pre-append SHA bol
  `835FD4E211E6237565D45B5DFB30E868409677C3700E548C9393A99409D2650B`;
- `15` single-copy evidence položiek, `7` controls a response template `1`,
  spolu `23 < 40`;
- package-curation county sú `0` live science, `1` central register a
  `1` live file total; package copies sú `22`;
- podkladový science closure mal `1` science + `4` central = `5` live
  súborov; balík ich nemení;
- `REPRO` files `0`, runtime mapa je header-only;
- balík neobsahuje Python, physical kernel/search, raw výsledok, DESI dátový
  vektor ani generated JSON;
- curator `/root/ea043_package_curator`, author `/root`, internal auditor
  `/root/b6b2_physics_auditor` a designated external auditor
  `/root/ea043_external_auditor` sú oddelené identity;
- stav čaká na R6 preflight a následný nezávislý package review;
- kurátor balík nezapečaťuje ani nevydáva auditný názor.

## 2026-07-23 — PREFLIGHT_PASSED / DRAFT_NOT_DELIVERED

- prvý PowerShell R6 preflight po vytvorení úplného obsahu prešiel `96/96`,
  exit code `0`;
- source/copy parita je `15/15`, package files `22`, response template `1`,
  `REPRO` files `0` a runtime rows `0`;
- tento lifecycle zápis nemení evidence, manifest TSV ani runtime mapu;
- po tomto zápise sa vykoná finálny R6 preflight pred register appendom;
- balík zostáva `DRAFT_NOT_DELIVERED`, nezapečatený a neodovzdaný;
- ďalšia rola je nezávislý package reviewer, nie external auditor.

## 2026-07-23 — SEALED_READY_FOR_AUDIT

- nezávislý reviewer `/root/b6b1_documentation_steward`, task
  `A2K4-EA043-INDEPENDENT-PACKAGE-REVIEW-20260723-68`, vydal
  `READY_TO_SEAL_EA043`;
- reviewer overil source/copy paritu `15/15`, ruleset/config hashe, prázdnu
  response šablónu, register a county bez nálezu;
- jeho nezávislý R6 preflight prešiel `96/96`, exit code `0`, wall `708 ms`;
- curator `/root/ea043_package_curator`, reviewer
  `/root/b6b1_documentation_steward` a external auditor
  `/root/ea043_external_auditor` sú rozdielne identity;
- external auditor pred sealom potvrdil iba identitu: čítania `0`, zápisy
  `0`, procesy `0`;
- hlavný orchestrátor `/root` vykonal lifecycle seal v tasku
  `A2K4-EA043-SEAL-20260723-69`;
- Python nebol spustený; balík neobsahuje runtime ani computed claim;
- od tejto zmeny je package immutable. Povolený je už iba post-seal
  read-only preflight, register/handoff a response mimo package.
