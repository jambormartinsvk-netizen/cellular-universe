# KMPC-127 — C2 autoritatívny agregát: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Interný auditor a autoritatívny zápis:** Codex (OpenAI)  
**Stav:** `INTERNAL_AUDIT_PASS / C2_GATE_CLOSED / C3_UNLOCKED`  
**Autoritatívny verdict:** `PASS_C2_FOURIER_COVERAGE_10_OF_10`  
**Dopad:** C2 aggregate `NOT_RUN→PASS`; K4 zostáva `LIVE / 60/100`;
P5 zostáva `3.5/6`; active technical counter `0/10`

## Immutable evidence

| Artefakt | SHA-256 |
|---|---|
| base `c2_authoritative_atom_aggregate.py` | `69E0C35CDC871CEB5185C51D35A3F26D3B26FD4D6117DC443E6E16CB7EEE8EEC` |
| runner 371 / KMPC-127 | `EE25391AC56D561FF7B9E1FFD38F23906772CE763C1EF045EAB56A38F223F6FC` |
| aggregate raw | `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F` |

Pred spustením boli v dokumente 198 zmrazené presné mená, hashe, identity,
candidate hodnoty, brány, spread vzorec, prah aj rozhodovací strom.
Base neimportuje fyzikálny solver a agregát iba číta immutable JSON.

## Execution a negatívny guard

- base+runner `py_compile`: exit `0`, 0.157 s;
- `--help`: exit `0`, 0.148 s;
- behaviorálny smoke: exit `0`, 0.144 s, `4/4` checks;
- fresh-copy register bez KMPC-126: exit `2`, 0.391 s, bez outputu;
- official: exit `0`, wall 0.189 s, interný runtime 0.016 s.

Negatívny test skončil na exact chýbajúcom mene pred vytvorením agregátu.
Žiadna vetva nespustila fyzikálny solve.

## Nezávislý interný audit registra

PowerShell audit znovu načítal všetkých desať pôvodných rawov, vypočítal ich
SHA-256 a porovnal brány mimo Python agregátora.

| Kontrola | Výsledok |
|---|---|
| expected/observed atómy | `10/10` |
| unique exact kartézsky register | `10/10`, PASS |
| exact SHA-256 | `10/10`, PASS |
| identity `mode×k×nominal` | `10/10`, PASS |
| exact povolený PASS candidate a execution status | `10/10`, PASS |
| core/common/tail/background a vnorené background brány | všetky true |
| technical-failure output vo výbere | `0` |
| source hash parity | base aj runner PASS |

## Nezávislý prepočet background spread

| a | Veličina | Relatívny spread | Prah | Stav |
|---:|---|---:|---:|---|
| `1e-8` | `D` | `0` | `1e-12` | PASS |
| `1e-8` | `H_Mpc_inverse` | `0` | `1e-12` | PASS |
| `1e-8` | `rho_f_over_rho_r` | `0` | `1e-12` | PASS |
| `1e-8` | `rho_ash_over_rho_r` | `4.60781186570449e-16` | `1e-12` | PASS |
| `3e-8` | `D` | `0` | `1e-12` | PASS |
| `3e-8` | `H_Mpc_inverse` | `0` | `1e-12` | PASS |
| `3e-8` | `rho_f_over_rho_r` | `0` | `1e-12` | PASS |
| `3e-8` | `rho_ash_over_rho_r` | `0` | `1e-12` | PASS |

Najhorší spread je iba `4.61e-16`, približne 2170-krát pod frozen limitom.
Nezávislý prepočet sa zhoduje s rawom na všetkých ôsmich metrikách.

## Autoritatívne rozhodnutie

Interný audit prijíma candidate
`PASS_C2_FOURIER_COVERAGE_10_OF_10_CANDIDATE_ONLY` ako autoritatívny
`PASS_C2_FOURIER_COVERAGE_10_OF_10`. Povinná C2 brána z dokumentu 104 je
uzavretá a C3 je odblokovaná.

Tento PASS nepridáva bod K4 ani P5: agregát nič nové fyzikálne neriešil,
iba potvrdil konzistentnosť desiatich už prijatých atómov. K4 preto ostáva
`60/100` a P5 `3.5/6`.

## Nonclaims a ďalší krok

Výsledok nepotvrdzuje C3 `gamma0/af0`, fyzickú S-M paru, full hierarchy,
finite opacity, P5.4, G8/G9, dáta, A3 ani release.

Najprv sa zapečatí jeden kompaktný externý balík EA-029 pre KMPC-127.
Potom sa pred akýmkoľvek ďalším Python procesom vypracuje samostatný
kontrakt/predregistrácia C3; nesmie sa len odhadnúť z názvu `gamma0/af0`.
