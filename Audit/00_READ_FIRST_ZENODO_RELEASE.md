# Čítaj ako prvé — Zenodo vydania

## Aktuálne rozhodnutie

```text
R3.18-DOC  = NO-GO ZATIAĽ; odporúčané najbližšie vydanie
R3.18-PHYS = NO-GO bez príslušných fyzikálnych brán
v4.0       = NEOTVORENÁ; fundament sa zatiaľ nemení
```

## Autoritatívne dokumenty

1. `Questions/ZENODO_VERSION_PUBLICATION_CRITERIA.md` — kedy vydať/nevydať verziu a patch/minor/v4 hranica;
2. `Questions/ZENODO_RELEASE_CHECKLIST_v3.18.md` — povinné GO/NO-GO kontroly;
3. `Questions/ZENODO_CHANGELOG_TEMPLATE.md` — povinná štruktúra changelogu;
4. `Questions/00_AKCNY_PLAN_v3.18_ADDENDUM_ZENODO_RELEASE_GATE.md` — poradie práce;
5. `Audit/ZENODO_VERSION_PUBLICATION_POLICY_GAP_AUDIT_2026-07-14.md` — dôvod a vzťah k AR5/AR9;
6. SK/EN register AR48 a Q74.

## Najdôležitejšie pravidlá

- Zmena publikovaného súboru vždy znamená novú verziu.
- Patch nesmie meniť rovnice, čísla, verdikty, scope ani záver.
- Materiálna zmena bez zmeny fundamentu zostáva v rade `3.x`.
- Zmena fundamentálnych postulátov alebo jadrovej dynamiky vyžaduje `4.0`.
- Timeout, jedna podbrána, nový pracovný súbor ani desatinný bod skóre samy nevyvolávajú Zenodo release.
- Každý release musí mať changelog, manifest/SHA-256, Git commit/tag, audit zmrazeného kandidáta a post-publish hash kontrolu.

## Aktuálne blokery R3.18-DOC

- upratanie a mapa dokumentácie;
- jediný verejný stavový pointer;
- changelog v3.17 -> v3.18;
- SK/EN cross-check;
- čistý release balík a celkový manifest;
- Git commit/tag;
- nezávislý release audit.

