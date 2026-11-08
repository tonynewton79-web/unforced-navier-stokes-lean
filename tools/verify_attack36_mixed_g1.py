#!/usr/bin/env python3
"""Exact finite symbolic/rational checks for Attack 36. NOT a G1 existence proof."""
import sympy as sp
from fractions import Fraction as Q
from math import factorial, comb

h,eta,j0,X=sp.symbols("h eta j0 X",real=True)
D=sp.Rational(1,2)-h; A=sp.Rational(1,2)+h
d=1-eta**2; L=1-2*h*eta**2
za=lambda c,f:(2*c*eta*f+d*sp.diff(f,eta))/L
q=4*eta+j0
assert sp.simplify((-za(-A-D,za(-A,q))/2).subs(eta,0)-A*j0)==0
f0,f1,f2=sp.symbols("f0 f1 f2")
f=f0+f1*eta+f2*eta**2/2
b=-A-sp.Rational(1,2)
assert sp.simplify((-za(b-D,za(b,f))/4).subs(eta,0)-(1+h)*f0/2+f2/4)==0
u=sp.Function("u")(eta)
v1=(2*A*eta*q-d*sp.diff(q,eta))/L
v2=((2-D)*eta*u-d*sp.diff(u,eta)/2)/L
omega=(D*eta*sp.diff(v1,eta)+v1)/L+v1**2/2+q*(d*sp.diff(v1,eta)-2*eta*v1)/L-4*v2
assert sp.simplify(omega.subs(eta,0)-(4+2*A*j0**2+2*sp.diff(u,eta).subs(eta,0)))==0

h=sp.Rational(1,200); A=sp.Rational(1,2)+h; D=sp.Rational(1,2)-h
L=1-2*h*eta**2
for i in (1,2,3):
 for j in (1,2,3):
  F=X**i*(1+eta+eta**2/3)*(1+X+X**2)
  H=X**j*(2-eta+eta**3/7)*(1+2*X)
  V=sum(X**(a+1)/L*(2*eta*c-2*eta*(D+2*h*i)*c/(a+1)-d*sp.diff(c,eta)/(a+1))
       for (a,),c in sp.Poly(F,X).terms())
  Z=(2*(-A+2*h*i)*eta*F+d*sp.diff(F,eta)-2*eta*X*sp.diff(F,X))/L
  assert sp.cancel(sp.diff(V,X)+Z)==0
  assert sp.cancel(V*sp.diff(H,X)-sp.diff(V*H,X)-Z*H)==0

def w(a,b):
 return Q(factorial(2*a+b),factorial(2*a)*(a+1)**2*(b+1)**2)
ratio_count=0
for a in range(50):
 for beta in (0,1,2,3,4,5,10,25,80):
  assert (a+1)*w(a,beta)/w(a,beta+1)<=4
  if a>=1:
   assert w(a,beta+1)/((a+1)*w(a+1,beta))<=8
   assert w(a,beta+2)/((a+1)**2*w(a+1,beta))<=16
  ratio_count+=1
mix_count=0
for a in range(11):
 for j in range(11):
  for beta in range(18):
   src=sum((Q(comb(beta,t))*w(a,t)*w(j,beta-t+1)
           for t in range(beta+1)),Q(0))
   assert src<=176*w(a+j,beta+1)
   mix_count+=1
print("PASS first-order source-normalized axial/swirl/pressure startup jets")
print("PASS 9 nonconstant true incompressibility/transport identities")
print("PASS",ratio_count,"weak-pressure and J1 Z rational weights")
print("PASS",mix_count,"strong × weak Leibniz samples")
print("NOTE full analytic hierarchy, authentic startup and unforced NS remain OPEN")
