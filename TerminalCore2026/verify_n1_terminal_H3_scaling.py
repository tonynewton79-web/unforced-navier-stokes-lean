#!/usr/bin/env python3
"""Edition XV exact anisotropic H3 scaling, model Gaussian integrals.
The actual source projected-residual H3 bound and unforced blowup remain HOLD.
"""
import sympy as s
from fractions import Fraction as Q
from random import Random
h,x=s.symbols('h x',positive=True,real=True)
D=s.Rational(1,2)-h
A=s.Rational(1,2)+h
vol=1+D
alpha=s.factor(A+s.Rational(3,2)-vol/2)
beta=s.factor(2*A+s.Rational(1,2)+s.Rational(3,2)-vol/2)
assert alpha==s.Rational(5,4)+3*h/2
assert beta==s.Rational(9,4)+5*h/2
assert s.simplify((1+D)-2*A)==s.Rational(1,2)-3*h
assert s.simplify(s.Rational(1,2)-alpha)==-s.Rational(3,4)-3*h/2
assert s.simplify(2*alpha)==s.Rational(5,2)+3*h
assert s.simplify(beta-alpha)==1+h
def check_gaussian(a,expected):
    P=s.simplify(s.exp(a*x*x)*s.diff(x*s.exp(-a*x*x),x,3))
    sigma2=s.Rational(1,4)/a
    E=s.factor(sum(coef*(s.factorial2(k-1)*sigma2**(k//2) if k else 1)
                  for (k,),coef in s.Poly(s.expand(P*P),x).terms()))
    assert E==expected
check_gaussian(1,s.Rational(105,4))
check_gaussian(2,s.Integer(105))
rng=Random(20261023)
for _ in range(10000):
    hv=Q(rng.randrange(1,100),rng.randrange(10100,10500))
    aa=Q(1,2)+hv; dd=Q(1,2)-hv
    al=aa+Q(3,2)-(1+dd)/2
    be=2*aa+Q(1,2)+Q(3,2)-(1+dd)/2
    assert al==Q(5,4)+Q(3,2)*hv and be==Q(9,4)+Q(5,2)*hv
    assert al>Q(1,2) and be>Q(3,2)
    assert 2*al==Q(5,2)+3*hv
print("PASS exact source-characteristic exponent algebra")
print("PASS Gaussian Cartesian radial third-derivative constants 105/4 and 105")
print("PASS 10000/10000 exact rational h controls")
print("HOLD authentic corrected source H3, projected residual and full Lean PDE")
