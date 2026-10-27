"""Exact cylindrical-frame source identity for the four-field H8 tensor.

This is an algebraic Cartesian-to-cylindrical calculation for arbitrary
smooth functions A, B, C, D and p on r>0. It does not instantiate the
authentic Case 006 cutoff, shapers, source, pressure, or cone density.
For the existing Lean tensor product-rule bridge see
UnforcedPatching/FrameConnectionDerivative.lean.
"""

from __future__ import annotations

import sympy as sp


def cylindrical_frame(theta: sp.Expr) -> sp.Matrix:
    """Physical columns e_r, e_theta, e_z in Cartesian coordinates."""
    c, s = sp.cos(theta), sp.sin(theta)
    return sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def cylindrical_connection() -> sp.Matrix:
    """E.T * partial_theta E, the constant SO(2) generator."""
    return sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])


def source_tensor(A: sp.Expr, B: sp.Expr,
                  C: sp.Expr, D: sp.Expr) -> sp.Matrix:
    """Full trace-free source-frame tensor, including hoop/stress gauge."""
    return sp.Matrix([[-D, C, A], [C, 0, B], [A, B, D]])


def frame_derivative_residuals(r: sp.Symbol, theta: sp.Symbol) -> dict[str, sp.Matrix]:
    """Exact frame derivative identity in all five coordinate directions."""
    E, omega = cylindrical_frame(theta), cylindrical_connection()
    def dx(M: sp.Matrix) -> sp.Matrix:
        return sp.cos(theta) * M.diff(r) - sp.sin(theta) * M.diff(theta) / r
    def dy(M: sp.Matrix) -> sp.Matrix:
        return sp.sin(theta) * M.diff(r) + sp.cos(theta) * M.diff(theta) / r
    return {
        "theta": E.diff(theta) - E * omega,
        "r": E.diff(r),
        "z": sp.zeros(3),  # E has no z dependence by construction.
        "x": dx(E) + sp.sin(theta) * E * omega / r,
        "y": dy(E) - sp.cos(theta) * E * omega / r,
    }


def cartesian_source(A: sp.Expr, B: sp.Expr, C: sp.Expr, D: sp.Expr,
                     p: sp.Expr, r: sp.Symbol, theta: sp.Symbol,
                     z: sp.Symbol) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Calculate div(E H E.T)+grad(p) in Cartesian, then pull into frame.

    The Cartesian differential operators are exactly
    Dx=cos(theta)*Dr-sin(theta)/r*Dtheta and
    Dy=sin(theta)*Dr+cos(theta)/r*Dtheta.
    """
    E = cylindrical_frame(theta)
    K = E * source_tensor(A, B, C, D) * E.T

    def dx(expr: sp.Expr) -> sp.Expr:
        return sp.cos(theta) * sp.diff(expr, r) - sp.sin(theta) * sp.diff(expr, theta) / r

    def dy(expr: sp.Expr) -> sp.Expr:
        return sp.sin(theta) * sp.diff(expr, r) + sp.cos(theta) * sp.diff(expr, theta) / r

    physical = sp.Matrix([
        dx(K[i, 0]) + dy(K[i, 1]) + sp.diff(K[i, 2], z)
        for i in range(3)
    ]) + sp.Matrix([dx(p), dy(p), sp.diff(p, z)])
    local = E.T * physical
    return tuple(sp.trigsimp(sp.expand(expr)) for expr in local)


def cylindrical_source_formula(A: sp.Expr, B: sp.Expr, C: sp.Expr,
                               D: sp.Expr, p: sp.Expr, r: sp.Symbol,
                               theta: sp.Symbol, z: sp.Symbol
                               ) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Hand-derived local source including each geometric connection."""
    return (
        -sp.diff(D, r) + sp.diff(C, theta) / r + sp.diff(A, z)
        - D / r + sp.diff(p, r),
        sp.diff(C, r) + 2 * C / r + sp.diff(B, z)
        + sp.diff(p, theta) / r,
        sp.diff(A, r) + A / r + sp.diff(B, theta) / r
        + sp.diff(D, z) + sp.diff(p, z),
    )


def cartesian_source_via_connections(E: sp.Matrix, H: sp.Matrix,
                                     p: sp.Expr, r: sp.Symbol,
                                     theta: sp.Symbol, z: sp.Symbol
                                     ) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Full Cartesian divergence via SO(3) moving-frame connections.

    PRECONDITION: E.T * E = I (on r>0). The formula works for a general
    smoothly varying orthogonal frame, not only the cylindrical frame.
    It computes E.T*(div(E*H*E.T) + grad(p)), retaining all ∂E terms.
    
    Gamma_i = E.T * ∂_i E; hence Gamma_i.T = -Gamma_i, and
    ∂_i(E H E.T) = E (∂_i H + [Gamma_i,H]) E.T.
    """
    if E.shape != (3, 3) or H.shape != (3, 3):
        raise ValueError("E and H must both be 3-by-3 matrices")

    def dx(expr):
        return sp.cos(theta)*sp.diff(expr, r) - sp.sin(theta)*sp.diff(expr, theta)/r

    def dy(expr):
        return sp.sin(theta)*sp.diff(expr, r) + sp.cos(theta)*sp.diff(expr, theta)/r

    def dz(expr):
        return sp.diff(expr, z)

    derivatives = (dx, dy, dz)
    source = sp.zeros(3, 1)
    for i, deriv in enumerate(derivatives):
        gamma = E.T * E.applyfunc(deriv)
        pulled_derivative = H.applyfunc(deriv) + gamma*H - H*gamma
        for b in range(3):
            source[b] += sum(E[i, a]*pulled_derivative[a, b] for a in range(3))
            source[b] += E[i, b]*deriv(p)
    return tuple(source)


def pressure_axial_jump(D: sp.Expr, p: sp.Expr, r: sp.Symbol,
                        theta: sp.Symbol, z: sp.Symbol,
                        lower: sp.Expr, upper: sp.Expr) -> sp.Expr:
    """The retained trace [K_zz+p] at the two axial faces."""
    del r, theta  # They remain free symbolic parameters in D and p.
    return sp.simplify((D + p).subs(z, upper) - (D + p).subs(z, lower))
