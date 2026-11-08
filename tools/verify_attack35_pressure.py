#!/usr/bin/env python3
"""Exact rational checks of Attack 35 mixed pressure weights (finite tests only)."""
from fractions import Fraction as Q
from math import factorial

def w(a, b):
    return Q(factorial(2*a+b), factorial(2*a)*(a+1)**2*(b+1)**2)

count = 0
for a in range(1, 65):
    for beta in (0, 1, 2, 3, 5, 10, 20, 50, 100):
        for r in range(4):
            ratio = w(a,beta+r)/w(a+1,beta+1)
            cap = Q(8,a+1) if r==0 else 4*2**(r-1)*(a+1)**(r-1)
            assert ratio <= cap, (a,beta,r)
            count += 1
for a in range(1, 35):
    for beta in (0, 2, 6, 20, 50, 100):
        for radial_gain in (1, 2):
            for axial_derivatives in range(2*radial_gain+1):
                ratio=w(a,beta+axial_derivatives)/w(a+radial_gain,beta)
                cap=(radial_gain+1)**2*(2*radial_gain)**axial_derivatives*(a+1)**axial_derivatives
                assert ratio<=cap
                count+=1
assert w(4,103)/w(5,100)>w(4,13)/w(5,10)
print('PASS',count,'exact radial/weak pressure coefficient ratios')
print('WARNING: finite tests do not prove complete G1 local analytic convergence')
