# K11-CS2/S0 — predbehový záznam štrukturálnej implementácie

**Dátum:** 2026-07-16  
**Stav:** `RUN001_REVIEW / RERUN1_PASS / S0_CLOSED`  
**Rozsah:** syntax a presná algebra; bez ODE, bez fyzikálneho stability
verdiktu a bez zmeny skóre

## Ľudský opis

Nový base modul má na jednom mieste register všetkých zložiek, presný
K11-R drag, A1 backgroundovú bilanciu a štandardné fotónové,
polarizačné a free-streaming koeficienty. Prvý beh nebude sledovať vývoj
vesmíru. Iba preverí, či sme rovnice a stavový register zapísali formálne a
algebraicky konzistentne.

## Beh 1 — syntax

```text
C:\Python311\python.exe -m py_compile
  scripts/baseScripts/a2_k11_cs2/__init__.py
  scripts/baseScripts/a2_k11_cs2/full_multispecies_constrained_dae.py
  scripts/262_script_A2_K11_CS2_full_multispecies_constrained_DAE_runner.py
```

**Očakávanie:** exit `0`, žiadny traceback.  
**Vonkajší timeout:** `10 s`.  
**PASS:** všetky tri súbory sa skompilujú.  
**STOP implementácie:** syntax/import-time parse chyba; nejde o fyzikálny
STOP koľaje. Pred ďalším Python behom sa chyba opraví a tento dokument sa
aktualizuje.

## Beh 2 — S0 exact structural

Spustí sa iba po PASS behu 1:

```text
C:\Python311\python.exe
  scripts/262_script_A2_K11_CS2_full_multispecies_constrained_DAE_runner.py
  --mode structural --lmax 8 --max-runtime-seconds 5
```

**Vnútorný timeout:** `5 s`.  
**Vonkajší timeout:** `10 s`.

Očakávané presné výsledky:

| Kontrola | Očakávanie |
|---|---:|
| `d_c+d_f-Gamma/H` | presne `0` |
| vážená drag reakcia | presne `0` |
| interaction determinant plus `d_c g/delta` | presne `0` |
| A1 transfer pair sum | presne `0` |
| derivácia backgroundu podľa Fourierovho `k` | presne `0` |
| state count `lmax=4/6/8` | `27/35/43` |
| všetky CAMB `J/G/E` koeficientové rezíduá | presne `0` |
| CAMB polarization source residual | presne `0` |
| `physics_evolution_executed` | `false` |
| `score_effect` | `0` |

### PASS

`PASS_K11_CS2_S0_STRUCTURAL_ONLY`. Potom možno auditovať hashe a dopĺňať
plný RHS, opacity/slip, regulárnu bázu a holdouty v tom istom base module.

### STOP implementácie

Ľubovoľné nenulové symbolické rezíduum, chybný state count, traceback alebo
timeout znamená `STOP_K11_CS2_IMPLEMENTATION_DO_NOT_USE`. Nevydáva sa
fyzikálna smrť K11. Chyba sa zapíše do error ledgeru; povolené sú najviac
dve technické opravy podľa hlavnej CS2 predregistrácie.

### Prekvapivý výsledok

Ak CAMB alebo SymPy verzia zmení kanonický zápis bez fyzikálnej zmeny,
prahy sa neuvoľnia. Najprv sa urobí rozdielový audit zdroja a hashov.

## Záznam po behu 1

```text
exit_code = 0
wall_time  = približne 0.6 s
stdout     = prázdny
stderr     = prázdny
```

Verdikt behu 1: `PASS_K11_CS2_S0_PY_COMPILE`.

Beh 2 uloží nemenný strojový výsledok do
`scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_S0_001.json`. Cesta pred behom
neexistuje; runner odmieta prepísanie existujúceho výsledku.

## Záznam po behu 2 / RUN-001

Exact structural payload sa dokončil za `1.125 s`, všetkých 36 checks je
`true` a JSON má hash
`083314EA810443ED92D2C2C6133627F333955B338E814D8F0BD8D2CE995CED46`.
Vonkajší proces však skončil timeoutom `124`, preto je výsledok iba
`REVIEW_EXTERNAL_EXIT_TIMEOUT`; podrobnosti sú v samostatnom RUN-001 audite.

Pred ďalším Python behom je povolená technická oprava 1/2: skompilovať
runner 263, ktorý nemení base a pri zápise výsledku tlačí iba krátke
zhrnutie. Očakávanie kompilácie: exit `0` do `10 s`; pri neúspechu sa
RERUN1 nespustí.

## Záznam kompilácie technickej opravy 1/2

```text
runner = scripts/263_script_A2_K11_CS2_S0_structural_quiet_output_rerun1.py
SHA-256 = F008465A16681DCECBDDD0A8E1A00B8B4FBC7D0BB3017C75D158D5894291DF45
py_compile exit = 0
wall_time = približne 0.6 s
```

## RERUN1 — očakávanie pred spustením

Výstup:
`scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_S0_002.json`.

- vnútorný limit `5 s`, vonkajší `10 s`;
- rovnaký base hash
  `19263A674E1F342E06E6D0D3999E65E58687CCFF20E5EE083A05D06D7BB107FF`;
- rovnakých 36/36 checks `true` a všetky rezíduá presne `0`;
- `runtime_seconds` očakávane `<5`;
- stdout iba stručný summary, `full_payload_printed=false`;
- shell exit `0`.

Ak sa zmení algebraický payload, nejde o quiet-output paritu a RERUN1
zlyhá. Ak payload prejde, ale shell znova skončí timeoutom, výsledok ostane
`REVIEW_BLOCKED_IMPLEMENTATION` a druhá oprava sa bez lifecycle auditu
nespustí.

## Záznam po RERUN1

```text
internal runtime = 0.828 s
external wall    = 5.3 s
exit             = 0
checks           = 36/36 true
payload parity with RUN-001 except runtime = true
RUN-002 SHA-256  = AD112474E1432DC797B76E05B2FE565ACB3D063F75213359F7CD8CAC92DBE65B
```

Autoritatívny výsledok: `PASS_K11_CS2_S0_STRUCTURAL_ONLY`; bez ODE a bez
bodov. Samostatný výsledkový audit je
`K11_CS2_S0_STRUCTURAL_RESULT_AND_AUDIT.md`.
