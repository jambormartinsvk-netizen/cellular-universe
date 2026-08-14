# Upresnenie A0: verzovanie a nemennosť publikovaných verzií

Dátum: 2026-07-13

Tento dodatok upresňuje a nahrádza nejednoznačnú formuláciu kroku A0 v súboroch:

- `Questions/doplnenie_otazok_a_krokov_po_fyzikalnom_audite_2026-07-13.md`,
- `Audit/fyzikalny_audit_bunkoveho_priestoru_2026-07-13.md`.

## Význam slova „zmraziť“

„Zmraziť v3.17/Zenodo v2“ neznamená zastaviť vývoj teórie ani prestať vytvárať nové verzie. Znamená to ponechať už publikovaný a citovateľný snapshot v3.17/Zenodo v2 nemenný.

Ak niekto túto verziu prečíta, použije jej výsledok alebo ju cituje, musí byť aj neskôr schopný získať presne ten istý obsah. Changelog môže vysvetliť zmeny medzi verziami, ale nesmie slúžiť ako ospravedlnenie na tiché prepísanie súborov starej citovanej verzie.

## Opravené znenie A0

| Krok | Úloha | Výstup | Kritérium dokončenia |
|---|---|---|---|
| A0 | Ponechať už publikovanú v3.17/Zenodo v2 nemennú; každú opravu alebo rozšírenie vydať ako novú verziu a viesť changelog | Mapa verzií, DOI, dátumov a kontrolných súčtov | Citácia konkrétnej verzie zostane reprodukovateľná; starý snapshot sa neprepisuje a každá zmena je uvedená v changelogu novej verzie |

## Odporúčané pravidlá vydávania

1. v3.17/Zenodo v2 ponechať obsahovo aj súborovo nezmenenú.
2. Opravy a nové tvrdenia zaradiť do v3.18 alebo ďalšej jasne označenej verzie.
3. Každej verzii priradiť vlastný verziový identifikátor a verziový DOI; spoločný concept DOI používať iba ako odkaz na celý rad verzií alebo na najnovšiu verziu.
4. Ku každej verzii uložiť zoznam súborov, ich SHA-256 kontrolné súčty, dátum vydania a použitý zdrojový commit alebo ekvivalentný identifikátor snapshotu.
5. Changelog viesť smerom „stará verzia → nová verzia“ a pri každej zmene uviesť aspoň: dotknuté tvrdenie alebo rovnicu, dôvod zmeny, starú hodnotu, novú hodnotu a vplyv na závery.
6. Opravu chyby v starej verzii zaznamenať ako erratum a opravu vykonať v novej verzii; pôvodný obsah spätne neprepisovať.
7. V citáciách odporučiť verziový DOI, ak záver závisí od konkrétnych rovníc, čísel alebo dátových súborov.

## Záver

Verzovanie je potrebné a správne. Audit nenavrhuje obmedziť tvorbu verzií; navrhuje oddeliť nemenné publikované snapshoty od ďalšieho vývoja. Tým sa chráni citovateľnosť, reprodukovateľnosť a dôvera v záznam teórie.
