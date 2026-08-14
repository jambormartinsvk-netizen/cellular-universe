# L2-B1 — predregistrácia: equation/state audit projektovaného K7 lineage

**Stav pred behom:** `PRIPRAVENÉ`  
**Skript:** `scripts/238_script_lineage_L2_B1_projected_k7_ast_audit.py`  
**Vnútorný limit:** 5 s. **Vonkajší limit:** 10 s. **Bez importu modelov a ODE.**

## Otázka

Ktoré skripty v K7 projected lineage priamo definujú redukovanú 13-state
RHS bez `U_c`, ktoré ju iba kontrolujú a ktoré sú iba historické pomocníky?

## Vstupný balík

`179, 181–183, 197, 203–210, 213–216` plus všetky jeho explicitne
uvedené `physical_rhs` potomky. Každý analyzovaný súbor dostane jeden status:

- `DEFINES_LIMITED_RHS`;
- `CHECKER_OF_LIMITED_RHS`;
- `HISTORICAL_RESULT_OR_LINEAGE_HELPER`.

## Očakávania

Očakávame, že definujúce K7 skripty nemajú identifikátor `U_c`; aspoň 197,
209 a 213 používajú `K_MPC=0.05` v backgroundovej formulácii. PASS auditu
znamená, že táto mapa sa dá presne reprodukovať; neznamená PASS ich fyziky.

## STOP

Chýbajúci súbor, neparsovateľný zdroj, timeout alebo neočakávaný plný K4
stav v definujúcom skripte zastaví klasifikáciu, kým sa nevysvetlí zmena.
Po PASS sa Markdown verdict zapíše ku každej triede; až potom sa rieši B2.
