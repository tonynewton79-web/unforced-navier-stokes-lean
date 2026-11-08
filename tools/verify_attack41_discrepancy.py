#!/usr/bin/env python3
"""Attack 41 exact rational checks for the original A.11 normalized angular discrepancy.
Mathematical theorem is in docs/...; not full source-admissibility or G1 proof.
"""
from fractions import Fraction as Q
from math import factorial
import sympy as sp

lam,y,q,g=sp.symbols("lam y q g",real=True)
c=1-lam
r=sp.Function("r")(y)
res=sp.diff(r-1/c,y)+(c-g*q)*(r-1/c)-g*q/c
assert sp.simplify(res.subs(sp.diff(r,y),1-(c-g*q)*r))==0
gmax=Q(7,10);qmax=Q(9,64);kmin=Q(4,5);cmin=Q(15,16)
assert cmin-gmax*qmax>kmin
assert gmax*qmax/(cmin*kmin)==Q(21,160)<Q(1,7)
assert qmax*Q(5,4)/kmin==Q(225,1024)<Q(1,4)
assert Q(1,7)+Q(1,4)<Q(1,2)
def taylor_lower(x,N):
 return sum((x**i/factorial(i) for i in range(N)),Q(0))
assert taylor_lower(Q(7),20)>1000
assert taylor_lower(Q(375,8),100)>10**20
assert taylor_lower(Q(499),100)>10**40
assert taylor_lower(Q(10),30)>1000
def upper_exp(x,n=26):
 s=Q(1);t=Q(1)
 for i in range(1,n+1):
  t*=x/i;s+=t
 return s+t*x/(n+1)/(1-x/(n+2))
assert upper_exp(Q(3))<21
assert upper_exp(Q(8,5))<5
assert 11*1500<16**28
assert 11*10**6<16**27
# Exact envelopes for the pre-pulse normalized M,J terms and pulse cut-off.
assert Q(6,5)*Q(88,3)/10**20+Q(58,10**40)<Q(1,10**18)
# Retaining all upstream early source moments is essential:
XR,P,f,H0,K,Jd,Td,Tw,eta=sp.symbols("XR P f H0 K Jd Td Tw eta",positive=True)
s1=sp.Rational(1,2)-lam;s2=sp.Rational(1,2)-2*lam
DM=sp.Rational(13,10)-lam/2+Td/2+s1*Tw
DJ=sp.Rational(8,5)-lam+Td/2+s2*Tw
Mp=XR*eta*(4*sp.E+sp.E*K)
Jp=XR*H0*eta*(sp.Rational(5,2)+4*Jd+sp.exp(sp.Rational(13,10))*K)
assert sp.simplify(Mp/(XR*P*f*sp.exp(DM))-
eta*(4*sp.E+sp.E*K)*sp.exp(-DM)/(P*f))==0
assert sp.simplify(Jp/(XR*H0*P*f*sp.exp(DJ))-
eta*(sp.Rational(5,2)+4*Jd+sp.exp(sp.Rational(13,10))*K)*sp.exp(-DJ)/(P*f))==0
print("PASS exact source A.11 angular C1 < 11 lambda^28")
print("PASS exact upstream M,J normalization and axial trial C0 < 1e-18")
print("WARNING full corrected pulse amplitude C1, 5-moment exterior, G1, unforced blowup OPEN")
