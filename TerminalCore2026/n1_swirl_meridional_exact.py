#!/usr/bin/env python3
"""Edition IX exact algebra checks. NOT a blow-up certificate."""
import sympy as s
r,z,t,nu,A,k,eps=s.symbols('r z t nu A k eps',positive=True,real=True)
U,W=s.symbols('U W',real=True)
assert s.simplify(-((U+W)**2-U**2)/r+(2*U*W+W**2)/r)==0
uu=r*s.exp(-r*r-z*z)
ww=eps*r*z*s.exp(-r*r-z*z)
ff=s.simplify((2*uu*ww+ww*ww)/r)
assert s.simplify(s.diff(ff,z).subs(z,0)-2*eps*r*s.exp(-2*r*r))==0
u0=A*s.sin(k*z)
u=A*s.exp(-nu*k*k*t)*s.sin(k*z)
w=s.simplify(u-u0)
assert s.simplify(s.diff(u,t)-nu*s.diff(u,z,2))==0
assert s.simplify(s.diff(w,t)-nu*s.diff(w,z,2)-nu*s.diff(u0,z,2))==0
assert s.simplify(s.diff(u0,t)-nu*s.diff(u0,z,2)-nu*k*k*A*s.sin(k*z))==0
print("PASS: cylindrical swirl centrifugal correction")
print("PASS: exact mixed-pressure negative control")
print("PASS: known exact unforced sinusoidal shear positive control")
print("HOLD: source-specific n=1 coupled meridional correction and full unforced PDE")
