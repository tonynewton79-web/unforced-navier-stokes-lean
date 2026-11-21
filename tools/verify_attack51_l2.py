#!/usr/bin/env python3
"""Attack51 exact arithmetic only. Does NOT prove PDE/source identities."""
from fractions import Fraction as Q
import sympy as S
x,a,b,c=S.symbols("x a b c", real=True)
h=Q(1,200); A=Q(1,2)+h; beta=Q(1,2)-2*h
assert A==Q(101,200) and beta==Q(49,100)
chi=16*x*x*(1-x)*(1-x)
assert S.integrate(chi,(x,0,1))==S.Rational(8,15)
assert S.expand(S.diff(chi,x)-32*x*(1-x)*(1-2*x))==0
assert S.expand(18*(a*a+b*b+c*c)-(32*a*b+4*c*b)
 - (16*(a-b)**2+2*(c-b)**2+2*a*a+16*c*c))==0
j=Q(36501,274877906944)
c0=Q(201,4000)*j
assert c0==Q(7336701,1099511627776000)
source=Q(8,15)*c0
assert source==Q(2445567,687194767360000)
c_linear=(Q(83968)+Q(33,8)+Q(17,40))/8
c_final=c_linear+18
assert c_final==Q(1682331,160)
lower=source/c_final
assert lower==Q(815189,2408518875348992000)
assert lower>Q(338,10**15)
print("PASS: cutoff, nonlinear energy square and exact rational L2 margin")
print("Q_T lower bound =",lower,"=",float(lower))
print("NOT TESTED: source pairing, support, complete weak PDE identity, or blow-up")
