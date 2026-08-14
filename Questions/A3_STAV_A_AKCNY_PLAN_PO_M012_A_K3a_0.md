# A3/Q20 — stav a akčný plán po M-012 a K3a.0

**Dátum:** 2026-07-13  
**Nahrádza stavovú časť:** `Questions/A2_STAV_A_AKCNY_PLAN_PO_K5_1.md`  
**Historické dokumenty sa nemažú.**

## Aktuálny stav koľají

| Koľaj | Stav | Dôvod/ďalšia brána |
|---|---|---|
| A2-K1 | `MŔTVA M-009` | archivovaná superhorizontová nestabilita |
| A2-K2 | `MŔTVA M-008` | záporná rýchlosť zvuku |
| A2-K3 | `MŔTVA M-010` | superhorizontový relatívny mód |
| A2-K4 | `MŔTVA M-011` | singularita/nestabilita úplného módu |
| A2-K5/K1 | `MŔTVA M-012` | CMB-normalizovaný rast je príliš veľký |
| A2-K5/K3a | `PREŽÍVA K3a.0 — 40/100` | prešla akcia, A1 background a high-k stabilita; čaká `G_eff` |
| K5/K2a, K5/K4a, K5/K6 | `ČAKAJÚ` | záložné koľaje, ak K3a zomrie |

M-012 nemení výsledok K5.1: K5/K1 bola matematicky konzistentná, ale
observačne zlyhala na neskorom raste. Mŕtva koľaj, skripty a dôvod zostávajú
archivované.

## Najbližší fyzikálny krok — K3a.1

1. odvodiť gauge-invariantné lineárne kontinuity, Eulerovu a skalárnu rovnicu
   pre `f=-f1(phi)rho_c+eta Z^2`;
2. odvodiť spoločný kinetický/gradientový systém bez kvázistatického skoku;
3. overiť `eta->0` proti K5/K1 a `f1->0` proti čistej momentum triede;
4. spočítať presné subhorizontové `G_cc`, `G_cb`, `G_bc`, `G_bb` na A1;
5. na grid-e `eta={0,0.1,0.5,1,2,5}` určiť, či existuje zdravý interval
   `G_eff,c<=G` bez post-data rušenia;
6. výsledok označiť `PREŽÍVA N/100` alebo `MŔTVA M-013`;
7. ak K3a zomrie, bez mazania pokračovať K5/K2a.

Piata sila zostáva dovolená, ak ju akcia vynúti. Zakázané je iba vymazať ju
z rovníc alebo pridať nezávislú brzdu po zhliadnutí výsledku.

## Paralelný nerešeršný krok — upratanie dokumentácie

Použiť samostatný plán
`Questions/PLAN_upratania_dokumentacie_GitHub_Zenodo.md`. Do skončenia
inventára a mapy presunov sa fyzikálne dôkazové súbory nepremiestňujú.

## Brány pred vydaním v3.18

1. uzavrieť alebo presne označiť otvorenú K3a.1;
2. dokončiť inventár, mapu kanonických súborov a kontrolu odkazov;
3. vyriešiť neplatný lokálny `.git` bez straty dát;
4. porovnať workspace so vzdialenou vetvou `main`;
5. commitnúť reprodukovateľný release candidate do
   `github.com/jambormartinsvk-netizen/cellular-universe`;
6. zapísať commit hash, tag, changelog, manifest a SHA-256;
7. až potom publikovať nemenný balík na Zenodo.

## Čo sa nesmie urobiť

- oživiť K5/K1 pridaním `eta` pod rovnakým názvom;
- tvrdiť, že K3a.0 už dokázala slabú gravitáciu;
- vybrať `eta` podľa minima `S8` pred odvodením `G_eff`;
- presúvať súbory bez mapy stará cesta -> nová cesta a kontroly odkazov;
- commitnúť `.deps`, `__pycache__`, `*.pyc` alebo neoverené pracovné výstupy;
- publikovať Zenodo skôr než existuje Git commit a changelog.
