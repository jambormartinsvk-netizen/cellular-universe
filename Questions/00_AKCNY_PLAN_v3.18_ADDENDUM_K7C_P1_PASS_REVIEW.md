# Akčný plán v3.18 — po K7c P1

Dátum: 2026-07-15

## Dokončené P1

- mechanicky odvodený čistý skript 197 zo zdroja 179 s overeným hashom;
- odstránený celý nedosiahnuteľný adaptívny blok bez zmeny RHS, seedu, škály, closure alebo krokov;
- `py_compile`, CLI smoke-test a corpus checker 198 prešli pred fyzikou;
- mriežky 100/200/400 majú samostatné nemenné checkpointy;
- historický výsledok bol reprodukovaný v zmrazených toleranciách;
- auditná reprodukcia PASS, fyzikálna konvergencia REVIEW, skóre bez zmeny.

## P2 — nasleduje

Cieľ: určiť, prečo je rozdiel 200/400 väčší než 100/200 a prečo dominuje rovnica `M'`.

1. Skript 186 ponechať nedotknutý a `DO_NOT_RUN_TECHNICAL`; vytvoriť nový číslovaný diagnostický skript.
2. Zdroj a očakávania zmraziť v samostatnom MD ešte pred prvým výpočtom.
3. Na identických uložených stavoch rozložiť `M'` na všetkých deväť aditívnych členov a exportovať znamienko, absolútnu veľkosť, súčet absolútnych hodnôt a cancellation ratio.
4. Porovnať obyčajný float64 súčet, `math.fsum` a 80-dps referenciu. Vysoká presnosť na float64 stave testuje iba sčítanie, nie chybu samotného stavu; tieto závery sa nesmú miešať.
5. Diagnostický ledger nesmie meniť RHS ani pridávať body.
6. Až následná samostatná podkoľaj smie nahradiť súčet v RHS a zopakovať 100/200/400.
7. `fsum` podkoľaj prežije iba pri predregistrovanom najmenej desaťnásobnom zlepšení na každom aktívnom checkpoint-e a pri posune pomeru smerom ku konvergentnému RK4 režimu. Inak sa označí za mŕtvu s uloženými výpočtami.
8. Ak sčítanie nie je príčina, ďalšie oddelené koľaje sú algebraické preusporiadanie, lokálna tuhosť/eigenmódy a vyššia pracovná presnosť. Nesmú sa kombinovať v jednom behu.

## Stop podmienky

- timeout alebo technická chyba znamená REVIEW, nie smrť K4;
- zmena seedu, backgroundu, rovníc alebo closure ruší porovnateľnosť a vyžaduje novú koľaj;
- žiadny CMB/S8 beh pred konvergovanou evolučnou bránou;
- bez zmeny predikčnej tabuľky nevzniká z P1/P2 samostatný Zenodo release trigger.

## Údržba

Po uzavretí P2 aktualizovať centrálny register, read-first, stav koľají a obidva SK/EN metodické registre. Upratanie adresárov, Git commit a Zenodo changelog ostávajú povinné pred publikovaním v3.18.

## ORG-V2 — stanice, cesty koľají a auditné thready

Stav: **návrh pripravený; fyzická migrácia ešte nezačala**.

1. A1, A2, A3, ... modelovať ako stanice; route prefix sa fyzicky zapisuje `A1/A1Kx/A2/A2Ky/...`.
2. Každá stanica aj koľaj má `PASS`, `REVIEW`, `STOP`, `HISTORY`, `AUDIT_THREADS` a `ARTIFACTS`.
3. Každý auditný thread uchováva nemenné kolá `audit → response → evidence → open points → reaudit` a samostatné thread decision.
4. Podkoľaje A2-K4 patria do `A2K4/SUBTRACKS`; nie sú novými stanicami.
5. Terminálny dokument každej mŕtvej cesty uvádza poslednú dosiahnutú stanicu a dôvod smrti.
6. A2-K10 ostáva kanonicky pod route prefixom A1-K2, pokiaľ audit nepreukáže platnosť aj pre A1-K1.
7. Fáza 1 vytvorí iba strom a manifesty odkazujúce na dnešné cesty; existujúce súbory sa ešte nepohnú.
8. Fáza 2 sa začne až po SHA/path manifeste, Git baseline a kontrole všetkých 468 rozpoznaných väzieb.
9. Reorganizácia sa commitne oddelene od fyzikálnych zmien a sama nepridáva auditnú hĺbku.

Autoritatívny návrh: `Questions/DIRECTORY_STRUCTURE_AND_MIGRATION_PROPOSAL_V2_STATIONS_ROUTES_AND_AUDIT_THREADS_2026-07-15.md`.

## ORG-V2.1 — história, váhy, spoločné jadro a externý audit

1. Každý uzol dostane povinný append-only HISTORY/00_EVENT_LEDGER.md a
   podregistre rozhodnutí, zmien skóre, obmedzení, supersession a zmien cesty.
2. Každý test sa pred behom priradí verziovanej gate s váhou; scorecard
   oddelí podporu, blocker, otvorenú váhu a auditované pokrytie.
3. Pre C7.7c sa používa návrh C7-W1: K7 má konzervatívne podporu 40/100,
   blocker G5 20/100, otvorené 40/100 a pokrytie PASS+FAIL 60/100.
   Tieto čísla nenahrádzajú ani sa nesčítajú s hĺbkou A2-K4 66.5/100.
4. Historické K1 až K6 sa nepremenúvajú. Jednotná matica explicitne označí
   PASS/FAIL/REVIEW/NOT_REACHED/INHERITED, takže neprítomné K1c už nebude
   vyzerať ako zabudnutý výsledok.
5. Zaviesť pilot scripts/baseScripts/v001 iba pre K7c P1. Pred ďalšou
   migráciou musí manifest reprodukovať skript 197 a všetky tri checkpointy.
6. Pripraviť route-conditioned externý auditný export zlyhania G5 so
   skriptom, checkpointmi, rovnicami, normou, očakávaniami, hashmi a otázkami
   pre nezávislého auditora.
7. Fyzická migrácia a extrakcia Python jadra ostávajú samostatná neskoršia
   zmena; tento zápis nevykonal fyzikálny výpočet ani nezmenil verdikt K4.

Podklady:

- Audit/A2_K4_C7_7C_K1_K7_LINEAGE_GATE_COVERAGE_AND_WEIGHT_AUDIT_2026-07-15.md
- Questions/BASESCRIPTS_VERSIONED_ARCHITECTURE_AND_MIGRATION_2026-07-15.md
- Questions/EXTERNAL_AUDIT_PACKAGE_STANDARD_AND_K7C_RK4_PILOT_2026-07-15.md
## Ochrana vedeckého P2 počas ORG-V2-P1

1. Historické P2 je stabilne pomenované
   SCI-A2K4-C7G5-K7C-P2-MLEDGER; jeho obsah ostáva nezmenený.
2. ORG-V2-P1 smie vytvárať iba adresáre, indexy, HISTORY, scorecardy a
   manifestové odkazy. Nesmie meniť skript 186, RHS ani P2 predregistráciu.
3. ORG-V2-P2 je budúci fyzický presun súborov a nesmie sa označiť iba P2.
4. BASE-V001-PARITY-197 a AUD-C7G5-K7C-P1-RK4 sú samostatné podporné úlohy;
   najbližším vedeckým výpočtom zostáva M-prime ledger.
5. Vytvorený route strom je navigačný. Pôvodné artefakty neboli presunuté.

Scope freeze:
Questions/A2_K4_K7C_P2_SCOPE_FREEZE_AND_ORG_NAMESPACE_2026-07-15.md.