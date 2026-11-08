#!/usr/bin/env python3
"""Exact-rational A.19 corrected amplitude and A.15 axial two-moment check.
This is NOT a numerical Cpre, exterior-admissibility, G1, or PDE certificate.
"""
from fractions import Fraction as Q
import sympy as s

def exp_lower(x, N):
    x = Q(x)
    term = Q(1)
    total = term
    for k in range(1, N):
        term *= x / k
        total += term
    return total

Klo = Q(2450492327, 10**10)
Khi = Q(2450520132, 10**10)
amin, amax, eps = Q(49, 50), Q(26, 25), Q(1, 100)
assert exp_lower(26, 22) > 1000
assert Khi * amin**2 - Q(249, 1000) + eps < 0
assert Klo * amax**2 - Q(1, 4) - eps > 0
assert 2 * Klo * Q(9, 10) - eps > 0
assert 2 * Klo * amin - eps > Q(47, 100)

lam = s.symbols("lam", positive=True)
s2 = s.Rational(1, 2) - 2 * lam
p = s.expand(s2 * (2 / lam - 3))
q = s.expand(s2 * (13 / lam - 3))
assert s.simplify(p - (1 / lam - s.Rational(11, 2) + 6 * lam)) == 0
assert s.simplify(q - (s.Rational(13, 2) / lam - s.Rational(55, 2) + 6 * lam)) == 0
assert p.subs(lam, s.Rational(1, 64)) == Q(1875, 32)
assert 64**2 - 64 - 6 > 0
assert 64**2 - 2 * 64 - 6 > 0
assert Q(13, 2) * 64**2 - 2 * 64 - 6 > 0
assert exp_lower(Q(1875, 32), 150) > 10**25
assert exp_lower(499, 100) > 10**40

# The complete pre-pulse C1 source bound has the sum 198 exp(-499).
upstream = Q(198, 10**40)
Lsup = Q(352, 15 * 10**25)
dmax = 2 * (amax + Q(1, 47)) * Lsup + upstream
assert dmax < Q(1, 10**23)
cmax = Q(15, 14) * 64 * dmax
assert cmax < Q(4, 10**22)
assert 64 * cmax < Q(3, 10**20)
assert 64000 * Q(3, 10**20) < Q(2, 10**15)

a, k, zA, zE = s.symbols("a k zA zE", real=True)
jac = 2 * k * a + zA
assert s.simplify(jac * (-zE / jac) + zE) == 0
print("PASS (A.19) conditional unique amplitude 0.98<A<1.04, |A'|<1/47")
print("PASS A.15 complete C1 discrepancy <1e-23, C1 bump <4e-22 and <3e-20*lambda")
print("OPEN numeric source Cpre, full exterior, G1 and global unforced Navier-Stokes")
