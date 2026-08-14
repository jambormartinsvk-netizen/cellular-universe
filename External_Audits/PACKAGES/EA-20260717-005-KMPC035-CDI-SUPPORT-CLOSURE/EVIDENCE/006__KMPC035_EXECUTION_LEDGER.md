# KMPC-035 — CDI support step 2 execution ledger

**Stav:** `EXECUTED / AUTHORITATIVE SCOPED PASS+REVIEW`; pozri dokument 62  
**Interný limit:** `4.8 s`; **vonkajší limit:** `10 s` na proces

## Predbehové očakávania

| Fáza | Proces | Očakávanie | Odchýlka | Stav |
|---:|---|---|---|---|
| 1 | compile base | exit 0 bez výstupu | technická chyba, fyzika NOT RUN | `PASS`; exit 0; wall `0.5 s` |
| 2 | compile runner | exit 0 bez výstupu | technická chyba, fyzika NOT RUN | `PASS`; exit 0; wall `0.5 s` |
| 3 | `--help` | `GLOBAL_C1 / CDI_SUPPORT_STEP_2` CLI; historický token súboru `C2` nie je Fourier C2 | technická chyba | `PASS`; exit 0; wall `0.6 s`; bez JSON |
| 4 | `--smoke --max-runtime-seconds 4.8` | hashe/support/count/negative fixture/registry restoration/JSON safety; pri PASS bez JSON | pri výnimke technický failure JSON, audit zakázaný | `PASS`; exit 0; wall `1.3 s`; bez JSON |
| 5 | `--audit --max-runtime-seconds 4.8` | immutable regresia + tri supporty + core/common/tail | failure JSON bez fyziky | `COMPLETE`; exit 0; wall `3.0 s`; internal `1.609 s` |

## Ľudské očakávanie

Ak `[0,3]` je dostatočný, koeficienty `0..3` sa pri `[0,5]` prakticky
nezmenia a nový tail 4–5 bude pod `1e-6/1e-12`. Ak tail neprejde, ide o
neuzavretý remainder, nie o automatický STOP. Ak zlyhá regresia proti
KMPC-034, výsledok sa nesmie interpretovať ako fyzika.

Identita balíka je `GLOBAL_C1 / CDI_SUPPORT_STEP_2`; nejde o globálnu
Fourierovu C2 bránu. `SCORE_EFFECT`, `RELEASE_TRIGGER`, `ZENODO_TRIGGER` a
`PREDICTION_TABLE_EFFECT` sú všetky `NONE`.

Výsledok každej samostatnej Python fázy sa doplní až po jej behu;
predbehové očakávania sa spätne nemenia.

## Finálny predbehový refreeze

Dokumentačný recheck zachytil ešte pred prvým Python procesom nejednoznačný
text `CDI C2` a užšiu množinu strojových nonclaims. Boli opravené bez zmeny
rovníc, supportov, plôch alebo prahov. Failure JSON teraz tiež explicitne nesie
štyri nulové triggery.

| Artefakt | Zmrazený SHA-256 |
|---|---|
| `cdi_support_ladder.py` | `A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068` |
| runner 279 | `09F86A2A6E8BA81F4F41C73722BC40264888D1EF45BB4016F223A5E2C76649E3` |

### Pred procesom 1 — compile base

Ľudsky: kontroluje sa iba to, či Python vie načítať gramatiku zdieľaného
modulu; nič fyzikálne sa ešte nepočíta. Očakávame `exit 0` bez výstupu do
`10 s`. PASS povoľuje samostatný compile runnera. Ak proces zlyhá alebo vyprší,
zapíše sa technická chyba, fyzika zostane `NOT_RUN` a audit sa nespustí.

### Výsledok procesu 1

`C:\Python311\python.exe -m py_compile` skončil s `exit 0` za `0.5 s` a bez
výstupu. Ide iba o technický PASS syntaxe base modulu; nepridáva fyzikálny
výsledok ani neresetuje počítadlo technických chýb.

### Pred procesom 2 — compile runner

Ľudsky: overí sa syntax ohraničeného spúšťača, jeho fail-closed kontrol a
zápisu výsledku. Očakávame `exit 0` bez výstupu do `10 s`. PASS povoľuje iba
samostatný `--help`; chyba alebo timeout zastaví balík ako technický problém
bez fyzikálneho verdiktu.

### Výsledok procesu 2

Compile runnera skončil s `exit 0` za `0.5 s` a bez výstupu. Je to technický
PASS syntaxe, nie fyzikálny výsledok.

### Pred procesom 3 — `--help`

Ľudsky: runner iba vypíše svoje povolené argumenty. Očakávame jednoznačný
ohraničený CLI s voľbou `--smoke` alebo `--audit`, limitom `4.8 s` a bez
vytvorenia výsledkového JSON. PASS povoľuje smoke; chyba, timeout alebo
zavádzajúca identita znamená technickú opravu pred ďalším procesom.

### Výsledok procesu 3

Help skončil s `exit 0` za `0.6 s`. Vypísal `--smoke`, `--audit`, runtime a
output argument a explicitnú identitu `GLOBAL_C1 / CDI_SUPPORT_STEP_2` s
`NOT_GLOBAL_C2_FOURIER_GATE`. Kanonický success ani failure JSON nevznikol.
Je to technický PASS CLI, nie fyzikálny výsledok.

### Pred procesom 4 — smoke

Ľudsky: krátky smoke preverí presné zdrojové hashe, zmrazené supporty a počty,
zámerne chybný vstup, obnovenie dočasne zmenených registrov a bezpečnú JSON
serializáciu. Nevykonáva plný audit a pri úspechu nesmie vytvoriť JSON.
Očakávame `SMOKE_PASS`, `exit 0` a čas pod interným limitom `4.8 s`. PASS
povoľuje hlavný audit; výnimka/timeout je technická chyba a audit sa nespustí.

### Výsledok procesu 4

Smoke vrátil `{"run_id":"KMPC-035","smoke_pass":true}`, `exit 0`, za
`1.3 s`. Success ani failure JSON nevznikol. Je to technický PASS ochrannej
kostry; nepočíta sa ako čiastočný fyzikálny výsledok a neresetuje počítadlo.

### Pred procesom 5 — hlavný audit

Ľudsky: výpočet najprv musí presne zopakovať immutable support `[0,1]`, potom
vyrieši supporty `[0,3]` a `[0,5]`. Skontroluje ranky a holdouty, stabilitu
spoločných koeficientov `0..3` medzi poslednými dvoma supportmi a veľkosť iba
nových členov `4,5` na `z=10^-4` a `z=10^-2` pre F0 aj M3.

Očakávanie: regresia ostane pod `1e-12` relatívne alebo `1e-14` absolútne,
common bridge pod `1e-8` relatívne alebo `1e-12` absolútne a cancellation-safe
obálka `|c4|z^4+|c5|z^5` pod `1e-6` relatívne, prípadne pod absolútnym
fallbackom `1e-12`. Ak všetko prejde, `[0,3]` sa stane iba lokálne adekvátnym
kandidátom v tomto CDI/k/variant atóme. Ak tail neprejde, zostáva `REVIEW`
remainder a automaticky sa nepokračuje na `[0,7]`. Ak zlyhá regresia/core,
výsledok sa nesmie vykladať ako fyzika. Výnimka alebo timeout je iba technická
chyba, zachová sa a fyzický verdikt nevznikne.

### Výsledok procesu 5 — pred autoritatívnym auditom

Proces skončil s `exit 0` za `3.0 s`; interný runtime bol `1.609 s`, teda pod
limitom `4.8 s`. Vznikol jediný kanonický JSON s SHA-256
`A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`
a veľkosťou `74 741 B`. Failure JSON nevznikol.

Strojové brány: immutable regresia `PASS`, core `PASS`, common bridge `PASS`,
S-C0 conditional guard `PASS`, pure tail `FAIL`. Pri `z=10^-4` prešli F0 aj
M3. Pri `z=10^-2` zlyhali presne F0 `delta_f` s relatívnou obálkou
`2.5240162385e-5` a M3 `sigma_fs` s `3.2167075395e-3`; ostatné exportované
M3 stavy na tejto ploche prešli. Common bridge ostal hlboko pod prahom:
F0 maximum `1.1548e-14`, M3 maximum `6.6107e-13`.

Skript preto navrhol iba neautoritatívne
`REVIEW_CDI_SUPPORT_STEP_2_SUPPORT_03_REMAINDER_UNCLOSED`. Toto ešte nie je
verdikt hlavného auditora. Vecný, technicky úspešný výsledok resetuje aktívne
počítadlo technických chýb na `0/10`; compile/help/smoke sa za taký výsledok
samostatne nepočítali.

### Autoritatívny rozsudok hlavného auditora

Po troch nezávislých post-run auditoch:
`PASS_CDI_SUPPORT_STEP_2_CORE_AND_COMMON_03_05_STABILITY_ONLY /
REVIEW_CDI_SUPPORT_03_REMAINDER_UNCLOSED`.

Tail FAIL je skutočný v predregistrovanej metrike, nie numerický artefakt.
Support `[0,3]` sa neprijíma, ale CDI/K4 neumiera. Ďalší support je blokovaný
M1 `order=7` provenance bránou; úplný rozpis a nonclaims sú v dokumente 62.
