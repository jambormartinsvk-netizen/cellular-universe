# Skripty — route index

**Aktualizované:** 2026-07-16  
**Účel:** vstup do číslovaného korpusu bez fyzického presunu súborov.

| Route/koľaj | Vlastnícky manifest |
|---|---|
| A1-K1 / A2 všeobecne | `tracks/A1/A1K1/A2/00_TRACK_REGISTER.md` |
| A2-K1,K2,K3,K5,K6 | vlastný ARTIFACTS manifest; konkrétna cesta je v `tracks/A1/A1K1/A2/00_TRACK_REGISTER.md` |
| A2-K4 | `tracks/A1/A1K1/A2/A2K4/ARTIFACTS/00_MANIFEST.md` |
| A2-K4/P5 | `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/RUNNERS/00_MANIFEST.md` |
| A2-K7,K8,K9,K11,K12 | príslušný route manifest |
| A1-K2/A2-K10 | `tracks/A1/A1K2/A2/A2K10/ARTIFACTS/00_MANIFEST.md` |

Pred spustením:

1. nájdi vlastníka a gate;
2. prečítaj `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md` a error ledger;
3. použi celý názov, pretože prefixy 45–47, 150–155 a 255–257 kolidujú;
4. prečítaj predbehový Markdown a over interný ≤5 s/vonkajší ≤10 s limit;
5. zapíš base moduly a ich SHA podľa
   `baseScripts/00_MODULE_OWNERSHIP_REGISTER.md`.

Historické skripty zostávajú v tomto adresári kvôli väzbám
`Path(__file__).with_name()`, auditným citáciám a hashom.
