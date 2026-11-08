#!/usr/bin/env python3
"""Finite algebra regression for source B.34 -> B.8. Not an actual Xi C2 certificate."""
import sympy as s
from fractions import Fraction as Q
qi,qs,am,as_,aj,g=s.symbols("qi qs am as aj g",positive=True)
p=s.Rational(8,5)
L=(1-(qi/qs)**p)/p
assert s.simplify((qs-qi)*g+(am-qs)*g-(am-qi)*g)==0
assert s.simplify((qs-qi)*g**2+(as_-qs)*g**2-(as_-qi)*g**2)==0
assert s.simplify(qs**p*L+aj-qs**p/p-(aj-qi**p/p))==0
assert s.Rational(3,2)+s.Rational(1,10)+1==s.Rational(8,5)
assert 1+s.Rational(1,5)==s.Rational(6,5)
eta,a,E0,de=s.symbols("eta a E0 de",real=True)
U=4*eta+a*g;E=E0+de
assert s.expand((U*E-4*eta*E0)-4*eta*de-a*g*E)==0
assert s.expand((U**2-E**2/2)-(16*eta**2-E0**2/2)-8*eta*(U-4*eta)-(a*g)**2+(E**2-E0**2)/2)==0
# Uniform source B.33 gives T>60||tau||; all kernel parameters obey 4m/p <= 40.
assert max(Q(4*m,1)/p for p,m in ((Q(8,5),1),(Q(6,5),2),(Q(1,5),2)))==40
# sigma(2/5)<1/5 follows from exp(125/36)>4; e^(125/36)>1+125/36>4.
assert Q(1)+Q(125,36)>4
print("PASS source five-row propagation, separation cancellation and cutoff-length arithmetic")
print("NOT CERTIFIED: original Xi endpoint functions, five nonlinear coefficients, strict cone, G1")
