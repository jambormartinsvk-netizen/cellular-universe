# A2-K6.1 — reprodukovateľný numerický výstup rozsudku M-013

**Dátum:** 2026-07-13  
**Generátor:** `scripts/49_script_A2_K6_1_continuous_eta_no_go.py`  
**Exit kód:** `1` z obalu nástroja; fyzikálny skript zámerne vracia nenulový
stav pri rozsudku `MŔTVA`  
**Poznámka:** tento súbor zachováva rozhodujúce čísla aj bez opätovného behu

## Presné redukované vzťahy

Pre `t=1+2 eta`, `r=t-1`, `d=delta rho_f/rho_c_hat`,
`P0=3 delta X_f/E^2`, `s=d ln A/dx` a
`B=1+eps_H+eps_Delta2-eps_Delta3` platí

```text
q_c = A [1 + (r/t)d]
r2  = r d
r1/A = (2s/P0) [s(1+r) + r d (s + dln(d)/dx - B)]
mu_cc = [1+r1/A]/[1+r2]
mu_cb = 1/[1+r2],  mu_bc=mu_bb=1
```

## Predregistrovaný grid

| `eta` | `mu_cc(0)` | `mu_cb(0)` | min–max `mu_cc`, `z<=10` | max `|r1_closed-r1_direct|` | rast / `eta=0` |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 5.674662 | 1.000000 | 1.000004–5.674662 | 1.776e-15 | 1.000000 |
| 0.1 | 7.222625 | 0.990201 | 1.000008–7.222625 | 3.553e-15 | 1.022118 |
| 0.5 | 13.122551 | 0.952853 | 1.000021–13.122551 | 7.105e-15 | 1.111272 |
| 1.0 | 19.899770 | 0.909952 | 1.000038–19.899770 | 1.066e-14 | 1.224102 |
| 2.0 | 31.774623 | 0.834781 | 1.000071–31.774623 | 1.776e-14 | 1.453557 |
| 5.0 | 57.965432 | 0.668987 | 1.000172–57.965432 | 4.263e-14 | 2.160409 |

Rast je scale-independentný QS diagnostický beh so spoločným počiatočným
stavom pri `z=100`; nie je to CMB likelihood ani nová predikcia `S8`.

## Nulové limity

- `eta->0`: maximálna chyba voči
  `1+2(d ln A/dvarphi)^2` je `1.776e-15`;
- `f1->0`: maximálna chyba voči čistému momentum limitu je `2.220e-16`;
- `mu_bc=mu_bb=1` po prepočte na fyzickú hustotu presne.

## Spojitá veta pri `z=0`

Po dosadení má väzba tvar

```text
mu_cc(r)=(n0+r n1)/(1+r d),  r=2 eta>=0.
```

Jej derivácia má konštantné znamienko. Numericky:

```text
smer                                      = rastúca
mu_cc(eta=0,z=0)                          = 5.674661891
lim eta->infinity mu_cc(z=0)              = 163.646709760
n1-d*n0                                   = 7.816408230e+00
```

Preto `mu_cc(z=0)>1` pre každé `eta>=0`; nejde iba o interpoláciu medzi
šiestimi bodmi.

## Konvergencia

| veličina | relatívny rozdiel krokov `5e-4` a `2.5e-4` |
|---|---:|
| `mu_cc(0)`, `eta=0` | 0.000e+00 |
| `mu_cc(0)`, `eta=0.1` | 3.446e-09 |
| `mu_cc(0)`, `eta=0.5` | 9.125e-09 |
| `mu_cc(0)`, `eta=1` | 1.149e-08 |
| `mu_cc(0)`, `eta=2` | 1.321e-08 |
| `mu_cc(0)`, `eta=5` | 1.450e-08 |
| `mu_cc(eta->infinity,0)` | 1.552e-08 |

## Strojový rozsudok

```text
stabilita a konečnosť na gride = PASS
oba nulové limity              = PASS
nutná podmienka mu_cc<=1       = FAIL
A2-K6                           = MŔTVA M-013
```

