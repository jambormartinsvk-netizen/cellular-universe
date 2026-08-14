"""Independent frozen contract for the conditional S-C0 collective split.

The module contains no solver and no physical coefficient calculation.  It
defines the expected external structure against which the KMPC-032 candidate
is validated.  Deliberately keeping this separate prevents a candidate from
passing by comparing locally constructed lists with themselves.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Mapping


MODES = ("AD", "CDI", "BI", "NID", "NIV")
LOWER_MOMENTS = ("delta", "U", "sigma")
STATE_TO_MOMENT = {
    "delta_fs": "delta",
    "U_fs": "U",
    "sigma_fs": "sigma",
}
EXPECTED_STATE = (
    "h", "eta", "delta_gamma", "delta_fs", "delta_b", "delta_c",
    "U_gamma", "U_fs", "sigma_fs", "U_b", "U_c", "delta_f", "U_f",
)
EXPECTED_DRIVER = (
    "gamma_continuity", "gamma_Euler",
    "fs_continuity", "fs_shear", "fs_Euler",
    "baryon_continuity", "cdm_continuity", "cdm_Euler",
    "tight_coupling", "fuel_continuity", "fuel_Euler",
    "Einstein_trace", "Einstein_traceless",
)
EXPECTED_HOLDOUT = ("Einstein_00", "Einstein_0i")
MODE_SPEC = {
    "AD": {
        "primary": (0, 2), "extended": (0, 4), "leading_j": 2,
        "f0_primary": 6, "f0_extended": 10,
        "m3_primary": 39, "m3_extended": 65,
    },
    "CDI": {
        "primary": (0, 1), "extended": (0, 3), "leading_j": 1,
        "f0_primary": 4, "f0_extended": 8,
        "m3_primary": 26, "m3_extended": 52,
    },
    "BI": {
        "primary": (0, 1), "extended": (0, 3), "leading_j": 1,
        "f0_primary": 4, "f0_extended": 8,
        "m3_primary": 26, "m3_extended": 52,
    },
    "NID": {
        "primary": (0, 3), "extended": (0, 5), "leading_j": 0,
        "f0_primary": 8, "f0_extended": 12,
        "m3_primary": 52, "m3_extended": 78,
    },
    "NIV": {
        "primary": (-1, 2), "extended": (-1, 4), "leading_j": -1,
        "f0_primary": 8, "f0_extended": 12,
        "m3_primary": 52, "m3_extended": 78,
    },
}
EXPECTED_HIERARCHY_SCOPE = "OPERATOR_ONLY_L3_L4_COEFFICIENTS_NOT_IN_SCOPE"


@dataclass(frozen=True)
class CandidateValidation:
    valid: bool
    errors: tuple[str, ...]


def canonical_candidate() -> dict[str, object]:
    """Return a fresh candidate manifest, not an alias to contract objects."""
    return {
        "modes": list(MODES),
        "moments": list(LOWER_MOMENTS),
        "state": list(EXPECTED_STATE),
        "driver": list(EXPECTED_DRIVER),
        "holdout": list(EXPECTED_HOLDOUT),
        "mode_spec": deepcopy(MODE_SPEC),
        "collective_equal": True,
        "direct_Q_s": 0,
        "coefficient_lift_present": True,
        "nid_compensation_weight": "R_fs",
        "niv_compensation_weight": "R_fs",
        "velocity_bridge": "P5_U_REGISTERED_NOT_SCRIPT84_q",
        "hierarchy_scope": EXPECTED_HIERARCHY_SCOPE,
    }


def _ordered_tuple(value: object) -> tuple[object, ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(value)


def validate_candidate(candidate: Mapping[str, object]) -> CandidateValidation:
    """Fail-closed validation used by production and every negative fixture."""
    errors: list[str] = []
    if _ordered_tuple(candidate.get("modes")) != MODES:
        errors.append("ordered mode register differs from S-C0 contract")
    if _ordered_tuple(candidate.get("moments")) != LOWER_MOMENTS:
        errors.append("lower-moment register differs from S-C0 contract")
    if _ordered_tuple(candidate.get("state")) != EXPECTED_STATE:
        errors.append("13-state register differs from frozen R-A contract")
    if _ordered_tuple(candidate.get("driver")) != EXPECTED_DRIVER:
        errors.append("driver register differs from frozen R-A contract")
    if _ordered_tuple(candidate.get("holdout")) != EXPECTED_HOLDOUT:
        errors.append("holdout register differs from frozen R-A contract")

    observed_spec = candidate.get("mode_spec")
    if not isinstance(observed_spec, Mapping):
        errors.append("mode support specification is missing")
    else:
        for mode in MODES:
            observed = observed_spec.get(mode)
            if not isinstance(observed, Mapping):
                errors.append(f"mode support missing: {mode}")
                continue
            expected = MODE_SPEC[mode]
            for key, value in expected.items():
                got = observed.get(key)
                if isinstance(value, tuple):
                    got = _ordered_tuple(got)
                if got != value:
                    errors.append(f"{mode} support/count mismatch for {key}")

    if candidate.get("collective_equal") is not True:
        errors.append("S-C0 requires Y_nu=Y_s=Y_fs")
    if candidate.get("direct_Q_s") != 0:
        errors.append("S-C0 requires exactly zero direct steam source")
    if candidate.get("coefficient_lift_present") is not True:
        errors.append("weight-only identity is not a coefficient passport")
    if candidate.get("nid_compensation_weight") != "R_fs":
        errors.append("NID compensation must use the combined R_fs weight")
    if candidate.get("niv_compensation_weight") != "R_fs":
        errors.append("NIV compensation must use the combined R_fs weight")
    if candidate.get("velocity_bridge") != "P5_U_REGISTERED_NOT_SCRIPT84_q":
        errors.append("P5 U must not be replaced by the script-84 q variable")
    if candidate.get("hierarchy_scope") != EXPECTED_HIERARCHY_SCOPE:
        errors.append("higher-multipole coefficient scope is overstated")

    return CandidateValidation(valid=not errors, errors=tuple(errors))


def negative_fixture_candidates() -> dict[str, dict[str, object]]:
    """Ten malformed candidates; all travel through validate_candidate()."""
    fixtures: dict[str, dict[str, object]] = {}

    item = canonical_candidate()
    item["modes"] = list(MODES[:-1])
    fixtures["missing_mode"] = item

    item = canonical_candidate()
    item["mode_spec"]["NID"]["primary"] = (0, 2)
    item["mode_spec"]["NID"]["extended"] = (0, 4)
    fixtures["universal_AD_J4_support_inserted_into_NID"] = item

    item = canonical_candidate()
    item["moments"] = ["delta", "U"]
    fixtures["missing_sigma"] = item

    item = canonical_candidate()
    item["driver"] = list(EXPECTED_DRIVER) + ["Einstein_00"]
    fixtures["holdout_inserted_into_driver"] = item

    item = canonical_candidate()
    item["collective_equal"] = False
    fixtures["steam_not_equal_to_neutrino"] = item

    item = canonical_candidate()
    item["nid_compensation_weight"] = "R_nu"
    fixtures["NID_uses_R_nu"] = item

    item = canonical_candidate()
    item["niv_compensation_weight"] = "R_nu"
    fixtures["NIV_uses_R_nu"] = item

    item = canonical_candidate()
    item["direct_Q_s"] = 1
    fixtures["nonzero_direct_Q_s"] = item

    item = canonical_candidate()
    item["coefficient_lift_present"] = False
    fixtures["weight_only_tautology"] = item

    item = canonical_candidate()
    item["velocity_bridge"] = "SCRIPT84_q_COPIED_DIRECTLY"
    fixtures["script84_q_used_as_P5_U"] = item

    return fixtures

