# A2-K11 — fyzikálny audit opraveného skriptu 45 a momentum drag

**Dátum:** 2026-07-13  
**Auditovaná revízia skriptu 45:** SHA-256
`61558FAF0D08E35B9B6D6CAFE30FFD55FD2E3FB2399D2A69F92D534EFC590CB1`  
**Rozsudok skriptu 45:** `PASS ZAMIETNUTÝ — NEPLATNÝ DÔKAZ`  
**Rozsudok fyzikálnej koľaje:** `A2-K11 PREŽÍVA IBA FORMULAČNÚ BRÁNU — 15/100`

## Stručný výsledok

Oprava faktora interakčných sadzieb z `1/(aE)` na `1/E` bola správna.
Neopravila však rozhodujúce chyby v znamienku silového štvorvektora,
CDM/fuel Eulerových rovniciach, fuel kontinuite, tlakovom člene ani v
numerickej akceptácii. Skript navyše nevypočítava prenosovú funkciu,
`sigma_8` ani `S8`; jeho názov preto nie je dôkazom riešenia tenzie `S8`.

Myšlienka **čistého prenosu hybnosti bez zmeny backgroundu** je fyzikálne
zmysluplná a v literatúre existuje. Predložená realizácia ju ale ešte
nekorektne implementuje. Preto nevzniká potvrdená koľaj, ale nová otvorená
koľaj A2-K11 s nízkym skóre a presnými kill bránami.

## 1. Čo je A2-K11 a v čom je nová

Kanonická definícia kandidáta je

```text
Q_c^mu = +Gamma rho_f u_c^mu + F_c^mu,
Q_f^mu = -Q_c^mu,
u_{c,mu} F_c^mu = 0.
```

- A2-K1 mala iba energetický tok rovnobežný s `u_c^mu`; CDM bolo
  geodetické a koľaj zomrela na recoil paliva.
- A2-K11 pridáva fyzikálne odlišný, ortogonálny momentum-transfer operátor.
- A2-K6 odvodzovala energy+momentum väzbu z konkrétnej skalárnej akcie a
  povinná piata sila ju zabila. A2-K11 zatiaľ žiadnu skalárnu piatu silu
  nepredpokladá, ale musí ešte ukázať vlastnú lokálnu akciu alebo collision
  operátor.
- A2-K9 má jedným operátorom spájať produkciu častíc aj rozptyl. A2-K11
  zatiaľ zachováva fluidný A1 tok a pridáva iba elastický prenos hybnosti.

Zmena gauge, integračného kroku alebo amplitúdy by nebola novou koľajou.
K11 je nová iba vďaka novému ortogonálnemu fyzikálnemu operátoru.

## 2. Audit znamienka silového štvorvektora

Pri signatúre `(-,+,+,+)` definujme

```text
h_c^{mu alpha}=g^{mu alpha}+u_c^mu u_c^alpha.
```

Na prvom perturbačnom ráde platí

```text
h_c^{i alpha}u_{f,alpha}=(v_f^i-v_c^i)/a.
```

Predložený tvar

```text
F_c^mu=-gamma rho_c h_c^{mu alpha}u_{f,alpha}
```

preto dáva

```text
F_c^i=-(gamma rho_c/a)(v_f^i-v_c^i),
F_{c,i}=-a gamma rho_c(v_{f,i}-v_{c,i}).
```

Ak `F_c^mu` znamená silu **na CDM**, pri `gamma>0` urýchľuje CDM od
rýchlosti paliva: je to anti-drag. Tlmiace znamienko je

```text
F_c^mu=+gamma rho_c h_c^{mu alpha}u_{f,alpha}.
```

Mínus by bolo možné zachrániť iba explicitnou opačnou definíciou, napríklad
ak by sa `F_c` vkladalo do `Q_c` ako `-F_c`. Predložené tvrdenia takúto
konvenciu nezaviedli a ich Eulerova interpretácia zodpovedá plusovému, nie
mínusovému projektoru.

Ortogonalita `u_c.F_c=0` je správna a zaručuje, že čistý silový člen na
homogénnom backgrounde mizne. Sama ortogonalita však neurčuje tlmiace
znamienko.

## 3. Audit rovníc skriptu 45

Použité konvencie sú `x=ln(a)`, `u_A=H0 theta_A/k^2`,
`w_f=-1+delta`, `c_s,f^2=1`, `Gamma=lambda H0`.

| Miesto | Skript 45 | Auditovaný výsledok |
|---|---|---|
| sadzby v `x` | po oprave `lambda/E`, `gamma/E` | správne pre konštantné proper-time sadzby `lambda H0`, `gamma H0` |
| CDM kontinuita | chýba `+Psi` v zdrojovej zátvorke | musí obsahovať `(delta_f-delta_c+Psi)` |
| CDM Euler | obsahuje tlmenie `lambda rho_f/(E rho_c)` | pre energetickú časť `Q_c^mu || u_c^mu` musí byť presne nula; pôsobí iba ortogonálne `F_c^mu` |
| fuel kontinuita | používa iba `-lambda/E(delta_f-delta_c)` | chýba sound-speed prevod, `Psi`, velocity-transfer člen a príslušné metrické členy |
| fuel tlak v Euleri | `(delta_f+Phi)/(aE)` | pre `c_s,f^2=1` je tlakový člen `delta_f/[delta aE]` |
| fuel energetický recoil | tlmiace `lambda/(delta E)(u_c-u_f)` | znamienkovo auditovaná K1 časť je anti-damping `lambda/(delta E)(2u_f-u_c)` |
| drag reakcia na fuel | zlúčená do jedného `G_f` | samostatne `gamma rho_c/(delta rho_f E)(u_c-u_f)` pre plusový projektor |
| Einsteinove rovnice | evolúcia cez `0i`, kontrola `00` | nie je to „úplný Einsteinov systém“; `00` sa nekontroluje relatívne na aktívnych bodoch |

Referenčný audit energetickej časti K1 je v
`Audit/A2_1_linearne_perturbacie_Einsteinove_constrainty_a_superhorizontovy_test.md`
a znamienková mapa v
`scripts/24_script_A2_K1_equation_sign_and_null_limit_audit.py`.

## 4. Prečo numerický `PASS` neplatí

Aktuálna revízia skriptu 45 vytlačila `PASS_S8_K1b_SUPERHORIZON_GATE`, ale:

1. `step_log_transfer_relative_difference=1.34664e-6` nesplnilo prah
   `1e-6`; skript ho napriek tomu označil za úspech cez
   `step_conv < 1e-6 or is_damped`.
2. `global_relative_00_constraint_residual=1.0`; úspech vznikol iba preto,
   že absolútne rezíduum bolo menšie než voľný prah `1e-8`.
3. deklarovaný transfer `1.89419e-13` je približne 528-krát menší než
   `atol=1e-10`. Solver takúto konečnú amplitúdu nerozlišuje.
4. beh nazvaný `uncoupled_fine` vypol iba `gamma`, ale ponechal
   `lambda=0.15`; nie je to nulový limit interakcií.
5. test nepočíta `P(k)`, `sigma_8` ani `S8` a nepoužíva CMB-normalizované
   počiatočné podmienky.

Skript 53 využil linearitu: pri spoločnom zväčšení počiatočnej amplitúdy o
`10^12` sa bezrozmerný transfer mal zachovať. Namiesto toho sa zmenil z
`1.95490e-12` na `3.37370e-15`; logaritmická relatívna odchýlka bola
`0.190923`. Aj rozlíšený krokový test zlyhal hodnotou `8.03101e-5` a
relatívne `00` rezíduum ostalo `1.0`. Verdikt skriptu 53 je
`FAIL_NUMERICAL_RESOLUTION`.

Úplné zachované čísla sú v
`Audit/A2_K11_NUMERICAL_OUTPUT_45_51_52_53.md`.

## 5. Fyzikálny problém, ktorý zostáva aj po oprave znamienka

Pri plusovom projektore je reakcia na palivo zosilnená jeho malou
inerciálnou hustotou:

```text
gamma rho_c/[delta rho_f E].
```

Predložený koeficient sily je úmerný iba `rho_c`. Nezaniká pri
`rho_f -> 0`, hoci druhé médium zmizlo, a reakcia paliva v tomto limite
diverguje. To je riziko silnej väzby, nie automatický dôkaz zdravého
tlmenia. Mikroskopický collision operátor typicky musí určiť aj hustotnú
závislosť koeficientu, spätnú reakciu a prípadný šum.

Čistý momentum exchange bez backgroundového toku je známy fyzikálny typ
modelu, ale jeho kozmologické dôsledky závisia od presného operátora:

- Simpson, *Scattering of Dark Matter and Dark Energy*,
  <https://arxiv.org/abs/1007.1034>;
- Baldi a Simpson, *Simulating Momentum Exchange in the Dark Sector*,
  <https://arxiv.org/abs/1412.1080>;
- Clemson et al., znamienkový a perturbačný rámec interagujúcej tmavej
  energie, <https://arxiv.org/abs/1109.6234>.

Tieto práce podporujú existenciu triedy mechanizmov, nie konkrétny parameter
`gamma=0.03` ani rovnice skriptu 45.

## 6. Stav, skóre a kill kritérium

**A2-K11: `PREŽÍVA IBA FORMULAČNÚ BRÁNU — 15/100`.**

Prežila iba možnosť zapísať kovariantný ortogonálny momentum-transfer s
opraveným znamienkom a nulovým backgroundovým príspevkom. Nezískala body za
superhorizont, constrainty, high-k stabilitu, CMB ani `S8`.

Historické revízie skriptu 45 sa nemažú a ich výstupy zostávajú v audite,
ale ich `PASS` label je **neplatný dôkaz**, nie samostatná mŕtva fyzikálna
koľaj. Rovnaký mechanizmus po oprave rovníc zostáva K11 podľa pravidla
neduplikovania koľají.

Rezervovaný rozsudok je `M-015`. K11 zomrie, ak nastane aspoň jedno:

- žiadny lokálny operátor nedá tlmiace znamienko a pravidelný limit
  `rho_f -> 0` bez ručného vymazania reakcie;
- úplný gauge-invariantný systém poruší Bianchiho identity alebo Einsteinove
  constrainty;
- superhorizontový alebo high-k fyzikálny mód má kladný nestabilný exponent;
- potrebné `gamma` je nezávislý post-data fit bez vzťahu k bunkovej
  mikrofyzike;
- CMB-normalizovaný Boltzmannov výpočet alebo nelineárne dáta vylúčia
  rozsah potrebný na zníženie `S8`.

## 7. Povinný ďalší krok K11.1

1. odvodiť `F_c^mu` z lokálnej akcie alebo collision operátora a určiť jeho
   závislosť od `rho_c`, `rho_f`, `delta` a teploty;
2. fixovať jednu znamienkovú konvenciu pre `Q_c^mu`, `F_c^mu`, `theta_A` a
   metriku;
3. odvodiť úplné `delta Q_A`, kontinuity, Eulerove rovnice a oba Einsteinove
   constrainty z tej istej definície;
4. preveriť nulové limity `gamma->0`, `lambda->0`, `rho_f->0`, `delta->0`
   a zachovanie celkového `T^{mu nu}`;
5. až po analytickom prejdení týchto brán vytvoriť nový numerický
   superhorizontový a high-k test bez tolerančného bypassu;
6. `S8` sa smie počítať až následným CMB-normalizovaným Boltzmannovým behom.

K7.1 zostáva zachovaná ako samostatná koľaj s mediátorom; audit K11 ju
neruší ani neprepisuje.

