# Q22a/Q18 — ledger mantinelov pre funkciu skorého zdroja pary

**Účel:** najprv určiť prienik všetkých fyzikálnych a observačných podmienok;
až potom hľadať možný priebeh zdroja `C_steam`.  
**Stav:** `PREREGISTROVANÝ CONSTRAINT LEDGER; bez vybraného tvaru funkcie`.

## Premenná, ktorú chceme obmedziť

V homogénnej FLRW limite platí

```text
d rho_s/dx + 4 rho_s = S_s(x),   x=ln a.
```

Fundamentálne prijateľný zdroj však nesmie byť iba ručne zvolená funkcia
koordináty `x`. Musí mať lokálny kovariantný pôvod

```text
S_s^mu = C_s(chi, I_1, I_2, ...) u^mu,
```

kde `chi` je definovaný lokálny skalárny clock/stav rezervoára a `I_i` sú
lokálne skalárne invarianty. Na FLRW riešení potom `S_s=C_s/H` dá funkciu
času. Bez `chi` alebo ekvivalentného dynamického stavu je `S_s(x)` len
efektívna história, nie mikrofyzický zákon.

## Tvrdé mantinely

| ID | Mantinel | Čo musí platiť | Súčasný stav |
|---|---|---|---|
| M0 | Lokálnosť a kovariancia | `C_s` je skalár z definovaných miestnych polí/stavov; žiadny voľný kozmický čas | **REVIEW/STOP** — audit `Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md` potvrdil, že chýba `chi`/rezervoár; nejde o smrť efektívnej triedy |
| M1 | Energia-hybnosť | `nabla T_s=+S_s`, `nabla T_e=-S_s`, teda súčet zdrojov je nula | Algebraicky splniteľné |
| M2 | Kladnosť | `rho_s>=0`, `rho_e>=0`, `H^2>0` po celej histórii | Testovať po definícii rezervoára |
| M3 | Neskorý parný rozpočet | perzistentný priamy neskorý kanál je M-015; pri priamom podiele platí `f_R<~3.2e-5` | **TVRDÝ SCREEN PASS iba pre nulový/zanedbateľný neskorý chvost** |
| M4 | Časovanie | konzervatívne: zdroj skončí pred BBN; miernejšie verzie potrebujú spoločný BBN+CMB likelihood | Q18/Q23 otvorené |
| M5 | Reliktná normalizácia | po skončení zdroja `rho_s∝a^-4`; cieľová `Delta N_eff` je boundary condition, nie fit do pozadia | `0.0535` je podmienené |
| M6 | Entropia | celková produkcia entropie je nezáporná a bez dvojitého účtovania | Q29 otvorená |
| M7 | Poruchy | z toho istého operátora vznikne `delta S_s`, frame, šum a `P_AB(k)`; bez zakázanej izokurvatúry | Q22/Q20 otvorené |
| M8 | Causalita a stabilita | žiadne superluminalné charakteristiky, duchy, gradientový rast ani nekonečné sadzby | A2/Q20 brána |
| M9 | Žiadny skrytý fit | tvar, prah, šírka a normalizácia vychádzajú z mikrofyziky; dáta ich iba testujú | OTVORENÝ |
| M10 | Žiadne `k` v pozadí | realizovaný Fourierov mód nevstupuje do `H(a)` ani `C_s` backgroundu | TVRDÝ, AR8 |

## Prienik, ktorý sa bude testovať

Funkcia môže byť kandidátom iba vtedy, ak patrí do množiny

```text
F_allowed = M0 ∩ M1 ∩ M2 ∩ M3 ∩ M4 ∩ M5 ∩ M6 ∩ M7 ∩ M8 ∩ M9 ∩ M10.
```

V súčasnosti vieme dokázať, že prienik `M1∩M2∩M3∩M4∩M5∩M10` nie je prázdny
na úrovni **efektívnej FLRW histórie**: kladný zdroj s konečnou skorou podporou
a párovým rezervoárom ho splní. Nevieme však ešte rozhodnúť, či zostane
neprázdny po M0, M6, M7, M8 a M9. To je presná forma otvoreného problému.

## Ako z mantinelov odvodíme priebeh, nie fit

1. Najprv sa určí, čo je `chi` a rezervoár `e`; tým M0 zmení voľnú funkciu na
   funkciu stavu.
2. M1–M2 určia dovolené znamienko, energetický budget a maximálnu amplitúdu.
3. M3–M5 určia, že zdroj musí mať skorú podporu a nulový/zanedbateľný neskorý
   chvost; nevyberajú zatiaľ jeho detailný tvar.
4. M6–M8 odstránia priebehy s nesprávnou entropiou, šumom alebo nestabilitou.
5. M9 rozhodne, či zostávajúci tvar naozaj predikuje sieť, alebo je len fit.

Ak po krokoch 1–4 zostane prázdna množina, hypotéza skorého reliktu zomrie.
Ak zostane neprázdna, ale M9 nie je splnené, ide iba o fyzikálne možnú triedu,
nie o predikciu bunkového vesmíru.

Presný protokol, ktorý z každého mantinelu robí rovnicu, nerovnosť alebo
okrajovú podmienku pre spoločný systém stavov, je v
`Q22A_CONSTRAINT_TO_FUNCTION_DERIVATION_PROTOCOL_SK.md`. Jeho výsledkom musí
byť jedna trajektória, explicitná rodina alebo prázdna množina — nie voľne
vybraná funkcia.

## Najbližší auditný krok

M0 audit je uzavretý s výsledkom `REVIEW/STOP`: súčasné premenné neurčujú
lokálny monotónny `chi` ani rezervoár. Pred akýmkoľvek výpočtom tvarov sa
preto musí vytvoriť auditovateľná jazvová alebo exit/reheating koľaj podľa
`Audit/Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md`. Až jej
M0 prechod oprávňuje testovať M1–M5 na konkrétnom funkčnom tvare.

Obmedzený pracovný strom P1–P5 s presnými STOP kritériami je v
`Q22A_CONSTRAINT_TO_FUNCTION_WORK_PLAN_SK.md`; začína read-only inventúrou
P1.1 a výslovne zakazuje voľný sken tvarov pred prechodom M0–M2.
