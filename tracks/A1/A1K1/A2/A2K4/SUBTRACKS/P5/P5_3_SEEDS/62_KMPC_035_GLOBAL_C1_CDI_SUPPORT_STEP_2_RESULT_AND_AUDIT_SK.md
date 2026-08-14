# KMPC-035 — GLOBAL_C1 CDI support step 2: výsledok a audit

**Dátum:** 2026-07-17  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / CDI_SUPPORT_STEP_2`  
**Hlavný rozsudok:**
`PASS_CDI_SUPPORT_STEP_2_CORE_AND_COMMON_03_05_STABILITY_ONLY / REVIEW_CDI_SUPPORT_03_REMAINDER_UNCLOSED`  
**K4:** `LIVE / 60/100`; bez zmeny skóre alebo hĺbky

## 1. Čo sa počítalo

V tom istom zmrazenom CDI atóme (`k=0.05 Mpc^-1`, nominal variant,
conditional S-C0) sa porovnali supporty `[0,1]`, `[0,3]` a `[0,5]`.
`[0,1]` bol regression anchor z KMPC-034, `[0,3]` kandidát a `[0,5]`
nezávislý audit kandidáta. Nové členy `4,5` sa hodnotili cancellation-safe
obálkou `|c4|z^4+|c5|z^5`; signed súčet bol iba diagnostický.

| Artefakt | SHA-256 |
|---|---|
| base `cdi_support_ladder.py` | `A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068` |
| runner 279 | `09F86A2A6E8BA81F4F41C73722BC40264888D1EF45BB4016F223A5E2C76649E3` |
| immutable výsledok KMPC-035 | `A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01` |

Kanonický výsledok je
`scripts/results/k_mpc_005/RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json`.
Historický token názvu `C2` nie je globálna Fourierova C2 brána.

## 2. Technická integrita

- compile base, compile runner, help a smoke prešli;
- audit skončil `exit 0`, wall `3.0 s`, interný runtime `1.609 s < 4.8 s`;
- existuje iba success JSON; failure ani temp artefakt nezostal;
- všetkých 11 zdrojových hashov sa zhoduje a JSON nemá nefinálne čísla;
- vecný výsledok resetoval aktívne technické chyby tejto línie na `0/10`.

## 3. Prejdené brány

| Brána | Výsledok | Presný význam |
|---|---|---|
| immutable KMPC-034 regression | PASS | exportované `[0,1]/[0,3] × F0/M3` mapy sa reprodukovali |
| core `[0,1]/[0,3]/[0,5]` | PASS | plné ranky F0 `4/8/12`, M3 `26/52/78`; driver a nezávislé `00/0i` holdouty PASS |
| regularita/contract | PASS | forbidden, production a `U_c` guardy PASS |
| common bridge `0..3` | PASS | F0 max relative drift `1.1548e-14`; M3 `6.6107e-13` pri prahu `1e-8` |
| conditional S-C0 | PASS_SCOPE | algebraický lift/collapse guard; nie species dynamika |
| pure tail pri `z=1e-4` | PASS | F0 aj M3 |
| pure tail pri `z=1e-2` | FAIL | presne F0 `delta_f` a M3 `sigma_fs` |

Jadro teda nekoliduje s constraintmi ani regularitou a spoločné koeficienty
sú stabilné. Tento PASS je lokálny; neudeľuje celý CDI seed, P5.3 ani G8.

## 4. Prečo tail FAIL nie je numerický artefakt

| Sektor/stav | Candidate base `[0,3]` | Obálka `4,5` | Relatívna metrika | Prah |
|---|---:|---:|---:|---:|
| F0 `delta_f` | `1.7075415368e-9` | `4.3098625669e-14` | `2.5240162385e-5` | `1e-6` |
| M3 `sigma_fs` | `4.6216105734e-10` | `1.4866369576e-12` | `3.2167075395e-3` | `1e-6` |

Fyzický prvý koeficient je `j=2` pre `delta_f` a `j=3` pre `sigma_fs`.
Ich bases sú približne `1707×` a `462×` nad absolute-branch hranicou, takže
nejde o delenie nulou. Pomer `|signed|/envelope` je `0.999267` a `0.999112`;
zlyhanie teda nevytvorila kancelácia znamienok. `sigma_fs` obálka by navyše
zlyhala aj absolútnym prahom `1e-12`.

Rozsudok je preto presný: support `[0,3]` nestačí na predregistrovanú
per-state presnosť na celej ploche do `z=0.01`. Nejde o smrť CDI alebo K4;
žiadny potvrdený fyzikálny zákon ani constraint nebol porušený a remainder
sa oproti predchádzajúcemu support kroku výrazne zmenšil.

## 5. Hranica ďalšieho kroku

Priamy `[0,5]→[0,7]` beh je zatiaľ zakázaný. Aktuálny ukotvený štandardný
M1 zdroj končí na `order=5`; priamy beh by chýbajúce štandardné koeficienty
`j=6,7` potichu nahradil nulou.

Nasledujú dve sekvenčné fail-closed brány s dvoma immutable výsledkami.
Skript ani jeden spoločný proces nesmie kandidátskym výsledkom fázy 1 sám
autorizovať fyzický výpočet fázy 2:

1. **KMPC-036 — M1 order-7 provenance gate:** ukotvený seed `order=7`, očakávaný full
   vector `11×9=99`, po hard anchore `98` neznámych, matica `121×99`;
   explicitné holdouty pre powers `-1..7`; common M1 `-1..5` musí
   reprodukovať order-5 seed.
2. **Nový run po autoritatívnom PASS KMPC-036 — GLOBAL_C1 /
   CDI_SUPPORT_STEP_3:** immutable
   regresia `[0,3]` a `[0,5]`, candidate `[0,5]`, audit `[0,7]`, počty F0
   `12/16`, M3 `78/104`, common bridge `0..5` a autoritatívna obálka iba
   powers `6,7` voči baseline `1..5` na rovnakých plochách a prahoch.

Bez autoritatívneho PASS hlavného auditora pre KMPC-036 sa druhý run ani
nepredregistruje. Ak STEP_3 neprejde, nesmie automaticky
vzniknúť `[0,9]`; najprv sa audituje rast koeficientov, asymptotický pomer,
polomer konvergencie a prípadná zmena premennej/série.

## 6. Autorita a nonclaims

Nezávislý fyzikálny auditor odporučil scoped PASS jadra/common a REVIEW
remainderu. Nezávislý matematický auditor potvrdil, že tail FAIL nie je
denominator, cancellation ani conditioning artefakt a zachytil povinnú M1
order-7 bránu. Dokumentačný steward potvrdil immutable artefakt a nulové
release triggery. Autoritatívny rozsudok v hlavičke udelil až hlavný agent.

Výsledok nič netvrdí o BI/NID/NIV, iných `k` alebo variantoch, S-M pôvode
pary, interných nu-steam módoch, species-resolved `F_l>=3`, full hierarchy,
ODE, finite opacity, G8/G9, BBN/CMB/CLASS, `S8/H0` ani celej teórii.

`SCORE_EFFECT=NONE`, `PREDICTION_TABLE_EFFECT=NONE`,
`RELEASE_TRIGGER=NONE`, `ZENODO_TRIGGER=NONE`. Theory a bilingválny dokument
05 sa týmto lokálnym support výsledkom nemenia.
