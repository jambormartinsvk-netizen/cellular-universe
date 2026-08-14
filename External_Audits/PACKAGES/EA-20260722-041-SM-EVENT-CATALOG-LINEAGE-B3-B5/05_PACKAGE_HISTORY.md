# História balíka EA-041

## 2026-07-22 — DRAFT_NOT_DELIVERED

- nový immutable package ID; EA-040 zostáva nezmenený;
- scope je statický T1 audit ucelenej časti B3–B5;
- `15` single-copy položiek, `7` controls a response `1`, spolu `23 < 40`;
- primárny dokument je iba v `EVIDENCE/`; `REPRO/` je prázdne a runtime
  mapa header-only;
- balík neobsahuje Python, raw výsledok ani generated JSON;
- autor teórie Martin Jambor; formalizácia a skripty Codex;
- kurátor `/root` a fresh externý auditor `/root/ea041_external_audit` sú
  rozdielne task identity; auditor pred sealom nečítal evidence;
- prvý R6 preflight odhalil iba chýbajúci exact header `## Nonclaims`; po
  oprave prešiel `96/96`, exit code `0`, wall time `1276 ms`;
- read-only curatorial review potvrdil `15/15`, controls `7`, package `22`
  plus response `1`, duplicity `0`, `REPRO/runtime=0` a dostatočný B3–B5
  evidence scope; pred sealom vyžiadal plnú R6 response šablónu a kanonické
  tokeny `PASS_B3` a `PASS_DEFINITION_INVENTORY`;
- obe kurátorské korekcie boli zapracované bez vedeckej zmeny;
- skutočný fresh agent `/root/ea041_external_audit` bol vytvorený pred
  sealom a potvrdil iba identitu a pripravenosť, bez čítania evidence;
- opravný R6 preflight po response/token korekciách prešiel `96/96`, exit
  code `0`, wall time `1088 ms`;
- root kontrola agentového stromu s exact
  `path_prefix=/root/ea041_external_audit` vrátila existujúceho agenta v
  stave `completed: ready`; ide o tú istú deklarovanú fresh identitu;
- stav čaká už iba na finálne kurátorské `READY_TO_SEAL`.

## 2026-07-22 — SEALED_READY_FOR_AUDIT

- finálny read-only curatorial review udelil `READY_TO_SEAL_EA041`;
- jeho kontrolný R6 preflight prešiel `96/96`, exit code `0`;
- bezprostredný pre-seal root preflight prešiel `96/96`, exit code `0`,
  wall time `1116 ms`;
- source/copy parita `15/15`, package files `22`, response `1`, spolu `23`;
- `REPRO` files `0`, runtime map rows `0`, duplicate hash groups `0`;
- external auditor `/root/ea041_external_audit` je fresh a odlišný od
  kurátora aj reviewerov; pred sealom nečítal evidence;
- Python nebol spustený, nevznikol raw výsledok ani vedecký verdict;
- po tejto lifecycle zmene je package immutable; nasleduje iba kontrolný
  post-seal preflight a odovzdanie auditorovi.
