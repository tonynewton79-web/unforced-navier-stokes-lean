#!/usr/bin/env python3
"""Edition XXXI exact symbolic source-shell and unforced-correction controls.
This does not supply the missing actual source constants.
"""
from fractions import Fraction as Q
from random import Random
import sympy as s
V,R,m,G,L,H,K,nu,T=s.symbols("V R m G L H K nu T",positive=True)
r=s.symbols("r",positive=True)
small=s.simplify((2*s.pi)**-3*R**2*V*m**2*
                 4*s.pi*s.integrate(r**4,(r,0,L)))
assert s.simplify(small-R**2*V*m**2*L**5/(10*s.pi**2))==0
L0=(5*s.pi**2/(4*R**2*V))**s.Rational(1,5)
assert s.simplify((small/m**2).subs(L,L0)-s.Rational(1,8))==0
assert s.simplify((G**2/H**2).subs(H,4*G/m)/m**2-s.Rational(1,16))==0
assert 1-s.Rational(1,8)-s.Rational(1,16)==s.Rational(13,16)
integral=s.integrate(4*s.pi,(r,K,2*K))
assert s.simplify(integral-4*s.pi*K)==0
ck=s.simplify((2*s.pi)**(-s.Rational(3,2))*s.sqrt(integral)/nu)
assert s.simplify(ck-s.sqrt(K)/(s.sqrt(2)*s.pi*nu))==0
x,F,Fk,U,A=s.symbols("x F Fk U A",nonnegative=True)
d=s.exp(A); ak=s.exp(-nu*K**2*T)
W=d*(x+F)
rhs=2*ak*x+ck*x**2+Fk+ck*(2*U*W+W**2)
alpha=ck*(1+d**2); beta=2*ak+2*ck*U*d+2*ck*d*d*F
gamma=Fk+ck*(2*U*d*F+d*d*F*F)
assert s.simplify(rhs-(alpha*x*x+beta*x+gamma))==0
theta=s.symbols("theta",real=True)
assert s.integrate(s.sin(theta),(theta,0,2*s.pi))==0
assert s.integrate(s.cos(theta),(theta,0,2*s.pi))==0
rng=Random(20261024)
for j in range(25000):
  e=Q(rng.randrange(1,300),rng.randrange(1,50))
  low=Q(rng.randrange(2),8)*e
  high=Q(rng.randrange(2),16)*e
  middle=e-low-high
  N=rng.randrange(1,60)
  assert middle>=Q(13,16)*e
  assert middle/N>=Q(13,16)*e/N
print("PASS exact zero mean angular factor, Fourier cutoffs 1/8,1/16,13/16")
print("PASS independent Duhamel R3 shell constant and correction quadratic")
print("PASS 25000 exact rational partitions")
print("HOLD actual r0,z0,e0,m,G,full physical force and retention constants")
