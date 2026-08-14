# Erratum/rozsah skriptu 78 — chýbajúci lokálny Fortran kompilátor

Skript `78_script_A2_K4_3b_RG_collective_CAMB_regular_seed_active_start_fixed.py`
opravil chybu nulových placeholderov skriptu 77, ale pridal symbolický export
`pi_r`. Lokálny predkompilovaný CAMB 1.6.6 funguje; kompilácia nového
symbolického source výrazu však vyžaduje `gfortran >= 6` alebo `ifort`, ktorý
v prostredí nie je dostupný. Beh preto skončil `ERROR_UNCLOSED`.

Tento stav nie je fyzikálnou smrťou K4.3b. Skript 79 používa iba premenné
vystavené predkompilovaným binárnym backendom a zachováva opravenú logiku
spoločného aktívneho štartu. Hodnota neutrínového kvadrupólu sa v skripte 79
nenahrádza nulou; presné koeficienty neutrínovej hierarchie auditoval skript
76.
