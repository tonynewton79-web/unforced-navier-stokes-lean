#!/usr/bin/env python3
"""Finite independent audit for Proof Attack 14 (2026-10-24).

Tests a rational beta integral, positive Gaussian curl, bilinear polynomial
cancellation, and sample values of scalar bounds. NOT a PDE or Lean proof.
"""
from collections import Counter
from fractions import Fraction
from math import exp, factorial, pi, sqrt

Q = Fraction
mass = Q(1, 2**9) * Q(factorial(4)**2, factorial(9))
assert mass == Q(1, 322560), mass
assert 8 * Q(1, 4) * Q(1, 2) == 1
pairing_floor = pi * exp(-4) * float(mass**2)
assert pairing_floor > 0
print("exact chi mass:", mass)
print("pressure-free meridional pairing lower bound:", pairing_floor)

def residual_radial(r, z):
    return -r * exp(-2 * (r*r + z*z))

for r,z in [(0.6,0.7),(0.85,0.90),(1.0,1.0)]:
    eps=1e-5
    derivative=(residual_radial(r,z+eps)-residual_radial(r,z-eps))/(2*eps)
    exact=4*r*z*exp(-2*(r*r+z*z))
    assert exact > 0
    assert abs(derivative-exact)/exact < 1e-8

# For N(w)=B(background,w)+B(w,background)+B(w,w),
# cancellation of N(w1) leaves precisely the w2-containing terms.
cancelled = Counter({("B","w1"):1,("w1","B"):1,("w1","w1"):1})
quadratic = Counter({
    ("B","w1"):1, ("w1","B"):1, ("B","w2"):1, ("w2","B"):1,
    ("w1","w1"):1, ("w1","w2"):1, ("w2","w1"):1, ("w2","w2"):1
})
assert quadratic-cancelled == Counter({
    ("B","w2"):1,("w2","B"):1,("w1","w2"):1,
    ("w2","w1"):1,("w2","w2"):1
})

nu,A,F,Cs=1.,2.,3.,4.
for T in [0.0001,0.001,0.01,0.05]:
    H=T+sqrt(2*T/(exp(1)*nu))
    W1=T*F
    W2=Cs*H*(2*A*W1+W1*W1)
    E2=Cs*(2*A*W2+2*W1*W2+W2*W2)
    assert all(x>0 for x in [H,W1,W2,E2])
    print("T",T,"W1 bound",W1,"W2 bound",W2,"residual bound",E2)

print("FINITE_AUDIT_PASS; full source-matched PDE and Lean proofs remain open")
