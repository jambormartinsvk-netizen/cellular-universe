# A2 — stav spätného auditu po nálezoch falošných PASS a STOP

**Dátum:** 2026-07-16  
**Otázka:** boli po nájdení implementačných a interpretačných chýb spätne
preverené všetky A2 koľaje tak, aby sa vylúčila falošná smrť aj falošný PASS?  
**Autoritatívna odpoveď:** **nie úplne**. Existujú dôležité čiastkové
retrospektívy, ale balíky R7 a R8 z retrospektívneho master plánu ešte nie
sú uzavreté pre všetky koľaje.

Tento dokument nemení fyzikálny verdikt žiadnej koľaje. Určuje iba mieru
dôvery, s akou možno dnešný verdikt používať, a čo ešte treba zaauditovať.

## Aktualizácia 2026-07-16 po uzavretí R7 a šírkovom audite

- R7 je `CONFIRMED_SCOPE` pre A2-K1, K2, K3, K5 a K6 podľa
  `Audit/A2_R7_POST_ERROR_SCOPE_SEALS_K1_K2_K3_K5_K6_2026-07-16.md`;
- K4 zostáva živá na `60/100`, ale R1–R4/B1 sú iba čiastočne uzavreté;
- pri K7, K8, K9, K11 a K12 je R8 pre-solver blocker presne zmapovaný,
  no formula seal sa môže uzavrieť až pre konkrétnu dcéru s operátorom;
- úplný all-A2 post-error audit preto stále nie je „všetko PASS“, ale už
  vieme, ktoré STOP-y sú dôveryhodné a ktoré živé rodiče sú blokované
  chýbajúcou fyzikou.

## 1. Čo už spätný audit skutočne zachytil

### Falošná alebo príliš široká smrť

| Koľaj | Pôvodný problém | Oprava rozsudku |
|---|---|---|
| A2-K4 | historický M-011 použil `ln(T_K4/T_0)` voči prudko zanikajúcej referencii ako absolútny rast | M-011 bol pozastavený; K4 sa znovu otvorila a prešla do species-first P5 |

### Falošný alebo príliš široký PASS

| Koľaj/implementácia | Pôvodný PASS | Neskorší nález | Aktuálny rozsah |
|---|---|---|---|
| A2-K4 / projektovaná K7 | numerická stabilita a G0–G7 boli vydávané za vysokú podporu K4 | redukovaná RHS nemala dynamické `U_c`; viacero potomkov nieslo aj fixed `K_MPC=0.05` v backgrounde | `IMPLEMENTATION_STOP_FOR_K4`; historické výsledky iba regression/review |
| A2-K4 / KMPC-024 | pomenovaný „úplný“ P5.3g7-M3 seed | PF-058: lokálny stav vynechal dynamické `delta_f,U_f` a fuel continuity/Euler rows | `DO_NOT_USE_PHYSICS`; M1 anchor zostal použiteľný, úplný M3 nie |
| A2-K11 / skript 45 | `PASS_S8_K1b_SUPERHORIZON_GATE` | chybné znamienko a rovnice, tolerančný bypass, nerozlíšená amplitúda, neplatný relatívny constraint; skript vôbec nepočítal `S8` | PASS zamietnutý; K11 prežíva iba ako neodvodená hypotéza |

### Falošné technické FAIL bez zmeny fyzikálneho verdiktu

- A2-K6 skript 48 označil nulový limit ako FAIL pre okrajovú numerickú
  deriváciu a príliš tvrdý prah. Analytický skript 49 dal presné limity a
  spojitý no-go; M-013 sa tým nezrušil, ale zosilnil.
- K4/K7/G8 vetva obsahuje viacero opravených matcherov, znamienok,
  constraintových a škálovacích testov. Immutable staré výstupy ostávajú,
  no nesmú určovať fyzikálny verdikt mimo presne opraveného rozsahu.

Tieto nálezy dokazujú, že audit už našiel chyby v oboch smeroch. Nedokazujú
však, že každá ďalšia A2 koľaj bola po poslednom náleze znovu certifikovaná.

### Rozsah konkrétnej chyby `K_MPC=0.05`

Statické vyhľadanie priameho `K_MPC=0.05`/`k_mpc=0.05` v Python zdrojoch
našlo fyzikálne použitia v potomkoch A2-K4/K7/G8 a v ich auditných
checkeroch. V zdrojoch K1, K2, K3, K5 a K6 sa táto konkrétna konštanta ako
backgroundový vstup nenašla. To znižuje riziko, že práve chyba `k^p`
spôsobila ich rozsudky, ale nie je to náhrada za úplný formula-provenance
audit: iný chybný člen, znamienko, chýbajúci stav alebo tolerančný bypass
môže byť nezávislý od `K_MPC`.

## 2. Stav po jednotlivých A2 koľajach

| Koľaj | Vykonaný spätný audit | Dnešná dôvera vo verdikt | Čo ešte chýba do post-error certifikácie |
|---|---|---|---|
| A2-K1 | R7 parent equation, term map, GI invariant, nulový limit a hash | **vysoká, scope-limited** pre constant-rate `Q parallel u_c` fluid | `R7 CONFIRMED_SCOPE`; iba nový mechanizmus |
| A2-K2 | R7 analytický high-k hlavný symbol a záporné `c_s^2=w` | **veľmi vysoká** pre striktne barotropickú uzáveru | `R7 CONFIRMED_SCOPE`; bez numerického replayu |
| A2-K3 | R7 znamienka, GI relatívny mód, nulový limit a hash | **vysoká, scope-limited** pre constant-rate `Q parallel u_f` fluid | `R7 CONFIRMED_SCOPE`; iba nový operátor |
| A2-K4 | rozsiahly lineage audit odlíšil K7, BR2 a P5; zachytil falošnú smrť aj falošné PASS | **aktívna, ale REVIEW_BLOCKED**; dôverovať iba explicitným P5.1/P5.2 scope PASS | dokončiť R1–R4: `A_f`, coefficient/row manifest, úplné fuel/ash rows, Bianchi/left-null, plný seed a P5.4 |
| A2-K5 | R7 zdrojová akcia, mapa do sily/rastu a nezávislá `A_s` aritmetika | **stredne vysoká, scope-limited** pre konkrétnu akciu; nie pre všetky piate sily | `R7 CONFIRMED_SCOPE`; nepripisovať plný vlastný Boltzmann PASS |
| A2-K6 | R7 presné `G_ij`, nulové limity a spojitý `eta>=0` no-go | **vysoká, scope-limited** pre `f=-f1 rho_c+eta Z^2`, kanonické `G2`, `eta>=0` | `R7 CONFIRMED_SCOPE`; nevzťahovať M-013 na iné operátory |
| A2-K7 | vykonaný breadth triage a viacero dcér má vlastné dôvody smrti | **zmiešaná**; mŕtve dcéry možno citovať iba v ich rozsahu, rodič zostáva otvorený | R8 formula provenance pred každým novým kernelom; celý rodič nemá univerzálny PASS ani STOP |
| A2-K8 | G2 audit dokázal, že samotný number source neurčuje momentum moment; Fc/Ff sa mapujú na K1/K3 | **dobrá pre negatívny test dostatočnosti**, nie pre živú Fkin hypotézu | konkrétny collision kernel a úplný R8 audit pred solverom |
| A2-K9 | G2 audit dokázal degeneráciu rovnakého number/background momentu s rôznym momentum transferom | **dobrá pre negatívny test názvu „jeden operátor“**, nie pre fyzický kernel | konkrétna akcia alebo `C[f]`, nultý/prvý/druhý moment, reakcia a noise; potom R8 |
| A1-K2/A2-K10 | patrí inej backgroundovej route | **nepatrí do reauditu A1-K1/A2** | samostatný A1-K2 background audit pred hodnotením K10 |
| A2-K11 | audit skriptu 45 výslovne zrušil falošný PASS | **nedôverovať žiadnemu starému numerickému PASS**; živá je iba hypotéza | lokálny ortogonálny operátor, úplné rovnice, Bianchi, limity a až potom nový solver |
| A2-K12 | rodič a niektoré dcéry sú rozlíšené; symetrická K12-K1 nepostačila | **čiastočná** | konkrétny párový produkčný kernel, nábojová segregácia, celkový momentum/pressure/noise ledger a R8 audit |

## 3. Čo z toho možno a nemožno tvrdiť

Možno tvrdiť:

- K1–K5 dostali mechanizmovo špecifickú retrospektívu;
- pri K4 sa našla a opravila falošná smrť;
- pri K4 a K11 sa našli falošné alebo príliš široké PASS tvrdenia;
- K6 dostala opravu falošného technického FAIL bez zmeny scope-limited
  smrti;
- K8 a K9 majú korektné lacné negatívne G2 testy dostatočnosti.

Nemožno tvrdiť:

- že všetky A2 koľaje prešli jednotným post-error auditom;
- že žiadny starší PASS alebo STOP už nemôže obsahovať chybu;
- že stará K7 numerika dokazuje aktívnu K4/P5;
- že potvrdený no-go jednej konkrétnej akcie zabíja celú triedu mechanizmov;
- že živé K7/K8/K9/K11/K12 návrhy sú pripravené na solver.

## 4. Povinný uzatvárací program R7/R8

Každá koľaj dostane jeden bounded Markdown balík. Staré skripty sa
nespúšťajú hromadne.

1. **Identity seal:** parent equation, presná verzia, SHA-256, vstupy a
   rozhodujúci artefakt.
2. **Formula provenance:** každý člen rodičovskej rovnice sa zmapuje do
   skriptu alebo analytického no-go; lokálny zoznam premenných sa porovná s
   nadradeným kontraktom.
3. **Nezávislý dôvod rozsudku:** hlavný symbol, Bianchi/left-null,
   eigenvalue alebo observačný invariant sa odvodí nezávisle od machine
   labelu pôvodného runnera.
4. **Povinné limity:** nulová väzba, rozmery, gauge/frame a regulačný limit;
   podľa mechanizmu aj high-k alebo hustotný limit.
5. **Numerický replay iba ak je potrebný:** interný a vonkajší timeout,
   dve rozlíšenia/metódy, netautologické residualy a fail-closed JSON.
6. **Rozsahový verdikt:** `CONFIRMED_SCOPE`, `REOPEN_FALSE_STOP`,
   `WITHDRAW_FALSE_PASS`, `REVIEW_BLOCKED_PARENT` alebo `STOP_SCOPE`.
7. **Zachovanie histórie:** pôvodný artefakt sa nemaže; oprava dostane
   erratum, dôvod a odkaz na nástupcu.

## 5. Odporúčané poradie

1. **Aktívna K4/P5:** dokončiť R1–R4, pretože na nej stojí najbližší A2
   pokus a prípadné G8.
2. **Mŕtve K1–K6:** vytvoriť krátke R7 seals, začať K2 a K6, kde existuje
   najsilnejší analytický invariant; potom K1, K3 a K5.
3. **Záložné K7/K8/K9/K11/K12:** R8 vykonať vždy tesne pred otvorením
   konkrétnej dcéry, nie pre všetky hypotetické kombinácie vopred.
4. **K10:** auditovať iba na samostatnej route A1-K2.

Physics auditor a math/script auditor odovzdajú nezávislé read-only posudky;
iba hlavný orchestrátor smie potvrdiť alebo zmeniť PASS/REVIEW/STOP.

## 6. Bezprostredný záver

Aktuálne rozsudky sa nesmú hromadne zrušiť. Zároveň sa pri release ani pri
výbere náhradnej koľaje nesmú označiť za „post-error certified“, kým nemajú
vyššie uvedený R7/R8 seal. Najväčšiu prioritu má úplné uzavretie K4/P5;
krátke seals mŕtvych K1–K6 majú prebehnúť pred konečným tvrdením, že A1-K1
nemá inú životaschopnú A2 cestu.

## 7. Autoritatívne zdroje tohto statusu

- `Independent_Audits/00_RETROSPECTIVE_AUDIT_MASTER_PLAN_SK.md`;
- `Audit/A2_K1_K5_RETROSPEKTIVNY_AUDIT_MAX_HLBKY_ROVNIC_VYPOCTOV_A_ROZSUDKOV.md`;
- `Independent_Audits/Implementation_Lineage/03_L0B_DEPENDENCY_INVENTORY_SK.md`;
- `Independent_Audits/Implementation_Lineage/05_L2_B1_PROJECTED_K7_RESULT_SK.md`;
- `Independent_Audits/Implementation_Lineage/07_L2_B2_GENERAL_SYNCHRONOUS_RESULT_SK.md`;
- `Independent_Audits/Implementation_Lineage/09_L2_B2_1_BR2_EQUATION_RESULT_SK.md`;
- `Audit/A2_K4_P5_3G7_RERUN2_CONTRACT_PARITY_AUDIT_2026-07-16.md`;
- `Audit/A2_K4_P5_3G7_KMPC024_MULTI_AUDITOR_SYNTHESIS_2026-07-16.md`;
- `Audit/A2_K6_MRTVA_M013_exact_Gij_a_spojity_eta_no_go.md`;
- `Audit/A2_K11_audit_opraveneho_scriptu_45_a_momentum_drag.md`;
- `Audit/A2_K8_1_G2_NUMBER_SOURCE_MOMENT_AUDIT.md`;
- `Audit/A2_K9_1_G2_SINGLE_OPERATOR_MOMENT_AUDIT.md`.
