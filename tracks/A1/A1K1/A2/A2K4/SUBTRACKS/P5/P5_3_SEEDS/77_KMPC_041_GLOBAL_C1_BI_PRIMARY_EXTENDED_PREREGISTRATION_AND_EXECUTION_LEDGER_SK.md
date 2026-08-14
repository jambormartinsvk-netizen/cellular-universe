# KMPC-041 — GLOBAL_C1 BI primary/extended: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / BI`  
**Stav pri predregistrácii:** `AUTHORIZED_NOT_EXECUTED`  
**Identita:** `BI / k=0.05 Mpc^-1 / nominal`  
**Skóre a triggery:** `NONE`

## 1. Účel a hranica prenosu

KMPC-040 uzavrel iba CDI support pri rovnakej škále a variante. Na BI sa
neprenášajú CDI koeficienty, support PASS ani fyzikálny verdikt. Prenáša sa
iba zmrazená R-A architektúra a auditná metóda podľa dokumentu 51.

BI má nezávisle zmrazené:

```text
leading_j = 1
primary   = [0,1]
extended  = [0,3]
```

Immutable prerequisite výsledky:

- S-C0 passport KMPC-033, SHA-256
  `4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C`;
- predchádzajúci coverage uzol KMPC-040, SHA-256
  `69C78F70ECD851D8B8A48E4E09445181C0D4559E9BD2E90A7BA19933351BD219`.

KMPC-040 je iba sekvenčný prerequisite; jeho numerický stav nevstupuje do
BI solve.

## 2. Support, počty a nemenné prahy

| Rola | Support | F0 počet | M3 počet |
|---|---:|---:|---:|
| primary | `[0,1]` | 4 | 26 |
| extended | `[0,3]` | 8 | 52 |

Povinné brány:

- frozen a nezávislý R-A contract, B1 left-null/Bianchi a TCA0 bridge;
- M1 order-5 accepted state;
- F0 aj M3 rank, driver, leading/forbidden/production/regularity a finite;
- nezávislé `Einstein_00/0i` holdouty pre primary aj extended;
- actual S-C0 lift/collapse na BI koeficientoch;
- common koeficienty powers `0,1` osobitne pre F0 aj M3;
- čistý added tail iba powers `2,3` voči baseline power `1`, osobitne pre
  F0 aj M3, na `z={1e-4,1e-2}`.

Prahy ostávajú: common relative `1e-8`, tail relative `1e-6`, absolute
fallback norm/tolerance `1e-12`. Tail je autoritatívne
`sum(abs(c_j)*z**j)` pre `j=2,3`; signed súčet je iba diagnostický. Toto
sprísnenie zabraňuje falošnému PASS z rušenia znamienok a je predregistrované
pred behom. Raw rozdiel dvoch solve zostáva diagnostický.

## 3. Rozhodovací strom

1. Hash/source/runtime/CLI/JSON/write alebo iná technická chyba:
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`.
2. Core, holdout, M1, contract alebo S-C0 FAIL:
   `REVIEW_BI_C1_CORE_GATE_UNCLOSED`.
3. Core PASS, ale common `0,1` FAIL:
   `REVIEW_BI_C1_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`.
4. Core/common PASS, ale tail `2,3` FAIL:
   `REVIEW_BI_C1_SUPPORT_EXTENSION_REQUIRED`. Znamená iba, že primary
   `[0,1]` nestačí; nehovorí, či `[0,3]` remainder prejde.
5. Všetko PASS: `PASS_BI_C1_PRIMARY_EXTENDED_ATOM_CANDIDATE_ONLY`.

Skript nevydáva autoritatívny verdikt. Pri tail FAIL smie ďalší support
`[0,3]→[0,5]` vzniknúť iba v novej predregistrácii. Invariantný core FAIL
nie je fyzikálny STOP bez nezávislej reprodukcie a formulačného auditu.

## 4. Prevádzkový kontrakt

Povolené poradie je `compile → --help → --smoke → jeden --audit`.
Interný limit je presne `4.8 s`, externý najviac `10 s`. Canonical success,
failure a tmp cesty sú exkluzívne; nič sa neprepisuje. Zakázaná je zmena
rovníc, supportu, tolerancií, plôch alebo post-hoc rerun.

## 5. Nonclaims

Bez CDI extrapolácie, NID/NIV, iného `k`/variantu, S-M, full hierarchy,
finite opacity, ODE, P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny skóre,
predikčnej tabuľky alebo release.

## 6. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | používateľ prikázal pokračovať po KMPC-040 | `AUTHORIZED` |
| 2026-07-18 | BI identita, support, metriky, prahy a rozhodovací strom zmrazené | `PREREGISTERED` |
| 2026-07-18 | `py_compile` nového base a runnera | `PASS` |
| 2026-07-18 | runner `--help` | `PASS` |
| 2026-07-18 | smoke: support/prerequisite/JSON/write guardy | `PASS` |
| 2026-07-18 | jediný bounded audit, interný limit `4.8 s` | `TECHNICAL_COMPLETE` |
| 2026-07-18 | canonical JSON zapísaný exkluzívne; failure/tmp nevznikli | `PASS` |
| 2026-07-18 | nezávislý JSON a CDI/BI mode-routing parity audit | dokument 78 |
