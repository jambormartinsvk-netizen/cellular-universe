# A2-K4/P5.3g7 — audit uzavretia vstupov pre plný dvojštartový seed

**Dátum:** 2026-07-16  
**Rozsudok:** `REVIEW_BLOCKED_INPUT_CLOSURE`; nejde o fyzikálnu smrť A2-K4.  
**Dôsledok:** skript 261/plný residual sa zatiaľ nesmie napísať ako keby už
existoval úplný seedový vektor.

## Čo už je pre full seed k dispozícii

| Sektor | Stav | Zdroj |
|---|---|---|
| štandardné hustoty, `q_gamma`, `q_nu`, `eta_s` pre AD/CDI/BI/NID/NIV | formulačný zdroj dostupný | script 84 |
| palivo a popol pre štandardné módy pri zadanom `h_x=H a^n` | leading formula PASS | P5.3b/P5.3d |
| neutrínový `l=2` | formula PASS | 254 / RUN 017 |
| photon/polarization TCA blok a synchronná shear mapa | formula PASS | 255 + 260 / RUN 018+021 |
| skorý opacity časový rád a samostatné hybnosti | formula PASS | 256 / RUN 019 |

## Dva chýbajúce vstupy

1. **Úplný K4-spätne viazaný synchronný metrický seed.** Script 84 vracia
   `eta_s`, ale nie `h`, `hdot`; následná zdrojová mapa BMT ich už dáva pre
   štandardný nulový limit (pozri `P5_3_SEEDS/26...`). P5.3d však určuje tmavý
   sektor iba pod podmienkou všeobecného `h_x=H a^n`; neodvodil spätný K4
   príspevok do `h,eta` ani ho nepripojil k `00`, `0i`, trace a traceless
   rovniciam. Bez toho by test rezíduí implicitne vybral K4 amplitúdu z
   constraintu, ktorý má testovať — to by bolo kruhové.
2. **Para S1.** Plný P5 stav obsahuje `delta_s,U_s,sigma_s,...`, ale zdroj
   84 má iba fotóny a štandardné neutrína. Adiabatické zdieľanie seedov S1 je
   možná **podmienená testovacia voľba**, nie odvodený fakt: Q18/Q22 stále
   nemajú mikrofyzikálny zdroj pary ani jej počiatočný korelačný stav.

## Čo sa z toho nesmie vyvodiť

- nie je dovolené nastaviť `h=0`, `U_c=0` ani `delta_s=0` iba preto, aby sa
  ledger uzavrel;
- nie je dovolené použiť jeden constraint na definovanie `h` a ten istý
  constraint potom označiť za nezávisle prejdený;
- S1 nemožno ticho nahradiť agregovanou radiačnou tekutinou, lebo P5 práve
  testuje anisotropný stres a samostatné multipóly.

## Korektný ďalší postup

**P5.3g7 sa rozdeľuje na dve pevné vstupné vetvy, nie na nové fyzikálne
mechanizmy:**

1. odvodiť/plne citovať štandardný synchronný `h,eta` seed a nezávislú
normalizáciu pred akýmkoľvek residualom;
2. označiť S1 seed ako podmienený `ASSUMPTION_S1_ADIABATIC` a viesť ho
oddelene od odvodeného verdiktu Q18/Q22, alebo počkať na ich mikrofyzikálny
mechanizmus.

Potom môže 261 robiť dva jasne označené výsledky: matematický conditional-S1
seedový residual a samostatný rozsudok, že fundamentálna teória jeho S1
počiatočnú podmienku zatiaľ neodvodila. P5.4/G8 sú dovtedy zavreté.

## Spresnenie po kontrole štandardnej bázy

Štandardný CDM-synchronný rad je prípustný iba ako **nezávislý nulový limit a
gauge kotva**. Jeho štartovacia voľba `U_c=0` nesmie odstrániť dynamické `U_c`
z interagujúceho P5 systému; musí sa v 261 objaviť a dostať vlastnú RHS. Pre
S1 nie je prípustné univerzálne priradenie `delta_s=delta_nu`, lebo pri NID/NIV
mení kompenzáciu. Úplná mapa je
`tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/25_P5_3G7_INPUT_RAILS_SK.md`.
