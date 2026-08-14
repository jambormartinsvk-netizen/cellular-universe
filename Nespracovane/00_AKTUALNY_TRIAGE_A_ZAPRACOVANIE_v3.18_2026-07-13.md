# Aktuálna triáž adresára Nespracovane pre v3.18

**Dátum:** 2026-07-13  
**Účel:** rozhodnúť, čo sa smie zapracovať, čo čaká na fyzikálnu bránu a čo zostáva iba historickým podkladom

## 1. Pravidlo zapracovania

Súbor v `Nespracovane` nie je automaticky súčasťou teórie. Každý vstup autora je hypotéza. Do hlavného dokumentu sa smie presunúť iba obsah, ktorý má:

1. určený vedecký status;
2. zdokumentované predpoklady;
3. splnenú príslušnú bránu;
4. zosúladenú SK/EN verziu;
5. auditnú stopu a changelog.

Tento súbor aktualizuje stav známych aktívnych materiálov. Pôvodné súbory sa nemenia ani nemažú, aby sa zachoval spätný audit.

## 2. Aktuálny register

| Súbor/položka | Stav | Rozhodnutie pre v3.18 | Potrebná akcia |
|---|---|---|---|
| `A16_K1_kovariantne_zobrazenie_SK_v3.18_NAVRH.md` | **PRIPRAVENÝ NÁVRH POZADIA** | Zapracovať iba do úzkej R3.18-DOC a výslovne ho označiť ako kandidáta pozadia. Nevyhlasovať za hotové perturbácie. | Zosúladiť s A2 ledgerom; ponechať T7/T8 otvorené. |
| `A16_K1_covariant_embedding_EN_v3.18_DRAFT.md` | **PRIPRAVENÝ EN NÁVRH POZADIA** | Rovnaké obmedzenie ako SK verzia. | Terminologická a rovnicová kontrola SK/EN po A2.0. |
| `krok_D_registrovy_balik.md` | **HISTORICKÝ / PREKONANÉ PORADIE** | Nezapracovať ako aktuálny plán. Zachovať ako auditnú stopu. | Riadiť sa `Questions/00_AKCNY_PLAN_v3.18_AKTUALNY_2026-07-13.md`. |
| `Kozmologická pipeline 09.txt` | **POMOCNÝ PODKLAD, INTERPRETÁCIA ZASTARALA** | Nezapracovať tvrdenia o presnom `S8/H0` alebo globálnom fite. | Prepísať opis na background/toy sensitivity; fyzikálne perturbácie presunúť do A2/A3. |
| `sud_14_slabin_a_latex_ns.md` | **AUDITNÝ VSTUP, NIE DÔKAZ ODVODENIA** | Slabiny možno použiť v registri; `n_s`, `m=1/2` a `C=28` nezapracovať ako vety. | Priradiť k A5/Q11d/Q28 a doplniť look-elsewhere kontrolu. |
| Hypotézy drag/krivosti a gridy `S8/H0` | **SPRACOVANÉ AUDITOM** | Nezapracovať ako nové predikcie. Možno zapracovať iba verdikty, erratá a označenie toy sensitivity. | Autoritatívny stav je v `Audit/00_READ_FIRST_S8_H0.md` a finálnych auditných súboroch. |
| Návrh `gamma_drag=0.03` | **MŔTVY V DODANEJ FORME** | Nezapracovať. | Ak sa bude skúmať ďalej, iba ako nová kovariantná S8-K1b po A2. |
| Návrh `Omega_K=0.005` ako riešenie napätí | **MŔTVY AKO DÔKAZ/PREDIKCIA** | Nezapracovať do tabuľky predikcií. | K4b musí najprv odvodiť krivosť zo siete bez kalibrácie na `H0`. |
| Otázky Q4/Q8/Q11d/Q6 | **SPRACOVANÉ DO REGISTRA, FYZIKÁLNE OTVORENÉ** | Zapracovať iba ako otvorené otázky a kill conditions. | Riešiť v ich samostatných koľajach; neoznačiť za uzavreté. |

## 3. Obsah, ktorý možno zaradiť do R3.18-DOC

Po redakčnej kontrole možno zaradiť:

- pravidlo nemenných publikovaných verzií a changelog;
- opravený ledger baryónov a CDM na pozadí;
- A1-K1 ako **pracovného kandidáta pozadia**;
- výsledky kontrol pozadia vrátane približne `8.999 %` dodatočnej komovanej CDM od rekombinácie v danej implementácii;
- register otvorených testov T7/T8;
- erratá k interpretácii skriptov a vetvy `S8/H0`;
- zoznam falzifikačných brán A2–A8.

## 4. Obsah, ktorý sa zatiaľ nesmie zaradiť ako výsledok teórie

- presná predikcia `S8=0.82` z drag mechanizmu;
- tvrdenie, že `Omega_K=0.005` je odvodené zo siete;
- tvrdenie o zlepšení globálneho `chi2` oproti ΛCDM;
- post-data optimum v dvojparametrovom gride;
- hotové perturbácie A1-K1;
- odvodené `n_s` z `m=1/2` alebo `C=28` bez A5;
- jednotný mechanizmus domény I bez operátora, Bornovho pravidla, no-signalling a energetickej bilancie;
- odvodenie `epsilon` z prvých princípov.

## 5. Poradie spracovania fronty

1. **A2 ledger a perturbácie** — vytvoriť nové návrhy A17 a testovací protokol.
2. **A16 SK/EN** — po A2.0 opraviť terminológiu; pri R3.18-DOC jasne obmedziť na pozadie.
3. **Pipeline 09** — doplniť erratum/opis rozsahu; nepoužívať na perturbácie.
4. **A4/A5 materiály** — para, exit, `zeta`, gaussovskosť, `m` a `C`.
5. **K4b materiál** — iba nezávislé odvodenie diskrétnej krivosti.
6. **Predikčné tabuľky** — aktualizovať až po A3/A8; dovtedy zachovať staré čísla ako historické čísla príslušnej verzie.

## 6. Vydávacia kontrola pre každý presunutý text

Pred presunom z `Nespracovane` označiť:

- pôvodný súbor a jeho SHA-256;
- cieľový súbor a sekciu;
- typ zmeny: oprava / nové odvodenie / hypotéza / erratum;
- fyzikálny status;
- súvisiaci skript a jeho verziu;
- rozdiel SK/EN;
- položku changelogu.

Kým tieto polia chýbajú, položka zostáva v `Nespracovane`.

