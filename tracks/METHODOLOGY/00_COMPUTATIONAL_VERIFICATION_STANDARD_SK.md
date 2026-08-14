# Štandard overiteľnosti výpočtov

**Zavedené:** 2026-08-14
**Nahrádza:** prozaickú časť `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md` ako
prevenčný nástroj (historický register sa nemaže, len prestáva byť jediným
nositeľom prevencie)
**Cieľ:** aby chyba v programe nevyrobila dvesto nadväzujúcich výpočtov, a aby
každé publikované číslo vedel fyzik zvonku spustiť, overiť a spätne dohľadať

---

## 1. Princíp

> **Výpočet nesie svoje vlastné falzifikačné testy a spustí ich zakaždým.
> Výsledok, ktorého povinné kontroly neprešli, nie je výsledok.**

Nie je to náhrada nezávislého auditu. Je to filter **pred** ním, ktorý
oddelí chybu implementácie od fyziky bez toho, aby na to musel byť druhý
človek alebo agent.

Doklad, že to funguje: externý audit 2 sám predpísal
*„pri `W = k²` a cutoffe v nekonečne musí formula dať nulu — ak nedá, je chyba
v implementácii, nie vo fyzike"*. To je celá metodika v jednej vete. Táto
sekcia z nej robí povinnosť namiesto poznámky.

## 2. Triedy kontrol

| Trieda | Čo overuje | Povinná? |
|---|---|---|
| `NULL_LIMIT` | vypni novú fyziku → musí vyjsť známy výsledok (`λ→0` dá ΛCDM, `g→0` zabije všetky nové toky, `W=k²` dá nulové LV) | **áno**, aspoň jedna z `NULL_LIMIT`/`ANCHOR` |
| `ANCHOR` | prípad s uzavretým analytickým riešením | **áno**, viď vyššie |
| `IDENTITY` | veličina, ktorá musí byť presne nula (conservation, constraint reziduum) | áno, ak existuje |
| `CONVERGENCE` | stabilita voči rozlíšeniu, tolerancii, metóde | nie |
| `CROSSCHECK` | nezávislá reimplementácia kritického kroku (RK4 vs DOP853) | nie |
| `SEED` | stabilita voči náhodnému seedu (Monte Carlo, Delaunay) | áno pri stochastike |
| `DIMENSION` | rozmerová/jednotková kontrola | nie |

**Padnutie `NULL_LIMIT`, `ANCHOR` alebo `IDENTITY` zadrží výsledok** a beh
skončí nenulovým exit kódom. Ostatné sa vykážu ako `PASS_WITH_SOFT_FAILURES`.

### Prečo je konvergencia mäkká

Overené experimentom: pri zavedení preklepu `5/96 → 5/95` do smyčkovej formuly
padli všetky tri povinné kontroly, ale **konvergenčná prešla**. Konvergencia
meria, či numerika sedí sama so sebou — nie či počítaš správnu vec. Sama o sebe
je bezcenná ako dôkaz správnosti.

To isté platí o reprodukovateľnosti na 10⁻¹²: `EA-004` reprodukoval
`A_f = 7809.270101963506` iným integrátorom na 10⁻¹². Je to dobrá práca, ale
dokazuje to zhodu dvoch integrátorov, nie správnosť rovnice.

## 3. Harness

`scripts/qcts_check.py` — jeden súbor, bez projektových závislostí.

```python
from qcts_check import Run

r = Run("nazov_vypoctu", question="Q-A0-LORENTZ-RADIATIVE-STABILITY")

r.is_zero("LI disperzia, cutoff=inf", val, tol=1e-12,
          why="LI disperzia nesmie generovat LV; nenulove = chyba implementacie")
r.check("analyticka kotva", val2, ocakavane, tol=2e-3, kind="ANCHOR",
        absolute=False, why="overuje normalizaciu, prefaktor aj integracnu mez")
r.converged("rozlisenie", [v_lo, v_mid, v_hi], rtol=1e-9)
r.crosscheck("RK4 vs DOP853", a, b, rtol=1e-10)

r.note("interpretacna poznamka, ktora sa ma dostat do receiptu")
r.result("dc2/c2", hodnota, unit="1")
r.finish()
```

Harness automaticky zapíše `<nazov>_receipt.json` s:

- **SHA-256 samotného spusteného súboru** (nie prepísaného kódu)
- verziou Pythonu, numpy, scipy, sympy, mpmath
- všetkými kontrolami: hodnota, očakávané, odchýlka, tolerancia, prečo
- výsledkami a poznámkami
- stavom `PASS` / `PASS_WITH_SOFT_FAILURES` / `FAIL_IMPLEMENTATION`

Receipt sa **nepíše ručne**. Manuálny manifest je miesto, kde vzniká drift.

## 4. Dokument nikdy neobsahuje prepísaný kód

> **Do dokumentu ide súbor alebo jeho SHA-256, nikdy nie prepísaný listing.**

Doklad, prečo: Dodatok A1 externého auditu 2 obsahuje
`om_rec = (Y[1]+Y[2])[i]*1091**3*h**2`. Pri deklarovanej normalizácii má byť
`/1091**3`. Ako je publikovaný, snippet dá `2.4×10¹⁷` namiesto `0.14299`.

Audit, ktorého celou témou bola reprodukovateľnosť, poslal nereprodukovateľný
dodatok — pretože kód v dokumente nebol kód, ktorý bežal. To sa nestane
nikomu, kto prepisovanie zakáže.

## 5. Chyby sa zapisujú ako testy, nie ako próza

> **Chyba zapísaná v próze sa zopakuje. Chyba zapísaná ako test sa nezopakuje
> nikdy.**

`scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md` má desiatky záznamov a `AGENTS.md`
sám priznáva, že ho nikto nečíta celý. To nie je nedostatok disciplíny — je to
vlastnosť prózy ako média prevencie.

Nový postup pri technickej chybe:

```
1. jeden kompaktny error riadok (ako doteraz)
2. + REGRESNY TEST v scripts/tests/, ktory na tej chybe padne
3. + ak je trieda chyby prenositelna, jedna kontrola pridana
     do povinneho suite harnessu
```

Historický ledger zostáva ako forenzný register a nemaže sa. Prestáva však byť
nositeľom prevencie — tým sa stáva `scripts/tests/`, ktorý beží sám.

Test má byť napísaný tak, aby padol na **triede** chyby, nie na jednom výskyte:

| Historická chyba | Test, ktorý ju chytí navždy |
|---|---|
| `k`-závislosť backgroundu (`EA-004`) | `assert dH/dk == 0` pre tri rôzne `k` |
| skrátený K7 rad mimo doménu | porovnanie skráteného a plného radu s hlásením, kde prekročí 0.1 % |
| `4·lmax+9` vs `+11` stavov (`PF-062`) | `assert len(state_vector) == 4*lmax+9` |
| zámena kvantifikátora actual/universal (`task573`) | typová anotácia + test na prázdnu množinu |
| konečné `s₋, s₊` na neobmedzenom komponente (`task626`) | test na neohraničený vstup |

## 6. Dohľadateľnosť: jeden riadok na číslo, nie na balík

Súčasné manifesty sú orientované na **balíky**. Otázka, ktorú treba vedieť
zodpovedať, je však iná:

> *Našiel som bug v skripte X. **Ktoré publikované čísla** z neho pochádzajú?*

Preto jedna plochá tabuľka `scripts/results/00_PUBLISHED_NUMBERS.tsv`,
append-only, **jeden riadok na publikované číslo**:

```
cislo | hodnota | skript_sha256 | receipt_sha256 | vstupy_sha256 |
stav_kontrol | datum | kde_je_pouzite
```

Pri náleze chyby sa dá spätne odpovedať jedným grepom. To je „spätne zistiť,
či v nich nebola skrytá chyba", o ktoré ti ide, a stojí to jeden riadok
za výsledok.

## 7. Čo musí platiť, aby to fyzik vedel spustiť

```
1. JEDEN subor, spustitelny ako `python skript.py`
2. ziadne projektove importy okrem qcts_check.py
3. ziadne cesty na tvoj disk, ziadna siet
4. vsetky vstupne cisla v hlavicke suboru, s uvedenim povodu
   (odvodene / merane / zmrazena vetva)
5. beh do niekolkych minut na beznom stroji; ak nie, dodaj
   zmensenu verziu, ktora prejde kontroly
6. na stdout najprv KONTROLY, potom vysledok
7. nenulovy exit kod pri padnutej povinnej kontrole
```

Bod 4 je dôležitejší, než vyzerá: `λ = 0.15` sa musí v hlavičke označiť ako
`ZMRAZENA VETVA, historicky data-selected`, nie ako vstup. Recenzent, ktorý to
nájde priznané, získa dôveru; ten, ktorý si to všimne sám, ju stratí.

## 8. Vzťah k existujúcemu workflow

Toto **nenahrádza** `DEV → RC_FREEZE → INDEPENDENT_STATIC_MATH_AUDIT →
OFFICIAL_RUN`. Vkladá sa pred neho:

```
DEV_SANDBOX
  -> povinny suite harnessu prejde        <- NOVE, tu sa zachyti chyba programu
  -> DEV_TESTS_PASS
  -> RC_FREEZE
  -> INDEPENDENT_STATIC_MATH_AUDIT        <- teraz uz iba matematika a fyzika
```

Efekt: nezávislý auditor prestane míňať kolá na preklepy a začne robiť to,
na čo je — kontrolovať rovnice, znamienka, jednotky a provenienciu.

## 9. Čo tento štandard nechytí

Poctivo, aby sa naň nespoliehalo viac, než unesie:

- **kategoriálnu chybu.** Ak počítaš správne zlú vec, všetky kontroly prejdú.
  Na to je `FRAME_CHALLENGE` (`AGENTS.md` §7.1) a človek zvonku.
- **chybnú null-kontrolu.** Ak je zle napísaný samotný test, dá falošné PASS.
  Preto sa aspoň jedna `ANCHOR` viaže na **uzavretý analytický tvar**, nie na
  iný numerický výsledok.
- **správnosť fyzikálneho modelu.** Harness overuje, že počítaš to, čo si
  chcel. Či to bolo správne chcieť, nehovorí.
