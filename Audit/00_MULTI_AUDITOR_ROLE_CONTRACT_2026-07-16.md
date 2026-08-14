# Kontrakt nezávislého trojitého auditu

**Dátum:** 2026-07-16  
**Autoritatívny orchestrátor:** hlavný agent  
**Rozsah:** A2 fyzika, matematické skripty, dokumentácia a release pripravenosť

## Roly

| Rola | Prístup | Povinný výstup | Zakázané |
|---|---|---|---|
| `physics_track_auditor` | read-only | nezávislý Markdown-ready fyzikálny posudok; pri smrti alebo vážnom blockeri nové koľaje odvodené z konkrétnych príčin a rozdiel voči existujúcim | editovať súbory, udeliť autoritatívny verdict, meniť mechanizmus potichu |
| `math_script_auditor` | read-only | nezávislý Markdown-ready audit vzorcov, matíc, skriptov, výsledkov, tolerancií a parity s predregistráciou | editovať/patchovať kód, vydať autoritatívny PASS/STOP, prepísať výsledok |
| `documentation_release_steward` | read-only | kontrolný zoznam povinných dokumentov, histórie, hashov, release triggerov a chýbajúcich väzieb | fyzicky meniť dokumenty, commitovať, publikovať alebo meniť release stav |

## Jediná autorita

Iba hlavný orchestrátor smie:

- udeliť a zapísať `PASS`, `REVIEW`, `STOP` alebo smrť koľaje;
- meniť autoritatívne Markdowny a kód;
- prijať alebo odmietnuť pripomienky nezávislých auditorov s odôvodnením;
- vytvoriť commit, release alebo publikovať na Zenodo.

Subauditorské posudky sú poradné. Ak sa nezhodujú, hlavný agent musí rozpor
zapísať a rozhodnúť podľa dôkazov, nie hlasovaním. Nijaký posudok nesmie
potichu zmeniť už registrovaný rozsudok.

## Povinný predauditný preflight

Pred každým posudkom si každý audítor prečíta v tomto poradí:

1. tento multi-audítorský kontrakt;
2. `tracks/00_READ_FIRST.md`, route register a kontrakt aktívnej koľaje;
3. najnižší aktívny `00_WORK_PLAN.md` a relevantný SK/EN metodický register;
4. pri skriptoch error ledger, karanténu, predregistráciu, base modul,
   runner a immutable výsledok;
5. pri release úlohe release protokol, trigger ledger a changelog.

Posudok musí uviesť prečítané autority, oddeliť dôkaz od inferencie a
zaznamenať vlastný procesný rozpor. Read-only audítor nesmie spustiť výpočet,
meniť súbor ani vytvoriť autoritatívny stav. Jeho mandát je trvalo read-only.

## Hranica rodiny 05

Audítori nesmú navrhovať ani vytvárať nový pracovný dodatok v
`theory/SK` alebo `theory/EN`. Pracovné AR/Q/L delty patria do príslušnej
hĺbky `tracks`; spoločné delty do `tracks/METHODOLOGY/`. Do `theory/` ich
môže konsolidovať iba hlavný orchestrátor pri release candidate podľa AR70.

## Prvé pridelené kolo

Prvé kolo nezávisle kontroluje KMPC-024/PF-058:

1. fyzikálny význam chýbajúcich dynamických `delta_f,U_f`;
2. matematickú a skriptovú paritu RERUN2 s P5.3g7 kontraktom;
3. úplnosť dokumentácie, karantény, histórie a release triggerov.

Výstupy sa po doručení zachovajú v autoritatívnom audite s jasným označením,
ktoré odporúčania hlavný orchestrátor prijal, obmedzil alebo odmietol.
