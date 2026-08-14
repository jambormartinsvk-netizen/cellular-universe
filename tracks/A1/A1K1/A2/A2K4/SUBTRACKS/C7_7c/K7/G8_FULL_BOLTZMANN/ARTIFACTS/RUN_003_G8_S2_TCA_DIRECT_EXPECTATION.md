# RUN-003 — G8 SCREEN-S2: očakávanie pred evolúciou TCA/direct

**Rodič:** `A1-K1 → A2-K4 → C7.7c-K7 → G8`  
**Vstup:** `S0+S1 PASS 40/40; support/WBS 90/100`  
**Skript:** `scripts/222_script_A2_K4_C7_7c_K7_G8_S2_TCA_direct_screen.py`

## Čo sa počíta ľudskou rečou

Na krátkom skorom intervale `x=-23 → -22` sa porovnajú dva opisy tej istej
fotónovo-baryónovej hybnosti na presnom K4 pozadí zo zmrazeného skriptu 213:

1. **direct:** oddelené rýchlosti `U_gamma`, `U_b` a explicitný tuhý
   Thomsonov prenos hybnosti;
2. **TCA:** ich spoločný K7 limit
   `U_x=qU-R/(1+R)U+delta_gamma/[4(1+R)]`.

Sonda používa normovaný konštantný lineárny zdroj `delta_gamma=1e-6` a
pevnú bezrozmernú opacitu `chi=100`. Je to zámerne operátorový test: `chi`
nie je odvodená ionizačná história a tento beh preto **nesmie** tvrdiť
rekombináciu, CMB ani plný G8 PASS.

## Predregistrované rovnice

Pri `R=3 rho_b/(4 rho_gamma)` a `chi>0`:

```text
U_gamma,x = q U_gamma + delta_gamma/4 + chi (U_b-U_gamma)
U_b,x     = (q-1) U_b + chi/R (U_gamma-U_b)
```

Po váženom sčítaní a v limite `U_b=U_gamma` presne vznikne K7 TCA rovnica
uvedená vyššie. Algebraický dôkaz je S1; S2 overuje numerický overlap
explicitne tuhého a redukovaného operátora na meniacom sa K4 pozadí.

## Očakávanie a PASS/STOP

- oba integrátory dosiahnu `x=-22`, majú konečný stav a neprekročia
  normalizačný safety cap `1e6`;
- `max |U_gamma(direct)-U(TCA)| / max |U(TCA)| <= 1e-4`;
- `max |U_b-U_gamma| / max |U_gamma| <= 1e-6`;
- efektívny tight-coupling parameter
  `1/[chi(1+1/R)] <= 1e-6` na celej trajektórii;
- zdrojový SHA-256 skriptu 213 musí presne sedieť s K7d manifestom;
- direct Radau a TCA DOP853 majú oddelený `RHS_CAP=100000`, interný deadline
  `45 s`; celý proces má externý timeout `55 s`.

**PASS:** iba `SCREEN-S2 PASS`, skóre `0`, povolí sa S3.  
**STOP:** nesplnený overlap/slip pri platnej numerike je
`STOP_G8_TCA_DIRECT_MISMATCH`; import, timeout, cap alebo zmena zdroja sú
technické `REVIEW`, nie smrť K7.  
**Mimo rozsahu:** fotónový šmyk/polarizácia, neutrínový chvost, fyzikálna
opacita a rekombinácia — tie patria do S3/FULL.

## Preflight

Pred autoritatívnym JSON sa samostatne spustí `py_compile`, `--help` a
`--smoke`; každý Python proces má vonkajší limit. PF-035 pripomína, že aj
takýto preflight musí mať tento dokument vopred.
