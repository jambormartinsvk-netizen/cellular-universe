# Dodatok k 05 — integrita importovaných brán a dosiahnuteľnosť kódu (SK)

Dátum: 2026-07-15  
Stav: záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR39 už všeobecne prikazuje zloženému verdiktu zlyhať uzavreto pri chýbajúcej dátovej ceste. AR45 už zakazuje počítať vynútenú algebraickú identitu ako nezávislý constraint PASS. Nové AR51 preto iba zavádza vykonateľnú kontrolu existencie a typu importovaných polí; AR52 rieši odlišnú medzeru, keď generovaný skript ponechá budúce markery v nedosiahnuteľnom kóde. Tautologické checky nedostávajú nové duplicitné pravidlo, iba konkrétnu aplikáciu AR45 v Q77.

## AR51 — Porovnanie importovaných polí musí najprv dokázať ich existenciu

Brána porovnávajúca dve hodnoty z JSON, registra alebo child výstupu musí pred rovnosťou alebo číselným prahom samostatne overiť:

- existenciu oboch kľúčov na očakávanej ceste;
- očakávaný typ a podľa potreby konečnosť;
- identitu producenta, módu, povrchu a backgroundu, ak ovplyvňujú význam hodnoty.

Samotný vzor `mapping.get(a) == mapping.get(b)` je zakázaný, pretože pri dvoch chýbajúcich kľúčoch vracia `True`. Chýbajúce pole je `REVIEW/FAIL-CLOSED`, nikdy implicitný PASS.

## AR52 — Autoritatívny marker musí ležať na preukázateľne vykonanej ceste

Ak wrapper generuje nový zdroj vložením bloku pred skorý `return`, nesmie ponechať starý solver alebo budúci patchovací marker za týmto returnom ako zdanlivo aktívnu cestu. Nový výpočtový variant musí byť samostatná dosiahnuteľná funkcia alebo skript a musí exportovať identifikátor skutočne vykonanej cesty. Patch markera v nedosiahnuteľnom bloku je technické zlyhanie aj vtedy, keď textová náhrada prešla.

## Q77 — Ktoré formulácie K7b/K7c obmedzil audit skriptov 173–185?

- PASS 174–176 sa numericky neruší: fyzikálny register bol opravený a skutočný payload mal `reduced_rank=free_count=58`.
- Rankový check zdedený zo 172 je však implementačne fail-open a pred publikáciou potrebuje novú fail-closed náhradu.
- `seed["D"]==D`, `seed["M"]==M`, `rhs[0]-(3D+2s²eta)` a `rhs[1]-M` sú self/konštrukčné identity bez nezávislého confidence kreditu.
- Density/momentum znovuzloženie po definovaní species cez `D,M` je iba monitor float64 kancelácie.
- Skript 185 exportuje pomer zjemnenia, ale nemá pomerovú bránu. Dnešný REVIEW sa nemení, lebo zlyhal aj endpoint prah a pomer `0.367` je neasymptotický.
- Fixed-RK4 blok v 183–185 sa vykoná, ale starý `solve_ivp` za skorým returnom je nedosiahnuteľný a nesmie slúžiť ako ďalší marker.
- Nedokončený skript 186 je neautoritatívna zachovaná stopa; náhrada musí mať nové číslo.
