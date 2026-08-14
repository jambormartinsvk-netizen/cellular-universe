# A2-K4 C7.7c — predregistrácia evolučného species/mode ledgeru

**Dátum:** 2026-07-14  
**Vstup:** `C7.7b PASS; K4=66.5/100`  
**Možný prírastok:** `+0.2`

## Otázka

Obsahoval úspešný beh 136 všetkých 13 komponentov iba ako názvy, alebo bol
každý komponent počas evolúcie numericky rozlíšený a dynamicky aktívny?

## Povinný výstup

Pre každý NID/NIV, deep/shallow a každý segment sa uloží:

1. 13-zložkový checkpointový stav;
2. absolútna hodnota 13 zložiek RHS;
3. component maximum počas celej trajektórie;
4. maximálna checkpointová zmena každej zložky.

`U_c=0` a `L5=0` nie sú medzi 13 integrovanými komponentmi. Musia zostať
uvedené ako explicitné scope limity, nie ako prežité dynamické módy.

## Zmrazená aktivita

Pre komponent `i` sa definuje rozlišovacia podlaha

```text
floor_i = max(10*atol, 10*rtol*max_trajectory_abs_i),
```

pri rovnakých `atol=1e-14`, `rtol=1e-10` ako v 136.

Komponent je pre C7.7c numericky aktívny iba ak súčasne:

```text
max_checkpoint_abs(RHS_i) > floor_i
max_checkpoint_abs(Delta y_i) > floor_i.
```

Podmienka sa nesmie po výsledku zmenšiť. Samotná nenulová počiatočná hodnota
ani JSON key nestačia.

## Acceptance

C7.7c prejde iba ak:

- exportný klon nemení ODE ani solver skriptu 136;
- všetky štyri trajektórie znovu prejdú C7.7b;
- stavové a RHS kľúče sa presne rovnajú registrovaným 13 menám;
- každý z 13 komponentov prejde oboma activity podmienkami v každej zo
  štyroch trajektórií;
- nevznikne nový timeout, safety-cap alebo nefinite výsledok.

Ak zlyhá iba vysoký multipól pod numerickou podlahou, výsledok je
`REVIEW_UNCLOSED`, nie fyzikálna smrť. Ďalšia oprava musí použiť
predregistrované rescalovanie alebo component-wise toleranciu; nesmie nulovať
fyzikálny multipól ani spätne uvoľniť activity floor.

