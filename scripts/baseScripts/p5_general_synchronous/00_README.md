# p5_general_synchronous — aktívne formulačné jadro A2-K4/P5

**Vlastník:** `A1K1 → A2K4 → P5`  
**Stav:** `ACTIVE_FORMULA_SCOPE / CDI SUPPORT-03 REVIEW / M1 ORDER-7 POWER7 PRECISION REVIEW`

Tento balík oddeľuje spoločné rovnice od tenkých runnerov P5. Obsahuje
koeficientové identity, constraintové identity, leading seedy, prvý fotónový
TCA člen a skorý opacity ledger. Každý modul má užší rozsah než celá P5.

ARCH-A uzavrela B1 contract a AD/k=.05/nominal J4 support sentinel, nie celý
P5.3 seed. Fyzický S-M parný seed stále nie je odvodený.
`mode_resolved_puiseux.py` navyše nemá uzavretý
palivový coefficient/row kontrakt: leading `delta_f,U_f` vložil pevne a
neoveril ich continuity/Euler na celej použitej veži. V2 modul korektne
ukotvuje M1, ale neopravuje tento PF-058 rozsah. Preto tento balík
neoprávňuje P5.4, G8 ani G9.
Vlastnícky kontrakt je
`tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/00_WORK_PLAN.md`.

Conditional S-C0 formula je zmrazená v dokumente 51. Jej lower-moment
coefficient lift/collapse passport prešiel v KMPC-033; vyššie päťmódové
multipólové koeficienty ani S-M nepokrýva.

Pre KMPC-032 sú vytvorené dva oddelené moduly:

- `s1_collective_contract.py` — nezávislý contract bez solvera;
- `s_c0_coefficient_passport.py` — V1 auditný lift/collapse, PF-069 history;
- `s_c0_coefficient_passport_v2_numpy_scalar.py` — autoritatívny úzky
  technický overlay pre immutable KMPC-033 výsledok SHA `4CED9D...CFE8C`.

Prvý audit 276 zastal technicky na PF-069 pred fyzikálnou identitou. V1 sa
nemení. `s_c0_coefficient_passport_v2_numpy_scalar.py` je jediný povolený
RERUN1 overlay: opravuje iba konverziu numpy skalára a po behu obnoví V1
helper. Zmrazený rozsah je v dokumente 54.

`cdi_c1_coverage.py` vykonal immutable KMPC-034 (result SHA
`37FB4453...DCE20`). Nemenný CDI R-A solver dal core/common PASS; powers
2–3 ukázali, že baseline `[0,1]` nestačí.

`cdi_support_ladder.py` vykonal immutable KMPC-035 (result SHA
`A9BD519F...E42A01`). Reprodukoval `[0,1]/[0,3]`, vyriešil `[0,5]`, obnovil
dočasné shape guardy a súdil F0 aj M3 cancellation-safe obálkou. Core/common
prešli, ale `[0,3]` remainder pri `z=.01` neprešiel pre `delta_f` a
`sigma_fs`. Identita: `GLOBAL_C1/CDI_SUPPORT_STEP_2`, nie Fourier C2.

Hashe, runnery a rozsahy: `../00_MODULE_OWNERSHIP_REGISTER.md`.

Ledger `Phi^0/Phi^1 × z^j`, species/Bianchi kontrakt a AD support boli
vykonané v balíkoch 4–10. Pred support step 3 musí vzniknúť samostatná M1
order-7 provenance/holdout brána; priamy `[0,5]→[0,7]` je zakázaný. Balík
výslovne ešte neobsahuje celý päťmódový P5.3 verdict, finite opacity, P5.4
ani G8.

`m1_order7_provenance.py` je tenký vykonaný KMPC-036 auditný adaptér. Volá existujúci
hard-anchored helper s `order=5/7`, ale autoritatívne znovu zostaví všetkých
121 driver+initial a 18 nezávislých holdout riadkov pre powers `-1..7`.
Nemení rovnice a nesmie volať CDI support step 3. Result SHA
`39BB3886...B7B497`: všetky holdouty a proveniencia PASS, ale tri terminal
driver `[7]` riadky majú relative precision-floor REVIEW pri absolute
residualoch `~1e-15`. Ďalší krok je samostatný precision/boundary audit.
