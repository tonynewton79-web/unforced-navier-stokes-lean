#!/usr/bin/env python3
"""Attack 33: source-composed inverse ratio gates and exact quadratic pressure.

Finite exact arithmetic / symbolic regression ONLY; not an infinite-dimensional
Banach or PDE/Lean certificate. The proofs are in the scholarly note.
"""
from fractions import Fraction as Q
import sympy as sp

checks=0
for j in range(48):
    for beta in range(111):
        sh=Q((j+2)**2*(2*j+1)*(2*j+2),(j+1)**2*(2*j+beta+1)*(2*j+beta+2))
        eta1=sh*Q((2*j+beta+1)*(beta+1)**2,(beta+2)**2)
        eta2=eta1*Q((2*j+beta+2)*(beta+2)**2,(beta+3)**2)
        for nu in (1,2):
            den=(j+1)*(j+nu)
            assert sh/den <= Q(4,(j+1)**2)
            assert j*sh/den <= Q(4,j+1)
            assert eta1/den <= Q(8,j+1)
            assert eta2/den <= Q(16)
            checks+=4
        assert sh<=4
        assert sh/(j+1)<=Q(4,j+1)
        assert eta1/(j+1)<=8
        checks+=3
assert checks==58608

X,z=sp.symbols("X z")
h=sp.Rational(1,200)
L=1-2*h*z*z;d=1-z*z
U={1:X*(1+z*z),2:X**2*(z-1)}
V={1:X**2*(1+z),2:X**3*(z*z+2)}
def Z(k,f):
    return (4*h*k*z*f + d*sp.diff(f,z)-2*z*X*sp.diff(f,X))/L

pairs=((1,2),(2,1))
Omega=sum(V[i]*(sp.diff(V[j],X)-V[j]/(2*X))+U[i]*Z(j,V[j]) for i,j in pairs)
S=sum(V[i]*V[j] for i,j in pairs)
T=sum(U[i]*Z(j,V[j]) for i,j in pairs)
assert sp.cancel(Omega-(sp.diff(S,X)-S/X)/2-T)==0
assert sp.cancel(X*sp.diff(T,X)-4*T)==0
Pi=-S/(4*X)-T/8
assert sp.cancel(sp.diff(Pi,X)+Omega/(2*X))==0
assert sp.limit(Pi,X,0)==0
print("PASS_ATTACK33",checks,"rational operator ratio cases; quadratic source and pressure identities exact")
print("FULL G1 bilinear, authentic H8, unforced Navier-Stokes blow-up: OPEN")
