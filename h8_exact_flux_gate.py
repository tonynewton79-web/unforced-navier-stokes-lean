"""Exact radial H8 flux bookkeeping and rational-point one-sided cone gate.

The fixed channel names are an *audit partition*, not a claim that the
corresponding Case 006 profiles have been frozen. Every contribution must
be supplied, including explicitly zero terms, by the caller. A rational
pointwise verdict never certifies a continuum weighted estimate or a PDE
inverse. Nonrational values require a separate certified enclosure.
"""

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping

import sympy as sp

from h8_positive_cone import positive_support
from h8_rotating_frame import dual_covector
from h8_sharp_dual import sharp_support
from h8_positive_cone import GAMMA


SHEAR_CHANNELS = (
    "core_transition",
    "core_shaper",
    "poloidal_pairing",
    "toroidal_pairing",
    "viscous",
    "four_patch_overlap",
    "structured_remainder",
    "reference_center",
)

BOUNDARY_CHANNELS = (
    "core_pressure",
    "toroidal_pressure",
    "transition_pressure",
    "axial_tensor_jump",
    "four_patch_overlap",
    "other_boundary",
)


@dataclass(frozen=True)
class FluxLedger:
    radial_symbol: sp.Symbol
    inner_radius: sp.Expr
    shear: sp.Expr
    shear_at_a: sp.Expr
    axial_jump: sp.Expr
    boundary_primitive: sp.Expr
    J: sp.Expr
    source_axial_marginal: sp.Expr


@dataclass(frozen=True)
class PointGate:
    radius: Fraction
    shear: Fraction
    J: Fraction
    boundary_primitive: Fraction
    lower: Fraction
    upper: Fraction
    admissible_at_point: bool
    absolute_lower: Fraction
    absolute_upper: Fraction
    absolute_admissible_at_point: bool


def _validate_partition(data: Mapping[str, object], names: tuple[str, ...]):
    if not isinstance(data, Mapping):
        raise ValueError("each source partition must be a mapping")
    missing = set(names) - set(data)
    extra = set(data) - set(names)
    if missing or extra:
        raise ValueError(f"incomplete/ambiguous channel partition: "
                         f"missing {sorted(missing)}, extra {sorted(extra)}")
    if any(value is None for value in data.values()):
        raise ValueError("unknown source functions must not be replaced by None")


def assemble_flux(radial_symbol, inner_radius, shear_terms, boundary_terms):
    """Assemble S, q_s and J=(rS-aS(a)+int_a^r s*q_s ds)/r.

    `source_axial_marginal` is the source dictated by the exact integrated
    cylindrical-divergence law, not an independently validated NSE source.
    """
    _validate_partition(shear_terms, SHEAR_CHANNELS)
    _validate_partition(boundary_terms, BOUNDARY_CHANNELS)
    r = radial_symbol
    if not isinstance(r, sp.Symbol):
        raise ValueError("the radial coordinate must be a SymPy symbol")
    a = sp.sympify(inner_radius)
    S = sp.simplify(sum((sp.sympify(v) for v in shear_terms.values()), sp.S.Zero))
    q = sp.simplify(sum((sp.sympify(v) for v in boundary_terms.values()), sp.S.Zero))
    S_a = sp.simplify(S.subs(r, a))
    s = sp.Dummy("s", positive=True)
    primitive = sp.simplify(sp.integrate(s*q.subs(r, s), (s, a, r))/r)
    J = sp.simplify(S - a*S_a/r + primitive)
    f = sp.simplify(sp.diff(r*S, r)/r + q)
    return FluxLedger(r, a, S, S_a, q, primitive, J, f)


def _exact_fraction(expr, r, value):
    e = sp.simplify(sp.sympify(expr).subs(r, value))
    if e.is_Rational is not True or e.is_finite is not True:
        raise ValueError(f"rational point certificate unavailable for {e}")
    return Fraction(int(e.p), int(e.q))


def pointwise_cone_gate(ledger: FluxLedger, radial_symbol, radius,
                        axial_integrated_density, frame):
    """Check the sharp rotating-frame *shear* support at one rational r.

    The input weight is int rho(r,z) dz. This reduction assumes E does
    not vary in z (or theta) on that integration slice. It does not test
    source authenticity, derivative estimates or every point in a shell.
    """
    if radial_symbol != ledger.radial_symbol:
        raise ValueError("radial symbols differ")
    r = radial_symbol
    x = sp.Rational(radius)
    if x <= ledger.inner_radius:
        raise ValueError("the test radius must lie beyond the inner edge")
    mass = _exact_fraction(axial_integrated_density, r, x)
    if mass < 0:
        raise ValueError("the density must be nonnegative")
    if len(frame) != 3 or any(len(row) != 3 for row in frame):
        raise ValueError("a 3-by-3 orthogonal frame is required")
    E = tuple(tuple(_exact_fraction(entry, r, x) for entry in row)
              for row in frame)
    if any(sum((E[i][k]*E[j][k] for k in range(3)), Fraction(0))
           != (1 if i == j else 0)
           for i in range(3) for j in range(3)):
        raise ValueError("the frame must be exactly orthogonal")
    G = ((0, 0, 1), (0, 0, 0), (0, 0, 0))
    cov = dual_covector(E, G)
    upper = positive_support(*cov, mass)
    lower = -positive_support(*(-v for v in cov), mass)
    original_cap = sharp_support(*cov, GAMMA*mass)
    shear = _exact_fraction(ledger.shear, r, x)
    J = _exact_fraction(ledger.J, r, x)
    primitive = _exact_fraction(ledger.boundary_primitive, r, x)
    return PointGate(Fraction(x), shear, J, primitive, lower, upper,
                     lower <= shear <= upper, -original_cap, original_cap,
                     -original_cap <= shear <= original_cap)
