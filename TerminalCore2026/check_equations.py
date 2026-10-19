"""Exact checks for selected equations in Zenodo 23474915.

These are finite tests, not proofs of the PDE analytic estimates.
"""
from fractions import Fraction as Q
import sympy as s

h, p = s.symbols('h p', positive=True)
sigma = -(s.Rational(1, 2) + h) + (s.Rational(3, 2) - h) / p
assert s.simplify(sigma.subs(p, 3) + 4*h/3) == 0
pc = (3-2*h)/(1+2*h)
assert s.simplify(sigma.subs(p, pc)) == 0
assert s.simplify((2*p/(p-3))*sigma + 1 + 2*h*(p+1)/(p-3)) == 0
assert s.expand(4*(h+1)**3 - (h+2)**2*(2*h+1) - h**2*(2*h+3)) == 0
worst = (Q(0), None)
for nu in (1, 2):
    for a in range(101):
        for b in range(101):
            rat = Q(2*(a+2)**2*(2*a+1)*(b+1)**2,
                    (a+1)**2*(a+nu)*(b+3)**2)
            assert rat <= 8, (nu, a, b, rat)
            if rat > worst[0]:
                worst = (rat, (nu, a, b))
print('Exact symbolic exponent identities: PASS')
print('Two-derivative ratio grid <= sharp 8 (20,402 cases):', worst)
for n in range(1, 201):
    summ = sum((Q(1, (i+1)**2*(n-i+1)**2) for i in range(n+1)), Q(0))
    assert (n+1)**2 * summ <= Q(16, 3), n
print('Radial convolution bound for n=1..200: PASS')
