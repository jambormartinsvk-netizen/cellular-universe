# Register mŕtvych koľají a ich dôkazov

**Aktualizované:** 2026-07-16  
**Pravidlo:** `Audit/00_PRAVIDLO_ARCHIVACIE_MRTVYCH_KOLAJI.md`

Tento register chráni negatívne výsledky. Uvedené skripty sa nesmú mazať. Pri vydaní sa k nim a k zmrazeným výstupom doplnia SHA-256.

## M-001 — fyzikálne „presná kalibrácia“ gridov drag/krivosti

- **Stav:** MŔTVA — ARCHIVOVANÁ.
- **Presná hypotéza:** dodané gridy predstavujú exaktnú numerickú kalibráciu úplnej fyziky modelu v3.18.
- **Dôvod smrti:** čísla sa dajú reprodukovať ako algebraická response-surface/toy transformácia referenčného bodu, ale výpočet neintegruje úplné kovariantné perturbácie, Boltzmannovu hierarchiu ani likelihood.
- **Numerický dôkaz:** `scripts/17_script_reproduce_claimed_drag_curvature_grids.py` reprodukuje tabuľky; táto reprodukcia zároveň ukazuje, že ide o parametrickú mapu, nie o nezávislú fyzikálnu pipeline.
- **Analytický dôkaz:** `Audit/AUDIT_FINAL_S8_H0_drag_curvature_v3.18_2026-07-13.md`.
- **Čo nezomrelo:** možnosť, že budúca kovariantná fyzika vytvorí podobný kvalitatívny trend.
- **Podmienka novej koľaje:** úplné `Q_A^mu`, testy A2, implementácia A3 a predregistrovaný A8.

## M-002 — S8-K1a, konštantné trenie celej látky

- **Stav:** MŔTVA — ARCHIVOVANÁ.
- **Presná hypotéza:** člen s konštantným `gamma_drag` možno pridať do jednej rovnice celkovej látky a interpretovať ho ako fyzikálne trenie popola.
- **Dôvod smrti:** formulácia nerozlišuje baryóny od popola, neurčuje kovariantný prenos hybnosti ani nositeľa protihybnosti a sama neuzatvára celkovú bilanciu `sum_A Q_A^mu=0`.
- **Numerický materiál:** `scripts/17_script_reproduce_claimed_drag_curvature_grids.py` dokumentuje numerický účinok parametra, ale fyzikálny dôvod smrti je analytický.
- **Analytický dôkaz:** `Audit/AUDIT_FINAL_S8_H0_drag_curvature_v3.18_2026-07-13.md`.
- **Čo nezomrelo:** S8-K1b, teda nová kovariantná výmena hybnosti výhradne medzi presne určenými zložkami tmavého sektora.
- **Podmienka novej koľaje:** nový identifikátor, explicitné `F_A^mu`, protihybnosť, stabilita a oddelené baryóny.

## M-003 — interpretácia `gamma=0.03` ako priamych 3 % brzdenia za e-fold

- **Stav:** MŔTVA — ARCHIVOVANÁ.
- **Dôvod smrti:** koeficient v diferenciálnej rovnici nemožno bez odvodenia stotožniť s percentuálnym poklesom fyzikálnej rýchlosti alebo amplitúdy za e-fold. Výsledok závisí od celej integrovanej rovnice a definície premennej.
- **Numerický materiál:** `scripts/17_script_reproduce_claimed_drag_curvature_grids.py`.
- **Analytický dôkaz:** finálny audit vetvy `S8/H0`.
- **Podmienka novej koľaje:** odvodiť operačnú definíciu tlmenia z kovariantnej mikrofyziky a overiť ju na riešení.

## M-004 — konkrétna kombinácia `Omega_K=0.002`, `gamma=0.015` trafí cieľ

- **Stav:** MŔTVA — ARCHIVOVANÁ.
- **Presná hypotéza:** uvedená kombinácia prinesie približne `H0=68.0` a `S8=0.82`.
- **Dôvod smrti:** reprodukovaný toy model dal približne `H0=67.26722598` a `S8=0.825146`, teda netrafil deklarovaný bod.
- **Numerický dôkaz:** `scripts/18_script_test_proposed_curvature_drag_combo.py`.
- **Analytický audit:** `Audit/AUDIT_FINAL_S8_H0_drag_curvature_v3.18_2026-07-13.md`.
- **Čo nezomrelo:** všeobecná dvojparametrová trieda; tá však nemá predikčnú hodnotu, kým parametre nie sú odvodené pred dátami.
- **Podmienka novej koľaje:** nezávislé odvodenie oboch parametrov, nie ďalšie ladenie na ten istý cieľ.

## M-005 — `Omega_K=0.005` ako dokázané dvojité vyriešenie napätí

- **Stav:** MŔTVA ako dôkaz/predikcia — ARCHIVOVANÁ.
- **Dôvod smrti:** bod je post-data výber z toy mapy, nie odvodenie krivosti zo siete; nemá úplný likelihood. Pri surovom porovnaní so SH0ES zostáva približne `-4.17 sigma` a toy bod zároveň posúva `Omega_m` do problematického smeru.
- **Numerické dôkazy:** `scripts/17_script_reproduce_claimed_drag_curvature_grids.py` a `scripts/20_script_raw_H0_residuals.py`.
- **Analytický audit:** `Audit/ADDENDUM_FINAL_S8_H0_interpretacia_Hubbleho_napatia.md`.
- **Čo nezomrelo:** fenomenologické neploché FLRW ako test a K4b ako pokus odvodiť krivosť zo siete.
- **Podmienka novej koľaje:** pred dátami odvodené znamienko i veľkosť krivosti a globálny fit CMB+BAO+SN+LSS.

## M-006 — post-data optimum ako predikcia

- **Stav:** MŔTVA ako predikcia — ARCHIVOVANÁ.
- **Presná hypotéza:** nájdenie parametrov, ktoré presne vrátia cieľové `H0` a `S8`, má predikčnú váhu.
- **Dôvod smrti:** dva voľné parametre boli vyriešené priamo z dvoch cieľových hodnôt po ich zadaní. Ide o kalibráciu, nie nezávislú predikciu.
- **Numerický dôkaz:** `scripts/19_script_postdata_toy_calibration_H0_S8.py` našiel približne `Omega_K=0.0035563999`, `gamma=0.0110528629`, ale výstup je označený `NO_PREDICTIVE_WEIGHT`.
- **Podmienka novej koľaje:** parametre určiť z mikrofyziky alebo z oddeleného tréningového datasetu a testovať na vopred odloženej validačnej množine.

## M-007 — lokálne `chi2_3front` ako dôkaz zlepšenia globálneho fitu

- **Stav:** MŔTVA — ARCHIVOVANÁ.
- **Dôvod smrti:** použitá suma nie je úplný likelihood, ignoruje relevantné covariance, nuisance parametre, `H0/Omega_m` konzistenciu, cenu nových parametrov a look-elsewhere/post-data výber.
- **Numerický materiál:** `scripts/17_script_reproduce_claimed_drag_curvature_grids.py` reprodukuje deklarovanú aritmetiku; nerehabilituje jej štatistický význam.
- **Analytický dôkaz:** finálny audit a addendum vetvy `S8/H0`.
- **Čo nezomrelo:** budúci predregistrovaný A8 likelihood.
- **Podmienka novej koľaje:** vopred definované datasety, covariance, priory, nuisance parametre a model-comparison metrika.

## M-015 — Q22a-K2, perzistentná priama produkcia voľnej pary

- **Stav:** MŔTVA — ARCHIVOVANÁ, iba v presne uvedenom rozsahu.
- **Presná hypotéza:** celý kontinuálny neskorý A1 transfer
  `q=lambda rho_f` môže ísť priamo do voľnej relativistickej pary a pritom
  zachovať registrovaný dnešný parný rozpočet `Delta N_eff=0.0535`.
- **Dôvod smrti:** pri spätnom behu od dnešnej parnej hustoty sa `rho_steam`
  stane zápornou už pri prvom kroku `|Delta ln a|<=1e-4`. To nie je solverový
  problém: dnešný zdroj je približne `0.09723`, zatiaľ čo parný inventár iba
  `6.81e-7` v rovnakých kritických jednotkách.
- **Numerický dôkaz:**
  `scripts/259_script_Q22A_S2_steam_only_delta_neff_budget_screen.py`,
  výstupy `scripts/results/q22a/RUN_Q22A_006_S2_STEAM_ONLY_DELTA_NEFF_BUDGET_SCREEN.json`
  a konvergenčný `RUN_Q22A_007_S2_STEAM_ONLY_DELTA_NEFF_BUDGET_HALFSTEP.json`.
  Polkrokové intervaly sa prekrývajú; ich stredy sa líšia o `0.37 %`.
- **Analytický kontext:**
  `Questions/Q22A_S2_STEAM_ONLY_DELTA_NEFF_BUDGET_RESULT_SK.md`.
- **Čo nezomrelo:** skorý ukončený parný relikt, odvodený sekvenčný kernel,
  reabsorbujúci medzistav ani priamy paralelný limit s
  `f_R,direct<~3.2e-5`.
- **Podmienka novej koľaje:** explicitne odvodený časový/kinetický mechanizmus
  odlišný od perzistentného priameho `F->R`; nesmie iba premenovať alebo
  post-data utlmiť ten istý zdroj.

## Reprodukčné dokumenty skriptov

- `scripts/README_AUDIT_SCRIPTS_17-19.md`
- `scripts/README_AUDIT_SCRIPT_20.md`

## Kontrola úplnosti pred vydaním

Pred publikovaním v3.18 treba pre M-001 až M-007 doplniť:

- SHA-256 každého skriptu;
- SHA-256 zmrazeného surového výstupu;
- presný reprodukčný príkaz;
- verziu Pythonu a použitých knižníc;
- odkaz z changelogu.
