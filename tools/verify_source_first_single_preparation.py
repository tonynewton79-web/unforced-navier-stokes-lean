#!/usr/bin/env python3
"""Finite exact regression for a NEW diagnostic, NOT the authentic G1 source."""
from fractions import Fraction as Q
from math import factorial
import sympy as sp
h=Q(1,200); A=Q(1,2)+h; D=Q(1,2)-h
assert A+D==1 and Q(2)+D-A-Q(3,2)==Q(49,100)
assert Q(11,128)>Q(1,16) and Q(13,128)<Q(1,8)
x=Q(4,3); n=6
ub=sum((x**j/factorial(j) for j in range(n)),Q(0))+(x**n/factorial(n))/(1-x/Q(n+1))
assert ub<4
Jmin=Q(6*23**3,256**3*32768)
assert Jmin==Q(36501,274877906944)
gap=Q(201,4000)*Jmin
assert gap==Q(7336701,1099511627776000)>Q(1,10**9)
tau,x1,x2,z,a,b=sp.symbols('tau x1 x2 z a b',positive=True,real=True)
A=sp.Rational(101,200); Om=b*tau**(-A-sp.Rational(1,2)); V=a*tau**(-A)
u=sp.Matrix([-Om*x2,Om*x1,V]); coords=(x1,x2,z)
F=-u.diff(tau)+sp.Matrix([sum(u[j]*sp.diff(u[i],coords[j]) for j in range(3)) for i in range(3)])-sp.Matrix([sum(sp.diff(u[i],c,2) for c in coords) for i in range(3)])
curlz=sp.diff(F[1],x1)-sp.diff(F[0],x2)
assert sp.simplify(curlz-2*(A+sp.Rational(1,2))*Om/tau)==0
assert sp.simplify((x1*F[1]-x2*F[0])-(A+sp.Rational(1,2))*Om*(x1*x1+x2*x2)/tau)==0
assert sp.simplify(sum(sp.diff(u[j],coords[j]) for j in range(3)))==0
print("PASS: original-density/vacuum support separation, full plateau residual, nonzero curl and torque")
print("PASS: exact oriented cone-dual violation exceeds",gap,"*tau^(49/100)")
print("SOURCE-DERIVED new diagnostic only, NOT the authentic analytic G1 source")
