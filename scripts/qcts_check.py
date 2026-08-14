"""
qcts_check.py - overovaci harness pre vypocty projektu Teoria/QCTS.

Ciel: vypocet nesie svoje vlastne falzifikacne testy a spusti ich zakazdym.
Vysledok sa NEVYPISE, ak niektora povinna kontrola padla.

Pouzitie:  jeden import, ziadne projektove zavislosti.
Kazdy skript je samostatne spustitelny fyzikom: `python skript.py`

    from qcts_check import Run

    r = Run("A0K5_cutoff_scan", question="Q-A0-LORENTZ-RADIATIVE-STABILITY")

    r.check("LI limit, cutoff -> inf", val, 0.0, tol=1e-12, kind="NULL_LIMIT",
            why="Lorentzovsky invariantna disperzia nesmie generovat LV")
    r.check("analyticka kotva", val2, -1/(96*pi**2*kmax**2), tol=1e-3, kind="ANCHOR")
    r.converged("rozlisenie", [v_lo, v_mid, v_hi], rtol=1e-3)

    r.result("dc2/c2", 3.53e-2, unit="1")
    r.finish()

Vystup: stdout + <nazov>_receipt.json s SHA-256 SAMOTNEHO spusteneho suboru,
verziami prostredia a vsetkymi kontrolami. Receipt je audit trail; nepise sa rucne.
"""

import hashlib
import json
import os
import platform
import sys

__version__ = "1.0"

# povinne triedy kontrol - kazdy vypocet musi mat aspon NULL_LIMIT alebo ANCHOR
KINDS = {
    "NULL_LIMIT",    # vypni novu fyziku -> musi vyjst znamy vysledok
    "ANCHOR",        # pripad s uzavretym analytickym rieseniem
    "IDENTITY",      # velicina, ktora musi byt presne nula (conservation, constraint)
    "CONVERGENCE",   # stabilita voci rozliseniu / tolerancii / metode
    "DIMENSION",     # rozmerova/jednotkova kontrola
    "CROSSCHECK",    # nezavisla reimplementacia kritickeho kroku
    "SEED",          # stabilita voci nahodnemu seedu
}

_HARD = {"NULL_LIMIT", "ANCHOR", "IDENTITY"}   # padnutie = vysledok sa nevypise


def _sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(65536), b""):
            h.update(blk)
    return h.hexdigest()


class CheckFailed(Exception):
    pass


class Run:
    def __init__(self, name, question=None, contract_sha=None, strict=True):
        self.name = name
        self.question = question
        self.contract_sha = contract_sha
        self.strict = strict
        self.checks = []
        self.results = []
        self.notes = []
        try:
            self.script = os.path.abspath(sys.argv[0])
            self.script_sha = _sha256_of_file(self.script)
        except Exception:
            self.script = "<unknown>"
            self.script_sha = None
        self._env = self._environment()
        print(f"=== {name} ===")
        if question:
            print(f"otazka: {question}")
        print(f"skript: {os.path.basename(self.script)}  sha256={self.script_sha}")
        print(f"prostredie: {self._env['python']}, " +
              ", ".join(f"{k} {v}" for k, v in self._env["packages"].items()))
        print("--- kontroly ---")

    @staticmethod
    def _environment():
        pkgs = {}
        for mod in ("numpy", "scipy", "sympy", "mpmath"):
            try:
                pkgs[mod] = __import__(mod).__version__
            except Exception:
                pass
        return {"python": platform.python_version(),
                "platform": platform.platform(),
                "packages": pkgs}

    # --- kontroly -------------------------------------------------------

    def check(self, label, value, expected, tol, kind, why="", absolute=True):
        """Jedna kontrola. tol je absolutna (default) alebo relativna."""
        if kind not in KINDS:
            raise ValueError(f"neznama trieda kontroly: {kind}. Povolene: {sorted(KINDS)}")
        value = float(value)
        expected = float(expected)
        diff = abs(value - expected)
        if not absolute:
            denom = abs(expected) if expected != 0 else 1.0
            diff = diff / denom
        ok = diff <= tol
        self._record(label, kind, ok, value, expected, diff, tol, why)
        return ok

    def is_zero(self, label, value, tol, why=""):
        """Skratka pre veliciny, ktore musia byt presne nula."""
        return self.check(label, value, 0.0, tol, "IDENTITY", why)

    def converged(self, label, series, rtol, why=""):
        """series = vysledky pri rastucom rozliseni/presnosti. Posledne dva sa musia zhodovat."""
        series = [float(x) for x in series]
        a, b = series[-2], series[-1]
        denom = abs(b) if b != 0 else 1.0
        diff = abs(a - b) / denom
        ok = diff <= rtol
        self._record(f"{label} (rad {series})", "CONVERGENCE", ok, b, a, diff, rtol, why)
        return ok

    def crosscheck(self, label, value_a, value_b, rtol, why=""):
        """Dve nezavisle implementacie toho isteho kroku."""
        return self.check(label, value_a, value_b, rtol, "CROSSCHECK", why, absolute=False)

    def note(self, text):
        self.notes.append(text)
        print(f"  [pozn] {text}")

    def _record(self, label, kind, ok, value, expected, diff, tol, why):
        self.checks.append(dict(label=label, kind=kind, ok=bool(ok), value=value,
                                expected=expected, diff=diff, tol=tol, why=why))
        mark = "OK  " if ok else "PAD "
        hard = " [POVINNA]" if kind in _HARD else ""
        print(f"  {mark} {kind:<12} {label}{hard}")
        print(f"       hodnota={value:.6e}  ocakavane={expected:.6e}  "
              f"odchylka={diff:.2e}  tol={tol:.2e}")
        if why:
            print(f"       preco: {why}")
        if not ok and kind in _HARD:
            print(f"       >>> POVINNA KONTROLA PADLA. Je to chyba IMPLEMENTACIE, nie fyziky.")

    # --- vysledky -------------------------------------------------------

    @property
    def failed_hard(self):
        return [c for c in self.checks if not c["ok"] and c["kind"] in _HARD]

    @property
    def failed_soft(self):
        return [c for c in self.checks if not c["ok"] and c["kind"] not in _HARD]

    def result(self, label, value, unit="", sig=4):
        """Vysledok sa NEVYPISE, ak padla povinna kontrola."""
        if not self.checks:
            raise CheckFailed("ziadna kontrola nebola spustena - vysledok nie je pripustny")
        if not any(c["kind"] in ("NULL_LIMIT", "ANCHOR") for c in self.checks):
            raise CheckFailed("chyba aspon jedna NULL_LIMIT alebo ANCHOR kontrola")
        if self.failed_hard:
            print(f"  ZADRZANE  {label}: povinna kontrola padla, vysledok nie je vysledok")
            self.results.append(dict(label=label, value=None, unit=unit,
                                     withheld=True))
            if self.strict:
                return None
            return None
        self.results.append(dict(label=label, value=float(value), unit=unit,
                                 withheld=False))
        return value

    def finish(self, path=None):
        print("--- vysledky ---")
        for r in self.results:
            if r["withheld"]:
                print(f"  {r['label']}: ZADRZANE")
            else:
                print(f"  {r['label']} = {r['value']:.4g} {r['unit']}".rstrip())
        n_ok = sum(1 for c in self.checks if c["ok"])
        status = ("FAIL_IMPLEMENTATION" if self.failed_hard else
                  "PASS_WITH_SOFT_FAILURES" if self.failed_soft else "PASS")
        print(f"--- stav: {status}  ({n_ok}/{len(self.checks)} kontrol) ---")
        receipt = dict(
            harness_version=__version__, name=self.name, question=self.question,
            script=os.path.basename(self.script), script_sha256=self.script_sha,
            contract_sha256=self.contract_sha, environment=self._env,
            status=status, checks=self.checks, results=self.results, notes=self.notes,
        )
        path = path or os.path.join(os.path.dirname(self.script) or ".",
                                    f"{self.name}_receipt.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=2, ensure_ascii=False)
        print(f"receipt: {os.path.basename(path)}")
        if self.failed_hard and self.strict:
            sys.exit(2)          # fail-closed: neuspesny beh ma nenulovy exit kod
        return receipt
