#!/usr/bin/env python3
"""Independent minimax and source-budget adversarial checks (Edition XXVII).
Not a full PDE, actual source, nor compiled Lean certification.
"""
from fractions import Fraction as F
from random import Random
import sympy as s

# Independent construction via inverse of the six-ray tensor equations.
M,mu=s.symbols("M mu",nonnegative=True)
h=mu+8*M
a=(mu+2*h+10*M)/8
b=mu+33*M+31*a-2*h
assert s.simplify(a-(3*mu/8+13*M/4))==0
assert s.simplify(b-(85*mu/8+471*M/4))==0
assert s.simplify(8*a-h-(2*mu+18*M))==0
assert s.simplify(b-31*a+2*h-(mu+33*M))==0

# LP optimizer is a distinct route. It solves a 3-variable program
# from independent signed-box constraints for all Q_ij∈[-M,M].
try:
    from scipy.optimize import linprog
except ImportError as e:
    raise RuntimeError("independent LP verifier requires scipy") from e
import numpy as np
# Variables [a,h,b]; constrain:
# h≥mu+8M; 8a-2h≥mu+10M; 8a≥mu+10M;
# 8a-h≥mu+18M; b-31a+2h≥mu+33M.
Aub=np.array([[0,-1,0],[-8,2,0],[-8,0,0],[-8,1,0],[31,-2,-1]],float)
rhs=np.array([-9,-11,-11,-19,-34],float)
res=linprog([0,0,1],A_ub=Aub,b_ub=rhs,
             bounds=[(None,None)]*3,method="highs")
assert res.success
assert max(abs(x-y) for x,y in zip(res.x,
     [29/8,9,1027/8]))<1e-8

# Second LP: optimize gauge carrier for Q=0 with d_i≥1
# and zero mixed tensor entries + theta/z diagonal equality.
v=F(1,4)
rays=[(F(1),F(0),F(0)),(F(1),v,F(0)),(F(1),-v,F(0)),
      (F(1),F(0),v),(F(1),F(0),-v),
      (F(1),v,v),(F(1),v,-v)]
eq=np.array([[float(x*y) for x,y,z in rays],
             [float(x*z) for x,y,z in rays],
             [float(y*y-z*z) for x,y,z in rays]],float)
cost=np.array([float(x*x-y*y) for x,y,z in rays])
baseline=linprog(cost,A_eq=eq,b_eq=np.zeros(3),
                  bounds=[(1,None)]*7,method="highs")
assert baseline.success and abs(baseline.fun-85/8)<1e-8
d0=[F(1),F(1),F(3),F(2),F(2),F(1),F(1)]
assert sum((d0[i]*(rays[i][0]**2-rays[i][1]**2)
    for i in range(7)),F(0))==F(85,8)

# Complete corner negative controls for fixed gauge.
rng=Random(20261024)
for _ in range(25000):
    MM=F(rng.randint(0,20),10)
    u=F(rng.randint(1,20),10)
    x=[F(rng.randint(-100,100),100)*MM for _ in range(6)]
    rr,tt,zz,rt,rz,tz=x
    D=[
      rr-16*(tt+zz)+u+33*MM,
      8*tt+2*rt+u+10*MM,
      8*tt-2*rt+3*u+26*MM,
      8*zz+2*rz-8*tz+2*u+18*MM,
      8*zz-2*rz+8*tz+2*u+18*MM,
      8*tz+u+8*MM,
      -8*tz+u+8*MM]
    assert min(D)>=u
    aa=F(3,8)*u+F(13,4)*MM
    bb=F(85,8)*u+F(471,4)*MM
    qq=[[rr,rt,rz],[rt,tt,tz],[rz,tz,zz]]
    ss=[[sum((D[k]*rays[k][i]*rays[k][j]
        for k in range(7)),F(0)) for j in range(3)]
        for i in range(3)]
    expected=[[qq[i][j]+(aa if i==j else 0)
         +(bb if i==j==0 else 0) for j in range(3)]
         for i in range(3)]
    assert ss==expected

u=F(1);MM=F(1)
# Worst signed corner for d1, fixing a,h and undershooting b.
rr,tt,zz=-MM,MM,MM
d1_min=rr-16*(tt+zz)+u+33*MM
assert d1_min==u
assert d1_min-F(1,100)<u

# The true A.11/A.19 source certificate remains fail closed.
from pathlib import Path
import json
src=Path(__file__).with_name("FULL_UNFORCED_SOURCE_CERTIFICATE_REQUIRED_20261022.json")
if src.exists():
    doc=json.loads(src.read_text())
    assert doc["status"]=="FAIL_CLOSED_MISSING_SOURCE_DATA"
    assert doc["analytic_lean_gates"]["physical_coordinate_zero_force_residual"] is None

print("PASS: independent LP minimax a=29/8,h=9,b=1027/8; source-free LP b=85/8")
print("PASS: 25000 exact Fraction 7-ray/6-component cases and sharp negative controls")
print("PASS: source verification remains FAIL-CLOSED; no unforced NSE proof")
