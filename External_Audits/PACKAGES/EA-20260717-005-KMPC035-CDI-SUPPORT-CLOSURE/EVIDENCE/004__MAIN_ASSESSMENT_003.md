# Hlavný posudok externého auditu EA-20260717-003

**Dátum:** 2026-07-17  
**Externá odpoveď:** `00_AUDITOR_AUDIT.md`  
**Autorita:** hlavný orchestrátor  
**Spracovanie:** `ACCEPTED_WITH_LIMITATIONS_AND_FOLLOWUP_REQUIRED`

## Autoritatívny rozsudok spracovania

```text
PACKAGE_TIER = T1_PRIMARY_FORMULA + PARTIAL_RECOMPUTATION_DEVIATION
OFFICIAL_T2 = NOT_ACHIEVED_MISSING_RUNTIME_PREREQUISITE
PROJECT_VERDICT = UNCHANGED
```

Existujúci route-local výsledok zostáva:

```text
PASS_CDI_SUPPORT_STEP_2_CORE_AND_COMMON_03_05_STABILITY_ONLY /
REVIEW_CDI_SUPPORT_03_REMAINDER_UNCLOSED
```

A2-K4 zostáva `LIVE / 60/100`. Audit nemení skóre, predikcie, release,
Zenodo ani poradie fyzikálnych brán a neodomyká CDI support step 3.

## Prijatý prínos

1. Nález F1 je potvrdený zo zdroja: KMPC-034 JSON s hashom
   `37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20`
   chýba v balíku, hoci ho povinne načítava `run_smoke` aj `run_audit`.
2. Deklarovaná direct-solver odchýlka na Linuxe zopakovala ranky, residualy,
   holdouty, common stability a presný tail-failure pattern. Je to silná
   podpora existujúcej interpretácie, nie oficiálna T2 reprodukcia.
3. F3 správne oddeľuje autoritatívny absolute fallback od diagnostickej
   would-be relatívnej metriky.
4. F4 správne obmedzuje dvojčlenný remainder: budúci PASS je lokálna nutná,
   nie postačujúca podmienka konvergencie nekonečného radu.
5. F5 je potvrdený staticky: historický runner 279 nemá cleanup temp súboru
   vo `finally` po publish kolízii.
6. F6 a F7 sú prijaté ako procesné a metodické obmedzenia.

## Prijaté iba s obmedzením

- Pozorovaný cross-platform drift `1.7e-11` je dôležitý, ale jeho označenie
  za „čisto BLAS drift“ je zatiaľ inferencia. Zmrazený projektový prah
  `1e-12` sa spätne nemení.
- Nový voľnejší cross-platform prah môže existovať iba v novom
  predregistrovanom balíku ako `DIAGNOSTIC_ONLY / verdict_effect=NONE`.
- Exact rational solve tej istej implementácie odstráni FP neistotu, ale
  neuzavrie riziko spoločného equation-engine omylu. Na T3 je potrebný
  nezávislý row/equation builder.
- Odhad, že `[0,5]→[0,7]` prejde, je testovateľná hypotéza, nie výsledok a
  nesmie ovplyvniť prah ani obísť KMPC-036 precision closure.

## Náprava

Balík 003 ani runner 279 sa neprepisujú. Vzniká nový follow-up balík
`EA-20260717-005-KMPC035-CDI-SUPPORT-CLOSURE`, ktorý obsahuje:

- chýbajúci KMPC-034 JSON v `EVIDENCE/` aj presnej runtime ceste `REPRO/`;
- strojový source/copy manifest a runtime dependency mapu;
- technického reprodukčného nástupcu s nezmenenými fyzikálnymi prahmi;
- environment a BLAS/LAPACK metadata;
- collision-safe immutable publish a negatívny fixture;
- would-be relative a z-scan diagnostiku bez verdict effect;
- oddelený official audit a cross-platform diagnostic výsledok.

Globálny protokol balíkov sa povyšuje na R3 a pred stavom READY vyžaduje
strojový package preflight.
