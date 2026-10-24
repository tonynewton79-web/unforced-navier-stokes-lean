#!/usr/bin/env python3
"""Sharp affine 7/8 H8 virtual-work inequality, exact fractions."""
from fractions import Fraction as F
t=F(1,4)
rays=[(F(1),F(0),F(0)),(F(1),t,F(0)),(F(1),-t,F(0)),
      (F(1),F(0),t),(F(1),F(0),-t),
      (F(1),t,t),(F(1),t,-t)]
v=[x*x+y*y-2*z*z for x,y,z in rays]
assert v==[F(1),F(17,16),F(17,16),F(7,8),
           F(7,8),F(15,16),F(15,16)]
assert min(v)==F(7,8)
for k in range(7):
    coeff=[F(0)]*7
    coeff[k]=F(1)
    assert sum((coeff[j]*v[j] for j in range(7)),F(0))>=F(7,8)
print("PASS: exact affine virtual-work factors and sharp minimum 7/8")
print("Necessity: integral(Qxx+Qyy-2Qzz) >= 7/8 integral(sum ray coefficients)")
print("This whole-space compact-support gate does not apply to periodic axial test fields.")
