#!/usr/bin/env python3
"""Exact rational/symbolic audit: weak-in-time terminal velocity obstruction.
Only for Attack49's SOURCE-FIRST DIAGNOSTIC, not the original analytic G1 carrier.
"""
from fractions import Fraction as F
from math import factorial
import sympy as S
h=F(1,200);A=F(1,2)+h;D=F(1,2)-h;beta=F(1,2)-2*h
assert A+D==1 and beta==F(49,100)
# Derivatives of original flat k, via sup_x x^j exp(-x)=j^j exp(-j)
assert sum((F(1,factorial(k)) for k in range(5)),F(0))>F(27,10)
for j,c in [(2,1),(3,2),(4,5)]:
    assert F(j**j,1)*F(10,27)**j<c
assert 2+16+20<40
Ws=128*2; Wxi=16*2; Wss=128**2*40; Wxx=16**2*40
smax=F(1,8);ximax=F(1,16)
assert smax*(smax*Ws/2+F(1,2)*ximax*Wxi)==F(17,8)
assert smax*Ws==32 and smax*Wxi==4
assert 3*Ws+smax*Wss+smax*Wxx==83968
assert 8*(smax*smax/2)*F(1,8)<=F(1,128)
linear=(F(1,20)+F(1,160))*4+F(1,160)*32
assert linear==F(17,40)
part_time=F(39,1024);part_viscous=F(83968,64)
part_linear=linear*F(2,128);part_quadratic=F(36*2,128)
assert part_viscous==1312 and part_linear==F(17,2560) and part_quadratic==F(9,16)
assert part_time+part_viscous+part_linear+part_quadratic<1313
J=F(36501,274877906944)
c0=F(201,4000)*J
assert c0==F(7336701,1099511627776000)
assert c0/1313==F(7336701,1443658767269888000)>F(1,200000000000)
assert (J/20)/1313==F(36501,7218293836349440)>F(1,200000000000)
# Exact arbitrary-component contraction, no axisymmetry imposed on w
r,z=S.symbols('r z',positive=True,real=True)
wr,wt,wz,ut,uz=S.symbols('wr wt wz ut uz',real=True)
W=S.Function('W')(r,z);g=r*W
lin=(uz*wt+ut*wz)*S.diff(g,z)+ut*wr*(S.diff(g,r)-g/r)
quad=wr*wt*(S.diff(g,r)-g/r)+wz*wt*S.diff(g,z)
assert S.simplify(lin-(uz*wt+ut*wz)*r*S.diff(W,z)-ut*wr*r*S.diff(W,r))==0
assert S.simplify(quad-wr*wt*r*S.diff(W,r)-wz*wt*r*S.diff(W,z))==0
print('PASS: all test derivative inequalities and weak time-integration constants')
print('PASS: exact original-source dual coefficient, uniform-h margin, nonlinear toroidal identities')
print('NO original B12 analytic G1/H8 carrier or unforced singular solution is proved')
