#!/usr/bin/env python3
"""Attack38 finite exact source-moment and axis-selector verification.
This is not a full source-parameter, G1 convergence or Navier-Stokes PDE certificate.
"""
import sympy as s
from fractions import Fraction as F
eta,theta=s.symbols("eta theta",real=True)
f=(1+eta**2)**(-2*theta)
for m in range(5):
    jet=(-1)**m*s.factorial(2*m)*s.rf(2*theta,m)/s.factorial(m)
    assert s.simplify(s.diff(f,eta,2*m).subs(eta,0)-jet)==0

assert F(128,225)==F(1,2)*F(16,15)**2
e2=F(1,6400)
positive=F(10)/(1+e2)**2
negative=F(1,2)/(1-e2)*(1+e2/(1-e2))
assert positive-negative>9
assert 4+F(1,2)/F(6399,6400)<5
Umax=F(81,20)
bound=F(51,100)*((2*Umax+8)*Umax+4*(1+2*Umax))
bound+=4*(F(1,2)+2*Umax+4)
assert bound<103
assert 4+14+4*F(51,100)/2+4*F(51,100)*2<24
assert F(4)+F(49,100)-F(1,20)-3>1
assert F(49,100)-F(201,10000)*F(409,100)>F(2,5)
assert F(400,401)>F(99,100)
for k in range(150):
    assert F((k+1)**2,4**k)<=1
    assert F((k+1)**3,4**k)<=2
I=s.symbols("I",positive=True)
assert s.simplify(s.Rational(1,10)-
    (103+24*I)/(10*(104+24*I))-
    1/(10*(104+24*I)))==0
h,I0,I1=s.symbols("h I0 I1",positive=True)
jet=(1+2*h)*(-I0/2)-I1-12
assert s.simplify(jet+12+(s.Rational(1,2)+h)*I0+I1)==0
print("PASS: source pressure Taylor moments, global strip Cauchy margin")
print("PASS: axis root positivity, explicit sigma selector B.2, shared multiplier ratio")
print("WARNING: full exterior schedule, radial leading profile, all G1 startup and PDE remain OPEN")
