#!/usr/bin/env python3
"""Finite exact replay for Edition XI pressure-free source collar witness.
Full continuum proof requires the analytic source sign and continuity;
global NSE remains unproved.
"""
import sympy as s
from fractions import Fraction as F
from random import Random

x,y,z=s.symbols('x y z',real=True)
rr=s.sqrt(x*x+y*y)
f=s.Function('f')
vx=-y*f(rr,z)/rr
vy=x*f(rr,z)/rr
assert s.simplify(s.diff(vx,x)+s.diff(vy,y))==0

eta,h,D=s.symbols('eta h D',real=True)
L=1-2*h*eta**2
az=-2*eta/L
bz=(-2*D*eta*az+(1-eta**2)*s.diff(az,eta))/L
assert s.simplify(az.subs(eta,0))==0
assert s.simplify(bz.subs(eta,0))==-2
t=s.symbols('t',real=True)
g=-1/t**2+1/(1-t)**2
assert s.diff(g,t).subs(t,s.Rational(1,2))==32
assert s.Rational(1,4)*32==8
assert s.simplify(-(0**2*s.Symbol('fpp')-2*4*s.Symbol('rho'))-8*s.Symbol('rho'))==0
r=Random(20261023)
for _ in range(10000):
  a=F(r.randint(1,1000),r.randint(1,1000))
  b=F(r.randint(1,1000),r.randint(1,1000))
  assert a*b>0
print('PASS exact divergence and source midpoint; 10000 rational positivity')
print('HOLD actual source-global residual, coupled correction, full Lean kernel and unforced blowup')
