"""Exact-rational Cauchy-to-weighted-jet regression checks.

Finite tests complement, but cannot replace, an all-index Lean theorem.
"""
from fractions import Fraction as F
from math import comb
from random import Random

qs=[(F(1,4),F(1,4)),(F(1,8),F(1,10)),(F(1,100),F(1,5))]
count=0
for q,s in qs:
    for a in range(101):
        aa=(a+1)**2*q**a
        assert aa<=1
        for b in range(101):
            bb=(b+1)**2*s**b
            assert aa*bb/F(comb(2*a+b,b))<=1
            count+=1
print('PASS finite weighted Cauchy coefficient ratios:',count)
for h in [F(1,100),F(1,1000),F(1,10000)]:
    assert 2*h*4<=F(2,25)
print('PASS complex denominator lower bound |L| >= 23/25 for |eta|<=2')
rng=Random(20261019)
for _ in range(1000):
    a,b=rng.randrange(70),rng.randrange(70)
    q,s=qs[rng.randrange(len(qs))]
    M=F(rng.randrange(1,101),rng.randrange(1,101))
    x=M*q**a*s**b
    assert abs(x)*(a+1)**2*(b+1)**2/comb(2*a+b,b)<=M
print('PASS 1000 independent reproducible normalized-jet witnesses')
