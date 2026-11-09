#!/usr/bin/env python3
"""Finite exact arithmetic checks for REGULAR source-selected H8 positive control.
The analytic H4 contraction is proved separately; no singular unforcing is certified.
"""
from fractions import Fraction as Q
from math import factorial
import sympy as s

gamma=Q(15971,122900); eps=gamma/8
assert Q(172,1229)-2*eps == Q(1,100)+3*gamma/4
b=s.Matrix([35,2,0])/s.sqrt(1229)
H=s.zeros(3); H[0,2]=H[2,0]=s.Rational(eps.numerator,eps.denominator)
M=b*b.T-s.eye(3)/3+H
assert s.trace(M.T*M)==s.Rational(2,3)+2*s.Rational(eps.numerator,eps.denominator)**2<1
assert M[1,0]==s.Rational(70,1229)>s.Rational(1,18)
assert M[2,0]>s.Rational(1,64)

# Explicit Cauchy derivative bounds; e>2 and 30/49>3/5.
assert Q(33,256)<Q(1,6)
assert Q(30,49)>Q(3,5)
D4=factorial(4)*216**4
H4factor=16*576*D4
assert H4factor==481469424205824<5*10**14
# Fourier H4 algebra/embedding shell and mild mapping.
assert Q(52,36**4)<Q(1,1000)
amp=Q(1,10**7); delta=Q(1,10**50)
A=2000*amp; d=Q(5*10**14)*delta
R=2*(A+d)
assert R<Q(1,2000)
assert 32*R<Q(1,4) and 64*R<Q(1,2)
assert 32*(R+A)<Q(1,2)
assert 2*d==Q(1,10**35)
# Nonzero Fourier source at k=(1,0,0).
kappa_hat=Q(1,65536)
assert 6*eps*kappa_hat-13*delta>Q(1,10**6)
assert 6*Q(70,1229)*kappa_hat-13*delta>Q(1,250000)
# e^5 <149 implies e^40<149^8<10^18.
term=total=Q(1)
for n in range(1,31):
 term*=Q(5,n); total+=term
rem=term*Q(5,31)/(1-Q(5,32))
assert total+rem<149 and 149**8<10**18
assert Q(2,10**35)/Q(1,10**25)==Q(2,10**10)
print("PASS exact seven-ray floor, Fourier-source, explicit H4/contractive parameter margins")
print("REGULAR model only: preassigned singular-source inverse and unforced blowup remain OPEN")
