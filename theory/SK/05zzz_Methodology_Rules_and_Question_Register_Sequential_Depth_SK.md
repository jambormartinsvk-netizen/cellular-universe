# Dodatok k 05 — jednotná sekvenčná hĺbka koľají (SK)

**Dátum:** 2026-07-14  
**Obmedzuje:** AR14  
**Nemení:** fyzikálne dôvody smrti ani ich rozsah

## Kontrola duplicity

AR14 správne oddelila skóre od pravdepodobnosti pravdivosti, ale neurčila,
či „najvzdialenejšia zdokumentovaná brána“ musela byť úspešne prejdená a či
museli prejsť všetky medzibrány. AR30 dopĺňa práve túto chýbajúcu sekvenčnú
podmienku; nie je duplikátom AR14.

## AR30 — Skóre je iba najvyššia sekvenčne prejdená kanonická brána

Pre každú koľaj sa používajú rovnaké brány G1–G10 a skóre po desiatkach.
Skóre `N/100` je najvyššia úspešne prejdená brána iba vtedy, ak prešli aj
všetky predchádzajúce brány alebo ich výslovne dokázaná ekvivalencia.

Neskorší no-go, screen alebo kill test:

- môže koľaj fyzikálne zabiť;
- zapisuje sa ako `najhlbšie vykonaný test / brána smrti`;
- nezvyšuje kanonické skóre, ak boli medzibrány preskočené;
- musí zostať spolu so skriptom, výstupom a dôvodom smrti.

Staré medziskóre `25`, `32–42`, `45`, `55`, `59`, `75` sa nemažú z
historických auditov. V aktuálnych tabuľkách sa vedú iba ako starý checkpoint
alebo najhlbšie vykonaný test, nie ako porovnateľná kanonická hĺbka.

## Kanonické brány

| Brána | Skóre | Obsah |
|---|---:|---|
| G1 | 10 | registrovaná odlišná hypotéza |
| G2 | 20 | uzavretý A1 background a ledger |
| G3 | 30 | lokálna akcia alebo úplný kovariantný uzáver |
| G4 | 40 | úplné lineárne rovnice a Einsteinove constrainty |
| G5 | 50 | úplná regulárna superhorizontová báza |
| G6 | 60 | high-k/subhorizontová stabilita celej bázy |
| G7 | 70 | vlastný plný Einstein–Boltzmann a fyzické transfery |
| G8 | 80 | CMB-normalizované spektrá a `sigma8/S8` |
| G9 | 90 | spoločná likelihood a systematiky |
| G10 | 100 | všetky brány verzie a nezávislá reprodukcia |

## Q57 — Prečo má K4 po K4.2 skóre 60/100 a čo jej ešte chýba?

**Stav:** `K4 JE NAJHLBŠIA SEKVENCNE PREJDENÁ A2 KOĽAJ; G7 JE OTVORENÁ.`

K4.1 prešla G5 úplnou regulárnou bázou a K4.2 prešla G6 high-k a
subhorizontovou stabilitou. Staré `59/100` sa preto jednotne prekalibruje na
`60/100`.

K4 nechýba iba napísanie jednej rovnice. G7 vyžaduje celý balík:

1. fotónovú a neutrínovú Boltzmannovu hierarchiu;
2. anizotropný stres a `Phi != Psi`;
3. tight coupling a rekombináciu;
4. úplné regulárne počiatočné módy rozšíreného systému;
5. implementáciu K4 bez nového post-data parametra;
6. constraint, null, gauge/independent-code a konvergenčné testy;
7. fyzické transfery `delta_m(k,z)`.

Až celá G7 dá `70/100` a vstup do A3/G8. `S8` a CMB normalizácia patria do
G8, nie do aktuálneho skóre 60.

## Rekalibračný výsledok

Kanonické skóre K1–K12 je uložené v
`Audit/JEDNOTNA_SEKVENCNA_STUPNICA_HLBKY_A2_A_REKALIBRACIA_K1_K12.md`.
Fyzikálne rozsudky M-008 až M-016 sa rekalibráciou nemenia.

