"""Exact meridional velocity/viscous shear from separable Case 006 shapers.

This reduces the *named shaper* term family only. It excludes the still
unspecified curl localization, temporal residual, full pressure, inverse
stress and nonlinear four-patch overlaps. Inputs are source-compatible
symbolic functions, not a claim that the authentic profiles are frozen.
"""

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class ShaperFlux:
    gamma: sp.Expr
    delta: sp.Expr
    quadratic: sp.Expr
    viscous: sp.Expr
    total: sp.Expr


def shaper_flux(r, z, z_lower, z_upper, U_r, U_z, b,
                profiles, *, viscosity=1):
    """Integrate shell-induced physical rz transport and viscous stress.

    Each profile is (constant K_i, radial a_i(r), axial Xi_i(z)) with
    Psi_i=K_i*a_i*b*Xi_i. Require divergence-free axisymmetric core,
    Xi_i=Xi_i'=0 at both axial endpoints. The radius is assumed >0.
    """
    U_r, U_z, b = map(sp.sympify, (U_r, U_z, b))
    nu = sp.sympify(viscosity)
    if sp.simplify(sp.diff(r*U_r, r) + r*sp.diff(U_z, z)) != 0:
        raise ValueError("the core must satisfy cylindrical divergence zero")
    if not profiles:
        raise ValueError("at least one shaper profile is required")
    means = []
    moments = []
    normalized = []
    for K, a, Xi in profiles:
        K, a, Xi = map(sp.sympify, (K, a, Xi))
        if K.has(r, z) or a.has(z) or Xi.has(r):
            raise ValueError("the amplitudes must be constant and profiles separable")
        for endpoint in (z_lower, z_upper):
            if (sp.simplify(Xi.subs(z, endpoint)) != 0 or
                    sp.simplify(sp.diff(Xi, z).subs(z, endpoint)) != 0):
                raise ValueError("axial shaper function and derivative must vanish")
        means.append(sp.integrate(Xi, (z, z_lower, z_upper)))
        moments.append(sp.integrate(U_r*Xi, (z, z_lower, z_upper)))
        normalized.append((K, a, Xi))

    gamma = sp.S.Zero
    delta = sp.S.Zero
    quadratic = sp.S.Zero
    viscous = sp.S.Zero
    for (K, a, Xi), mass, I in zip(normalized, means, moments):
        gamma += K*a*I/r
        delta += K*(sp.diff(a, r)*I - a*(sp.diff(I, r)+I/r))/r
        viscous -= nu*K*mass*sp.diff(sp.diff(a*b, r)/r, r)
    for i in range(len(normalized)):
        K_i, a_i, Xi_i = normalized[i]
        for j in range(i+1, len(normalized)):
            K_j, a_j, Xi_j = normalized[j]
            J = sp.integrate(sp.diff(Xi_i, z)*Xi_j,
                             (z, z_lower, z_upper))
            quadratic += (K_i*K_j/r**2 *
                          (a_j*sp.diff(a_i, r)-a_i*sp.diff(a_j, r))*J)
    gamma, delta, quadratic, viscous = (
        sp.simplify(x) for x in (gamma, delta, quadratic, viscous))
    total = sp.simplify(gamma*sp.diff(b, r)+delta*b+quadratic*b*b+viscous)
    return ShaperFlux(gamma, delta, quadratic, viscous, total)
