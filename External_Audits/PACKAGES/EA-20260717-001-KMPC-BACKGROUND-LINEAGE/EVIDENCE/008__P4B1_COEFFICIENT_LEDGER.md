# K-N2/P4b1 — exact A1 coefficient ledger pre K7

**Stav:** `PASS — backgroundové koeficienty majú jednoznačné A1 definície.`  
**Ešte neprešlo:** P4b2, t. j. nezávislá kovariantná kontrola všetkých
lineárnych zdrojových členov RHS a ich znamienok.

## Pravidlo

Zachováva sa A2-K4 operátor

```text
Q^mu = Gamma rho_f u_d^mu,    Gamma=lambda H0.
```

Používajú sa presné A1 riešenia `X_f(a), X_m(a), X_r(a)` a
`X_b(a)=X_b0 a^-3`, `X_c=X_m-X_b`. Všetky definície nižšie platia iba tam,
kde `E^2>0` a `X_c>0`; to je samostatná kontrola A1, nie voľba parametra.

## Náhrada K7 backgroundových koeficientov

| Starý symbol | Presná A1 definícia | Ranný radiačný limit | Status |
|---|---|---|---|
| `D` / denominator | `D_A1=a^4 E^2/Omega_r0` | `1+O(a)` | PASS |
| `ell` | `D_x/D=(4-3delta)Omega_f+Omega_b+Omega_c` | log-derivácia ranného radu | PASS |
| `q` | `-1+ell/2` | nezmenená definícia | PASS |
| `Og`, `On` | `Rgamma X_r/E^2`, `Rnu X_r/E^2` | `Rgamma`, `Rnu` | PASS |
| `Ob`, `Oc`, `Of` | `X_b/E^2`, `X_c/E^2`, `X_f/E^2` | presné podiely hustôt | PASS |
| `g` | `gamma=Gamma/H=lambda/E` | `lambda a^2/sqrt(Omega_r0)` | PASS |
| `gr` | `gamma X_f/X_c` | staré `G2 z^(p+1)/(FC MU)` | PASS |
| `beta_c` | `d ln(a^4X_c)/dx = 1+gamma X_f/X_c` | `1+gr` | PASS |
| `beta_f` | `d ln(a^4X_f)/dx = p-gamma` | `p-g` | PASS |
| loading | `R=3X_b/(4X_gamma)` | starý baryón-fotónový pomer | PASS |
| `inv1r`, `load_fraction` | `1/(1+R)`, `R/(1+R)` | nezmenené | PASS |

Tu `Rgamma=1/(1+0.2271 N_eff)` a `Rnu=1-Rgamma`, takže
`X_gamma=Rgamma X_r`. Výraz pre `ell` plynie priamo z P4a; pri `lambda`
sa transfer zo súčtu hustôt vyruší.

## Jediný prípustný výskyt perturbatívneho módu

Pre konkrétny Fourierov mód `k_mode` platí

```text
s2(a,k_mode) = k_mode^2/Hconf(a)^2
             = k_mode^2 a^2/[H0^2 Omega_r0 D_A1(a)].
```

To je fyzikálne správne miesto pre `k_mode`: opisuje veľkosť poruchy voči
horizontu. `k_mode` **nesmie** vstúpiť do `D_A1`, `Omega_i`, `ell`,
`gamma`, `gr`, `beta_c` ani `beta_f`. Starý `K_MPC=0.05` sa preto nesmie
ďalej používať ako backgroundová konštanta; ak sa zvolí mód pre test,
musí byť uvedený ako samostatný vstup poruchového behu.

## Kontrola odvodení

Z A1:

```text
X_c,x = -3X_c + lambda X_f/E,
X_f,x = -3delta X_f - lambda X_f/E.
```

Preto:

```text
d ln(a^4X_c)/dx = 1 + lambda X_f/(E X_c) = 1+gr,
d ln(a^4X_f)/dx = 4-3delta-lambda/E = p-gamma.
```

V čisto radiačnom limite `E=sqrt(Omega_r0)/a^2` sa `gamma` presne zmení na
staré `g=G2z^2`; tým sa overuje, že nejde o novú fyziku, ale o odstránenie
neprípustnej neskorej extrapolácie.

## Čo tento PASS ešte neoprávňuje

Táto tabuľka nepreukazuje, že každý riadok pôvodného `physical_rhs()` má
správny kovariantný faktor a znamienko po náhrade. Najmä členy s `gr`,
`gamma U_f/delta`, pressure perturbation a energy-frame rýchlosť musia
prejsť P4b2 nezávislým odvodením z `Q^mu`. Starý skript 213 zostáva
immutable historický výsledok; nevykonáva sa na ňom patch.

## Ďalší krok

P4b2 vytvorí line-by-line ledger: každý interakčný člen v `physical_rhs`
bude mať kovariantný pôvod, exact-A1 koeficient, nulový limit
`Gamma->0` a znamienkovú kontrolu. Až po tom môže P4c pripraviť nový
RHS/constraint audit a až potom G8.
