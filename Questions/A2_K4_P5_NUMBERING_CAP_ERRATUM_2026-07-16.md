# A2-K4/P5 — erratum číslovania a obmedzený zvyšný budget

**Dôvod:** starý plán 209–240 predpokladal pokračovanie redukovaného K7 do
G8. Následný lineage audit našiel chýbajúce dynamické `U_c` a neplatný
background transfer, preto vznikol samostatný nápravný P5 program 234–254.
Tieto súbory sú zachované; nesmú sa vydávať za technické obchádzanie capu.

**Rozhodnutie (opravené 2026-07-16):** pôvodný rozsah `255–258` sa stal
nepoužiteľným pre pôvodný plán: `257` je zachovaný fail-closed markerový
pokus (PF-054) a `258–259` boli medzitým správne pridelené nezávislej Q22a
vetve. Nejde o novú fyzikálnu koľaj. Pre P5 zostáva jediný konečný rozsah
`260–262`, s presne tromi nižšie uvedenými úlohami.

| Skript | Balík | Účel |
|---:|---|---|
| 255 | P5.3g4 | fotónový `l=2`/polarizačný TCA algebraický blok; PF-053 scope erratum |
| 256 | P5.3g5 | skorá opacity a zdrojový constraint ledger |
| 257 | P5.3g6 | PF-054 technický marker STOP; zachovaný, nepoužiť na fyziku |
| 260 | P5.3g6 RERUN1 | iba oprava markerovej cesty a exact gauge bridge |
| 261 | P5.3g7 | dvojštartový úplný photon+neutrino/dark-sector seed audit, iba ak 260 prejde |
| 262 | P5.4 | krátka species-first evolúcia, iba ak 261 prejde |

Každý balík má jednu implementáciu a najviac dve technické opravy. Neúspech
algebry, ledgeru alebo regularity je fyzikálny STOP/REVIEW podľa dôkazu;
parser, import a timeout nie sú nová koľaj. Číslo za `262` vyžaduje nový
autoritatívny architektonický audit, nie automatické pokračovanie.
`258–259` ostávajú patriť Q22a a nesmú sa premenovať ani použiť ako P5
obchádzka.

**Technické spresnenie PF-055:** opravný súbor s rovnakým route číslom `261`
a novým run ID `KMPC_023 ... RERUN1` sa počíta ako prvá technická oprava
balíka 261, nie ako nová fyzikálna úloha a nie ako použitie rezervovaného
skriptu 262. Pôvodný 261/KMPC-022 ostáva immutable `DO_NOT_RUN_TECHNICAL`.
RERUN1 nesmie meniť base hash, rovnice ani prahy; mení iba JSON typy.

**Posledná oprava po výsledku RERUN1:** KMPC-023 dobehol, ale odhalil
formula-väzbovú chybu: M1 amplitúda bola iba post-check a všetkých 15
štandardných matíc malo hodnosť `76/77`. KMPC-024/RERUN2 je druhá a posledná
povolená oprava 261. Smie iba tvrdo eliminovať M1 `h` koeficient z už
existujúcej matice, opraviť stale run label a zachovať všetky fyzikálne
rovnice, vstupy a prahy. Po ňom nie je automaticky povolený RERUN3; ďalší
kód by vyžadoval nový architektonický audit.

**Stav po KMPC-024:** druhá oprava dobehla. M1 a štandardný seed prešli,
ale PF-058 contract-parity audit zistil chýbajúce dynamické `delta_f,U_f` a
ich dve rovnice v frakčnej matici. Limit 261 je tým vyčerpaný a RERUN3 je
zakázaný. Datovaný architektonický audit autorizuje iba textové odvodenie
úplného dvojparametrového coefficient/Bianchi ledgeru; neautorizuje nový runner. Číslo nad 262 alebo
iné znovupoužitie 261 sa smie povoliť až po uzavretí tohto ledgeru. `262`
ostáva výhradne P5.4.

Toto erratum nemení skóre K4 (`60/100`) ani neotvára G8. Nahrádza iba
zastaranú technickú numerickú hranicu v pláne z 2026-07-15 pre P5 successor.

## Neskoršie metodické obmedzenie — cap 10

Formulácie „najviac dve technické opravy“, „limit 261 je vyčerpaný“ a
„neautorizuje nový runner“ zostávajú historickým záznamom rozhodnutia v čase
KMPC-024. Neskoršie autoritatívne pravidlo používateľa odlišilo technickú
chybu od fyzikálneho pokusu a zaviedlo cap `10` technických pokusov na jednu
implementačnú vetvu. Legacy RERUN3 KMPC-022/023/024 zostáva zakázaný, ale
úplná R-A realizácia po B1 je povolená ako konzervatívny spoločný pokus
`4/10`. Premenovanie modulu counter nevynuluje. Skóre K4 zostáva `60/100`.

## Neskorší vykonaný stav

Pokus 4 odhalil PF-064 a pokus 5 ju opravil nezávislým contract validatorom.
Spoločný counter je `5/10`; B1 má `PASS_CONTRACT_PREFLIGHT_ONLY`. Seedový
pokus 6 dostal samostatnú predregistráciu v dokumente 37. Shared modul a
runner KMPC-027 sú vytvorené, ale v čase tohto dodatku stále `NOT_RUN`;
prebieha iba read-only/statický delta audit pred hash freeze.

## Supersession po KMPC-031 a novom counter pravidle

Vyššie uvedený stav `5/10 / attempt 6 NOT_RUN` je nemenný dobový snapshot.
Balíky 6–10 neskôr prebehli a KMPC-031 uzavrel AD/k=.05/nominal J4 support
sentinel. Aktuálne platí `historical_packages_total=10` a po vecnom úspechu
`consecutive_technical_failures=0/10`. Nevzniká attempt 11 ARCH-A; ďalší
samostatný coverage/formula balík je S-C0 coefficient passport podľa
dokumentov 51–52. Skript 262 zostáva rezervovaný P5.4.
