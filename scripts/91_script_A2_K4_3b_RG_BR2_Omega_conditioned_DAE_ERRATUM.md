# Erratum skriptu 91 — iba JSON typ

**Dátum:** 2026-07-14

Prvý beh skriptu 91 dokončil numerickú časť, ale pri záverečnom `json.dumps`
vrátil `ERROR_UNCLOSED`, pretože kontrola interného módu bola typu
`numpy.bool_`, ktorý štandardný JSON encoder neserializuje.

Opravný alias `92_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE_json_fixed_alias.py`
mení iba serializáciu `numpy.bool_ -> bool` a potom vykoná nezmenený skript
91. Rovnice, tolerancie, počiatočné podmienky a integrátor sa nemenia.

Prvý beh nie je fyzikálny `FAIL` ani dôvod smrti koľaje; je to výlučne
výstupná chyba.
