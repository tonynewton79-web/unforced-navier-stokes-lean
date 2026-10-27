"""Exact rational source-matched obstruction to an entrywise stress bound.

This certificate tests the *physical cylindrical tensor-entry* condition
    |H_ij| <= beta * rho,
not the H8 four-parameter positive-cone condition. The coordinate map from
the latter to physical entries has not been proved. The result is a rigorous
necessary-bound diagnostic and cannot certify or refute the original H8 cone.

The compact polynomial profiles have zero extensions of regularity W^(2,∞)
in r and W^(3,∞) in z. Their products can be approximated by nonnegative
smooth compact profiles while preserving the strict rational inequality.
"""

from fractions import Fraction as Q


def product(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return tuple(out)


def derivative(p):
    return tuple(i * p[i] for i in range(1, len(p)))


def evaluate(p, x):
    return sum((a * x**i for i, a in enumerate(p)), Q(0))


def integrate(p, a, b):
    return sum((v * (b**(i + 1) - a**(i + 1)) / (i + 1)
                for i, v in enumerate(p)), Q(0))


def radial_profile():
    # P(r) = (r-1)^2 (2-r)^2, 1 <= r <= 2, zero elsewhere.
    q = product((Q(-1), Q(1)), (Q(2), Q(-1)))
    return product(q, q)


def axial_profile():
    # eta(z) = (1-z^2)^3, -1 <= z <= 1, zero elsewhere.
    q = (Q(1), Q(0), Q(-1))
    return product(product(q, q), q)


def certificate():
    p, eta = radial_profile(), axial_profile()
    pd, ed = derivative(p), derivative(eta)
    psquared, etad_squared = product(p, p), product(ed, ed)
    radial_r_p_squared = integrate(product((Q(0), Q(1)), psquared), Q(1), Q(2))

    # P increases then decreases, vanishing at the ends; eta does likewise
    # around z=0. These signed integrals compute their *absolute* products.
    radial_p_abs_pprime = (
        integrate(product(p, pd), Q(1), Q(3, 2))
        - integrate(product(p, pd), Q(3, 2), Q(2))
    )
    axial_eta_abs_etaprime = (
        integrate(product(eta, ed), Q(-1), Q(0))
        - integrate(product(eta, ed), Q(0), Q(1))
    )
    radial_p = integrate(p, Q(1), Q(2))
    axial_eta = integrate(eta, Q(-1), Q(1))
    axial_eta_abs_z = 2 * integrate(product(eta, (Q(0), Q(1))), Q(0), Q(1))
    axial_eta_abs_z_cubed = 2 * integrate(
        product(eta, (Q(0), Q(0), Q(0), Q(1))), Q(0), Q(1)
    )

    # For 1<=r<=2: |P''|<=2, r<=2. On |z|<=1: |eta''|<=6,
    # |eta'''|<=72|z|+120|z|^3. Bound the full orthonormal cylindrical
    # |nabla v|_1 including the hoop entry v_r/r.
    axial_eta_abs_eta2_upper = 6 * axial_eta
    axial_eta_abs_eta3_upper = 72 * axial_eta_abs_z + 120 * axial_eta_abs_z_cubed
    radial_r2_p_abs_pd_upper = 4 * radial_p_abs_pprime
    radial_r2_psquared_upper = 4 * integrate(psquared, Q(1), Q(2))
    radial_r_p_abs_pd_upper = 2 * radial_p_abs_pprime
    radial_r2_p_abs_p2_upper = 8 * radial_p
    gradient_upper = (
        (4 * radial_r_p_squared + 2 * radial_r2_p_abs_pd_upper)
        * axial_eta_abs_eta2_upper
        + radial_r2_psquared_upper * axial_eta_abs_eta3_upper
        + (3 * radial_r_p_abs_pd_upper + radial_r2_p_abs_p2_upper)
        * axial_eta_abs_etaprime
    )

    pairing = radial_r_p_squared * integrate(etad_squared, Q(-1), Q(1))
    beta = Q(15971, 1720600)
    return {
        "radial_p": radial_p,
        "radial_p_squared": integrate(psquared, Q(1), Q(2)),
        "radial_r_p_squared": radial_r_p_squared,
        "radial_p_abs_pprime": radial_p_abs_pprime,
        "axial_eta": axial_eta,
        "axial_eta_abs_etaprime": axial_eta_abs_etaprime,
        "axial_etaprime_squared": integrate(etad_squared, Q(-1), Q(1)),
        "beta": beta,
        "dual_source_pairing": pairing,
        "dual_gradient_upper": gradient_upper,
        "strict_margin": pairing - beta * gradient_upper,
    }


if __name__ == "__main__":
    for key, value in certificate().items():
        print(f"{key} = {value}")
