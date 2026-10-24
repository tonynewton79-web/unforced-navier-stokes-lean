#!/usr/bin/env python3
"""Independent exact source heat-exterior sign and gamma derivative replay.
No authentication of final oscillatory/localized velocity or unforced PDE.
"""
from fractions import Fraction as F
from random import Random
import sympy as s
import mpmath as m
R,a,h=s.symbols("R a h",positive=True)
g=1/R/(R*R+a)**h
C=(1+2*h)*(2+2*h)*(3+2*h)
P=6*a**3+(6*h+18)*a*a*R*R+(12*h+18)*a*R**4+C*R**6
assert s.simplify(-s.diff(g,R,3)*R**4*(R*R+a)**(h+3)-P)==0
Q,d=s.symbols("Q d",positive=True)
assert s.simplify((2*d/(R**2/(2*Q))).subs(d,1/Q)-4/R**2)==0
rr=Random(20261023)
for _ in range(10000):
  hh=F(rr.randint(1,100),rr.randint(10101,10200))
  aa=F(rr.randint(0,50),rr.randint(1,23))
  rv=F(rr.randint(1,50),rr.randint(1,23))
  cv=(1+2*hh)*(2+2*hh)*(3+2*hh)
  assert 6*aa**3+(6*hh+18)*aa**2*rv**2+(12*hh+18)*aa*rv**4+cv*rv**6>0
m.mp.dps=60
hh=m.mpf("0.005");A=m.mpf("0.5")+hh
lo=m.mpf(4); hi=m.mpf(5)
cv=(1+2*hh)*(2+2*hh)*(3+2*hh)
mass=lambda v:m.exp(-v)*v**hh/m.gamma(hh+1)
def dd(R,v):
  av=4*v
  pp=6*av**3+(6*hh+18)*av**2*R**2+(12*hh+18)*av*R**4+cv*R**6
  return R**(-4)*(R*R+av)**(-hh-3)*pp
bound=2**A*cv*lo**2/(hi**2+4)**(hh+3)*m.exp(-1)/m.gamma(hh+2)
for x in [lo,(lo+hi)/2,hi]:
  d3=2**A*m.quad(lambda v:mass(v)*dd(x,v),[0,1,m.inf])
  H=lambda y:m.quad(lambda v:mass(v)*(1+4*v/y**2)**(-hh),[0,1,m.inf])
  direct=-m.diff(lambda y:2**A*y**(-2*A)*H(y),x,3)
  assert d3>bound and abs((direct-d3)/d3)<m.mpf("1e-35")
assert lo>=2*m.sqrt(2) and 2-m.mpf(1)/16*2**(2*hh)>1
print("PASS source exact heat integral and 3rd radial derivative sign")
print("PASS 10000 exact rational positivity tests and three 60-digit derivative comparisons")
print("Illustrative source-family lower:",m.nstr(bound,15))
print("HOLD actual parameter freeze, corrected full physical field, unforced PDE and Lean kernel")
