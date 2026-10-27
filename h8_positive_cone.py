"""Exact one-sided positivity-floor cone for the seven source-frame rays.

Unlike the *sufficient* symmetric |delta c_i|<=gamma*rho constraint,
the actual coefficient floor demands only
    c_i^(0)*rho + delta c_i >= rho/100.
The third ray has a larger starting coefficient, so the sharp cone is
asymmetric. Nothing here asserts that a compact PDE stress exists.
"""

from fractions import Fraction as Q


GAMMA = Q(15971, 122900)  # Six rays: 172/1229 - 1/100.
GAMMA_THIRD = Q(22371, 122900)  # Third ray: 236/1229 - 1/100.


def _data(a, b, c, d, rho):
    a, b, c, d, rho = (Q(x) for x in (a, b, c, d, rho))
    if rho < 0:
        raise ValueError("the nonnegative density weight is required")
    return a, b, c, d, rho


def _sign(x):
    return (x > 0) - (x < 0)


def positive_support(a, b, c, d, rho):
    a, b, c, d, rho = _data(a, b, c, d, rho)
    g, h = GAMMA, GAMMA_THIRD
    k = (h+3*g)/4
    center = (h-g)*c/4
    B_part = g*abs(4*a+b)/8
    at_lower_D = k*abs(c) - g*d/4
    at_upper_D = k*abs(a) + (g+h)*d/8
    return rho * (center + B_part + max(at_lower_D, at_upper_D))


def axial_flux_cap(rho):
    """Sharp |H_rz|=|A| cap for the original one-sided seven-ray floor.

    For nonnegative rho the two support values in the +/- A directions
    coincide at (5*GAMMA + GAMMA_THIRD)*rho/4. This is a pointwise
    necessary bound and does not solve the divergence equation.
    """
    return positive_support(1, 0, 0, 0, rho)


def positive_maximizer(a, b, c, d, rho):
    a, b, c, d, rho = _data(a, b, c, d, rho)
    g, h = GAMMA, GAMMA_THIRD
    k = (h+3*g)/4
    B = g*rho*_sign(4*a+b)/8
    center_C = (h-g)*rho/4
    if k*abs(a)+(g+h)*d/8 >= k*abs(c)-g*d/4:
        D = (g+h)*rho/8
        C = center_C
        x = k*rho*_sign(a)
    else:
        D = -g*rho/4
        C = center_C+k*rho*_sign(c)
        x = Q(0)
    return x+4*B, B, C, D
