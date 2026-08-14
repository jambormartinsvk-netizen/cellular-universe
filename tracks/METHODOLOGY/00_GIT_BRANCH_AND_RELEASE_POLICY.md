# Git pracovná a release politika

**Dátum prijatia:** 2026-07-16  
**Repozitár:** `jambormartinsvk-netizen/cellular-universe`

## Vetvy

| Vetva | Účel | Povolený obsah |
|---|---|---|
| `main` | verejný release/publikačný korpus | iba schválené hlavné dokumenty, dôkazy, reprodukčné skripty, changelog a release manifest |
| `work/v3.18-audit-2026-07-16` | pracovná auditovateľná v3.18 | pracovné tracks, audity, otázky, skripty, immutable výsledky a release staging; bez cache, buildov a tajomstiev |

## Oddelenie na disku

- `D:\Teoria` je výhradne pracovný worktree vetvy
  `work/v3.18-audit-2026-07-16`;
- `D:\Teoria-main` je výhradne čistý publikačný worktree vetvy `main`;
- medzi worktree sa súbory nekopírujú ručne a checkout jednej vetvy sa
  nevykonáva v adresári druhej;
- povýšenie prebieha Git commitom a kontrolovaným PR/merge, nie prepisom
  adresárov;
- pred každou zmenou sa overí `git branch --show-current` v cieľovom worktree.

## Ochrany

- zákaz priameho pracovného commitu na `main`;
- zákaz práce na `main` v adresári `D:\Teoria`; jeho obraz patrí iba do
  `D:\Teoria-main`;
- zákaz force-push a tichého prepisu publikovaných tagov/verzií;
- zákaz `git add .` pred baseline manifestom, secret scanom a size auditom;
- jeden commit pokrýva jeden logický auditný alebo formulačný balík;
- oprava dôkazu zachová pôvodný artefakt a pridá limitation/changelog;
- nefunkčné skripty zostávajú v histórii alebo karanténe s dôvodom;
- Python cache, lokálne dependencies, IDE a build výstupy sa necommitujú;
- externý CLASS sa vedie ako pinovaný submodule alebo dependency manifest,
  nie ako neauditovaná lokálna kópia.

## Prvý pracovný baseline

Pred prvým commitom treba:

1. klasifikovať tracked rozdiely voči historickému `main`;
2. vyriešiť staré vnorenie `theory/theory/...` cez explicitnú migračnú mapu;
3. rozhodnúť, ktoré koreňové `LICENSE` a `README.md` sa obnovia alebo nahradia;
4. použiť `.gitignore` a znovu spočítať pracovné artefakty;
5. vykonať secret scan a audit veľkých súborov;
6. vytvoriť presný staging manifest; žiadny implicitný hromadný add;
7. commitnúť najprv organizačný baseline, potom vedecké balíky.

## Povýšenie do `main`

Do `main` sa prenesie iba release výber cez kontrolovaný PR/merge po:

- fyzikálnom a matematickom audite;
- dokumentačnom/release checkliste;
- SK/EN kontrole;
- aktualizácii tabuľky predpovedí a scope obmedzení;
- changelogu a SHA-256 manifeste;
- reprodukčnom teste skriptov označených ako release-ready;
- potvrdení, že sa nepublikuje cache, lokálny build ani pracovné tajomstvo.
