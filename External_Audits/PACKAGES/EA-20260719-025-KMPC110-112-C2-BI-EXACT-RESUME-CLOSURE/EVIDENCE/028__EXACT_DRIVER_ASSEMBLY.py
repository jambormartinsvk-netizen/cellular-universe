"""80-dps driver assembly boundary for C2 BI/k=.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The authoritative driver is rebuilt and solved at high precision.  Einstein
00/0i remain independent holdouts and never enter either driver solve.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_holdout_assembly_v3_fixture as prior


assembly = prior.v1
hp = assembly.hp
physics = assembly.physics
contract = assembly.contract
PRECISION_DPS = assembly.PRECISION_DPS
AUDIT_SUPPORT = (0, 7)
EXPECTED_ROWS = 104
EXPECTED_COLUMNS = 104
EXPECTED_HOLDOUT_ROWS = 16
_PRIOR_SOURCE_HASHES = prior.source_hashes
_PRIOR_CONTRACT_GUARD = prior.contract_guard
_ASSEMBLY_SOLVE_M3 = assembly._solve_m3
_HP_SOLVER = hp._solve_equilibrated
_FLOAT_MATRIX = None
_FLOAT_CONSTANT = None
_EXACT_BOUNDARY: dict[str, object] | None = None


def configure(**config: object) -> None:
    prior.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return prior.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return prior.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_PRIOR_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_high_precision_driver_assembly.py"] = (
        prior.v2.hash_owner.sha256_file(
            here / "c2_bi_k0p15_high_precision_driver_assembly.py"
        )
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _PRIOR_CONTRACT_GUARD()
    guard["checks"].update({
        "driver_shape_exact": (EXPECTED_ROWS, EXPECTED_COLUMNS) == (13 * 8, 13 * 8),
        "holdout_shape_exact": (EXPECTED_HOLDOUT_ROWS, EXPECTED_COLUMNS)
        == (2 * 8, 13 * 8),
        "ordered_driver_exact": len(contract.AUTHORITATIVE_DRIVER) == 13,
        "ordered_state_exact": len(contract.AUTHORITATIVE_STATE) == 13,
        "two_hp_solves_exact": True,
        "holdout_nonfit": not set(contract.AUTHORITATIVE_DRIVER)
        & set(contract.AUTHORITATIVE_HOLDOUT),
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _capture_hp_solver(matrix, constant, expected_rank, row_labels=None, deadline=None):
    global _FLOAT_MATRIX, _FLOAT_CONSTANT
    if expected_rank == EXPECTED_COLUMNS:
        if _FLOAT_MATRIX is not None:
            raise RuntimeError("more than one 104x104 baseline driver capture")
        _FLOAT_MATRIX = matrix.copy()
        _FLOAT_CONSTANT = constant.copy()
    return _HP_SOLVER(
        matrix, constant, expected_rank, row_labels=row_labels, deadline=deadline
    )


def _fingerprint(matrix: list[list[mp.mpf]], constant: list[mp.mpf]) -> str:
    digest = hashlib.sha256()
    for row, c_value in zip(matrix, constant):
        digest.update(mp.nstr(c_value, 90).encode("ascii"))
        digest.update(b"|")
        for value in row:
            digest.update(mp.nstr(value, 90).encode("ascii"))
            digest.update(b"|")
    return digest.hexdigest().upper()


def _vector_fingerprint(vector: list[mp.mpf]) -> str:
    digest = hashlib.sha256()
    for value in vector:
        digest.update(mp.nstr(value, 90).encode("ascii"))
        digest.update(b"|")
    return digest.hexdigest().upper()


def _solve_affine(matrix: list[list[mp.mpf]], constant: list[mp.mpf]) -> list[mp.mpf]:
    rows = len(matrix)
    columns = len(matrix[0])
    if rows != columns or len(constant) != rows:
        raise ValueError("exact driver affine system is not square")
    floor = assembly._mp(1.0e-300)
    row_scale = [
        max([abs(value) for value in matrix[i]] + [abs(constant[i]), floor])
        for i in range(rows)
    ]
    column_scale = [
        max([abs(matrix[i][j] / row_scale[i]) for i in range(rows)] + [floor])
        for j in range(columns)
    ]
    scaled = mp.matrix([
        [matrix[i][j] / row_scale[i] / column_scale[j] for j in range(columns)]
        for i in range(rows)
    ])
    rhs = mp.matrix([-constant[i] / row_scale[i] for i in range(rows)])
    solved = mp.lu_solve(scaled, rhs)
    return [solved[j] / column_scale[j] for j in range(columns)]


def _metrics(matrix: list[list[mp.mpf]], constant: list[mp.mpf],
             solution: list[mp.mpf], labels: list[str], threshold: float,
             pass_key: str) -> dict[str, object]:
    relative_max = mp.mpf("0")
    absolute_max = mp.mpf("0")
    relative_worst: int | None = None
    absolute_worst: int | None = None
    relative_count = 0
    absolute_count = 0
    norm_floor = assembly._mp(physics.ABS_FALLBACK_NORM)
    for i, row in enumerate(matrix):
        terms = [row[j] * solution[j] for j in range(len(solution))]
        residual = constant[i] + mp.fsum(terms)
        term_norm = abs(constant[i]) + mp.fsum(abs(term) for term in terms)
        if term_norm > norm_floor:
            relative_count += 1
            metric = abs(residual) / term_norm
            if metric > relative_max:
                relative_max, relative_worst = metric, i
        else:
            absolute_count += 1
            metric = abs(residual)
            if metric > absolute_max:
                absolute_max, absolute_worst = metric, i
    passed = bool(
        relative_max <= assembly._mp(threshold)
        and absolute_max <= assembly._mp(physics.ABS_FALLBACK_TOL)
    )
    return {
        "precision_dps": PRECISION_DPS,
        "max_relative_residual": float(relative_max),
        "max_relative_residual_decimal": mp.nstr(relative_max, 50),
        "max_absolute_fallback_residual": float(absolute_max),
        "max_absolute_fallback_residual_decimal": mp.nstr(absolute_max, 50),
        "relative_row_count": relative_count,
        "absolute_fallback_row_count": absolute_count,
        "worst_relative_row": labels[relative_worst]
        if relative_worst is not None else None,
        "worst_absolute_fallback_row": labels[absolute_worst]
        if absolute_worst is not None else None,
        pass_key: passed,
    }


def _assembly_difference(matrix: list[list[mp.mpf]], constant: list[mp.mpf],
                         labels: list[str], names: tuple[str, ...]) -> dict[str, object]:
    if _FLOAT_MATRIX is None or _FLOAT_CONSTANT is None:
        raise RuntimeError("float64 baseline matrix capture unavailable")
    if tuple(_FLOAT_MATRIX.shape) != (EXPECTED_ROWS, EXPECTED_COLUMNS):
        raise ValueError("float64 baseline shape mismatch")
    max_absolute = mp.mpf("0")
    max_relative = mp.mpf("0")
    worst_absolute = None
    worst_relative = None
    changed = 0
    total = EXPECTED_ROWS * EXPECTED_COLUMNS + EXPECTED_ROWS
    floor = assembly._mp(1.0e-30)
    for i in range(EXPECTED_ROWS):
        entries = [("constant", constant[i], assembly._mp(_FLOAT_CONSTANT[i]))]
        entries.extend(
            (names[j], matrix[i][j], assembly._mp(_FLOAT_MATRIX[i, j]))
            for j in range(EXPECTED_COLUMNS)
        )
        for column_name, exact, baseline in entries:
            difference = abs(exact - baseline)
            if difference != 0:
                changed += 1
            relative = difference / max(abs(exact), abs(baseline), floor)
            if difference > max_absolute:
                max_absolute = difference
                worst_absolute = f"{labels[i]}::{column_name}"
            if relative > max_relative:
                max_relative = relative
                worst_relative = f"{labels[i]}::{column_name}"
    return {
        "entries_total": total,
        "entries_changed": changed,
        "max_absolute_difference": float(max_absolute),
        "max_absolute_difference_decimal": mp.nstr(max_absolute, 50),
        "worst_absolute_entry": worst_absolute,
        "max_relative_difference_floor_1e30": float(max_relative),
        "max_relative_difference_floor_1e30_decimal": mp.nstr(max_relative, 50),
        "worst_relative_entry": worst_relative,
        "float64_matrix_constant_sha256": hp._matrix_fingerprint(
            _FLOAT_MATRIX, _FLOAT_CONSTANT
        ),
    }


def _exact_driver_boundary(k_mpc: float, inputs: object,
                           standard: dict[str, dict[int, float]],
                           support: tuple[int, int]) -> dict[str, object]:
    lo, hi = support
    exponents = list(range(lo, hi + 1))
    series = assembly._MPSeries(min(-8, lo - 8), hi + 12)
    pair = assembly._MPPairSeries(series, inputs.p, lo - 8, hi + 8)
    bg = assembly._background(k_mpc, inputs, hi, series, pair)
    names = tuple(contract.AUTHORITATIVE_STATE)
    drivers = tuple(contract.AUTHORITATIVE_DRIVER)
    index = {
        (name, power): position
        for position, (name, power) in enumerate(
            item for name in names for item in ((name, e) for e in exponents)
        )
    }
    if len(index) != EXPECTED_COLUMNS:
        raise ValueError("exact driver state shape mismatch")
    standard_mp = {name: assembly._mp_dict(standard[name]) for name in names}
    zero = mp.mpf("0")
    one = mp.mpf("1")
    two = mp.mpf("2")
    three = mp.mpf("3")
    four = mp.mpf("4")
    delta = assembly._mp(inputs.delta)

    def row_values(vector: list[mp.mpf]) -> list[mp.mpf]:
        state = {
            name: (
                standard_mp[name],
                {e: vector[index[(name, e)]] for e in exponents},
            )
            for name in names
        }
        hx = pair.dx(state["h"])
        etax = pair.dx(state["eta"])
        hxx = pair.dx(hx)
        etaxx = pair.dx(etax)
        u_difference = pair.add(state["U_f"], pair.scale(state["U_c"], -one))
        u_d = pair.add(state["U_c"], pair.mul(bg["beta"], u_difference))
        gamma_r = pair.mul(bg["gamma"], bg["r"])
        gamma_r_beta = pair.mul(gamma_r, bg["beta"])
        pressure_factor = pair.add(({0: three * delta}, {}), bg["gamma"])
        fuel_pressure = pair.add(
            state["delta_f"],
            pair.scale(pair.mul(pressure_factor, state["U_f"]), two - delta),
        )
        rows = {
            "gamma_continuity": pair.add(
                pair.dx(state["delta_gamma"]),
                pair.scale(pair.mul(bg["s2"], state["U_gamma"]), four / three),
                pair.scale(hx, two / three),
            ),
            "gamma_Euler": pair.add(
                pair.dx(state["U_gamma"]),
                pair.scale(pair.mul(bg["hc"], state["U_gamma"]), -one),
                pair.mul(bg["load_fraction"], state["U_gamma"]),
                pair.scale(pair.mul(bg["inv1R"], state["delta_gamma"]), -one / four),
            ),
            "fs_continuity": pair.add(
                pair.dx(state["delta_fs"]),
                pair.scale(pair.mul(bg["s2"], state["U_fs"]), four / three),
                pair.scale(hx, two / three),
            ),
            "fs_shear": pair.add(
                pair.scale(pair.dx(state["sigma_fs"]), two),
                pair.scale(hx, -four / assembly._mp(15)),
                pair.scale(etax, -assembly._mp(8) / assembly._mp(5)),
                pair.scale(pair.mul(bg["s2"], state["U_fs"]),
                           -assembly._mp(8) / assembly._mp(15)),
            ),
            "fs_Euler": pair.add(
                pair.dx(state["U_fs"]),
                pair.scale(pair.mul(bg["hc"], state["U_fs"]), -one),
                pair.scale(state["delta_fs"], -one / four),
                state["sigma_fs"],
            ),
            "baryon_continuity": pair.add(
                pair.dx(state["delta_b"]), pair.mul(bg["s2"], state["U_b"]),
                pair.scale(hx, one / two),
            ),
            "cdm_continuity": pair.add(
                pair.dx(state["delta_c"]), pair.mul(bg["s2"], state["U_c"]),
                pair.scale(hx, one / two),
                pair.scale(pair.mul(
                    gamma_r,
                    pair.add(state["delta_f"], pair.scale(state["delta_c"], -one)),
                ), -one),
            ),
            "cdm_Euler": pair.add(
                pair.dx(state["U_c"]),
                pair.scale(pair.mul(
                    pair.add(bg["hc"], ({0: -one}, {})), state["U_c"]
                ), -one),
                pair.scale(pair.mul(gamma_r_beta, u_difference), -one),
            ),
            "tight_coupling": pair.add(
                state["U_b"], pair.scale(state["U_gamma"], -one)
            ),
            "fuel_continuity": pair.add(
                pair.dx(state["delta_f"]),
                pair.scale(state["delta_f"], three * (two - delta)),
                pair.scale(pair.mul(bg["s2"], state["U_f"]), delta),
                pair.scale(hx, delta / two),
                pair.scale(state["U_f"], assembly._mp(9) * delta * (two - delta)),
                pair.scale(pair.mul(bg["gamma"], state["U_f"]),
                           three * (two - delta)),
            ),
            "fuel_Euler": pair.add(
                pair.dx(state["U_f"]),
                pair.scale(pair.mul(
                    pair.add(bg["hc"], ({0: two}, {})), state["U_f"]
                ), -one),
                pair.scale(state["delta_f"], -one / delta),
                pair.scale(pair.mul(
                    bg["gamma"],
                    pair.add(pair.scale(state["U_f"], two), pair.scale(u_d, -one)),
                ), -one / delta),
            ),
            "Einstein_trace": pair.add(
                hxx, pair.mul(pair.add(bg["hc"], ({0: two}, {})), hx),
                pair.scale(pair.mul(bg["s2"], state["eta"]), -two),
                pair.scale(pair.mul(bg["Og"], state["delta_gamma"]), three),
                pair.scale(pair.mul(bg["Ofs"], state["delta_fs"]), three),
                pair.scale(pair.mul(bg["Of"], fuel_pressure), assembly._mp(9)),
            ),
            "Einstein_traceless": pair.add(
                hxx, pair.mul(pair.add(bg["hc"], ({0: two}, {})), hx),
                pair.scale(pair.add(
                    etaxx,
                    pair.mul(pair.add(bg["hc"], ({0: two}, {})), etax),
                ), assembly._mp(6)),
                pair.scale(pair.mul(bg["s2"], state["eta"]), -two),
                pair.scale(pair.mul(bg["Ofs"], state["sigma_fs"]),
                           assembly._mp(12)),
            ),
        }
        if tuple(rows) != drivers:
            raise RuntimeError("exact driver row order differs from contract")
        return [rows[name][1].get(e, zero) for name in drivers for e in exponents]

    zero_vector = [zero for _ in range(EXPECTED_COLUMNS)]
    constant = row_values(zero_vector)
    matrix = [[zero for _ in range(EXPECTED_COLUMNS)] for _ in range(EXPECTED_ROWS)]
    for column in range(EXPECTED_COLUMNS):
        probe = list(zero_vector)
        probe[column] = one
        values = row_values(probe)
        for row in range(EXPECTED_ROWS):
            matrix[row][column] = values[row] - constant[row]
    labels = [f"{name}[{e}]" for name in drivers for e in exponents]
    column_names = tuple(f"{name}[{e}]" for name in names for e in exponents)
    comparison = _assembly_difference(matrix, constant, labels, column_names)
    solution = _solve_affine(matrix, constant)
    driver = _metrics(
        matrix, constant, solution, labels, physics.DRIVER_TOL, "pass_driver"
    )
    driver.update({
        "shape": [EXPECTED_ROWS, EXPECTED_COLUMNS],
        "matrix_constant_sha256": _fingerprint(matrix, constant),
        "solution_sha256": _vector_fingerprint(solution),
        "solver": "mpmath.lu_solve_equilibrated",
        "solve_count": 1,
        "holdout_rows_added_to_solve": 0,
        "assembly_difference_from_float64": comparison,
    })
    holdout = assembly._holdout_affine(k_mpc, inputs, standard, solution, support)
    return {
        "precision_dps": PRECISION_DPS,
        "driver": driver,
        "holdout": holdout,
        "exact_driver_solve_count": 1,
        "scope": "HP_DRIVER_AND_HOLDOUT_ASSEMBLY_FROM_EXACTLY_BRIDGED_FLOAT64_UPSTREAM_COEFFICIENTS",
        "upstream_scope_limit": "M1_F0_AND_BACKGROUND_GENERATORS_REMAIN_FLOAT64",
    }


def _solve_m3(mode, k_mpc, inputs, standard, support, deadline):
    global _EXACT_BOUNDARY
    result = _ASSEMBLY_SOLVE_M3(mode, k_mpc, inputs, standard, support, deadline)
    if mode == "BI" and k_mpc == 0.15 and support == AUDIT_SUPPORT:
        with mp.workdps(PRECISION_DPS):
            _EXACT_BOUNDARY = _exact_driver_boundary(k_mpc, inputs, standard, support)
    return result


@contextmanager
def _overlay() -> Iterator[None]:
    global _FLOAT_MATRIX, _FLOAT_CONSTANT, _EXACT_BOUNDARY
    before = (assembly._solve_m3, hp._solve_equilibrated,
              prior.source_hashes, prior.contract_guard)
    _FLOAT_MATRIX = _FLOAT_CONSTANT = _EXACT_BOUNDARY = None
    try:
        assembly._solve_m3 = _solve_m3
        hp._solve_equilibrated = _capture_hp_solver
        prior.source_hashes = source_hashes
        prior.contract_guard = contract_guard
        yield
    finally:
        (assembly._solve_m3, hp._solve_equilibrated,
         prior.source_hashes, prior.contract_guard) = before


def _owners_restored() -> bool:
    return bool(
        assembly._solve_m3 is _ASSEMBLY_SOLVE_M3
        and hp._solve_equilibrated is _HP_SOLVER
        and prior.source_hashes is _PRIOR_SOURCE_HASHES
        and prior.contract_guard is _PRIOR_CONTRACT_GUARD
    )


def _fixture() -> dict[str, bool]:
    with mp.workdps(PRECISION_DPS):
        matrix = [[mp.mpf("2"), mp.mpf("0")],
                  [mp.mpf("0"), mp.mpf("4")]]
        constant = [mp.mpf("-2"), mp.mpf("-8")]
        solution = _solve_affine(matrix, constant)
        metrics = _metrics(
            matrix, constant, solution, ["row0", "row1"],
            physics.DRIVER_TOL, "pass_driver",
        )
    return {
        "exact_driver_solution": solution == [mp.mpf("1"), mp.mpf("2")],
        "exact_driver_residual": bool(metrics["pass_driver"]),
        "ordered_driver_contract": contract.validate_contract(
            contract.AUTHORITATIVE_STATE,
            contract.AUTHORITATIVE_DRIVER,
            contract.AUTHORITATIVE_HOLDOUT,
        ).valid,
        "holdout_nonfit": not set(contract.AUTHORITATIVE_DRIVER)
        & set(contract.AUTHORITATIVE_HOLDOUT),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = prior.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({f"driver_assembly_{key}": value
                                  for key, value in _fixture().items()})
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["driver_assembly_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float,
             result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = prior.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored() or _EXACT_BOUNDARY is None:
        raise RuntimeError("high-precision driver assembly lifecycle incomplete")
    baseline = payload["high_precision_holdout_boundary"]
    baseline_sha = baseline["driver"]["matrix_constant_sha256"]
    captured_sha = _EXACT_BOUNDARY["driver"][
        "assembly_difference_from_float64"
    ]["float64_matrix_constant_sha256"]
    other_gates = bool(
        payload["M1"]["pass"] and payload["common_pass"] and payload["tail_pass"]
        and payload["background_guard"]["pass"] and payload["S_C0_actual_guard"]["pass"]
        and baseline["high_precision_solve_count"] == 1
        and baseline_sha == captured_sha
    )
    driver_pass = bool(_EXACT_BOUNDARY["driver"]["pass_driver"])
    holdout_pass = bool(_EXACT_BOUNDARY["holdout"]["pass_holdout"])
    passed = bool(other_gates and driver_pass and holdout_pass)
    payload["high_precision_driver_assembly_boundary"] = {
        **_EXACT_BOUNDARY,
        "baseline_float_assembled_driver_sha256": baseline_sha,
        "baseline_high_precision_solve_count": baseline["high_precision_solve_count"],
        "total_high_precision_solve_count": baseline["high_precision_solve_count"] + 1,
        "all_other_frozen_gates_pass": other_gates,
        "pass": passed,
    }
    if not driver_pass:
        candidate = "REVIEW_C2_BI_K0p15_EXACT_DRIVER_SYSTEM_UNCLOSED"
    elif not holdout_pass:
        candidate = "REVIEW_C2_BI_K0p15_UPSTREAM_COEFFICIENT_PRECISION_REQUIRED"
    else:
        candidate = "PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"
    payload["candidate_interpretation_not_verdict"] = candidate
    payload["core_pass_high_precision_driver_assembly"] = passed
    payload["score_effect"] = "NONE_PENDING_INTERNAL_AUDIT"
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision driver assembly has no aggregate scope")
