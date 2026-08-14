# Plán upratania dokumentácie a reťazec GitHub -> Zenodo

**Dátum:** 2026-07-13  
**Stav:** `NAPLÁNOVANÉ — ZATIAĽ BEZ PRESUNOV`  
**GitHub:** <https://github.com/jambormartinsvk-netizen/cellular-universe>

## 1. Zistený stav

Pred pridaním tohto balíka mal workspace 242 súborov. Najväčšie skupiny:

| Skupina | Počet |
|---|---:|
| `Audit/*.md` | 42 |
| `Questions/*.md` | 31 |
| `scripts/*.py` | 42 |
| `scripts/*.md` | 25 |
| generované `scripts/**/*.pyc` | 39 |
| `theory/*.md` | 22 |
| `Nespracovane` celkom | 11 |

Lokálny `D:/Teoria/.git` je adresár, ale neobsahuje platný repozitár;
`git status` končí správou `not a git repository`. Vzdialený repozitár je
dostupný, má vetvu `main` a pri kontrole ukazoval na commit
`77828f767ce2ecdbf7e4535e91926f7cbc1b5a50`.

## 2. Prečo sa teraz súbory nepresúvajú

Auditné manifesty obsahujú cesty a SHA-256. Okamžitý hromadný presun by
rozbil odkazy a sťažil spätný audit. Najprv musí vzniknúť inventár,
kanonická mapa a kontrola kolízií s obsahom vzdialeného repozitára.

## 3. Navrhovaná cieľová logika

Presný názov koreňa sa schváli až po porovnaní s GitHubom. Logické skupiny:

```text
docs/
  00_project/                 README, slovník, metodika
  01_theory/SK/               kanonická slovenská teória
  01_theory/EN/               synchronizovaná anglická teória
  02_audits/background/       A0-A1
  02_audits/perturbations/    A2-K*
  02_audits/cosmology/        A3, S8, H0
  02_audits/dead_tracks/      registre smrti a dôkazové indexy
  03_questions/active/        aktuálny stav a najbližšie kroky
  03_questions/archive/       nahradené, ale nezmazané plány
  04_release/                 changelog, manifesty, Zenodo metadata
  05_unprocessed/             obsah dnešného Nespracovane
scripts/
  audit/                      aktívne reprodukovateľné výpočty
  archived_failed_runs/       chybné behy + erratá
  outputs/                    kompaktné MD výstupy
legacy/                       dnešné Old a nahradené vydania
web/                          prezentačná vrstva
```

Mŕtva koľaj sa neoddelí od dôkazu: jej audit, skript, výstup, erratum a hash
budú prepojené jedným indexom.

## 4. Etapy

### D0 — zmrazenie a inventár

- vytvoriť zoznam všetkých ciest, veľkostí, SHA-256 a logickej roly;
- označiť kanonický, nahradený, generovaný a nespracovaný obsah;
- nájsť duplicitné názvy a odkazy `file:///`;
- uložiť stav pred migráciou do MD manifestu.

### D1 — bezpečný Git staging

- zálohovať alebo premenovať neplatný prázdny `.git` až po samostatnej
  kontrole a výslovnom zápise operácie;
- vzdialený repozitár naklonovať do samostatného staging adresára;
- porovnať GitHub `main` s workspace, nie slepo inicializovať cez existujúce
  súbory;
- zvoliť merge/import stratégiu bez prepisu histórie.

### D2 — pravidlá repozitára

- pridať `.gitignore` minimálne pre `.deps/`, `__pycache__/`, `*.pyc`,
  dočasné renderovania a lokálne cache;
- zachovať zdrojové skripty, MD výstupy, erratá a release manifesty;
- určiť jednu kanonickú SK a EN cestu registra 05.

### D3 — dávková migrácia

- presúvať po jednej logickej skupine;
- ku každej dávke uložiť mapu `stará cesta -> nová cesta`;
- po každej dávke opraviť relatívne odkazy a spustiť link checker;
- historické dokumenty nemažú obsah; dostanú index alebo stav `SUPERSEDED`.

### D4 — validačná brána

- nulové chýbajúce interné odkazy;
- nulové nečakané zmeny hashov obsahu mimo vedomých opráv;
- SK/EN register obsahovo synchronizovaný;
- kritické skripty A1, A2, A3 a K3a opakovateľné z čistého prostredia;
- žiadne `.pyc` ani `.deps` v commite.

### D5 — GitHub release candidate

- vytvoriť čitateľné commity podľa logických dávok;
- zapísať finálny commit hash a vytvoriť release tag, napr. `v3.18-rc1`;
- push vykonať až po kontrole diffu, bez force-push;
- GitHub commit je zdroj balíka pre Zenodo, nie tichá náhrada starého Zenodo.

### D6 — Zenodo

- vytvoriť changelog voči v3.17/Zenodo v2;
- vložiť Git commit/tag, manifest a SHA-256;
- skontrolovať verziu 3.x vs 4 podľa pravidla nezmeneného fundamentu;
- publikovať nový nemenný záznam/verziu; staré čísla a súbory neprepisovať.

## 5. Kritérium dokončenia

Upratanie je hotové iba ak čisté naklonovanie označeného Git tagu obsahuje
všetky kanonické dokumenty a dôkazy, prejde kontrolou odkazov a reprodukuje
kritické výpočty bez lokálnych cache. Zenodo balík sa musí zhodovať s týmto
tagom podľa manifestu, nie iba názvom verzie.
