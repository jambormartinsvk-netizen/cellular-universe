"""Read-only PF-079 false-check diagnostic; no physics solve and no JSON."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR / "baseScripts" / "p5_general_synchronous"
EXPECTED = {
    "c2_fourier_coverage.py": "757F97E14657CC7046177C2D33115CA87639B9C92E89BDABE2BFF3B4380DF3FC",
    "c2_fourier_coverage_v2_c1_closed_support.py": "B563B919436B129E9B3C52AC011DC3190C6BA4773BD2B8094C35671AEE1B8A15",
    "c2_fourier_coverage_v3_exact_diff.py": "6AB7097DE6774086D664ACDCA4BC3171824003F177C191E7F5A73422A83391C9",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def main() -> int:
    actual = {name: sha256_file(BASE_DIR / name) for name in EXPECTED}
    if actual != EXPECTED:
        raise RuntimeError("KMPC-060 source hash mismatch")
    from baseScripts.p5_general_synchronous import c2_fourier_coverage_v3_exact_diff as audit
    guard = audit.contract_guard()
    false_checks = {name: value for name, value in guard["checks"].items() if not value}
    if not false_checks:
        raise RuntimeError("KMPC-060 expected at least one false check")
    payload = {
        "run_id": "KMPC-060",
        "execution_status": "READ_ONLY_DIAGNOSTIC_COMPLETE_NO_PHYSICS_VERDICT",
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "false_checks": false_checks,
        "guard_pass": guard["pass"],
        "closed_C1_supports": audit.v2.CLOSED_C1_SUPPORTS,
        "historical_S1_extended": audit.v2.HISTORICAL_S1_EXTENDED,
        "runtime_supports": audit.SUPPORTS,
        "source_hashes": actual,
    }
    print(json.dumps(payload, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
