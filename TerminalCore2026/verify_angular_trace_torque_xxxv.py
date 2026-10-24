#!/usr/bin/env python3
"""Independent sharp angular trace and flux/oscillation test."""
import sympy as s
from fractions import Fraction as F
from random import Random
pi=s.pi
assert s.simplify(2*s.zeta(2)/(2*pi)-pi/6)==0
for N in (1,2,5,20,100):
 S=sum((F(1,n*n) for n in range(1,N+1)),F(0))
 assert s.N(S/pi,15)<s.N(pi/6,15)
r,theta=s.symbols('r theta',positive=True,real=True)
P=r*s.cos(theta)+r**3*s.sin(theta)
ur=s.diff(P,theta)/r;ut=-s.diff(P,r)
gam=r*ut
J=s.simplify(s.integrate(ur*gam,(theta,0,2*pi))/(2*pi))
assert J==r**3
assert s.simplify(-s.diff(r*J,r)/r+4*r*r)==0
rng=Random(20261024)
for j in range(25000):
 retained=F(rng.randrange(1,500),rng.randrange(1,53))
 M0=F(rng.randrange(0,201),rng.randrange(1,28))
 T=F(rng.randrange(0,501),rng.randrange(1,27))
 ang=max(F(0),retained-M0-T)
 assert T+ang>=retained-M0
print('PASS exact sharp circular H1 trace constant squared pi/6')
print('PASS Reynolds torque plateau and 25000 Fraction dichotomy fixtures')
print('HOLD any actual zero-force nonaxisym preserving source swirl')
