"""Exact weighted dual of the unrelaxed H8 seven-ray coefficient budget.

For any nonnegative tau, this calculates the support function of the
four-coordinate polytope whose seven coefficient perturbations satisfy
max_i |delta c_i| <= tau. It does not assert that a compact PDE inverse
exists, and it does not infer absent authentic source data.
"""

from fractions import Fraction as Q


def _arguments(ell_A, ell_B, ell_C, ell_D, tau):
    values = tuple(Q(x) for x in (ell_A, ell_B, ell_C, ell_D, tau))
    if values[-1] < 0:
        raise ValueError("coefficient budget must be nonnegative")
    return values


def _sign(x):
    return (x > 0) - (x < 0)


def sharp_support(ell_A, ell_B, ell_C, ell_D, tau):
    a, b, c, d, tau = _arguments(ell_A, ell_B, ell_C, ell_D, tau)
    return tau * (max((abs(a) + abs(c)) / 2, abs(d) / 4) +
                  abs(4 * a + b) / 8)


def maximizer(ell_A, ell_B, ell_C, ell_D, tau):
    a, b, c, d, tau = _arguments(ell_A, ell_B, ell_C, ell_D, tau)
    B = tau / 8 * _sign(4 * a + b)
    if abs(d) >= 2 * (abs(a) + abs(c)):
        D, C, x = tau / 4 * _sign(d), Q(0), Q(0)
    else:
        D, C, x = Q(0), tau / 2 * _sign(c), tau / 2 * _sign(a)
    return x + 4 * B, B, C, D
