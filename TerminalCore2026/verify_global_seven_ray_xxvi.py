#!/usr/bin/env python3
"""Exact universal seven-ray quotient-cone tests; full unforced NSE is OPEN."""
import random
from fractions import Fraction as F
import sympy as s

qrr,qtt,qzz,qrt,qrz,qtz,A,B,chi=s.symbols(
    "qrr qtt qzz qrt qrz qtz A B chi",real=True)
Q=s.Matrix([[qrr,qrt,qrz],[qrt,qtt,qtz],[qrz,qtz,qzz]])
d=[qrr-16*(qtt+qzz)+(B-29*A)*chi,
   8*qtt+6*A*chi+2*qrt,8*qtt+8*A*chi-2*qrt,
   8*qzz+7*A*chi+2*qrz-8*qtz,
   8*qzz+7*A*chi-2*qrz+8*qtz,
   A*chi+8*qtz,A*chi-8*qtz]
t=s.Rational(1,4)
V=[s.Matrix(v) for v in [(1,0,0),(1,t,0),(1,-t,0),
 (1,0,t),(1,0,-t),(1,t,t),(1,t,-t)]]
S=sum((d[j]*V[j]*V[j].T for j in range(7)),s.zeros(3,3))
assert S.applyfunc(s.expand)==(Q+A*chi*s.eye(3)+B*chi*s.diag(1,0,0)).applyfunc(s.expand)

rng=random.Random(20261024)
for n in range(10000):
    v=[F(rng.randint(-30,30),rng.randint(1,11)) for _ in range(6)]
    M=max(map(abs,v))
    AA=16*M+1
    BB=29*AA+64*M+1
    h=F(1) if n%4 in (0,1) else F(rng.randint(0,9),10)
    if h!=1: v=[F(0)]*6
    rr,tt,zz,rt,rz,tz=v
    dd=[rr-16*(tt+zz)+(BB-29*AA)*h,
        8*tt+6*AA*h+2*rt,8*tt+8*AA*h-2*rt,
        8*zz+7*AA*h+2*rz-8*tz,
        8*zz+7*AA*h-2*rz+8*tz,
        AA*h+8*tz,AA*h-8*tz]
    assert min(dd)>=h
    vv=[tuple(map(F,x)) for x in V]
    actual=[[sum((dd[k]*vv[k][i]*vv[k][j] for k in range(7)),F(0))
             for j in range(3)] for i in range(3)]
    qq=[[rr,rt,rz],[rt,tt,tz],[rz,tz,zz]]
    expect=[[qq[i][j]+(AA*h if i==j else 0)
             +(BB*h if i==j==0 else 0)
             for j in range(3)] for i in range(3)]
    assert actual==expect

# Independent Cartesian check for a nonconstant radial tensor carrier k=r^2.
x,y,z=s.symbols("x y z",real=True)
K=s.Matrix([[x*x,x*y,0],[x*y,y*y,0],[0,0,0]])
divK=s.Matrix([sum(s.diff(K[i,j],(x,y,z)[j]) for j in range(3))
              for i in range(3)])
assert divK==s.Matrix([3*x,3*y,0])
P=s.Rational(3,2)*(x*x+y*y)
assert divK==s.Matrix([s.diff(P,c) for c in (x,y,z)])
print("PASS 6 exact universal tensor identities and 10000/10000 Fraction checks")
print("PASS d_j >= chi including cutoff collar; Cartesian gradient check")
print("HOLD authentic source, bounded H8 gain, nonlinear PDE and final Lean theorem")
