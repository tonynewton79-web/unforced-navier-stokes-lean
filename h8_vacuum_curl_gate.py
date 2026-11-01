"""Exact rank-one quadratic-vacuum curl screen for the H8 seven-ray cone.

If a smooth nonnegative density vanishes at x0 with Hessian
lambda*e_z tensor e_z, and the smooth stress satisfies the original
seven-ray floor, then all coefficient first jets vanish and each
second jet is axial. The local Cartesian source curl, expressed in the
frame E(x0) with E(x0)e_z=e_z, must lie in the sharp parallelogram
certified here. Frame *derivatives* do not enter its second stress jet.

The required Hessian and frame hypotheses are analytic conditions,
not tested or authenticated by this finite arithmetic module.
"""

from fractions import Fraction as Q

from h8_positive_cone import GAMMA, GAMMA_THIRD


def axial_rank_one_curl_feasible(omega_r, omega_theta, omega_z, curvature):
    """Sharp necessary local curl inequalities, in fixed axial frame.

    curvature = d_z^2 rho(x0) >= 0, with the other Hessian entries zero.
    omega = curl(div K + grad p)(x0) in the frame E(x0)=(e_r,e_theta,e_z).
    """
    wr, wt, wz, lam = (Q(v) for v in
                       (omega_r, omega_theta, omega_z, curvature))
    if lam < 0:
        raise ValueError("nonnegative density has nonnegative curvature")
    k = (3*GAMMA + GAMMA_THIRD)/4
    return (wz == 0 and abs(wr) <= GAMMA*lam/8
            and abs(wt + 4*wr) <= k*lam)


def axial_rank_one_curl_witness(omega_r, omega_theta, omega_z,
                               curvature):
    """Construct the exact second-jet (A,B,C,D) attaining a feasible curl.

    This is a pointwise quadratic-jet witness only, not a positive
    compact stress with a prescribed global divergence.
    """
    if not axial_rank_one_curl_feasible(
            omega_r, omega_theta, omega_z, curvature):
        raise ValueError("curl jet violates the seven-ray vacuum cone")
    lam = Q(curvature)
    return (Q(omega_theta), -Q(omega_r),
            (GAMMA_THIRD-GAMMA)*lam/4,
            (GAMMA+GAMMA_THIRD)*lam/8)
