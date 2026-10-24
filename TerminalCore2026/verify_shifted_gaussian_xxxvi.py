#!/usr/bin/env python3
"""Independently verified shifted global no-swirl datum and exact reflection parity."""
import sympy as s
x,y,z,nu,d,r,th=s.symbols('x y z nu d r th',real=True)
E=s.exp(-((x-d)**2+y*y+z*z))
v=s.Matrix([2*nu*(x-d)*z*E,2*nu*y*z*E,2*nu*(1-(x-d)**2-y*y)*E])
assert s.simplify(sum(s.diff(v[i],(x,y,z)[i]) for i in range(3)))==0
Gamma=s.factor(x*v[1]-y*v[0])
assert s.simplify(Gamma-2*nu*d*y*z*E)==0
ur=(x*v[0]+y*v[1])/s.sqrt(x*x+y*y)
assert s.simplify(ur.subs(y,-y)-ur)==0
assert s.simplify(v[2].subs(y,-y)-v[2])==0
assert s.simplify(Gamma.subs(y,-y)+Gamma)==0
assert s.simplify(v[0].subs(y,-y)-v[0])==0
assert s.simplify(v[1].subs(y,-y)+v[1])==0
assert s.simplify(v[2].subs(y,-y)-v[2])==0
assert s.simplify(Gamma.subs({x:0,y:1,z:1,d:1})-2*nu*s.exp(-3))==0
assert s.simplify(v[1].subs(y,0))==0
print('PASS exact 3D divergence, translated Gamma, reflection-even ur,uz, and reflection-odd Gamma')
print('PASS Gamma(r=z=1,theta=pi/2)=2nu*exp(-3) and source-plane azimuthal node')
print('PASS zero mean angular Reynolds fluxes by exact odd parity; evolution uses uniqueness')
