# A2-K4 / K7b P0 — konečný segmentovaný fail-closed audit

Dátum: 2026-07-15  
Verdict: **PASS_C7_7C_K7B_P0_SEGMENTED_FAIL_CLOSED_REGRESSION**  
Hĺbka A2-K4: **66.5/100**, bez zmeny  
Rozsah: validačná brána metadát a regresia koeficientov/constraintov; bez ODE evolúcie

## Výsledok jednou vetou

Pôvodná latentná chyba `None == None` je uzavretá fail-closed: pozitívne prípady zachovali fyziku bitovo, každý samostatne chýbajúci rank kľúč aj oba chýbajúce kľúče skončili REVIEW s presne tromi zlyhanými rank checkmi.

## Pozitívne prípady

| Prípad | Exit | D activity rel. | Stav/allowance | RHS/allowance | Verdict |
|---|---:|---:|---:|---:|---|
| B-NID-D / 175 | 0 | `5.951092201666446e-3` | `9.40216128693087e-6` | `8.591785327983005e-13` | PASS |
| B-NID-S / 175 | 0 | `1.0921373772368643e-4` | `8.008345561921744e-6` | `6.34852107741292e-12` | PASS |
| C-NID-D / 192 | 0 | `5.951092201666446e-3` | `9.40216128693087e-6` | `8.591785327983005e-13` | PASS |
| C-NID-S / 192 | 0 | `1.0921373772368643e-4` | `8.008345561921744e-6` | `6.34852107741292e-12` | PASS |
| NIV-D / 166 | 0 | n/a | `3.212661495674644e-5` | `3.550307606751329e-11` | PASS |
| NIV-S / 166 | 0 | n/a | `3.8442168649492025e-5` | `2.6233339451805013e-10` | PASS |

Všetky hodnoty prešli predregistrovanou relatívnou toleranciou `1e-4`. Kandidátsky solver mal presne `fixed_count=30`, `free_count=58`, `reduced_rank=58`, `hard_conflict_count=0` a fixed-anchor error pod `1e-60`.

## Exact regresia fyziky

Kanonický fyzikálny payload zahŕňal background, projected seeds, state comparison, všetkých 13 RHS auditov, najhoršie pomery, D activity a solver audit. Runtime, názov testu, verdict a fault metadata boli vylúčené.

| Povrch | Baseline 175 SHA-256 | Kandidát 192 SHA-256 | Výsledok |
|---|---|---|---|
| NID/deep | `0a06bfd53fc8f080305a9eb7c1c98f3e5d7905359fae10bd3b775b3164df720a` | `0a06bfd53fc8f080305a9eb7c1c98f3e5d7905359fae10bd3b775b3164df720a` | exact |
| NID/shallow | `0e38b355fd284a7be8fe5cd1e2958584e8468b03720051179a8107df289f8254` | `0e38b355fd284a7be8fe5cd1e2958584e8468b03720051179a8107df289f8254` | exact |

## Negatívne kontroly

| Fault | Exit | Odstránené | Zlyhané checky | Výsledok |
|---|---:|---|---|---|
| `reduced_rank` | 1 | `reduced_rank` | presence, plain-int type, guarded full-rank | PASS negatívnej brány |
| `free_count` | 1 | `free_count` | presence, plain-int type, guarded full-rank | PASS negatívnej brány |
| `both` | 1 | oba kľúče | presence, plain-int type, guarded full-rank | PASS; žiadne `None == None` |

Vo všetkých troch prípadoch zostali D, state a RHS metriky rovnaké ako C-NID-D a dynamics fingerprint bol exact. Fault injection menila iba solver metadata pred validačnou bránou.

## Zachované neúspechy

- 189: `DO_NOT_RUN_TECHNICAL`, PF-012 — parser marker bol patchovaný o jednu generovanú vrstvu priskoro;
- 190: technicky nepoužiteľný pre závislosť od 189;
- 193: `SUPERSEDED`, monolitický agregátor skončil na predregistrovanom internom limite 15 s;
- 192: opravená aktívna fail-closed brána;
- 195: autoritatívny čisto offline agregátor;
- 196: aktuálny korpusový checker.

## Reprodukčné kotvy

- manifest segmentov: `Audit/A2_K4_K7B_P0_SEGMENT_MANIFEST_2026-07-15.json`;
- manifest SHA-256: `4c3805250a7da6fc1409f76eaef3362005a43b807b53a4d7b01f1ee437bd163c`;
- offline výsledok: `Audit/A2_K4_K7B_P0_SEGMENTED_OFFLINE_RESULT_2026-07-15.json`;
- offline výsledok SHA-256: `771ADCE48E6EB776FABB5E7627A27D6C403C7C3B4C916BDE58D808D934386E69`;
- korpus: checker 196, 200 ostatných `.py`, 68 karanténnych položiek, PASS.

## Fyzikálny význam a hranica tvrdenia

PASS dokazuje, že K7b coefficient/initial-constraint výsledok nie je závislý od fail-open rank metadát a že hardening nezmenil serializovanú fyziku. Nedokazuje ODE evolúciu, endpoint agreement, Boltzmannovu hierarchiu, CMB likelihood ani správnosť K7c. Preto sa hĺbka 66.5/100 nemení.

## Rozhodnutie

P0 je **dokončené**. Ďalší krok je P1: čistá samostatná RK4 reprodukcia 184/185 podľa už zmrazených očakávaní. Potom P2: nový M-prime ledger namiesto blokovaného 186.
