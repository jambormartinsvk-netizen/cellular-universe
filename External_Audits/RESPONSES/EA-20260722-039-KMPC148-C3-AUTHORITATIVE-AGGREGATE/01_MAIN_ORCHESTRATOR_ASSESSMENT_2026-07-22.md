# Hlavný posudok EA-039 — KMPC-148 C3 aggregate

**Dátum:** 2026-07-22  
**Autorita:** hlavný orchestrátor  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Rozhodnutie:** `ACCEPT_T2_AGREE_IN_SCOPE_WITH_PROCESS_LIMITATIONS`

## 1. Vstupy posudku

| vstup | výsledok / SHA-256 |
|---|---|
| externý T2 audit `00_AUDITOR_AUDIT.md` | `AGREE_IN_SCOPE`; `4ADC2B0759DAB2EC3AE5995D6D36966C38C219925ED83D1F1ACFF82172FD284A` |
| interný audit 243 | `PASS_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45`; `39296FA5A02FA8F103A25AF6D29D04960CFCA57BCAF1620F6FB6005E7251353E` |
| immutable live raw KMPC-148 | `C493B102859CE6181F42BABDFE69A12C9D3B5900040F796D2DECAE0403678238` |
| druhý read-only procesný agent | `AGREE_WITH_LIMITATION`; bez zápisu do projektu |

Hlavný posudok čítal celý externý audit a overil jeho SHA. Externý auditný
súbor sa neprepisuje; tento dokument je nová autoritatívna response vrstva.

## 2. Prijatá T2 evidencia

Externý audit v čerstvých kópiách reprodukoval bez odchýlky:

- R6 preflight `212/212`, manifest `25/25`, runtime closure `22/22`;
- compile, help, smoke a official s exit `0/0/0/0`;
- generated JSON SHA `82CB60CC2D766D85B225745A20C5244F02F6B793DF30B985BC9E23D2B69CE0A4`;
- exact nezávislý register `45/45`, unikátnych `45`, mode counts
  `9/9/9/9/9`;
- rekurzívny field diff `0` po jedinej povolenej normalizácii top-level
  `runtime_seconds`;
- missing-pair a missing-authority guard s exit `3`, iba technickým
  failure receiptom a bez success rawu alebo fyzikálneho verdiktu;
- exact nemennosť 32-súborového package snapshotu pred/po auditných behoch.

T2 odporúčanie `AGREE_IN_SCOPE` sa prijíma.

## 3. Autoritatívny vedecký stav

EA-039 nezvyšuje vedecký score a nemení jednotlivé C3 atómy. Potvrdzuje
iba reprodukovateľnosť ich read-only autoritatívneho indexu:

```text
AD 9/9 + CDI 9/9 + BI 9/9 + NID 9/9 + NIV 9/9 = C3 45/45.
```

Zostáva v platnosti:

- C3: `PASS_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45`;
- K4: `LIVE / 60/100`;
- P5: `3.5/6`;
- P5.4: `NOT RUN`;
- G8/G9: `BLOCKED`;
- release, Zenodo a prediction table: bez zmeny.

Toto nie je T3, nový fyzikálny solve, dátový fit ani dôkaz empirickej
pravdivosti celej teórie.

## 4. Prijaté procesné obmedzenia a náprava

### P-039-01 — nesprávny live-file count (`MATERIAL_PROCESS_ONLY`)

Zapečatený dokument 00 uvádza `LIVE_FILES_CHANGED=6`. Exact pracovná stopa
je:

```text
LIVE_SCIENTIFIC_ARTIFACTS = 5
  base + runner + preregistrácia + raw + interný audit

LIVE_CENTRAL_REGISTERS_UPDATED = 3
  DNR + current execution plan + package register

LIVE_FILES_CHANGED_TOTAL = 8
AUDIT_PACKAGE_COPIES = 25
PACKAGE_CONTROL_FILES = 7
RESPONSE_FILES_AT_HANDOFF = 1
```

Limity `5` vedeckých artefaktov, najviac `4` registrov a celkový auditný
budget `<40` boli dodržané. Chyba neovplyvňuje T2, C3 ani K4, ale pôvodný
počet `6` sa nesmie ďalej citovať ako celkový live count.

EA-039 zostáva zapečatený a nemení sa. Oprava je zámerne iba v tejto novej
response vrstve. Protokol bol pre ďalšie balíky zmenený na samostatné
počítadlá scientific artefacts, central registers a total.

### P-039-02 — preregistračný freeze (`MINOR_PROCESS`)

Časová stopa podporuje správne poradie: preregistrácia existovala pred
rawom a pred prvým Python procesom bol zaznamenaný hash
`110FCE7195A2ECBC972A23D74AF9804245DCB801588E28C4F6B872B056E26B20`.
Po official behu však ten istý dokument dostal execution ledger a jeho
finálny hash sa zmenil na
`26ECB5963E87951AE29B101219D661AAB6E9393099BA13A8A2327059454A3283`.

Preto sa prijíma označenie
`PREREG_CHRONOLOGY_PROCESS_ASSERTION_ONLY`: poradie je podporené, ale
package neobsahuje samostatný immutable pre-run receipt. Od ďalšieho atómu
je úprava preregistrácie po prvom Python procese zakázaná; execution ledger
musí byť samostatný result/audit dokument.

### P-039-03 — protokol R5/R6 (`MINOR_DOCUMENTATION`)

Protokol mal hlavičku R5, hoci povinný preflight a closure pravidlá už
používali R6. Hlavička aj revízny popis boli zosúladené na R6 a doplnené o
presné count/freeze pravidlá.

### P-039-04 — meno auditného agenta (`EDITORIAL_PROVENANCE`)

Orchestračná úloha, ktorá vytvorila externý T2 audit, je evidovaná ako
agent `Ohm`, ale metadata auditného súboru uvádzajú `Lagrange`. Druhý
read-only procesný agent bol evidovaný ako `Lagrange`. Ide o editorial
provenance mismatch bez vplyvu na príkazy, hashe, generated JSON alebo T2
výsledok. Auditný súbor sa neprepisuje; budúce response musia prevziať meno
priamo z orchestration identity.

## 5. Ďalší povolený uzol

Externý checkpoint EA-039 je týmto autoritatívne spracovaný. Ďalší krok
nie je P5.4 ani nový numerický C3 suffix. Povolená je iba samostatná
teoretická predregistrácia S-M/Q18/Q22, ktorá musí pred akýmkoľvek Pythonom
odvodiť alebo explicitne uzavrieť:

1. nultý moment produkcie energie pary a väzbu na palivo/popol;
2. prvý moment prenosu hybnosti a Eulerove znamienka;
3. tlak, shear, vyššie momenty a decoupled hierarchiu;
4. čas produkcie, thermalizácie a decouplingu;
5. koreláciu s AD/CDI/BI/NID/NIV alebo nový nezávislý mód;
6. total-energy/total-momentum identity a nulový limit;
7. pozitivitu, regularitu a kauzalitu; historické `Delta N_eff=0.0535`
   iba vykázať ako superseded legacy sensitivity case, nie vynútiť ako
   rovnosť ani podľa neho ladiť kernel.

Kým tento kontrakt nevznikne a neprejde vlastným auditom, P5.4, G8 a G9
ostávajú zakázané. Samotné prijatie EA-039 nepredregistruje nový výpočet.
