"""Exact second-jet coefficient for a shared radial curl/shaper envelope.

This is a conditional *physical* rz shear calculation.  It does not
reconstruct the authentic H8 inverse stress, spatially varying H8 frame,
or pressure-compensated source without the remaining original profiles.
"""

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class SharedCutoffShear:
    core_moment: sp.Expr
    shaper_moment: sp.Expr
    second_coefficient: sp.Expr
    physical_shear: sp.Expr
    first_order_remainder: sp.Expr


def _axial_azimuthal_mean(expr, theta, z, z_lower, z_upper):
    """Integrate axial height and *normalized* full angular period."""
    angular = sp.integrate(sp.sympify(expr), (theta, 0, 2*sp.pi))/(2*sp.pi)
    return sp.simplify(sp.integrate(angular, (z, z_lower, z_upper)))


def shared_cutoff_physical_shear(r, theta, z, z_lower, z_upper,
                                 background_r, background_z,
                                 potential_r, potential_theta, potential_z,
                                 poloidal_profiles, cutoff, *, viscosity=1):
    r"""Decompose K_rz for u=U+curl(b(r) A)+sum_i P_i.

    Each poloidal profile (K_i,a_i(r),Xi_i(z)) is included as the
    azimuthal potential K_i a_i Xi_i/r *before* applying the same b.
    The potential may have C4 (rather than SO2) angular dependence.
    Purely azimuthal velocities do not change physical K_rz directly.

    For physical symmetric stress
    K_rz=u_r*u_z-nu*(d_z u_r+d_r u_z), the b'' coefficient is
    -nu * int_z <A_theta + sum_i K_i a_i Xi_i/r>_theta dz.
    """
    b = sp.sympify(cutoff)
    nu = sp.sympify(viscosity)
    if b.has(theta, z):
        raise ValueError("The shared cutoff must depend on radius only")

    ar, at, az = map(sp.sympify, (potential_r, potential_theta, potential_z))
    profiles = tuple(poloidal_profiles)
    shaper_theta = sum((sp.sympify(K)*sp.sympify(a)*sp.sympify(xi)/r
                        for K, a, xi in profiles), sp.S.Zero)
    total_theta = at+shaper_theta
    # Cylindrical curl of the *unmultiplied* vector potential.
    vr = sp.diff(az, theta)/r-sp.diff(total_theta, z)
    vz = sp.diff(r*total_theta, r)/r-sp.diff(ar, theta)/r
    wz = total_theta

    du_r = b*vr
    du_z = b*vz+sp.diff(b, r)*wz
    ur, uz = map(sp.sympify, (background_r, background_z))
    physical_increment = ((ur+du_r)*(uz+du_z)-ur*uz
                          -nu*(sp.diff(du_r, z)+sp.diff(du_z, r)))
    physical_shear = _axial_azimuthal_mean(
        physical_increment, theta, z, z_lower, z_upper)

    core_moment = _axial_azimuthal_mean(at, theta, z, z_lower, z_upper)
    shaper_moment = _axial_azimuthal_mean(
        shaper_theta, theta, z, z_lower, z_upper)
    second_coefficient = sp.simplify(-nu*(core_moment+shaper_moment))
    first_order_remainder = sp.simplify(
        physical_shear-second_coefficient*sp.diff(b, r, 2))
    return SharedCutoffShear(core_moment, shaper_moment,
                             second_coefficient, physical_shear,
                             first_order_remainder)


def axial_curl_circulation_primitive(r, theta, z, z_lower, z_upper,
                                     reference_radius,
                                     reference_circulation,
                                     axial_curl):
    r"""Reconstruct int_z <A_theta> from <curl(A)_z> and annular trace.

    The reference circulation is
    H=int_z r0*<A_theta(r0,theta,z)> dz, which may be nonzero on an
    annulus.  For an axis-spanning smooth potential, r0=0 and H=0.
    This follows from d_r(r*<A_theta>)=r*<curl(A)_z>, since the
    normalized theta average kills d_theta A_r.
    """
    height_curl = _axial_azimuthal_mean(
        axial_curl, theta, z, z_lower, z_upper)
    s = sp.Dummy("s", positive=True)
    weighted = sp.integrate(s*height_curl.subs(r, s),
                            (s, sp.sympify(reference_radius), r))
    return sp.simplify((sp.sympify(reference_circulation)+weighted)/r)
