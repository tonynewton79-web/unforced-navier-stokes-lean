"""Exact source-conditional A.11 cancellation and strict cone arithmetic.

Source fields and terminal gauges are NOT constructed or validated here.
"""
from fractions import Fraction as F
import sympy as s
v,dv,a,b,da,db=s.symbols('v dv a b da db',nonzero=True)
D=a/(2*v*v);P=b/(2*v*v);g=dv/v
assert s.cancel(2*g*(D-P)+da/(2*v*v)-a*dv/v**3
                -(db/(2*v*v)-b*dv/v**3)-(da-db)/(2*v*v))==0
assert F(1,2)-F(63,250)==F(31,125)
assert F(1,2)-F(3,20)*F(63,125)**2==F(144343,312500)>F(9,20)
total=0
for den in (20,21,30,40,100,200,1000):
 lam=F(1,den);delta=40960*lam**28
 assert 0<delta<F(1,10**31)
 K=1536*lam**28*(1+delta)/(1-delta)**2
 assert K<F(1,1000)
 for hj in (100,101,1000):
  h=lam/hj
  Db=(1+8*delta)*(F(93,40)+h**7/3)
  assert Db<F(233,100)
  Pbound=(1+8*delta)/2
  assert 4*h*Db+4*(F(1,2)+h)*Pbound+K<F(1008,1000)
  total+=1
print('PASS symbolic local derivative cancellation and',total,
      'rational conditional stress instances')
print('NO source-authenticated c_i, S(infinity), Pi(infinity), Q_s, or PDE theorem')
