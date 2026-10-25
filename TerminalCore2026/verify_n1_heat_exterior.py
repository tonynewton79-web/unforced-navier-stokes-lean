#!/usr/bin/env python3
"""Finite independent controls for exterior gamma-mixture IBP heat identity.

Not a global or Lean-certified Navier-Stokes proof.
"""
from fractions import Fraction as Q
import mpmath as mp

count=0
for h in [Q(1,200), Q(1,17), Q(3,8)]:
    for ri in [1,2,3,5,13]:
        for v in [Q(1,4),Q(3,2),Q(11,3)]:
            R=Q(ri); S=R**2+4*v
            lhs=4*h*(R**2*(1+h-v)-4*v*v)/S**2
            rhs=4*h*((1+h-v)/S-4*(h+1)*v/S**2)
            assert lhs==rhs,(h,ri,v)
            count+=1
assert count==45
print("exact rational integration-by-parts coefficient identities:",count,"PASS")

mp.mp.dps=45
for htxt,Rtxt in [('0.005','2'),('0.005','4'),('0.09','5'),('0.5','3')]:
    h,R=mp.mpf(htxt),mp.mpf(Rtxt)
    A=mp.mpf('.5')+h
    f=lambda x: mp.quad(
        lambda v: mp.exp(-v)*v**h*(x*x+4*v)**(-h),
        [0,mp.inf]
    )/(mp.gamma(1+h)*x)
    defect=mp.diff(f,R,2)+mp.diff(f,R)/R-f(R)/R**2 - A*f(R)-R*mp.diff(f,R)/2
    assert abs(defect)<mp.mpf('1e-35'),(h,R,defect)
    print("h",h,"R",R,"relative heat ODE defect",mp.nstr(defect/f(R),10))

print("FINITE_HEAT_EXTERIOR_PASS; global smoothness and force-free gluing OPEN")
