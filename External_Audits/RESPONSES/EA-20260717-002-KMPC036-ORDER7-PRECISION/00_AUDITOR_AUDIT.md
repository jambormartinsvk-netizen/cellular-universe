# Opakovaný externý audit R3 — `EA-20260717-002` (podľa šablóny 06)

**Auditor/prostredie:** externý fyzikálno-numerický auditor (Claude), čerstvý kontajner
**Dátum:** 2026-07-17
**Auditovaná revízia:** `R3_REFREEZE_AFTER_EXTERNAL_TECHNICAL_STOP`
**Python / NumPy / BLAS-LAPACK / OS / architektúra:** Python 3.12.3 / NumPy 2.4.4 / scipy-openblas 0.3.31 / Ubuntu 24.04 / Linux x86_64 (referencia bola Windows, Python 3.11)

---

## 1. Integrita R3

Overených **27 položiek**: 14 EVIDENCE + 6 package-control (vrátane nových 05, 06) + 5 REPRO + 2 nové prerekvizitné kópie. Všetky zmrazené súbory z R2 sú **nezmenené** (runner, tri base moduly, preregistrácia, referenčný JSON `39BB…B7B497`).

- hash KMPC-035 prerequisite v `EVIDENCE/015`: `A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`
- hash KMPC-035 prerequisite v `REPRO/`: `A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`

Obe kópie sú **byte-identické** (74 741 B) a zhodné s pinom v preregistrácii aj v base module. Deklarácia R3 „jediná obsahová oprava balenia" je pravdivá. `[INDEPENDENTLY_RECOMPUTED]`

## 2. Smoke

- presný príkaz: `timeout 10s python3 REPRO/scripts/280_script_KMPC_036_P5_3g7_M1_order7_provenance_gate.py --smoke --max-runtime-seconds 4.8`
- exit code: **0**
- wall time: **1.10 s**
- výsledok: `smoke_pass=true`, 6/6 negatívnych fixtures odmietnutých, žiadny JSON nevznikol. `[INDEPENDENTLY_RECOMPUTED]`

## 3. Oficiálna audit vetva

- presný príkaz: `timeout 10s python3 REPRO/scripts/280_script_KMPC_036_P5_3g7_M1_order7_provenance_gate.py --audit --max-runtime-seconds 4.8 --output REPRO/scripts/results/k_mpc_005/RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json`
- exit code: **0**
- wall time: **0.63 s** (interný runtime 0.201 s)
- pôvodný `FileNotFoundError` odstránený: **YES**
- generated JSON vytvorený: **YES** (69 224 B, SHA-256 `56363A8B104BD28BE5B274B088EFC71AE652F1C0E5C7FC612947FACA29E733DC`)
- technický stav: `TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT`

**Všetky tri kritériá úspechu z dokumentu 05 sú splnené** — prerekvizit nájdený a hashovo prijatý, žiadny FileNotFoundError, auditný výsledok vznikol. `[INDEPENDENTLY_RECOMPUTED]`

## 4. Nezávisle prepočítané výsledky

Porovnanie generated vs. referenčný JSON po poliach a zmrazených prahoch (bitová zhoda nebola vyžadovaná a ani nenastala — očakávane, iná platforma):

**Zhodné exaktne (24 rozhodovacích polí):** `candidate_interpretation_not_verdict = REVIEW_M1_ORDER7_CORE_OR_HOLDOUT_UNCLOSED`, `core_pass=false`, `regression_pass=true`, `shapes/rank/anchor/condition/finite/state_guard`, `dimensions`, `thresholds` (identické s preregistráciou), `source_hashes`, `scope`, triggery `NONE`. Rovnaký kandidát, rovnaký smer výsledku. `[INDEPENDENTLY_RECOMPUTED]`

- **rank:** `98/98`, aj nezávislý `numpy.linalg.matrix_rank` = 98 — zhoda. `[INDEPENDENTLY_RECOMPUTED]`
- **condition:** `634.7968462451697` vs ref `634.7968462451696` — zhoda na 1 ulp; inverse condition ≈ 1.58e-3 ≥ 1e-10. `[INDEPENDENTLY_RECOMPUTED]`
- **anchor:** `h[1]` exaktná stĺpcová eliminácia, absolútny rozdiel presne `0.0`. `[INDEPENDENTLY_RECOMPUTED]`
- **order5→7 regresie:** state aj background PASS; najhorší rozdiel `db[0]` = 1.11e-15 pri bounde 1e-14. Order-5 metadata prešli regresiou voči **skutočnému obsahu** KMPC-035 (`M1_standard_metadata`: rank 76, shape [99,77], condition 340.3205… — overené priamo proti dodanému prerekvizitu). `[INDEPENDENTLY_RECOMPUTED]`
- **driver/initial kontroly:** 121 riadkov (99 driver + 22 initial); všetky do `j=6` PASS na oboch platformách. `[INDEPENDENTLY_RECOMPUTED]`
- **holdouty:** 18/18 PASS; najhorší `Einstein_0i[7]` = 7.38e-11 (ref 3.84e-11), pod prahom 1e-10. `[INDEPENDENTLY_RECOMPUTED]`
- **floor-level riadky a absolútne rezíduá:** na tejto platforme formálne zlyhali **2 riadky** — `gamma_Euler[7]` (metrika 3.61e-10; abs 9.89e-16) a `cdm_continuity[7]` (metrika 8.65e-10; abs 2.01e-15). Pásmo absolútnych rezíduí všetkých power-7 riadkov: **2.6e-17 až 2.0e-15**, t. j. rovnaké ε-pásmo ako referencia (ref: 1.55–4.88 × ε, overené aritmeticky). `[INDEPENDENTLY_RECOMPUTED]`
- **rozdiel voči Windows referencii:** jediný pass/fail flip — `tight_coupling[7]` tu **prešiel** s 8.83e-11 (ref: fail 1.1663e-9). Maximálny rozdiel absolútnych rezíduí cez všetkých 139 riadkov je 2.5e-15. Toto je presne prípad „platformovo odlišná podmnožina floor-level failov", ktorý R3 doplnila do reprodukčného opisu: metriky sa menia o faktor ~1.3–13× len zmenou BLAS/poradia FMA operácií, zatiaľ čo absolútne rezíduá ostávajú prilepené na machine floor. Identita zlyhaných riadkov nie je fyzikálny signál. `[INDEPENDENTLY_RECOMPUTED]`

## 5. Nálezy a závažnosť

**TECHNICAL (nízka závažnosť):** Pri probe opakovaného `--audit` v tom istom strome guard správne odmietol prepísať kanonický výstup (SHA nezmenený, fail-closed failure JSON zapísaný) — no `_write_atomic_exclusive` pri kolízii vo fáze `publish` nechá v adresári **stale `.tmp-…json`** súbor, ktorý zablokuje aj budúce failure zápisy hláškou „stale temporary artifact exists". Fail-closed, teda bezpečné, ale neupratané; oprava patrí do nového skriptu, nie retroaktívne. Druhá drobnosť: existenčná kontrola výstupu beží v smoke, ale `run_audit` prepočíta celú fyziku a odmietne až pri publishi — „fail-early" check by bol čistejší.

**FORMULA/IMPLEMENTATION:** žiadny nález. Hash lineage uzavretá (zdroj → runner → JSON), regresia voči skutočnému KMPC-035 obsahu prešla, rank/anchor/holdouty potvrdené na druhej platforme.

**NUMERICAL_PRECISION:** potvrdený a cross-platformovo zdokumentovaný floor charakter troch REVIEW riadkov (ε-pásmo absolútnych rezíduí, platformovo nestabilná množina formálnych failov, metrika ~ 1/term_norm). Trvá dizajnová výhrada z R2: per-row relatívny prah delený lokálnym term_norm robí terminálne riadky s term_norm ≲ 1e-5 vo float64 predvídateľne neuzavretými, lebo chyba riešenia škáluje s globálnou normou sústavy (stavy O(1), cond ≈ 635), nie s lokálnym term_norm.

**PHYSICAL:** žiadny nález. Nič v R3 behu nenaznačuje fyzikálny rozpor; `REVIEW` ostáva numerickou, nie fyzikálnou udalosťou.

## 6. Odporúčanie

R3 **uzavrela reprodukčnú medzeru z R2** — oficiálna cesta je teraz plne reprodukovateľná a tier `T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP` považujem za **legitímne dosiahnutý** (environment gap zostáva len ako rozdiel platforiem, teraz kvantifikovaný).

Odporúčania (auditor odporúča, neprideľuje projektový PASS/REVIEW/STOP a nemení skóre ani hĺbku):

1. Ponechať projektový `REVIEW` bezo zmeny a support step 3 `BLOCKED`.
2. Po tokenovej pauze vykonať predregistrovaný `M1_ORDER7_NUMERICAL_REFINEMENT_AND_BOUNDARY_CLOSURE_AUDIT` na nezmenenej sústave a prahoch. Očakávanie auditora na základe R2 diagnostiky: krok „bounded refinement tej istej float64 matice" uzavrie všetky tri riadky s metrikami ~1e-16 pri korekcii koeficientov ≤ 6.5e-16, teda hlboko pod regresným pásmom 1e-14/1e-12; high-precision solve a native rebuild budú potvrdzujúce.
3. Do budúcich runnerov doplniť zápis NumPy/BLAS verzie do payloadu.
4. V novom skripte opraviť tmp-leak z nálezu TECHNICAL vyššie (upratanie temporary súboru pri publish kolízii, prípadne fail-early existenčný check v `run_audit`).
5. Pri cross-platform reprodukciách vyhodnocovať ε-pásmo absolútnych rezíduí a invariant metrika × term_norm, nie identitu množiny zlyhaných riadkov (R3 túto vetvu do opisu už doplnila).

## 7. Deklarované odchýlky

Mimo predpísanej R3 cesty auditor vykonal:

- (a) probe opakovaného `--audit` na overenie immutability guardu (výsledok v §5; kanonický výstup nedotknutý, SHA nezmenený);
- (b) v R2 kole modulovú rekomputáciu a bounded mixed-precision refinement diagnostiku na tej istej zmrazenej float64 matici (float64 lstsq korekcie + rezíduá v extended precision). Tá **nie je** oficiálnym R3 výsledkom a nie je zaň vydávaná; slúži len ako audítorské zdôvodnenie očakávania v §6. Jej výsledok: korekcia riešenia max 6.52e-16 na koeficient, po refinemente 121/121 driver+initial aj 18/18 holdout riadkov v zmrazených prahoch, tri sporné riadky s metrikami ≤ 2.3e-17.

Prahy, rovnice ani parametre neboli nikde menené.

---

## Záver

R3 je úspešná oprava presne toho a len toho, čo R2 audit vytkol. Oficiálna `--audit` vetva teraz beží end-to-end, generated výsledok sa s referenciou zhoduje vo všetkých rozhodovacích poliach a zmrazených prahoch a líši sa iba v ε-šume na terminálnej vrstve. Práve táto platformová nestabilita množiny formálnych failov je najsilnejší doteraz získaný dôkaz, že tri `power=7` REVIEW riadky sú float64 precision floor, a nie chyba vzorca či fyziky. Balík je pripravený na predregistrovaný precision/boundary closure audit ako posledný krok k uzavretiu order-7 proveniencie.

---

### Príloha A — súhrn R2 kola (kontext)

Prvé kolo auditu (R2, ten istý deň) skončilo: integrita 23/23 hashov PASS; smoke reprodukovaný (exit 0, 0.77 s); oficiálna `--audit` vetva `TECHNICAL_STOP` — `FileNotFoundError` na chýbajúcom KMPC-035 prerekvizite (fail-closed, korektne). Modulová rekomputácia potvrdila rank/anchor/condition/regresie/holdouty; na Linux platforme zlyhali 2 z 3 referenčných riadkov a `tight_coupling[7]` prešiel — prvý dôkaz platformovej nestability floor množiny. Hlavný nález R2 (chýbajúci prerekvizit, tier T2 nesplnený pre audit vetvu) bol v R3 odstránený jediným baliacim doplnkom s pinovaným SHA; nič zmrazené sa nezmenilo.
