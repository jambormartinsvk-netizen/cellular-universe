# Návrh verziovaných `baseScripts` pre opakovateľné výpočty koľají

Dátum: 2026-07-15  
Stav: návrh na implementáciu; historické skripty sa zatiaľ nepresúvajú ani neprepisujú

## Cieľ

Oddeliť spoločnú fyziku, numeriku a auditné brány od parametrov konkrétnej
cesty. Oprava jednej potvrdenej chyby potom môže vytvoriť novú verziu jadra
a riadený batch re-run všetkých dotknutých manifestov. Nesmie však potichu
prepísať historické výsledky ani zmeniť význam už citovaného výpočtu.

## Navrhovaný strom

```text
scripts/
└── baseScripts/
    ├── 00_README.md
    ├── 00_VERSION_REGISTER.md
    ├── HISTORY/
    │   ├── 00_EVENT_LEDGER.md
    │   ├── SCORE_CHANGES/
    │   └── SUPERSESSIONS/
    ├── schemas/
    │   ├── run_manifest.schema.json
    │   └── result_manifest.schema.json
    ├── v001/
    │   ├── CHANGELOG.md
    │   ├── physics/
    │   │   ├── background.py
    │   │   ├── state_basis.py
    │   │   ├── rhs.py
    │   │   └── constraints.py
    │   ├── numerics/
    │   │   ├── integrators.py
    │   │   ├── scaling.py
    │   │   ├── convergence.py
    │   │   └── checkpoints.py
    │   ├── audit/
    │   │   ├── gates.py
    │   │   ├── weights.py
    │   │   └── evidence_manifest.py
    │   ├── runner.py
    │   └── tests/
    └── v002/
        └── ...
```

Konkrétny route uzol nebude kopírovať celé jadro. Bude obsahovať tenký,
ľahko čitateľný manifest, napríklad:

```text
tracks/A1/A1K1/A2/A2K4/SUBTRACKS/C7_7c/K7/K7c_EVOLUTION/ARTIFACTS/
├── manifests/K7c_P1_grid100.json
├── manifests/K7c_P1_grid200.json
├── manifests/K7c_P1_grid400.json
├── scripts/197_legacy_frozen.py
├── results/
└── audits/
```

## Čo musí manifest zmraziť

- route ID, stanicu, koľaj, podkoľaj a gate ID;
- `baseScripts` verziu a SHA-256 všetkých importovaných modulov;
- physics model ID, background, znamienkové konvencie a stavovú bázu;
- presný integrátor, kroky, tolerancie, pracovnú presnosť a closure;
- mód, deep/shallow plochu, interval, seed a vstupné súbory;
- vnútorný aj vonkajší timeout;
- očakávania pred behom, váhu gate a akceptačné/stop podmienky;
- cestu k výsledku a hash výsledného JSON/MD.

Výsledok bez manifestu alebo s nezhodným hashom je `PROVENANCE_FAIL` a
nezískava vedecké body.

## Prečo jadro musí byť verziované

`baseScripts/current` alebo jeden stále prepisovaný univerzálny súbor by
znemožnil reprodukciu starého auditu. Preto:

1. `v001` sa po prvom autoritatívnom výsledku nemení.
2. Oprava vytvorí `v002` a changelog s ID chyby, rozsahom dosahu a testom opravy.
3. Starý výsledok naďalej ukazuje na `v001`; nový batch re-run vytvorí nový
   výsledok s `v002`, novým ID a rozdielovým auditom.
4. Ak chyba zasahuje stovky behov, `HISTORY/SUPERSESSIONS` uvedie úplný zoznam
   dotknutých manifestov. Staré výsledky sa označia `LIMITED` alebo
   `SUPERSEDED`, nie zmažú.

## Oddelenie zodpovedností

- `physics/` obsahuje rovnice a konvencie, nie CLI, súbory ani tolerancie;
- `numerics/` obsahuje integrátory, škálovanie a konvergenciu, nie fyzikálny verdikt;
- `audit/` mapuje výsledok na preregistrované brány a váhy;
- manifest nesie voľby konkrétnej koľaje;
- `runner.py` iba skladá tieto vrstvy a vždy uplatní timeout a checkpointy.

Veľký „god script“ s desiatkami vetiev by iba centralizoval nové riziko.
Spoločné funkcie majú byť malé, čisté, bez skrytého globálneho stavu a s
explicitnými vstupmi/výstupmi.

## Povinné regresné testy jadra

1. analytická ODE s očakávaným RK4 pomerom približne 16;
2. nulový a príslušný štandardný limit;
3. test znamienok, jednotiek a poradia registrovaného stavu;
4. constraint test, ktorý nepočíta identitu z tej istej definície;
5. lineárne škálovanie amplitúdy;
6. porovnanie dvoch FD krokov pri numerickom Jacobiáne;
7. kontrola hashov a úplnosti serializácie aj pri timeoute;
8. test, že interný timeout je kratší než vonkajší;
9. cross-version fingerprint, ktorý presne ukáže, čo sa medzi `v001` a `v002` zmenilo.

## Bezpečná migrácia

### Pilot

Ako prvý sa extrahuje iba čistý K7c P1 skript 197 do `baseScripts/v001`.
Nový manifest musí reprodukovať všetky tri uložené mriežky v už zmrazených
toleranciách. Kým sa výsledky a hashe nezhodujú, historický skript 197 ostáva
autoritatívny a jadro je iba kandidát.

### Rozšírenie

Po pilote sa K1 až K6 zapíšu ako samostatné manifesty používajúce tie isté
moduly, ale svoje pôvodné scaling/integrator stratégie. Následne sa migrujú
ďalšie route uzly po jednom závislostnom komponente.

### Zakázané skratky

- neprepísať historický skript importom nového jadra;
- nemenovať mutable alias `latest` ako autoritatívny dependency pin;
- nemeníť fyziku a adresáre v tom istom Git commite;
- nevykonať hromadný re-run bez zoznamu očakávaných zmien;
- nepreniesť PASS z jedného manifestu na iný background iba preto, že používajú rovnaké jadro.

## Rozhodnutie k implementácii

Najprv vytvoriť iba prázdny version register, schémy a pilot K7c P1. Až po
externom alebo nezávislom internom audite jeho parity sa môže začať batch
migrácia. Tým získame výhodu jednej opravy pre mnoho behov bez straty
reprodukovateľnosti a bez tichého prepisovania histórie.

