"""Exact enclosure for the manufactured meridional one-sided H8 dual.

This computes LOWER and UPPER rational enclosures on the *available*
dual support, whose direction is -grad(v). A non-obstructing dual field
does not establish a primal spatial stress, much less the true H8 source.
"""

from fractions import Fraction as Q

from h8_sharp_dual_certificate import (
    bernstein_coefficients, polynomial_scale, polynomial_sum,
)
from h8_positive_cone import GAMMA, GAMMA_THIRD
from meridional_h8_certificate import (
    axial_profile, certificate, derivative, integrate, product, radial_profile,
)


def signed_bernstein_upper(terms, rlo, rhi, zlo, zhi):
    """Upper envelope using *signed* bivariate Bernstein coefficients."""
    if not terms:
        return Q(0)
    rdegree = max(len(u)-1 for u, _ in terms)
    zdegree = max(len(v)-1 for _, v in terms)
    converted = [
        (bernstein_coefficients(u, rlo, rhi, rdegree),
         bernstein_coefficients(v, zlo, zhi, zdegree))
        for u, v in terms
    ]
    return max(sum((u[i]*v[j] for u,v in converted), Q(0))
               for i in range(rdegree+1) for j in range(zdegree+1))


def integrate_weighted_terms(terms, rw, zw, rlo, rhi, zlo, zhi):
    """Exact integral of rw(r)zw(z)*sum U(r)V(z) on a rectangle."""
    return sum((integrate(product(rw, u), rlo, rhi) *
                integrate(product(zw, v), zlo, zhi)
                for u,v in terms), Q(0))


def manufactured_one_sided_certificate(grid_size=40):
    if type(grid_size) is not int or grid_size <= 0:
        raise ValueError("positive integer grid_size is required")
    p, eta = radial_profile(), axial_profile()
    pd, pdd = derivative(p), derivative(derivative(p))
    ed = derivative(eta)
    edd, eddd = derivative(ed), derivative(derivative(ed))
    rp = product((Q(0), Q(1)), p)
    # Differentiating the meridional solenoidal test field:
    # a=∂_z v_r+∂_r v_z, d=∂_z v_z-∂_r v_r.
    a_terms = (
        (polynomial_scale(rp, Q(-1)), eddd),
        (polynomial_sum(polynomial_scale(pd, Q(3)),
                        product((Q(0), Q(1)), pdd)), ed),
    )
    d_terms = ((polynomial_sum(polynomial_scale(p, Q(3)),
                                polynomial_scale(product((Q(0), Q(1)), pd), Q(2))), edd),)
    g, h = GAMMA, GAMMA_THIRD
    k, u = (h+3*g)/4, (g+h)/8

    def linear_terms(alpha, beta):
        return tuple((polynomial_scale(U, alpha), V) for U,V in a_terms) + \
               tuple((polynomial_scale(U, beta), V) for U,V in d_terms)

    # The exact support for the dual covector (-a,0,0,-d) equals max F_j.
    # These four affine vertex actions are independent of rho.
    actions = (
        linear_terms(g/2, g/4),
        linear_terms(-g/2, g/4),
        linear_terms(g/2+k, -u),
        linear_terms(-(g/2+k), -u),
    )

    n = grid_size
    lower = upper = Q(0)
    for i in range(n):
        rlo, rhi = Q(1)+Q(i, n), Q(1)+Q(i+1, n)
        mass_r = integrate(rp, rlo, rhi)
        for j in range(n):
            zlo, zhi = Q(-1)+Q(2*j, n), Q(-1)+Q(2*(j+1), n)
            mass = mass_r * integrate(eta, zlo, zhi)
            lower += max(integrate_weighted_terms(
                terms, rp, eta, rlo, rhi, zlo, zhi) for terms in actions)
            upper += mass * max(signed_bernstein_upper(
                terms, rlo, rhi, zlo, zhi) for terms in actions)
    pairing = certificate()["dual_source_pairing"]
    return {
        "source_kind": "manufactured_meridional_only",
        "grid_size": n,
        "dual_source_pairing": pairing,
        "support_integral_lower": lower,
        "support_integral_upper": upper,
        "lower_minus_pairing": lower-pairing,
        "upper_minus_pairing": upper-pairing,
    }


if __name__ == "__main__":
    for key, value in manufactured_one_sided_certificate().items():
        print(f"{key} = {value}")
