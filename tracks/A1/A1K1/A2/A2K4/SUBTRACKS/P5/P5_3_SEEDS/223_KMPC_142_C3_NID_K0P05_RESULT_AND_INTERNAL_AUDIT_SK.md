# Interný audit C3 NID/k=0.05 — KMPC-142

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.05`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autorita dokumentu:** interný audit hlavného orchestrátora  
**Výsledok:** `REVIEW_C3_NID_K0P05_AUDIT_M3_DRIVER_BOUNDARY`  
**Globálny C3 register:** `35/45 PASS`, bez prírastku  
**K4 score effect:** `NONE`, ostáva `60/100`

**Účtovné erratum 2026-07-19:** počas tohto REVIEW bol mode-local stav
`NID 5/9`, nie `3/9`; tri historical nominal atómy a dva `.005` nulové
atómy už boli PASS. Globálny stav `35/45` a REVIEW verdikt sa nemenia.

## 1. Autoritatívny záver

KMPC-142 technicky dokončil úplný NID/.05 nulový pár, ale oba nové logické
atómy ostávajú REVIEW:

| atóm | jediná nepravdivá brána | autoritatívny stav |
|---|---|---|
| `NID/k=0.05/gamma0` | audit `[0,7]` M3 driver | REVIEW |
| `NID/k=0.05/af0` | audit `[0,7]` M3 driver | REVIEW |

Historický nominal atóm KMPC-053 ostáva PASS. NID mód preto ostáva `5/9`
a globálne C3 `35/45`; nevznikol fyzikálny STOP.

Immutable raw:

`scripts/results/k_mpc_005/RUN_KMPC_142_P5_3G7_C3_NID_K0p05_ZERO_VARIANT_PAIR.json`

SHA-256:
`95CC95E96E04E32A3EB98FEA3A7EBD5E6D64A36A43A34B1143C778DE662A76D2`.

## 2. Technická a schema línia

Pôvodný KMPC-131 smoke odhalil PF-127 pred fyzikou: legacy loader odmietol
správny šesťpoľový KMPC-053 identity objekt pre whole-object equality.
Nevznikol raw ani solver call. KMPC-142 potom pridal iba fail-closed exact
schema adapter. Jeho compile `5/5`, zúžený help a smoke `4/4` prešli pri
`physics_executed=false`.

Official KMPC-142 skončil za `4.422 s < 9.0 s`. Workery skončili za:

| worker | runtime |
|---|---:|
| `gamma0/accepted` | `1.937 s` |
| `gamma0/audit` | `2.735 s` |
| `af0/accepted` | `2.078 s` |
| `af0/audit` | `2.906 s` |

Všetkých osem contract checks a sedem worker-parity checks je pravdivých.
Nominal SHA, presný šesťpoľový identity objekt, support `[0,5]→[0,7]`, M1
depth 7, source hashe a frozen prahy sa zhodujú s predregistráciou 222.

## 3. Jediný fyzikálno-numerický blocker

Accepted `[0,5]` solve prešiel v oboch variantoch. Audit `[0,7]` má plný
rank `104/104`, finite riešenie, F0 PASS a nezávislý holdout PASS, ale M3
driver tesne prekročil `1e-10`:

| variant | accepted M3 driver | audit M3 driver | limit | audit worst row |
|---|---:|---:|---:|---|
| `af0` | `1.8225e-11` | `1.3994e-10` | `1e-10` | `fuel_Euler[7]` |
| `gamma0` | `2.7604e-11` | `1.9348e-10` | `1e-10` | `fuel_continuity[7]` |

Audit independent holdout je `3.5980e-11` pre `af0` a `3.7904e-11` pre
`gamma0`, teda pod `1e-9`; holdout rows neboli pridané do driver solve.
F0 audit driver maximá sú `2.7936e-14/2.8196e-14` a prešli.

## 4. Ostatné brány

Oba varianty majú PASS pre frozen contract, nominal reference, B1/TCA0,
M1, accepted solve, combined-Rfs, common, tail, background, null limit a
logical accounting mimo audit M3 drivera.

| metrika | af0 | gamma0 | limit |
|---|---:|---:|---:|
| M3 common max rel. | `1.3282e-10` | `1.0436e-10` | `1e-8` |
| tail envelope max | `1.01361e-16` | `1.01361e-16` | `1e-6` |
| background worst rel. | `0.0` | `0.0` | `1e-12` |

`af0` nominal coefficient bridge aj nulový limit prešli; `gamma0` nulový
limit prešiel. REVIEW preto nesmie byť interpretovaný ako problém tailu,
supportu, holdoutu alebo rovníc.

## 5. Cause-derived nástupca

Jediný predregistrovateľný nástupca je lokálny same-matrix refinement oboch
audit rank-104 M3 solve. Smie použiť presne tri korekcie na identickej
equilibrated matici a RHS, rovnaký mechanizmus ako úspešný KMPC-133.
Accepted solve sa nerefinuje. Support, M1, rows, unknowns, `rcond`, prahy,
varianty a všetky ostatné brány sa nesmú meniť.

Refined stav sa smie vybrať iba ak je konečný, relative driver residual sa
zlepší a absolute-fallback residual sa nezhorší. Ak oba driver residualy
neklesnú pod `1e-10` alebo sa poškodí iná brána, NID/.05 ostáva REVIEW a
ďalší krok sa musí odvodiť z nového immutable rawu.
