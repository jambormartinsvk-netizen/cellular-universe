# RUN-002 — očakávanie technickej opravy PF-034

**Nástupca:** `scripts/233_script_A2_K4_C7_7c_K7_G8_S0_S1_PF034_corrected.py`  
**Rozsah:** iba oprava formálnej identity `inv1r=1/(1+R)` z RUN-001.

Výpočet znovu nerieši ODE, rekombináciu ani dáta. Znova má mať 40 presných
algebraických kontrol. Očakávanie je `40/40 PASS`, pretože RUN-001 už
potvrdil zvyšných 39 identít a opravuje sa iba smer symbolickej substitúcie.

**PASS:** SCREEN-S0+S1 je uzavretý so skóre `0`; povolí sa SCREEN-S2.  
**STOP:** ak zlyhá iná identita alebo opravená identita, G8 ostáva na
`STOP_G8_IMPLEMENTATION_MAPPING` a vyžaduje sa audit bez fyzikálneho
verdiktu.  
**Limity:** vnútorný 10 s, vonkajší 15 s; pred behom oddelene `py_compile`,
`--help`, `--smoke`.
