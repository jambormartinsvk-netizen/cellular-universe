"""Authoritative exact ordered contract for P5.3g7-M3-FULL/R-A."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


AUTHORITATIVE_STATE = (
    "h", "eta", "delta_gamma", "delta_fs", "delta_b", "delta_c",
    "U_gamma", "U_fs", "sigma_fs", "U_b", "U_c", "delta_f", "U_f",
)
AUTHORITATIVE_DRIVER = (
    "gamma_continuity", "gamma_Euler",
    "fs_continuity", "fs_shear", "fs_Euler",
    "baryon_continuity",
    "cdm_continuity", "cdm_Euler",
    "tight_coupling",
    "fuel_continuity", "fuel_Euler",
    "Einstein_trace", "Einstein_traceless",
)
AUTHORITATIVE_HOLDOUT = ("Einstein_00", "Einstein_0i")


@dataclass(frozen=True)
class ContractValidation:
    valid: bool
    errors: tuple[str, ...]


def _tuple(values: Iterable[str]) -> tuple[str, ...]:
    return tuple(values)


def validate_contract(
    state: Iterable[str], driver: Iterable[str], holdout: Iterable[str]
) -> ContractValidation:
    state_tuple = _tuple(state)
    driver_tuple = _tuple(driver)
    holdout_tuple = _tuple(holdout)
    errors: list[str] = []

    if state_tuple != AUTHORITATIVE_STATE:
        errors.append("state ordered tuple differs from authoritative contract")
    if driver_tuple != AUTHORITATIVE_DRIVER:
        errors.append("driver ordered tuple differs from authoritative contract")
    if holdout_tuple != AUTHORITATIVE_HOLDOUT:
        errors.append("holdout ordered tuple differs from authoritative contract")
    if len(set(state_tuple)) != len(state_tuple):
        errors.append("state tuple contains a duplicate")
    if len(set(driver_tuple)) != len(driver_tuple):
        errors.append("driver tuple contains a duplicate")
    if len(set(holdout_tuple)) != len(holdout_tuple):
        errors.append("holdout tuple contains a duplicate")
    if set(driver_tuple) & set(holdout_tuple):
        errors.append("driver and holdout sets overlap")

    return ContractValidation(valid=not errors, errors=tuple(errors))

