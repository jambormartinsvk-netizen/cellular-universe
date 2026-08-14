# RUN-001 — technický STOP PF-034: zápis `inv1r`

**Artefakt:** `ARTIFACTS/RUN_001_G8_S0_S1_STRUCTURAL_RESULT.json`  
**Verdikt artefaktu:** `STOP_G8_IMPLEMENTATION_MAPPING`  
**Fyzika/ODE:** nevykonaná  
**Účinok na skóre:** `0`

Z 40 kontrol prešlo 39. Nulové sú všetky CAMB rezíduá (22), počty stavov
32/44/56, K7 multipólové redukcie, Thomsonova hybnostná kancelácia, oddelený
fotónovo-baryónový Euler aj projekcia `M`. Jediná chyba bola kontrola
`combined_Euler_to_K7_background_notation` s rezíduom

```text
delta_gamma*(-inv1r*(R + 1) + 1)/(4*(R + 1))
```

To neukazuje fyzikálnu nezhodu. Starý skript nahrádzal výraz
`1/(1+R)` symbolom `inv1r` v opačnom smere a SymPy preto nemal informáciu
o definujúcej rovnosti `inv1r=1/(1+R)`. Správna kontrola musí dosadiť
obidve definície do generického K7 zápisu:

```text
load_fraction = R/(1+R),   inv1r = 1/(1+R).
```

Skript 221 a jeho shared modul sa nemenia; zostávajú reprodukovateľným
zdrojom tohto technického STOP. Nástupca 233 je ohraničená technická oprava
iba tejto substitúcie a nesmie meniť žiadnu z ostatných 39 identít.
