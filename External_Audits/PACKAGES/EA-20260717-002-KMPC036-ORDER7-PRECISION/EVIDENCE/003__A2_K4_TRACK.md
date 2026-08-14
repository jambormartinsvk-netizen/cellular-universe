# A1K1 → A2K4 — entalpicky vážený energy-frame

**Stav:** `ŽIVÁ / S-C0 LOWER-MOMENT PASS / CDI STEP-2 CORE+COMMON PASS / SUPPORT-03 REMAINDER REVIEW / MODE COVERAGE OPEN`  
**Fyzikálna hĺbka:** `60/100`  
**Historická technická hĺbka K7:** `66.5/100` — neprenosná na K4  
**Aktívna formulácia:** `SUBTRACKS/P5`

A2-K4 smeruje prenos energie a hybnosti podľa spoločnej entalpicky váženej
rýchlosti tmavého sektora. Od K1 a K3 sa líši tým, že neprivileguje iba
popol ani iba palivo. Plná implementácia preto povinne obsahuje samostatné
`U_c`, `U_f` a `U_d=(1-beta)U_c+beta U_f`.

Historická K7 línia prešla mnoho technických brán v projektovanej
13-zložkovej RHS, ale nemala dynamické `U_c` a používala starý fixed-`K_MPC`
background. Jej výsledky zostávajú auditovateľnou históriou, nie fyzikálnym
PASS A2-K4. Aktívny nástupca P5 obnovuje plný general-synchronous stav.

Ohraničený šírkový audit 2026-07-16 potvrdil, že K4 je jediná živá A2
koľaj na alebo nad `50/100`. To nie je nový PASS: pred G7 treba uzavrieť
normalizáciu `A_f`, coefficient/row manifest, úplné fuel/ash rows,
Bianchi/left-null identitu a plný seed.

Balíky 6–10 sú historicky uzavreté. KMPC-031 priniesol interpretovateľný
čiastkový výsledok pre `AD/k=.05/nominal`, preto je podľa najnovšieho
pravidla aktívny counter po sebe idúcich technických zlyhaní `0/10`;
`historical_packages_total=10` sa zachováva. KMPC-033 následne uzavrel iba
conditional S-C0 lower-moment
lift/collapse bez double countingu. Otvorené zostávajú S-M, skutočné vyššie
multipóly, CDI/BI/NID/NIV, ďalšie `k`/varianty a finite opacity. KMPC-035
potvrdil stabilitu CDI core/common medzi `[0,3]` a `[0,5]`, ale vyvrátil
dostatočnosť `[0,3]` pri `z=.01`. KMPC-036 prešiel order-7 provenance a
holdouty, ale tri driver `[7]` riadky ostali precision REVIEW. Ďalší krok je
precision/boundary closure audit; support step 3 ostáva blokovaný. Hĺbka
ostáva `60/100`.

- hrubý plán: `00_WORK_PLAN.md`;
- detail P5: `SUBTRACKS/P5/00_WORK_PLAN.md`;
- artefakty: `ARTIFACTS/00_MANIFEST.md`;
- base závislosti: `BASE/00_BASE_DEPENDENCIES.md`;
- história: `HISTORY/00_EVENT_LEDGER.md`.
