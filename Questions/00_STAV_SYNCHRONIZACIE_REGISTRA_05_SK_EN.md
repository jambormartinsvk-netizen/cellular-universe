# Stav synchronizácie registra 05 — SK/EN

**Aktualizované:** 2026-07-16 — hranica AR70

## Autoritatívne vrstvy

- zmrazený základ SK:
  `theory/SK/05_Methodology_Rules_and_Question_Register_SK.md`;
- zmrazený základ EN:
  `theory/EN/05b_Methodology_Rules_and_Question_Register_EN.md`;
- kumulatívny v3.18 dodatok SK/EN:
  `theory/SK/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_SK.md`
  a `theory/EN/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_EN.md`;
- neskoršie párové tematické dodatky v `theory/SK/` a `theory/EN/` sú
  zmrazené historické pracovné artefakty.

Základné registrované pravidlá sa spätne nemenia. Od AR70 nové pravidlo
najprv dostáva párovú pracovnú deltu v príslušnej hĺbke `tracks`; spoločné
pravidlo patrí do `tracks/METHODOLOGY/`. Do `theory/` sa prijaté delty
konsolidujú až pri release candidate. Neskorší audit obmedzí staršie
tvrdenie cez explicitný scope záznam alebo HISTORY udalosť.

## Stav páru po reorganizácii

| Rozsah | SK | EN | Stav |
|---|---|---|---|
| AR67 | `05_AR67_Evidence_Priority_and_Confirmed_Stop_SK.md` | `05_AR67_Evidence_Priority_and_Confirmed_Stop_EN.md` | pair |
| AR68 | `05_AR68_Gate_and_Station_Constraint_Passports_SK.md` | `05_AR68_Gate_and_Station_Constraint_Passports_EN.md` | pair |
| AR69 | `05_AR69_Canonical_Artifact_Ownership_and_Base_Core_SK.md` | `05_AR69_Canonical_Artifact_Ownership_and_Base_Core_EN.md` | pair |
| L1–L7 | v3.18 kumulatívny dodatok | v3.18 kumulatívny dodatok | mirrored scope limitations |
| Q20 PF-058 status | v3.18 kumulatívny dodatok, riadok Q20 | v3.18 kumulatívny dodatok, row Q20 | mirrored `REVIEW_BLOCKED_ARCHITECTURE` |

AR69 nie je duplicitou AR59/61/62: AR59 definuje route, AR61 append-only
históriu, AR62 verziovanie jadra a AR69 ich spája do povinného vlastníckeho
manifestu jedného behu.

Pozor: starý manifest `theory/05c_REGISTER_v3.18_SK_EN_MANIFEST.md` už
nezodpovedá aktuálnym hashom pracovného páru 05c a historická rodina má 11
kolíznych skupín AR/Q ID. Aktuálna evidencia je v
`Audit/THEORY_05_FAMILY_LOCATION_AND_AUDITOR_COMPLIANCE_AUDIT_2026-07-16.md`
a `tracks/METHODOLOGY/00_IDENTIFIER_COLLISION_LEDGER.md`.

## Release kontrola

Pri zostavení v3.18 sa základ, prijaté pracovné delty a historické dodatky
rekoncilujú do jedného vydávacieho registra bez prepisu pôvodných častí.
Nesmú sa iba mechanicky spojiť: historická rodina obsahuje kolízne AR/Q
identifikátory, ktoré treba vyriešiť s explicitnou mapou. Pred release sa
overí množina AR/Q/L identifikátorov v SK a EN, odkazy, SHA-256, changelog
a Git tag.

Aktuálny pracovný zdroj pravdy je
`tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md`
a jeho EN pár. Klasifikácia starých súborov je v
`tracks/METHODOLOGY/HISTORY/00_THEORY_05_LEGACY_INVENTORY.md`.
