# REGISTER 05 — SK dodatok k rozsudku A2-K6/M-013

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; existujúce pravidlá sa nemenia

## Kontrola duplicity

P5 už vyžaduje konvenciu a citlivosť každého čísla. Neobsahuje však
špecifickú povinnosť prepočítať maticu gravitačných väzieb pri zmene
definície zdrojovej hustoty. AR11 preto nie je duplicitné; konkretizuje novú
auditnú chybu odhalenú v K6. Q40 je nová stavová otázka.

## AR11 — Gij sa porovnáva až po mapovaní zdrojovej hustoty

Pred tvrdením `G_eff/G`, `mu_ij` alebo „slabšia/silnejšia gravitácia“ musí
audit uviesť, ktorú hustotu daný koeficient násobí. Ak zdroj používa
`rho_c`, ale auditovaný background používa `rho_c_hat=A rho_c`, musí sa
vykonať explicitný prepočet, napríklad

```text
mu_cc=G_cc/(A G),
mu_bc=G_bc/(A G).
```

Zmena definície hustoty sa nesmie vydávať za fyzikálnu zmenu gravitácie.
Oba tvary a ich nulový limit musia zostať v auditnom dokumente.

## Q40 — Môže A2-K6 vytvoriť slabú fyzickú gravitáciu popola?

**Stav:** `UZAVRETÁ — NIE; A2-K6 JE MŔTVA M-013.`

Pre akciu
`f=-f1(phi)rho_c+eta Z^2`, A1 tok, kanonické `G2=X-V` a zdravý interval
`eta>=0` vyšlo

```text
mu_cc(eta=0,z=0)=5.674661891,
lim eta->infinity mu_cc(z=0)=163.646709760.
```

`mu_cc` je na celom intervale lineárno-frakčná monotónne rastúca funkcia.
Predregistrovaný grid navyše zvýšil rastový diagnostický faktor z `1` na
`2.160409`. Oba nulové limity prešli na úrovni `1.776e-15` a `2.220e-16`;
smrť teda nespôsobila chyba znamienka ani nulového limitu.

Rozhodujúci dokument:
`Audit/A2_K6_MRTVA_M013_exact_Gij_a_spojity_eta_no_go.md`.

## Obmedzenie staršieho stavu

Záznam K6.0 `PREŽÍVA 40/100; G_eff otvorené` zostáva dôkazom prejdenej
backgroundovej a kinetickej brány, ale nesmie sa citovať ako aktuálny stav.
Od M-013 je kanonický stav A2-K6 iba `MŔTVA`.

Prvý machine-label nulového limitu v skripte 48 bol obmedzený skriptom 49:
odchýlku `5.225e-7` spôsobila okrajová numerická derivácia. Analytický tvar
prešiel a fyzikálny rozsudok smrti sa nezmenil.

