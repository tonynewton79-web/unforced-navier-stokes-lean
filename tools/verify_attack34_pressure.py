#!/usr/bin/env python3
"""Finite exact replay for Attack34 quadratic pressure composite.

The infinite-index theorem is proved mathematically in the note. This
checker does not prove that theorem in Lean or complete Navier--Stokes G1.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial
import sympy as s

h=s.Rational(1,200)
eta,X=s.symbols("eta X")
D=s.Rational(1,2)-h
L=1-2*h*eta**2
d=1-eta**2
a=2*eta/L; b=-2*eta/L; c=-d/L
alpha=4*h*eta/L; beta=d/L; gamma=-2*eta/L
for j in (1,2,3,7):
    mu=D+2*h*j
    for p in (j,j+1,j+4):
        U=X**p*(1+eta+s.Rational(2,5)*eta**2)
        AU=U/(p+1)
        V=X*(a*U+b*mu*AU+c*s.diff(AU,eta))
        actual=j*alpha*V+beta*s.diff(V,eta)+gamma*X*s.diff(V,X)
        normal=X*((j*alpha*a+beta*s.diff(a,eta)+gamma*a+gamma*b*mu)*U
            +gamma*a*X*s.diff(U,X)
            +(beta*a+gamma*c)*s.diff(U,eta)
            +mu*(j*alpha*b+beta*s.diff(b,eta))*AU
            +(j*alpha*c+beta*b*mu+beta*s.diff(c,eta))*s.diff(AU,eta)
            +beta*c*s.diff(AU,eta,2))
        assert s.cancel(actual-normal)==0

@lru_cache(None)
def w(j,q):
    return Q(factorial(2*j+q),factorial(2*j)*(j+1)**2*(q+1)**2)

count=0
for i in range(1,13):
 for j in range(1,13):
  m=i+j
  for u in range(4):
   for v in range(4-u):
    k=u+v
    for beta_idx in (0,1,2,3,5,9,13,20):
     raw=sum((Q(comb(beta_idx,t))*w(i,t+u)*w(j,beta_idx-t+v)
           for t in range(beta_idx+1)),Q(0))
     cap=Q(176)*9*4**k*(m+1)**k*w(m+2,beta_idx)
     assert raw<=cap,(i,j,u,v,beta_idx)
     count+=1
assert count==11520

kernel_count=0
for i in range(1,300):
 for j in range(1,300):
  m=i+j
  for u in (0,1):
   for v in (0,1):
    assert Q((m+1)**(u+v+1),(m+2)**2*(i+1)**u*(j+1)**v)<=1
    kernel_count+=1
  for k,coef in ((0,m+1),(0,j),(1,1),(2,Q(1,j+1))):
   assert Q((m+1)**(k+1),(m+1)*(m+2)**2)*coef<=1
   kernel_count+=1
assert kernel_count==715208
print("PASS: 12 six-term source identity checks")
print("PASS: 11,520 split-derivative exact ratios")
print("PASS: 715,208 source-graded radial kernels")
print("G1 FULL CONVERGENCE AND GLOBAL UNFORCED NS: OPEN")
