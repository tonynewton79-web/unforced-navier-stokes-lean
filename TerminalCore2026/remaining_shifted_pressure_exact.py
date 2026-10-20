"""Exact-rational checks of the final two shifted-pressure source bounds.

Covers the strong-velocity times shifted-pressure convolution, radial
integration/axial-derivative weights, and exact source integration by parts.
Finite replay supplements, but cannot replace, the all-index paper proof.
"""
from fractions import Fraction as F
from math import factorial, comb
import sympy as s

def w(a,b):
    return F(factorial(b)*comb(2*a+b,b),(a+1)**2*(b+1)**2)
def P(a,b):
    return w(a,b+1)

cases=0
for N in range(24):
    for b in range(35):
        mixed=sum((F(comb(b,u))*w(i,u)*P(N-i,b-u)/P(N,b)
                   for i in range(N+1) for u in range(b+1)),F(0))
        assert mixed<=64,(N,b,mixed)
        cases+=1
print("PASS strong-by-shifted-pressure multiplication",cases)

transfer=0
for a in range(70):
    for b in range(65):
        assert w(a,b)/P(a,b)<=4
        assert P(a,b)/P(a+1,b)<=4
        assert P(a,b+1)/((a+1)*P(a+1,b))<=8
        assert P(a,b)/((a+1)*P(a+1,b))<=F(4,a+1)
        assert w(a,b)/P(a+1,b)<=F(16,3)
        assert w(a,b+1)/P(a+1,b)<=4
        assert w(a,b+2)/((a+1)*P(a+1,b))<=8
        transfer+=7
print("PASS radial lifts, shifted jets and pressure primitives",transfer)

ordered=0
for i in range(1,19):
 for j in range(1,19):
  for a in (i,i+1,i+8):
   for b in (j,j+2,j+9):
    lam=F(j,50)
    assert a+lam<=a+b+1
    assert (a+1)*(b+1)>=a+b+1
    ordered+=2
print("PASS ordered quadratic transport and double-average gates",ordered)

X,eta=s.symbols('X eta')
h=s.Rational(1,200)
L=1-2*h*eta*eta
B=2*eta/L
G=(1-eta*eta)/L
D=s.Rational(1,2)-h
DX=lambda f:X*s.diff(f,X)
identities=0
for k in (1,2,4):
 for a in (k,k+1):
  for c in (0,2):
   v=X**c*(2+eta)
   u=X**c*(3+eta**2)
   f=X**a*(1+eta+eta**2)
   lam=2*h*k
   W=X**a*(B*(1-(D+lam)/(a+1))*(1+eta+eta**2)
             -G*(1+2*eta)/(a+1))
   K0=G*s.diff(v,eta)-B*(v+DX(v))
   source=u*(G*s.diff(W,eta)+B*((lam-1)*W-DX(W)))
   original=X*v*W+s.integrate(source+f*K0,(X,0,X))
   integrated=X*(v-B*u)*W+s.integrate(
       u*G*s.diff(W,eta)+B*(lam*u+DX(u))*W+f*K0,(X,0,X))
   assert s.cancel(original-integrated)==0
   identities+=1
for i,j in ((1,1),(2,1),(1,3),(3,2),(5,4)):
 u=X**i*(2+eta)
 W=X**j*(1+eta+eta**2)
 lam=2*h*j
 before=s.integrate(u*(G*s.diff(W,eta)+B*((lam-1)*W-DX(W))),
                    (X,0,X))
 after=-X*B*u*W+s.integrate(
     u*G*s.diff(W,eta)+B*(lam*u+DX(u))*W,(X,0,X))
 assert s.cancel(before-after)==0
 identities+=1
print("PASS exact leading and ordered quadratic pressure source identities",
      identities)
print("PASS TOTAL",cases+transfer+ordered+identities,"finite checks")
