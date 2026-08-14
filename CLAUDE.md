# Teória / QCTS — projektové inštrukcie

@AGENTS.md

## Čo je v tomto repozitári nové (od 2026-08-14)

| Súbor | Rola |
|---|---|
| `tracks/00_STATE.json` | **jediný strojový zdroj pravdy.** Markdown registre sú pohľady na neho, nie zdroje |
| `scripts/check_state.py` | linter stavu — 13 pravidiel, každé s precedensom konkrétnej minulej chyby |
| `scripts/qcts_check.py` | harness výpočtov — výsledok bez povinných kontrol sa nevypíše |
| `scripts/release_gate.py` | branka pred vydaním verzie |
| `tracks/A0/00_STATION.md` | **upstream stanica**; `A2` a `A3` sú do jej rozhodnutia zmrazené |
| `tracks/00_POST_AUDIT_PLAN_2026-08-14_SK.md` | poradie prác |

## Tvrdé pravidlá (vynucované hookmi, nie týmto textom)

1. **Stav sa overí na začiatku sedenia.** `BLOCK` znamená, že sedenie má dve
   legálne možnosti: opraviť porušenie, alebo pracovať na `A0`.
2. **Nové vnorené podkoľaje v `A2` sú blokované.** Precedens: `D2SW0..D2SW16`,
   222 taskov, pohyb hĺbky nula.
3. **Zjemnenie špecifikácie chýbajúceho objektu nie je povolený krok**
   (`AGENTS.md` §4.1). Povolený krok je najhrubší explicitný kandidát.
4. **Smrť vyžaduje certifikát, nikdy nie neprítomnosť.** „Nevieme spočítať" je
   `UNDECIDED_FINITE` s cenovkou, nie verdikt.
5. **Vetva nikdy neobmedzuje inú koľaj.** `λ = 0.15` je vetva, nie mantinel.
6. **Do dokumentu sa nikdy neprepisuje kód** — len cesta a SHA-256.

## Rituál

- začiatok sedenia: hook spustí linter sám
- nový výpočet: `/qcts-new-calculation`
- koniec sedenia: `/qcts-session-close` — rozhodne (a)(b)(c) alebo **suchý beh**
- pred verziou: `python scripts/release_gate.py --version X.Y`

## Jazyk

Slovensky. Diakritika v texte áno, v kóde a identifikátoroch nie.
