# A2-K9 — spoločný produkčno-rozptylový operátor

**Stav:** `LIVE_BACKUP / WAITING_FOR_SINGLE_SHARED_PRODUCTION_TRANSPORT_OPERATOR`  
**Workflow fáza:** `CONTRACT_DRAFT_NOT_OPEN / ACTIVE_ERROR_BATCH_NOT_STARTED`  
**Post-error stav:** `R8 PRE-SOLVER BLOCKER MAPPED — 2026-07-16`  
**FS-GATE-01:** `NONEMPTY_MARKOV_MOMENT_CLASS / REVIEW`; scoped STOP pre
`K9-1TO2-EXACT-THRESHOLD-FINITE-RATE`; bez zmeny skóre  
**Max. hĺbka:** `10/100`

K9 požaduje jeden mikrofyzický operátor, ktorý súčasne určí produkciu a
rozptyl. Audit ukázal nejednoznačnosť momentov pri voľbe iba makroskopických
sadzieb. Životaschopná verzia nesmie zaviesť dva nezávislé fitované kernely
pre background a poruchy.

Scoped STOP exact-threshold dcéry nie je technický ani fyzikálny STOP
rodiča. Nový shared-operator contract začne vlastný batch `0/10`.

Pokus o postup ku G5 sa zastavil na G2: jeden konkrétny proces musí naraz
odvodiť produkciu, rozptyl, reakciu, tlak a noise. Dve nezávisle ladené
sadzby by už neboli K9.

Behaviorálny obal vyžaduje, aby produkcia, drag a noise reagovali na ten
istý coupling a nulový limit. Nezávislý ľubovoľný `kappa` je mimo množiny
K9 ešte pred poznaním presného kernelu.

FS-GATE našla explicitný cold gain–loss svedok: background môže mať
`q=m_cS_n`, `P_c=0`, kým number-conserving reset dá na lineárnom ráde
pasívny `-K(v_c-v_f)` a ohrev až `O(v_rel^2)`. Preto momentový priestor nie
je prázdny. Svedok však neodvodzuje oba kanály z jedného QFT/bunkového
maticového elementu, takže G2 neprešla a stav 10/100 sa nemení.

Bežný hladký dvojtelesový rozpad presne na cold prahu s konečnou nenulovou
šírkou je mŕtvy: na prahu zanikne fázový priestor; nad prahom vznikne warm
tlak a narazí na K8 pressureless-A1 no-go. Aktuálny constraint-derived cieľ
`K9-CTLR` potrebuje coherent/cold production a z tej istej interakcie
odvodený pomer production/transport bez druhého fitu. Detaily sú v
`ARTIFACTS/FS_GATE_01_K9_SHARED_PRODUCTION_SCATTERING_RESULT_AND_AUDIT.md`.
