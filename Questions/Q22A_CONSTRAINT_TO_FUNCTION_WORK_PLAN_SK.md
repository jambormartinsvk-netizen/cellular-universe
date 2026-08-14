# Q22a/Q18 — návrh postupu: od mantinelov k zdroju pary

**Cieľ:** bez voľného fitovania rozhodnúť, či existuje lokálna kovariantná
funkcia skorého zdroja pary, a ak áno, či ju mantinely určujú jednoznačne alebo
ponechávajú obmedzenú rodinu.  
**Východisko:** efektívna FLRW trieda je nezakázaná; fundamentálny M0 clock a
rezervoár nie sú dnes definované.  
**Mimo rozsahu:** nemení A1/K4 ani umelo nevytvára novú mikrofyziku.

## Aktuálny stav koľají v tomto úzkom probléme

| Rozsah | Stav | Presný význam |
|---|---|---|
| Q22a-K1, neskorý `F->C` | `BASELINE EFFECTIVE PASS` | zachovaný A1 ledger; nie je to mikroverdikt o vzniku pary |
| Q22a-K2, perzistentné priame `F->R` | `MŔTVA M-015` | samostatný rozpočet `Delta N_eff` vylučuje dodanú neskorú voľno-relativistickú formu |
| Q22a-K3, priamy paralelný podiel pary | `PODMIENEČNE ŽIVÁ` | len v zanedbateľnom priamom limite `f_R<~3.2e-5`; podiel nie je odvodený |
| skorý ukončený relikt ako efektívna FLRW história | `ŽIVÁ EFEKTÍVNA TRIEDA` | M1–M5 nevylučujú hladký skorý zdroj s párovým ledgerom |
| skorý relikt ako fundamentálna lokálna mikrofyzika | `REVIEW/STOP NA M0` | dnes neexistuje kandidát s uzavretým `chi`, rezervoárom a `T_e^(mu nu)` |

Teda: **nemáme ešte živú fundamentálne uzavretú A4 koľaj**, ale nemáme ani
rozsudok, že žiadna nemôže existovať. P1.1 má rozhodnúť, či dnešné postuláty
obsahujú aspoň jeden oprávnený vstup do P2, alebo či A4 ostane blokovaná do
doplnenia novej mikrofyziky.

**Aktualizácia 2026-07-16:** P1.1 je dokončená. Audit
`Audit/Q22A_P1_1_EXISTING_SOURCE_MAP_AUDIT_2026-07-16.md` našiel nulový počet
P2-ready kandidátov. P1 je preto `STOP` pre súčasnú fundamentálnu A4 vetvu;
efektívna FLRW trieda tým nie je usmrtená.

**Rozšírené potvrdenie 2026-07-16:** P1.2 preverila hlavný dokument a
relevantné `Nespracovane`. A12 obsahuje iba podmienenú termalizačnú hranicu,
nie `C_g`/rezervoár; A16 potvrdzuje iba `F->C`. Pozri
`Audit/Q22A_P1_2_EXTENDED_CORPUS_SOURCE_AUDIT_2026-07-16.md`. P1 STOP je tým
potvrdený v prehľadanom relevantnom korpuse.

## Rozhodovací strom

```text
existujúce premenné a ledgery
        |
        v
P1: uzavretá inventúra zdrojov/stavov
        |-- žiadny lokálny stav + rezervoár --> A4 fundamentálne BLOCKED
        v
P2: M0–M2 algebraický operátor a nulové limity
        |-- poruší ledger/pozitivitu --> príslušná vetva DEAD
        v
P3: M3–M6 časovanie, termodynamika, BBN a reliktný budget
        |-- prázdna množina --> mechanizmus DEAD
        v
P4: M7–M8 poruchy a stabilita
        |-- nestabilita/izokurvatúra --> mechanizmus DEAD
        v
P5: M9 počet voľností + predregistrovaný observačný test
        |-- voľný profil ostáva --> CONDITIONAL FAMILY, nie predikcia
        `-- žiadna voľná funkcia nezostane --> DERIVED PREDICTION
```

## P1 — úplná inventúra bez novej hypotézy

**Otázka:** ktorý už definovaný objekt môže byť lokálny stav `chi` a ktorý
môže energeticky zaplatiť paru?

| Kandidát z dnešnej dokumentácie | Čo treba overiť | Aktuálne známe riziko |
|---|---|---|
| palivo `rho_f` a A1 `Gamma rho_f` | či existuje odvodený lokálny prah/stav, ktorý zdroj prirodzene ukončí | konštantný neskorý `F->C` sám nevytvára skorý parný impulz; pri `F->R` narazí na M-015 |
| jazva/doména I | definovať `n_I,xi`, ich evolúciu, energiu a `T_I^(mu nu)` | Q4/Q8 dnes nemajú operátor ani ledger; nesmie to byť skrytý rezervoár |
| exit/reheating rezervoár | nájsť už existujúcu zložku a jej lokálny transfer | Q18/Q23 zatiaľ definujú otázku, nie objekt |

**PASS P1:** tabuľka všetkých existujúcich kandidátov s presnými zdrojmi,
jednotkami a rozhodnutím „spĺňa / nespĺňa minimálny M0 vstup“.  
**STOP P1:** nijaký existujúci kandidát nemá súčasne lokálny stav, energiu a
párový ledger. Výsledok bude: „v3.18 zatiaľ nemá fundamentálnu A4 funkciu“,
nie „skorá para je fyzikálne nemožná“.

## P2 — uzavretie operátora a dva nulové limity

Pre každý P1 kandidát, ktorý prejde, sa bez numerického fitu zapíše

```text
S_s^mu(Y),  S_e^mu(Y),  sum_A Q_A^mu=0,
rho_A>=0.
```

Povinne sa overia dva limity:

1. vypnutý mechanizmus: `S_s^mu -> 0` vráti pôvodný ledger;
2. po skončení udalosti: `S_s^mu -> 0` a `rho_s -> a^-4`.

**PASS P2:** lokálny, dimenzionálne správny a bilančne uzavretý operátor bez
nového fitovaného času/podielu.  
**DEAD P2:** nevybilancovaná energia/hybnosť, záporná hustota alebo povinný
globálny čas či realizovaný Fourierov mód.

## P3 — mantinely určujú obal funkcie

Z P2 rovníc sa vytvorí systém `dY/dtau=F(Y)`. M2–M6 potom dajú:

- intervaly počiatočných podmienok z energetického rozpočtu;
- hranicu, do ktorej musí zdroj skončiť (BBN a M-015);
- podmienku pozitívnej entropie a stavovej rovnice;
- integrovaný reliktný budget, nie ručne zvolený bump.

**Výstup P3:** dôkaz, či množina riešení `F_allowed` je prázdna, jednoprvková
alebo rodina, plus počet jej voľných počiatočných podmienok.

## P4 — poruchy rozhodnú, či background nie je klamný

Z toho istého operátora sa odvodí `delta S_s^mu`, birth frame, šum a
izokurvatúrne módy. Až potom sa testujú superhorizontové a subhorizontové
mantinely. Žiadna backgroundová zhoda s `Delta N_eff` nesmie preskočiť P4.

## P5 — pozorovania sú súd, nie zdroj vzorca

Pred testom sa zmrazí zvyšná rodina riešení a dataset. BBN, CMB a lensing
potom môžu:

- vylúčiť rodinu (`DEAD`);
- zúžiť ju (`CONDITIONAL FAMILY`);
- alebo potvrdiť už odvodenú trajektóriu v predikovanom intervale.

Ak `x_*`, šírka, amplitúda alebo branch ratio ostanú voľné po P4, musia byť
vydané ako voľné parametre, nie ako predikcia.

## Najbližší vykonateľný krok

**P1.1 — zdrojová mapa existujúcich veličín.** Dokončené read-only auditom
`Audit/Q22A_P1_1_EXISTING_SOURCE_MAP_AUDIT_2026-07-16.md`. Tabuľka
„premenná → lokálny stav? → energia? → evolúcia? → párový ledger? → verdict“
nedala P2-ready kandidáta. Preto sa funkcie ďalej nehádajú; P2 sa otvorí iba
po novom explicitne označenom fyzikálnom vstupe Q4/Q8 alebo Q23.

## Väzby

- `Q22A_EARLY_STEAM_FUNCTION_CONSTRAINT_LEDGER_SK.md`
- `Q22A_CONSTRAINT_TO_FUNCTION_DERIVATION_PROTOCOL_SK.md`
- `Audit/Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md`
- `00_GATE_AND_STATION_CONSTRAINT_LEDGER_SK.md`
