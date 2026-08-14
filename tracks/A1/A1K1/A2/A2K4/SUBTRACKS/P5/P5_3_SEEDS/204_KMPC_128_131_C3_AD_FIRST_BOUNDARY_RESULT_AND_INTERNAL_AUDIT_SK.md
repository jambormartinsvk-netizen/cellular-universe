# KMPC-128 až 131 — C3 AD prvá hranica, výsledok a interný audit

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `AD_C3_PARTIAL / K0P005_PAIR_PASS / K0P05_SUPPORT_REVIEW / K0P15_NOT_RUN`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autoritatívny dopad:** K4 `60/100`, P5 `3.5/6`, score/release/Zenodo bez
zmeny.

## 1. Výsledok ľudskou rečou

Prvý úplný C3 nulový pár `AD/k=.005` prešiel. `gamma0` aj `af0` mali PASS
pre core, accepted/audit solve, common coefficient bridge, tail, S-C0,
background, vlastný nulový limit a pri `af0` aj most k immutable nominal
koeficientom.

Nasledujúci `AD/k=.05` bol technicky úplný, ale oba nulové varianty skončili
predregistrovaným `REVIEW_C3_SUPPORT_EXTENSION_REQUIRED`. Nezlyhala rovnica,
Bianchi, nulový limit ani nominal bridge. Zlyhal iba tail pri historickom
supporte `[0,2]→[0,4]`; nuly zmenili koeficientový rozvoj natoľko, že tento
support už nie je dostatočný. `AD/k=.15` sa podľa fail-fast poradia nespustil.

## 2. Immutable dôkazy

| Beh | Stav | SHA-256 |
|---|---|---|
| KMPC-128 AD/.005 | PF-117 timeout po `gamma0`, bez verdiktu | `E974DEE195641A68CA753074E73D416E53EFC471A09473929560950E8825E3D9` |
| KMPC-130 AD/.005 | PF-119; `gamma0` partial PASS, `af0` timeout, bez finálneho verdiktu | `01E9498EC21C9BA2229CE77416A0E906FF804BA7CF4D7C898CC7CC252EFFB5C6` |
| KMPC-131 AD/.005 | `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY` | `D3FB5710390B3395212067B8BC968E48AEBA04AF9A0D38A4313195A39C6B3DAA` |
| KMPC-131 AD/.05 | `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED` | `1D239D5C94D24C4FD52AC094043A505D41CBDADCA62E6E98A9B2F76A9BAE76E1` |

PF-118 vznikla iba v smoke runnera 373; žiadny raw ani solve nevznikol.
Technická línia 128→131 zmenila iba granularitu procesu. Zdroj rovníc
`full_ra_m3_seed.py` ostal na SHA
`070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` a
C2 helper na SHA
`757F97E14657CC7046177C2D33115CA87639B9C92E89BDABE2BFF3B4380DF3FC`.

## 3. AD/.005 audit

| Brána | gamma0 | af0 |
|---|---|---|
| core + M1 + B1/TCA0 + accepted/audit | PASS | PASS |
| common accepted→audit | PASS | PASS |
| tail na `z=1e-4,1e-2` | PASS | PASS |
| S-C0 a background | PASS | PASS |
| vlastný nulový limit | PASS | PASS |
| nominal coefficient bridge | n/a | PASS |
| logický atóm | PASS | PASS |

Najpomalší support worker trval `3.235 s < 4.8 s`; ostatné boli
`2.203–3.078 s` podľa terminal summary. Parent solver calls boli nula.

## 4. AD/.05 audit a presný blocker

Všetky netail brány boli true pri oboch variantoch. Tail limit bol nezmenený
`1e-6`.

| variant | sektor, `z` | najhorší stav | metrika | násobok limitu |
|---|---|---|---:|---:|
| gamma0 | F0, `.01` | `delta_f` | `2.814480743e-3` | `2814.48×` |
| gamma0 | M3, `.01` | `eta` | `3.281732116e-3` | `3281.73×` |
| af0 | F0, `.01` | `delta_f` | `2.814480884e-3` | `2814.48×` |
| af0 | M3, `.01` | `eta` | `3.281732115e-3` | `3281.73×` |

Aj na `z=1e-4` je najhorší relatívny tail približne
`2.81e-5` (F0) a `3.28e-5` (M3), stále nad `1e-6`. Zlyhanie teda nie je
float64 šum ani prepis poslednej cifry. Takmer rovnaké gamma0/af0 hodnoty a
súčasný PASS nominal-af0 coefficient bridge ukazujú na nedostatočnú hĺbku
supportu, nie na porušenie nulového limitu.

## 5. Autoritatívne vyhodnotenie

- `AD/.005/gamma0` a `AD/.005/af0`: scoped PASS;
- `AD/.05/gamma0` a `AD/.05/af0`: REVIEW, support extension required;
- `AD/.15/gamma0` a `AD/.15/af0`: NOT_RUN by preregistered fail-fast;
- AD mód C3: `5/9` logických atómov PASS (tri už prijaté nominal + dva nové
  nulové atómy na `.005`);
- globálne C3: `17/45` logických atómov PASS, z toho nové nulové varianty
  `2/30`; aggregate zakázaný;
- nejde o fyzikálny STOP A2-K4 a nejde o dôvod meniť score.

## 6. Ďalší predregistrovaný krok

Samostatný support successor pre `AD/k=.05` smie skúsiť iba najbližší
monotónny pár `[0,4]→[0,6]` s M1 depth `6`, pri rovnakých rovniciach,
plochách a prahoch. Najprv musí vzniknúť nová predregistrácia a source hash
freeze. Ak `[0,4]→[0,6]` prejde, nahradí iba dve REVIEW nulové vetvy; nominal
KMPC-028/031 sa neprepisuje. Ak tail znovu zlyhá, ďalší support sa nesmie
domyslieť po výsledku bez nového ledgeru.

## 7. Súborová a procesná kontrola R5

Do tohto closure vzniklo alebo sa zmenilo `20` live projektových súborov:
`3` živé pravidlá/registre, `4` predregistrácie, `4` base moduly, `4`
runnery, `4` immutable rawy a tento interný audit. Vyšší počet než pôvodný
plán spôsobili tri povinne zachované technické nástupníctva PF-117 až
PF-119; nie je to 20 zmien rovníc. Vedecký source ostal jeden a rovnice sa
nemenili.

EA-030 musí použiť R5 single-copy capsule, osobitne uviesť
`LIVE_FILES_CHANGED=20` a `AUDIT_PACKAGE_COPIES`, neprekročiť 40 fyzických
súborov a nesmie kopírovať runtime položku súčasne do `EVIDENCE/` aj
`REPRO/`.
