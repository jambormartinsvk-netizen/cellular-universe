# B6b-2.11 — C01-RW1 lokálny väzbovo-rozhraniový carrier: analytický contract

**Task:** `A2K4-B6B2-11-H-RDIV-C01-RW1-ZREC-LINK-INTERFACE-CONTRACT-20260729-410`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.11`  
**Autor fyzikálneho vstupu:** Martin Jambor  
**Formalizácia:** OpenAI Codex, hlavný orchestrátor  
**Stav:** `CONTRACT_DRAFT / AUTHOR_INPUT_RECORDED / NO_RUN / NO_PYTHON`  
**Rodičovská koľaj:** `C01-RW1 LIVE / NO_PHYSICAL_WITNESS`

## 1. Autorovo rozhodnutie

Martin Jambor 2026-07-29 výslovne schválil:

```text
Z_rec = lokálna konfigurácia väzieb a pripravovaného rozhrania.
```

Tým sa uzatvára iba identita fyzického carriera v kroku `W2`. Nevyberá sa
energia jednej väzby, interface tension, geometria dokončenia, `P_rec`,
`W_*`, `u_cell`, `dmu_cell` ani reset. Schválenie nie je fyzikálny witness,
PASS/STOP, official run ani povolenie Pythonu.

## 2. Presný typ carriera a identita koľaje

Kanonický lokálny pre-event carrier jednej parent bunky zapisujeme

```text
Z_rec := [B_rec, Sigma_prep]_rel,
```

kde:

- `B_rec` je lokálna konfigurácia väzieb na causal supporte parent bunky;
- `Sigma_prep` je lokálny stav pripravovaného, ešte nedokončeného nového
  rozhrania;
- hranaté zátvorky `_rel` znamenajú triedu fyzicky ekvivalentných
  reprezentácií po prelabelovaní buniek/väzieb a po dovolených lokálnych
  súradnicových zmenách.

`B_rec` a `Sigma_prep` sú dve zložky jedného coupled carriera, nie dva
nezávislé eventové mechanizmy. C02 sa quotientuje do C01 presne vtedy, ak je
jej bond-completion coordinate iba monotónnou stavovou reparametrizáciou
toho istého `W[Z_rec]` a nemení crossing prediction.

Carrier musí byť lokálny Markovský state record: dve fyzicky identické
hodnoty `Z_rec` nesmú niesť rozdielny work credit iba pre rozdielnu
nepozorovateľnú históriu. Čistý integrátor času alebo prichádzajúcej dávky
bez fyzickej zmeny `B_rec` alebo `Sigma_prep` je zakázaný hidden clock.

## 3. Stavový work functional, ktorý treba odvodiť

Hľadaný lokálny skalár musí mať tvar

```text
W_rec[Z_rec; Z_birth]
  = E_rec[Z_rec] - E_rec[Z_birth],
[W_rec] = E,
W_rec(Z_birth) = 0,
D_u W_rec = P_rec >= 0
```

na admissible pre-event prípravnej vetve. `E_rec` je zatiaľ neodvodený
lokálny väzbovo-rozhraniový energy/work functional; tento contract ho
nenahrádza voľnou Planckovou škálou. Jeho odvodenie smie používať iba
fyziku tej istej lokálnej konfigurácie, napríklad fyzicky odvodenú väzbovú
prácu a interface contribution, ale každá zložka musí mať source lineage,
units a disjunktné conservation účtovanie.

`W_rec` je work credit už realizovaný alebo nevratne zaviazaný v
`Z_rec`. Nie je ďalší energy stock. Nesmie sa preto druhýkrát pripočítať k
rezervoáru ani k interface energii.

## 4. Zvyšné odvodenia D1–D6

| ID | Analytický blok | DONE_WHEN |
|---|---|---|
| `D1` | carrier/state mapa | je explicitné, ktoré lokálne bond a interface premenné určujú `Z_rec`, ich ekvivalencie a reachable pre-event doménu |
| `D2` | energy/work functional | z prijatej lokálnej fyziky sa odvodí `E_rec[Z]`, znamienka a jednotka energie bez použitia `delta`, `C=28`, `H0`, `S8` alebo času ako energy scale |
| `D3` | výkon a conservation | `P_rec=D_uW_rec` sa rozloží na disjunktné causal current/stress-work kanály a uzavrie sa lokálny reservoir/flux ledger bez double countu |
| `D4` | completion prah | lokálna množina dokončených interface stavov určí kladné konečné cycle-frozen `W_*`; prah sa nefitne podľa event rate ani observables |
| `D5` | cell measure a reset | odvodia sa `u_cell`, regular congruence, invariantná lokálne konečná `dmu_cell` a `R_reset^Z` s nulovým dcérskym work creditom a oddelenou residual energiou |
| `D6` | integrovaný witness | jeden explicitný reachable pre-event stav prejde `W0–W12` z dokumentu 259 a regular first passage z dokumentu 254 |

Analytické poradie je `D1 -> D2 -> D3 -> D4 -> D5 -> D6`. Neúspech jedného
ansatzu je scoped výsledok alebo presný `WAITING_FOR`, nie fyzikálny STOP
celej C01 koľaje.

## 5. Zmrazené hranice

Počas tohto atómu platí:

```text
chi_div = W_rec / W_*,
chi_c = 1,
W_* > 0 a počas parent cyklu je frozen,
event = prvý jednoduchý transverzálny upward crossing,
source-off bez dostupného rezervoára => P_rec = 0,
parent sa vyradí a dcéry dostanú nové ID,
W_rec,daughter = 0.
```

Zakázané je odvodiť `E_rec`, `P_rec` alebo `W_*` z `R_div`, `Q_D`, už
realizovaného eventu, produktov, makroskopickej expanzie, `Theta_cell`,
`a`, `H0`, Fourierovho `k`, `S8`, biologického targetu, samotnej dimenzie
alebo z bezrozmerných `delta` a `C=28`.

## 6. Rozhodovacie vetvy

```text
Ak D1-D6 dajú explicitný lokálny konzervatívny prvok A_RW1:
  CANDIDATE_PHYSICAL_RW1_WITNESS_FOUND_PENDING_INDEPENDENT_AUDIT.

Ak carrier ostáva definovaný, ale accepted equations neurčia energy/work
functional, prah, measure alebo reset:
  LIVE / WAITING_FOR_EXACT_MISSING_PHYSICAL_DERIVATION;
  nie STOP ani closure.

Ak konkrétny functional potrebuje hidden timer, energiu zadarmo, double
credit, fitted threshold alebo post-event príčinu:
  PRECHECK_EXCLUDED_SCOPE iba pre tento functional.

Ak by oprava vyžadovala zmenu carriera, stavového priestoru, interaction
topology, causal graph alebo bunkovej ontológie:
  TRACK_IDENTITY_GATE / MARTIN_DECISION pred ďalším výpočtom.
```

## 7. Fázový a technický stav

```text
CURRENT_PHASE: CONTRACT_DRAFT_AUTHOR_INPUT_RECORDED
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 6_RETAINED_PROJECT_HISTORY
P4_PHYSICAL_WITNESS_ATTEMPTS_CONSUMED_BY_THIS_CONTRACT: 0
```

Bežná budúca technická chyba dostane iba compact route-local error row a
regresný test; nevytvorí nový contract, auditný dokument ani successor
suffix. Tento analytický contract sám nič nespúšťa.

## 8. Nezávislý auditný handoff

```text
TASK_ID: A2K4-B6B2-11-H-RDIV-C01-RW1-ZREC-LINK-INTERFACE-CONTRACT-AUDIT-20260729-411
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: VERIFY_AGAINST_CURRENT_MANIFEST_BEFORE_AUDIT
ASSIGNED_AGENT_TASK_ID: NOT_ASSIGNED_UNTIL_EXTERNAL_SHA_FREEZE
ARTIFACT_AUTHOR_TASK_ID: /root task410
STATIC_AUDITOR_TASK_ID: NOT_ASSIGNED_UNTIL_EXTERNAL_SHA_FREEZE
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_UNTIL_ANALYTIC_RESULT
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED
SEPARATION_OF_DUTIES_CHECK: REQUIRED_author_root_neq_static_auditor
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.11_C01_RW1_ZREC_LINK_INTERFACE
CURRENT_PHASE: CONTRACT_DRAFT_AWAITING_HASH_FREEZE_AND_INDEPENDENT_STATIC_MATH_LOGIC_AUDIT
ALLOWED_NEXT_ACTION: main orchestrator records exact document293 SHA outside this file; then an independent auditor checks exact frozen bytes, equations, units, locality, quotient rule, hidden-clock guard, conservation reach and track identity
ALLOWED_READS: mandatory bootstrap; exact documents245_254_256_259_260_293; theory main A1-A3; event-ledger task409-410; current role config and manifest
ALLOWED_WRITES: none by auditor; advisory response only
FORBIDDEN_ACTIONS: edit document293; choose unapproved link energy_interface tension_completion geometry_threshold_measure_or reset; Python_network_project-code_or official run; physical PASS_STOP_score_depth_or checkpoint package
IMMUTABLE_INPUT_PATHS_AND_SHA256: theory_main=01B8DD903C3BB97B30E29E2C1E2E2B280D3968EDD0679C610E84A78CC55CBF43; document245=AF289165385801F019454F2CAFF41EFEB25D0A3E2444FA73EAF6B6EBF4E901CB; document254=9AF71F8289D6D5D1072439BF322F261480C76A3AACC8F3A55FCDE10BE9C02B99; document256=3BA221F3D88C90EC961F4B48835C046E5C2DA287DFB0130BC81E99034F8F9975; document259=9766E5223C7AB95B8D3D3B9914BF8B02034F160F84EF0E47BEE8E4C14EB453E2; document260=91C25DD777FB9A10B1157F3CF729408B55A3CA264A03E29AA9C2F9E6747CA774
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit recommendation; no project output
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 6
FINDING_ID: NONE_OPEN
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CANDIDATE_PENDING_AUDIT
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_AS_SOURCE_ELIGIBILITY_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE_INTERNAL_PHASE
DONE_WHEN: exact frozen contract preserves the author-selected carrier without inventing its energy scale; D1-D6 are sufficient and noncircular; next analytic step is uniquely D1-D2 with no compute authorization
NEXT_ROLE: math_script_auditor
```

## 9. Nonclaims a súborový rozpočet

- carrier selection nepreukazuje neprázdnosť `A_RW1`;
- nie sú odvodené `P_rec`, `W_*`, conservation, cell measure ani reset;
- C01-RW1, P5 a A2-K4 ostávajú `LIVE`, nie `CLOSED`;
- skóre `K4=60/100` a `P5=3.5/6` sa nemení;
- nevzniká raw, výsledok, checkpoint ani externý balík.

```text
LIVE_SCIENTIFIC_ARTIFACTS: 1 contract
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
