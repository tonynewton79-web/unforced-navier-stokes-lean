#!/usr/bin/env python3
"""Axis-localization obstruction for pure radial gauge, independently checked."""
import sympy as s
r,z=s.symbols("r z",positive=True,real=True)
k=s.Function("k")(r,z)
divr=s.diff(k,r)+k/r
assert s.simplify(s.diff(divr,z)-(s.diff(k,z,r)+s.diff(k,z)/r))==0
f=r**3*s.exp(-r**2)
g=s.exp(-z**2)
example=s.simplify(s.diff(divr.subs(k,f*g).doit(),z))
assert s.simplify(example-s.diff(g,z)*(s.diff(f,r)+f/r))==0
assert s.simplify(example.subs({r:1,z:1})+4*s.exp(-2))==0
assert s.simplify(s.diff(divr.subs(k,f).doit(),z))==0
R=s.symbols("R",positive=True)
fr=R**2*s.exp(-R**2)
phi=fr+s.integrate(fr/R,R)
assert s.simplify(s.diff(phi,R)-(s.diff(fr,R)+fr/R))==0
print("PASS compact axial modulation produces explicit nonzero curl")
print("PASS radial-only smooth carrier gives gradient divergence")
print("Analytic no-go: curl=0 and compact z-support imply k_r+k/r=0; radial compactness gives k=0")
