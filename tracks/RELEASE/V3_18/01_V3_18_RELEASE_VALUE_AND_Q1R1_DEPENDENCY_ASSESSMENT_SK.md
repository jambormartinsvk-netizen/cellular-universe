# v3.18 — prínos verzie, závislosť od Q1R1-V3 a odporúčanie na vydanie

**Dátum:** 2026-08-01  
**Autorita posúdenia:** hlavný orchestrátor; finálne vydanie schvaľuje Martin Jambor  
**Release trieda:** `R3.18-DOC / ERRATUM`  
**Odporúčanie:** `VYDAŤ PO DOKONČENÍ 14-SÚBOROVÉHO RC A JEHO NEZÁVISLOM AUDITE`  
**Zenodo upload/publish:** ručne vykoná Martin Jambor; projekt pripraví a overí súbory, manifesty a kontrolné súčty

## 1. Je výsledok Q1R1-V3 potrebný pre v3.18?

Nie. Autoritatívny stav Q1R1-V3 už navyše nie je „bežiaci výpočet“, ale:

```text
TECHNICAL_SUPPORT_LINE_CLOSED / CHECKPOINT_ACCEPTED
SOURCE_SUPPORT_CLOSED / CHECKPOINT_ACCEPTED
```

Výsledok je v
`tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/292_B6B2_10_H_RDIV_C01_RW1_Q1R1_V3_SOURCE_ARCHIVE_ELIGIBILITY_RESULT_SK.md`.
Source archív bol získaný a prijatý ako reusable boundary, ale jeho presný
vedecký výsledok ostal
`REVIEW_Q1R1_SOURCE_ARCHIVE_ELIGIBILITY_UNRESOLVED`. G0 až G2 potvrdili iba
spôsobilosť zdroja; G3 nedodal potrebný konečný kladný work/barrier witness.
Nevznikla žiadna fyzikálna inferencia pre C01/P5.

Result292 výslovne nemení:

- hĺbku `A2-K4 = 60/100`;
- skóre P5 `3.5/6`;
- stav A1-K1 alebo A3;
- `H0`, `S8`, `Delta N_eff` ani inú predikciu;
- release stav v3.18.

Q1R1-V3 nie je vstupom zmrazeného 14-súborového release write setu.
Pre v3.18 preto netvorí release blocker. Ak v aplikácii stále vyzerá ako
bežiaca úloha, jej ďalšia source operácia alebo fyzikálny výpočet nie je
podľa živého handoffu autorizovaný; najprv sa má zosúladiť s prijatým
result292, nie čakať na ňu s vydaním.

## 2. Čo v3.18 reálne prináša

### 2.1 Opravu vedeckej poctivosti publikovaných tvrdení

V3.18 nebude predstierať, že všetky čísla z v3.17 zostávajú odvodenými
predikciami. Zavedie explicitné stavy `derived`, `conditional`, `hypothesis`,
`open`, `withdrawn` a `historical` a ku každej zmene uvedie dôvod a evidence.

Najdôležitejšie zmeny prediction statusov:

| ID | Koncept | Stav v3.18 | Hlavná zmena oproti v3.17 |
|---|---|---|---|
| P01 | `N_eff / Delta N_eff` | `SCOPE_NARROWED / NOT_YET_AVAILABLE` | tvrdá hodnota sa nevydáva ako odvodená, kým nie je odvodený zdroj |
| P02 | `n_s` | `RECALCULATION_OPEN` | historické číslo ostáva označené ako v3.17, nie current |
| P03 | `r` | `RECALCULATION_OPEN` | stará horná hranica nie je potvrdená ako current |
| P04 | `H0` | `RECALCULATION_OPEN` | iba tri podmienené legacy-anchor body, nie tvrdá predikcia |
| P05 | `S8` | `RECALCULATION_OPEN` | iba podmienená simplified-growth citlivosť |
| P06 | `w0, wa` | `SCOPE_NARROWED` | jeden konzistentný SK/EN status bez nadmerného claimu |
| P07 | priama detekcia DM/popola | `SCOPE_NARROWED` | žiadny absolútny zákaz interakcie bez odvodeného mechanizmu |
| P08 | presný vzťah `n_s-w` | `WITHDRAWN` | presná formula sa odvoláva; broad shared-delta hypotéza ostáva otvorená |
| P09 | drift `delta` | `NOT_YET_AVAILABLE` | bez neodvodenej časovej funkcie |
| P10 | Lorentz/disperzia | `SCOPE_NARROWED` | iba párnosť auditovaného scalar cosine-Laplacian operátora; nie photon claim |
| P11 | termálne gravitónové pozadie | `RECALCULATION_OPEN` | `0.90 K / 53 GHz` sa nevydáva ako potvrdená current predikcia |

### 2.2 Externe reprodukovanú diagnostiku H0/S8

V3.18 môže uviesť tri diskrétne body:

| `Delta N_eff` | podmienené `H0` [km/s/Mpc] | podmienené `S8` |
|---:|---:|---:|
| `0` | `65.79213819466531` | `0.8856095825403126` |
| `0.02675` | `66.08320294879377` | `0.8800254370658636` |
| `0.0535` | `66.37433224357665` | `0.874499891729803` |

Všetkých deväť final grid cells prešlo interným auditom a externý T2 audit
ich reprodukoval. R2 následne uzavrel package-control finding bez dosahu na
vedecké tvrdenie.

Povinný význam zostáva obmedzený: sú to
`THREE_DISCRETE_CONDITIONAL_LEGACY_ANCHOR_SENSITIVITY_POINTS`, nie likelihood,
posterior, interval, fit ani tvrdá predikcia. `H0` používa syntetickú kotvu
`h_ref=0.673`; `S8` zjednodušený rast a `sigma8_LCDM=0.811`.

### 2.3 Auditovateľnejšiu metodiku

Nový konsolidovaný SK/EN register 05aa má zverejniť najmä:

- systém staníc, koľají, podkoľají a fyzikálnych mantinelov;
- zákaz mazania mŕtvych koľají, ich dôvodov, skriptov a výpočtov;
- oddelenie technickej chyby od fyzikálneho STOP;
- desaťchybové technické dávky a povinnú autorovu bránu;
- dvojfázový DEV -> RC -> nezávislý audit -> official workflow;
- claim quarantine a klasifikáciu P0/T1/S1-S4;
- checkpoint DAG, immutable hashe a opakovateľné externé audity;
- zákaz povýšiť pracovnú interpretáciu alebo toy výpočet na fyzikálnu vetu.

### 2.4 Transparentnú históriu verzií

V3.18 pridá:

- changelog `OLD -> NEW -> REASON -> EVIDENCE`;
- nový SK/EN main dokument bez tichého prepisu v3.17;
- statusovú tabuľku predikcií namiesto miešania historických a current claimov;
- release-scope/nonclaim dokument v oboch jazykoch;
- staging manifest a SHA-256 manifest;
- presnú Git/Zenodo provenienciu.

Git archival baseline už bol prijatý a zálohovaný:

```text
branch = codex/v3.18-release
commit = e9e3579afdffc3c719f0beabb4ec33929cfb4d62
tree = 6e317b76e17c08febb800fcc80742c77c8801aeb
Zenodo v2.0 byte parity = 16/16
independent archival review = PASS
```

Tento commit je nemenný historický rodič v3.18, nie finálny obsah release
stromu. Finálny `codex/v3.18-release` current tree bude obsahovať iba 14
v3.18 release súborov, `LICENSE` a `.gitattributes`. Staré v3.17 súbory a
publikované skripty zostanú auditovateľné cez commit `e9e3579...` a Zenodo
2.0, ale nebudú zavadzať vedľa aktuálnej verzie. Desiatka nájdených
`theory/theory/...` duplikátov sa odstráni spolu s ostatnými superseded
cestami až po úspešnom successor preflight.

## 3. Čo v3.18 neprináša

V3.18 nesmie tvrdiť:

- dokončenie A2-K4 alebo vstup do A3;
- odvodenú univerzálnu funkciu palivo -> hmota/para/popol;
- uzavretie G8 alebo G9;
- plnú fotónovú/neutrínovú Boltzmannovu hierarchiu a CMB likelihood;
- nový validovaný interval alebo posterior pre `H0` alebo `S8`;
- odvodenú tvrdú hodnotu `Delta N_eff`;
- potvrdenú current predikciu `n_s`, `r`, `w0`, `wa`, `0.90 K` alebo `53 GHz`;
- experimentálne potvrdenie bunkovej ontológie.

Preto je správne označenie `R3.18-DOC / ERRATUM`, nie `PHYS`,
`PREDICTION` alebo v4.

## 4. Má zmysel v3.18 vydať?

Áno, ale jej hodnota je korekčná a metodická, nie triumfálna.

Najsilnejší dôvod na vydanie nie je nové „headline“ číslo. Je ním to, že
publikovaná v3.17 obsahuje formulácie a čísla, ktorých dnešný auditný status
je už užší, otvorený alebo odvolaný. Nevydaním by verejná verzia zbytočne
dlho prezentovala staršie odhady bez dnešných obmedzení. V3.18 preto zvyšuje
vedeckú dôveryhodnosť tým, že:

1. opraví rozsah claimov bez prepisovania historickej verzie;
2. ukáže, čo je skutočne auditované a čo ostáva otvorené;
3. zverejní prvý externe reprodukovaný, hoci podmienený, H0/S8 výsledok;
4. umožní budúcemu auditorovi pokračovať z hashovo viazaných checkpointov;
5. pripraví projekt na neskoršiu fyzikálnu verziu bez zamieňania pracovných
   hypotéz s predikciami.

Vydanie by nemalo zmysel iba vtedy, ak by sa prezentovalo ako dôkaz teórie
alebo nová presná kozmologická predikcia. V zmrazenom DOC/ERRATUM scope má
zmysel a odporúčam ho vydať.

## 5. Čo ešte treba dokončiť pred ručným Zenodo uploadom

1. nezávisle schváliť exact mapu finálneho 16-súborového Git stromu a
   podmieneného odstránenia 25 starých/duplicitných ciest;
2. vytvoriť presne zmrazených 14 release súborov v
   `D:/Teoria-v3.18-release`;
3. overiť 11-ID SK/EN parity prediction tabuľky;
4. overiť SK/EN parity main dokumentu, 05aa a release-scope dokumentu;
5. dokončiť changelog, link/DOI audit, UTF-8 a CSV kontrolu;
6. vytvoriť staging manifest a SHA-256 manifest;
7. až potom odstrániť exact 25-path allowlist a overiť exact 16-path
   current tree v čistom checkoute;
8. vykonať nezávislý frozen-RC documentation/release audit;
9. commitnúť a pushnúť presný RC; aktualizáciu `main` a immutable tag
   `v3.18` vykonať až po explicitnom release GO;
10. Martin Jambor ručne nahrá presný 14-súborový manifestový set na Zenodo;
11. pred publikovaním porovná Zenodo preview s manifestom;
12. po publikovaní stiahnuť súbory zo Zenodo a znovu overiť hashe.

Q1R1-V3 nie je súčasťou tohto critical pathu.

## 6. Evidence

- `tracks/RELEASE/V3_18/00_R3_18_DOC_RELEASE_CONTRACT_2026-08-01_SK.md`
- `tracks/RELEASE/V3_18/PT1_H0/00_WORK_PLAN.md`
- `tracks/RELEASE/V3_18/PT1_H0/ARTIFACTS/H0_S8_C2_C3_RESULT_AND_INTERNAL_AUDIT_2026-08-01_SK.md`
- `tracks/METHODOLOGY/00_RELEASE_PROMOTION_LEDGER.md`
- `Audit/V3_18_RELEASE_READINESS_AUDIT_2026-07-28_SK.md`
- `tracks/A1/A1K1/A2/A2K4/00_TRACK.md`
- `tracks/A1/A1K1/A2/A2K4/00_WORK_PLAN.md`
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/292_B6B2_10_H_RDIV_C01_RW1_Q1R1_V3_SOURCE_ARCHIVE_ELIGIBILITY_RESULT_SK.md`
