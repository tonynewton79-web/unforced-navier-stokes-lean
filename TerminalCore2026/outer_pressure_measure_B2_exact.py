"""Exact rational source bounds behind positive-measure Appendix-B (B.2).

This checks algebraic inequalities; it does not construct the source's
exterior schedule, a pressure mass, or its nonlinear fixed point.
"""
from fractions import Fraction as F
import sympy as s

eta,h,j,t,eta0=s.symbols("eta h j t eta0",real=True)
D=s.Rational(1,2)-h;A=s.Rational(1,2)+h
U=4*eta+j
H=s.expand(D*eta+(1-eta**2)*U)
Q=s.factor((H-H.subs(eta,eta0))/(eta-eta0))
assert s.simplify((eta-eta0)*Q-(H-H.subs(eta,eta0)))==0
assert s.simplify(H.subs(eta,-j/4)+D*j/4)==0
assert s.simplify(H.subs(eta,-j/5)-j*(1-D-j*j/25)/5)==0
jmax=F(1,20);tmax=jmax/4;Dmin=F(49,100)
assert Dmin-4*tmax*tmax-jmax>F(2,5)
assert Dmin-4*tmax*tmax>F(2,5)
assert F(1,2)*tmax/(1-tmax*tmax)<jmax/7
assert 1+2*tmax*jmax/7<2
Amax=F(51,100);Umax=F(81,20)
noP=Amax*((2*Umax+8)*Umax+(1+2*Umax)*4)+4*F(83,5)
withP=2*2+8+4*Amax+4*Amax*2
assert noP<120 and withP<20
assert F(1,2)*(1-F(2,7))>F(1,3)
assert F(144,145)>F(99,100)
assert F(5,2)/(1+tmax*tmax)**2>1
print("PASS symbolic cubic secant, root bracket and rational Z derivative constants")

rho=s.symbols("rho",nonnegative=True)
ws=(1+eta**2)**(-2*rho)
assert s.simplify(s.diff(ws,eta)+4*rho*eta/(1+eta**2)*ws)==0
assert s.simplify(
 s.diff(ws,eta,2)
 -(-4*rho*(1-eta**2)/(1+eta**2)**2
 +16*rho*rho*eta*eta/(1+eta**2)**2)*ws)==0
print("PASS pressure-mixture analytic derivative identities")

cases=0
for pp in [1,10,10000]:
 for hh in [F(1,200),F(1,10000)]:
  for jj in [F(1,50),F(1,1000)]:
   # Synthetic masses only; NEVER the unfrozen actual source schedule.
   mass=F(5,2)*pp*pp+F(1,2)
   K=200*(1+mass)
   eps=jj/F(12*K)
   delta=jj/12
   sigma=eps/30
   assert K*eps==delta
   assert sigma>0 and sigma<F(1,10)
   assert F(4,25)*eps*eps/(F(4,25)*eps*eps+sigma*sigma)==F(144,145)
   cases+=1
print("PASS",cases,"synthetic rational mass consistency checks; not source-profile certification")
