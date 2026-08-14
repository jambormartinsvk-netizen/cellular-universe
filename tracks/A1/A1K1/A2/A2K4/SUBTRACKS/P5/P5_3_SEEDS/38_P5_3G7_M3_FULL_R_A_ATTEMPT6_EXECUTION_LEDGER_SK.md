# P5.3g7-M3-FULL/R-A — pokus 6/10, vykonávací ledger

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-027`  
**Autoritatívna predregistrácia:** dokument 37  
**Stav:** `ATTEMPT_6_TECHNICAL_TIMEOUT / CLOSED / PHYSICS_NOT_RUN`  
**Fyzikálna hĺbka:** bez zmeny, `60/100`

## Nemenné pravidlo

Každý Python proces je ešte pred spustením opísaný v tomto ledgeri:
ľudský význam, očakávaný výsledok, PASS pokračovanie a STOP/REVIEW vetva.
Vnútorný limit runnera je najviac 5 s, vonkajší limit každého procesu 10 s.
Celý sled je jediný technický pokus `6/10`.

## Fázy

| Fáza | Čo sa počíta | Očakávanie pred behom | Ak prejde | Ak neprejde | Výsledok |
|---|---|---|---|---|---|
| hash freeze | iba shell SHA-256, bez Pythonu | presná zhoda s dokumentom 37 | povoliť compile | neotvoriť pokus | PASS |
| `py_compile` | syntax shared modulu a runnera; bez fyziky | exit 0, ticho, do 10 s | CLI help | technický STOP pokusu 6; K4 ostáva živá | **PASS, 0.9 s** |
| `--help` | argparse CLI kontrakt; bez importu fyzikálneho modulu a bez solve | exit 0; voľby `--smoke/--mode/--aggregate`, runtime a output | smoke | technický CLI STOP | **PASS, exit 0, 0.8 s** |
| smoke | AD, `k=0.05`, nominal, primary; contract+B1+TCA0+M1+F0+M3+holdout | všetky smoke checks true, do 5 s interne/10 s externe | päť shardov | technický alebo numerický REVIEW; bez fyzikálnej smrti | **PASS 12/12, interný čas 0.813 s, proces 2.7 s** |
| shard AD | tri k × nominal/gamma0/af0 × J/J+2 | frozen checks true; immutable JSON | CDI | zachovať failure JSON, zastaviť balík | **TECHNICAL_TIMEOUT po 4.8 s internom limite; failure JSON zachovaný** |
| shard CDI | rovnaký kontrakt pre CDI | checks true | BI | zachovať failure JSON, zastaviť balík | NOT_RUN |
| shard BI | rovnaký kontrakt pre BI | checks true | NID | zachovať failure JSON, zastaviť balík | NOT_RUN |
| shard NID | rovnaký kontrakt pre NID | checks true | NIV | zachovať failure JSON, zastaviť balík | NOT_RUN |
| shard NIV | rovnaký kontrakt pre NIV | checks true | aggregate | zachovať failure JSON, zastaviť balík | NOT_RUN |
| aggregate | iba proveniencia, úplnosť a cross-mode background; nový solve nie | 5 immutable shardov, všetky PASS, zhodné hashe/prahy | výsledkový audit | REVIEW; žiadny fyzikálny STOP bez analýzy | NOT_RUN |

## Predbehový zápis nasledujúcej fázy: CLI help

Runner má iba vypísať deklarované prepínače. Očakáva sa exit `0` a žiadny
import fyzikálneho modulu, solve ani výsledkový JSON. PASS povoľuje smoke.
CLI výnimka alebo timeout uzatvoria pokus 6 ako technické zlyhanie;
nevypovedajú o fyzike K4.

## Predbehový zápis nasledujúcej fázy: smoke

Smoke importuje frozen zdroje, porovná hashe a pre `AD`, `k=0.05` vyrieši
iba nominal primary M1+F0+M3. Očakávame presný B1/TCA0 guard, M1 PASS, plný
F0/M3 rank, driver a `00/0i` holdout v tolerancii, actual contract paritu,
spectator-order guard a konečný stav. Interný limit je 4.5 s, vonkajší 10 s.
Ak prejde, spustia sa shardy. Ak nie, nejde sa ďalej: výsledok je technický
alebo numerický REVIEW podľa presnej príčiny, bez smrti K4.

## Predbehový zápis nasledujúcej fázy: shard AD

AD shard vykoná tri dynamické `k`, pre každý nominal, `gamma=0` a `A_f=0`,
pričom primary aj `J+2` sú skutočné nové solve. Očakávame všetky frozen
checks true a nový immutable AD JSON. Smoke naznačuje vyššiu pracovnosť;
limit sa však nemení: 4.8 s interne, 10 s externe. Ak deadline nestačí,
ide výhradne o `TECHNICAL_TIMEOUT` pokusu 6 a nasledujúci pokus smie iba
jemnejšie shardovať tú istú fyziku. Timeout nie je numerický ani fyzikálny
FAIL.

## Uzavretie

AD full-mode shard prekročil interný limit počas extended holdout matrix.
CDI/BI/NID/NIV ani aggregate sa nespustili. Autoritatívny výsledok a ďalší
krok sú v dokumente 39.
