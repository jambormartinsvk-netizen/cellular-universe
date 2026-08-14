# KMPC-131 — C3 NID/k=0.05 nulový pár

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.05`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

## 1. Rozsah a jediný dovolený výpočet

Táto jednotka overí dva podmienené C3 atómy
`NID/k=0.05/gamma0` a `NID/k=0.05/af0`. Historický nominal atóm sa
neprepočítava. Použije sa jeho immutable autorita KMPC-053 a frozen
KMPC-131 four-support-shard runner. Nový runner, nový vedecký base ani
zmena fyzikálneho kontraktu nevznikne.

Štyri izolované shardy sú:

```text
gamma0 × accepted [0,5]
gamma0 × audit    [0,7]
af0    × accepted [0,5]
af0    × audit    [0,7]
```

Každý worker má vlastný interný limit `4.8 s`; parent iba validuje `4/4`
payloady, zostaví common/tail/null/bridge brány a má wall guard `9.0 s`.
Vonkajší process limit ostáva `10 s`. Shardy nie sú samostatné fyzikálne
atómy.

## 2. Frozen nominal a support kontrakt

| položka | frozen hodnota |
|---|---|
| mód / k | `NID / 0.05` |
| nominal autorita | `RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json` |
| nominal SHA-256 | `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD` |
| nominal run / candidate | `KMPC-053 / PASS_NID_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY` |
| schema | `solved_supports`, accepted key `05`, audit key `07` |
| support authority | `C1_DIRECT_SCOPED_PASS` / interný audit dokument 98 |
| accepted / audit support | `[0,5] / [0,7]` |
| M1 depth | `7` |

Interný audit 98 udelil nominal výsledku
`PASS_NID_SUPPORT_05_ADEQUATE_AT_K005_NOMINAL`. Common maximá boli
`4.13e-15/1.11e-10 < 1e-8`; refined driver maximum `1.62e-16`, holdout
`2.62e-11` a tail maximá pri `z=.01` boli `F0=3.14e-9` a `M3=1.68e-7`
voči `1e-6`. Tieto hodnoty dokazujú nominal support autoritu, ale
nepredpovedajú automaticky nulové varianty.

KMPC-127 C2 aggregate SHA
`CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F`
ostáva povinným globálnym shared guardom. NID/.05 nie je jedným z jeho
desiatich endpoint atómov; lokálna nominal autorita je preto explicitne
KMPC-053, nie vymyslený aggregate atóm.

## 3. Frozen prahy a vetvy

Bez zmeny ostávajú driver `1e-10`, independent holdout `1e-9`, common
accepted→audit `1e-8`, cancellation-safe tail `1e-6`, absolute fallback
`1e-12` a background `1e-12`.

- `PASS candidate`: oba varianty technicky dokončia všetky shardy a všetky
  core, common, tail, background, null-limit, bridge a logical-atom brány
  sú pravdivé.
- `REVIEW candidate`: receipt je technicky úplný, ale aspoň jedna frozen
  fyzikálna brána je nepravdivá. Ďalší krok sa smie odvodiť iba z presne
  pomenovanej zlyhanej brány; prahy ani support sa spätne neupravujú.
- `TECHNICAL FAILURE / NO VERDICT`: worker/runtime/identity/hash/schema
  zlyhanie alebo neúplný pair. Failure raw sa zachová bez fyzikálneho
  REVIEW či STOP verdiktu.

Skriptový candidate nie je autoritatívny verdikt. Ten smie vzniknúť až v
samostatnom internom audite immutable rawu.

## 4. Predregistrovaný postup a runtime kontrola

`compile runner → help → NID/.05 four-worker smoke → NID/.05 official`.

Smoke nesmie spustiť solver ani zapísať raw. Official beh smie vytvoriť
práve jeden z výstupov:

`scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NID_K0p05_ZERO_VARIANT_PAIR.json`

alebo príslušný immutable technical-failure receipt. Pred predregistráciou
neexistoval ani jeden, takže nehrozí prepísanie histórie.

Rovnaký support/depth kontrakt dokončil frozen KMPC-131 pre CDI/.05 za
`4.500 s` a BI/.05 za `4.329 s`; NID/.005 s hlbším `[0,7]→[0,9]` skončil
za `5.281 s`. Ide iba o technický runtime precedens, nie o fyzikálnu
predikciu NID/.05.

## 5. Source freeze

| artefakt | SHA-256 |
|---|---|
| frozen scientific/pair base | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| frozen four-support-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| frozen runner `375/KMPC-131` | `45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal. Predregistrácia a source
freeze sú dokončené pred compile, smoke aj official behom a odteraz sa
nemenia. Externý auditný balík vznikne až po uzavretí alebo pomenovanom STOP
celého NID módu.
