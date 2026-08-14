# A2-K4 BR3C-a — predregistrácia a rozhodnutie depth-first verzus breadth-first

**Dátum:** 2026-07-14  
**Vstup K4:** `66.0/100; G6 PASS; G7 OTVORENÁ`  
**Najbližší checkpoint:** `C7.7a`, maximálne `+0.2` bodu

## Rozhodnutie o poradí

Nezačaté alebo plytké koľaje na G1–G2 sa nedajú po krátkom registračnom
teste označiť za fyzikálne životaschopné. Taký prechod by zväčšil iba počet
„nezabitých hypotéz“, nie počet koľají s rovnicami, constraintmi a
stabilitou.

Preto sa použije tento hybridný postup:

1. dokončiť K4/BR3C cez C7.7 a C7.8, najviac po `68.0/100`;
2. ak K4 fyzikálne zomrie, breadth-first triage sa otvorí okamžite;
3. ak BR3C ostane opakovane technicky `UNCLOSED` z rovnakej príčiny, triage
   sa otvorí pred ďalším drahým zásahom;
4. ak K4 BR3C prejde, pred drahým BR4 sa vykoná časovo ohraničený G1–G3
   triage plytkých alternatív tej istej A1-K1 vetvy;
5. A1-K2/A2-K10 sa do tohto počtu nemieša, pretože mení A1 background.

Triage musí osobitne uviesť `registrovaná`, `prešla G2`, `prešla G3` a
`mŕtva`. Samotný stav `ČAKÁ` alebo `nezabitá` sa nesmie prezentovať ako
životaschopnosť.

## Rozsah C7.7a

BR3C-a ešte neevolvuje poruchy. Z autoritatívneho koeficientového motora 127
zostaví dva povrchy toho istého analytického NID a NIV riešenia:

| Parameter | Zmrazená hodnota |
|---|---:|
| gauge | general synchronous, konvencia skriptu 127 |
| `x_deep=ln(a)` | `-25` |
| `x_shallow=ln(a)` | `-23` |
| `k` | `0.05 Mpc^-1` |
| štandardný rád | autoritatívny `6`; auditný cross-check `5` |
| fuel-fraction coefficient | `1` v deklarovanej per-unit Puiseux normalizácii |
| interný limit jedného koeficientového behu | `15 s` |
| vonkajší limit jedného behu | `25 s` |

Hodnota fuel-fraction coefficient `1` nie je nový kozmologický fit. Je to
koeficientová normalizácia už použitého rozvoja
`rho_f/rho_r = Phi z^(4-3delta)`. Absolútna fyzická amplitúda sa v C7.7a
nefituje.

## Povinný stavový ledger

Na oboch povrchoch a pre NID aj NIV musia byť explicitne uložené:

- `h`, `eta`, `h_x`, `eta_x`;
- `delta_gamma`, `delta_fs`, `delta_b`, `delta_c`, `delta_f`;
- `U_gamma=U_b`, `U_fs`, `U_c`, `U_f`;
- `sigma_fs`, rescalované `L3`, `L4` a rekonštruované `F3`, `F4`;
- `Omega_gamma`, `Omega_fs`, `Omega_b`, `Omega_c`, `Omega_f`;
- `z=k a/(H0 sqrt(Omega_r))`, `s=k/Hconf`, backgroundový denominator;
- normalizačný anchor príslušného seedu.

`U_c=0` je v tomto prvom ráde dovolené iba s explicitným označením, že
interakčný zdroj `U_c` je `O(Phi^2)` podľa skriptu 128. Nesmie ísť o tichý
placeholder.

## Acceptance kritériá C7.7a

C7.7a prejde iba ak:

1. zdrojová transformácia 127 má pre každý zásah presne jeden match;
2. oba módy a oba povrchy obsahujú celý povinný stavový ledger;
3. všetky hodnoty sú konečné a `0 < z_deep < z_shallow < 10^-3`;
4. súčet piatich backgroundových `Omega_A` je jedna s absolútnym rezíduom
   pod `2e-12`;
5. identity `L3=s F3` a `L4=s^2 F4` prejdú pod `2e-12` po škálovaní;
6. NID a NIV používajú rovnaké koeficienty a normalizačný anchor na oboch
   povrchoch; nejde o dva nezávisle fitované seedy;
7. spoločné stavové polia pri štandardnom ráde 5 a 6 sú stabilné podľa
   predregistrovaného absolútneho aj škálovaného testu;
8. skripty skončia v časovom limite a ich machine PASS zodpovedá uvedeným
   kontrolám.

PASS pridá `+0.2` a stav K4 bude `66.2/100; G7 OTVORENÁ`. Syntax, timeout,
neúplný export alebo čisto numerická nezhoda znamenajú `UNCLOSED/REVIEW` a
nedávajú body. Fyzikálna smrť sa smie vyhlásiť iba pri robustne potvrdenej
neexistencii spoločného regulárneho stavu, nie pri chybe transformácie.

