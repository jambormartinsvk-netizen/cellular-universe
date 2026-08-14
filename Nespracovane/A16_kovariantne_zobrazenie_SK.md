# A16. Kovariantné zobrazenie rovníc V1 (interagujúca dvojtekutinová sústava)

**Účel sekcie:** ukázať, že sústava V1 nie je zbierka ad-hoc pravidiel
stojacich mimo všeobecnej relativity, ale presná FRW limita štandardnej
kovariantnej triedy interagujúcich modelov tmavej energie. Bianchiho
identita je splnená identicky, nie deklaráciou. Modelovo špecifická
ostáva *mikroskopická interpretácia* dvoch konštánt (δ, λ), ktorá žije
o poschodie nižšie — tak, ako kinetická teória žije pod
Navierom–Stokesom.

## A16.1 Kovariantná sústava

Nech palivo, hmota a žiarenie nesú tenzory energie-hybnosti T_f^{μν},
T_m^{μν}, T_r^{μν} so stavovými rovnicami w_f = −1 + δ, w_m = 0,
w_r = 1/3, a nech si vymieňajú energiu cez prenosový prúd:

    ∇_μ T_f^{μν} = −Q u^ν
    ∇_μ T_m^{μν} = +Q u^ν
    ∇_μ T_r^{μν} = 0
    Q = λ H₀ ρ_f

kde u^ν je spoločná komohybná štvorrýchlosť. Súčet dáva

    ∇_μ (T_f + T_m + T_r)^{μν} = 0

**identicky** — celková energia-hybnosť je zachovaná konštrukciou,
Bianchiho identita platí a Einsteinove rovnice G_{μν} = 8πG T^tot_{μν}
sú konzistentné. Tým je zodpovedaná otázka „kde sa δ objaví
v Einsteinovej rovnici": v T_f^{μν} cez w_f = −1 + δ, a λ v prenosovom
prúde Q.

## A16.2 FRW limita reprodukuje V1 presne

V plochom FRW pozadí s x = ln a a ρ̇ = H·dρ/dx prejdú rovnice
kontinuity na

    dρ_f/dx = −3(1 + w_f) ρ_f − (Q/H)  = −3δ ρ_f − λ (H₀/H) ρ_f
    dρ_m/dx = −3 ρ_m + λ (H₀/H) ρ_f
    dρ_r/dx = −4 ρ_r

čo sú po vydelení dnešnou kritickou hustotou presne rovnice V1
používané v pipeline (skript 09). Pri preklade sa nič nepridalo ani
nestratilo.

## A16.3 Miesto v literatúre

Sústava patrí do štandardnej, rozsiahlo študovanej triedy
interagujúcich modelov tmavej energie s rýchlosťou prenosu Q = Γ ρ_DE
a **konštantným** Γ = λH₀. Bunkový vesmír vyberá jedného člena tejto
triedy a — na rozdiel od generickej fenomenológie — viaže jeho dve
konštanty na mikrofyziku: δ = 1/(⟨k⟩ + C) z réžie delenia (merané
v modeli, Q2/Q9) a λ z katalýzy jaziev (odvodenie V1, Q3). Na úrovni
tejto sekcie však δ a λ fungujú ako obyčajné konštanty kovariantného
efektívneho popisu — pozadie sa nikde neodchyľuje od VR.

## A16.4 Poruchy: voľba prenosu, vyslovená nahlas

Každý interagujúci model musí povedať, ako prenosový prúd vstupuje do
porušených rovníc. Pipeline používa **geodetický (bezhybnostný)
prenos**: Q^ν = Q u^ν s u^ν v pokojovej sústave hmoty — vytvorená
hmota sa rodí komohybná s lokálnym tokom a výmena nesie energiu, ale
žiadnu hybnosť do porúch. Pri tejto voľbe si lineárne rovnice rastu
zachovávajú štandardný tvar (sekcia V3) a celý vplyv bunkového sektora
na rast štruktúr vstupuje výlučne cez funkcie pozadia E(x) a Ω_m(x).

Je to *voľba s povrchovou stopou*: prenos nesúci hybnosť by pridal do
Eulerovej rovnice člen podobný piatej sile a deformoval by
redshift-space distortions. Súčasná formulácia predpovedá žiadnu takú
deformáciu nad rámec efektu pozadia; potvrdená RSD anomália vyžadujúca
prenos hybnosti by toto čítanie výmeny falzifikovala, nie iba
preparametrizovala.

## A16.5 Čo sekcia tvrdí a čo netvrdí

**Tvrdí:** sústava V1 žije vnútri všeobecnej relativity ako
kovariantný interagujúci dvojtekutinový model; Bianchi platí presne;
fenomenológia pozadia (účtovný tieň w(z), H₀, éra paliva) nevyžaduje
žiadnu modifikáciu Einsteinových rovníc.

**Netvrdí:** fundamentálny Lagrangián samotnej siete ani odvodenie
δ a λ z akcie. Tie ostávajú na mikrodynamickej úrovni (merania VCM
a odvodenie V1 člen po člene) a sú tak poctivo registrované.
