# P5.3g7-M3-FULL/R-A — pokus 6/10, technický timeout

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-027`  
**Autoritatívny technický výsledok:** `TECHNICAL_TIMEOUT_MODE_SHARD`  
**Fyzikálny výsledok:** žiadny  
**K4:** `LIVE / REVIEW_TECHNICAL_UNRESOLVED`, hĺbka bez zmeny `60/100`  
**Counter:** `6/10`

## Čo prešlo

| Fáza | Výsledok |
|---|---|
| frozen shell hash | PASS |
| base + runner `py_compile` | PASS, 0.9 s |
| CLI help | PASS, 0.8 s |
| smoke AD/`k=0.05`/nominal/primary | **PASS 12/12**, interný čas 0.813 s, celý proces 2.7 s |

Smoke potvrdil frozen B1/Bianchi referenciu, presnú produkčnú TCA0
redukciu, M1, F0/M3 rank a driver, `00/0i` holdout, actual contract,
spectator-order guard a konečnosť v tomto úzkom rozsahu. Smoke nie je
fyzikálny verdict celej podbrány.

## Kde a prečo pokus skončil

Prvý plný AD mode shard mal vykonať tri `k`, tri varianty a primary/J+2.
Interný limit 4.8 s sa vyčerpal počas zostavovania rozšírenej holdout matice
v `_solve_m3`; proces skončil fail-closed pred výsledkovým AD JSON. Ostatné
módy sa správne nespustili.

Immutable failure evidence:

```text
scripts/results/k_mpc_005/
RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_AD_TECHNICAL_FAILURE.json
SHA-256 6AB1CB51F528B4A7CBD67B0BF57027A3CA0F742916C7D62DE00E5BEE2220A475
```

Traceback ukazuje `TimeoutError: KMPC-027 AD internal deadline exceeded` v
cooperative deadline checku `_affine_system`, nie rank, rezíduum alebo
fyzikálny rozpor. Failure evidence pozná mód AD, ale neexportuje presný
aktuálny `k/variant`; to je samostatná auditná slabina PF-068.

## Rozsudok

```text
ATTEMPT_6 = TECHNICAL_TIMEOUT
PHYSICS_ATTEMPTS = 0
NO_DEATH_VERDICT
NO_SCORE_OR_DEPTH_CHANGE
NO_RELEASE_TRIGGER
```

Runner 271 sa nesmie znovu spúšťať s `--mode`: rovnaký mode-shard rozsah je
pri povinnom limite preukázane príliš široký. `--smoke` ostáva iba
regresnou diagnostikou, nie cestou k verdictu.

## Povolený pokus 7

Pokus 7 smie zmeniť iba technickú granularitu:

- jeden proces = jeden `mode × k × variant`, stále primary aj `J+2`;
- rovnice, state/driver/holdout, prahy, podpory a hashe fyzikálnych zdrojov
  sa nemenia;
- každý subshard exportuje `mode`, `k`, `variant`, poslednú dokončenú fázu a
  immutable failure evidence;
- následný módový a globálny agregátor fail-closed overí úplnosť všetkých
  `5×3×3=45` subshardov a cross-mode background.

Ak aj jeden taký subshard prekročí limit, pokus 7 skončí technicky. Nie je
dovolené zvýšiť timeout alebo zúžiť fyzikálny test po zhliadnutí výsledku.
