"""80-dps reassembly of the independent BI/k=.15 holdout.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The 104x104 driver solve is inherited unchanged from KMPC-083.  Only the
independent Einstein 00/0i audit rows are reassembled at high precision;
they are never added to the fit.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Callable, Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_holdout as hp
from . import c2_bi_k0p15_high_precision_holdout_v2_deadline as v2


physics = hp.physics
legacy = physics.legacy
contract = physics.contract
PRECISION_DPS = hp.PRECISION_DPS
AUDIT_SUPPORT = (0, 7)
EXPECTED_ROWS = 16
EXPECTED_COLUMNS = 104
_ORIGINAL_SOLVE_M3 = physics._solve_m3
_V2_SOURCE_HASHES = v2.source_hashes
_V2_CONTRACT_GUARD = v2.contract_guard
_EXACT_HOLDOUT: dict[str, object] | None = None


def configure(**config: object) -> None:
    v2.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v2.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v2.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V2_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_high_precision_holdout_assembly.py"] = legacy.sha256_file(
        here / "c2_bi_k0p15_high_precision_holdout_assembly.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V2_CONTRACT_GUARD()
    guard["checks"].update({
        "assembly_precision_exact": PRECISION_DPS == 80,
        "audit_support_exact": AUDIT_SUPPORT == (0, 7),
        "holdout_shape_exact": (EXPECTED_ROWS, EXPECTED_COLUMNS) == (2 * 8, 13 * 8),
        "holdout_contract_exact": contract.AUTHORITATIVE_HOLDOUT
        == ("Einstein_00", "Einstein_0i"),
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _mp(value: object) -> mp.mpf:
    if isinstance(value, mp.mpf):
        return value
    return hp._mp(float(value))


class _MPSeries:
    def __init__(self, lo: int, hi: int) -> None:
        self.lo = lo
        self.hi = hi
        self.floor = _mp(1.0e-300)

    def clean(self, item: dict[int, mp.mpf]) -> dict[int, mp.mpf]:
        return {
            int(key): _mp(value) for key, value in item.items()
            if self.lo <= int(key) <= self.hi and abs(value) > self.floor
        }

    def add(self, *items: dict[int, mp.mpf]) -> dict[int, mp.mpf]:
        out: dict[int, mp.mpf] = {}
        for item in items:
            for key, value in item.items():
                if self.lo <= key <= self.hi:
                    out[key] = out.get(key, mp.mpf("0")) + value
        return self.clean(out)

    def scale(self, item: dict[int, mp.mpf], factor: object) -> dict[int, mp.mpf]:
        factor_mp = _mp(factor)
        return self.clean({key: factor_mp * value for key, value in item.items()})

    def mul(
        self, first: dict[int, mp.mpf], second: dict[int, mp.mpf]
    ) -> dict[int, mp.mpf]:
        out: dict[int, mp.mpf] = {}
        for i, left in first.items():
            for j, right in second.items():
                if self.lo <= i + j <= self.hi:
                    out[i + j] = out.get(i + j, mp.mpf("0")) + left * right
        return self.clean(out)

    def dx(self, item: dict[int, mp.mpf]) -> dict[int, mp.mpf]:
        return self.clean({key: _mp(key) * value for key, value in item.items()})

    def inv(self, item: dict[int, mp.mpf]) -> dict[int, mp.mpf]:
        entries = sorted((key, value) for key, value in item.items()
                         if abs(value) > _mp(1.0e-15))
        if not entries:
            raise ZeroDivisionError("zero standard series")
        lead_key, lead = entries[0]
        out = {-lead_key: mp.mpf("1") / lead}
        for n in range(1, self.hi + lead_key + 1):
            total = mp.fsum(
                item.get(lead_key + j, mp.mpf("0"))
                * out.get(-lead_key + n - j, mp.mpf("0"))
                for j in range(1, n + 1)
            )
            out[-lead_key + n] = -total / lead
        return self.clean(out)


Pair = tuple[dict[int, mp.mpf], dict[int, mp.mpf]]


class _MPPairSeries:
    def __init__(self, standard: _MPSeries, p: object, f_lo: int, f_hi: int) -> None:
        self.s = standard
        self.p = _mp(p)
        self.f_lo = f_lo
        self.f_hi = f_hi
        self.floor = _mp(1.0e-300)

    def fclean(self, item: dict[int, mp.mpf]) -> dict[int, mp.mpf]:
        return {
            int(key): _mp(value) for key, value in item.items()
            if self.f_lo <= int(key) <= self.f_hi and abs(value) > self.floor
        }

    def fadd(self, *items: dict[int, mp.mpf]) -> dict[int, mp.mpf]:
        out: dict[int, mp.mpf] = {}
        for item in items:
            for key, value in item.items():
                if self.f_lo <= key <= self.f_hi:
                    out[key] = out.get(key, mp.mpf("0")) + value
        return self.fclean(out)

    def fscale(self, item: dict[int, mp.mpf], factor: object) -> dict[int, mp.mpf]:
        factor_mp = _mp(factor)
        return self.fclean({key: factor_mp * value for key, value in item.items()})

    def sfmul(
        self, standard: dict[int, mp.mpf], fractional: dict[int, mp.mpf]
    ) -> dict[int, mp.mpf]:
        out: dict[int, mp.mpf] = {}
        for i, left in standard.items():
            for j, right in fractional.items():
                if self.f_lo <= i + j <= self.f_hi:
                    out[i + j] = out.get(i + j, mp.mpf("0")) + left * right
        return self.fclean(out)

    def add(self, *pairs: Pair) -> Pair:
        return self.s.add(*(item[0] for item in pairs)), self.fadd(
            *(item[1] for item in pairs)
        )

    def scale(self, pair: Pair, factor: object) -> Pair:
        return self.s.scale(pair[0], factor), self.fscale(pair[1], factor)

    def mul(self, left: Pair, right: Pair) -> Pair:
        return self.s.mul(left[0], right[0]), self.fadd(
            self.sfmul(left[0], right[1]), self.sfmul(right[0], left[1])
        )

    def inv(self, pair: Pair) -> Pair:
        inv_standard = self.s.inv(pair[0])
        fractional = self.fscale(
            self.sfmul(inv_standard, self.sfmul(inv_standard, pair[1])), -1.0
        )
        return inv_standard, fractional

    def dx(self, pair: Pair) -> Pair:
        return self.s.dx(pair[0]), self.fclean({
            j: (self.p + _mp(j)) * value for j, value in pair[1].items()
        })


def _mp_dict(item: dict[int, object]) -> dict[int, mp.mpf]:
    return {int(key): _mp(value) for key, value in item.items()}


def _background(k_mpc: float, inputs: object, hi: int,
                series: _MPSeries, pair: _MPPairSeries) -> dict[str, Pair]:
    float_series = legacy.Series(series.lo, series.hi)
    bg0 = legacy._standard_background(k_mpc, inputs, float_series)
    bg1 = legacy._fractional_background(k_mpc, hi + 10, inputs)
    denominator = (_mp_dict(bg0["D"]), _mp_dict(bg1["D1"]))
    invd = pair.inv(denominator)
    hc = pair.add(
        ({0: _mp(-1.0)}, {}),
        pair.scale(pair.mul(pair.dx(denominator), invd), 0.5),
    )
    s2 = pair.mul(({2: _mp(1.0)}, {}), invd)
    rg, rfs, _, _ = inputs.radiation_weights
    og = pair.scale(invd, rg)
    ofs = pair.scale(invd, rfs)
    mu = _mp(bg0["mu"])
    ob = pair.mul(({1: _mp(inputs.fb) * mu}, {}), invd)
    oc = pair.mul(({1: _mp(inputs.fc) * mu}, _mp_dict(bg1["ash"])), invd)
    of = pair.mul(({}, _mp_dict(bg1["fuel"])), invd)
    loading = ({1: _mp(3.0) * _mp(inputs.fb) * mu / (_mp(4.0) * _mp(rg))}, {})
    inv1r = pair.inv(pair.add(({0: _mp(1.0)}, {}), loading))
    load_fraction = pair.mul(loading, inv1r)

    gamma0 = _mp_dict(bg1["gamma"])
    d1_over_d0 = pair.sfmul(_mp_dict(bg0["invD"]), _mp_dict(bg1["D1"]))
    gamma1 = pair.fscale(pair.sfmul(gamma0, d1_over_d0), -0.5)
    gamma = (gamma0, gamma1)
    fc_mu = _mp(inputs.fc) * mu
    r1 = {power - 1: _mp(value) / fc_mu for power, value in bg1["fuel"].items()}
    beta1 = {power: _mp(inputs.delta) * value for power, value in r1.items()}
    return {
        "hc": hc, "s2": s2, "Og": og, "Ofs": ofs, "Ob": ob, "Oc": oc,
        "Of": of, "inv1R": inv1r, "load_fraction": load_fraction,
        "gamma": gamma, "r": ({}, pair.fclean(r1)),
        "beta": ({}, pair.fclean(beta1)),
    }


def _holdout_affine(
    k_mpc: float, inputs: object, standard: dict[str, dict[int, float]],
    solution: list[mp.mpf], support: tuple[int, int],
) -> dict[str, object]:
    lo, hi = support
    exponents = list(range(lo, hi + 1))
    series = _MPSeries(min(-8, lo - 8), hi + 12)
    pair = _MPPairSeries(series, inputs.p, lo - 8, hi + 8)
    bg = _background(k_mpc, inputs, hi, series, pair)
    names = tuple(contract.AUTHORITATIVE_STATE)
    index = {
        (name, power): position
        for position, (name, power) in enumerate(
            item for name in names for item in ((name, e) for e in exponents)
        )
    }
    if len(index) != EXPECTED_COLUMNS or len(solution) != EXPECTED_COLUMNS:
        raise ValueError("exact holdout assembly shape mismatch")
    standard_mp = {name: _mp_dict(standard[name]) for name in names}

    def row_values(vector: list[mp.mpf]) -> list[mp.mpf]:
        state: dict[str, Pair] = {
            name: (
                standard_mp[name],
                {e: vector[index[(name, e)]] for e in exponents},
            )
            for name in names
        }
        hx = pair.dx(state["h"])
        etax = pair.dx(state["eta"])
        density = pair.add(
            pair.mul(bg["Og"], state["delta_gamma"]),
            pair.mul(bg["Ofs"], state["delta_fs"]),
            pair.mul(bg["Ob"], state["delta_b"]),
            pair.mul(bg["Oc"], state["delta_c"]),
            pair.mul(bg["Of"], state["delta_f"]),
        )
        momentum = pair.add(
            pair.scale(pair.mul(bg["Og"], state["U_gamma"]), 2.0),
            pair.scale(pair.mul(bg["Ofs"], state["U_fs"]), 2.0),
            pair.scale(pair.mul(bg["Ob"], state["U_b"]), 1.5),
            pair.scale(pair.mul(bg["Oc"], state["U_c"]), 1.5),
            pair.scale(pair.mul(bg["Of"], state["U_f"]), 1.5 * inputs.delta),
        )
        rows = {
            "Einstein_00": pair.add(
                pair.scale(hx, -0.5), pair.scale(density, 1.5),
                pair.mul(bg["s2"], state["eta"]),
            ),
            "Einstein_0i": pair.add(etax, pair.scale(momentum, -1.0)),
        }
        return [rows[name][1].get(e, mp.mpf("0"))
                for name in contract.AUTHORITATIVE_HOLDOUT for e in exponents]

    zero = [mp.mpf("0") for _ in range(EXPECTED_COLUMNS)]
    constant = row_values(zero)
    matrix = [[mp.mpf("0") for _ in range(EXPECTED_COLUMNS)]
              for _ in range(EXPECTED_ROWS)]
    for column in range(EXPECTED_COLUMNS):
        probe = list(zero)
        probe[column] = mp.mpf("1")
        values = row_values(probe)
        for row in range(EXPECTED_ROWS):
            matrix[row][column] = values[row] - constant[row]

    labels = [f"{name}[{e}]" for name in contract.AUTHORITATIVE_HOLDOUT
              for e in exponents]
    norm_floor = _mp(physics.ABS_FALLBACK_NORM)
    relative_max = mp.mpf("0")
    absolute_max = mp.mpf("0")
    relative_worst: int | None = None
    absolute_worst: int | None = None
    relative_count = 0
    absolute_count = 0
    row_details: dict[str, dict[str, object]] = {}
    for row in range(EXPECTED_ROWS):
        terms = [matrix[row][column] * solution[column]
                 for column in range(EXPECTED_COLUMNS)]
        residual = constant[row] + mp.fsum(terms)
        term_norm = abs(constant[row]) + mp.fsum(abs(term) for term in terms)
        if term_norm > norm_floor:
            relative_count += 1
            metric = abs(residual) / term_norm
            branch = "relative"
            if metric > relative_max:
                relative_max, relative_worst = metric, row
        else:
            absolute_count += 1
            metric = abs(residual)
            branch = "absolute_fallback"
            if metric > absolute_max:
                absolute_max, absolute_worst = metric, row
        row_details[labels[row]] = {
            "branch": branch,
            "residual_decimal": mp.nstr(residual, 50),
            "absolute_residual": float(abs(residual)),
            "affine_term_norm_decimal": mp.nstr(term_norm, 50),
            "affine_term_norm": float(term_norm),
            "metric_decimal": mp.nstr(metric, 50),
            "metric": float(metric),
        }

    digest = hashlib.sha256()
    for row in range(EXPECTED_ROWS):
        digest.update(mp.nstr(constant[row], 90).encode("ascii"))
        digest.update(b"|")
        for value in matrix[row]:
            digest.update(mp.nstr(value, 90).encode("ascii"))
            digest.update(b"|")
    passed = bool(
        relative_max <= _mp(physics.HOLDOUT_TOL)
        and absolute_max <= _mp(physics.ABS_FALLBACK_TOL)
    )
    return {
        "precision_dps": PRECISION_DPS,
        "scope": "HP_REASSEMBLY_FROM_EXACTLY_BRIDGED_FLOAT64_UPSTREAM_COEFFICIENTS",
        "shape": [EXPECTED_ROWS, EXPECTED_COLUMNS],
        "matrix_constant_sha256": digest.hexdigest().upper(),
        "rows_added_to_driver_solve": 0,
        "max_relative_residual": float(relative_max),
        "max_relative_residual_decimal": mp.nstr(relative_max, 50),
        "max_absolute_fallback_residual": float(absolute_max),
        "max_absolute_fallback_residual_decimal": mp.nstr(absolute_max, 50),
        "relative_row_count": relative_count,
        "absolute_fallback_row_count": absolute_count,
        "worst_relative_row": labels[relative_worst] if relative_worst is not None else None,
        "worst_absolute_fallback_row": labels[absolute_worst]
        if absolute_worst is not None else None,
        "Einstein_0i_7": row_details["Einstein_0i[7]"],
        "pass_holdout": passed,
    }


def _solve_m3(mode: str, k_mpc: float, inputs: object,
              standard: dict[str, dict[int, float]], support: tuple[int, int],
              deadline: Callable[[], None]):
    global _EXACT_HOLDOUT
    result = _ORIGINAL_SOLVE_M3(mode, k_mpc, inputs, standard, support, deadline)
    if mode == "BI" and k_mpc == 0.15 and support == AUDIT_SUPPORT:
        if hp._HP_SOLUTION is None:
            raise RuntimeError("high-precision driver solution unavailable for assembly audit")
        with mp.workdps(PRECISION_DPS):
            _EXACT_HOLDOUT = _holdout_affine(
                k_mpc, inputs, standard, hp._HP_SOLUTION, support
            )
    return result


@contextmanager
def _overlay() -> Iterator[None]:
    global _EXACT_HOLDOUT
    before = (physics._solve_m3, v2.source_hashes, v2.contract_guard)
    _EXACT_HOLDOUT = None
    try:
        physics._solve_m3 = _solve_m3
        v2.source_hashes = source_hashes
        v2.contract_guard = contract_guard
        yield
    finally:
        physics._solve_m3, v2.source_hashes, v2.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        physics._solve_m3 is _ORIGINAL_SOLVE_M3
        and v2.source_hashes is _V2_SOURCE_HASHES
        and v2.contract_guard is _V2_CONTRACT_GUARD
    )


def _fixture() -> dict[str, bool]:
    with mp.workdps(PRECISION_DPS):
        bridged = _mp(0.1)
        numerator, denominator = 0.1.as_integer_ratio()
        exact_bridge = bridged == mp.mpf(numerator) / denominator
        affine_constant = _mp(0.1) + _mp(0.2)
        affine_coefficient = (_mp(1.1) + _mp(0.2)) - affine_constant
        affine_value = affine_constant + affine_coefficient * _mp(2.0)
        affine_pass = affine_value == affine_constant + _mp(2.0)
    return {
        "exact_float_bridge": bool(exact_bridge),
        "affine_reassembly_fixture": bool(affine_pass),
        "holdout_nonfit_contract": contract.AUTHORITATIVE_HOLDOUT
        == ("Einstein_00", "Einstein_0i"),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v2.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({f"assembly_{key}": value
                                  for key, value in _fixture().items()})
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["assembly_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float,
             result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v2.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored() or _EXACT_HOLDOUT is None:
        raise RuntimeError("high-precision assembly lifecycle incomplete")
    hp_boundary = payload["high_precision_holdout_boundary"]
    driver = hp_boundary["driver"]
    other_gates = bool(
        payload["M1"]["pass"] and payload["common_pass"] and payload["tail_pass"]
        and payload["background_guard"]["pass"] and payload["S_C0_actual_guard"]["pass"]
        and driver["pass_driver"] and hp_boundary["high_precision_solve_count"] == 1
    )
    passed = bool(other_gates and _EXACT_HOLDOUT["pass_holdout"])
    payload["high_precision_holdout_assembly"] = {
        "driver_matrix_constant_sha256": driver["matrix_constant_sha256"],
        "driver_identity": driver["matrix_identity"],
        "high_precision_solve_count": hp_boundary["high_precision_solve_count"],
        "driver_pass_replacement": driver["pass_driver"],
        "all_other_frozen_gates_pass_with_hp_replacements": other_gates,
        "holdout": _EXACT_HOLDOUT,
        "pass": passed,
        "scope_limit": "DRIVER_MATRIX_ASSEMBLY_REMAINS_FLOAT64",
    }
    payload["core_pass_high_precision_holdout_assembly"] = passed
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C2_BI_K0p15_HOLDOUT_ASSEMBLY_ROUNDOFF_CLOSED_CANDIDATE_ONLY"
        if passed else "REVIEW_C2_BI_K0p15_EXACT_DRIVER_ASSEMBLY_REQUIRED"
    )
    payload["score_effect"] = "NONE_PENDING_INTERNAL_AUDIT"
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision holdout assembly has no aggregate scope")
