#!/usr/bin/env python3
"""Independent generic Cartesian axis-jet angular averaging and Gaussian audit."""
import sympy as s
from fractions import Fraction as F
from random import Random
r,t=s.symbols('r t',real=True)
x=r*s.cos(t);y=r*s.sin(t)
u0,v0,ux,uy,vx,vy,uxx,uxy,uyy,vxx,vxy,vyy,w0,wx,wy=s.symbols('u0 v0 ux uy vx vy uxx uxy uyy vxx vxy vyy w0 wx wy',real=True)
U=u0+ux*x+uy*y+s.Rational(1,2)*uxx*x*x+uxy*x*y+s.Rational(1,2)*uyy*y*y
V=v0+vx*x+vy*y+s.Rational(1,2)*vxx*x*x+vxy*x*y+s.Rational(1,2)*vyy*y*y
W=w0+wx*x+wy*y
ur=s.expand(U*s.cos(t)+V*s.sin(t));G=s.expand(x*V-y*U)
avg=lambda a:s.simplify(s.integrate(s.expand_trig(s.expand(a)),(t,0,2*s.pi))/(2*s.pi))
J=s.expand(avg(ur*G)-avg(ur)*avg(G))
K=s.expand(avg(W*G)-avg(W)*avg(G))
J3=s.factor((-2*u0*uxy+u0*vxx-u0*vyy+uxx*v0-uyy*v0+2*v0*vxy)/8)
K2=s.factor((v0*wx-u0*wy)/2)
assert s.simplify(J.coeff(r,3)-J3)==0
assert s.simplify(J.coeff(r,2))==0 and s.simplify(J.coeff(r,1))==0
assert s.simplify(K.coeff(r,2)-K2)==0 and s.simplify(K.coeff(r,1))==0
assert not any(a in J3.free_symbols for a in (ux,uy,vx,vy))
X,Y,Z,eps=s.symbols('X Y Z eps',real=True)
pot=eps*s.exp(-X*X-Y*Y-Z*Z)*(X+(X*X+Y*Y)*Y)
aU=s.diff(pot,Y);aV=-s.diff(pot,X)
subs={u0:aU.subs({X:0,Y:0}),v0:aV.subs({X:0,Y:0}),
uxx:s.diff(aU,X,2).subs({X:0,Y:0}),uxy:s.diff(aU,X,Y).subs({X:0,Y:0}),
uyy:s.diff(aU,Y,2).subs({X:0,Y:0}),vxx:s.diff(aV,X,2).subs({X:0,Y:0}),
vxy:s.diff(aV,X,Y).subs({X:0,Y:0}),vyy:s.diff(aV,Y,2).subs({X:0,Y:0})}
assert s.simplify(J3.subs(subs)-eps**2*s.exp(-2*Z*Z))==0
rng=Random(20261025)
for _ in range(20000):
    a,b,c,g,e,f,p,q=[F(rng.randrange(-40,41),rng.randrange(1,17)) for _ in range(8)]
    J3q=(a*(p-q-2*g)+b*(e-f+2*c))/8
    assert 8*J3q==a*(p-q-2*g)+b*(e-f+2*c)
print("PASS generic axial J3, K2, exact first-derivative cancellation, Gaussian J3")
print("PASS 20000 independent Fraction axis-jet identities")
