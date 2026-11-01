"""Exact checks of the terminal integrating-factor lemma.

These are finite symbolic regressions; they do not prove the H8 PDE
existence hypotheses or provide a complete Lean certificate.
"""
from fractions import Fraction

import pytest
import sympy as sp


@pytest.mark.parametrize("D,sigma,kappa", [
    (sp.Rational(49, 100), sp.Rational(1, 100), sp.Rational(1, 4)),
    (sp.Rational(1, 2), sp.Rational(1, 10), sp.Rational(1, 5)),
    (sp.Rational(2, 5), sp.Rational(1, 4), sp.Rational(3, 5)),
])
def test_terminal_matched_exact_solution(D, sigma, kappa):
    tau, M = sp.symbols("tau M", positive=True)
    power = D + sigma
    assert power > kappa
    a = -M * tau ** power / (power - kappa)
    # d/dt = -d/dtau, b=kappa/tau, f=M*tau^(power-1)
    residual = -sp.diff(a, tau) + kappa / tau * a - M * tau ** (power - 1)
    assert sp.simplify(residual) == 0
    assert sp.simplify(a / tau ** D) == -M * tau ** sigma / (power - kappa)


def test_neutral_untuned_amplitude_has_nonzero_terminal_limit():
    tau, tau0, D, sigma, M = sp.symbols(
        "tau tau0 D sigma M", positive=True
    )
    power = D + sigma
    # a(t0)=0, a'=M*tau^(power-1).
    a = M * (tau0 ** power - tau ** power) / power
    assert sp.limit(a, tau, 0, dir="+") == M * tau0 ** power / power
