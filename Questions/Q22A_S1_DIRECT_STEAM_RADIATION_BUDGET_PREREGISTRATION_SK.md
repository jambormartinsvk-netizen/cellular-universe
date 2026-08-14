# Q22a-S1 — preregistrácia sita priamej pary z radiačného rozpočtu

**Stav pred behom:** `PRIPRAVENÉ; analyticko-numerické sito, bez skóre`  
**Rozsah:** iba K2 a priamy podiel K3, kde para je voľná relativistická zložka
počítaná v `X_r`.

## Čo sa počíta ľudskou rečou

Súčasný A1 transfer odoberá energiu palivu rýchlosťou
`q=lambda X_f/E`. Zaveďme iba auditnú súradnicu `f_R` — podiel tohto už
existujúceho transferu, ktorý by šiel priamo do pary/radiácie:

```text
X_f,x = -3 delta X_f - q
X_c,x = -3 X_c + (1-f_R) q
X_r,x = -4 X_r + f_R q.
```

`f_R=0` je A1-K1; `f_R=1` je Q22a-K2; `0<f_R<1` je priamy paralelný podiel
Q22a-K3. `f_R` sa **nefitne** — je len os, po ktorej sa overí, čo povoľuje
už zmrazený dnešný radiačný obsah a kladnosť hustôt až po rekombináciu.

## Zmrazené vstupy a očakávanie

Použijú sa už registrované A1 hodnoty `h=0.6637`, `Omega_m0=0.3517`,
`lambda=0.15`, `delta=0.02297`, `Delta_Neff=0.0535`,
`omega_gamma=2.469e-5` a `z*=1089.9`. Pri `x=0` je `X_r` malý pozorovaný
radiačný rozpočet.

Očakávanie:

* `f_R=0` reprodukuje A1-K1 a zostane pozitívne;
* `f_R=1` sa pri spätnom behu rýchlo dostane na záporné `X_r`, lebo dnešný
  transfer je rádovo väčší než dnešný radiačný inventár;
* bisection nájde hornú hranicu `f_R,max` z podmienky `X_r>0` až po `z*`.

## Interpretácia PASS / STOP

* **PASS sita:** presná conservation identita, nulový limit `f_R=0` a
  reprodukovateľná hranica kladnosti.
* **K2 STOP v zmrazenom A1:** ak `f_R=1` neprejde kladnosťou do rekombinácie,
  nie je kompatibilná s dnešným radiačným rozpočtom v tejto vetve.
* **K3 obmedzenie:** prípadný priamy podiel pary musí byť najviac
  `f_R,max`; nie je tým odvodený ani povolený ako fitovaný parameter.

Sito netestuje kanál, v ktorom sa energia najprv uloží v inom medzistave,
reabsorbuje sa alebo nie je relativistickou parou. Taký kanál patrí do K4–K7
a vyžaduje vlastný odvodený kernel.

## Bezpečnostné limity

Skript používa pevnokrokový RK4, vlastný limit najviac 4.5 s a maximálne
200 000 krokov v jednom behu. Vonkajší limit bude 10 s.
