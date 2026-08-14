# KMPC-036 — M1 order-7 execution ledger

**Stav:** `EXECUTED / AUTHORITATIVE SCOPED PASS+REVIEW`; pozri dokument 65  
**Interný limit:** `4.8 s`; **vonkajší limit:** `10 s` na proces

| Fáza | Proces | Očakávanie | Odchýlka | Stav |
|---:|---|---|---|---|
| 1 | compile base | exit 0 bez výstupu | technická chyba; fyzika NOT_RUN | `PASS`; exit 0; wall `0.5 s` |
| 2 | compile runner | exit 0 bez výstupu | technická chyba; fyzika NOT_RUN | `PASS`; exit 0; wall `0.5 s` |
| 3 | `--help` | iba M1 order-7 CLI | zlá identita/technická chyba | `PASS`; exit 0; wall `0.6 s`; bez JSON |
| 4 | smoke | hash/count/negative fixtures/JSON safety; bez JSON | technická chyba; audit zakázaný | `PASS`; exit 0; wall `1.1 s`; 6/6 fixtures; bez JSON |
| 5 | audit | order5 regression + order7 full-range core/holdout | failure JSON bez fyziky | `COMPLETE`; exit 0; wall `1.5 s`; internal `0.265 s` |

## Ľudské očakávanie

Ak je order-7 iba konzistentným pokračovaním toho istého seedu, lower
coefficients `-1..5` sa nezmenia nad hybridný prah, rank bude `98/98` a
všetkých 139 full-range driver+initial+holdout riadkov prejde. PASS povoľuje
iba tri nezávislé audity a hlavný rozsudok; support step 3 sa nespustí
automaticky. Pri drift/core/holdout odchýlke zostane REVIEW a hľadá sa presná
príčina. Technický pád nemení fyziku.

Očakávania sa po procesoch spätne nemenia. Pred každým Python procesom sa
sem doplní jeho ľudský opis, presný očakávaný rozsah, PASS a odchýlkový postup.

## Pred procesom 1 — compile base

Kontroluje sa iba syntax tenkého order-7 auditného adaptéra; žiadna fyzika
sa ešte nerieši. Očakávame `exit 0` bez výstupu do `10 s`. PASS povoľuje
samostatný compile runnera. Chyba/timeout je technický incident, fyzika ostáva
`NOT_RUN` a ďalší proces sa nespustí.

## Výsledok procesu 1

Base compile skončil `exit 0` za `0.5 s` bez výstupu. Je to iba technický
PASS syntaxe a neresetuje technické počítadlo.

## Pred procesom 2 — compile runner

Kontroluje sa syntax runnera 280, jeho hash/canonical-output/deadline/failure
guardov. Očakávame `exit 0` bez výstupu do `10 s`. PASS povoľuje iba `--help`;
chyba/timeout zastaví balík bez fyzikálneho výsledku.

## Výsledok procesu 2

Runner compile skončil `exit 0` za `0.5 s` bez výstupu. Je to technický PASS.

## Pred procesom 3 — `--help`

Runner iba vypíše povolené argumenty. Očakávame vzájomne výlučné
`--smoke/--audit`, limit a canonical output a jasnú identitu
`M1_ORDER7_PROVENANCE_GATE only`; nesmie tvrdiť ani spúšťať support step 3 a
nesmie vytvoriť JSON. Odchýlka je technický/dokumentačný blocker pred smoke.

## Výsledok procesu 3

Help skončil `exit 0` za `0.6 s`, explicitne uviedol
`M1_ORDER7_PROVENANCE_GATE only; does not run CDI support step 3` a
nevytvoril success ani failure JSON.

## Pred procesom 4 — smoke

Smoke bez fyzikálneho solve overí tri zmrazené zdrojové hashe, rozmery
`121×99`/`121×98`, 18 holdoutov a šesť negatívnych fixtures: wrong order,
reordered states, missing high power, missing anchor, missing a duplicate
holdout. Očakávame `smoke_pass=true`, `exit 0` pod `4.8 s` a bez JSON. Chyba
alebo timeout je technický incident a hlavný audit sa nespustí.

## Výsledok procesu 4

Smoke skončil `exit 0` za `1.1 s`; všetkých šesť negatívnych fixtures bolo
správne odmietnutých a success/failure JSON nevznikol. Je to technický PASS,
nie vecný výsledok, preto sám neresetuje counter.

## Pred procesom 5 — hlavný order-7 audit

Ľudsky: rovnaký ukotvený CDI M1 seed sa vypočíta do order 5 a order 7.
Order 7 musí mať 99 full coefficients, exact anchor nechá 98 unknowns a
samostatný audit znovu zostaví všetkých 121 driver+initial a 18 `00/0i`
holdout riadkov na powers `-1..7`. Lower coefficients a background sa
porovnajú s order 5 a order-5 metadata s immutable KMPC-035.

Očakávame rank `98/98`, inverse condition `>=1e-10`, anchor diff `<=1e-14`,
každý full-range residual pod relative `1e-10` alebo absolute `1e-12` a
order5→7 drift pod hybrid `1e-14/1e-12`. PASS vytvorí iba kandidáta na M1
order-7 provenienciu a následné tri audity; support step 3 stále nebude
spustený. Regression/core/holdout odchýlka znamená REVIEW a lokalizáciu
príčiny. Exception/timeout je technická chyba bez fyzikálneho verdiktu.

## Výsledok procesu 5 — pred autoritatívnym auditom

Audit skončil `exit 0` za `1.5 s`, interný runtime `0.265 s`. Kanonický JSON
má SHA-256 `39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497`
a `69 194 B`; failure JSON nevznikol.

Regression, shapes, rank `98/98`, anchor, condition, state coverage, holdout,
finite a order5→7 state/background brány prešli. Core zlyhal iba na troch
driver riadkoch power 7 pri relative prahu `1e-10`:

- `gamma_Euler[7] = 2.8658e-10`;
- `cdm_continuity[7] = 4.6572e-10`;
- `tight_coupling[7] = 1.1663e-9`.

Ich absolútne residualy sú iba `7.85e-16`, `1.08e-15`, `3.44e-16`; všetkých
18 nezávislých holdoutov prešlo, najhorší `Einstein_0i[7]=3.8377e-11`.
Skript preto navrhol iba neautoritatívne
`REVIEW_M1_ORDER7_CORE_OR_HOLDOUT_UNCLOSED`. Vecný výsledok resetuje active
technický counter na `0/10`; význam troch riadkov ešte posúdia audity.

## Autoritatívny rozsudok

`PASS_M1_ORDER7_REGRESSION_SHAPE_RANK_ANCHOR_CONDITION_STATE_AND_HOLDOUT_ONLY /
REVIEW_M1_ORDER7_POWER7_DRIVER_PRECISION_FLOOR_UNCLOSED`.

Tri power-7 fail riadky sa nesmú spätne prehlásiť za PASS, ale nepreukazujú
fyzikálny rozpor. Support step 3 zostáva blokovaný; ďalší krok je samostatný
precision/boundary-closure audit podľa dokumentu 65.
