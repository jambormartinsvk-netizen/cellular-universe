# REGISTER 05 — SK dodatok k A2-K7 M-014d1b

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; existujúce pravidlá sa nemenia

## Kontrola duplicity

AR20 oddeľuje typy bathu a AR21 korelačný čas od interakčnej rýchlosti.
Neoddeľujú však `2->2` bath scattering od emisného prechodu ani neurčujú,
kedy high-frequency spontaneous emission prestáva byť lokálnym KMS
bathom. AR23 a AR24 preto nie sú duplicitné.

## AR23 — Thermal-scattering rate nie je univerzálny bound emisného prechodu

Odhad odvodený pre relativistické `2->2` procesy pri energii `T` sa nesmie
bez nového odvodenia použiť na decay, spontaneous/stimulated emission alebo
koherentný kolektívny prechod. Každý kanál musí mať vlastnú energetickú
medzeru, maticový element, výberové pravidlá, form factor a rate skript.
Príliš široký skorší rozsudok sa zachová s erratom.

## AR24 — High-frequency spontánna emisia bez reverse absorption nie je lokálny KMS bath

Ak potrebný prechod spĺňa `omega/T>>1`, reverse absorption je Boltzmannovsky
potlačená. Taký kanál sa nesmie používať ako lokálny termálny Onsager/KMS
bath. Musí sa presunúť do vákuovej alebo netermálnej farebnej koľaje s
vlastným memory/noise kernelom. Koherentné zosilnenie musí byť odvodené,
nie nahradené počtom buniek bez form factoru.

## Q50 — Prežil nekoherentný KMS gravitonový prechod K1a2a?

**Stav:** `NIE — MŔTVA M-014d1b, Max. hĺbka 42/100.`

V optimistickej obálke `Gamma=omega^3/Mbar_Pl^2` chýba pri `omega<=T`
zosilnenie `2.2e26–3.7e33`. Rate bez zosilnenia by vyžadoval
`omega=10.8–229 MeV`, čiže `omega/T~6e8–1.5e11`; reverse absorption je
prakticky nulová. Koherentná K1a2b ostáva otvorená a high-frequency
spontaneous vetva sa presúva do K2. K7 ostáva `30/100`.

### Obmedzenie starších formulácií

M-014d1 sa po audite vzťahuje iba na K1a1 thermal-scattering kanál, nie na
každý gravity-only prechod. Číselná `M_eff` časť M-014d2a je tiež viazaná na
thermal-scattering model; soft-Ward smrť vedúcej K1b1 zostáva platná.

