# A2 — ohraničený šírkový pokus dostať živé koľaje ku G5 = 50/100

**Dátum:** 2026-07-16  
**Rozsah:** A2-K4, K7, K8, K9, K11 a K12  
**Pravidlo:** body sa udeľujú iba za úplne a sekvenčne prejdenú bránu;
chýbajúci fyzikálny operátor sa nesmie nahradiť placeholderom alebo fitom.

## Výsledok jednou vetou

**Jediná živá koľaj A2, ktorá už dosiahla aspoň 50/100, je A2-K4 na
60/100. K7, K8, K9, K11 a K12 zostávajú živými rodičovskými triedami, ale
žiadna dnes nemá konkrétnu dcéru s uzavretou mikrofyzikou potrebnou na
sekvenčný postup ku G5.**

## Stav pokusu

| Koľaj | Stav po pokuse | Hĺbka | Prvá neprejdená brána | Presný blocker |
|---|---|---:|---|---|
| A2-K4 | `REVIEW_BLOCKED_ARCHITECTURE` | `60/100 = G6` | G7 | dokončiť R1–R4/B1: normalizácia `A_f`, coefficient/row manifest, úplné fuel/ash rows, Bianchi/left-null a plný seed |
| A2-K7 | `REVIEW_BLOCKED_PARENT` | `20/100 = G2` | G3 | chýba konkrétny lokálny pozitívny kernel, `delta Q`, retarded/noise/FDT a memory uzáver |
| A2-K8 | `REVIEW_BLOCKED_PARENT` | `10/100 = G1` | G2 | chýba explicitný produkčný collision operator `C[f]`, birth distribúcia a jeho nultý/prvý/druhý moment |
| A2-K9 | `REVIEW_BLOCKED_PARENT` | `10/100 = G1` | G2 | chýba jeden konkrétny maticový element alebo kernel, ktorý naraz určí produkciu, rozptyl, reakciu a noise |
| A2-K11 | `WITHDRAW_FALSE_PASS / REVIEW_BLOCKED_PARENT` | `10/100 = G1` | G2/G3 | projector je iba ansatz; chýba lokálna akcia/kernel, regulárny hustotný limit, reakcia, noise/memory a úplný ledger |
| A2-K12 | `REVIEW_BLOCKED_PARENT` | `10/100 = G1` | G2 | chýba párový produkčný kernel, distribúcia dvoch nábojov, segregácia a spoločný momentum/pressure/noise ledger |

## A2-K7

Breadth triage už otestoval viac konkrétnych listov. Fixed-width cascade,
holý Onsager cross-term, thermal gravity-only bath, nekoherentný lokálny
KMS prechod a vedúca zosilnená spin-2 väzba majú zachované vlastné dôvody
smrti M-014*. Rodič nezomiera, pretože curvature operator alebo nový
nespin-2 bath nie sú týmito no-go vetami pokryté. Nie sú však definované
dostatočne na G3. Ďalší numerický solver by rátal voľný ansatz, nie K7.

## A2-K8

Audit G2 dokázal, že number source určuje backgroundovú produkciu, ale nie
jednoznačne hybnosť, tlak ani šum. Uzávery `Q||u_c`, `Q||u_f` a spoločný
energy-frame sa zlievajú s K1, K3 a K4. Jediná skutočne nová dcéra je
K8-Fkin s úplnou birth distribúciou `C[f]`; tá zatiaľ neexistuje. Preto
rodič ostáva živý na G1, ale nemožno mu udeliť G2.

## A2-K9

Rovnaký nultý/backgroundový moment môže mať rôzne prvé momentum momenty.
Pridaním ľubovoľného elastického `kappa` by vznikli dva nezávislé fitované
kernely, čo porušuje definíciu K9. K9 postúpi iba vtedy, ak jeden konkrétny
proces odvodí produkciu aj rozptyl vrátane pressure/noise. Názov „jeden
operátor“ sám nie je operátor.

## A2-K11

Starý skript 45 nepočíta `S8` a jeho PASS bol zrušený pre chybné znamienka,
neúplné rovnice, tolerančný bypass a nerozlíšenú amplitúdu. Kovariantný
ortogonálny projector môže mať nulový background, ale sám neurčuje
hustotnú závislosť koeficientu ani regulárny `rho_f->0` a `delta->0`
limit. K11 preto prežíva ako fyzikálne odlišná hypotéza, nie ako
implementovaný model.

## A2-K12

Symetrická dcéra K12-K1 je `STOP M-016`, pretože dá nulový čistý tok.
Asymetrická K12-K2 a lokálna párová K12-K3 zostávajú otvorené, ale bez
produkčného kernelu nemožno odvodiť, či opačné náboje zvýšia rozptyl,
prenesú energiu alebo iba vytvoria ďalší príťažlivý/odpudivý mód.

## Prečo sa pokus zastavil pred 50

G2–G3 v týchto koľajach nie sú numerické checkpointy. Sú to definície
fyziky. Bez nich nemožno korektne odvodiť G4 kontinuity/Eulery/Einsteinove
constrainty ani G5 regulárnu superhorizontovú bázu. Pokračovať
placeholderom by zopakovalo chybu, pri ktorej nižší skript už nerátal
pôvodnú formuláciu.

Tento výsledok preto nie je smrť rodičov K7/K8/K9/K11/K12. Je to
`REVIEW_BLOCKED_PARENT` s presným vstupom, ktorý musí dodať nová fyzikálna
dcéra.

## Poradie ďalšieho postupu

1. dokončiť K4/B1 a R1–R4, lebo K4 jediná už prešla G5 aj G6;
2. ako prvú záložnú konštrukciu otvoriť K8-Fkin, lebo priamo zodpovedá
   bunkovej produkcii popola a núti odvodiť momenty z jedného `C[f]`;
3. ak jeden proces prirodzene vytvorí aj rozptyl, povýšiť ho na K9; inak
   K9 nezakladať duplikovaním;
4. K12 otvoriť iba s explicitným párovým kernelom a nábojovou asymetriou;
5. K11 alebo K7 otvoriť až po dodaní lokálnej akcie/kernelu, nie ďalším
   fenomenologickým koeficientom.

## Autoritatívne podklady

- `Audit/A2_K7_REENTRY_AFTER_BREADTH_TRIAGE.md`;
- `Audit/A2_K8_1_G2_NUMBER_SOURCE_MOMENT_AUDIT.md`;
- `Audit/A2_K9_1_G2_SINGLE_OPERATOR_MOMENT_AUDIT.md`;
- `Audit/A2_K11_audit_opraveneho_scriptu_45_a_momentum_drag.md`;
- `Audit/JEDNOTNA_SEKVENCNA_STUPNICA_HLBKY_A2_A_REKALIBRACIA_K1_K12.md`.
