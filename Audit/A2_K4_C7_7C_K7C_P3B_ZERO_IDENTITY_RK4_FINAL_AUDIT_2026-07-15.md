# A2-K4 / C7.7c / K7c / P3b — konečný audit RK4 po kanonizácii presných núl

**Dátum:** 2026-07-15  
**Stabilné ID:** `SCI-A2K4-C7G5-K7C-P3B-ZERO-IDENTITY-RK4`  
**Rozsudok:** `PASS_P3B_ZERO_IDENTITY_RK4_CONVERGENCE`  
**Hĺbka A2-K4:** `66.5/100`, bez zmeny  
**Celý C7-G5:** `PARTIAL PASS / REVIEW`, nie úplný PASS

## Otázka testu

P1 ukázalo nekonvergentný klasický RK4 pomer `0.367129155...` a rozdiel
200/400 `3.9312396406e-6`. P2 vylúčilo hypotézu „stačí math.fsum“ a P3a-A
dokázalo, že dva koeficienty v rovnici `M'` sú z registrovaných definícií
presne nula. P3b preto testovalo, či práve ich float64 vyhodnocovanie ako
rozdielov takmer rovnakých čísel spôsobovalo zlyhanie krokovej konvergencie.

Jediná fyzikálna zmena voči skriptu 197 bola kanonizácia:

- `(1.5*Ob-Wg*load_fraction)*U_gamma -> 0`,
- `(0.25*Wg*inv1r-0.5*Og)*delta_gamma -> 0`.

Seed, background, 13-zložkový stav, closure `L5=0`, interval, normy,
checkpointy, RK4 kroky a rozhodovacie prahy zostali nezmenené. Statický
AST/source-delta audit 207 potvrdil, že nepribudla iná zmena RHS.

## Očakávanie zapísané pred behom

| Veličina | Preregistrovaná brána | Pozorovanie | Stav |
|---|---:|---:|---|
| rozdiel 200/400 | `< 1e-6` | `3.0308221210528785e-14` | PASS |
| klasický RK4 pomer | `8–32`, centrum približne 16 | `16.004120997052343` | PASS |
| hustotný constraint | `< 5e-12` | max. `1.3672192413960893e-22` | PASS |
| hybnostný constraint | `< 5e-12` | max. `4.32321445172391e-17` | PASS |
| safety cap | `<= 1` normalizovane | `1.0` | PASS |

Odchýlka pomeru od ideálneho štvrtého rádu 16 je `0.004121`, približne
`0.0258 %`. Rozdiel 200/400 sa oproti P1 zmenšil o viac než osem rádov.
Dominantnou zložkou najjemnejšieho rozdielu je `delta_f`, nie pôvodné `M`.

## Kauzálny rozsudok

V presne testovanom NID/deep intervale 0,25 e-foldu bola príčinou starého
ne-RK4 správania numerická reprezentácia dvoch algebraicky nulových
koeficientov. Nie je to nový fyzikálny člen ani dôkaz nestability módu.
Výsledok je kauzálny v rámci tohto testu, pretože source-delta audit povolil
iba tieto dve zmeny a následný pomer sa vrátil na očakávaný štvrtý rád.

## Ktoré staršie tvrdenia sú obmedzené

1. P1 a skript 197 zostávajú platnou reprodukciou **legacy float64 zápisu**.
   Už sa však nesmú používať ako dôkaz fyzikálnej nekonvergencie kanonických
   rovníc ani ako aktuálny blocker opravenej formulácie.
2. Mŕtva vetva `K7c.3e fsum-only` zostáva mŕtva. P3b ju neoživuje, pretože
   `math.fsum` neopravovalo vznik chyby pri zostavení koeficientu.
3. P3a-A zostáva samostatným dôkazom presnej identity; P3b je samostatný
   evolučný dôkaz. Ani jeden sa nesmie spätne zameniť za druhý.
4. Historický G5 FAIL sa pre opravenú formuláciu mení na `PARTIAL PASS / REVIEW`:
   kroková RK4 konvergencia na jednej ploche prešla, no celá brána vyžaduje
   aj tolerančnú a metódovú konvergenciu.

## Čo test nedokázal

- netautologické G4 constrainty a aktivitu pozdĺž celej trajektórie;
- NID aj NIV na deep aj shallow povrchu, teda C7-G6;
- plný požadovaný interval a deep/shallow endpoint agreement;
- plnú fotónovú/neutrínovú Boltzmannovu hierarchiu;
- CMB, `S8`, `H0` ani likelihood;
- fyzikálnu správnosť samotného K4 mechanizmu mimo auditovaného systému.

Preto zostáva A2-K4 na `66.5/100` a preregistrovaný `score_effect` je `NONE`.
To neznamená nulový vedecký význam: odstránil sa predchádzajúci blocker,
ale ešte sa neuzavrela celá vážená brána.

## Dôkazy a kontrolné súčty

| Artefakt | SHA-256 |
|---|---|
| `scripts/205_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_audited.py` | `B7EC8BAD3BFB0D48EC91D6F1BB0A602FA1834A021BB94C92D6D1B398D5F3CDC2` |
| `Audit/A2_K4_K7C_P3B_ZERO_IDENTITY_RAW_2026-07-15.json` | `D4C66810FD799C31329012A0C9684EBCE8452EEB0E4EBF285F748E07D06242F2` |
| `Audit/A2_K4_K7C_P3B_20260715_grid100.json` | `5F7CC28A2DD832CCCAB038B611E4B2EF88CE96EFA1C73C89E6380D7304668E0D` |
| `Audit/A2_K4_K7C_P3B_20260715_grid200.json` | `1BA3F90A446169097FAACEDF0A0F237CA7ACA55251A007E647CAC26FD590E316` |
| `Audit/A2_K4_K7C_P3B_20260715_grid400.json` | `9E3C73D635924E829A5F57BA540EBB1F5861F67F21CFCE69BD93423D6FA8FC8D` |
| source-delta raw 207 | `AE07F945D4B199D0E47A41227A62FE3C2747D8FCA9B51EB4583748673C51A904` |
| corpus checker raw 208 | `EF485ECE8102D0210E38406C6A0D0D21EFD84C11E23B0868222FBEE151AC0C26` |
| preregistrácia P3b | `5FF6A16B60CC5AFFF7D62F1F1C92D85E5F3D7DCBCFACF1DA97ED8E9C1F04AA8F` |

## Ďalší postup

Pripraviť samostatnú preregistráciu, nie okamžitý široký beh:

1. dokončiť C7-G5 metódovým a tolerančným cross-checkom na rovnakej ploche;
2. definovať a spustiť netautologickú C7-G4 activity/constraint bránu;
3. až po ich PASS rozšíriť identický kanonický operátor na C7-G6:
   NID/NIV × deep/shallow;
4. ak ktorákoľvek plocha zlyhá fyzikálne pri platnej numerike, zachovať jej
   výstupy a vydať lokálny STOP; timeout alebo technická chyba zostáva REVIEW.
