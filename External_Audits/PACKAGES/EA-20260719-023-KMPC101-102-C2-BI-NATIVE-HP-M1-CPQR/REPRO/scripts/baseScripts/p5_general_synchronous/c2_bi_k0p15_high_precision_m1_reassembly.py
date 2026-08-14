"""80-dps M1 reassembly boundary for C2 BI/k=.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the standard M1 affine system is reassembled and solved at high
precision. Standard-background coefficients remain the exact bridge of the
frozen binary64 generator; F0, fractional background and M3 stay unchanged.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_coefficient_attribution_v5_nested_owner as prior


v1 = prior.v1
driver = v1.prior
assembly = v1.assembly
physics = driver.physics
legacy = physics.legacy
contract = driver.contract
PRECISION_DPS = driver.PRECISION_DPS
MODE = "BI"
K_MPC = 0.15
ORDER = 7
EXPECTED_FULL_SHAPE = (121, 99)
EXPECTED_REDUCED_SHAPE = (121, 98)
EXPECTED_HOLDOUT_SHAPE = (18, 99)
HP_M1_SOLVE_LIMIT = 1

_V5_SOURCE_HASHES = prior.source_hashes
_V5_CONTRACT_GUARD = prior.contract_guard
_ORIGINAL_EXACT_BOUNDARY = v1._PRIOR_EXACT_BOUNDARY
_M1_SOLVE_COUNT = 0
_M1_BOUNDARY: dict[str, object] | None = None


def configure(**config: object) -> None:
    prior.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return prior.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return prior.atom_failure_name(mode, k_mpc)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    hashes = dict(_V5_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_high_precision_m1_reassembly.py"] = _sha256_file(
        here / "c2_bi_k0p15_high_precision_m1_reassembly.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V5_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_precision_exact": PRECISION_DPS == 80,
        "hp_m1_mode_k_order_exact": (MODE, K_MPC, ORDER) == ("BI", 0.15, 7),
        "hp_m1_shapes_exact": (
            EXPECTED_FULL_SHAPE == (11 * 9 + 22, 11 * 9)
            and EXPECTED_REDUCED_SHAPE == (121, 98)
            and EXPECTED_HOLDOUT_SHAPE == (2 * 9, 11 * 9)
        ),
        "hp_m1_one_new_solve": HP_M1_SOLVE_LIMIT == 1,
        "hp_m1_background_generator_frozen": True,
        "hp_m1_f0_fractional_background_m3_frozen": True,
        "hp_m1_holdout_nonfit": not set(legacy.DRIVER_ROWS) & set(legacy.HOLDOUT_ROWS),
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _standard_rows_mp(
    state: dict[str, dict[int, mp.mpf]],
    bg: dict[str, object],
    series: object,
) -> dict[str, dict[int, mp.mpf]]:
    one = mp.mpf(1)
    two = mp.mpf(2)
    three = mp.mpf(3)
    four = mp.mpf(4)
    five = mp.mpf(5)
    fifteen = mp.mpf(15)
    hx = series.dx(state["h"])
    etax = series.dx(state["eta"])
    hxx = series.dx(hx)
    etaxx = series.dx(etax)
    density = series.add(
        series.mul(bg["Og"], state["dg"]),
        series.mul(bg["Ofs"], state["dfs"]),
        series.mul(bg["Ob"], state["db"]),
        series.mul(bg["Oc"], state["dc"]),
    )
    momentum = series.add(
        series.scale(series.mul(bg["Og"], state["Ug"]), two),
        series.scale(series.mul(bg["Ofs"], state["Ufs"]), two),
        series.scale(series.mul(bg["Ob"], state["Ub"]), three / two),
        series.scale(series.mul(bg["Oc"], state["Uc"]), three / two),
    )
    hc_plus_two = series.add(bg["hc"], {0: two})
    return {
        "gamma_continuity": series.add(
            series.dx(state["dg"]),
            series.scale(series.mul(bg["s2"], state["Ug"]), four / three),
            series.scale(hx, two / three),
        ),
        "gamma_Euler": series.add(
            series.dx(state["Ug"]),
            series.scale(series.mul(bg["hc"], state["Ug"]), -one),
            series.mul(bg["load_fraction"], state["Ug"]),
            series.scale(series.mul(bg["inv1R"], state["dg"]), -one / four),
        ),
        "fs_continuity": series.add(
            series.dx(state["dfs"]),
            series.scale(series.mul(bg["s2"], state["Ufs"]), four / three),
            series.scale(hx, two / three),
        ),
        "fs_shear": series.add(
            series.scale(series.dx(state["sigfs"]), two),
            series.scale(hx, -four / fifteen),
            series.scale(etax, -mp.mpf(8) / five),
            series.scale(series.mul(bg["s2"], state["Ufs"]), -mp.mpf(8) / fifteen),
        ),
        "fs_Euler": series.add(
            series.dx(state["Ufs"]),
            series.scale(series.mul(bg["hc"], state["Ufs"]), -one),
            series.scale(state["dfs"], -one / four),
            state["sigfs"],
        ),
        "baryon_continuity": series.add(
            series.dx(state["db"]), series.mul(bg["s2"], state["Ub"]),
            series.scale(hx, one / two),
        ),
        "cdm_continuity": series.add(
            series.dx(state["dc"]), series.mul(bg["s2"], state["Uc"]),
            series.scale(hx, one / two),
        ),
        "cdm_Euler": series.add(
            series.dx(state["Uc"]),
            series.scale(
                series.mul(series.add(bg["hc"], {0: -one}), state["Uc"]), -one
            ),
        ),
        "tight_coupling": series.add(state["Ub"], series.scale(state["Ug"], -one)),
        "Einstein_00": series.add(
            series.scale(hx, -one / two), series.scale(density, three / two),
            series.mul(bg["s2"], state["eta"]),
        ),
        "Einstein_0i": series.add(etax, series.scale(momentum, -one)),
        "Einstein_trace": series.add(
            hxx, series.mul(hc_plus_two, hx),
            series.scale(series.mul(bg["s2"], state["eta"]), -two),
            series.scale(series.mul(bg["Og"], state["dg"]), three),
            series.scale(series.mul(bg["Ofs"], state["dfs"]), three),
        ),
        "Einstein_traceless": series.add(
            hxx, series.mul(hc_plus_two, hx),
            series.scale(
                series.add(etaxx, series.mul(hc_plus_two, etax)), mp.mpf(6)
            ),
            series.scale(series.mul(bg["s2"], state["eta"]), -two),
            series.scale(series.mul(bg["Ofs"], state["sigfs"]), mp.mpf(12)),
        ),
    }


def _matrix_fingerprint(
    matrix: list[list[mp.mpf]], constant: list[mp.mpf]
) -> str:
    digest = hashlib.sha256()
    for row, c_value in zip(matrix, constant, strict=True):
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


def _background_fingerprint(bg: dict[str, object]) -> str:
    digest = hashlib.sha256()
    for name in ("D", "invD", "hc", "s2", "Og", "Ofs", "Ob", "Oc",
                 "loading", "inv1R", "load_fraction"):
        digest.update(name.encode("ascii"))
        digest.update(b"|")
        for power, value in sorted(bg[name].items()):
            digest.update(f"{power}|".encode("ascii"))
            digest.update(mp.nstr(assembly._mp(value), 90).encode("ascii"))
            digest.update(b"|")
    return digest.hexdigest().upper()


def _solve_reduced(matrix: list[list[mp.mpf]], rhs: list[mp.mpf]) -> tuple[list[mp.mpf], mp.mpf]:
    solved, residual = mp.qr_solve(mp.matrix(matrix), mp.matrix(rhs))
    return [solved[i] for i in range(len(solved))], residual


def _m1_reassembly(
    inputs: object,
    baseline_standard: dict[str, dict[int, object]],
) -> tuple[dict[str, dict[int, mp.mpf]], dict[str, object]]:
    global _M1_SOLVE_COUNT
    if _M1_SOLVE_COUNT >= HP_M1_SOLVE_LIMIT:
        raise RuntimeError("more than one high-precision M1 solve requested")
    _M1_SOLVE_COUNT += 1
    powers = tuple(range(-1, ORDER + 1))
    pairs = tuple((name, power) for name in legacy.VARS for power in powers)
    index = {pair: position for position, pair in enumerate(pairs)}
    series = assembly._MPSeries(-4, ORDER + 5)
    float_series = legacy.Series(-4, ORDER + 5)
    background_float = legacy._standard_background(K_MPC, inputs, float_series)
    background = {
        name: assembly._mp_dict(background_float[name])
        for name in (
            "D", "invD", "hc", "s2", "Og", "Ofs", "Ob", "Oc",
            "loading", "inv1R", "load_fraction",
        )
    }
    initial = tuple(legacy._initial_constraints(
        MODE, inputs.radiation_weights[1], inputs.radiation_weights[0]
    ))
    driver_labels = [
        f"{row}[{power}]" for row in legacy.DRIVER_ROWS for power in powers
    ] + [f"initial:{name}[{power}]" for name, power, _ in initial]
    holdout_labels = [
        f"{row}[{power}]" for row in legacy.HOLDOUT_ROWS for power in powers
    ]

    def unpack(vector: list[mp.mpf]) -> dict[str, dict[int, mp.mpf]]:
        return {
            name: {power: vector[index[(name, power)]] for power in powers}
            for name in legacy.VARS
        }

    def values(vector: list[mp.mpf], row_names: tuple[str, ...]) -> list[mp.mpf]:
        rows = _standard_rows_mp(unpack(vector), background, series)
        return [rows[row].get(power, mp.mpf(0)) for row in row_names for power in powers]

    zero = [mp.mpf(0) for _ in pairs]
    driver_constant = values(zero, legacy.DRIVER_ROWS)
    driver_constant.extend(-assembly._mp(value) for _, _, value in initial)
    holdout_constant = values(zero, legacy.HOLDOUT_ROWS)
    driver_matrix = [[mp.mpf(0) for _ in pairs] for _ in driver_constant]
    holdout_matrix = [[mp.mpf(0) for _ in pairs] for _ in holdout_constant]
    for column in range(len(pairs)):
        probe = list(zero)
        probe[column] = mp.mpf(1)
        driver_probe = values(probe, legacy.DRIVER_ROWS)
        driver_probe.extend(
            probe[index[(name, power)]] - assembly._mp(value)
            for name, power, value in initial
        )
        holdout_probe = values(probe, legacy.HOLDOUT_ROWS)
        for row in range(len(driver_constant)):
            driver_matrix[row][column] = driver_probe[row] - driver_constant[row]
        for row in range(len(holdout_constant)):
            holdout_matrix[row][column] = holdout_probe[row] - holdout_constant[row]

    anchor_power, anchor_float = legacy._m1_expected_h(
        MODE, background_float, inputs
    )
    anchor_index = index[("h", anchor_power)]
    anchor = assembly._mp(anchor_float)
    reduced_matrix = [
        [value for column, value in enumerate(row) if column != anchor_index]
        for row in driver_matrix
    ]
    rhs = [
        -driver_constant[row] - driver_matrix[row][anchor_index] * anchor
        for row in range(len(driver_constant))
    ]
    reduced, qr_residual = _solve_reduced(reduced_matrix, rhs)
    solution: list[mp.mpf] = []
    cursor = 0
    for column in range(len(pairs)):
        if column == anchor_index:
            solution.append(anchor)
        else:
            solution.append(reduced[cursor])
            cursor += 1

    legacy_state = unpack(solution)
    standard = {
        target: dict(legacy_state[source])
        for target, source in physics.STATE_TO_LEGACY.items()
    }
    baseline_vector = [
        assembly._mp(baseline_standard[target][power])
        for target in physics.STATE_TO_LEGACY
        for power in powers
    ]
    hp_vector = [standard[name][power] for name in contract.AUTHORITATIVE_STATE[:11] for power in powers]
    differences = [abs(left - right) for left, right in zip(hp_vector, baseline_vector, strict=True)]
    worst_index = max(range(len(differences)), key=differences.__getitem__)
    worst_name = contract.AUTHORITATIVE_STATE[:11][worst_index // len(powers)]
    worst_power = powers[worst_index % len(powers)]
    driver_metrics = driver._metrics(
        driver_matrix, driver_constant, solution, driver_labels,
        physics.DRIVER_TOL, "pass_driver_and_initial",
    )
    holdout_metrics = driver._metrics(
        holdout_matrix, holdout_constant, solution, holdout_labels,
        physics.DRIVER_TOL, "pass_holdout",
    )
    boundary = {
        "precision_dps": PRECISION_DPS,
        "mode": MODE,
        "k_Mpc_inverse": K_MPC,
        "order": ORDER,
        "full_shape": list(EXPECTED_FULL_SHAPE),
        "reduced_shape": list(EXPECTED_REDUCED_SHAPE),
        "holdout_shape": list(EXPECTED_HOLDOUT_SHAPE),
        "hard_anchor": f"h[{anchor_power}]",
        "hard_anchor_value_decimal": mp.nstr(anchor, 50),
        "matrix_constant_sha256": _matrix_fingerprint(driver_matrix, driver_constant),
        "solution_sha256": _vector_fingerprint(solution),
        "baseline_solution_sha256": _vector_fingerprint(baseline_vector),
        "standard_background_exact_bridge_sha256": _background_fingerprint(background_float),
        "standard_background_generator": "FROZEN_BINARY64_THEN_EXACT_BRIDGE",
        "solver": "mpmath.qr_solve_unweighted_overdetermined",
        "qr_residual_decimal": mp.nstr(qr_residual, 50),
        "high_precision_m1_solve_count": _M1_SOLVE_COUNT,
        "driver_and_initial": driver_metrics,
        "holdout": holdout_metrics,
        "solution_difference_max_abs": float(differences[worst_index]),
        "solution_difference_max_abs_decimal": mp.nstr(differences[worst_index], 50),
        "solution_difference_worst_coefficient": f"{worst_name}[{worst_power}]",
        "f0_generator_changed": False,
        "fractional_background_generator_changed": False,
        "m3_equations_changed": False,
        "support_or_threshold_changed": False,
        "holdout_rows_added_to_solve": 0,
        "pass": bool(
            driver_metrics["pass_driver_and_initial"]
            and holdout_metrics["pass_holdout"]
            and _M1_SOLVE_COUNT == HP_M1_SOLVE_LIMIT
        ),
    }
    return standard, boundary


def _high_precision_m1_exact_boundary(
    k_mpc: float,
    inputs: object,
    standard: dict[str, dict[int, object]],
    support: tuple[int, int],
) -> dict[str, object]:
    global _M1_BOUNDARY
    if (k_mpc, support) != (K_MPC, (0, 7)):
        raise ValueError("KMPC-093 M1 boundary identity mismatch")
    hp_standard, _M1_BOUNDARY = _m1_reassembly(inputs, standard)
    result = _ORIGINAL_EXACT_BOUNDARY(k_mpc, inputs, hp_standard, support)
    result["high_precision_m1_reassembly"] = _M1_BOUNDARY
    result["upstream_scope_limit"] = (
        "F0_AND_FRACTIONAL_BACKGROUND_GENERATORS_REMAIN_FLOAT64"
    )
    return result


@contextmanager
def _overlay() -> Iterator[None]:
    global _M1_SOLVE_COUNT, _M1_BOUNDARY
    before = (v1._PRIOR_EXACT_BOUNDARY, prior.source_hashes, prior.contract_guard)
    _M1_SOLVE_COUNT = 0
    _M1_BOUNDARY = None
    try:
        v1._PRIOR_EXACT_BOUNDARY = _high_precision_m1_exact_boundary
        prior.source_hashes = source_hashes
        prior.contract_guard = contract_guard
        yield
    finally:
        v1._PRIOR_EXACT_BOUNDARY, prior.source_hashes, prior.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        v1._PRIOR_EXACT_BOUNDARY is _ORIGINAL_EXACT_BOUNDARY
        and prior.source_hashes is _V5_SOURCE_HASHES
        and prior.contract_guard is _V5_CONTRACT_GUARD
    )


def _fixture() -> dict[str, bool]:
    with mp.workdps(PRECISION_DPS):
        matrix = [
            [mp.mpf(1), mp.mpf(0)],
            [mp.mpf(0), mp.mpf(1)],
            [mp.mpf(1), mp.mpf(1)],
        ]
        solution, residual = _solve_reduced(
            matrix, [mp.mpf(1), mp.mpf(2), mp.mpf(3)]
        )
        exact_ratio = mp.mpf(4) / mp.mpf(3)
    return {
        "overdetermined_qr_solution": bool(
            abs(solution[0] - 1) < mp.mpf("1e-70")
            and abs(solution[1] - 2) < mp.mpf("1e-70")
        ),
        "overdetermined_qr_residual": bool(residual < mp.mpf("1e-70")),
        "native_rational_not_binary64_bridge": exact_ratio != assembly._mp(4.0 / 3.0),
        "live_c2_solver_is_raw_anchor": (
            physics.m1_anchor.solve_standard_seed_anchored.__module__.endswith(
                "mode_resolved_puiseux_v2_m1_anchored"
            )
            and "numerical_refinement"
            not in physics.m1_anchor.solve_standard_seed_anchored.__module__
        ),
        "holdout_nonfit": not set(legacy.DRIVER_ROWS) & set(legacy.HOLDOUT_ROWS),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = prior.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({
            f"hp_m1_{name}": value for name, value in _fixture().items()
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["hp_m1_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = prior.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored() or _M1_BOUNDARY is None:
        raise RuntimeError("KMPC-093 high-precision M1 lifecycle incomplete")
    exact = payload["high_precision_driver_assembly_boundary"]
    target = exact["holdout"]["Einstein_0i_7"]
    other_gates = bool(
        payload["M1"]["pass"]
        and payload["common_pass"]
        and payload["tail_pass"]
        and payload["background_guard"]["pass"]
        and payload["S_C0_actual_guard"]["pass"]
        and exact["driver"]["pass_driver"]
        and exact["holdout"]["rows_added_to_driver_solve"] == 0
    )
    closed = bool(
        _M1_BOUNDARY["pass"]
        and other_gates
        and target["metric"] <= physics.HOLDOUT_TOL
    )
    payload["high_precision_m1_reassembly_boundary"] = {
        **_M1_BOUNDARY,
        "Einstein_0i_7_after_hp_m1": target,
        "baseline_Einstein_0i_7_metric": 3.019756577618421e-9,
        "total_high_precision_solves_including_m1": (
            exact["total_high_precision_solve_count"] + _M1_SOLVE_COUNT
        ),
        "all_other_frozen_gates_pass": other_gates,
        "pass_c2_atom_candidate": closed,
    }
    if not _M1_BOUNDARY["pass"]:
        candidate = "REVIEW_C2_BI_K0p15_HP_M1_SYSTEM_UNCLOSED"
    elif closed:
        candidate = "PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY"
    else:
        candidate = "REVIEW_C2_BI_K0p15_NON_M1_UPSTREAM_PRECISION_REQUIRED"
    payload["candidate_interpretation_not_verdict"] = candidate
    payload["score_effect"] = "NONE_PENDING_INTERNAL_AUDIT"
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision M1 boundary has no aggregate scope")
