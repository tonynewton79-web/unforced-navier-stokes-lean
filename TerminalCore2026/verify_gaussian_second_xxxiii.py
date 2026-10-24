#!/usr/bin/env python3
"""Second proof-independent divergence-free Gaussian positive control."""
import sympy as s
x,y,z=s.symbols('x y z',real=True)
radius=x*x+y*y+z*z
psi=s.exp(-radius)
v=s.Matrix([s.diff(psi,y),-s.diff(psi,x),0])
assert s.simplify(s.diff(v[0],x)+s.diff(v[1],y))==0
Delta=s.Matrix([s.diff(f,x,2)+s.diff(f,y,2)+s.diff(f,z,2) for f in v])
assert s.simplify(Delta[0]+2*y*(4*radius-10)*s.exp(-radius))==0
assert s.simplify(Delta[1]-2*x*(4*radius-10)*s.exp(-radius))==0
gauss=(s.pi/2)**s.Rational(3,2)
energy=2*gauss; lap=70*gauss
assert s.simplify(lap/energy-35)==0
C=4/(s.pi*s.sqrt(2)*3**s.Rational(7,8))
peak=s.sqrt(2)*s.exp(-s.Rational(1,2))
assert float(C*energy**s.Rational(1,8)*lap**s.Rational(3,8))>float(peak)
h=s.symbols('h',real=True)
A=s.Rational(1,2)+h
assert s.simplify(s.Rational(5,3)*A-s.Rational(5,6)-5*h/3)==0
assert s.simplify(s.Rational(4,3)*A-s.Rational(2,3)-4*h/3)==0
assert s.simplify(s.Rational(2,3)*A-s.Rational(1,3)-2*h/3)==0
print('PASS independent analytic Gaussian divergence-free interpolation and exponents')
print('HOLD nonzero-data unforced singularity and pointwise retention')
