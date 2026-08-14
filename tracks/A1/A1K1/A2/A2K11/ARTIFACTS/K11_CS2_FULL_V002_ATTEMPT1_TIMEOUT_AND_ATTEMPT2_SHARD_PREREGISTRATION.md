# K11-CS2 full v002 — pokus 1 timeout a predregistrácia sharded pokusu 2/10

**Dátum:** 2026-07-16  
**Architektúra:** `ARCH-A / K11-TC-A3`  
**Counter po pokuse 1:** `1/10`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`

## 1. Výsledok pokusu 1

Smoke `L=4` prešiel. Full proces vypočítal a zapísal payload s verdiktom

```text
PASS_ARCH_A_ATTEMPT_1_EXACT_SET_INTERIOR_AND_REGISTERED_TRUNCATION_ONLY
```

a interným časom `3.25 s`, ale celý proces vrátane importu CAMB/SymPy
prekročil vonkajší limit: `exit 124`, wall približne `10.9 s`. Podľa
metodiky preto payload nie je autoritatívny PASS. Ostáva zachovaný ako
diagnostický dôkaz.

**Kategória:** `PYTHON_OR_DEPENDENCY_FAILURE / EXTERNAL_RUNTIME_BUDGET`  
**Dôvod:** súčet import overheadu a troch `lmax` algebraických sweepov
presiahol 10 s; nejde o nenulový fyzikálny alebo algebraický rezíduál.

## 2. Technická oprava v pokuse 2

Base fyzika, state contract, closure metadata ani prahy sa nemenia. Nový
runner iba rozdelí presne ten istý sweep na tri procesy:

```text
L=4 -> RUN_A2_K11_CS2_FULL_V002_ATTEMPT2_L4.json
L=6 -> RUN_A2_K11_CS2_FULL_V002_ATTEMPT2_L6.json
L=8 -> RUN_A2_K11_CS2_FULL_V002_ATTEMPT2_L8.json
```

Každý proces má vnútorný limit 5 s a vonkajší 10 s. Runner importuje ťažký
base až po spracovaní CLI, takže `--help` zostane ľahký. Pôvodný runner 266
a oba jeho JSON výstupy sa nemenia.

## 3. Očakávanie pred behom

| Shard | Počet stavov | Očakávaný algebraický výsledok | Vonkajší výsledok |
|---|---:|---|---|
| `L=4` | 25 | všetky checks PASS, presné rezíduá nula | exit 0 pod 10 s |
| `L=6` | 33 | všetky checks PASS, presné rezíduá nula | exit 0 pod 10 s |
| `L=8` | 41 | všetky checks PASS, presné rezíduá nula | exit 0 pod 10 s |

**PASS pokusu 2:** všetky tri immutable shardy exit 0, rovnaký autoritatívny
scope verdict a zhodné source hashes. Potom sa counter zapíše ako `2/10`
(jeden neúspešný a jeden úspešný balík), bez fyzikálnych bodov.

**Technický FAIL:** ktorýkoľvek timeout/import/exit problém zvýši counter na
`2/10` ako druhý neúspech a zachová presný shard. Algebraický nesúlad sa
nesmie maskovať shardovaním.

**Po PASS:** ďalšia brána je full thermal/TCA/DAE implementácia a až potom
skutočný `lmax`/closure-family evolučný konvergenčný test.

## 4. Nový artefakt

```text
scripts/267_script_A2_K11_CS2_full_v002_structural_truncation_shard.py
```

