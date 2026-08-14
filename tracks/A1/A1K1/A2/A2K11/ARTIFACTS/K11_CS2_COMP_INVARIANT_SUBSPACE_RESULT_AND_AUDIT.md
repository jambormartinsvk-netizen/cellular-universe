# K11-CS2-COMP — audit invariantného kompenzovaného dark podpriestoru

**Dátum:** 2026-07-16  
**Autorita verdiktu:** hlavný orchestrátor  
**Typ:** analytický necessary-condition audit; bez Pythonu a bez ODE  
**Verdikt:**
`K11-CS2-COMP-INVARIANT-DARK-SUBSPACE: EMPTY_CERTIFIED_SCOPE`  
**Dopad na rodiča K11-R:** žiadna smrť; full viacdruhová DAE zostáva nutná  
**Skóre/release:** bez zmeny

## 1. Otázka

Chceli sme zistiť, či možno plný K11-CS2 rozhodnúť exaktnou skratkou bez
fotónov, baryónov, neutrín, pary a metriky. Taká skratka by existovala, ak
by dark perturbácie vytvorili nenulový invariantný podpriestor s

```text
Phi=Psi=0,
standard species perturbations=0,
delta rho_dark=0,
momentum_dark=0,
delta p_dark=0.
```

Potom by sa metrika ani štandardné species nikdy nezapli a relative mód by
mal vlastnú uzavretú rovnicu.

## 2. Definície

Použime

```text
gamma = a Gamma,
h     = mathcal H,
r     = rho_f/rho_c,
s     = delta rho_f/rho_c = delta r,
A_c   = a Upsilon/rho_c,
A_f   = a Upsilon/(delta rho_f).
```

Exact momentum reaction dáva

```text
A_c=s A_f.
```

Pre pressure conversion zaveďme

```text
B=(2-delta)(3h delta+gamma),
delta p_f/rho_f = delta_f+B V_f.
```

## 3. Okamžitá algebraická kompenzovaná priamka

Podmienky

```text
D_rho=rho_c delta_c+rho_f delta_f=0,
D_Pi =rho_c V_c+delta rho_f V_f=0,
D_p  =delta p_f=0
```

majú pre každý nenulový `V_f` na jednej časovej ploche jediné riešenie

```text
V_c     = -s V_f,
delta_f = -B V_f,
delta_c =  r B V_f.
```

Teda nenulová **okamžitá algebraická priamka existuje**. To samo nie je
dynamická invariantnosť.

## 4. Čo exact reaction zachová

Po dosadení backgroundových kontinuitných rovníc a úplných dark
perturbačných riadkov platí na kompenzovanej ploche

```text
D_rho'=0,
D_Pi'=rho_c V_f(1+s)(A_c-s A_f)=0.
```

Hustotná a hybnostná kompenzácia teda nezlyhávajú pre porušenie conservation.
Exact reaction ich zachováva, pokiaľ zostane tlak nulový.

## 5. Presný escape source tlaku

Definujme normalizovaný pressure residual

```text
D_p_norm=delta_f+B V_f.
```

Jeho derivácia na okamžite kompenzovanej priamke je

```text
D_p_norm'=B V_f Xi_p,

Xi_p=B'/B-h+gamma(1+r)-A_f(1+s).
```

Pre fyzický tlak, keď `D_p_norm=0`, teda

```text
(delta p_f)'=rho_f B V_f Xi_p.
```

Nenulová priamka by bola invariantná iba pri dodatočnej časovo závislej
podmienke

```text
A_f(1+s)=B'/B-h+gamma(1+r).
```

Táto rovnosť nie je identita K1, K11 ani exact reaction. Obsahuje `h'` cez
`B'/B` a všeobecne neurčuje kladný lokálny pasívny drag.

## 6. Harmonický K11-R svedok

Pre

```text
Upsilon_R=Gamma rho_c delta rho_f/(rho_c+delta rho_f)
```

platí

```text
A_f=gamma/(1+s),
A_f(1+s)=gamma.
```

Preto

```text
Xi_p^(R)=B'/B-h+gamma r

=[3delta(h'-h^2)+gamma r(3delta h+gamma)]
 /(3delta h+gamma).
```

Toto nie je nulová backgroundová identita.

## 7. Rozhodujúci skorý radiačný limit

Na štandardnej A1 skorej radiačnej vetve

```text
h'=-h^2,
gamma/h -> 0,
gamma r/h -> 0.
```

Teda

```text
B'/B -> -h,
Xi_p^(R) -> -2h != 0.
```

Pre každý nenulový `V_f` vznikne

```text
(delta p_f)' -> -2h rho_f B V_f != 0.
```

Silnejšie: pre všeobecný pasívny `A_f>=0` je v rovnakom limite

```text
Xi_p -> -2h-A_f(1+s) < 0.
```

Invariantnosť by vyžadovala `A_f<0`, čiže anti-drag. Preto je trieda
nenulových skorých **pasívnych** presne kompenzovaných invariantných dark
podpriestorov prázdna.

## 8. Prečo sa zapne celý systém

Keď vznikne `delta p_f!=0`, stopová Einsteinova rovnica budí metriku:

```text
Phi''+h(Psi'+2Phi')+(2h'+h^2)Psi
=4 pi G a^2 delta p_f
```

v leading superhorizontovom limite. Metrika následne budí fotóny, baryóny,
neutrína a paru, aj keď boli na počiatočnej ploche nulové.

Compensated priamka teda neopúšťa fyzický systém pre chybu conservation,
ale pre povinný neadiabatický pressure conversion.

## 9. Scoped rozsudok

```text
INSTANTANEOUS NONZERO COMPENSATED DARK LINE:
EXISTS.

DYNAMICALLY INVARIANT PASSIVE COMPENSATED DARK SUBSPACE:
DOES NOT EXIST ON THE EARLY A1 RADIATION BRANCH.

K11-R EXACT ESCAPE SOURCE:
(delta p_f)'=rho_f B V_f(B'/B-h+gamma r).
```

Autoritatívny scoped stav je

```text
K11-CS2-COMP-INVARIANT-DARK-SUBSPACE: EMPTY_CERTIFIED_SCOPE.
```

Tento výsledok **nezabíja K11-R**. Dokazuje, že interaction-only `2x2`
determinant ani tangentová okamžitá sadzba `V_f'/V_f` nemôžu byť vydávané
za exact exponent fyzického kompenzovaného módu. Full metric/species DAE je
skutočne potrebná.

## 10. Ďalší krok

Pokračuje sa jedinou už predregistrovanou K11-CS2 full DAE. COMP nie je nová
koľaj ani CS3 suffix; nemení operátor, parameter ani povinný stavový priestor.
Nevzniká runner, JSON, nový base ani release trigger.

