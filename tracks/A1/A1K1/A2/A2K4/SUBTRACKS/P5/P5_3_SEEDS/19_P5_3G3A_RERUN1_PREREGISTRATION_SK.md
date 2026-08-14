# P5.3g3a RERUN1 — predregistrácia skutočného výstupu `qn`

**Skript:** `scripts/253_script_KMPC_016_P5_3g3a_seed84_qn_semantics_rerun1.py`  
**Nadväzuje na:** 252, PF-045.  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE a bez skóre.

RERUN1 už neporovnáva presne `eta`, pretože `Omega_m tau` je subleading a pri
fixnom `k tau` sa mení s `k`. Overí len relevantné tvrdenie: funkcia 84 vracia
`qn=4 tn/(3k)` a pre NIV je toto **vrátené** `qn` pri fixnom `y=k tau`
invariantné. To je nutná, nie postačujúca kontrola pred novou deriváciou `F2`.

**PASS_SCOPE:** explicitný return a fixed-`y` NIV kontrola prejdú. **REVIEW:**
ak nie, P5.3g2 sa obmedzí. Výsledok stále nepreukazuje celý štandardný seed.
