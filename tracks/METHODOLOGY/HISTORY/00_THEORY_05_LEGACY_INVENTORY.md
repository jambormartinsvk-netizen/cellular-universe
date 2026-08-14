# Inventúra historickej rodiny `theory/*/05*`

**Snímka:** 2026-07-16  
**Účel:** bezstratové zmrazenie umiestnenia pred budúcou migráciou  
**Nemení obsah ani staršie verdikty.**

## Počty

| Skupina | SK | EN | Spolu | Aktuálna klasifikácia |
|---|---:|---:|---:|---|
| všetky súbory začínajúce `05` v `theory/SK`, `theory/EN` | 57 | 57 | 114 | zmrazené do klasifikácie |
| klasická rodina `05*Methodology_Rules_and_Question_Register*` | 54 | 54 | 108 | base, v3.18 draft alebo historické route dodatky |
| AR67–AR69 samostatné tematické páry | 3 | 3 | 6 | historické pracovné dodatky |

## Triedy

| Trieda | Obsah | Pravidlo od 2026-07-16 |
|---|---|---|
| `RELEASE_BASE` | v3.17 SK `05_...` a EN `05b_...` | nemení sa bez novej verzie |
| `LEGACY_RELEASE_DRAFT` | kumulatívny v3.18 `05c` pár | zmrazený pracovný snapshot; nie živý register |
| `HISTORICAL_ROUTE_REGISTER` | A2/K4/K7 a ďalšie route-specific páry | zachovať na pôvodnej ceste pre hashe a odkazy |
| `HISTORICAL_METHOD_ADDENDUM` | všeobecné AR a tematické metodické páry | zachovať; nové delty už vznikajú v `tracks` |

## Zistený problém

Pracovný tok ešte 2026-07-16 vytvoril alebo menil AR68, AR69 a kumulatívny
`05c` priamo v `theory`. Dokument
`Questions/00_STAV_SYNCHRONIZACIE_REGISTRA_05_SK_EN.md` zároveň prikazoval
nový párový tematický dodatok v `theory`. Tento pokyn je od AR70 nahradený.

Manifest `theory/05c_REGISTER_v3.18_SK_EN_MANIFEST.md` obsahuje staršie hashe
než aktuálny obsah páru `05c`; preto je historickým manifestom pred ďalšími
pracovnými zmenami, nie dôkazom aktuálne zmrazeného páru. Aktuálne hashe sa
evidujú v audite hranice a pri release sa vytvorí nový manifest.

Jednotlivé dodatky navyše používajú 11 kolíznych skupín heading ID:
AR8, AR9, AR37, AR38, AR39, Q20, Q64, Q65, Q66, Q67 a Q72. Väčšina má
odlišný význam, Q20 je historická revízna séria. Presná mapa je v
`tracks/METHODOLOGY/00_IDENTIFIER_COLLISION_LEDGER.md`; prosté spájanie
súborov je release blocker.

## Migračná brzda

Súbory sa teraz fyzicky nepresúvajú. `D:\Teoria` zatiaľ nemá Git baseline a
stovky auditov, hash manifestov a smerovníkov citujú pôvodné cesty. Presun je
povolený až po:

1. Git baseline;
2. úplnom zozname párov a `OLD_PATH -> NEW_PATH`;
3. kontrole textových aj skriptových odkazov;
4. SHA-256 pred/po presune;
5. redirect/superseding zázname a samostatnom audite.

Do tej doby je zákaz nových pracovných zápisov do rodiny `theory/*/05*`
bezpečnou náhradou fyzického presunu.
