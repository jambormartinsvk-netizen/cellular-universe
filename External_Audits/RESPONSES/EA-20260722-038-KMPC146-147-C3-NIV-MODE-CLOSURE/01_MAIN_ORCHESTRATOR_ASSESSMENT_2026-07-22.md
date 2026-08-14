# Hlavný posudok EA-038 — KMPC-146/147 C3 NIV mode closure

**Dátum:** 2026-07-22  
**Autorita:** hlavný orchestrátor  
**Externý posudok SHA-256:**
`A18EAA2A6C4619E32E1E2A0EAD06E95FE1165BC97B789AF062839866B759CC3D`  
**Rozhodnutie:** `ACCEPT_EXTERNAL_AGREE_IN_DECLARED_MIXED_TIER_SCOPE`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

## 1. Overenie posudku

Externý agent zachoval originálny package immutable a vykonal všetky
povinné kontroly. R6 preflight prešiel `105/105`; manifest `15/15`, runtime
mapa `3/3`, package snapshot pred/po aj nulové duplicity boli potvrdené.

KMPC-146 bol auditovaný na deklarovanej úrovni T1. Source/raw audit
potvrdil ranky 104/130, tri same-matrix corrections, nezmenenú maticu/RHS,
support/depth/prahy, nulové pridanie holdoutu do drivera, owner restoration,
štyri úspešné selection rules a všetky inherited fyzikálne brány true.
PF-129 bola nezávisle potvrdená ako presná štvorka JSON key-type parity
false-negative, nie fyzikálny alebo numerický rozdiel.

KMPC-147 dosiahol T2 bez odchýlky. Compile/help/smoke/official mali exit
`0/0/0/0`; generated raw SHA bol
`8633DF7C8E583A04A6EE4F05BCEA9D4CB04F7A410BCC9DA6EE9E00AC8BF3A2CE`.
Po jedinej povolenej normalizácii runtime poľa bol diff `0` a normalized
SHA oboch strán
`33C977BA43D3E94D4EF3798C5A82EE8BC74D66C05324ED3E9E410868D36E5635`.
Protected projekcia bola exact na SHA
`9F76DD48A83DEC2AB825A0E1B2B0D22B443F5965868BCAAFD46812033E360A0A`;
operation counts boli `workers=solvers=physics=0`. Oba missing-input guardy
skončili exit `2` fail-closed bez success/failure rawu a bez fyzikálneho
verdiktu.

Externý audit nenašiel CRITICAL, MATERIAL ani MINOR nález a nepoužil nijakú
`DECLARED_DEVIATION`.

## 2. Rozhodnutie hlavného orchestrátora

Prijímam odporúčanie `AGREE` v presne deklarovanom mixed-tier scope:

- `PASS_C3_NIV_K0P15_3_OF_3` ostáva autoritatívny;
- NIV ostáva `9/9 PASS`;
- globálna C3 logical coverage ostáva `45/45 PASS`;
- K4 ostáva `60/100`;
- technický counter ostáva `0/10` a PF-129 zostáva historicky zachovaná.

Scope limit KMPC-146 T1 sa nezamlčuje ani nerozširuje na fresh T2. Je
akceptovateľný pre túto auditnú jednotku, pretože nezmenený fyzikálny základ
má EA-037 T2 a EA-038 priamo auditoval novú source/raw delta; KMPC-147
read-only kompozícia bola navyše reprodukovaná na T2.

## 3. Otvorený ďalší krok

Externá auditná pauza EA-038 je uzavretá. Povolený je iba samostatne
predregistrovaný read-only C3 aggregate nad exact hashovým registrom 45
autoritatívnych logických atómov. Aggregate nesmie volať solver ani meniť
rovnice, hodnoty, prahy alebo jednotlivé verdikty. Musí fail-closed overiť
identity, SHA, `9/9` pre všetkých päť módov a `45/45` súčet.

Toto rozhodnutie samo nespúšťa aggregate, P5.4, G8, G9, release, Zenodo ani
prediction-table zmenu. S-M mikrofyzická para zostáva osobitne otvorená.
