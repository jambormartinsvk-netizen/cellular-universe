# A2-K7.0 — manifest dôkazov

**Dátum:** 2026-07-13  
**Algoritmus:** SHA-256  
**Rozsudok balíka:** `PREŽÍVA K7.0 — 30/100`

| Súbor | Bajty | SHA-256 |
|---|---:|---|
| `scripts/50_script_A2_K7_0_mediator_ledger_collision_gate.py` | 8449 | `E1317B772F73AB37B277D10A6DFC342692068080CFA7AE32F1FD5A6A18FE90B8` |
| `Audit/A2_K7_0_NUMERICAL_OUTPUT.md` | 2401 | `F9D1FA40F90CF178A1932F867A26B8A72F33B34B504EC46D39269D5FB3C20FC6` |
| `Audit/A2_K7_0_akcna_ledgerova_a_collision_brana.md` | 7589 | `3E62D77A53EA848D9FAB6370999D8CC20EA60F40DEE62C551B12F485EFFD9540` |
| `Audit/A2_KATALOG_STAVOVE_ERRATUM_PO_K7_0.md` | 739 | `F2BF1915FD6EACC2DF6487FE74142DDF5109D43F9B05F5079DEA31C255CEAAEA` |
| `Questions/A2_K7_STAV_A_AKCNY_PLAN_PO_K7_0.md` | 2762 | `83443E691A3E313C5558E90FFEBC008D092CE4C2613FE650FAD607CFAE2B6F21` |
| `Questions/A3_STAV_A_AKCNY_PLAN_PO_K7_0.md` | 1139 | `62E5B9E1EB838999C3A081149F5E07FA88B0AD616D13A209B18E867F02BEA0AA` |
| `theory/SK/05n_Methodology_Rules_and_Question_Register_A2_K7_0_SK.md` | 1991 | `FAAC34D1620C9ACA408938F5D0F066059AB564D7B76DD75768A732B27D2ED4FB` |
| `theory/EN/05n_Methodology_Rules_and_Question_Register_A2_K7_0_EN.md` | 1945 | `01E3E42799C168A75377B830968F9189FB7CAD0F6BF6FDE09144BFC4DD22AFBB` |

## Auditná väzba

- skript 50 reprodukuje iba backgroundový ledger a collision eigenhodnoty;
- numerický výstup zachováva predregistrovaný grid a čísla;
- hlavný audit oddeľuje lokálnu UV akciu od zatiaľ neodvodeného
  coarse-grained Markovovského toku;
- plán K7.1 obsahuje všetky zostávajúce kill brány;
- AR12/Q41 sú uložené obsahovo zrkadlovo v SK aj EN.

Staršie katalógové stavy `ČAKÁ` sa nemažú. Ich obmedzenie je explicitne
zapísané v stavovom erráte a v registri 05n.

