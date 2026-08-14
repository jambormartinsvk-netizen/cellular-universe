# EA-042 — B6b constraint-first mapa rodín mechanizmov

**Stav:** `SEALED_READY_FOR_AUDIT`  
**Target tier:** `T1_PRIMARY_FORMULA / FAMILY_MAP_AND_FALSIFICATION_AUDIT_ONLY`  
**Autorita:** živý dokument 245; externý auditor iba odporúča  
**Autor teórie:** Martin Jambor  
**Formalizácia a procesný orchestrátor:** Codex (OpenAI)  
**PACKAGE_CURATOR_TASK_ID:** `/root`  
**EXTERNAL_AUDITOR_TASK_ID:** `/root/ea042_external_auditor`  
**PHYSICS_REVIEWER_TASK_ID:** `/root/external_audit_ea036`  
**SEPARATION_OF_DUTIES_CHECK:** `PASS(curator != external auditor)`  
**AUDITOR_ROLE_CONFIG_SHA256:** `6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14`  
**PACKAGE_CURATOR_ROLE_CONFIG_SHA256:** `26CAB7693DBB372C4FAEEFBACF9101CD2C1BA3F40E628CB20E6514EA8A906AE1`  
**PACKAGE_CURATOR_CONFIG_BINDING:** `REFERENCE_ONLY_MAIN_ORCHESTRATOR_CURATOR_AFTER_THREE_INCOMPLETE_AGENT_HANDOFFS`  
**RUN_AUTHORIZED:** `false`  
**LIVE_SCIENTIFIC_ARTIFACTS:** `1`  
**LIVE_CENTRAL_REGISTERS_UPDATED:** `4`  
**LIVE_FILES_CHANGED_TOTAL:** `5`  
**AUDIT_PACKAGE_COPIES:** `14` evidence + `7` controls = `21`; response `1`; spolu `22 < 40`.

## AUDITOR_RULESET_PATHS_AND_SHA256

```text
EVIDENCE/010__AGENTS.md=BD64D6AC1C583194A67B3ABC5423467AF3F5F292F0293AF68F02AA3BBC503EE5
EVIDENCE/011__PROJECT_OPERATING_SYSTEM.md=F4F0C3610CBE5BDF05DEC7EE606534682222DBF959F439686CF89FA7B0F7E543
EVIDENCE/012__AUDITOR_PACKAGE_PROTOCOL_R6.md=4330FFD3D22C27CC60A3693E9B4694B601903FC6490A4DB7F56B56B1C4FD5272
EVIDENCE/013__EXTERNAL_AUDITOR_ROLE.toml=6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14
EVIDENCE/014__AGENT_ROLE_MANIFEST.md=76921D8F2FA0FB02C70F511AFB4396C4148F052938DA21C33B91D1594C20061E
```

## Scope markery

```text
B6_C0=PASS_B6_C0_TOPOLOGY
B6A_PH1=PASS_B6A_PH1_CONDITIONAL_MANTLE
B6B=PASS_B6B_FAMILY_MAP_INTERNAL
MF1_DIVISION_LOCKED=OPEN_FAMILY
MF2_INTERNAL_CLOCK=OPEN_FAMILY
MF3_STATE_SWITCHED_HYBRID=OPEN_FAMILY
MF4_PARALLEL_CONSERVATIVE_CHANNELS=OPEN_FAMILY
PH1=MF2_CONDITIONAL_CANDIDATE_ONLY
ONE_WINDING_GATE=SUPERSEDED_AS_SOLE_NEXT_ACTION
S8=INDEPENDENT_HOLDOUT_NOT_CONSTRUCTOR
D03=PARTIAL_AUTHOR_INPUT
D04_D11=BLOCKED
K4=60/100_UNCHANGED
P5=3.5/6_UNCHANGED
NO_RUNTIME
NO_PYTHON
NO_COMPUTED_VERDICT
```

## Presná otázka

1. Pokrývajú MF1 až MF4 bez skrytého preferovania základné možnosti:
   viazanie na delenie, samostatný vnútorný clock, lokálny stavový switch a
   súbežné konzervatívne kanály?
2. Sú rodiny rozlíšené tak, aby sa rovnaká udalosť, bunka alebo energia
   nezapočítala dvakrát a aby MF3/MF4 zachovali všetky `Q_A^mu` a momenty?
3. Je správne, že nenájdenie svedka dáva `REVIEW/UNRESOLVED`, kým scoped
   `F_D=empty` vyžaduje univerzálny argument pokrývajúci všetky rodiny?
4. Je PH1 korektne zachovaný iba ako podmienený MF2 kandidát bez rozhodnutia
   `one winding = one event`?
5. Je S8 správne použitý až ako holdout: B6b-2 zmrazí passport a uzavrie
   perturbation moments, B6b-3 vykoná forward predikciu a porovnanie?
6. Je B6b-1 analytická background/source-moment obálka všetkých štyroch
   rodín správny najmenší ďalší krok pred detailnou mikrofyzikou?

## Poradie čítania

1. `EVIDENCE/001` — primárny dokument, najmä oddiel 8.15;
2. `EVIDENCE/004` a `005` — constraint-to-function výsledky a M0–M10;
3. `EVIDENCE/006` a `007` — momentový/support kontrakt a metodika;
4. `EVIDENCE/002` a `003` — filozofia a A2/A7/A12/A15 lineage;
5. `EVIDENCE/008` — autoritatívny stav a ďalší krok;
6. `EVIDENCE/009` — formula-provenance checklist;
7. manifest, runtime mapa a bootstrap `EVIDENCE/010` až `014`.

## Predregistrované hodnotenie externého posudku

- `AGREE_IN_SCOPE`: rodiny, konzervácia, falsifikácia, PH1 a S8 workflow sú
  v deklarovanom T1 scope úplné a férové;
- `AGREE_WITH_LIMITATION`: jadro sedí, ale chýba presne pomenovaná rodina,
  invariant, conservation podmienka alebo scope korekcia;
- `DISAGREE_IN_SCOPE`: materiálny family-map, double-count, hidden-fit alebo
  falsification defect;
- `CANNOT_AUDIT`: chýba primárna formula, pravidlo alebo source lineage.

## Nonclaims

Balík nevyberá ani nedokazuje konkrétnu rodinu. Neobsahuje numerický S8
passport, predikciu, runner, raw výsledok, generated JSON ani T2 runtime.
`PASS_B6B_FAMILY_MAP` je interný scoped stav mapy, nie dôkaz pravdivosti
teórie. D03 zostáva partial, D04–D11 blokované, K4 `60/100`, P5 `3.5/6` a
P5.4/G8/G9/Python sú blokované.

## Autorita a oddelenie rolí

Externý auditor je odlišný od kurátora a interného fyzikálneho reviewera.
Posudok nemení projektový `PASS/REVIEW/STOP`; autoritatívne ho spracuje iba
hlavný orchestrátor.
