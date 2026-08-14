#!/usr/bin/env python3
"""
release_gate.py - branka pred vydanim akejkolvek verzie teorie.

Kazda kontrola tu zodpoveda JEDNEJ zdokumentovanej chybe verzie 3.18.
Ziadne zavislosti, ziadny LLM.

Spustenie z korena repozitara:
    python scripts/release_gate.py --version 3.18
    python scripts/release_gate.py --version 3.19 --readme theory/EN/00_README_EN.md

Exit: 0 = verzia sa smie vydat, 1 = nesmie.
"""
import argparse
import json
import os
import re
import subprocess
import sys

# ---- zakazane slova v release/README (audit 2 VI.2, VI.3) -------------------
ZAKAZANE = {
    "derives": "README tvrdi 'derives', kym v3.18 hovori, ze lambda je data-selected a C bolo zvolene",
    "without unconstrained free parameters": "nepravda: lambda, C, l_cell, A_f, M",
    "fully falsifiable": "§12 vyzaduje 'demonstrovatelne vycerpavajuci top-level zoznam' - nesplnitelne",
    "external audit": "cela vrstva su jazykove modely; spravny tvar je 'independent LLM agent audit'",
    "external auditor": "to iste",
    "independent mathematical and physical audits": "konotuje recenziu clovekom",
}
# slova povolene len s vyslovnou kvalifikaciou v tej istej vete
PODMIENENE = {
    "predicts": ("conditional", "diagnostic", "not a prediction", "pre-A3"),
    "graviton": ("has not been derived", "nie je odvodene", "hypothes"),
}

# ---- kill conditions, ktore preukazatelne nefunguju (audit 2 VI.2) ----------
ZLE_KILL = {
    "wimp": "neodporuje teorii: vlastne P07 hovori, ze mikrofyzika popola nie je odvodena",
    "h0 >= 72": "uz splnene (SH0ES 73.0 +- 1.0); unikova klauzula 'without systematics' "
                "ho robi nefalzifikovatelnym",
}

FAILS = []
WARNS = []


def fail(rid, msg, precedent):
    FAILS.append((rid, msg, precedent))


def warn(rid, msg, precedent):
    WARNS.append((rid, msg, precedent))


def sig_digits(tok):
    t = tok.lstrip("+-").replace(".", "").lstrip("0").rstrip("0")
    return len(t)


# ---------------------------------------------------------------- kontroly

def g01_git_tag(version, root):
    """audit 2 VI.1 - tag v3.18 neexistuje, vsetky evidence odkazy su 404"""
    try:
        out = subprocess.run(["git", "-C", root, "tag", "-l"], capture_output=True,
                             text=True, timeout=20).stdout.split()
    except Exception as e:
        warn("G01", f"git sa neda spustit ({e!r}) - tag neoverany", "VI.1")
        return
    if f"v{version}" not in out:
        fail("G01", f"git tag 'v{version}' neexistuje -> kazdy odkaz na dokazovy balik "
                    f"v release vedie na 404 a §13 citacna podmienka nie je splnena", "VI.1")


def g02_zakazane_slova(paths):
    """audit 2 VI.2, VI.3 - README tvrdi presne to, co v3.18 popiera"""
    for p in paths:
        if not os.path.exists(p):
            warn("G02", f"subor {p} neexistuje - nekontrolovany", "VI.2")
            continue
        txt = open(p, encoding="utf-8", errors="replace").read()
        low = txt.lower()
        for slovo, preco in ZAKAZANE.items():
            if slovo in low:
                fail("G02", f"{os.path.basename(p)}: obsahuje '{slovo}' -> {preco}", "VI.2/VI.3")
        for slovo, kvalif in PODMIENENE.items():
            for m in re.finditer(re.escape(slovo), low):
                veta = low[max(0, m.start() - 250): m.start() + 250]
                if not any(k in veta for k in kvalif):
                    fail("G02", f"{os.path.basename(p)}: '{slovo}' bez kvalifikacie "
                                f"({'/'.join(kvalif)}) v okoli", "VI.2")
                    break


def g03_verzia_a_doi(version, paths):
    """audit 2 VI.1 - README popisuje v3.17 a cituje stary DOI"""
    for p in paths:
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8", errors="replace").read()
        vs = set(re.findall(r"v?(\d+\.\d+)", txt))
        stare = {v for v in vs if re.match(r"^3\.\d+$", v) and v != version}
        if stare:
            fail("G03", f"{os.path.basename(p)}: spomina ine verzie teorie {sorted(stare)} "
                        f"popri v{version}", "VI.1")


def g04_falosna_precizia(paths, maxd):
    """audit 2 C2 - A_f = 7809.270101963506 pri vstupoch s 3-4 ciframi"""
    for p in paths:
        if not os.path.exists(p):
            continue
        for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
            if line.lstrip().startswith(("```", "    ", "\t")):
                continue        # kod a bloky sa netykaju publikovanych cisel
            for tok in re.findall(r"(?<![\w.])\d+\.\d+(?![\w])", line):
                if sig_digits(tok) > maxd:
                    fail("G04", f"{os.path.basename(p)}:{i}: {tok} ma {sig_digits(tok)} "
                                f"platnych cifier > {maxd}", "C2")
                    return       # jeden nalez staci, inak zaplavi vystup


def g05_kill_conditions(paths):
    """audit 2 VI.2 - dve kill conditions nefunguju"""
    for p in paths:
        if not os.path.exists(p):
            continue
        low = open(p, encoding="utf-8", errors="replace").read().lower()
        if "kill" not in low:
            continue
        for vzor, preco in ZLE_KILL.items():
            if vzor in low:
                fail("G05", f"{os.path.basename(p)}: kill condition obsahuje '{vzor}' -> {preco}",
                     "VI.2")


def g06_ns_okno(paths):
    """audit 2 VI.2 - README ma +-0.004, P02 ma +-0.0016, faktor 2.5"""
    okna = set()
    for p in paths:
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"0\.965\d*\s*(?:\+/-|±|\+-)\s*(0\.\d+)", txt):
            okna.add(m.group(1))
    if len(okna) > 1:
        fail("G06", f"kill window pre n_s je nekonzistentne: {sorted(okna)}", "VI.2")


def g07_predikcie(state):
    """audit 2 V.10 - interne 'Neprijate' vs publikovane survival targets"""
    for p in state.get("predikcie", []):
        if not p.get("status"):
            fail("G07", f"{p['id']}: chyba status", "V.10")
        if not p.get("internal_accepted", True) and "PRE_A3" not in p.get("status", "") \
                and p.get("status") not in ("WITHDRAWN", "IDENTITY"):
            fail("G07", f"{p['id']}: interne neprijate, ale publikovane ako "
                        f"'{p['status']}'", "V.10")
        if p.get("value") is not None and not p.get("receipt"):
            fail("G07", f"{p['id']}: publikovana hodnota {p['value']} bez receiptu "
                        f"-> nedohladatelna", "moja poznamka k Dodatku A1")


def g08_state_linter(root):
    """stav musi byt cisty; verzia sa nevydava na porusenom stave"""
    lint = os.path.join(root, "scripts", "check_state.py")
    st = os.path.join(root, "tracks", "00_STATE.json")
    if not (os.path.exists(lint) and os.path.exists(st)):
        warn("G08", "check_state.py alebo 00_STATE.json chyba - stav neoverany", "-")
        return
    r = subprocess.run([sys.executable, lint, st], capture_output=True, text=True)
    if r.returncode == 1:
        fail("G08", "check_state.py hlasi BLOCK -> verzia sa nesmie vydat na porusenom stave. "
                    "Spusti `python scripts/check_state.py` a oprav.", "-")


def g09_stanice(state):
    """nova: verzia sa nevydava, kym je upstream stanica nerozhodnuta"""
    for s in state.get("stanice", []):
        if s.get("status") == "LIVE_ACTIVE" and s["id"] == "A0":
            warn("G09", "stanica A0 je nerozhodnuta -> kazde A2/A3 cislo v release je "
                        "podmienene a musi to byt v texte napisane", "V.9")


# ---------------------------------------------------------------- beh

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True)
    ap.add_argument("--root", default=".")
    ap.add_argument("--readme", action="append", default=[])
    ap.add_argument("--max-digits", type=int, default=4)
    a = ap.parse_args()
    root = os.path.abspath(a.root)

    paths = a.readme or [os.path.join(root, p) for p in (
        "00_README_EN.md",
        f"tracks/RELEASE/V{a.version.replace('.', '_')}/DEV_SURVIVAL_REWRITE/README.md",
        f"tracks/RELEASE/V{a.version.replace('.', '_')}/DEV_SURVIVAL_REWRITE/theory/EN/00_README_EN.md",
    )]

    st_path = os.path.join(root, "tracks", "00_STATE.json")
    state = json.load(open(st_path, encoding="utf-8")) if os.path.exists(st_path) else {}

    print(f"=== release_gate.py :: v{a.version} ===\n")
    g01_git_tag(a.version, root)
    g02_zakazane_slova(paths)
    g03_verzia_a_doi(a.version, paths)
    g04_falosna_precizia(paths, a.max_digits)
    g05_kill_conditions(paths)
    g06_ns_okno(paths)
    if state:
        g07_predikcie(state)
        g09_stanice(state)
    g08_state_linter(root)

    for rid, msg, prec in FAILS:
        print(f"  BLOCK {rid}  {msg}\n        precedens: audit 2 {prec}")
    for rid, msg, prec in WARNS:
        print(f"  WARN  {rid}  {msg}")
    if not FAILS and not WARNS:
        print("  vsetky kontroly presli")
    print(f"\n=== {len(FAILS)} blokujucich, {len(WARNS)} varovani ===")
    if FAILS:
        print(f"v{a.version} sa NESMIE vydat.")
        return 1
    print(f"v{a.version} sa smie vydat.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
