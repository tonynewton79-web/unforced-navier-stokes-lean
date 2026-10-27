"""Exact split-cutoff physical flux and certified rotating-frame enclosures.

The core cutoff chi(r,theta,z) and poloidal shaper cutoff b(r) are
independent, as allowed by the available Case 006 source architecture.
The caller must still supply the genuine functions, pressure and frame;
symbolic examples are not authentication of that missing source.
"""

from dataclasses import dataclass
from fractions import Fraction as Q

import sympy as sp

from h8_positive_cone import positive_support
from h8_rotating_frame import dual_covector


@dataclass(frozen=True)
class SplitCutoffShear:
    shear: sp.Expr
    core_radial_second: sp.Expr
    core_nonradial_second: sp.Expr
    shaper_radial_second: sp.Expr
    lower_order_shear: sp.Expr
    axial_jump: sp.Expr | None
    J: sp.Expr | None
    source_axial_marginal: sp.Expr | None
    time_axial_marginal: sp.Expr | None = None
    J_full: sp.Expr | None = None
    full_source_axial_marginal: sp.Expr | None = None


@dataclass(frozen=True)
class SpatialFrameSupport:
    nominal_plus: Q
    nominal_minus: Q
    lower_plus: Q
    upper_plus: Q
    lower_minus: Q
    upper_minus: Q
    error: Q


@dataclass(frozen=True)
class RotatingDivergence:
    frozen_frame: tuple[sp.Expr, ...]
    connection: tuple[sp.Expr, ...]
    full: tuple[sp.Expr, ...]


def rotated_stress_divergence(frame, source_stress, coordinates):
    r"""Exact Cartesian div(E H E^T), separating the connection terms.

    In an ordinary Cartesian chart, for each physical component i,
       flat_i=sum_{j,a,b} E_ia E_jb partial_j H_ab,
       connection_i=sum_{j,a,b} [partial_j E_ia E_jb
                                + E_ia partial_j E_jb] H_ab.
    Cylindrical components additionally require the usual metric
    connection; using this Cartesian identity on a cylindrical matrix
    without that term is not permitted.
    """
    if len(coordinates) != 3:
        raise ValueError("three Cartesian coordinates are required")
    if len(frame) != 3 or len(source_stress) != 3 or any(
            len(row) != 3 for row in (*frame, *source_stress)):
        raise ValueError("frame and source tensor must be 3-by-3")
    E = tuple(tuple(sp.sympify(v) for v in row) for row in frame)
    H = tuple(tuple(sp.sympify(v) for v in row) for row in source_stress)
    flat, connection = [], []
    for i in range(3):
        flat_i = sum(
            (E[i][a]*E[j][b]*sp.diff(H[a][b], coordinates[j])
             for j in range(3) for a in range(3) for b in range(3)),
            sp.S.Zero)
        conn_i = sum(
            ((sp.diff(E[i][a], coordinates[j])*E[j][b]
              +E[i][a]*sp.diff(E[j][b], coordinates[j]))*H[a][b]
             for j in range(3) for a in range(3) for b in range(3)),
            sp.S.Zero)
        flat.append(sp.simplify(flat_i))
        connection.append(sp.simplify(conn_i))
    return RotatingDivergence(tuple(flat), tuple(connection),
                              tuple(sp.simplify(flat[i]+connection[i])
                                    for i in range(3)))


def _mean(expr, theta, z, z_lower, z_upper):
    angular = sp.integrate(sp.sympify(expr), (theta, 0, 2*sp.pi))/(2*sp.pi)
    return sp.simplify(sp.integrate(angular, (z, z_lower, z_upper)))


def _boundary_mean(expr, theta, z, z_lower, z_upper):
    jump = sp.simplify(expr.subs(z, z_upper)-expr.subs(z, z_lower))
    return sp.simplify(sp.integrate(jump, (theta, 0, 2*sp.pi))/(2*sp.pi))


def split_cutoff_shear(r, theta, z, z_lower, z_upper, background_meridional,
                       core_potential, core_cutoff, poloidal_profiles,
                       shaper_cutoff, *, viscosity=1, pressure=0,
                       inner_radius=None, time_symbol=None):
    r"""Compute the full physical rz shear of two separately cut off curls.

    Total u_{r,z} = background + curl(chi*A_c + b*sum K*a*Xi/r e_theta)_{r,z}.
    chi may vary in (r,theta,z); b must be radial. For the physical shear
        K_rz = u_r*u_z - nu*(d_z u_r+d_r u_z)
    the *entire* pure cutoff-second-jet contribution is partitioned into
        -nu*A_theta*chi_rr,
        -nu*(-A_theta*chi_zz+A_z*chi_{theta z}/r
                                 -A_r*chi_{r theta}/r),
        -nu*(sum K*a*Xi/r)*b_rr.
    Other contributions include cutoff first derivatives, nonlinear
    cross terms and derivatives of the base potential.

    For a specified full pressure representative, also compute
        q_s = [<u_z^2 - 2*nu*d_z u_z + p>_theta]_{z_lower}^{z_upper}
        J = S - a*S(a)/r + (1/r)*int_a^r s*q_s(s) ds.
    This is a necessary integrated identity, not an inverse-stress solver.
    The spatial flux J is not the primitive of the *time-dependent*
    Navier--Stokes source. If time_symbol is supplied and the fields
    depend on it, add the separately computed axial d_t u_z marginal
    to obtain J_full. Otherwise J_full is explicitly unknown.
    """
    chi, b, nu = map(sp.sympify, (core_cutoff, shaper_cutoff, viscosity))
    if b.has(theta, z):
        raise ValueError("the shaper envelope must be radial")
    ar, at, az = map(sp.sympify, core_potential)
    U_r, U_z = map(sp.sympify, background_meridional)
    psi_theta = sum(
        (sp.sympify(K)*sp.sympify(a)*sp.sympify(xi)/r
         for K, a, xi in poloidal_profiles), sp.S.Zero)
    phi_theta = chi*at + b*psi_theta
    u_r = U_r + sp.diff(chi*az, theta)/r-sp.diff(phi_theta, z)
    u_z = U_z + sp.diff(r*phi_theta, r)/r-sp.diff(chi*ar, theta)/r
    physical = (u_r*u_z-nu*(sp.diff(u_r, z)+sp.diff(u_z, r)))
    S = _mean(physical, theta, z, z_lower, z_upper)

    core_rr = -nu*_mean(at*sp.diff(chi, r, 2),
                        theta, z, z_lower, z_upper)
    core_other = -nu*_mean(
        -at*sp.diff(chi, z, 2)
        +az*sp.diff(chi, theta, z)/r
        -ar*sp.diff(chi, r, theta)/r,
        theta, z, z_lower, z_upper)
    shaper_rr = -nu*_mean(psi_theta*sp.diff(b, r, 2),
                          theta, z, z_lower, z_upper)
    remaining = sp.simplify(S-core_rr-core_other-shaper_rr)

    if inner_radius is None:
        time_marginal = (_mean(sp.diff(u_z, time_symbol), theta, z,
                               z_lower, z_upper)
                         if time_symbol is not None else None)
        return SplitCutoffShear(S, core_rr, core_other, shaper_rr,
                                remaining, None, None, None,
                                time_marginal)
    a = sp.sympify(inner_radius)
    q_s = _boundary_mean(u_z*u_z-2*nu*sp.diff(u_z, z)
                         +sp.sympify(pressure), theta, z,
                         z_lower, z_upper)
    s = sp.Dummy("s", positive=True)
    primitive = sp.integrate(s*q_s.subs(r, s), (s, a, r))
    J = sp.simplify(S-a*S.subs(r, a)/r+primitive/r)
    source = sp.simplify(sp.diff(r*S, r)/r+q_s)
    if time_symbol is not None:
        time_marginal = _mean(sp.diff(u_z, time_symbol),
                              theta, z, z_lower, z_upper)
        time_primitive = sp.integrate(s*time_marginal.subs(r, s),
                                       (s, a, r))
        J_full = sp.simplify(J+time_primitive/r)
        source_full = sp.simplify(source+time_marginal)
    else:
        time_marginal = J_full = source_full = None
    return SplitCutoffShear(S, core_rr, core_other, shaper_rr, remaining,
                            q_s, J, source, time_marginal, J_full, source_full)


def spatial_frame_support_bounds(patches):
    """Rigorous interval bounds for variable-frame H8 shear support.

    Each patch supplies (mass, E0, delta), where mass=int_patch rho>=0,
    E0 is an EXACT orthogonal rational matrix, and delta is a CERTIFIED
    upper bound on sup_patch ||E(x)-E0||_F for the true moving frame.
    No grid sampling establishes delta by itself.

    The four-coordinate source correction
       H=[[-D,C,A],[C,0,B],[A,B,D]]
    has ||H||_F <= rho under the one-sided seven-ray positivity floors:
    the exact coordinate-wise extrema are each less than rho/4.
    For orthogonal E and E0, |(EHE^T-E0HE0^T)_rz|
       <= 2*rho*||E-E0||_F.
    Additivity of the independent pointwise support and this error give
    rigorous upper/lower enclosures of both weighted dual supports.
    """
    g = ((0, 0, 1), (0, 0, 0), (0, 0, 0))
    plus, minus, error = Q(0), Q(0), Q(0)
    count = 0
    for mass, frame, delta in patches:
        count += 1
        mass, delta = Q(mass), Q(delta)
        if mass < 0 or delta < 0:
            raise ValueError("mass and certified frame error must be nonnegative")
        if len(frame) != 3 or any(len(row) != 3 for row in frame):
            raise ValueError("a 3-by-3 orthogonal reference frame is required")
        E = tuple(tuple(Q(v) for v in row) for row in frame)
        if any(sum((E[i][k]*E[j][k] for k in range(3)), Q(0))
               != (1 if i == j else 0)
               for i in range(3) for j in range(3)):
            raise ValueError("the reference frame must be exactly orthogonal")
        cov = dual_covector(E, g)
        plus += positive_support(*cov, mass)
        minus += positive_support(*(-v for v in cov), mass)
        error += 2*mass*delta
    if not count:
        raise ValueError("at least one certified frame patch is needed")
    return SpatialFrameSupport(plus, minus, max(Q(0), plus-error),
                               plus+error, max(Q(0), minus-error),
                               minus+error, error)
