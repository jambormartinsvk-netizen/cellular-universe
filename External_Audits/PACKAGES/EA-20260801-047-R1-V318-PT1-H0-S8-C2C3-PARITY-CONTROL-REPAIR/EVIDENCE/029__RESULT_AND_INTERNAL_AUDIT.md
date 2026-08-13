# v3.18 PT1 H0/S8 C2-C3 — výsledok a interný audit

**Dátum:** 2026-08-01  
**Route:** `RELEASE/v3.18/PT1_H0/C2-C3`  
**Autoritatívny stav:** `WORKING_ACCEPTED / NOT_RELEASED`  
**Claim class:** `THREE_DISCRETE_CONDITIONAL_LEGACY_ANCHOR_SENSITIVITY_POINTS`  
**RUN_AUTHORIZED:** `false`

## Otázka a rozsah

Test meria, ako sa v historickej legacy pipeline zmenia podmienené hodnoty
`H0` a zjednodušené `S8`, keď sa zmení iba sampled príspevok
`Delta N_eff = 0, 0.02675, 0.0535`. Uhlová kotva je synteticky vytvorená z
flat-LambdaCDM referencie `h_ref=0.673`. Výsledok preto nie je nezávislé
pozorovacie určenie ani aktuálna tvrdá predikcia teórie.

## Immutable výsledky

| `Delta N_eff` | grid | `H0` [km/s/Mpc] | podmienené `S8` | raw SHA-256 |
|---:|---:|---:|---:|---|
| `0` | 2000 | `65.78294389881194` | `0.8857121346393813` | `4AF3E71312669D0B5C6A11727744AE2D1A5CFA825412CE9F40228FB3951BC7DE` |
| `0` | 4000 | `65.7918328139931` | `0.8856125779281363` | `B923BE76D1AD9DAB3E0FBE27A89C09E70F4B6D111653F7A577374C011118C3C2` |
| `0` | 8000 | `65.79213819466531` | `0.8856095825403126` | `0D0D9352FC0144835DFDBC03181D4D3F9945BBBD0FC07B7CE03184F281833850` |
| `0.02675` | 2000 | `66.07397857122123` | `0.8801271060684014` | `31823491AB09A451B1A3B5936DB30BEFF668BC0F2E67DB412D7FD8F6CC4EAE4C` |
| `0.02675` | 4000 | `66.0828963574022` | `0.8800284093382995` | `20D9DA52D84CD17B366E8CAB95190E60A0E0D762B6C5BAC69E49CECD8EBF5C15` |
| `0.02675` | 8000 | `66.08320294879377` | `0.8800254370658636` | `67B1218BA8B061DE75665EAD0129E89C68C277F01316065D6E38E444307AD66A` |
| `0.0535` | 2000 | `66.36507778428495` | `0.8746006882362584` | `5A86DB61D291D18F716F9FB705505445FD2AB1B59590DFC686A5ED271867F05C` |
| `0.0535` | 4000 | `66.37402444146574` | `0.8745028411409409` | `2FC1AE5D9F96969728946613CDCE971D2F9A9B7A5A8A62A73A6043B7438568AB` |
| `0.0535` | 8000 | `66.37433224357665` | `0.874499891729803` | `DE86BBD810B282565E5BCFCAA436067E4168CE87600E8AFA350361D0045DF06D` |

## Konvergencia a materialita

| vetva | `abs(H0_8000-H0_4000)` | prah | `abs(S8_8000-S8_4000)` | prah | redukcia poslednej korekcie |
|---|---:|---:|---:|---:|---:|
| null | `0.000305380672216` | `0.005` | `2.99538782367e-6` | `0.0005` | `29.108x / 33.237x` |
| half | `0.00030659139156` | `0.005` | `2.97227243595e-6` | `0.0005` | `29.087x / 33.206x` |
| full | `0.00030780211091` | `0.005` | `2.94941113776e-6` | `0.0005` | `29.066x / 33.175x` |

High-grid endpointový posun je

```text
Delta H0(full-null) = +0.582194048911333 km/s/Mpc
Delta S8(full-null) = -0.0111096908105096
```

Obe absolútne hodnoty prekračujú predregistrované prahy materiality
`0.05 km/s/Mpc` a `0.005`. Ide o materialitu pre zobrazovaciu presnosť
tabuľky, nie o štatistickú významnosť voči dátam.

## Auditná evidencia

- `math_script_auditor`: `RECOMMEND_RC_AUDIT_PASS`; presné hashe, schémy,
  guardy, zdieľaná non-Delta projekcia, predecessor reťazec, konvergencia a
  endpointová aritmetika prešli.
- `physics_track_auditor`:
  `RECOMMEND_ACCEPT_NINE_CELL_SAMPLED_LEGACY_SENSITIVITY`; smer rastúceho
  `Delta N_eff` -> menšie `r_s`, vyššie podmienené `H0`, menšie `Omega_m`,
  rast a podmienené `S8` je v tomto backgroundovom scope koherentný.
- Všetky komponenty zostali kladné, floor/clip sa neaktivoval. Maximálny
  matter residual je približne `8.63e-11`, angular residual `1.33e-10` a
  quadrature error `6.07e-12`.
- `full` bod reprodukuje historické comparatory v zmrazených toleranciách.
- Nebol nájdený žiadny `S1-S4` finding; `TRACK_IDENTITY_GATE` je
  `SAME_TRACK_CONFIRMED`.

## Proveniencia

```text
V5 contract SHA256 = 6706912598C536099A1E230D20650D8A792943AF87FB36C283DF4F1449CCB3A1
base SHA256 = 74AE3B0BC31FA1AE4BB9FDB3339C84869DA38131440795BD0C7B2B82677F30D9
runner SHA256 = 89C12064BA72ADB70C443DD14B0A64B5139314D8AB996A9FB2C63E7F6F4B6FF3
reference raw SHA256 = 0BFC88D8FFC5196B137570B149CBBC7ED3B93DC3EF81D14D9E7F4F130E050234
error batch = 2; used = 3/10; cumulative = 13
```

Segmentácia `10+10+9` je technické rozdelenie presne tej istej
29-krokovej bisection operácie. Nemení mechanizmus, stavový priestor,
prahy, sampled body ani fyzikálnu interpretáciu.

## Autoritatívny rozsudok

```text
AUTHORITATIVE_DECISION = WORKING_ACCEPTED_NINE_CELL_SAMPLED_LEGACY_SENSITIVITY
RELEASE_STATUS = NOT_RELEASED
FINDING_ID = NONE
FINDING_CLASS = NONE
TRACK_IDENTITY_GATE = SAME_TRACK_CONFIRMED
RUN_AUTHORIZED = false
```

## Povinné nonclaims

- Nie je to likelihood, posterior, confidence/credible interval, fit ani
  spojitá `Delta N_eff` obálka.
- Nie je to aktuálna tvrdá predikcia `H0` alebo `S8` pre v3.18.
- `H0` je podmienená numerická inverzia voči syntetickej legacy kotve
  `h_ref=0.673`.
- `S8` používa zjednodušený rast a pevný comparator
  `sigma8_LCDM=0.811`; nejde o G9 CMB/lensing výsledok.
- `Delta N_eff=0` znamená iba nulový legacy príspevok pary. Nie je to
  LambdaCDM ani vypnutie palivovo-hmotového mechanizmu.
- Výsledok neuzatvára P5.4, G8, G9, covariance, gauge, causality ani
  perturbatívnu stabilitu.
- Nemení A2-K4, stav A1-K1, skóre ani hĺbku.

## Ďalší krok

Jeden canonical externý `T2_REPRODUCIBLE_CALCULATION` balík s presnými
contractmi, RC zdrojmi, všetkými immutable rawmi, runtime mapou a fresh-copy
reprodukciou. Bez nového projektového vedeckého behu.
