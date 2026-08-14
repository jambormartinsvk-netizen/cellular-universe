# P5.3g7-M3/TCA0 RERUN2 — predbehový execution ledger

**Dátum:** 2026-07-16  
**Stav pred behmi:** preregistrované, nič ešte nebolo vykonané  
**Vonkajší limit každého Python procesu:** najviac 10 s  
**Vnútorný limit vedeckého runnera:** najviac 5 s

## Samostatné behy a očakávania

| Poradie | Beh | Ľudský význam | Očakávaný výsledok | PASS | Ak neprejde |
|---:|---|---|---|---|---|
| 1 | `C:\Python311\python.exe --version` | overí, že sa volá priamy interpreter, nie Windows alias | Python `3.11.x`, návrat do 10 s | exit 0 a text `Python 3.11` | STOP prostredia; fyzika sa nespustí |
| 2 | `py_compile` overlay V2 | syntax/import-independent kontrola nového base overlay | bez výstupu, exit 0 | exit 0 | overlay `DO_NOT_RUN_TECHNICAL` |
| 3 | `py_compile` runner RERUN2 | syntax runnera a parserových definícií | bez výstupu, exit 0 | exit 0 | runner `DO_NOT_RUN_TECHNICAL` |
| 4 | `--help` | overí CLI bez vedeckého behu | zobrazí `--max-runtime-seconds`, `--phase`, `--output`, `--smoke` | exit 0 a všetky voľby | STOP CLI/proveniencie |
| 5 | `--smoke` | overí presnú elimináciu na malej singularnej matici, jeden reálny AD seed `76/76`, M1 nulu a JSON typy | všetky kontroly true, `SMOKE_PASS`, runtime `<5 s` | exit 0 | oba nové artefakty označiť technicky nepoužiteľné; plný beh zakázaný |
| 6 | plný `m3-tca0` RERUN2 | tri `k`, päť módov, exact background, M1-anchored štandard a frakčný K4 holdout | M1 rozdiel `<1e-14`, štandardná hodnosť `76/76`; ostatné prahy bez zmeny z dokumentu 27 | podľa celej zmrazenej check mapy | vedecký `REVIEW/STOP`; nie ďalší automatický RERUN |

Výsledok plného behu sa zapíše iba do novej immutable cesty
`scripts/results/k_mpc_005/RUN_KMPC_024_P5_3G7_M3_TCA0_RERUN2.json`.
Existujúci KMPC-023 JSON sa nesmie prepísať.

## Priebežný záznam vykonania

| Beh | Pozorovanie | Stav |
|---|---|---|
| priamy interpreter | `Python 3.11.3`, exit 0, približne 0.5 s | PASS |
| `py_compile` V2 overlay | bez výstupu, exit 0, približne 0.6 s | PASS syntax |
| `py_compile` RERUN2 runner | bez výstupu, exit 0, približne 0.6 s | PASS syntax |
| `--help` | všetky štyri povinné voľby prítomné; exit 0, približne 1.3 s | PASS CLI/import |
| `--smoke` | 11/11 kontrol true; reálny AD `76/76`, M1 presne ukotvená; runtime `0.109 s` | `SMOKE_PASS` |
| plný `m3-tca0` | runtime `2.046 s`; M1 a všetky štandardné brány PASS; 21 FAIL vo frakčných holdoutoch/dvojštarte; vznikol immutable JSON | machine `REVIEW_M3_TCA0_UNCLOSED`; audit `STOP_M3_RUNNER_CONTRACT` |

Post-run contract parity zistila, že frakčný stav nemal dynamické
`delta_f,U_f` ani ich dve rovnice. Preto sa 21 FAIL nesmie prehlásiť za smrť
K4. Podrobnosti sú v dokumente 31 a datovanom contract-parity audite.

## Pravidlo zmeny očakávania

Po zhliadnutí výsledku sa žiadny prah nemení. Ak sa ukáže, že očakávanie
`76/76` bolo matematicky nesprávne, runner končí REVIEW a zmena sa najprv
obháji novým architektonickým auditom; tretí opravný suffix nie je povolený.

## Neskoršie obmedzenie

„Tretí opravný suffix“ zostáva zakázaný pre túto legacy architektúru.
Technické chyby PF-055 až PF-060 sa však po novom evidujú ako spoločné
pokusy `1–3/10` a nezabíjajú fyziku K4. Po úplnom B1 ledgeri smie vzniknúť
odlišný R-A preflight bez solve ako pokus `4/10`.
