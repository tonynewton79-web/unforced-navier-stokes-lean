#!/usr/bin/env python3
"""Edition XXXV exact Cartesian no-swirl and nonaxis flux audit."""
import sympy as s
from fractions import Fraction as F
from random import Random
x,y,z,nu=s.symbols('x y z nu',real=True,positive=True)
P=s.exp(-x*x-y*y-z*z)
U=s.Matrix([2*nu*x*z*P,2*nu*y*z*P,2*nu*(1-x*x-y*y)*P])
assert s.simplify(sum(s.diff(U[j],(x,y,z)[j]) for j in range(3)))==0
assert s.simplify(x*U[1]-y*U[0])==0
r,Z=s.symbols('r Z',real=True)
vr=2*nu*r*Z*s.exp(-r*r-Z*Z)
vz=2*nu*(1-r*r)*s.exp(-r*r-Z*Z)
assert s.simplify(s.diff(vr,Z)-s.diff(vz,r)
       -2*nu*r*(5-2*(r*r+Z*Z))*s.exp(-r*r-Z*Z))==0
q=s.symbols('q',positive=True)
assert s.integrate(q**3*s.exp(-q*q/4),(q,0,s.oo))==8
critical=s.simplify((2*s.pi)**(-s.Rational(3,2))*
                     s.sqrt(2)*s.pi**2)
assert critical==s.sqrt(s.pi)/2
assert critical>s.Rational(1,16)
theta=s.symbols('theta',real=True)
AZ=r*s.cos(theta)+r**3*s.sin(theta)
ur=s.diff(AZ,theta)/r
ut=-s.diff(AZ,r)
gam=r*ut
flux=s.simplify(s.integrate(ur*gam,(theta,0,2*s.pi))/(2*s.pi))
assert s.simplify(flux-r**3)==0
assert s.simplify(-s.diff(r*flux,r)/r+4*r*r)==0
rng=Random(20261024)
for j in range(15000):
 a=F(rng.randrange(-10,11),rng.randrange(1,12))
 b=F(rng.randrange(-10,11),rng.randrange(1,12))
 rr=F(rng.randrange(1,21),rng.randrange(1,19))
 assert a*b*rr**3==F(1,2)*((a*rr)*(3*b*rr*rr)-(b*rr**3)*a)
print('PASS Gaussian axisymmetric no-swirl divergence and omega_theta/r')
print('PASS critical norm sqrt(pi)/2 > 1/16')
print('PASS exact nonaxis flux r^3 and torque -4r^2, 15000 Fraction cases')
print('HOLD singularity-preserving unforced nonaxisym solution')
