#!/usr/bin/env python3
"""Independent exact audit of m=+1/-1 cylindrical coupling.
Not a true source-corrected unforced Navier-Stokes solution.
"""
from fractions import Fraction as F
from random import Random
import sympy as s

r,z,m=s.symbols("r z m", positive=True, real=True)
I=s.I
U=s.Function("U")(r,z)
a=s.Function("a")(r,z)
b=s.Function("b")(r,z)
c=s.Function("c")(r,z)

def divergence(x,y,v):
    return s.diff(x,r)+x/r+I*m*y/r+s.diff(v,z)

Cr=I*m*U*a/r-2*U*b/r
Ct=I*m*U*b/r+(s.diff(U,r)+U/r)*a+s.diff(U,z)*c
Cz=I*m*U*c/r
pressure_check=s.expand(
    divergence(Cr,Ct,Cz)
    -(2*I*m/r)*(s.diff(U,r)*a+s.diff(U,z)*c)
    +(2/r)*s.diff(U*b,r)
    -(I*m*U/r)*divergence(a,b,c))
assert s.simplify(pressure_check)==0

lam=s.symbols("lam", real=True)
f=s.exp(-r**2)
A=f*s.cos(z)
B=I*A+lam*r**2*f*s.cos(z)
C=-s.diff(f,r)*s.sin(z)-I*lam*r*f*s.sin(z)
assert s.simplify(divergence(A,B,C).subs(m,1))==0

Qrt=s.simplify(A*s.conjugate(B)+s.conjugate(A)*B)
Qzt=s.simplify(C*s.conjugate(B)+s.conjugate(C)*B)
g=s.simplify(s.diff(r*r*Qrt,r)/r**2+s.diff(Qzt,z))
expected=2*lam*r*s.exp(-2*r*r)*(2-2*r*r+s.cos(2*z))
assert s.trigsimp(s.simplify(g-expected))==0
slice_torque=s.simplify(s.integrate(r*r*g,(r,0,s.oo)))
assert s.simplify(slice_torque-lam*s.cos(2*z)/4)==0
assert s.simplify(s.integrate(slice_torque,(z,0,2*s.pi)))==0

# Independent real-angle average, not using complex Fourier multiplication.
theta=s.symbols("theta", real=True)
Vr=2*A*s.cos(theta)
Vt=2*(-A*s.sin(theta)+lam*r*r*A*s.cos(theta))
Vz=2*r*f*s.sin(z)*(2*s.cos(theta)+lam*s.sin(theta))
assert s.simplify(s.integrate(Vr*Vt,(theta,0,2*s.pi))/(2*s.pi)-Qrt)==0
assert s.trigsimp(s.simplify(
    s.integrate(Vz*Vt,(theta,0,2*s.pi))/(2*s.pi)-Qzt))==0

# Nonzero curl of the +2 self-convection: pressure cannot absorb it.
Nr=s.simplify(A*s.diff(A,r)+I*B*A/r+C*s.diff(A,z)-B**2/r)
Nt=s.simplify(A*s.diff(B,r)+I*B*B/r+C*s.diff(B,z)+A*B/r)
curl2=s.simplify(s.diff(r*Nt,r)/r-2*I*Nr/r)
assert s.simplify(curl2.subs({lam:1,r:1,z:0}) -
                  2*(-2+5*I)*s.exp(-2))==0

# Independent Cartesian reconstruction; exactly divergence-free.
x,y=s.symbols("x y",real=True)
ff=s.exp(-(x*x+y*y))
Vx=2*ff*s.cos(z)*(1-lam*x*y)
Vy=2*lam*x*x*ff*s.cos(z)
Vzz=(4*x+2*lam*y)*ff*s.sin(z)
assert s.simplify(s.diff(Vx,x)+s.diff(Vy,y)+s.diff(Vzz,z))==0

alpha,beta,gamma,delta=s.symbols("alpha beta gamma delta",real=True)
gram=s.expand(
 (2*(alpha**2+beta**2))*(2*(gamma**2+delta**2))
 -(2*(alpha*gamma+beta*delta))**2
 -4*(alpha*delta-beta*gamma)**2)
assert gram==0
rng=Random(20261024)
for _ in range(12000):
    M=F(rng.randint(1,100),rng.randint(1,40))
    h=F(rng.randint(1,100),rng.randint(1,12))
    f0=F(rng.randint(1,40),rng.randint(1,40))
    correction=M/h-f0
    assert h*(f0+correction)==M
    assert (h*f0>2*M)==(correction < -f0/2)

print("PASS: exact m-mode pressure compatibility and solenoidal fixture")
print("PASS: independent Fourier and real-angle averages, Gaussian torque")
print("PASS: nonzero m=2 curl, independent Cartesian check, Gram identity")
print("PASS: 12000/12000 rational tests; NO physical unforced blowup proof")
