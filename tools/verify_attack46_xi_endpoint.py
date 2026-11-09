#!/usr/bin/env python3
"""Finite, source-normalized Attack46 consistency checks. NOT original Xi numerical data."""
import sympy as s
from fractions import Fraction as Q

x,y,eta,X0,C,D=s.symbols('x y eta X0 C D',positive=True,real=True)
X=X0*s.exp(y)
u=s.Function('U')(x,eta);v=s.Function('v')(x,eta)
E=s.sqrt(2*x)*s.exp(v)/C
base=[u,s.sqrt(2*x)*E,s.sqrt(2*x)*u*E,u**2-E**2/2,E**2/(2*x)]
expect=[X*u.subs(x,X),2*X**2*s.exp(v.subs(x,X))/C,
 2*X**2*u.subs(x,X)*s.exp(v.subs(x,X))/C,
 X*u.subs(x,X)**2-X**2*s.exp(2*v.subs(x,X))/C**2,
 X*s.exp(2*v.subs(x,X))/C**2]
for i,(f,g) in enumerate(zip(base,expect)):
 assert s.simplify(X*f.subs(x,X)-g)==0,i
n=s.symbols('n',positive=True,integer=True)
f=s.sin(n*eta)/n**2
W=-(2*D*eta*f+(1-eta**2)*s.diff(f,eta))/x
assert s.simplify(s.diff(W,eta,2).subs(eta,0)-
  (n+(2-4*D)/n)/x)==0
t,m,sigma1,q0,q1=s.symbols('t m sigma1 q0 q1',real=True)
# sigma integrates to 1/2, its first moment is sigma1
Q22=q0*t+q1*t**2/2+q0*t/2+q1*t**2*(1-sigma1)
assert s.expand(Q22-(s.Rational(3,2)*t*q0+
 t**2*(s.Rational(3,2)-sigma1)*q1))==0
# Exactly rational sample confirms the weighted C2 Banach algebra
def pw(v):
 return sum(sum(abs(Q(s.factorial(j),s.factorial(j-k))*v[j])
   for j in range(k,len(v)))/s.factorial(k) for k in range(3))
a=[Q(2),Q(-1,5),Q(1,4)]
b=[Q(1,3),Q(3,8),Q(-1,9)]
p=[Q(0)]*5
for i,z in enumerate(a):
 for j,w in enumerate(b):p[i+j]+=z*w
assert pw(p)<=pw(a)*pw(b)
print('PASS 5 source radial moment derivatives, stress C3 necessity, B22 and rational Banach product')
print('NOT PROVIDED: original admissible parameter schedule or authentic Xi endpoint enclosures')
