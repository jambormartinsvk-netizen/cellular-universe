# A2-K4 / C7.7c / K7d — finálny audit integrovanej brány G4+G6+G7

**Dátum:** 2026-07-15  
**Stabilné ID:** `SCI-A2K4-C7G467-K7D-INTEGRATED`  
**Rozsudok:** `PASS_K7D_C7_G4_G6_G7_INTEGRATED`  
**C7-G4:** PASS  
**C7-G6:** PASS  
**C7-G7:** PASS  
**Fyzikálny stav A2-K4:** ŽIVÁ

## Ľudský výsledok

Projektovaná K7 formulácia prešla celým požadovaným skorým intervalom na
štyroch počiatočných plochách: NID aj NIV, deep aj shallow. Všetkých 13
registrovaných komponentov bolo numericky rozlíšených, druhová formulácia a
projektovaná formulácia sa po správnom high-precision audite zhodli a
Einsteinove trace/traceless ledgery zostali konzistentné. Hlboký a plytký
štart toho istého módu dali na `x=-18` prakticky identický stav.

K7 teda nenarazila na stenu G4/G6/G7. Výsledok však ešte nepoužíva plnú
fotónovú/neutrínovú hierarchiu a nie je CMB/S8 testom.

## Zmrazený kontrakt

- štyri prípady: NID/NIV × deep/shallow;
- deep `x=-25→-18`, shallow `x=-23→-18`;
- DOP853, `rtol=1e-11`, normalizované `atol=1e-13`, `max_step=0.05`;
- checkpoint každých `0.25` e-foldu;
- 13 projektovaných zložiek, rovnaký background a RHS ako P4a;
- closure `L5=0` ostáva do G8;
- každý prípad mal interný limit 25 s, externý 30 s, RHS cap 100000 a
  normalizovaný safety cap `1e8`.

## Výsledok štyroch prípadov

| Prípad | Checkpointy | nfev | max `|w|` | min. activity signál | HP parita max | trace max/allow | traceless max/allow | Stav |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| NID-deep | 29 | 1781 | `1.000007668` | `4.12e-8` (`delta_gamma`) | `2.28e-72` | `9.86e-55` | `2.56e-47` | PASS |
| NID-shallow | 21 | 1277 | `1.000007667` | `4.12e-8` (`delta_gamma`) | `1.90e-72` | `9.86e-55` | `2.56e-47` | PASS |
| NIV-deep | 29 | 1781 | `1.000000027` | `9.9996e-1` (`M`) | `1.03e-70` | `3.16e-50` | `1.21e-43` | PASS |
| NIV-shallow | 21 | 1277 | `1.000000027` | `1.353e-1` (`U_gamma`) | `2.84e-71` | `3.16e-50` | `1.21e-43` | PASS |

`max/allow` je najväčší pomer absolútneho rezídua k vopred určenej mixed
hranici `1e-12+1e-8·norm`; PASS vyžaduje hodnotu `<=1`. Extrémne malé HP
čísla neznamenajú nový empirický dôkaz. Vyjadrujú algebraickú konzistenciu
matter product-rule a Einsteinovho ledgeru pri 80 dps.

## G7 deep/shallow zhoda

| Mód | Endpoint L2 | Prah | Endpoint envelope max | Prah | Overlap max | Prah | Stav |
|---|---:|---:|---:|---:|---:|---:|---|
| NID | `1.5773e-16` | `3e-3` | `3.4207e-10` | `1e-2` | `3.9210e-10` | `2e-2` | PASS |
| NIV | `6.0589e-16` | `3e-3` | `3.0252e-12` | `1e-2` | `3.5169e-12` | `2e-2` | PASS |

## Dôležitý audit opráv V1/V2

Prvá raw NID-deep trajektória mala správny solverový výsledok, ale chybnú
diagnostiku. Raw FAIL sa preto zachováva a je obmedzený týmto auditom.

1. **FE-K7D-01:** species derivácia bola zamenená za species stav v tlaku a
   šmyku. Vytvorila falošný trace FAIL.
2. **FE-K7D-02:** diagnostika znovu skladala kompenzované `D,M` vo float64 a
   obnovila známu cancellation chybu K1–K6.
3. **FE-K7D-03:** aj opravený float64 product rule ponechal v `D_x`
   absolútny roundoff približne `3.9e-21`; V2 preto použila 80 dps.
4. **FE-K7D-04:** starší ledger zamieňal multipól `F2=2σ` s K7 premennou
   `σ`. Správny zdroj je `S=(4/3)Ω_fs σ_fs`.

V1 znížila paritu `3.6841e-2 → 2.2169e-7`; V2 ju znížila na `2.28e-72` a
opravila traceless konvenciu. ODE sa ani raz neopakovala a fyzická RHS,
parametre, seedy, intervaly a prahy sa nezmenili. Obe povolené technické
opravy sú spotrebované; pre tento balík nevznikne V3.

## Prečo G4 nie je dvojito započítaná

Trace/traceless ledgery nie sú self-checky typu
`rhs[0]-(3D+2s²eta)`. Jedna implementácia počíta druhové continuity/Euler
rovnice a product-rule `D_x,M_x`; druhá vyhodnocuje Einsteinove rovnice.
Všeobecná relativita ich spája Bianchiho identitou, preto ich takmer presná
zhoda je očakávaná konzistencia, nie nezávislé štatistické meranie. Celý
výsledok dostáva iba jedinú váhu G4=15; trace, traceless, product parity a
activity sa nesčítajú ako štyri dôkazy.

## Skóre a vzdialenosť k ďalšej stene

- C7-W1 strict support: `60 -> 90/100`;
- úplné gate pokrytie: `60 -> 90/100`;
- blocker: `0/100`;
- otvorené: `40 -> 10/100` (`G8=5`, `G9=5`);
- WBS-1 progress: `60 -> 90/100`;
- jemná staniciová hĺbka A2-K4 zostáva `66.5/100` do samostatného depth
  crosswalku.

Najbližšia stena je **C7-G8**, plná fotónová/neutrínová Boltzmannova
hierarchia. Po nej zostáva G9 CMB/S8 likelihood. Numerické jadro K7d je
dokončené, ale A2-K4 ani celá K7 ešte nemajú finálny observačný verdikt.

## Čo PASS nedokazuje

- closure nad `L4` ešte nie je nahradená plnou hierarchiou;
- chýba recombination a baryón-fotónový backend;
- nebol počítaný CMB power spectrum ani likelihood;
- nebol vypočítaný neskorý rast, `S8` ani nový `H0`;
- PASS nie je dôkaz pravdivosti celej teórie, iba uzavretie G4/G6/G7.

## Autoritatívne dôkazy

- preregistrácia: `Questions/A2_K4_C7_7C_K7D_G4_G6_G7_INTEGRATED_PREREGISTRATION_2026-07-15.md`;
- preflight: `Audit/A2_K4_K7D_G4_G6_G7_PREFLIGHT_214_RAW_2026-07-15.json`;
- input pack: `Audit/A2_K4_K7D_G4_G6_G7_INPUT_PACK_213_RAW_2026-07-15.json`;
- štyri V2 corrected JSON: NID-deep, NID-shallow, NIV-deep, NIV-shallow;
- agregát: `Audit/A2_K4_K7D_G4_G6_G7_AGGREGATE_213_V2_RAW_2026-07-15.json`;
- skripty: 213, 214, 215, 216;
- manifest: `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/C7_7c/K7/K7d_FULL_ACTIVITY/ARTIFACTS/00_MANIFEST.md`.

