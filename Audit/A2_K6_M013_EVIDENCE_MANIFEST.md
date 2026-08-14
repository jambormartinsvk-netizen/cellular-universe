# A2-K6/M-013 — manifest zachovaných dôkazov

**Dátum:** 2026-07-13  
**Algoritmus:** SHA-256  
**Účel:** spätný audit mŕtvej koľaje; žiadny uvedený súbor sa pri uprataní
nesmie stratiť ani ticho prepísať

| Súbor | Bajty | SHA-256 |
|---|---:|---|
| `scripts/47_script_A2_K5_K3a_action_background_stability_gate.py` | 6873 | `4DF23622A64836A818BBD0BBF4DFBB0557A07FA136027B98F92B09A1815DCAF3` |
| `scripts/48_script_A2_K6_1_exact_Gij_and_growth_gate.py` | 14142 | `6E66E23D7A411F7E05DD42CAB36D6B5BAD8D6883ABAEFEA1702AE3655A533727` |
| `scripts/49_script_A2_K6_1_continuous_eta_no_go.py` | 11396 | `BFBB2DE6A65783C12F4E59379559A709BEA5076F997E00BC3C3726EF6F277253` |
| `Audit/A2_K5_K3a_0_akcna_backgroundova_stabilitna_brana.md` | 4652 | `0B479A6711F19F0804F467B970940193101FA4A1BDF0D00D41EF37AADB1CE511` |
| `Audit/A2_K6_1_NUMERICAL_OUTPUT_M013.md` | 2741 | `4A3CAB6D554928100971BF1E134D313A7DD7B38A3C501FD58359ABD12E8A430C` |
| `Audit/A2_K6_MRTVA_M013_exact_Gij_a_spojity_eta_no_go.md` | 6229 | `59BD09DD02FC9FA0A65C8F7D5F1013D8B6A0CE486ABC798D7221514D9EF0231A` |
| `Questions/A3_STAV_A_AKCNY_PLAN_PO_M013.md` | 5042 | `780CB764E922C83CD7F6D656888E316C66B72F115A25914B69A84FEAFB84C870` |
| `theory/SK/05m_Methodology_Rules_and_Question_Register_A2_K6_M013_SK.md` | 2147 | `40F6A2C5F98457910736F7BE782276D97005470EC99FA5A76894C6D0C8167687` |
| `theory/EN/05m_Methodology_Rules_and_Question_Register_A2_K6_M013_EN.md` | 2137 | `64727677B673CEEDB148319518C3B745BF79146A62FCD204E19744CD64EB8E11` |

## Väzby medzi dôkazmi

- skript 47 dokazuje iba K6.0 backgroundovú a kinetickú bránu;
- skript 48 zachováva prvý grid, vrátane neskôr obmedzeného machine-labelu
  nulového limitu;
- skript 49 je rozhodujúci pre analytický nulový limit, spojitý `eta>=0`
  no-go a konvergenciu;
- hlavný audit vysvetľuje, prečo novší výsledok obmedzuje starší bez jeho
  vymazania;
- SK/EN register udržuje AR11 a Q40 obsahovo zrkadlové.

## Stav repozitára

Príkaz `git status --short` v `D:/Teoria` dňa 2026-07-13 vrátil
`not a git repository`. Pripojenie pracovného adresára k
`github.com/jambormartinsvk-netizen/cellular-universe`, mapa presunov a prvý
commit preto zostávajú explicitnou úlohou pred publikovaním na Zenodo.

