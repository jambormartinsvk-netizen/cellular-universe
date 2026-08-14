# Pokyny externému auditorovi — EA-022

Over manifest, source/copy paritu, runtime mapu a oddelenie technických
incidentov od výsledku. Reprodukcie rob v dvoch samostatných čerstvých
kópiách `REPRO`; generated výstup z jednej vetvy nesmie byť vstupom druhej.

Over najmä:

- shape `121×98` a native/frozen/expected rank `98/98/98`;
- condition `634.5198855041807/634.5198855041809` a singular minimum
  `0.5374081557113753/0.5374081557113750`;
- RHS exact equal, matrix changed count `26`, maximum `1.7763568394e-15` v
  `fs_shear[6] × eta[6]` a relative Frobenius difference `6.0852e-18`;
- nula nulových stĺpcov, päť rovnakých nulových riadkov a plný stĺpcový rank;
- `authoritative_high_precision_m1_solve_count=0` a
  `pass_c2_atom_candidate=false`;
- KMPC-100 source SHA `93780C85...E96ECD9`, všetky receipt checks true a
  žiadny matrix rerun;
- PF-096 až PF-103 ako technickú audit trail bez fyzikálneho STOP.

Pre každý príkaz zapíš exit code, wall time, SHA generated JSON a odchýlky.
KMPC-099 official má očakávaný exit code 2 až po vytvorení generated JSON;
KMPC-100 official má exit code 0. Porovnaj KMPC-099 po odrátaní iba runtime
poľa, KMPC-100 byteovo. Každú inú odchýlku označ osobitne.
