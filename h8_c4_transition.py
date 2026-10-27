"""Exact C4 and pressure diagnostics for a *candidate* H8 transition profile.

The Case 006 text fixes C4 averaging and the radial toroidal pressure
derivative, but does not select a unique cutoff, pressure trace, or complete
four-patch field.  Functions here therefore retain the choices as explicit
inputs, and the smooth annular cutoff is an illustrative candidate only.
"""

from __future__ import annotations

from collections.abc import Sequence

import sympy as sp


def flat_step(s: sp.Expr) -> sp.Expr:
    """The standard C-infinity flat step, equal to 0/1 outside (0,1)."""
    t = sp.sympify(s)
    return sp.Piecewise(
        (sp.S.Zero, t <= 0),
        (sp.S.One, t >= 1),
        (sp.exp(-1 / t) / (sp.exp(-1 / t) + sp.exp(-1 / (1 - t))), True),
    )


def flat_annular_cutoff(
    radius: sp.Expr, inner: sp.Expr, plateau_start: sp.Expr,
    plateau_end: sp.Expr, outer: sp.Expr,
) -> sp.Expr:
    """Explicit smooth annular candidate, not the unfixed Case 006 cutoff."""
    a, b, c, d = (sp.sympify(k) for k in
                  (inner, plateau_start, plateau_end, outer))
    if not all(k.is_number for k in (a, b, c, d)):
        raise ValueError("Annular radii must be exact numeric endpoints")
    if not (bool(a < b) and bool(b <= c) and bool(c < d)):
        raise ValueError("Annular radii must satisfy inner < start <= end < outer")
    t = sp.sympify(radius)
    return flat_step((t - a) / (b - a)) * flat_step((d - t) / (d - c))


def _rotation(j: int) -> sp.Matrix:
    return sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]]) ** (j % 4)


def _rotate_field(field: Sequence[sp.Expr], j: int,
                  coords: Sequence[sp.Symbol]) -> tuple[sp.Expr, ...]:
    """Active Cartesian push-forward Q^j F(Q^{-j} x)."""
    q = _rotation(j)
    inv_coords = q.T * sp.Matrix(coords)
    subs = dict(zip(coords, inv_coords))
    return tuple(sp.expand(c) for c in
                 q * sp.Matrix([sp.sympify(f).subs(subs, simultaneous=True)
                                for f in field]))


def _curl(field: Sequence[sp.Expr],
          coords: Sequence[sp.Symbol]) -> tuple[sp.Expr, ...]:
    x, y, z = coords
    ax, ay, az = field
    return (sp.diff(az, y) - sp.diff(ay, z),
            sp.diff(ax, z) - sp.diff(az, x),
            sp.diff(ay, x) - sp.diff(ax, y))


def _ensure_c4_cutoff(cutoff: sp.Expr, coords: Sequence[sp.Symbol]) -> None:
    q = _rotation(1)
    inv_coords = q.T * sp.Matrix(coords)
    rotated = sp.sympify(cutoff).subs(dict(zip(coords, inv_coords)),
                                       simultaneous=True)
    if sp.simplify(rotated - sp.sympify(cutoff)) != 0:
        raise ValueError("A C4-invariant cutoff is required")


def rotated_local_fields(potential: Sequence[sp.Expr], cutoff: sp.Expr,
                         coords: Sequence[sp.Symbol]) -> tuple[tuple[sp.Expr, ...], ...]:
    """The four *unnormalized* rotated curls used in the source average."""
    if len(potential) != 3 or len(coords) != 3:
        raise ValueError("Expected three-dimensional potential and coordinates")
    _ensure_c4_cutoff(cutoff, coords)
    localized = tuple(sp.sympify(cutoff) * sp.sympify(a) for a in potential)
    basic = _curl(localized, coords)
    return tuple(_rotate_field(basic, j, coords) for j in range(4))


def localized_c4_velocity(potential: Sequence[sp.Expr], cutoff: sp.Expr,
                          coords: Sequence[sp.Symbol]) -> tuple[sp.Expr, ...]:
    """Curl of the normalized fourfold average of the localized potential."""
    if len(potential) != 3 or len(coords) != 3:
        raise ValueError("Expected three-dimensional potential and coordinates")
    _ensure_c4_cutoff(cutoff, coords)
    localized = tuple(sp.sympify(cutoff) * sp.sympify(a) for a in potential)
    averaged = tuple(sp.simplify(sum(_rotate_field(localized, j, coords)[i]
                                     for j in range(4)) / 4) for i in range(3))
    return tuple(sp.simplify(v) for v in _curl(averaged, coords))


def c4_transport_parts(fields: Sequence[Sequence[sp.Expr]],
                       coords: Sequence[sp.Symbol]) -> tuple[tuple[sp.Expr, ...], ...]:
    """Diagonal, ordered cross, full advective flux in a normalized C4 average.

    Every term is divided by 16.  The 12 ordered cross terms are retained.
    """
    if len(fields) != 4 or len(coords) != 3 or any(len(v) != 3 for v in fields):
        raise ValueError("Four three-dimensional C4 fields are required")

    def advect(v: Sequence[sp.Expr], w: Sequence[sp.Expr]) -> tuple[sp.Expr, ...]:
        return tuple(sum(v[i] * sp.diff(w[k], coords[i]) for i in range(3))
                     for k in range(3))

    diagonal = tuple(sp.simplify(sum(advect(fields[j], fields[j])[i]
                                       for j in range(4)) / 16) for i in range(3))
    cross = tuple(sp.simplify(sum(advect(fields[j], fields[k])[i]
                                    for j in range(4) for k in range(4) if j != k)
                              / 16) for i in range(3))
    complete = tuple(sp.simplify(diagonal[i] + cross[i]) for i in range(3))
    return diagonal, cross, complete


def c4_quadratic_stress_parts(fields: Sequence[Sequence[sp.Expr]]) -> tuple[sp.Matrix, ...]:
    """The exact 1/16 diagonal, ordered-overlap and full Reynolds tensors."""
    if len(fields) != 4 or any(len(v) != 3 for v in fields):
        raise ValueError("Four three-dimensional C4 fields are required")
    diagonal = sp.zeros(3)
    cross = sp.zeros(3)
    for j in range(4):
        for k in range(4):
            contribution = sp.Matrix(fields[j]) * sp.Matrix(fields[k]).T / 16
            if j == k:
                diagonal += contribution
            else:
                cross += contribution
    return (diagonal.applyfunc(sp.simplify), cross.applyfunc(sp.simplify),
            (diagonal + cross).applyfunc(sp.simplify))


def normalized_toroidal_pressure(radius: sp.Symbol, axial: sp.Symbol,
                                  inner: sp.Expr, core_toroidal: sp.Expr,
                                  transition_toroidal: sp.Expr) -> sp.Expr:
    r"""A candidate gauge p_T(inner,z)=0 with ∂_r p_T=(2uθT+T²)/r.

    Case 006 specifies the radial derivative but not its z-dependent trace.
    This routine fixes the trace as a modeling choice, not as source fact.
    """
    dummy = sp.Dummy("s", positive=True)
    u = sp.sympify(core_toroidal).subs(radius, dummy)
    t = sp.sympify(transition_toroidal).subs(radius, dummy)
    integrand = (2 * u * t + t * t) / dummy
    return sp.simplify(sp.integrate(integrand, (dummy, sp.sympify(inner), radius)))


def axial_pressure_jump(pressure: sp.Expr, axial: sp.Symbol,
                         lower: sp.Expr, upper: sp.Expr) -> sp.Expr:
    """Exact difference p(r,z_upper)-p(r,z_lower), with no gauge deletion."""
    p = sp.sympify(pressure)
    return sp.simplify(p.subs(axial, upper) - p.subs(axial, lower))
