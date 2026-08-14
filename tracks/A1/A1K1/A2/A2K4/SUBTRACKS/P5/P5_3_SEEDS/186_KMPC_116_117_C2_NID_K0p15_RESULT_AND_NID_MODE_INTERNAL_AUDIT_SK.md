# KMPC-116–117 — C2 NID/k=.15 a uzavretie NID módu: interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Interný auditor a autoritatívny zápis:** Codex (OpenAI)  
**Stav:** `INTERNAL_AUDIT_PASS / NID_MODE_CLOSED`  
**Autoritatívny verdict:**
`PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_SAME_MATRIX_REFINEMENT`  
**Dopad:** C2 `7/10→8/10 PASS`; oba NID k-body uzavreté; K4 zostáva
`LIVE / 60/100`; active technical counter `0/10`

## Immutable evidence

| Beh | Rola | SHA-256 | Candidate |
|---|---|---|---|
| KMPC-116 | NID/k=.15 nominal `[0,5]→[0,7]` | `0965E3D1F7726CC851B3D1B6043468169ADEBED44096B010565F768DBD8E25AB` | `REVIEW_C2_CORE_GATE_UNCLOSED` |
| KMPC-117 | tri same-matrix residual corrections | `F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4` | `PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY` |

## Rozlíšenie fyziky od numerickej hranice

KMPC-116 mal M1 PASS, accepted `[0,5]` PASS, audit rank `104/104`, F0 PASS,
common/tail/S-C0/background PASS a independent holdout PASS. Jediný false
check bol audit `M3_driver`; worst `gamma_Euler[7]` mal relative residual
`4.1865589368e-10` oproti frozen prahu `1e-10`. Holdout maximum bolo iba
`6.5626998417e-11 < 1e-9`. To je predregistrovaná same-matrix numerical
boundary, nie support alebo invariantný fyzikálny rozpor.

KMPC-117 znovu použil presne ten istý 104×104 driver a constant. Tri
corrections nemenili equation builder, support, rank, `rcond`, prah ani
holdout. Provenance uvádza:

| Kontrola | Hodnota | Audit |
|---|---:|---|
| matrix identity | `EXACT_SAME_MATRIX_AND_CONSTANT` | PASS |
| iterations | `3` | PASS |
| selection rule | `true` | PASS |
| driver relative pred | `4.1865589368e-10` | nad `1e-10` |
| driver relative po | `1.3513985475e-16` | PASS |
| absolute fallback pred | `9.8320546618e-15` | diagnostika |
| absolute fallback po | `9.8607613153e-32` | nezhoršené / PASS |
| independent holdout po | `1.4373221568e-11` | `<1e-9`, PASS |

V KMPC-117 je false-check množina prázdna. M1, accepted/audit solve, ranks,
forbidden-layer/stress, production contract, combined-`R_fs`, frozen B1,
S-C0, common, tail a background prešli. Najhorší common rozdiel je F0
`3.7511e-14` a M3 `2.1161e-10 < 1e-8`. Na `z=.01` je F0 tail
`1.2342e-7` a M3 tail `6.8291e-8`, oba pod `1e-6`; background worst
`3.4559e-16 < 1e-12`.

## Autoritatívne rozhodnutie

Interný audit prijíma scoped NID/k=.15 PASS. Spolu s dokumentom 183 je tým
uzavretý celý NID mód na oboch frozen k-bodoch:

- NID/k=.005: accepted `[0,7]`, audit `[0,9]`, PASS;
- NID/k=.15: accepted `[0,5]`, audit `[0,7]`, PASS po same-matrix
  refinement.

C2 sa zvyšuje na `8/10`. Nezvyšuje sa fyzikálna hĺbka K4 `60/100`, pretože
P5.3 ešte nemá oba NIV atómy a P5.4/G8 nebežali.

## Nonclaims a ďalší krok

Výsledok nepotvrdzuje NIV, S-M, ODE/P5.4, plnú hierarchiu G8, likelihood G9,
dáta, A3 ani release. Externý balík EA-027 musí auditovať KMPC-116/117 a
same-matrix identitu. Po jeho zapečatení je ďalší frozen atóm
`NIV/k=.005/nominal`, accepted `[-1,4]`, audit `[-1,6]`, M1 depth 6, s
rovnakými prahmi a stabilným single-atom adapterom.
