# Návrh adresárovej štruktúry koľají, skriptov a auditov

Dátum: 2026-07-15  
Stav: návrh na schválenie pred fyzickým presunom  
Odporúčanie: dvojvrstvová migrácia — najprv logický strom a manifesty, potom kontrolovaný presun

## Základný princíp

Každý skript, výsledok a audit má práve jedno kanonické miesto. `PASS`, `REVIEW` a `STOP` obsahujú rozhodovacie MD záznamy s odkazmi na dôkazy; neobsahujú duplicitné kópie skriptov. Mŕtva koľaj zostáva v strome so svojím `STOP` rozhodnutím, dôvodom smrti, výpočtami, skriptmi a možnou podmienkou znovuotvorenia.

## Navrhovaný koreň

```text
tracks/
├── 00_READ_FIRST.md
├── 00_GLOBAL_TRACK_REGISTER.md
└── A1/
    ├── 00_INDEX.md
    ├── PASS/
    ├── REVIEW/
    ├── STOP/
    ├── HISTORY/
    ├── ARTIFACTS/
    │   ├── scripts/
    │   ├── results/
    │   ├── audits/
    │   └── questions/
    ├── A1K1/
    │   ├── 00_TRACK.md
    │   ├── PASS/
    │   ├── REVIEW/
    │   ├── STOP/
    │   ├── HISTORY/
    │   ├── ARTIFACTS/
    │   └── A2/
    │       ├── 00_STAGE.md
    │       ├── PASS/
    │       ├── REVIEW/
    │       ├── STOP/
    │       ├── A2K1/
    │       ├── A2K2/
    │       ├── A2K3/
    │       ├── A2K4/
    │       ├── A2K5/
    │       ├── A2K6/
    │       ├── A2K7/
    │       ├── A2K8/
    │       ├── A2K9/
    │       ├── A2K11/
    │       └── A2K12/
    └── A1K2/
        └── A2/
            └── A2K10/
```

A2-K10 je podľa aktuálneho auditu odlišná backgroundová vetva A1-K2. Nemá byť kanonicky vložená pod A1-K1 iba preto, aby čísla 1–12 tvorili súvislý zoznam. V `A1K1/A2/00_STAGE.md` bude viditeľný odkaz na kanonické `A1K2/A2/A2K10`, bez duplikácie.

## Povinná štruktúra každého uzla koľaje

```text
A2Kx/
├── 00_TRACK.md
├── PASS/
│   └── 00_INDEX.md
├── REVIEW/
│   └── 00_INDEX.md
├── STOP/
│   └── 00_INDEX.md
├── HISTORY/
│   ├── SUPERSEDED/
│   └── ERRATA/
├── ARTIFACTS/
│   ├── 00_MANIFEST.md
│   ├── scripts/
│   ├── results/
│   ├── audits/
│   └── questions/
└── DEPENDENCIES.md
```

`00_TRACK.md` musí obsahovať: rodiča, hypotézu ľudskou rečou, rozdiel oproti súrodencom, aktuálny stav, maximálnu auditnú hĺbku, prejdené brány, otvorené brány, stop kritériá, posledné rozhodnutie, deti a staršie formulácie obmedzené neskorším auditom.

`ARTIFACTS/00_MANIFEST.md` musí mať pre každý súbor: ID, kanonickú cestu, SHA-256, typ, vstup, výstup, runtime limit, status skriptu, predchodcu/nástupcu, rozhodnutie, ktoré podporuje, a posledný úspešný spätný audit.

## Význam stavových adresárov

- `PASS`: konkrétna brána prešla. Neznamená, že celá teória alebo rodičovská koľaj je pravdivá.
- `REVIEW`: výpočet je konečný, ale nedostatočný, nekonvergentný, technicky otvorený alebo čaká na ďalšiu bránu.
- `STOP`: koľaj alebo podkoľaj je mŕtva; povinný je identifikátor smrti, dôvod, dôkaz a podmienka prípadného znovuotvorenia.
- `HISTORY/SUPERSEDED`: technicky alebo metodicky nahradený artefakt bez tvrdenia fyzikálnej smrti.
- `HISTORY/ERRATA`: neskôr nájdená chyba a presný dosah na staršie tvrdenia.

## Detailný návrh A2-K4

```text
A2K4/
├── 00_TRACK.md
├── PASS/  REVIEW/  STOP/  HISTORY/  ARTIFACTS/
├── CORE_SUPERHORIZON/          # skripty 27–31 a 64
├── K4_1/
├── K4_2/
├── K4_3a/                      # vrátane skriptu 72
├── K4_3b_RG/
│   ├── BR1/
│   ├── BR2/
│   └── BR3/
│       ├── BR3A/
│       ├── BR3B/
│       │   ├── BR3B1/
│       │   ├── BR3B2a/
│       │   ├── BR3B2b/
│       │   ├── BR3B2c/
│       │   ├── BR3B2d/
│       │   ├── BR3B2e/
│       │   ├── BR3B2f/
│       │   └── BR3B2g/
│       └── BR3C/
│           ├── BR3C_a/
│           ├── BR3C_b/
│           └── BR3C_c/
└── C7_7c/
    ├── SHARED/
    ├── K1/
    ├── K2/
    ├── K3/
    ├── K4_ANALYTIC_ENVELOPE/
    ├── K5/
    ├── K6/
    └── K7/
        ├── SHARED_K7B_K7C/     # vrátane skriptu 187
        ├── K7a_PROJECTED_JACOBIAN/
        ├── K7b_CONSTRAINTS/
        │   ├── K7b1/
        │   ├── K7b2/
        │   ├── K7b3a/
        │   └── K7b3b_P0/
        ├── K7c_EVOLUTION/
        │   ├── K7c1/
        │   ├── K7c2/
        │   ├── K7c3a/
        │   ├── K7c3b/
        │   ├── K7c3c_P1/
        │   └── K7c3d_P2/
        └── K7d_FULL_ACTIVITY/
```

Nová podkoľaj sa založí ako nový adresár až po vytvorení `00_TRACK.md`, v ktorom je uvedené, v čom sa líši od existujúcich podkoľají a ktorý dôvod smrti predchodcov odstraňuje.

## Dvojvrstvová migrácia

### Fáza 0 — zmrazenie

1. Vytvoriť kompletný SHA-256 a path manifest súčasného stavu.
2. Vytvoriť lokálny Git baseline commit pred prvým presunom; push na GitHub je samostatný schválený krok.
3. Zmraziť aktuálny corpus checker a error ledger.

### Fáza 1 — bezpečný navigačný strom

1. Vytvoriť `tracks/` a všetky `00_INDEX.md`/`00_TRACK.md`.
2. Existujúce súbory zatiaľ ponechať na pôvodných cestách.
3. Do `ARTIFACTS/00_MANIFEST.md` vložiť odkazy na pôvodné kanonické súbory, ich hash a status.
4. Každý artefakt musí mať práve jedného vlastníka; spoločné artefakty patria do `SHARED`.

Táto fáza okamžite zlepší navigáciu a nemení ani jeden výpočtový reťazec.

### Fáza 2 — fyzická migrácia

1. Najprv presúvať samostatné MD audity a výsledky; aktualizovať všetky odkazy cez machine-readable `OLD_PATH → NEW_PATH` mapu.
2. Skripty presúvať iba po závislostných komponentoch, nie jednotlivo podľa názvu.
3. Po každom balíku: broken-link kontrola, dependency kontrola, `py_compile`, corpus checker a porovnanie SHA-256 obsahu.
4. Historický skript sa pri presune obsahovo nemení. Ak potrebuje opravu importu/cesty, vznikne nový číslovaný nástupca; starý zostane v `HISTORY` s pôvodným hashom.
5. Fyzikálne regresné behy sa spustia až po samostatnej predregistrácii; organizačný presun sám nesmie dostať fyzikálny PASS.

### Fáza 3 — uzavretie

1. Regenerovať globálny register koľají a centrálny register skriptov.
2. Overiť, že žiadny súbor nie je nezaradený alebo duplicitne vlastnený.
3. Git commitnúť migráciu oddelene od fyzikálnych zmien.
4. Do Zenodo changelogu uviesť iba reorganizáciu ciest, ak sa nemenili fyzikálne tvrdenia; zmena predikčnej tabuľky má samostatný release trigger.

## Čo neodporúčam

- okamžite presunúť 203 skriptov podľa regexu názvu;
- kopírovať rovnaký skript do viacerých `PASS/STOP` priečinkov;
- použiť symlinky alebo hardlinky ako náhradu za kanonický manifest;
- miešať reorganizáciu ciest s opravou rovníc alebo novým fyzikálnym výpočtom;
- zaradiť A2-K10 pod A1-K1 iba kvôli číselnému poradiu;
- vytvoriť všeobecný `misc`, v ktorom sa znovu stratí pôvod súboru.

## Odporúčaný najbližší krok

Schváliť Fázu 1: vytvoriť neinvazívny `tracks/` strom a automaticky vygenerovať prvé manifesty bez presunu existujúcich súborov. Až po ručnom audite vlastníctva všetkých artefaktov a Git baseline rozhodnúť o Fáze 2.

## Neskoršie obmedzenie organizačného modelu V1

Používateľ následne spresnil, že A1, A2, A3, ... sú kontrolné stanice a že primárnym objektom auditu je celá cesta koľají medzi stanicami. Audit môže mať viac kôl odpovedí a reauditu. V1 sa preto nesmie použiť ako konečný fyzický strom. Je nahradený návrhom `DIRECTORY_STRUCTURE_AND_MIGRATION_PROPOSAL_V2_STATIONS_ROUTES_AND_AUDIT_THREADS_2026-07-15.md`; inventár, pravidlo jedného vlastníka artefaktu, zachovanie mŕtvych vetiev a dvojfázová migrácia z V1 zostávajú platné. Dôvod obmedzenia je samostatne v `Audit/DIRECTORY_MODEL_CORRECTION_STATIONS_ROUTES_AND_AUDIT_THREADS_2026-07-15.md`.
