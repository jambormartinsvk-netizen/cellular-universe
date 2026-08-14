# A2-K8 — kinetická produkcia s collision/noise kernelom

**Stav:** `LIVE_BACKUP / WAITING_FOR_EXPLICIT_RELAXATION_COLLISION_OPERATOR`  
**Workflow fáza:** `CONTRACT_DRAFT_NOT_OPEN / ACTIVE_ERROR_BATCH_NOT_STARTED`  
**Post-error stav:** `R8 PRE-SOLVER BLOCKER MAPPED — 2026-07-16`  
**FS-GATE-01:** `NONEMPTY_WITNESS_MOMENT_CONE`, ale
`STOP K8-Fkin-WARM-A1-SOURCE-ONLY`; rodič `REVIEW`; bez zmeny skóre  
**Max. hĺbka:** `10/100`

K8 používa kovariantné momenty produkčného collision operátora. Doterajší
ledger ukázal, že samotný počet vyrobených častíc neurčuje jednoznačne
hybnosť, tlak ani šum. Koľaj preto nie je mŕtva, ale bez explicitného `C[f]`
nemá uzavreté poruchové rovnice.

Scoped STOP source-only dcéry ani staré technické incidenty nezatvárajú
rodiča. Explicitný nový operator contract začne vlastný batch `0/10`.

Pokus o postup ku G5 sa zastavil na G2: treba konkrétny `C[f]`, birth
distribúciu a nultý, prvý aj druhý moment. Samotný number source body
nepridáva.

Mantinely teraz určujú správanie `C[f]` aj bez jeho presného tvaru. Pozitívna
on-shell birth miera s predpísaným `S_n,Q_c^mu` existuje, ale presný A1
background s tým istým `rho_c,q` vynúti `P_c=0`, cold podporu `p=0`,
`q=m_cS_n` a `Q_c^mu=q u_c^mu`. Preto je warm source-only dcéra analyticky
mŕtva; cold dcéra sa zlieva s K1 a dedí `M-009`.

Rodič zostáva v REVIEW iba pre taxonomicky širší prípad s explicitným
relaxačným/collision operátorom. Ak ten istý proces určuje produkciu aj
lineárny rozptyl, patrí do K9; samostatný drag patrí do K11 a warm mediátor
s vlastným energetickým ledgerom do K7. Presný dôkaz a obmedzenie staršieho
auditu sú v
`ARTIFACTS/FS_GATE_01_K8_FKIN_MOMENT_CONE_RESULT_AND_AUDIT.md`.
