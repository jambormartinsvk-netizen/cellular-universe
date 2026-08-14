# A2-K4.3b-RG BR3C-a — výstup skriptov 130 až 135

**Dátum:** 2026-07-14  
**Konečný rozsudok C7.7a:** `PASS`  
**K4:** `ŽIVÁ; 66.2/100; G6 PASS; G7 OTVORENÁ`

## Behy a zachované neúspechy

| Skript | Stav | Význam |
|---|---|---|
| 130 | `PASS_BR3C_A_TWO_SURFACE_STATE`, `74/74` | Prvý export dvoch povrchov; interné kontroly nestačili na prijatie. |
| 131 | `REVIEW_BR3C_A_ORDER_AUDIT_UNCLOSED`, `6/13` | Správne odhalil nestabilné `F3/F4` po delení round-off nulových slotov malým `s/s^2`. |
| 132 | `PASS_BR3C_A_REGISTERED_ZERO_STATE`, `76/76` | Nuluje iba sloty explicitne fixované počiatočným a regularitným ledgerom. |
| 133 | `ERROR_UNCLOSED` | Transformačný marker pre source verdict mal dva výskyty namiesto jedného; fyzika sa nespustila. |
| 134 | `PASS_BR3C_A_PROJECTED_ORDER5_ORDER6_AUDIT`, `15/15` | Nezávislý rád 5/6 audit pri pôvodnej stavovej tolerancii. |
| 135 | `PASS_BR3C_A_MANIFEST_CREATED` | SHA-256 manifest skriptov 130–134. |

Skripty 130, 131 a 133 sa nemažú. Dokumentujú, prečo samotný interný PASS
130 nebol prijatý a prečo oprava 132 nie je prahové čistenie výsledku.

## Autoritatívny export 132

Zmrazené povrchy:

| Povrch | `x=ln(a)` | `z=k a/(H0 sqrt(Omega_r))` |
|---|---:|---:|
| deep | `-25` | `3.20708749444715e-7` |
| shallow | `-23` | `2.36973494106489e-6` |

Backgroundový súčet piatich `Omega_A` mal na všetkých štyroch
mód/povrchoch rezíduum numericky `0`.

| Mód/povrch | `F3_fs` | `F4_fs` |
|---|---:|---:|
| NID/deep | `2.82980496610322e-22` | `1.00838143526908e-29` |
| NID/shallow | `1.14162453367257e-19` | `3.00594367414874e-26` |
| NIV/deep | `6.62619004560501e-15` | `3.14826236242080e-22` |
| NIV/shallow | `3.61777665098466e-13` | `1.27009939110856e-19` |

Projection ledger:

| Mód | Počet presne registrovaných nulových slotov | Najväčšia odstránená absolútna hodnota |
|---|---:|---:|
| NID | `40` | `1.90125692967058e-15` |
| NIV | `38` | `6.38378239159465e-16` |

Nebola použitá podmienka `abs(coefficient)<epsilon`. Sloty boli vybrané iba
podľa už existujúcich počiatočných a gradientovo-regularitných rovností.

## Nezávislý audit 134

```text
checks                         = 15/15
maximum_absolute_difference    = 4.65661287307739e-10
maximum_scaled_difference      = 2.49518043443058e-11
runtime                        = 1.812 s
```

Maximálny absolútny rozdiel vzniká pri veľkej rescalovanej NIV rýchlosti;
prešiel súčasnú absolútnu aj škálovanú predregistrovanú podmienku. Nebola
uvoľnená tolerancia po zobrazení výsledku.

## SHA-256

| Súbor | SHA-256 |
|---|---|
| `130_script_A2_K4_3b_RG_BR3C_a_two_surface_state_export.py` | `c5fdb8370fb339e56ee371ca4e0753c5673ac50201228a3f9813a1422cd91666` |
| `131_script_A2_K4_3b_RG_BR3C_a_order5_order6_state_audit.py` | `702afdd878902f8c63d53de13be91a59b015c692656b55c7ebfbd7c47583b03c` |
| `132_script_A2_K4_3b_RG_BR3C_a_registered_zero_projection.py` | `a67a12cb11042aa5d18dcb94c5c44a7fe721075c1b7f1d1894cb13b729cccbbb` |
| `133_script_A2_K4_3b_RG_BR3C_a_projected_order_audit.py` | `55058ff1c292e9b00f18356fdbbdae9964074d9cd52d3fdc732a2e00f120af72` |
| `134_script_A2_K4_3b_RG_BR3C_a_projected_order_audit_fixed.py` | `ad2f51633f54ccb8985dbba3b11350ec4f385ed24d2625d0947fa6d8a41d02ea` |

## Rozsah PASS

C7.7a dokazuje iba konzistentnú konštrukciu dvoch povrchov toho istého
koeficientovo normalizovaného riešenia. Nedokazuje evolučnú zhodu, štyri
Einsteinove rezíduá počas evolúcie, plný photon/polarization/recombination
backend, G7 ani `S8`.

