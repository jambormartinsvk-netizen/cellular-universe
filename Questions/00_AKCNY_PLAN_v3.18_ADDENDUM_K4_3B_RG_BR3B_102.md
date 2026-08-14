# Akčný plán v3.18 — dodatok po K4.3b-RG BR3B-2d

Dátum: 2026-07-14

## Aktívna priorita

Dokončiť A2-K4/G7 bez preskočenia skorších NID/NIV Puiseuxových sektorov.

| Poradie | Úloha | Brána úspechu | Stav |
|---:|---|---|---|
| 1 | BR3B-2e: odvodiť neutrínový šmyk a minimálnu regulárnu `l>=3` rekurziu pre NID/NIV | žiadny chýbajúci skorší exponent; regulárna hierarchia | NEXT |
| 2 | BR3B-2f: vyriešiť indukovanú odozvu sektor po sektore vzostupne | `rank(A)=rank(A|b)` a konečné koeficienty | PENDING |
| 3 | BR3C: dvojhĺbkový reziduálny a konvergenčný test všetkých štyroch Einsteinových rovníc | predregistrované absolútne/relatívne tolerancie | PENDING |
| 4 | BR4: úplná fotónová/neutrínová Boltzmannova implementácia | nulový limit + referenčný cross-check | PENDING |
| 5 | uzavrieť G7 | fyzikálne transfery všetkých módov bez nestability | PENDING |
| 6 | až potom G8 | CMB-normalizované spektrá a S8 | BLOCKED BY G7 |

## Ochranné pravidlá vykonania

- Každý nový skript musí mať vnútorný limit; vonkajší limit nesmie prekročiť dohodnuté maximum.
- Timeout a technická chyba ostávajú `UNCLOSED`, nikdy `DEAD`.
- Chybné skripty a výpočty sa nemažú; oprava vzniká ako nový označený klon.
- Skóre K4 ostáva 60/100 až do úplného prechodu G7.

