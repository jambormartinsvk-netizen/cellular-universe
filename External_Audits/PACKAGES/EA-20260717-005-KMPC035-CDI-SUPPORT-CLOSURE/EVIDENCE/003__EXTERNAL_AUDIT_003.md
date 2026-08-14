# Auditná správa — EA-20260717-003-KMPC035-CDI-SUPPORT (R2)

**Audítorské prostredie:** Linux x86_64, Python 3.12.3, NumPy 2.4.4, SymPy 1.14.0 (pôvodné prostredie: Windows, Python 3.11, NumPy neznámej verzie).

## 1. Odpoveď na presnú otázku scope

Tvrdenie KMPC-035 — že CDI core/common je stabilné v rozsahu `[0,3]↔[0,5]` a že `[0,3]` remainder zostáva `REVIEW`, nie tichý PASS — je **matematicky správne a nezávisle reprodukované** `INDEPENDENTLY_RECOMPUTED`. Dependency chain pred ďalším krokom **naozaj zlyháva uzavreto** — overené spustením, nie iba čítaním kódu. Verdikt `PASS_CORE_AND_COMMON.../REVIEW_REMAINDER_UNCLOSED` je korektne odvodený z rozhodovacieho stromu preregistrácie a nikde som nenašiel tiché povýšenie remainderu na PASS. Dependency closure balíka má však jednu vecnú dieru (nález F1 nižšie).

## 2. Čo som nezávisle overil

**Hashe** `INDEPENDENTLY_RECOMPUTED`: všetkých 13 kódových/výsledkových súborov v EVIDENCE sedí s manifestom aj s voľnými kópiami; runner 279 obsahuje rovnaké očakávané hashe ako manifest — trojitá zhoda.

**Plná fyzikálna rekomputácia** `INDEPENDENTLY_RECOMPUTED`: zostavil som REPRO strom z dodaných base súborov a znovu vyriešil všetky tri supporty. Všetkých 180 exportovaných koeficientov sa zhoduje s raw JSON s najhorším relatívnym rozdielom `1.7e-11` (`U_fs[4]` pri `[0,5]`) — čisto medziplatformový BLAS drift. Solve trval 1.19 s, pod interným limitom 4.8 s. Ranky F0 `4/8/12` a M3 `26/52/78` sedia, driver residuá ≤ `4.7e-12`, holdout `00/0i` residuá ≤ `4.1e-13`, forbidden layers ≤ `2.4e-16`, `U_c` regularita `5.6e-17` — všetky brány PASS ako deklarované.

**Tail verdikt** `INDEPENDENTLY_RECOMPUTED`: prepočítal som metriku, branch a pass/fail pre všetkých 15 stavov × 2 plochy dvoma nezávislými cestami (z raw JSON aj z vlastného solve). Vzor zlyhania sa reprodukoval **presne**: pri `z=1e-2` zlyhá iba F0 `delta_f` (`2.524016e-5`) a M3 `sigma_fs` (`3.216708e-3`), zhodné s referenciou na 7 platných číslic. Common bridge na mojej platforme: F0 `4.13e-15`, M3 `1.45e-12` — iné než referenčné `1.15e-14/6.61e-13`, ale hlboko pod prahom `1e-8`. Tvrdenia „1707×/462× nad absolute hranicou" a kancelačné pomery `0.9993/0.9991` sedia — tail FAIL je vecný, nie artefakt kancelácie ani delenia nulou.

**Fyzikálne vzťahy v `FrozenInputs`** `OBSERVED_IN_PRIMARY`: `Ω_r0 = ω_γ(1+0.2271·N_eff)/h²`, `H0` v Mpc⁻¹, radiačné váhy sčítavajúce sa na 1, `f_b = ω_b/(Ω_m h²)` — štandardné a korektné. Mechanizmus `Q_f = -Γρ_f u_d`, `p = 4-3δ` je projektová hypotéza; auditujem vnútornú konzistenciu, nie zhodu s ΛCDM, čo je v súlade s pravidlom 001.

## 3. Nálezy

**F1 — STREDNÝ (dependency closure balíka):** Immutable KMPC-034 JSON (`RUN_KMPC_034..., SHA 37FB4453...`) je **povinná runtime závislosť regresnej brány, ale v balíku chýba** a nie je v manifeste. Smoke aj audit režim preto končia `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT` (overené spustením — fail-closed funguje správne, žiadny tichý skip). Dôsledok: cieľový tier `T2_REPRODUCIBLE_CALCULATION` nie je z balíka samotného dosiahnuteľný v audit režime; ja som ho dosiahol iba obídením regresnej brány priamym volaním solvera, čo je mimo kontraktu. Nemení to algebraický záver, mení to úplnosť dodávky. **Odporúčanie: pribaliť KMPC-034 JSON do R3.**

**F2 — STREDNÝ (platformová tesnosť regresnej tolerancie):** Regresný prah `1e-12` relatívne je tesnejší než pozorovaný medziplatformový drift (`1.7e-11`). Keby externý audítor mal KMPC-034 súbor, regresná brána by na inej platforme pravdepodobne dala `REVIEW_REGRESSION` aj pri správnej fyzike. Dokumentácia to čiastočne predvída, ale odporúčam explicitný dvojstupňový prah: `1e-12` pre same-machine immutabilitu, dokumentovaný voľnejší (napr. `1e-9`) pre cross-platform reprodukciu.

**F3 — STREDNÝ (interpretačný):** „Tail PASS pri `z=1e-4` pre F0 aj M3" je čiastočne artefakt absolute-fallback vetvy. `sigma_fs` má pri `z=1e-4` would-be relatívnu kontamináciu `3.215e-5` — 32× nad relatívnym prahom `1e-6`; prechádza len preto, že base `4.6e-16` je pod podlahou `1e-12`. Dizajn je obhájiteľný (relatívna chyba pod fyzikálnou podlahou je bezvýznamná), ale formulácia v dokumente 008 preceňuje konvergenciu. Podobne `U_c` pri `z=1e-2` prechádza absolute vetvou s would-be rel `6.27e-7` — tesne pod prahom. **Odporúčanie: exportovať would-be relatívnu metriku ako diagnostiku pre absolute-branch stavy.**

**F4 — STREDNÝ (metodologický):** Remainder test ohraničuje iba nasledujúce dve vynechané mocniny (`c4,c5` z `[0,5]` solve), nie plnú trunkačnú chybu nekonečného radu. Pre FAIL je to konzervatívne správnym smerom (verdikt platí), ale budúci PASS touto konštrukciou je nutná, nie postačujúca podmienka — predpokladá geometrický rozpad koeficientov. Plánovaný krok `[0,5]→[0,7]` tento predpoklad správne testuje.

**F5 — MENŠÍ (bug):** V `_write_atomic_exclusive` runnera 279: keď failure JSON už existuje, `os.link` vyhodí výnimku **po** vytvorení temp súboru a `.tmp-KMPC-035` artefakt zostane na disku (reprodukoval som to). Porušuje to vlastnú hygienickú garanciu „žiadny temp artefakt" pri opakovaných zlyhaniach. Oprava: `try/finally` s `temporary.unlink(missing_ok=True)`.

**F6 — MENŠÍ:** NumPy/BLAS verzia a platforma nie sú zapísané v JSON (priznaný „environment gap"). Pridať `numpy.__version__`, `platform.platform()` a BLAS info do výstupu.

**F7 — INFO:** Holdout `00/0i` zdieľa equation engine s drivermi (poctivo priznané); a prah `TAIL_TOL=1e-6` je preregistrovaný, ale jeho väzba na presnosť downstream pozorovateľných (G8/G9) je otvorený predpoklad.

## 4. Súvislosti a lepšie riešenia

**Štruktúra zlyhania z koeficientov** `INDEPENDENTLY_RECOMPUTED`: `delta_f` kontaminácia škáluje ~`z²` (`|c4/c2|z² ≈ 0.254 z²`), prah `1e-6` prekročí pri `z* ≈ 2.0e-3`. `sigma_fs` škáluje ~`z` (`|c4/c3|z ≈ 0.322 z`) a v relatívnej vetve zlyháva prakticky od `z ≳ 1.3e-3`. Odporúčam lacný diagnostický z-scan (5–8 bodov), aby bol onset zlyhania v zázname, nie iba na dvoch plochách.

**Predikcia pre krok 3** `INFERRED_FROM_PROJECT_DOCS` + vlastný odhad: pomery `|c5/c4| ≈ 0.037` (delta_f) a `0.044` (sigma_fs) ukazujú zrýchľujúci sa rozpad. Odhad kontaminácie supportu `[0,5]` pri `z=1e-2`: `sigma_fs ≲ 1.4e-8`, `delta_f ≲ 1e-10` — **support `[0,5]` s vysokou pravdepodobnosťou prejde tú istú bránu na oboch plochách.** Toto je testovateľná predpoveď pre KMPC step 3; ak sa nepotvrdí, znamená to zlom v rozpade koeficientov a treba prehodnotiť F4.

**Exaktná verifikácia:** systémy sú malé (≤78 neznámych) — jednorazová rekomputácia v presnej racionálnej aritmetike (`fractions`/`sympy.Rational`) by úplne eliminovala FP pochybnosti aj F2, a zároveň by nezávisle validovala zostavenie riadkov (uzavrela by aj F7 riziko spoločnej formulačnej chyby).

## 5. Zhodnotenie stavu a ďalší postup

Balík je vnútorne konzistentný, poctivo scoped a numericky robustný; vecný záver — `[0,3]` je pri zmrazenom prahu nedostatočný, core/common `[0,3]↔[0,5]` je stabilné, remainder ostáva REVIEW — som **plne nezávisle reprodukoval na inej platforme**. Žiadny nález nemení algebraický záver; F1–F2 sa týkajú úplnosti a prenosnosti dodávky, F3–F4 interpretačnej presnosti, F5–F6 hygieny.

Navrhované poradie krokov: (1) do R3 pribaliť KMPC-034 JSON a env metadáta (F1, F6); (2) opraviť temp-leak v runneri (F5); (3) doplniť would-be-rel diagnostiku a dvojtierový regresný prah (F2, F3); (4) po M1 order-7 bráne spustiť step 3 `[0,5]→[0,7]` — moja predikcia je PASS, čo by zároveň validovalo geometrický predpoklad z F4; (5) zvážiť jednorazovú exaktnú racionálnu rekomputáciu ako definitívne uzavretie numerických rizík. Projektový verdikt v súlade s pokynmi neudeľujem — odporúčam potvrdiť existujúci `PASS_CORE_AND_COMMON / REVIEW_REMAINDER_UNCLOSED` s výhradami F1–F3.
