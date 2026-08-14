# Git pracovná vetva — bootstrap a ochrana účtu

**Dátum:** 2026-07-16  
**Repozitár:** `jambormartinsvk-netizen/cellular-universe`  
**Plánovaná pracovná vetva:** `work/v3.18-audit-2026-07-16`  
**Stav:** `BLOCKED_BY_ACCOUNT_IDENTITY — žiadny vzdialený zápis nevykonaný`

## Požadovaná identita

Pre tento projekt je povolený iba GitHub účet `jambormartinsvk-netizen`,
prihlásený cez používateľom určený Gmail účet. Identita autora commitu sa
nesmie zamieňať s právom zápisu: `user.name`/`user.email` iba podpisujú
commit, ale autentizovaný GitHub účet rozhoduje o push oprávnení.

## Zistený stav pred vytvorením vetvy

| Kontrola | Výsledok | Dopad |
|---|---|---|
| GitHub konektor | `JamborMartin`, ID `156589777` | iný účet než vlastník repozitára |
| vlastník repozitára | `jambormartinsvk-netizen`, ID `301893154` | požadovaný účet |
| oprávnenie konektora | `pull=true`, `push=false` | vzdialená vetva sa nesmie vytvoriť |
| lokálny `gh auth status` | účet `JamborMartin`, token v keyringu neplatný | lokálny push nie je dôveryhodný |
| lokálny Git podpis | `Martin Jámbor <jambor@chastia.com>` | nesprávny pre požadovanú projektovú identitu; zmeniť iba lokálne pre tento repozitár |
| `D:\Teoria\.git` | adresár existuje, ale je prázdny/neplatný; `git status` hlási „not a git repository“ | nejde o Git baseline |
| sieťový `git ls-remote` v sandboxe | blokovaný lokálnym proxy `127.0.0.1` | overiť cez GitHub konektor alebo eskalovaný Git po správnom login-e |

## Bezpečnostné rozhodnutie

- nevytvoriť vetvu cez nesprávny účet;
- nevykonať commit, push, reset ani checkout;
- neodstraňovať existujúci prázdny `.git` bez samostatnej kontroly;
- po prehlásení overiť `github_get_user_login == jambormartinsvk-netizen`;
- overiť write oprávnenie pred prvou mutáciou;
- až potom založiť vetvu z aktuálneho `main`.

## Bezstratový bootstrap po odblokovaní

1. read-only overiť aktuálny `main` SHA a neprítomnosť cieľovej vetvy;
2. inicializovať lokálnu Git históriu bez prepisu pracovného stromu;
3. pripojiť `origin` a načítať `main`;
4. založiť pracovnú vetvu z `origin/main` spôsobom, ktorý ponechá všetky
   lokálne súbory ako viditeľné zmeny; zákaz `reset --hard`;
5. skontrolovať `.gitignore`, veľké súbory, tajomstvá, cache, build výstupy a
   nefunkčné skripty pred stagingom;
6. urobiť prvý auditovateľný commit iba s explicitným manifestom súborov;
7. na `main` sa neskôr prenesie iba release balík cez kontrolovaný merge/PR.

## Odblokovacia podmienka

Používateľ prepojí GitHub konektor aj lokálny `gh` na
`jambormartinsvk-netizen`. Hlavný orchestrátor následne zopakuje read-only
kontrolu identity a oprávnení a výsledok doplní do tohto dokumentu.

## Kontrola po prihlásení v prehliadači

**Čas kontroly:** 2026-07-16, po oznámení používateľa o pripojení druhého účtu  
**Výsledok:** stále `BLOCKED_BY_ACCOUNT_IDENTITY`

- prehliadač môže byť prihlásený ako `jambormartinsvk-netizen`, ale Codex
  GitHub konektor naďalej vracia `JamborMartin`, ID `156589777`;
- konektor na repozitári stále hlási `pull=true`, `push=false`;
- lokálny `gh auth status` stále používa `JamborMartin` a neplatný token;
- `gh api user` preto nevrátil login ani ID;
- nebol vykonaný žiadny vzdialený zápis.

Samotné prihlásenie do `github.com` v karte neprepína už autorizovaný Codex
konektor ani token uložený v `gh` keyringu. Treba ich odpojiť a autorizovať
samostatne.

## Stav po odpojení konektora

Používateľ potvrdil odpojenie GitHub konektora a prihlásenie v prehliadači
do účtu `jambormartinsvk-netizen`. Následné volania
`github_list_installed_accounts` a `github_get_user_login` skončili internou
chybou bez identity, čo je konzistentné s odpojeným konektorom.

Plugin ostáva nainštalovaný, preto ho nemožno znovu vyvolať cez inštalačný
request. Používateľ musí v nastavení Codex pluginu GitHub stlačiť `Connect`
a v OAuth okne potvrdiť účet `jambormartinsvk-netizen`. Ovládanie samotnej
Codex aplikácie ani autentizačného dialógu sa automatizovať nebude. Vzdialený
zápis zostáva zablokovaný do úspešného `github_get_user_login` a `push=true`.

## Lokálny GitHub CLI device login

Po opakovanej kontrole sa potvrdilo, že Codex konektor nie je pripojený k
žiadnemu účtu; volania končia internou chybou. Neplatná lokálna relácia
`JamborMartin` bola následne úspešne odhlásená a bolo otvorené samostatné
viditeľné okno:

```text
gh auth login -h github.com -p https -w --skip-ssh-key
```

Používateľ musí v zariadenom browser/device flow osobne potvrdiť účet
`jambormartinsvk-netizen`. Otvorenie login flow nie je dôkaz úspešného
prihlásenia; pred Git zápisom treba znovu overiť `gh auth status`,
`gh api user` a write prístup k repozitáru.

## Úspešná kontrola identity

**Výsledok:** `IDENTITY_PASS / BRANCH_NOT_YET_CREATED`

Read-only kontrola mimo blokovaného sieťového sandboxu potvrdila:

- aktívny účet: `jambormartinsvk-netizen`;
- GitHub user ID: `301893154`, zhodné s vlastníkom repozitára;
- repozitár: `jambormartinsvk-netizen/cellular-universe`;
- `permissions.push=true`;
- predvolená vetva: `main`;
- lokálny protokol Git operácií: HTTPS;
- token má `repo` scope; samotná hodnota tokenu nebola zaznamenaná.

Pôvodné sandboxové hlásenie o neplatnom tokene bolo sieťový artefakt proxy
`127.0.0.1:9`, nie dôkaz zlej identity. Ďalší povolený krok je read-only
overenie SHA `main` a neprítomnosti cieľovej vetvy.

## Predregistrácia vytvorenia vzdialenej vetvy

- overený `main` SHA:
  `77828f767ce2ecdbf7e4535e91926f7cbc1b5a50`;
- cieľová vetva `work/v3.18-audit-2026-07-16` neexistovala;
- očakávanie: nová vetva vznikne presne na rovnakom SHA ako `main`;
- PASS: GitHub po vytvorení vráti rovnaký SHA a `main` ostane nezmenená;
- STOP: vetva existuje na inom SHA, API odmietne zápis alebo sa zmení `main`;
- tento krok necommitne ani nenahrá nijaký lokálny pracovný súbor.

## Výsledok vzdialenej vetvy

**Stav:** `REMOTE_BRANCH_PASS`

- vytvorená: `refs/heads/work/v3.18-audit-2026-07-16`;
- SHA pracovnej vetvy:
  `77828f767ce2ecdbf7e4535e91926f7cbc1b5a50`;
- SHA `main` po operácii:
  `77828f767ce2ecdbf7e4535e91926f7cbc1b5a50`;
- do vetvy nebol pridaný lokálny obsah a `main` sa nezmenila.

## Predregistrácia lokálneho pripojenia

Lokálny `D:\Teoria` sa pripojí bez checkoutu pracovných súborov a bez
`reset --hard`:

1. inicializovať metadáta v existujúcom prázdnom `.git`;
2. pridať `origin` a fetch `main` + pracovnej vetvy;
3. nastaviť lokálnu vetvu na vzdialený pracovný SHA cez ref/index operácie,
   ktoré nemenia pracovný strom;
4. nastaviť iba lokálnu commit identitu projektu na
   `jambormartinsvk-netizen` a používateľom určený Gmail;
5. zobraziť súhrnný status bez stagingu a bez commitu.

PASS vyžaduje zhodný HEAD SHA, správny upstream a zachované lokálne súbory.
STOP je akýkoľvek pokus o prepis pracovného stromu, iný SHA alebo zlyhaný
fetch. Pri STOP sa nič necommitne ani neposiela.

## Výsledok lokálneho pripojenia

**Stav:** `LOCAL_BRANCH_PASS / STATUS_AUDIT_BLOCKED_BY_SAFE_DIRECTORY`

- lokálna vetva: `work/v3.18-audit-2026-07-16`;
- HEAD: `77828f767ce2ecdbf7e4535e91926f7cbc1b5a50`;
- upstream: `origin/work/v3.18-audit-2026-07-16`;
- origin: `https://github.com/jambormartinsvk-netizen/cellular-universe.git`;
- lokálna identita: `jambormartinsvk-netizen` a používateľom určený Gmail;
- prvý eskalovaný súhrn napočítal 16 tracked rozdielov a 9 053 untracked
  súborov; nič nebolo staged ani commitnuté.

Bežný read-only status následne zastavila Git ochrana `dubious ownership`,
pretože `D:\Teoria` vlastní skupina Administrators a príkaz beží ako
`CHASTIA\jambor`. Povolená oprava je iba presná používateľská výnimka
`safe.directory=D:/Teoria`; všeobecná výnimka `*` je zakázaná.

## Safe-directory a baseline inventúra

Presná výnimka `D:/Teoria` bola pridaná; globálny wildcard nebol použitý.
Následný audit potvrdil:

- vzdialený repozitár nemá `.gitignore`;
- 16 tracked rozdielov voči historickému `main`;
- 9 053 untracked ciest pred lokálnym `.gitignore`;
- z toho 7 456 pod `.deps`, ďalej 642 `scripts`, 304 `Audit`, 242
  `Questions`, 211 `tracks`, 116 `theory` a ďalšie pracovné korene;
- historický `main` obsahuje vnorené cesty `theory/theory/SK` a
  `theory/theory/EN`, ktoré lokálny reorganizovaný strom nepoužíva;
- koreňové `LICENSE` a `README.md` sú v remote tracked, ale lokálne chýbajú.

**Rozhodnutie:** nevykonať `git add .`, staging ani commit. Najprv vzniká
`.gitignore`, explicitná migračná mapa a staging manifest. Branch politika je
`tracks/METHODOLOGY/00_GIT_BRANCH_AND_RELEASE_POLICY.md`.

## Predregistrácia oddeleného worktree pre main

- zdroj: `origin/main@77828f767ce2ecdbf7e4535e91926f7cbc1b5a50`;
- cieľ: nový, pred kontrolou neexistujúci `D:\Teoria-main`;
- existujúci `D:\Teoria` zostáva na pracovnej vetve a jeho súbory sa nemenia;
- PASS: `D:\Teoria-main` hlási vetvu `main`, rovnaký SHA a čistý status;
- STOP: cieľ existuje, `main` už používa iný worktree, SHA sa líši alebo sa
  zmení pracovný strom `D:\Teoria`;
- povolená operácia je `git worktree add`; zakázané sú presun, mazanie,
  checkout v pracovnom adresári a ručné kopírovanie.

## Výsledok oddelenia worktree

**Stav:** `PASS — DISK_BRANCH_SEPARATION`

| Adresár | Vetva | HEAD | Status |
|---|---|---|---|
| `D:\Teoria` | `work/v3.18-audit-2026-07-16` | `77828f767ce2ecdbf7e4535e91926f7cbc1b5a50` | pracovné lokálne rozdiely zachované, nič staged |
| `D:\Teoria-main` | `main` | `77828f767ce2ecdbf7e4535e91926f7cbc1b5a50` | čistý, `STATUS_COUNT=0` |

Git register worktree potvrdil oba adresáre a samostatné branch refs. Žiadny
súbor sa medzi nimi nekopíroval, pracovný strom `D:\Teoria` sa necheckoutoval
a vzdialený `main` sa nezmenil.
