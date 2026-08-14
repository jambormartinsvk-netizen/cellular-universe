# Audit umiestnenia rodiny 05 a súladu subaudítorov

**Dátum:** 2026-07-16  
**Autorita rozhodnutia:** hlavný orchestrátor  
**Rozsah:** organizačný; nemení fyzikálne verdikty

## Zistenie

Pracovná rodina registra 05 sa po vzniku `tracks/` ešte stále vytvárala a
menila v `theory/`. Inventúra našla 57 SK a 57 EN súborov začínajúcich `05`.
Najnovšie AR68, AR69 a zmena kumulatívneho `05c` pochádzajú z 2026-07-16.
Bezprostrednou príčinou bol hybridný workflow: route stav už používal
`tracks`, ale synchronizačný dokument stále prikazoval nový párový dodatok
v `theory`.

Nenašiel sa automatický generátor ďalších registrov 05. Skripty, ktoré ich
spomínajú, iba čítajú alebo hashujú existujúce súbory. Množenie spôsobovala
manuálna pracovná inštrukcia; tá bola týmto auditom nahradená.

## Nezávislá kontrola audítorov

- `physics_track_auditor` dodržal read-only režim a neudelil verdikt;
  spätne opravil vlastné označenie R-A/R-B: sú to implementačné architektúry
  v K4, nie nové fyzikálne koľaje bez splnenia K-ZROD.
- `math_script_auditor` dodržal read-only režim a neudelil verdikt, ale
  priznal, že pri prvom kole nečítal track kontrakt a error ledger ako prvé;
  raz preto zopakoval známu neškodnú PowerShell parser chybu PF-011/PF-016.
- `documentation_release_steward` dodržal read-only režim, nič nepublikoval
  a našiel 11 skupín kolíznych heading ID, ktoré blokujú prosté spojenie 05.

Tieto procesné medzery rieši povinný predauditný preflight doplnený do
`Audit/00_MULTI_AUDITOR_ROLE_CONTRACT_2026-07-16.md`.

## Autoritatívne rozhodnutie

1. AR70 je prijatá ako pracovná hranica dokumentácie.
2. Od tohto auditu sa nový pracovný `theory/*/05*` nevytvára ani neaktualizuje.
3. Stav koľaje nahrádzajú route-local `00_WORK_PLAN`,
   `00_CURRENT_DECISION`, `HISTORY`, manifesty a `AUDIT_THREADS`.
4. Skutočná nová AR/Q/L delta vznikne ako úzky SK/EN pár v príslušnom uzle
   `tracks`; spoločná delta v `tracks/METHODOLOGY/`.
5. `theory/` dostane iba konsolidovaný release/release-candidate register po
   prijatí hlavným orchestrátorom, changelogu, SK/EN kontrole a SHA manifeste.
6. Historických 114 súborov sa teraz nemaže ani nepresúva. Chýba Git baseline
   a úplná mapa závislostí; presun by porušil spätný audit hashov a odkazov.
7. Ďalšie globálne AR/Q číslo sa nepridelí pred vyriešením kolízneho ledgera.

## Zastaraný manifest 05c

`theory/05c_REGISTER_v3.18_SK_EN_MANIFEST.md` uvádza staršie hashe a rozsah
AR1–AR8. Aktuálny pracovný pár má:

| Jazyk | Aktuálny SHA-256 |
|---|---|
| SK `05c` | `590FE20A3FCF279A7628E95C2ADC24FFD19AF15A6F528B8035BDCB8D6ACC2A63` |
| EN `05c` | `73DBCCB479FB5974CCC822AC27B6D2B72D6FF8C2739FF2F31825A2C29EFE6244` |

Manifest sa preto od tohto dátumu interpretuje iba ako historická snímka
pred ďalšími pracovnými zmenami. Nesmie sa potichu prepísať na nový hash;
pri release vznikne nový datovaný manifest a changelog, ktorý rozdiel
vysvetlí.

## Kolízie ID

Potvrdené sú `AR8`, `AR9`, `AR37`, `AR38`, `AR39`, `Q20`, `Q64`, `Q65`,
`Q66`, `Q67` a `Q72`. Q20 je verzovaná historická otázka; ostatné skupiny
často označujú úplne iné pravidlá alebo otázky. Rozlíšenie je zapísané v
`tracks/METHODOLOGY/00_IDENTIFIER_COLLISION_LEDGER.md`. Release builder
nesmie použiť prosté zreťazenie dodatkov.

## Náhrada

- globálna pracovná metodika:
  `tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md`
  a EN pár;
- route stav a otázky: najnižší aktívny track kontrakt a audit thread;
- budúce povýšenie: `tracks/METHODOLOGY/00_RELEASE_PROMOTION_LEDGER.md`;
- bezstratová inventúra:
  `tracks/METHODOLOGY/HISTORY/00_THEORY_05_LEGACY_INVENTORY.md`;
- ID konflikt: `tracks/METHODOLOGY/00_IDENTIFIER_COLLISION_LEDGER.md`.

## Rozsah, ktorý zostáva otvorený

Úplná fyzická migrácia starých dodatkov nebola vykonaná. Pred ňou treba Git
baseline, úplný `OLD_PATH -> NEW_PATH` manifest, link audit a porovnanie
SHA-256. Toto je vedomá bezpečnostná brzda, nie strata dokumentácie.
