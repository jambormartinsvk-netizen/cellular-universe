# KMPC-033 — S-C0 numpy-scalar RERUN1 execution ledger

**Stav:** `TECHNICAL_COMPLETE / PENDING_INDEPENDENT_AUDIT`  
**Interný limit:** `4.8 s`  
**Vonkajší limit:** `10 s` na proces

## Ľudský význam

Najprv sa overí, že úzka oprava vie bezpečne prečítať oba typy desatinného
čísla. Až potom sa zopakuje rovnaký vecný audit ako KMPC-032. Ak prejde,
neznamená to objavenie mikrofyziky pary; znamená to iba, že podmienené
spoločné neutríno–para rozdelenie je algebraicky kompatibilné s existujúcimi
lower-moment M1 koeficientmi.

## Procesy a vopred určené očakávania

| Fáza | Proces | Očakávanie | Pri PASS | Pri odchýlke | Stav |
|---:|---|---|---|---|---|
| 1 | `py_compile` overlay | ticho, exit 0 | fáza 2 | technický fail | `PASS; exit 0; 0.5 s` |
| 2 | `py_compile` runner 277 | ticho, exit 0 | fáza 3 | technický fail | `PASS; exit 0; 0.5 s` |
| 3 | `--help` | CLI usage, exit 0 | fáza 4 | technický fail | `PASS; exit 0; 0.5 s` |
| 4 | `--smoke --max-runtime-seconds 4.8` | builtin/numpy exact parity a pôvodný contract smoke PASS; bez JSON | fáza 5 | technický fail; audit zakázaný | `PASS; smoke_pass=true; 1.1 s` |
| 5 | `--audit ... --output RUN_KMPC_033...json` | immutable JSON; všetky exact checks podľa dokumentov 52/54 | nezávislý audit | failure JSON alebo scoped formula REVIEW | `PASS_EXECUTION; 20/20; 1.5 s` |

Každý riadok je samostatný Python proces. Hashe v dokumente 54 musia byť
vyplnené pred fázou 1.

## Výsledky

Predbehové očakávania sa spätne nemenia. Skutočné výsledky sa doplnia po
každej fáze.

- Fáza 1 prešla podľa očakávania; iba syntax, active counter ostáva `1/10`.
- Fáza 2 prešla podľa očakávania; runner je syntakticky platný, ale
  opravená konverzia sa ešte behaviorálne nevykonala.
- Fáza 3 prešla; CLI obsahuje oddelené smoke/audit, runtime a output.
- Fáza 4 prešla. PF-069 reprodukčný typ je teraz behaviorálne pokrytý:
  builtin a numpy skalár majú exact parity, contract/fixtures zostali PASS a
  V1 helper sa obnovil. Active counter sa ešte nevynuloval, lebo smoke nie
  je vecný výpočet.
- Fáza 5 technicky prešla: `all_checks_pass=true`, 20/20 kontrol a 10/10
  negatívnych fixtures. Všetkých päť M1 systémov malo `rank=unknowns=76`,
  metadata guard PASS a po 21 skutočných lower-moment koeficientoch.
  Immutable JSON SHA-256 je
  `4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C`.
  Script exportoval iba kandidáta; autoritatívny verdikt čaká na tri
  nezávislé read-only posudky a rozhodnutie hlavného audítora.
