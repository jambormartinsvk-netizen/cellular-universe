# Contract: trojbodová legacy citlivosť `H0` a `S8`

**Task ID:** `V318-PT1-H0-S8-C1-20260730`  
**Route:** `RELEASE/v3.18/PT1_H0/C1`  
**Fáza:** `CONTRACT_DRAFT`  
**RUN_AUTHORIZED:** `false`  
**Dôkazový cieľ:** sampled citlivosť historickej v3.17 pipeline, nie plný
rozsah aktuálnej teórie

## 1. Otázka a DONE_WHEN

Pri nezmenenej historickej flat pipeline vypočítať tri body

```text
Delta N_eff = 0, 0.02675, 0.0535
```

a zistiť, ako odstránenie legacy pary mení podmienené `H0` a `S8`.
Výsledok je hotový iba ak každý bod prejde zmrazenými numerickými guardmi,
full-steam bod reprodukuje historické comparatory a nezávislý science audit
potvrdí presný scope.

## 2. Claim a nonclaims

Povolený claim:

```text
THREE_POINT_LEGACY_ANCHOR_H0_S8_SENSITIVITY
```

Zakázané interpretácie:

- nejde o confidence/credible interval ani posterior;
- nejde o spojitý envelope medzi troma bodmi;
- nejde o publikovateľnú tvrdú predikciu `H0` alebo `S8`;
- nejde o P5.4, G8 alebo G9 výsledok;
- `S8` dedí pevný comparator `sigma8_LCDM=0.811` a zjednodušenú rastovú
  rovnicu bez plnej fotónovej/neutrínovej Boltzmannovej hierarchie;
- `Delta N_eff=0` je steam-null, nie nulový limit celej K4 fyziky.

## 3. Source lineage

Kanonický formulačný predok je
`scripts/09_script_K3_cosmology_pipeline.py`, SHA-256
`349C209EBEC4E8F56D2E9BB47DC2A0349DD4FA8FA4FB517916C537540EFA6008`.

Skript 17, SHA
`36094FD6FAE4D8A3D9D43B2172C28582AFC2B5ADF29D68C18372F9CE8A976998`,
je iba reprodukčný comparator pre `H0=66.37` a `S8=0.8745`; jeho krivostná
vetva ani pseudo-`chi2` sa neprenášajú.

Lineage audit, SHA
`80AB8AB1E094CE6D224B9BFE46016373A26E1DE71373C2F63977218B2904AFA4`,
potvrdil syntetickú kotvu z `h_ref=0.673` a opravil označenie `r_d` na
`r_s(z_star)`.

## 4. Zmrazené vstupy a jednotky

```text
c = 299792.458 km/s
omega_b = 0.02237
omega_m = 0.1430
omega_gamma = 2.469e-5
N_eff_standard = 3.046
z_star = 1089.9
x_star = -ln(1+z_star)
h_ref = 0.673
lambda = 0.15
delta = 0.02297
sigma8_LCDM = 0.811
x_min = -7.8
h_bracket = [0.55, 0.80]
Delta N_eff points = [0, 0.02675, 0.0535]
background grids n = [2000, 4000, 8000]
```

`h`, `Omega_i`, `omega_i` a `Delta N_eff` sú bezrozmerné. `H0=100h` má
jednotku `km/s/Mpc`; `r_s` a `D_M` sú v `Mpc`; `theta=r_s/D_M` je
bezrozmerná.

## 5. Zmrazené rovnice

### 5.1 Radiácia a syntetická uhlová kotva

```text
omega_r(dN) = omega_gamma * [1 + 0.2271*(3.046+dN)]
R_b(a) = 3*omega_b*a/(4*omega_gamma)
H_ref(a;dN) = 100*sqrt(omega_m*a^-3 + omega_r(dN)*a^-4 + omega_L)
omega_L = h_ref^2 - omega_m - omega_r(dN)
r_s(z_star;dN) = integral[1e-9,a_star]
  c da / [sqrt(3*(1+R_b))*a^2*H_ref]
theta_ref = r_s(z_star;0) / D_M_LCDM(h_ref,DeltaNeff=0)
D_M_target(dN) = r_s(z_star;dN) / theta_ref
```

`omega_L` musí byť kladné; žiadny `max(...,0)` floor nie je povolený.
Počítaná veličina je `r_s(z_star)`, nie `r_d`.

### 5.2 Legacy fuel–matter–radiation background

Pre `x=ln(a)`:

```text
F' = -3*delta*F - lambda*F/E
M' = -3*M + lambda*F/E
R' = -4*R
E^2 = F+M+R
```

Počiatočné hodnoty pri `x=0`:

```text
R0 = omega_r(dN)/h^2
F0 = 1-M0-R0
```

`M0` sa iteruje tak, aby pri `x_star` platilo

```text
M(x_star) = omega_m*exp(-3*x_star)/h^2.
```

Transfer `-lambda*F/E` a `+lambda*F/E` sa musí v súčte zdrojov presne
zrušiť. Ide iba o homogénny energy-source ledger, nie momentum/Bianchi PASS.

Modelová vzdialenosť:

```text
D_M(h;dN) = c/(100h) * integral[x_star,0] exp(-x)/E(x) dx.
```

Bisekcia rieši

```text
D_M(h;dN)-D_M_target(dN)=0.
```

### 5.3 Legacy rast a `S8`

Od `x0=-ln(1001)` po `0`:

```text
d' = -Theta
Theta' = -(2+d ln E/dx)*Theta - (3/2)*(M/E^2)*d
d(x0)=exp(x0)
Theta(x0)=-d(x0).
```

Rovnaká diskrétna RK schéma ako v skripte 09 sa použije na všetkých troch
grid leveloch; výsledok musí konvergovať s gridom.

Referenčný rast `D_LCDM` sa vypočíta tou istou implementáciou pri
`lambda=0`, `delta=0`, `Delta N_eff=0`. Pre každý modelový bod:

```text
sigma8 = 0.811 * D_model/D_LCDM
S8 = sigma8*sqrt(Omega_m0/0.3).
```

## 6. Predregistrované guardy

### 6.1 Povinné technické a numerické PASS

1. všetky vstupy a výstupy sú konečné native JSON scalars;
2. `omega_L>0`, `F,M,R,E^2>0` na celej použitej dráhe;
3. nulový počet floor/clip aktivácií;
4. root residual má na koncoch `[0.55,0.80]` opačné znamienka;
5. inner matter fixed-point relative residual `<=1e-10`, max `40` iterácií;
6. outer bisection bracket width `<=5e-10`, max `40` iterácií;
7. relative angular residual `abs(theta_model/theta_ref-1)<=1e-8`;
8. relatívna chyba každej adaptívnej kvadratúry `<=1e-8`;
9. pre každý bod `abs(H0_n8000-H0_n4000)<=0.005 km/s/Mpc`;
10. pre každý bod `abs(S8_n8000-S8_n4000)<=0.0005`;
11. high-grid full-steam comparator
    `abs(H0-66.37)<=0.05 km/s/Mpc` a `abs(S8-0.8745)<=0.002`;
12. všetky tri body používajú identické vstupy okrem `Delta N_eff`.

Coarse→medium rozdiel aj konvergenčný pomer sa reportujú, ale nemajú
samostatný PASS prah. Ak high→medium prah zlyhá, výsledok je
`REVIEW_NUMERICAL_CONVERGENCE`, nie fyzikálny STOP.

### 6.2 Rozhodovacie vetvy

- `PASS_THREE_POINT_LEGACY_SENSITIVITY`: všetky guardy 1–12 prešli;
- `REVIEW_NUMERICAL_CONVERGENCE`: kompletný raw, ale grid/rezíduum/comparator
  je mimo prahu;
- `REVIEW_INVALID_BACKGROUND_OR_ROOT`: positivity alebo sign-change zlyhá;
- technický crash/timeout/schema/publish failure: žiadny vedecký výsledok.

Platí `NO_SIGN_GATE`: monotónnosť ani znamienko zmeny `H0`/`S8` nie sú PASS
kritériom a nesmú sa po výsledku dodatočne zaviesť.

### 6.3 Materialita verejného riadku

```text
H0 material at one-decimal display precision
  iff abs(H0_full-H0_null) >= 0.05 km/s/Mpc
S8 material at two-decimal display precision
  iff abs(S8_full-S8_null) >= 0.005
```

Táto klasifikácia neznamená observačnú štatistickú významnosť.

## 7. DEV, RC a official output contract

Pracovné cesty:

```text
scripts/baseScripts/release_v318_h0_s8_legacy_sensitivity_dev.py
scripts/393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py
```

Official cieľ po RC freeze:

```text
scripts/results/release_v318_h0_s8/
RUN_V318_PT1_H0_S8_THREE_POINT_LEGACY_SENSITIVITY.json
```

DEV smie vykonať iba `py_compile`, `--help` a offline synthetic `--self-test`.
Self-test nesmie použiť zmrazené vedecké tri body ani official output.

RC freeze zaznamená exact contract/base/runner hashe, absent-output guard a
official príkaz. Official proces bude mať interný limit najviac `45 s` a
vonkajší limit najviac `60 s`; ak benchmark ukáže, že tri gridy nemožno
bezpečne dokončiť, contract sa pred RC freeze rozdelí po bodoch, nie predĺži
na neobmedzený proces.

Publish je exclusive do neprítomného cieľa cez vlastný temp súbor a cleanup
`finally`. Kolízia, partial payload alebo failure nesmie prepísať official
cieľ.

## 8. Implementačný handoff kapsul

```text
TASK_ID: V318-PT1-H0-S8-C1-DEV-20260730
ROLE: main_orchestrator_as_DEV_source_author
ROLE_CONFIG_SHA256: NOT_APPLICABLE_ROOT_ORCHESTRATOR
ASSIGNED_AGENT_TASK_ID: /root
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/h0_s8_math_auditor
INTERNAL_AUDITOR_TASK_ID: /root/h0_s8_physics_auditor
PACKAGE_CURATOR_TASK_ID: NONE
EXTERNAL_AUDITOR_TASK_ID: NONE
SEPARATION_OF_DUTIES_CHECK: PASS(/root != /root/h0_s8_math_auditor; /root != /root/h0_s8_physics_auditor; package roles NONE). The configured python_script_author could not start because its gpt-5.6 model is unavailable to this ChatGPT account; no candidate or process existed at failure.
ROUTE: RELEASE/v3.18/PT1_H0/C1
CURRENT_PHASE: DEV_SANDBOX_SOURCE_AUTHORING
ALLOWED_NEXT_ACTION: implement the exact contract in the two allowlisted working Python files; do not run Python.
ALLOWED_READS: mandatory bootstrap; this contract; exact script09/script17 and lineage inputs; phase-appropriate DNR/known-pattern/runtime/base registers.
ALLOWED_WRITES: scripts/baseScripts/release_v318_h0_s8_legacy_sensitivity_dev.py; scripts/393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py
FORBIDDEN_ACTIONS: no Python process; no official data/output; no network; no edit to contract, route/current plans, registers, results, audits, theory, or unrelated files; no verdict.
IMMUTABLE_INPUT_PATHS_AND_SHA256: script09=349C209EBEC4E8F56D2E9BB47DC2A0349DD4FA8FA4FB517916C537540EFA6008; script17=36094FD6FAE4D8A3D9D43B2172C28582AFC2B5ADF29D68C18372F9CE8A976998; lineage_audit=80AB8AB1E094CE6D224B9BFE46016373A26E1DE71373C2F63977218B2904AFA4
PREREG_SHA256: PENDING_CONTRACT_FREEZE
RUN_AUTHORIZED: false
OUTPUT_PATHS: exactly the two ALLOWED_WRITES paths
ERROR_BATCH_INDEX: 1
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 0
FINDING_ID: NONE
FINDING_CLASS: NONE
EARLIEST_INVALID_CHECKPOINT_ID: NONE
INVALIDATED_DESCENDANT_CHECKPOINT_IDS: NONE
TRACK_IDENTITY_GATE: NOT_APPLICABLE_RELEASE_DIAGNOSTIC
CHECKPOINT_ID: NOT_CREATED_PRE_OFFICIAL
PARENT_CHECKPOINT_IDS: NONE
CANONICAL_PACKAGE_ID: NONE
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: both working files implement the exact equations, guards, synthetic self-test, internal deadline, native JSON and exclusive publish; no process executed; exact changed paths and hashes returned.
NEXT_ROLE: main orchestrator DEV executor, then math_script_auditor after DEV PASS and RC freeze
```

## 9. Stav pri vytvorení contractu

```text
RUN_AUTHORIZED=false
PYTHON_PROCESSES=0
OFFICIAL_OUTPUT=ABSENT_NOT_YET_CHECKED_FOR_RC
ERROR_BATCH_INDEX=1
ERRORS_USED_IN_CURRENT_BATCH=0/10
CUMULATIVE_TECHNICAL_ERRORS=0
```
