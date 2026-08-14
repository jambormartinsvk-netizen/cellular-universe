# A2-K4 / C7.7c — predregistrované očakávania najbližších behov

Dátum: 2026-07-15  
Stav: zapísané pred vytvorením a spustením nástupcov 175/176 a čistého RK4

## P0 — fail-closed nástupca K7b

Typ očakávania: `REGRESSION`.

Povolená zmena je iba validácia existencie a typu `reduced_rank/free_count`. Rovnice, parametre, fyzikálny `mu`, koeficienty, tolerancie a 13 RHS sa nesmú meniť.

### Očakávaný pozitívny beh

| Mód/povrch | D activity rel. | Najhorší stav/allowance | Najhorší RHS/allowance | Očakávaný stav |
|---|---:|---:|---:|---|
| NID/deep | `5.9511e-3` | `9.4022e-6` | `8.5918e-13` | PASS |
| NID/shallow | `1.0921e-4` | `8.0083e-6` | `6.3485e-12` | PASS |
| NIV/deep | nevyžadované | `3.2127e-5` | `3.5503e-11` | PASS |
| NIV/shallow | nevyžadované | `3.8442e-5` | `2.6233e-10` | PASS |

Ďalšie presné očakávania: `fixed_count=30`, `free_count=58`, `reduced_rank=58`, `hard_conflict_count=0`, nulová chyba tvrdých kotiev a fyzikálny register iba z `physical_mu` solve.

Keďže ide o validáciu bez zmeny výpočtu, všetky fyzikálne serializované čísla sa očakávajú bitovo rovnaké ako v autoritatívnom predchodcovi; runtime a poradie nevedeckých JSON kľúčov sú vylúčené. Ak sa fyzikálne číslo zmení, výsledok je `REVIEW_PROVENANCE_CHANGED`, aj keby zostalo pod starým prahom.

### Povinný negatívny kontrolný beh

Synteticky odstrániť každý rankový kľúč samostatne a potom oba. Očakávanie: gate musí zakaždým zlyhať uzavreto a nesmie vyhodnotiť `None==None` ako PASS. Tento test nevykonáva fyziku a nemení skóre.

Časové limity: child najviac 8 s, štvorpovrchový agregátor najviac 15 s interne a najviac 20 s externe; kontrola procesu najneskôr po 10 s.

## P1 — čistý samostatný RK4 regresný prepis

Typ očakávania: `REGRESSION`.

Prvý beh nesmie meniť RHS, seed, škálu, kroky ani closure. Musí odstrániť iba nedosiahnuteľný legacy `solve_ivp` blok a správne pomenovať diagnostické monitory.

Očakávanie reprodukcie:

- 100/200 endpoint rozdiel približne `1.44327e-6`;
- 200/400 endpoint rozdiel približne `3.93124e-6`;
- pomer predchádzajúci/nový v intervale `0.36–0.375`;
- dominantná zložka `M`;
- density residual rádovo `1e-22`, momentum residual rádovo `1e-17`;
- safety maximum približne `1`;
- verdikt stále `REVIEW`, nie PASS.

Prípustná regresná odchýlka endpoint metrík je absolútne `1e-12`; väčšia zmena znamená, že prepis nie je ekvivalentný a musí sa auditovať. Tautologické identity a species kancelácie majú `score_effect: NONE`.

## P2 — nový term ledger M-prime

Typ očakávania: `EXPLORATORY` s kauzálnou hypotézou cancellation.

Stredná hodnota chyby sa nevymýšľa. Očakáva sa však, že ledger ukáže, či `M'` vzniká súčtom veľkých kompenzujúcich členov. Povinné výstupy sú `sum_abs_terms/abs(HP_sum)`, chyba obyčajného súčtu, chyba `math.fsum`, 80-dps referencia a zlepšovací faktor.

- fsum podkoľaj môže prežiť iba pri zlepšení `>=10` na každom aktívnom checkpointe;
- faktor `<10` na ktoromkoľvek aktívnom checkpointe zabíja fsum vysvetlenie pre tento rozsah;
- nefinite hodnota, nesúlad zoznamu členov alebo timeout je REVIEW, nie fyzikálna smrť K4;
- zmena rovníc alebo prahov patrí do novej podkoľaje.

Skript 186 sa nespúšťa a nemení; nový ledger dostane nové číslo.
