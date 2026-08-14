# A2-K11 — base závislosti

Žiadny autoritatívny fyzikálny base modul ešte neexistuje. Historické
rovnice sú rozptýlené v 45–54 a ich numerický PASS bol neskôr obmedzený
auditom.

Kovariantný K11-R operátor, znamienka a úplný CS2 kontrakt sú už
predregistrované v
`../ARTIFACTS/K11_CS2_FULL_MULTISPECIES_CONSTRAINED_DAE_PREREGISTRATION.md`.
Balík `scripts/baseScripts/a2_k11_cs2/` už má zmrazenú prvú revíziu:

| Modul | SHA-256 | Stav |
|---|---|---|
| `full_multispecies_constrained_dae.py` | `19263A674E1F342E06E6D0D3999E65E58687CCFF20E5EE083A05D06D7BB107FF` | `K11-CS2-S0-v001 / PASS_FORMULA_IDENTITIES_ONLY / STOP_STATE_REGISTER_V001`; full propagátor fail-closed |
| `full_multispecies_constrained_dae_v002.py` | `NOT_CREATED` | posledná oprava 2/2; musí obsahovať celý exact-A1 thermal/full-DAE kontrakt, nie iba S0 |
| `finite_hierarchy_contract_v002.py` | `30610E17EA247B035962439EBF40467F33ACDBAB26298E3CBD47EC57DA48B42E` | autoritatívny ordered state/RHS contract 25/33/41 a non-exact closure metadata |
| `finite_hierarchy_source_ast_preflight_v003.py` | `58385E957E379AA1BFFB6F97453F58DD33682CAB05FFF097C9D8D7DC616B5203` | pinned CAMB source-AST a negatívne fixtures; attempt 5 PASS 55/55 |
| `__init__.py` lazy | `C3C739B916745581B8AEA8C698DFA82FFA441A8E9FF7F57FDAEDE32DAEF39391` | zabraňuje eager CAMB/SymPy importu; legacy exporty zachované |

Táto revízia sa nesmie rozšíriť tichým prepisom. Plný propagátor dostane
nový versioned modul v rovnakom balíku a nový hash. Historické skripty 45–54
sa nesmú importovať.

V002 sa nesmie vytvoriť ani spustiť, kým nie je uzavretý zdroj exact-A1
`x_e/opacity/T_b`, TCA/full handoff a top closure každej hierarchie.
Kopírovaná štandardná opacity by dovolila iba REVIEW, nie fyzický verdict.

Pripnutý zdrojový kandidát je `external/CLASS` na commite
`e85808324f51fc694d12e3ed7439552a3c3f9540` s HyRec 2020. Audit v
`../ARTIFACTS/K11_CS2_CLASS_HYREC_ARCHITECTURE_SOURCE_MAP_AND_FEASIBILITY_AUDIT.md`
potvrdil, že CLASS odovzdáva HyRec aktuálne `H(z)`, ale vyžaduje nový
coupled fuel/ash background, custom perturbácie/módy a exaktnú mapu medzi
natívnou CLASS polarizáciou a CAMB-E auditným registrom. Ide o dependency
candidate, nie o vytvorený base ani fyzický PASS.

Licenčná proveniencia checkout-u nie je zatiaľ uzavretá. Lokálny audit
zdroja môže pokračovať, no upravený CLASS strom sa nesmie zaradiť do
release balíka bez doloženej licencie.

Historická formulácia „posledná oprava 2/2“ bola 2026-07-16 obmedzená
pracovným pravidlom `WORKING-TECH-INCIDENT-NONCONSUMPTION`. Technická chyba
base, adaptera alebo runnera sa zapíše a opraví bez spotrebovania fyzikálneho
pokusu. Jedna implementačná línia má cap 10 po sebe idúcich technických
zlyhaní; potom dostane zdôvodnený
`TECHNICAL_STOP`, nie fyzikálny STOP. Nová fyzická verzia vznikne až pri
zmene rovníc, mechanizmu alebo rozsahu.

Readiness audit po zrušení capu 2/2 pôvodne zakázal vytvoriť full DAE base:
kanonický CAMB-E register bol `25/33/41`, ale chýbal poctivý status
`E_gamma_L` top rezu alebo exact native CLASS↔CAMB-E adapter. Následný audit
odmietol univerzálnu exact closure a povolil iba deklarovaný numerický rez s
konvergenciou; source-AST contract neskôr prešiel v pokuse 5/10.

K11-TC-A0 už má invariantný STOP: univerzálna exact finite-`L` CAMB-E
closure neexistuje. Povolený nasledovník K11-TC-A3 smie vytvoriť iba nový
contract/preflight base s deklarovaným numerickým topom; starý v001 base sa
nesmie patchovať ani importovať ako state autorita. Budúci full base musí
preukázať `lmax` a closure-family konvergenciu.

Historický balík 5 uzavrel ľahký source-AST/contract preflight a vynuloval
aktívny counter na `0/10`. Autoritatívne aktívne
závislosti sú `finite_hierarchy_contract_v002.py`,
`finite_hierarchy_source_ast_preflight_v003.py` a lazy `__init__.py`; ich
hashy sú v result dokumente. Heavy v001 base ostáva formula-regression
artefaktom a nie je state autorita. Ďalší full DAE balík má historické číslo
6, aktívny counter pred ním je `0/10` a zatiaľ je `NOT_CREATED`.
