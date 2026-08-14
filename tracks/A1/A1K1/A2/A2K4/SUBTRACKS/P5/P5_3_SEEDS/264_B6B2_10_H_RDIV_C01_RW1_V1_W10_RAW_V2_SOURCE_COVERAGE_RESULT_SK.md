# B6b-2.10 — H_RDIV-C01-RW1-v1 W10 raw-v2 source-coverage výsledok

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-W10-RAW-V2-SOURCE-RESULT-20260727-169`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Analytické vykonanie a source ledger:** Codex, hlavný orchestrátor  
**Stav:** `RESULT_CANDIDATE / REVIEW_SEARCH_COVERAGE_INCOMPLETE_NO_PHYSICAL_INFERENCE / NO_RUN / NO_PYTHON`

## 1. Frozen vstup a immutable evidencia

- frozen source protocol 261 SHA-256:
  `FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B`;
- frozen raw-v2 transport protocol 263 SHA-256:
  `8CC33C71C2C7479399741EF5F8B0019645210555F8AB59BE9AB468C75CC95AF3`;
- event ledger through task168 SHA-256:
  `D99DC66F8EF988642F48B8B13C1FC6C952A8EE243B27C999B770E2CE31898055`;
- Q1 receipt 263A SHA-256:
  `0C4FBC6F868DAE86C7ED8FA81195E9400918C5F8F8350BDFC7A0DDE8A74132E7`;
- Q2 receipt 263B SHA-256:
  `45BF5A2BE5F767EF90C7C4BB3D7FF0EB3D737AAADCB7A8D3467A8947F3124145`;
- Q3 receipt 263C SHA-256:
  `823E5FE8F8DE5D937EC0AE7E39EB86917D2BBD3A6F22F903B83DDD30C03648B1`;
- Q4 receipt 263D SHA-256:
  `BB41A43ED0B6ADF174FE9164C1D4A9F65B049C4965262028E8C49B19E5B7B3DE`.

Task167 overil oddelenie Q1–Q4, exact query/payload, hashe a provider namespaces.
Task168 prijal iba zdokumentovanú framing odchýlku terminálneho
`END_EXACT_TOOL_RETURN`; receipts sa neupravili a dotazy sa neopakovali.

## 2. Vykonanie frozen searchu

Presne vykonané:

```text
search_query calls: 4
query order: Q1 -> Q2 -> Q3 -> Q4
multi-query / extra query / rewrite / pagination: 0
raw hits: Q1=39, Q2=28, Q3=26, Q4=26, total=119
historical source open calls after integrity gate: 9_MAIN_ATTESTED_NOT_TRANSCRIPT_VERIFIED
historical source click calls after integrity gate: 2_MAIN_ATTESTED_NOT_TRANSCRIPT_VERIFIED
audit-closure persisted exact-target replay opens: 6_COMPLETED
audit-closure replay results: E1 Q1R1 arXiv SUCCESS; E2 Q1R3 Monash CACHE_MISS;
  E3 Q1R3 DOI UNSAFE_TO_OPEN; E4 Q1R3 IOP article CACHE_MISS;
  E5 Q1R3 IOP PDF UNSAFE_TO_OPEN; E6 existing Q1R3 Monash view SUCCESS
Python processes: 0
```

Historické open/click počty sú iba zachovaný main-attested procesný záznam a
nenesú coverage záver. Auditovateľné task171+173 replay tvorí šesť presných
open volaní uložených v Appendix A; neobsahuje nové search query. Žiadny
neskorší hit nebol fyzikálne vybraný.

## 3. Prvý F-A screening a skorý coverage blocker

### Q1 rank 1

[General relativistic bubble growth in cosmological phase transitions](https://arxiv.org/abs/2307.12080)
je pôvodný research paper a bol dostupný. Samotný zdroj však pracuje v limite
phase boundary zanedbateľnej šírky a dodáva self-similar GR fluid growth, nie
požadovaný finite-width local scalar/interface action s odvodeným critical
interface barrierom. Preto ide o
`PRIMARY_OUTSIDE_F_A_REQUIRED_INTERFACE_ACTION`, nie eligible F-A anchor.
Nevykonal sa S0–S13 passport screen.

### Q1 rank 2

[Gravitational waves from a first-order electroweak phase transition: a brief review](https://pmc.ncbi.nlm.nih.gov/articles/PMC5784032/)
je explicitne review, preto `SECONDARY_EXCLUDED`.

### Q1 rank 3 a duplicate rank 4

[Model-dependent analysis method for energy budget of the cosmological first-order phase transition](https://research.monash.edu/en/publications/model-dependent-analysis-method-for-energy-budget-of-the-cosmolog/)
je pôvodný peer-reviewed research článok, DOI
[10.1088/1475-7516/2023/07/006](https://doi.org/10.1088/1475-7516/2023/07/006).
Dostupné metadata a abstrakt explicitne uvádzajú local scalar-field EOM s
fenomenologickým trením, fluid boundary conditions, wall contribution do
energy-momentum tensoru a energy-budget výpočet. Preto je to prvý
`ELIGIBLE_PRIMARY` F-A kandidát v zmrazenom poradí.

Plné action/EOM/energy rovnice však neboli verifikovateľne dostupné cez
canonical DOI, IOP article/PDF ani bibliografickú alternatívu. Nemožno teda
overiť one-model parity, znamienka, `D_u W=P>=0`, barrier, conservation
channels, source-native worldtube/measure, regular crossing ani dynamický
daughter reset. Rank 4 je navigačný duplicate toho istého titulu a
normalizovanej URL; raw URL sa líši iba terminálnym `/`.

Frozen pravidlo 261.3.8 prikazuje pri skoršom inaccessible eligible zdroji
zastaviť. Rank 3 sa preto nesmie preskočiť v prospech neskoršieho kandidáta.

Audit-closure replay E3–E5 presne zachytáva zlyhanie DOI a oboch canonical
IOP cieľov. E6 úspešne a immutable viaže Q1R3 titul, autorov a research
metadata na DOI `10.1088/1475-7516/2023/07/006`. Raw search receipt dodáva
Q1R3 titul/autorov/abstrakt a E6 dodáva bibliografiu/DOI, ale ani jeden
nedodáva canonical author-preprint link; ďalšie search query na jeho
dohľadanie frozen protokol nepovoľuje.

## 4. Úplný ordered hit ledger

Status každého provider hitu je nižšie samostatne. Global rank je mechanický
concatenation Q1, Q2, Q3, Q4; family order je Q1+Q2 pre F-A, potom Q3/F-B a
Q4/F-C. `NOT_REACHED` nie je vedecké vylúčenie zdroja.

| Global | Family | Query | Query rank | Bibliografická identita | Status | Open status |
|---:|---|---|---:|---|---|---|
| 1 | F-A | Q1 | 1 | [General relativistic bubble growth in cosmological phase transitions](https://arxiv.org/abs/2307.12080) | PRIMARY_OUTSIDE_F_A_REQUIRED_INTERFACE_ACTION | OPENED_ABSTRACT; finite-width interface/action/barrier absent |
| 2 | F-A | Q1 | 2 | [Gravitational waves from a first-order electroweak phase transition: a brief review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5784032/) | SECONDARY_EXCLUDED | NOT_OPENED; explicit review |
| 3 | F-A | Q1 | 3 | [Model-dependent analysis method for energy budget of the cosmological first-order phase transition - Monash University](https://research.monash.edu/en/publications/model-dependent-analysis-method-for-energy-budget-of-the-cosmolog/) | ELIGIBLE_PRIMARY / INACCESSIBLE_EXACT_EQUATIONS | OPENED_METADATA+ABSTRACT; canonical DOI/publisher/preprint equations unavailable |
| 4 | F-A | Q1 | 4 | [Model-dependent analysis method for energy budget of the cosmological first-order phase transition - Monash University](https://research.monash.edu/en/publications/model-dependent-analysis-method-for-energy-budget-of-the-cosmolog) | DUPLICATE_OF_Q1_R3 | NOT_OPENED_SEPARATELY |
| 5 | F-A | Q1 | 5 | [Gravitional radiation from first-order phase transitions in the presence of a fluid](https://arxiv.org/abs/1405.4005) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 6 | F-A | Q1 | 6 | [First principles determination of bubble wall velocity](https://arxiv.org/abs/2204.13120) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 7 | F-A | Q1 | 7 | [Hydrodynamics of ultra-relativistic bubble walls - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0550321316000535) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 8 | F-A | Q1 | 8 | [Energy Budget of Cosmological First-order Phase Transitions](https://arxiv.org/abs/1004.4187) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 9 | F-A | Q1 | 9 | [Relativistic bubble collisions - a closer look - Weizmann Institute of Science](https://weizmann.elsevierpure.com/en/publications/relativistic-bubble-collisions-a-closer-look/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 10 | F-A | Q1 | 10 | [Evaporation of a Bubble Created by the Cosmological First-Order Phase Transition \| Progress of Theoretical Physics \| Oxford Academic](https://academic.oup.com/ptp/article/68/4/1157/1901192) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 11 | F-A | Q1 | 11 | [General relativistic bubble growth in cosmological phase transitions](https://sussex.figshare.com/articles/journal_contribution/General_relativistic_bubble_growth_in_cosmological_phase_transitions/28749791) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 12 | F-A | Q1 | 12 | [First principles determination of bubble wall velocity](https://repo.scoap3.org/records/71125/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 13 | F-A | Q1 | 13 | [Ultra-relativistic bubbles from the simplest Higgs portal and their cosmological consequences \| Journal of High Energy Physics \| Springer Nature Link](https://doi.org/10.1007/JHEP10%282022%29017) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 14 | F-A | Q1 | 14 | [Gravitational waves from bubble collisions and fluid motion in strongly supercooled phase transitions \| The European Physical Journal C \| Springer Nature Link](https://link.springer.com/article/10.1140/epjc/s10052-023-11241-3) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 15 | F-A | Q1 | 15 | [Field-theoretic derivation of bubble-wall force](https://ouci.dntb.gov.ua/en/works/9Zv2zxz9/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 16 | F-A | Q1 | 16 | [Bubble correlation in first-order phase transitions](https://iris.uniroma1.it/handle/11573/1643222) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 17 | F-A | Q1 | 17 | [PHYSICAL REVIEW D](https://electronicsandbooks.com/edt/manual/Magazine/P/Physical%20Review%20D/PhysRevD%201982-1994/root/data/PhysRevD%201982-1994/pdf/PRD/v49/i6/PRD_v49_i06_p2837_1.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 18 | F-A | Q1 | 18 | [https://helda.helsinki.fi](https://helda.helsinki.fi/server/api/core/bitstreams/1f873c08-3651-4053-9fa1-5f68f413ddb3/content) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 19 | F-A | Q1 | 19 | [HYDRODYNAMICS OF BUBBLES IN A FIRST-ORDER ELECTROWEAK PHASE TRANSITION](https://repositorio.ufmg.br/server/api/core/bitstreams/14b52bd5-b11b-484e-8079-c239d8ba90de/content) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 20 | F-A | Q1 | 20 | [KCL-PH-TH/2020-04](https://cds.cern.ch/record/2713263/files/2003.07360.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 21 | F-A | Q1 | 21 | [CERN-TH-2024-065](https://cds.cern.ch/record/2900016/files/2406.02359.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 22 | F-A | Q1 | 22 | [THE UNIVERSITY OF CHICAGO](https://knowledge.uchicago.edu/record/12424/files/Ireland_uchicago_0330D_17481.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 23 | F-A | Q1 | 23 | [Cosmological phase transition](https://en.wikipedia.org/wiki/Cosmological_phase_transition) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 24 | F-A | Q1 | 24 | [First law of thermodynamics (fluid mechanics)](https://en.wikipedia.org/wiki/First_law_of_thermodynamics_%28fluid_mechanics%29) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 25 | F-A | Q1 | 25 | [Phase-Coherent Vacuum and Emergent Gravity](https://www.reddit.com/r/LLM_supported_Physics/comments/1rqu4vq/phasecoherent_vacuum_and_emergent_gravity/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 26 | F-A | Q1 | 26 | [Tolman–Oppenheimer–Volkoff equation](https://en.wikipedia.org/wiki/Tolman%E2%80%93Oppenheimer%E2%80%93Volkoff_equation) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 27 | F-A | Q1 | 27 | [Kibble–Zurek mechanism](https://en.wikipedia.org/wiki/Kibble%E2%80%93Zurek_mechanism) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 28 | F-A | Q1 | 28 | [Four-gradient](https://en.wikipedia.org/wiki/Four-gradient) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 29 | F-A | Q1 | 29 | [Maxwell construction](https://en.wikipedia.org/wiki/Maxwell_construction) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 30 | F-A | Q1 | 30 | [[Removed]](https://www.reddit.com/r/LLMPhysics/comments/1sxlqo7/removed/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 31 | F-A | Q1 | 31 | [[Removed]](https://www.reddit.com/r/HypotheticalPhysics/comments/1uz6ghz/removed/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 32 | F-A | Q1 | 32 | [When looking at the growth of primordial density fluctuations, why can we treat them as a “cosmological fluid”?](https://www.reddit.com/r/AskPhysics/comments/1cr3nsl) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 33 | F-A | Q1 | 33 | [Noether's Theorem and the Stress Energy Tensor](https://www.reddit.com/r/Physics/comments/v4qyln) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 34 | F-A | Q1 | 34 | [Scrutinise this please](https://www.reddit.com/r/u_Little-Event-9796/comments/1qnrc11/scrutinise_this_please/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 35 | F-A | Q1 | 35 | [What do you mean by "Mass of Scalar Field"?](https://www.reddit.com/r/cosmology/comments/1cojxt1) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 36 | F-A | Q1 | 36 | [On the initial regime of pre-big bang cosmology By: Maurizio Gasperini](https://www.reddit.com/r/cosmology/comments/fha8zm) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 37 | F-A | Q1 | 37 | [Relativistic fluid dynamics project?](https://www.reddit.com/r/AskPhysics/comments/rc098g) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 38 | F-A | Q1 | 38 | [A confusion about spacetime evolution in general relativity, Einstein's field equation.](https://www.reddit.com/r/AskPhysics/comments/1cm3p3q) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 39 | F-A | Q1 | 39 | [I'm probably a fool but here you go: some ideas on Navier-Stokes](https://www.reddit.com/r/FluidMechanics/comments/1ftyyp8) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 40 | F-A | Q2 | 1 | [Surface tension of cavitation bubbles - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10104516/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 41 | F-A | Q2 | 2 | [Gas evolution rates – A critical uncertainty in challenged gas-liquid separations - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0920410516305708) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 42 | F-A | Q2 | 3 | [Gravitational waves from bubble collisions and fluid motion in strongly supercooled phase transitions \| The European Physical Journal C \| Springer Nature Link](https://link.springer.com/article/10.1140/epjc/s10052-023-11241-3) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 43 | F-A | Q2 | 4 | [Matter sourced bubble nucleation in the asymmetron scalar-tensor theory \| Phys. Rev. D](https://journals.aps.org/prd/abstract/10.1103/z9gn-q74p) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 44 | F-A | Q2 | 5 | [Generalized surface tension bounds in vacuum decay \| Phys. Rev. D](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.97.045017) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 45 | F-A | Q2 | 6 | [Generalized surface tension bounds in vacuum decay](https://arxiv.org/abs/1711.06776) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 46 | F-A | Q2 | 7 | [Resolving the Hubble Tension with New Early Dark Energy](https://arxiv.org/abs/2006.06686) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 47 | F-A | Q2 | 8 | [Gravitational waves from bubble collisions and fluid motion in strongly supercooled phase transitions](https://arxiv.org/abs/2208.11697) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 48 | F-A | Q2 | 9 | [Heterogeneous bubble nucleation dynamics \| Journal of Fluid Mechanics \| Cambridge Core](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/heterogeneous-bubble-nucleation-dynamics/045D2CED9F9B57578ECEED99B8406360) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 49 | F-A | Q2 | 10 | [(PDF) How fast can the wall move? A study of the electroweak phase transition dynamics](https://www.researchgate.net/publication/2029722_How_fast_can_the_wall_move_A_study_of_the_electroweak_phase_transition_dynamics) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 50 | F-A | Q2 | 11 | [The Growth of Bubbles in Cosmological Phase Transitions](https://arxiv.org/abs/astro-ph/9309059) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 51 | F-A | Q2 | 12 | [Extending classical nucleation theory to consider curvature and real-gas effects - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12744345/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 52 | F-A | Q2 | 13 | [Molecular mechanism for cavitation in water under tension - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5137690/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 53 | F-A | Q2 | 14 | [Bubble correlation in first-order... \| Archive ouverte UNIGE](https://archive-ouverte.unige.ch/unige%3A178019) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 54 | F-A | Q2 | 15 | [Bubble dynamics in a strong first-order quark-hadron transition](https://csnsdoc.ihep.ac.cn/article/doi/10.1088/1674-1137/abdea7) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 55 | F-A | Q2 | 16 | [A-B Transition in Superfluid $$^3$$ He and Cosmological Phase Transitions \| Journal of Low Temperature Physics \| Springer Nature Link](https://doi.org/10.1007%2Fs10909-024-03151-9) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 56 | F-A | Q2 | 17 | [SciPost Phys. Lect.Notes 24 (2021)](https://www.scipost.org/10.21468/SciPostPhysLectNotes.24/pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 57 | F-A | Q2 | 18 | [PHYSICAL REVIEW D](https://diposit.ub.edu/server/api/core/bitstreams/1c0dc508-38e7-4155-96e3-a31d03e96977/content) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 58 | F-A | Q2 | 19 | [Using gravitational waves to see the first second of the](https://eprints.soton.ac.uk/501480/1/2401.04388v3.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 59 | F-A | Q2 | 20 | [PHYSICAL REVIEW C](https://www.rcnp.osaka-u.ac.jp/~toki/p2564_1%20surface.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 60 | F-A | Q2 | 21 | [CERN-TH/96-13](https://cds.cern.ch/record/297990/files/arXiv%3Ahep-ph_9603208.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 61 | F-A | Q2 | 22 | [Chinese Physics C    Vol. 45, No. 4 (2021) 043104](https://scoap3-prod-backend.s3.cern.ch/media/files/67400/10.1088/1674-1137/abdea7.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 62 | F-A | Q2 | 23 | [False vacuum](https://en.wikipedia.org/wiki/False_vacuum) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 63 | F-A | Q2 | 24 | [Rayleigh–Plesset equation](https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Plesset_equation) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 64 | F-A | Q2 | 25 | [Hadamard–Rybczynski equation](https://en.wikipedia.org/wiki/Hadamard%E2%80%93Rybczynski_equation) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 65 | F-A | Q2 | 26 | [Surface tension](https://en.wikipedia.org/wiki/Surface_tension) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 66 | F-A | Q2 | 27 | [Vasiliev equations](https://en.wikipedia.org/wiki/Vasiliev_equations) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 67 | F-A | Q2 | 28 | [Dynamic fluid film equations](https://en.wikipedia.org/wiki/Dynamic_fluid_film_equations) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 68 | F-B | Q3 | 1 | [(PDF) Analysis on Irreversible Processes using the Phase-Field Variational Approach with the Entropy or Energy Functional](https://www.researchgate.net/publication/269040722_Analysis_on_Irreversible_Processes_using_the_Phase-Field_Variational_Approach_with_the_Entropy_or_Energy_Functional) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 69 | F-B | Q3 | 2 | [Non-isothermal phase-field models and evolution equation \| Archives of Mechanics](https://am.ippt.pan.pl/index.php/am/article/view/v58p257) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 70 | F-B | Q3 | 3 | [Analysis on Irreversible Processes using the Phase-Field Variational Approach with the Entropy or Energy Functional](https://arxiv.org/abs/1412.0575) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 71 | F-B | Q3 | 4 | [Thermodynamics of Stress and Electric Field Induced Phase Transition in Relaxor Ferroelectric Crystals - Tieqi Liu, Christopher S. Lynch, Elizabeth A. Mclaughlin, 2007](https://journals.sagepub.com/doi/abs/10.1177/1045389X06066531) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 72 | F-B | Q3 | 5 | [Arch. Mech., 58, 3, pp. 257–271, Warszawa 2006](https://am.ippt.pan.pl/index.php/am/article/download/v58p257/pdf/66) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 73 | F-B | Q3 | 6 | [Internal energy in dissipative relativistic fluids](https://msp.org/jomms/2008/3-6/jomms-v3-n6-p13-s.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 74 | F-B | Q3 | 7 | [Analysis of staggered evolutions for nonlinear energies in phase field fracture - University of Vienna](https://ucrisportal.univie.ac.at/en/publications/analysis-of-staggered-evolutions-for-nonlinear-energies-in-phase-/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 75 | F-B | Q3 | 8 | [Internal energy in dissipative relativistic fluids](https://arxiv.org/abs/0712.1437) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 76 | F-B | Q3 | 9 | [Relativistic Non-Equilibrium Thermodynamics Revisited](https://www.degruyterbrill.com/document/doi/10.1515/JNETDY.2006.002/html) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 77 | F-B | Q3 | 10 | [Deep Learning‐Based Phase‐Field Modelling of Brittle Fracture in Anisotropic Media - Plungė - 2026 - International Journal for Numerical Methods in Engineering - Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1002/nme.70381) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 78 | F-B | Q3 | 11 | [Thermodynamics of Irreversible Processes: Fundamental Constraints, Representations, and Formulation of Boundary Conditions \| MDPI](https://www.mdpi.com/2624-8174/6/2/50) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 79 | F-B | Q3 | 12 | [A Phase-Field Approach to Continuum Damage Mechanics \| MDPI](https://www.mdpi.com/1996-1944/15/21/7671) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 80 | F-B | Q3 | 13 | [The multiphase-field method based on internal state variables \| Continuum Mechanics and Thermodynamics \| Springer Nature Link](https://link.springer.com/article/10.1007/s00161-026-01470-8) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 81 | F-B | Q3 | 14 | [Principle of Virtual Power for thermomechanics of fluids and solids with dissipation - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0020722511001194) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 82 | F-B | Q3 | 15 | [A thermodynamic approach to non-isothermal phase-field evolution in continuum physics - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167278906000066) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 83 | F-B | Q3 | 16 | [Relativistic non-equilibrium thermodynamics revisited](https://arxiv.org/abs/gr-qc/0503047) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 84 | F-B | Q3 | 17 | [Irreversible thermodynamic basis of phase field models: Philosophical Magazine: Vol 91 , No 1 - Get Access](https://www.tandfonline.com/doi/full/10.1080/14786435.2010.491805) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 85 | F-B | Q3 | 18 | [A phase-field model of solidification with convection](https://upload.wikimedia.org/wikipedia/commons/e/ee/A_phase-field_model_of_solidification_with_convection_%28IA_phasefieldmodelo6237ande%29.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 86 | F-B | Q3 | 19 | [A phase-field model with convection: numerical simulations](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir6442.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 87 | F-B | Q3 | 20 | [Irreversible thermodynamic description of dark matter and radiation creation during inflationary reheating](https://arxiv.org/abs/1708.08004) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 88 | F-B | Q3 | 21 | [First law of thermodynamics](https://en.wikipedia.org/wiki/First_law_of_thermodynamics) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 89 | F-B | Q3 | 22 | [Non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 90 | F-B | Q3 | 23 | [Stefan problem](https://en.wikipedia.org/wiki/Stefan_problem) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 91 | F-B | Q3 | 24 | [Phase-field model](https://en.wikipedia.org/wiki/Phase-field_model) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 92 | F-B | Q3 | 25 | [Extremal principles in non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Extremal_principles_in_non-equilibrium_thermodynamics) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 93 | F-B | Q3 | 26 | [Quantum Elastic Geometry](https://es.wikipedia.org/wiki/Quantum_Elastic_Geometry) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 94 | F-C | Q4 | 1 | [A pseudo-dynamic phase-field model for brittle fracture - ScienceDirect](https://doi.org/10.1016/j.jmps.2025.106493) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 95 | F-C | Q4 | 2 | [Fracture in mode I using a conserved phase-field model - PubMed](https://pubmed.ncbi.nlm.nih.gov/11909175/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 96 | F-C | Q4 | 3 | [Fracture in Mode I using a Conserved Phase-Field Model](https://arxiv.org/abs/cond-mat/0108249) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 97 | F-C | Q4 | 4 | [A length-scale insensitive cohesive phase-field interface model: Application to concurrent bulk and interface fracture simulation in Lithium-ion battery materials - University of Southern Denmark](https://portal.findresearcher.sdu.dk/en/publications/a-length-scale-insensitive-cohesive-phase-field-interface-model-a-2/) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 98 | F-C | Q4 | 5 | [Effective fracture toughness in phase-field models for mode-II interface fracture: a maximum energy envelope method by Christopher Fear, Christopher M. Harvey :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6216334) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 99 | F-C | Q4 | 6 | [Laws of crack motion and phase-field models of fracture](https://arxiv.org/abs/0806.0593) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 100 | F-C | Q4 | 7 | [Phase‐field modelling of cohesive interface failure - Borst - 2024 - International Journal for Numerical Methods in Engineering - Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1002/nme.7412) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 101 | F-C | Q4 | 8 | [A phase-field model of frictional shear fracture in geologic materials](https://arxiv.org/abs/2003.04779) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 102 | F-C | Q4 | 9 | [Effective fracture toughness in phase-field models for mode-II interface fracture: a maximum energy envelope method by Christopher Fear, Christopher M. Harvey :: SSRN](https://papers.ssrn.com/sol3/Delivery.cfm/94d67f66-6f30-4cdf-b0c4-e6e28005c88b-MECA.pdf?abstractid=6216334&mirid=1) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 103 | F-C | Q4 | 10 | [An assessment of phase field fracture: crack initiation and growth.](https://www.repository.cam.ac.uk/items/0d3755f1-8923-49cc-896c-bf7102b5efa5) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 104 | F-C | Q4 | 11 | [Multi-level adaptive mesh refinement with non-local energy correction for sharp-diffusive phase-field fracture models by Ye Feng, Yudong Ren, Guangda Lu :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6805208) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 105 | F-C | Q4 | 12 | [The origin of the energy split in phase‐field fracture and eigenfracture - Storm - 2023 - Proceedings in Applied Mathematics and Mechanics - Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1002/pamm.202300295) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 106 | F-C | Q4 | 13 | [A unified sharp-diffusive phase-field model for bulk and interfacial cohesive fracture \| Kurate.org](https://kurate.org/paper/5b427747-37c2-4a7b-b41e-fa0ffa724e70) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 107 | F-C | Q4 | 14 | [PHYSICAL REVIEW E, VOLUME 65, 036117](https://sethna.lassp.cornell.edu/pubPDF/PhaseFieldFracture.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 108 | F-C | Q4 | 15 | [Phase Field Modeling of Fracture and Stress Induced Phase Transitions](https://arxiv.org/abs/cond-mat/0701101) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 109 | F-C | Q4 | 16 | [Multi-level adaptive mesh refinement with non-local energy correction for sharp-diffusive phase-field fracture models by Ye Feng, Yudong Ren, Guangda Lu :: SSRN](https://papers.ssrn.com/sol3/Delivery.cfm/1952a28c-8166-4e58-9955-b8cca27c2577-MECA.pdf?abstractid=6805208&mirid=1) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 110 | F-C | Q4 | 17 | [This is a repository copy of Phase-field regularised cohesive zone model for interface](https://eprints.whiterose.ac.uk/207468/1/chen_deborst22.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 111 | F-C | Q4 | 18 | [A Review on Cementitious Self-Healing and the Potential of Phase-Field Methods for Modeling Crack-Closing and Fracture Recovery \| MDPI](https://www.mdpi.com/1996-1944/13/22/5265) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 112 | F-C | Q4 | 19 | [A length-scale insensitive cohesive phase-field interface model: application to concurrent bulk and interface fracture simulation in Lithium-ion battery materials](https://www.mathematik.uni-ulm.de/stochastik/personal/schmidt/publications/Interface_model.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 113 | F-C | Q4 | 20 | [This is a repository copy of A phase-field model for cohesive fracture.](https://eprints.whiterose.ac.uk/96205/8/WRRO_96205.pdf) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 114 | F-C | Q4 | 21 | [A physically consistent and quantitative phase-field model for anisotropic fracture in brittle multiphase solids](https://publikationen.bibliothek.kit.edu/1000188192/171187452) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 115 | F-C | Q4 | 22 | [First published in:](https://publikationen.bibliothek.kit.edu/1000018565/1367565) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 116 | F-C | Q4 | 23 | [Gunduz Caginalp](https://en.wikipedia.org/wiki/Gunduz_Caginalp) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 117 | F-C | Q4 | 24 | [Phase-field model](https://en.wikipedia.org/wiki/Phase-field_model) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 118 | F-C | Q4 | 25 | [Energy release rate (fracture mechanics)](https://en.wikipedia.org/wiki/Energy_release_rate_%28fracture_mechanics%29) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |
| 119 | F-C | Q4 | 26 | [John W. Cahn](https://en.wikipedia.org/wiki/John_W._Cahn) | NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER | NOT_OPENED |

Kontrolný súčet riadkov:

```text
Q1 rows = 39
Q2 rows = 28
Q3 rows = 26
Q4 rows = 26
TOTAL = 119
```

## 5. S0–S13 a W10 dôsledok

```text
S0: NOT_COMPLETED / FIRST_ELIGIBLE_PRIMARY_EXACT_EQUATIONS_INACCESSIBLE
S1-S12: NOT_REACHED
S13: PASS_SCOPE_GUARD
```

Výsledok presne zodpovedá frozen coverage vetve:

```text
REVIEW_SEARCH_COVERAGE_INCOMPLETE_NO_PHYSICAL_INFERENCE
```

Preto:

- nebol získaný úplný W10;
- W10 nebol vyvrátený;
- nebol prijatý ani zamietnutý žiadny fyzikálny passport;
- F-A nebola vyčerpaná a F-B/F-C neboli fyzikálne screenované;
- nevznikol C01 no-go, globálny literature no-go ani dôkaz prázdnosti
  `A_RW1`;
- inaccessible kandidát nespotrebúva physical-witness attempt;
- coverage failure pred complete source-physics screenom nezvyšuje P4
  work-atom count.

## 6. Autoritatívne počítadlá a nonclaims

```text
P4 work atoms: 2_UNCHANGED
P4 physical witness attempts consumed: 0_UNCHANGED
K4: 60/100_UNCHANGED
P5: 3.5/6_UNCHANGED
RUN_AUTHORIZED: false
Python processes: 0
P5.4/G8/G9/steam/completion/S8-H0 fit: NOT_OPENED
```

Tento výsledok je technický/provenienčný coverage blocker. Nie je formula,
numerical, physical ani observational failure a nemení truth status teórie.

## 7. Súborový rozpočet a auditný handoff

V2 atóm vytvoril presne šesť vopred zdôvodnených live scientific/raw
artefaktov: preregistráciu 263, štyri immutable receipts 263A–263D a tento
result 264. Centrálny event ledger je jediný aktualizovaný register; auditné
package kópie sú nula.

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-W10-RAW-V2-SOURCE-RESULT-AUDIT-20260727-170
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_w10_v2_source_result_audit
ARTIFACT_AUTHOR_TASK_ID: /root task169
STATIC_AUDITOR_TASK_ID: /root/c01_w10_v2_prereg_audit task164R
INTERNAL_AUDITOR_TASK_ID: /root/c01_w10_v2_source_result_audit task170
PACKAGE_CURATOR_TASK_ID: UNASSIGNED_NOT_REACHED
EXTERNAL_AUDITOR_TASK_ID: UNASSIGNED_NOT_REACHED
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_RAW_V2
CURRENT_PHASE: CANDIDATE_SOURCE_COVERAGE_RESULT_AWAITING_INDEPENDENT_AUDIT
ALLOWED_NEXT_ACTION: independent read-only audit of exact document264 against frozen 261/263, receipts 263A-D, task167/task168 dispositions and cited primary metadata
ALLOWED_READS: mandatory bootstrap; plans; documents259-264; receipts263A-D; event ledger; exact cited primary source pages; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; new search; skip rank3; infer unavailable equations or missing W10 fields; physics truth/verdict; Python; score/depth/run change; package work
IMMUTABLE_INPUT_PATHS_AND_SHA256: document261=FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B; document263=8CC33C71C2C7479399741EF5F8B0019645210555F8AB59BE9AB468C75CC95AF3; 263A=0C4FBC6F868DAE86C7ED8FA81195E9400918C5F8F8350BDFC7A0DDE8A74132E7; 263B=45BF5A2BE5F767EF90C7C4BB3D7FF0EB3D737AAADCB7A8D3467A8947F3124145; 263C=823E5FE8F8DE5D937EC0AE7E39EB86917D2BBD3A6F22F903B83DDD30C03648B1; 263D=BB41A43ED0B6ADF174FE9164C1D4A9F65B049C4965262028E8C49B19E5B7B3DE
PREREG_SHA256: 8CC33C71C2C7479399741EF5F8B0019645210555F8AB59BE9AB468C75CC95AF3
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit recommendation
DONE_WHEN: all 119 rows, eligibility/dedup/rank stop, canonical-access attempts, S0-S13 branch, counts/nonclaims and file budget are independently verified
NEXT_ROLE: main_orchestrator
```

## Appendix A — immutable exact-target access replay

```text
ACCESS_EVIDENCE_ID: E1_Q1R1_ARXIV
TARGET_URL: https://arxiv.org/abs/2307.12080
PROVIDER_REF_OR_DIRECT_URL: DIRECT_URL
BEGIN_EXACT_OPEN_RETURN
[2307.12080] General relativistic bubble growth in cosmological phase transitions (https://arxiv.org/abs/2307.12080)
citeturn32view0 [wordlim: 200] Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2307.12080","lineno":null}); Total lines: 169
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Astrophysics > Cosmology and Nongalactic Astrophysics
L7: 
L8: [Submitted on 22 Jul 2023 (cite5†v1 ), last revised 29 Aug 2023 (this version, v2)]
L9: # Title:General relativistic bubble growth in cosmological phase transitions
L10: 
L11: Authors:cite6†Lorenzo Giombi , cite7†Mark Hindmarsh L12: 
L13: View a PDF of the paper titled General relativistic bubble growth in cosmological phase transitions, by Lorenzo Giombi and 1 other authors
L14: 
L15: cite8†View PDF L16: > Abstract:We use a full general relativistic framework to study the self-similar expansion of bubbles of the stable phase into a flat Friedmann-Lemaître-Robertson-Walker Universe in a first order phase transition in the early Universe.
L17: With a simple linear barotropic equation of state in both phases, and in the limit of a phase boundary of negligible width, we find that self-similar solutions exist, which are qualitatively similar to the analogous solutions in Minkowski space, but with distinguishing features. Rarefaction waves extend to the centre of the bubble, while spatial sections near the centre of the bubble have negative curvature.
L18: Gravitational effects redistribute the kinetic energy of the fluid around the bubble, and can change the kinetic energy fraction significantly. The kinetic energy fraction of the gravitating solution can be enhanced over the analogous Minkowski solution by as much as $\mathcal{O}(1)$, and suppressed by a factor as larger as $\mathcal{O}(10)$ in case of fast detonations.
L19: The amount of negative spatial curvature at the centre of the bubble is of the same order of magnitude of the naive expectation based on considerations of the energy density perturbation in Minkowski solutions, with gravitating deflagrations less negatively curved, and detonations more.
L20: We infer that general relativistic effects might have a significant impact on accurate calculations of the gravitational wave power spectrum when the bubble size becomes comparable to the cosmological Hubble radius, affecting the primary generation from the fluid shear stress, and inducing secondary generation by scalar perturbations.
L21: Comments:  | 42 pages, 11 figures
L22: Subjects:  | Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc)
L23: Report number:  | HIP-2023-12/TH
L24: Cite as:  | cite9†arXiv:2307.12080 [astro-ph.CO]
L25:    | (or cite10†arXiv:2307.12080v2 [astro-ph.CO] for this version)
L26:    | cite11†https://doi.org/10.48550/arXiv.2307.12080†doi.org arXiv-issued DOI via DataCite
L27: ## Submission history
L28: 
L29: From: Lorenzo Giombi [cite12†view email ]
L30: cite5†[v1] Sat, 22 Jul 2023 13:50:06 UTC (2,020 KB)
L31: [v2] Tue, 29 Aug 2023 12:38:14 UTC (2,244 KB)
L32: 
L33: Full-text links:
L34: 
L35: ## Access Paper:
L36: 
L37: View a PDF of the paper titled General relativistic bubble growth in cosmological phase transitions, by Lorenzo Giombi and 1 other authors
L38: 
L39:   * cite8†View PDF L40:   * cite13†TeX Source L41: 
L42: cite14†view license L43: ### Current browse context:
L44: 
L45: astro-ph.CO
L46: 
L47: cite15†< prev |   cite16†next > L48: 
L49: cite17†new | cite18†recent | cite19†2023-07 L50: 
L51: Change to browse by:
L52: 
L53: cite20†astro-ph L54: cite21†gr-qc L55: 
L56: ### References & Citations
L57: 
L58:   * cite22†INSPIRE HEP†inspirehep.net L59:   * cite23†NASA ADS†ui.adsabs.harvard.edu L60:   * cite24†Google Scholar†scholar.google.com L61:   * cite25†Semantic Scholar†api.semanticscholar.org L62: 
L63: [Button: export BibTeX citation] Loading...
L64: 
L65: ## BibTeX formatted citation
L66: 
L67: [Button: ×]
L68: 
L69: loading...
L70: 
L71: Data provided by:
L72: ### Bookmark
L73: 
L74: [Input] Bibliographic Tools
L75: 
L76: # Bibliographic and Citation Tools
L77: 
L78: [Input] Bibliographic Explorer Toggle
L79: 
L80: Bibliographic Explorer (cite26†What is the Explorer?†info.arxiv.org )
L81: 
L82: [Input] Connected Papers Toggle
L83: 
L84: Connected Papers (cite27†What is Connected Papers?†www.connectedpapers.com )
L85: 
L86: [Input] Litmaps Toggle
L87: 
L88: Litmaps (cite28†What is Litmaps?†www.litmaps.co )
L89: 
L90: [Input] scite.ai Toggle
L91: 
L92: scite Smart Citations (cite29†What are Smart Citations?†www.scite.ai )
L93: 
L94: [Input] Code, Data, Media
L95: # Code, Data and Media Associated with this Article
L96: 
L97: [Input] alphaXiv Toggle
L98: 
L99: alphaXiv (cite30†What is alphaXiv?†alphaxiv.org )
L100: 
L101: [Input] Links to Code Toggle
L102: 
L103: CatalyzeX Code Finder for Papers (cite31†What is CatalyzeX?†www.catalyzex.com )
L104: 
L105: [Input] DagsHub Toggle
L106: 
L107: DagsHub (cite32†What is DagsHub?†dagshub.com )
L108: 
L109: [Input] GotitPub Toggle
L110: 
L111: Gotit.pub (cite33†What is GotitPub?†gotit.pub )
L112: 
L113: [Input] Huggingface Toggle
L114: 
L115: Hugging Face (cite34†What is Huggingface?†huggingface.co )
L116: 
L117: [Input] ScienceCast Toggle
L118: ScienceCast (cite35†What is ScienceCast?†sciencecast.org )
L119: 
L120: [Input] Demos
L121: # Demos
L122: 
L123: [Input] Replicate Toggle
L124: 
L125: Replicate (cite36†What is Replicate?†replicate.com )
L126: 
L127: [Input] Spaces Toggle
L128: 
L129: Hugging Face Spaces (cite37†What is Spaces?†huggingface.co )
L130: 
L131: [Input] Spaces Toggle
L132: 
L133: TXYZ.AI (cite38†What is TXYZ.AI?†txyz.ai )
L134: 
L135: [Input] Related Papers
L136: # Recommenders and Search Tools
L137: 
L138: [Input] Link to Influence Flower
L139: 
L140: Influence Flower (cite39†What are Influence Flowers?†influencemap.cmlab.dev )
L141: 
L142: [Input] Core recommender toggle
L143: 
L144: CORE Recommender (cite40†What is CORE?†core.ac.uk )
L145: 
L146: [Input] IArxiv recommender toggle
L147: 
L148: IArxiv Recommender (cite41†What is IArxiv?†iarxiv.org )
L149: 
L150:   * Author
L151:   * Venue
L152:   * Institution
L153:   * Topic
L154: 
L155: [Input] About arXivLabs
L156: # arXivLabs: experimental projects with community collaborators
L157: 
L158: arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
L159: 
L160: Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
L161: Have an idea for a project that will add value for arXiv's community? cite42†Learn more about arXivLabs†info.arxiv.org .
L162: 
L163: cite43†Which authors of this paper are endorsers? | Disable MathJax (cite44†What is MathJax?†info.arxiv.org )
L164: 
L165: We gratefully acknowledge support from our major funders, cite45†member institutions†info.arxiv.org , , and all contributors.
L166: cite46†About†info.arxiv.org · cite47†Help†info.arxiv.org · cite48†Contact†info.arxiv.org · cite49†Subscribe†info.arxiv.org · cite50†Copyright†info.arxiv.org · cite51†Privacy†info.arxiv.org · cite52†Accessibility†info.arxiv.org · cite53†Operational Status (opens in new tab)†status.arxiv.org L167: 
L168: Major funding support from

END_EXACT_OPEN_RETURN
```

```text
ACCESS_EVIDENCE_ID: E2_Q1R3_MONASH_SEARCH_REF
TARGET_URL: https://research.monash.edu/en/publications/model-dependent-analysis-method-for-energy-budget-of-the-cosmolog/
PROVIDER_REF_OR_DIRECT_URL: turn15search1
BEGIN_EXACT_OPEN_RETURN
Internal Error ()
citeturn33view0 [wordlim: 200] Source: open({"ref_id":"turn15search1","lineno":null}); Total lines: 1
L0: Failed to fetch https://research.monash.edu/en/publications/model-dependent-analysis-method-for-energy-budget-of-the-cosmolog/: Cache miss

END_EXACT_OPEN_RETURN
```

```text
ACCESS_EVIDENCE_ID: E3_Q1R3_DOI
TARGET_URL: https://doi.org/10.1088/1475-7516/2023/07/006
PROVIDER_REF_OR_DIRECT_URL: DIRECT_URL
BEGIN_EXACT_OPEN_RETURN
Internal Error ()
citeturn34view0 [wordlim: 200] Source: open({"ref_id":"https://doi.org/10.1088/1475-7516/2023/07/006","lineno":null}); Total lines: 1
L0: URL https://doi.org/10.1088/1475-7516/2023/07/006 is not safe to open (non-retryable error)

END_EXACT_OPEN_RETURN
```

```text
ACCESS_EVIDENCE_ID: E4_Q1R3_IOP_ARTICLE
TARGET_URL: https://iopscience.iop.org/article/10.1088/1475-7516/2023/07/006
PROVIDER_REF_OR_DIRECT_URL: DIRECT_URL
BEGIN_EXACT_OPEN_RETURN
Internal Error ()
citeturn35view0 [wordlim: 200] Source: open({"ref_id":"https://iopscience.iop.org/article/10.1088/1475-7516/2023/07/006","lineno":null}); Total lines: 1
L0: Failed to fetch https://iopscience.iop.org/article/10.1088/1475-7516/2023/07/006: Cache miss

END_EXACT_OPEN_RETURN
```

```text
ACCESS_EVIDENCE_ID: E5_Q1R3_IOP_PDF
TARGET_URL: https://iopscience.iop.org/article/10.1088/1475-7516/2023/07/006/pdf
PROVIDER_REF_OR_DIRECT_URL: DIRECT_URL
BEGIN_EXACT_OPEN_RETURN
Internal Error ()
citeturn36view0 [wordlim: 200] Source: open({"ref_id":"https://iopscience.iop.org/article/10.1088/1475-7516/2023/07/006/pdf","lineno":null}); Total lines: 1
L0: URL https://iopscience.iop.org/article/10.1088/1475-7516/2023/07/006/pdf is not safe to open (non-retryable error)

END_EXACT_OPEN_RETURN
```

```text
ACCESS_EVIDENCE_ID: E6_Q1R3_MONASH_SUCCESSFUL_VIEW
TARGET_URL: https://research.monash.edu/en/publications/model-dependent-analysis-method-for-energy-budget-of-the-cosmolog/
PROVIDER_REF_OR_DIRECT_URL: turn21view0
BEGIN_EXACT_OPEN_RETURN

        Model-dependent analysis method for energy budget of the cosmological first-order phase transition
      -  Monash University (https://research.monash.edu/en/publications/model-dependent-analysis-method-for-energy-budget-of-the-cosmolog/)
citeturn37view0 [wordlim: 200] Content type: text/html; Source: open({"ref_id":"turn21view0","lineno":null}); Total lines: 173
L0: cite0†Skip to main navigation Skip to search cite1†Skip to main content L1: 
L2: cite2† Monash University Home  L3: 
L4: Search content at Monash University
L5: 
L6:   * cite2†Home L7:   * cite3†Profiles L8:   * cite4†Research units L9:   * cite5†Research Infrastructure L10:   * cite6†Projects L11:   * cite7†Outputs L12:   * cite8†Prizes L13:   * cite9†Activities L14:   * cite10†Press/Media L15: # Model-dependent analysis method for energy budget of the cosmological first-order phase transition
L16: 
L17:   * cite11†Xiao Wang L18:   * , Chi Tian
L19:   * , Fa Peng Huang
L20: 
L21: Research output: Contribution to journal › Article › Research › peer-review
L22: 
L23: cite12† 13 Link opens in a new tab †www.scopus.com Citations (Scopus)
L24: 
L25:   * cite13† Overview  L26: ## Abstract
L27: The kinetic energy of the fluid shell in the cosmological first-order phase transition is crucial for predicting the gravitational wave signals generated by the sound wave mechanism. We propose a model-dependent method to calculate the kinetic energy fraction by dividing the bubble-fluid system into three distinct regions: the symmetric phase, the broken phase, and the bubble wall.
L28: By solving the local equation of motion of the scalar field with a phenomenological friction term, the bubble wall velocity and the boundary conditions of the fluid equations of both phases can be derived simultaneously. Then, for a given particle physics model, the fluid profiles of different hydrodynamical modes and the corresponding kinetic energy fraction can be obtained. Our method can also capture the temperature dependency of the sound speed of the plasma.
L29: Compared with the conventional model-independent method, our approach is based on an accurate equation of state derived directly from the effective potential and takes into account the contribution of the bubble wall to the energy-momentum tensor. Therefore, our method in-principle provides a more consistent and accurate result, which is crucial for high-precision calculations of the gravitational waves induced by the first-order phase transition.
L30: Original language English
L31: Article number JCAP07(2023)006
L32: Number of pages 31
L33: Journal Journal of Cosmology and Astroparticle Physics
L34: Volume 2023
L35: Issue number 7
L36: DOIs
L37: 
L38:   * cite14†https://doi.org/10.1088/1475-7516/2023/07/006†doi.org L39: 
L40: Publication status Published - Jul 2023
L41: Externally published Yes
L42: ## Keywords
L43: 
L44:   * cosmological phase transitions
L45:   * cosmology of theories beyond the SM
L46:   * gravitational waves / theory
L47:   * physics of the early universe
L48: 
L49: ## Access to Document
L50: 
L51:   * cite14†10.1088/1475-7516/2023/07/006†doi.org L52: 
L53: ## Other files and links
L54: 
L55:   * cite15†Link to publication in Scopus†www.scopus.com L56: ## Cite this
L57: 
L58:   *  APA
L59:   *  Author
L60:   *  BIBTEX
L61:   *  Harvard
L62:   *  Standard
L63:   *  RIS
L64:   *  Vancouver
L65: 
L66: cite11†Wang, X. , Tian, C., & Huang, F. P. (2023). cite13†Model-dependent analysis method for energy budget of the cosmological first-order phase transition . Journal of Cosmology and Astroparticle Physics, 2023(7), Article JCAP07(2023)006. cite14†https://doi.org/10.1088/1475-7516/2023/07/006†doi.org L67: cite11†Wang, Xiao ; Tian, Chi ; Huang, Fa Peng. / cite13†Model-dependent analysis method for energy budget of the cosmological first-order phase transition . In: Journal of Cosmology and Astroparticle Physics. 2023 ; Vol. 2023, No. 7.
L68: 
L69: @article{d00873802e0f4eae985c1003e74600dc,
L70: 
L71: title = "Model-dependent analysis method for energy budget of the cosmological first-order phase transition",
L72: abstract = "The kinetic energy of the fluid shell in the cosmological first-order phase transition is crucial for predicting the gravitational wave signals generated by the sound wave mechanism. We propose a model-dependent method to calculate the kinetic energy fraction by dividing the bubble-fluid system into three distinct regions: the symmetric phase, the broken phase, and the bubble wall.
L73: By solving the local equation of motion of the scalar field with a phenomenological friction term, the bubble wall velocity and the boundary conditions of the fluid equations of both phases can be derived simultaneously. Then, for a given particle physics model, the fluid profiles of different hydrodynamical modes and the corresponding kinetic energy fraction can be obtained. Our method can also capture the temperature dependency of the sound speed of the plasma.
L74: Compared with the conventional model-independent method, our approach is based on an accurate equation of state derived directly from the effective potential and takes into account the contribution of the bubble wall to the energy-momentum tensor. Therefore, our method in-principle provides a more consistent and accurate result, which is crucial for high-precision calculations of the gravitational waves induced by the first-order phase transition.",
L75: keywords = "cosmological phase transitions, cosmology of theories beyond the SM, gravitational waves / theory, physics of the early universe",
L76: 
L77: author = "Xiao Wang and Chi Tian and Huang, \{Fa Peng\}",
L78: 
L79: note = "Publisher Copyright: {\textcopyright} 2023 IOP Publishing Ltd and Sissa Medialab.",
L80: 
L81: year = "2023",
L82: 
L83: month = jul,
L84: 
L85: doi = "10.1088/1475-7516/2023/07/006",
L86: 
L87: language = "English",
L88: 
L89: volume = "2023",
L90: 
L91: journal = "Journal of Cosmology and Astroparticle Physics",
L92: 
L93: issn = "1475-7516",
L94: publisher = "IOP Publishing",
L95: 
L96: number = "7",
L97: 
L98: }
L99: 
L100: cite11†Wang, X , Tian, C & Huang, FP 2023, 'cite13†Model-dependent analysis method for energy budget of the cosmological first-order phase transition ', Journal of Cosmology and Astroparticle Physics, vol. 2023, no. 7, JCAP07(2023)006. cite14†https://doi.org/10.1088/1475-7516/2023/07/006†doi.org L101: cite13†Model-dependent analysis method for energy budget of the cosmological first-order phase transition. / cite11†Wang, Xiao ; Tian, Chi; Huang, Fa Peng.
L102: In: Journal of Cosmology and Astroparticle Physics, Vol. 2023, No. 7, JCAP07(2023)006, 07.2023.
L103: 
L104: Research output: Contribution to journal › Article › Research › peer-review
L105: 
L106: TY - JOUR
L107: 
L108: T1 - Model-dependent analysis method for energy budget of the cosmological first-order phase transition
L109: 
L110: AU - Wang, Xiao
L111: 
L112: AU - Tian, Chi
L113: 
L114: AU - Huang, Fa Peng
L115: N1 - Publisher Copyright: © 2023 IOP Publishing Ltd and Sissa Medialab.
L116: 
L117: PY - 2023/7
L118: 
L119: Y1 - 2023/7
L120: N2 - The kinetic energy of the fluid shell in the cosmological first-order phase transition is crucial for predicting the gravitational wave signals generated by the sound wave mechanism. We propose a model-dependent method to calculate the kinetic energy fraction by dividing the bubble-fluid system into three distinct regions: the symmetric phase, the broken phase, and the bubble wall.
L121: By solving the local equation of motion of the scalar field with a phenomenological friction term, the bubble wall velocity and the boundary conditions of the fluid equations of both phases can be derived simultaneously. Then, for a given particle physics model, the fluid profiles of different hydrodynamical modes and the corresponding kinetic energy fraction can be obtained. Our method can also capture the temperature dependency of the sound speed of the plasma.
L122: Compared with the conventional model-independent method, our approach is based on an accurate equation of state derived directly from the effective potential and takes into account the contribution of the bubble wall to the energy-momentum tensor. Therefore, our method in-principle provides a more consistent and accurate result, which is crucial for high-precision calculations of the gravitational waves induced by the first-order phase transition.
L123: AB - The kinetic energy of the fluid shell in the cosmological first-order phase transition is crucial for predicting the gravitational wave signals generated by the sound wave mechanism. We propose a model-dependent method to calculate the kinetic energy fraction by dividing the bubble-fluid system into three distinct regions: the symmetric phase, the broken phase, and the bubble wall.
L124: By solving the local equation of motion of the scalar field with a phenomenological friction term, the bubble wall velocity and the boundary conditions of the fluid equations of both phases can be derived simultaneously. Then, for a given particle physics model, the fluid profiles of different hydrodynamical modes and the corresponding kinetic energy fraction can be obtained. Our method can also capture the temperature dependency of the sound speed of the plasma.
L125: Compared with the conventional model-independent method, our approach is based on an accurate equation of state derived directly from the effective potential and takes into account the contribution of the bubble wall to the energy-momentum tensor. Therefore, our method in-principle provides a more consistent and accurate result, which is crucial for high-precision calculations of the gravitational waves induced by the first-order phase transition.
L126: KW - cosmological phase transitions
L127: 
L128: KW - cosmology of theories beyond the SM
L129: 
L130: KW - gravitational waves / theory
L131: 
L132: KW - physics of the early universe
L133: 
L134: UR - https://www.scopus.com/pages/publications/85164438987
L135: 
L136: U2 - 10.1088/1475-7516/2023/07/006
L137: 
L138: DO - 10.1088/1475-7516/2023/07/006
L139: 
L140: M3 - Article
L141: 
L142: AN - SCOPUS:85164438987
L143: 
L144: SN - 1475-7516
L145: 
L146: VL - 2023
L147: 
L148: JO - Journal of Cosmology and Astroparticle Physics
L149: 
L150: JF - Journal of Cosmology and Astroparticle Physics
L151: 
L152: IS - 7
L153: 
L154: M1 - JCAP07(2023)006
L155: 
L156: ER -
L157: cite11†Wang X , Tian C, Huang FP. cite13†Model-dependent analysis method for energy budget of the cosmological first-order phase transition . Journal of Cosmology and Astroparticle Physics. 2023 Jul;2023(7):JCAP07(2023)006. doi: 10.1088/1475-7516/2023/07/006
L158: 
L159:   *   *   * cite16† †twitter.com L160:   *   *
L161: 
L162: Powered by cite17†Pure Link opens in a new tab†www.elsevier.com , cite18†Scopus Link opens in a new tab†www.scopus.com & cite19†Elsevier Fingerprint Engine™ Link opens in a new tab†www.elsevier.com L163: All content on this site: Copyright © 2026 Monash University, its licensors, and contributors. All rights are reserved, including those for text and data mining, AI training, and similar technologies. For all open access content, the relevant licensing terms apply
L164: 
L165: We use cookies to help provide and enhance our service and tailor content. By continuing you agree to the cite20†use of cookies L166: 
L167: cite21†Monash University data protection policy Link opens in a new tab†www.monash.edu L168: cite22†About web accessibility Link opens in a new tab L169: 
L170: cite23†Report vulnerability Link opens in a new tab†elsevier.responsibledisclosure.com L171: 
L172: cite24† Contact us 
END_EXACT_OPEN_RETURN
```
