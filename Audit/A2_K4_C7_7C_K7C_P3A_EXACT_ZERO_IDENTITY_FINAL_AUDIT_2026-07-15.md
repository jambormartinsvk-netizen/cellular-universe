# K7c P3a-A — konečný audit presnej nulovej identity

Dátum: 2026-07-15  
Verdikt: **PASS_P3A_EXACT_ZERO_IDENTITY**  
Score effect: `NONE`  
A2-K4 hĺbka: `66.5/100` bez zmeny

## Čo bolo testované

Skript 201 bez ODE overil, či dve cancellation-nebezpečné kombinácie v
`M'` musia byť presne nulové už z registrovaných backgroundových definícií.
Provenance bola uzamknutá na skript 199 a jeho P2 raw JSON.

Z definície

[
R={3over4}{Omega_boverOmega_gamma}
]

plynie (Omega_b=(4/3)ROmega_gamma). Preto

[
W_gamma=2Omega_gamma+{3over2}Omega_b
=2Omega_gamma(1+R),
]

[
c_U={3over2}Omega_b-W_gamma{Rover1+R}=0,
qquad
c_delta={W_gammaover4(1+R)}-{Omega_gammaover2}=0.
]

Racionálny audit dal pre všetkých päť redukčných rezíduí presne `0/1`.

## Numerická kontrola

| `x` | float64 `c_U` | float64 `c_delta` | najväčšie 80-dps normalizované rezíduum |
|---:|---:|---:|---:|
| -25.000 | 0 | `+5.5511151231e-17` | `1.7963e-81` |
| -24.875 | `+3.3087224502e-24` | `-5.5511151231e-17` | `2.5069e-81` |
| -24.750 | `+1.6543612251e-24` | 0 | `1.9476e-81` |
| -23.000 | `+3.9704669403e-23` | `-5.5511151231e-17` | `1.7963e-81` |

Všetky HP hodnoty sú pod predregistrovaným limitom `1e-70`. Float64
zvyšky teda nie sú fyzikálne koeficienty, ale artefakty spôsobu vyhodnotenia
presnej identity.

## Provenance a rozsah

- skript 201 SHA-256:
  `03AA42272D05B8031EC54A39209275EE6B15D448FFE7204AA20EE25967FCAF38`;
- raw výsledok SHA-256:
  `4C9747DEF1AB9662735E974B1A992C6FC12784F20F69EB4A73862A9E234C7E65`;
- P2 raw a skript 199: presné očakávané hashe PASS;
- všetky štyri plochy konečné;
- `new_ODE_executed=false`;
- runtime 0.0 s v rámci interného limitu 5 s.

Tento PASS nedokazuje RK4 konvergenciu, CMB likelihood ani S8. Dokazuje iba,
že pôvodný numerický kód nesmel tieto dva koeficienty počítať
cancellation-nebezpečným tvarom na danom backgrounde.

## Rozhodnutie

P3a-A povoľuje pripraviť samostatnú P3a-B. P3a-B smie zmeniť iba
vyhodnotenie `c_U` a `c_delta` na auditovanú presnú nulu a musí zopakovať
nezmenené mriežky 100/200/400 aj prahy pomeru `8–32` a rozdielu
`200/400 < 1e-6`. Až jej výsledok rozhodne, či presná algebraická oprava
rieši fyzikálnu G5 konvergenciu.
