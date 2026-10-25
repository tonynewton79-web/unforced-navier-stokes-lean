"""Exact independent finite regression for the radial valuation reconstruction.

Finite exact rational checks support (but cannot replace) Lean's all-index
binomial envelope and half-geometric-tail theorems. This script does not test
the physical Navier--Stokes hierarchy.
"""
from fractions import Fraction
from math import comb

bcount = 0
for a in range(161):
    for b in range(161):
        assert comb(2*a+b, b) <= 4**a * 2**b
        bcount += 1
print("PASS binomial envelope:", bcount, "exact integer cases")

tcount = 0
for n in range(50):
    for N in range(50):
        lhs = sum((Fraction(1,2)**(n+j) for j in range(N)), Fraction(0))
        rhs = 2 * Fraction(1,2)**n * (1-Fraction(1,2)**N)
        assert lhs == rhs
        assert lhs <= 2*Fraction(1,2)**n
        tcount += 1
print("PASS geometric tail:", tcount, "exact rational identities")

ccount = 0
for n in range(1,20):
    for b in range(35):
        estimate = sum((Fraction(comb(2*a+b,b), 8**a*(a+1)**2*(b+1)**2)
                        for a in range(n,60)), Fraction(0))
        bound = Fraction(2,2**n)*2**b/(b+1)**2
        assert estimate <= bound, (n,b)
        ccount += 1
print("PASS coefficient-weight derivative tails:",ccount,"exact rational cases")
