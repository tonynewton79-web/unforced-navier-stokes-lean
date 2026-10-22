#!/usr/bin/env python3
"""A.11/A.19 finite-dimensional exact controls: source/PDE HOLD."""
from fractions import Fraction as Q
from random import Random
import sympy as s
u,v,w,x,z,q1,q2,A,D=s.symbols("u v w x z q1 q2 A D")
k2,k1,k0=s.symbols("k2 k1 k0")
R1=u*(q1+x*q2)-D
R2=2*v*(q1+z*q2)+w*(q1**2+z*q2**2)
R3=k2*A**2+k1*A+k0
J=s.Matrix([R1,R2,R3]).jacobian([q1,q2,A])
assert s.expand(J.det()-2*u*(z*(v+w*q2)-x*(v+w*q1))*(2*k2*A+k1))==0
assert s.expand((2*k2*A+k1)**2-(k1**2-4*k2*k0)-4*k2*R3)==0
V1,V2,W1,W2,E2=s.symbols("V1 V2 W1 W2 E2")
G=E2*(2*V1*q1+2*V2*q2+W1*q1**2+W2*q2**2)
assert s.expand(G.subs({V1:v,V2:z*v,W1:w,W2:z*w})-E2*R2)==0
eta=s.symbols("eta")
Amp=s.Function("Amp")(eta)
K2,K1,K0=[s.Function(t)(eta) for t in ["K2","K1","K0"]]
poly=K2*Amp**2+K1*Amp+K0
exp=(2*K2*Amp+K1)*s.diff(Amp,eta)+s.diff(K2,eta)*Amp**2+s.diff(K1,eta)*Amp+s.diff(K0,eta)
assert s.expand(s.diff(poly,eta)-exp)==0
bad={u:1,v:1,w:20,x:7,z:s.Rational(1,8),q1:s.Rational(1,10),q2:0,D:s.Rational(1,10),A:1,k2:1,k1:0,k0:-1}
assert R1.subs(bad)==0 and R3.subs(bad)==0 and R2.subs(bad)==s.Rational(2,5)
good={**bad,q1:0,D:0}
assert R1.subs(good)==R2.subs(good)==R3.subs(good)==0 and J.det().subs(good)!=0
r=Random(20261022)
for _ in range(10000):
    aa=Q(r.randint(1,30),r.randint(2,31))
    kk=Q(r.randint(1,100),r.randint(1,25))
    bb=abs(Q(r.randint(-15,30),r.randint(1,9)))
    cc=-(kk*aa*aa+bb*aa)
    assert cc<0 and 2*kk*aa+bb>0
    assert (2*kk*aa+bb)**2==bb**2-4*kk*cc
print("PASS symbolic Jacobian/pressure/total-jet; 10000 rational trials; negative control")
print("SOURCE AND PDE: HOLD")
