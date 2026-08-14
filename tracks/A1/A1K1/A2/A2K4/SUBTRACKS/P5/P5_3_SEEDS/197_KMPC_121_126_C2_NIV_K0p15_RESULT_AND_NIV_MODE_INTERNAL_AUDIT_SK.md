# KMPC-121–126 — C2 NIV/k=.15 a uzavretie NIV módu: interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Interný auditor a autoritatívny zápis:** Codex (OpenAI)  
**Stav:** `INTERNAL_AUDIT_PASS / NIV_MODE_CLOSED / C2_ATOMS_10_OF_10`  
**Autoritatívny scoped verdict:**
`PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_MULTI_RANK_REFINEMENT`  
**Dopad:** C2 atómy `9/10→10/10 PASS`; povinný read-only C2 aggregate ešte
`NOT_RUN`; K4 zostáva `LIVE / 60/100`; active technical counter `0/10`

## Immutable evidence

| Beh | Rola | SHA-256 | Stav/candidate |
|---|---|---|---|
| KMPC-121 | nominal `[-1,4]→[-1,6]` | `8E5E8107833C9F2858BA180F9DBC3DFA4037566CCC2F7D30AF819B1FC94C0BEE` | core + tail REVIEW |
| KMPC-122 | nominal-support same-matrix core closure | `BAC68E1D85802852EEBF4B1AC2E277EC15FD32264E166F673D486FD747869419` | tail-only REVIEW |
| KMPC-123 | verdict-free widened checkpoint attempt | `D3B31093D84156D05BF4EE8EC707D53B5D653DE5700289E6EA68627674898DC8` | `checkpoint_complete=false`, no verdict |
| KMPC-124 | resume smoke | bez success raw | PF-114, exit 2 pred fyzikou |
| KMPC-125 | first wider-support refinement | failure SHA `1ED339AE9FBA7BA27C066A659926B0B822029F8BC3CF0AE4844DF4845E3A31D0` | PF-115, no verdict |
| KMPC-126 | explicit rank-104/130 refinement | `1D46AFD1CDEB650A7787A5E6FE9E2304A5212FF1FE9AA47657BEAAAA557B8AA0` | PASS candidate |

## Fyzikálny nález a technická história

KMPC-121 prešiel M1, accepted, common, S-C0, background a independent
holdout. Audit false bol iba M3 `fuel_Euler[6]=1.62542e-10 >1e-10`; tail
na `.01` bol F0 `1.80841e-6` a M3 `2.25684e-6`. KMPC-122 na presne tej
istej 104×104 nominal audit matici znížil driver na `1.51686e-16`, pričom
holdout ostal `4.25308e-12`; tail-only REVIEW preto oprávnene otvoril
`[-1,6]→[-1,8]`.

KMPC-123 ukázal, že fresh widened accepted rank-104 solve má vlastnú
boundary `1.48191e-10`; checkpoint preto správne nemal complete flag.
KMPC-124 tento stav odmietol pred restore. KMPC-125 následne odhalil, že
historický refinement post-processing podporoval iba rank 104, kým widened
audit je rank 130. Jeho failure raw nenesie fyzikálny verdikt.

Versioned successor KMPC-126 explicitne zmrazil target ranky `{104,130}`.
Smoke behaviorálne otestoval oba ranky a official publikoval samostatnú
exact-same-matrix provenance pre accepted aj audit. Rovnice, matice, pravé
strany, support, `rcond`, prahy a holdout definícia sa nezmenili.

## KMPC-126 rozhodovacie hodnoty

| Kontrola | Hodnota | Prah/audit |
|---|---:|---|
| M1 driver / holdout | `1.29883e-14` / `1.06157e-14` | PASS |
| accepted M3 baseline → after | `1.48191e-10→1.72471e-16` | `<1e-10`, PASS |
| audit M3 baseline → after | `1.41683e-7→2.13943e-16` | `<1e-10`, PASS |
| accepted/audit rank | `104/104`, `130/130` | PASS |
| audit independent holdout | `9.60602e-11` | `<1e-9`, PASS |
| common F0 / M3 | `9.69572e-14`, `8.36630e-14` | `<1e-8`, PASS |
| tail F0 `.01` | `2.80666e-12` (`delta_f`) | `<1e-6`, PASS |
| tail M3 `.01` | `3.40284e-12` (`U_f`) | `<1e-6`, PASS |
| background worst | `3.45586e-16` | `<1e-12`, PASS |

False-check množiny sú prázdne. Holdout riadky neboli pridané do driver
solve. Multi-rank provenance guard, source hashes, owners, 13-state order,
forbidden-layer/stress a production contract prešli.

## Autoritatívne rozhodnutie

Interný audit prijíma scoped NIV/k=.15 PASS s accepted `[-1,6]`, audit
`[-1,8]`, M1 depth 8. Spolu s dokumentom 190 je celý NIV mód uzavretý.
Desať C2 mode×k atómov má autoritatívny scoped PASS.

Podľa frozen dokumentu 104 to ešte nie je finálny C2 gate verdict:
read-only agregát musí overiť exact kartézsky register, hashe, identity,
všetky brány a cross-mode/cross-k background spread. Agregát nič znovu
nerieši a nemení atómové skóre; iba odblokuje C3.

## Nonclaims a ďalší krok

Výsledok nepotvrdzuje C2 aggregate, C3 `gamma0/af0`, fyzickú S-M paru,
P5.4, G8/G9, dáta, A3 ani release. K4 hĺbka ostáva `60/100`.

Najprv sa zapečatí jeden spoločný externý balík pre celý NIV mód
KMPC-118–126 vrátane PF-114/115. Potom sa predregistruje read-only C2
aggregate successor nad desiatimi autoritatívne vybranými atómovými rawmi.
