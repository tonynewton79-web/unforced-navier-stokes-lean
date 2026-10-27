"""Exact Bernstein upper bound for a manufactured H8 diagnostic source.

All arithmetic uses fractions; no floating-point estimate enters the
obstruction certificate. This does not authenticate the unavailable H8 source.
"""

from fractions import Fraction as Q
from math import comb

from meridional_h8_certificate import (
    axial_profile, certificate, derivative, integrate, product, radial_profile,
)


def polynomial_sum(*polynomials):
    width = max(map(len, polynomials), default=0)
    return tuple(sum((p[i] for p in polynomials if i < len(p)), Q(0))
                 for i in range(width))


def polynomial_scale(p, scalar):
    return tuple(scalar * v for v in p)


def bernstein_coefficients(poly, lo, hi, degree=None):
    """Return Bernstein coefficients over [lo, hi] at a common degree.

    For 0<=t<=1, p(lo+(hi-lo)t) is a convex combination of these values.
    """
    if not lo < hi:
        raise ValueError("Bernstein interval must have positive width")
    if not poly:
        raise ValueError("polynomial cannot be empty")
    if degree is None:
        degree = len(poly) - 1
    if degree < len(poly) - 1:
        raise ValueError("target Bernstein degree is too small")
    width = hi - lo
    shifted = [Q(0)] * (degree + 1)
    for j, coefficient in enumerate(poly):
        for k in range(j + 1):
            shifted[k] += coefficient * comb(j, k) * lo**(j - k) * width**k
    return tuple(
        sum((shifted[k] * Q(comb(i, k), comb(degree, k))
             for k in range(i + 1)), Q(0))
        for i in range(degree + 1)
    )


def bound_separable_polynomial(terms, rlo, rhi, zlo, zhi):
    """Certified supremum bound for |sum_i U_i(r)V_i(z)| on a rectangle."""
    if not terms:
        return Q(0)
    rdeg = max(len(u) - 1 for u, _ in terms)
    zdeg = max(len(v) - 1 for _, v in terms)
    converted = [
        (bernstein_coefficients(u, rlo, rhi, rdeg),
         bernstein_coefficients(v, zlo, zhi, zdeg))
        for u, v in terms
    ]
    return max(abs(sum((ur[i] * vz[j] for ur, vz in converted), Q(0)))
               for i in range(rdeg + 1) for j in range(zdeg + 1))


def manufactured_meridional_certificate(grid_size=40):
    """Bound the sharp original seven-ray cone dual on the polynomial source.

    Only the source f = P(r) eta'(z) e_z is tested. A real H8 test additionally
    requires the actual H8 source g - Leray(div(rho R_star)).
    """
    if type(grid_size) is not int or grid_size <= 0:
        raise ValueError("positive integer grid_size is required")

    p, eta = radial_profile(), axial_profile()
    pd, pdd = derivative(p), derivative(derivative(p))
    ed, edd, eddd = derivative(eta), derivative(derivative(eta)), derivative(derivative(derivative(eta)))
    r = (Q(0), Q(1))
    # The meridional solenoidal test v_r=-rP eta'',
    # v_z=(2P+rP') eta', v_theta=0 has
    # ell_A = partial_z(v_r)+partial_r(v_z),
    # ell_D = partial_z(v_z)-partial_r(v_r), ell_B=ell_C=0.
    radial_a1 = polynomial_scale(product(r, p), Q(-1))
    radial_a2 = polynomial_sum(polynomial_scale(pd, Q(3)), product(r, pdd))
    radial_d = polynomial_sum(polynomial_scale(p, Q(3)),
                              polynomial_scale(product(r, pd), Q(2)))
    a_terms = ((radial_a1, eddd), (radial_a2, ed))
    d_terms = ((radial_d, edd),)
    r_weight = product(r, p)
    support_upper = Q(0)
    n = grid_size
    for i in range(n):
        rlo, rhi = Q(1) + Q(i, n), Q(1) + Q(i + 1, n)
        radial_mass = integrate(r_weight, rlo, rhi)
        for j in range(n):
            zlo, zhi = Q(-1) + Q(2*j, n), Q(-1) + Q(2*(j + 1), n)
            axial_mass = integrate(eta, zlo, zhi)
            amax = bound_separable_polynomial(a_terms, rlo, rhi, zlo, zhi)
            dmax = bound_separable_polynomial(d_terms, rlo, rhi, zlo, zhi)
            local_sharp_upper = max(amax, amax / 2 + dmax / 4)
            support_upper += radial_mass * axial_mass * local_sharp_upper
    pairing = certificate()["dual_source_pairing"]
    original_budget = Q(15971, 122900)
    return {
        "source_kind": "manufactured_meridional_only",
        "grid_size": n,
        "dual_source_pairing": pairing,
        "original_budget": original_budget,
        "sharp_support_integral_upper": support_upper,
        "strict_original_budget_margin": pairing - original_budget * support_upper,
    }


if __name__ == "__main__":
    for key, value in manufactured_meridional_certificate().items():
        print(f"{key} = {value}")
