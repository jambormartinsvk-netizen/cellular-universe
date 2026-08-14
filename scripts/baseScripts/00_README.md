# baseScripts — zdieľané výpočtové jadro

**Aktualizované:** 2026-07-16  
**Stav:** `IMPLEMENTOVANÉ MODULY / LEGACY_UNVERSIONED / PIN BY SHA-256`

Tento adresár obsahuje znovupoužiteľnú matematiku. Nie je to odkladisko
runnerov ani výsledkov. Historické číslované runnery zostávajú v `scripts/`,
výsledky v `scripts/results/` a každá koľaj na ne odkazuje vlastným
artefaktovým manifestom.

## Aktuálne rodiny

| Rodina | Vlastník | Rozsah | Stav |
|---|---|---|---|
| `a2_k4_g8/` | historická A2-K4/K7/G8 línia | štrukturálny screen, TCA, hierarchia, background | `HISTORICAL_SCOPE`; K7 fyziku neobnovuje |
| `k_mpc_005/` | A1-K1/P4 a Q22A background | presný A1 background a `A_f` mapovanie | `REVIEW`; `0.05` nie je background parameter |
| `p5_general_synchronous/` | A2-K4/P5 | plný general-synchronous formulačný základ | `ACTIVE_FORMULA_SCOPE`; P5.3 je blokovaná |
| `000–002` | globálne nástroje | ohraničené PDF utility | nefyzikálne utility |

Presní vlastníci, importujúce runnery a SHA-256 sú v
`00_MODULE_OWNERSHIP_REGISTER.md`. Podadresár sa nesmie interpretovať podľa
názvu bez jeho lokálneho `00_README.md`.

## Nemennosť a opravy

Existujúce moduly boli použité ešte pred zavedením verzií `vNNN`. Preto sa
odteraz považujú za `LEGACY_UNVERSIONED` zmrazené svojím SHA-256. Nesmú sa
potichu opravovať na tej istej ceste po tom, ako výsledok pinol ich hash.
Oprava vytvorí novú verziu alebo nový modul, changelog, zoznam dotknutých
manifestov a nové výsledky. Staré výsledky ostanú `LIMITED` alebo
`SUPERSEDED`.

Nový runner musí uviesť:

1. route a gate ID;
2. presnú cestu a SHA-256 každého base modulu;
3. fyzikálny background a stavovú bázu;
4. výsledok a audit, ktoré vytvorí;
5. interný limit najviac 5 s a vonkajší najviac 10 s;
6. predbehový Markdown s očakávaním, PASS/STOP a ďalším krokom.

Base modul nie je dôkazom sám osebe. PASS patrí iba konkrétnemu
route-conditioned behu a jeho auditu.

## Zakázané skratky

- nevytvárať `current`, `latest` ani mutable autoritatívny alias;
- nekopírovať rovnaký vzorec do viacerých runnerov;
- neprenášať PASS medzi rozdielnymi backgroundmi;
- nepresúvať historický runner, ktorý používa `Path(__file__).with_name()`;
- nečítať obsah `__pycache__` ako zdroj alebo verziu.

Architektúra: `Questions/BASESCRIPTS_VERSIONED_ARCHITECTURE_AND_MIGRATION_2026-07-15.md`  
Pravidlá: AR62 a AR69.

