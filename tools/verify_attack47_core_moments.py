#!/usr/bin/env python3
"""Attack47 exact original-source comparison scalar certifier, not a G1 PDE proof."""
from fractions import Fraction as F
from math import factorial,comb
bounds={(0,1):(2393096190540,2393096190542),
        (1,1):(3836224657207,3836224657210),
        (2,1):(9055359580176,9055359580179),
        (0,2):(1602427000590,1602427000593),
        (1,2):(2035245417001,2035245417004)}
def c(n,p):
    if p==1:return F(1,factorial(n)*factorial(n+1))
    return F(comb(2*n+2,n+1),factorial(n)*factorial(n+2))
def a(n,r,p):
    return F((-1)**n*2**(n+2*r+2),n+r+1)*c(n,p)
for n in range(40):
    assert sum((c(k,1)*c(n-k,1) for k in range(n+1)),F(0))==c(n,2)
for (r,p),(lo,hi) in bounds.items():
    upper=sum((a(k,r,p) for k in range(25)),F(0))
    lower=upper+a(25,r,p)
    assert F(lo,10**12)<lower<upper<F(hi,10**12)
    assert upper<F(4**(r+1),r+1)
for n in range(1,60):
    ratio=2*F((2*n+4)*(2*n+3),(n+2)**2*(n+1)*(n+3))
    assert ratio<=F(5,6)
for k in range(1,4):assert F(2,k+2)<=F(2,3)
# Source Lemma B4 reference comparison: Xi=110, Lambda>=1 -> X0<=4.
assert F(6,5)*(110-F(16,110))>F(1318,10)
print("PASS: 40 exact f0-square coefficients, five certified integrals, alternating tails, conditional p1_r endpoint margin")
print("NO original nonlinear C3 fixed point, Xi, five-bump, cone or unforced NS solution is certified.")
