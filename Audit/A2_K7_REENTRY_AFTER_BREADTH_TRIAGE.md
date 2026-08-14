# A2-K7 — re-entry audit po breadth triage

## Rozsudok

**K7 zostáva živým rodičom na 20,0/100 = G2. Žiadna zachovaná dcéra zatiaľ neuzatvára celú G3.**

Staré `30–42/100` boli intra-G3 checkpointy podľa staršej stupnice. Neobnovujú sa ako aktuálna sekvenčná hĺbka.

## Inventarizácia listov

| List | Stav | Zachovaný dôvod |
|---|---|---|
| fixed-width cascade | mŕtva M-014a | konštantná šírka nevie sledovať povinný `H rho_F` profil |
| holý Onsager cross-term | mŕtva M-014b | kinetická matica má zápornú vlastnú hodnotu |
| thermal gravity-only bath | mŕtva M-014d1 | sadzba chýba o 83–97 rádov |
| nekoherentný lokálny KMS prechod | mŕtva M-014d1b | sadzba chýba o 26–33 rádov a high-frequency únik ruší KMS predpoklad |
| vedúca zosilnená spin-2 väzba | mŕtva M-014d2a | vyžaduje extrémne zosilnenie a naráža na soft univerzálnosť |
| pozitívna Onsagerova rekonštrukcia | otvorená iba formulačne | transportné koeficienty, bath a noise nie sú odvodené |
| curvature-operator K1b2 | aktívna hypotéza | operator basis, redundancie, cutoff a sadzba neboli auditované |
| nový nespin-2 alebo interný bath | čaká | zatiaľ iba názov triedy |

## Najkonkrétnejší živý list

K1b2 je aktuálne najkonkrétnejší otvorený názov, ale ešte nemá explicitnú nezávislú bázu operátorov. Pred ďalším výpočtom by musel:

1. vypísať difeomorfne invariantné lokálne curvature operátory;
2. odstrániť on-shell nulové a field-redefinition redundantné členy;
3. určiť cutoff a skontrolovať `H/Lambda`, `omega/Lambda`, unitárnosť a soft limity;
4. odvodiť spektrálnu hustotu, retarded kernel a noise;
5. preukázať požadovanú produkčnú sadzbu bez porušenia EFT platnosti.

To už nie je lacný re-entry test, ale nová mikrofyzická konštrukcia porovnateľná s K8-Fkin, K9 a K12-K3.

## Obmedzenie rozsudkov

- M-014d1 platí iba pre thermal gravity-only kanál.
- M-014d1b platí iba pre auditovaný nekoherentný KMS prechod.
- M-014d2a platí iba pre vedúcu K1b1 spin-2 väzbu.
- Tieto dôvody sa nesmú použiť na automatickú smrť curvature K1b2, nového bathu ani celého K7.

## Rozhodnutie o priorite

Breadth triage nenašiel alternatívu pripravenú na lacný postup do vyššej brány:

- K7 potrebuje nový kernel G3,
- K8/K9/K12 potrebujú nový produkčný kernel,
- K11 potrebuje nový lokálny ortogonálny operátor.

K4 preto zostáva najlepšie rozpracovanou A2 koľajou. Priorita sa vracia ku K4, ale prvým krokom bude krátke profilovanie NIV segmentov a RHS, nie opakovanie plného 45-sekundového timeoutu.

