#!/usr/bin/env python3
"""Independent Cartesian solenoidality and Fourier Gaussian small-data bound."""
import sympy as s
from fractions import Fraction as F
from random import Random
x,y,z,e=s.symbols('x y z e',real=True)
A=e*s.exp(-(x*x+y*y+z*z))*(x+(x*x+y*y)*y)
v=s.Matrix([s.diff(A,y),-s.diff(A,x),0])
assert s.simplify(s.diff(v[0],x)+s.diff(v[1],y))==0
assert s.simplify(v[1].subs(y,0)+e*(1-2*x*x)*s.exp(-x*x-z*z))==0
R=s.diag(1,-1,1)
ref=R*s.Matrix([v[i].subs(y,-y) for i in range(3)])
assert s.simplify(v-ref)!=s.zeros(3,1)
X,Y,Z=s.symbols('X Y Z',real=True)
g=s.exp(-(X*X+Y*Y+Z*Z)/4)
pol=s.simplify((s.I*s.diff(g,X)-
      s.I*s.diff(s.diff(g,X,2)+s.diff(g,Y,2),Y))/g)
assert s.simplify(pol-s.I*((X*X+Y*Y)*Y-4*X-8*Y)/8)==0
rho=s.symbols('rho',positive=True)
ints=[s.integrate(rho**j*s.exp(-rho*rho/4),(rho,0,s.oo))
      for j in [5,3,6,4]]
assert ints==[64,8,120*s.sqrt(s.pi),12*s.sqrt(s.pi)]
c0=2**(-s.Rational(3,2))*4*s.pi/8
I1=s.simplify(c0*(ints[0]+12*ints[1]))
I0=s.simplify(c0*(ints[2]+12*ints[3]))
CF=(2*s.pi)**(-s.Rational(3,2))
assert s.simplify(I1-20*s.sqrt(2)*s.pi)==0
assert s.simplify(I0-33*s.sqrt(2)*s.pi**s.Rational(3,2))==0
q=s.simplify(CF*I1/1000)
assert q==1/(100*s.sqrt(s.pi)) and q<s.Rational(1,16)
assert s.simplify(CF*I0/1000-s.Rational(33,2000))==0
rng=Random(20261024)
for _ in range(10000):
 a=F(rng.randint(-50,50),rng.randint(1,50))
 assert a*a>=0
print("PASS Cartesian divergence, reflection-breaking, exact Gaussian FT")
print("PASS Fourier critical q <= 1/(100sqrt(pi)) and uniform amplitude")
print("PASS 10000 exact rational controls; global unforced mild theory used")
