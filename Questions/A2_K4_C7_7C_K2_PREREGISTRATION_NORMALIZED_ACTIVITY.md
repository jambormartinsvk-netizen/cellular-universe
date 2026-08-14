# A2-K4 C7.7c-K2 — predregistrácia normalizovanej activity koľaje

**Dátum:** 2026-07-14  
**Rodič:** C7.7c; K1 uniformný `atol` je zachovaná ako mŕtvy numerický dôkaz  
**K4 vstup:** `66.5/100`

## Jediná zmena

Fyzický stav a ODE 136 sa nemenia. Integrátor pracuje s

```text
w_i = y_i/scale_i,
scale_i=max(abs(y_i(x_start)),1e-300),
dw_i/dx = RHS_i(x, scale*w)/scale_i.
```

Scale sa určí samostatne pre každý mód/povrch zo vstupu 132 ešte pred
integráciou. Žiadna scale nepoužíva endpoint, výsledok 140/141 ani žiadané
znamienko.

## Numerika

| Položka | Hodnota |
|---|---:|
| solver | `DOP853` |
| normalized `rtol` | `1e-10` |
| normalized `atol` | `1e-12` |
| `max_step` | `0.02` |
| segment | `1 e-fold` |
| `x_final` | `-18` |
| interný/vonkajší limit | `50/60 s` |

## Normalizovaná aktivita

Pre komponent `i`:

```text
floor_i=max(10*atol_norm,10*rtol*max(abs(w_i))).
```

PASS vyžaduje na každej zo štyroch trajektórií a pre všetkých 13
komponentov:

```text
max_checkpoint_abs((dy_i/dx)/scale_i) > floor_i
max_checkpoint_abs(Delta(y_i/scale_i)) > floor_i.
```

Ďalej musia znovu prejsť všetky C7.7b kontroly, presná množina kľúčov,
konečnosť a safety cap vo fyzických premenných.

Ak K2 prejde, C7.7c dostane `+0.2` a K4 bude `66.7/100`. Ak neprejde,
zostane `REVIEW`; activity floor sa po výsledku nemení.

