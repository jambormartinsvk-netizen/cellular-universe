# A2-K4.3b-RG BR3B-2g — výstup skriptov 126 až 129

Dátum: 2026-07-14  
K4: **ŽIVÁ, 60/100 = G6**  
BR3B-2g: **PASS**

## Behy

| Skript | Stav | Dôkazná váha |
|---|---|---|
| 126 | `REVIEW_HIERARCHY_REGULARITY_MISSING_PRESERVED` | Správne rovnice, ale dva nepovolené homogénne `L3/L4` módy kontaminovali skoré koeficienty; `30/40`. |
| 127 | `PASS_BR3B2G_L3_ASH_FULL_LEDGER` | Po regularite `40/40`, fyzikálne ranky `66/66`, lambda-zero regresia PASS. |
| 128 | `PASS_BR3B2G_EXACT_ORDER_AND_HIERARCHY` | `16/16` presných identít backgroundu, poradia a rescalovanej hierarchy. |
| 129 | `PASS_MANIFEST_CREATED` | SHA-256 ledger skriptov 126–128. |

## Skript 127 — order 6

| Mód | Matica/rank | Condition | Škálované rezíduum | Max. riadok |
|---|---|---:|---:|---:|
| NID | `88x66`, `66/66` | `255.13` | `2.332e-15` | `1.145e-15` |
| NIV | `88x66`, `66/66` | `324.22` | `2.866e-15` | `4.399e-15` |

Nové diagnostiky:

| Mód | `(3/5)L3` | Ash `delta_c` | Ash/CDM stress |
|---|---:|---:|---:|
| NID | `-4.122862e-3` | `5.363866e-12` | `-4.491322e-13` |
| NIV | `-2.699254e-2` | `6.919397e-11` | `-3.847021e-12` |

Order 5 dal znovu `40/40`, rank `66/66`; nové koeficienty sa od order 6
líšili najviac približne o `1.21e-16`.

## Reprodukčný manifest

| Súbor | SHA-256 |
|---|---|
| `scripts/126_script_A2_K4_3b_RG_BR3B2g_l3_ash_full_ledger.py` | `5ce670e19f068567ed5066b9d851943a9ee8cffbeb98dabd608d4f5993682a72` |
| `scripts/127_script_A2_K4_3b_RG_BR3B2g_l3_ash_regular_hierarchy.py` | `1bc0ad751fd7a990f057b94333433f9a12c2e7f2be879cfc7605b0fe240fdc6b` |
| `scripts/128_script_A2_K4_3b_RG_BR3B2g_exact_order_and_hierarchy_audit.py` | `998a7d42102701e870a3b13f10bd3aef21457e2e109bee85cedd665f23c265d6` |

