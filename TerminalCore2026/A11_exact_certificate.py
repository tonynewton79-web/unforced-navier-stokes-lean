"""Exact rational A.11 two-bump moment-correction scalar certificate.

This checks the universal source-bump bounds and does NOT freeze the
remaining global stress-cone parameters or the unforced PDE hierarchy.
"""
from fractions import Fraction as Q
from math import factorial
from sympy import symbols,expand

def exp_lower(x,n):
    x=Q(x)
    return sum((x**k/Q(factorial(k)) for k in range(n+1)),Q(0))

assert exp_lower(Q(19,10),14)>6
assert exp_lower(2,12)>7
assert exp_lower(3,13)>20
assert exp_lower(Q(7,10),12)>2
assert exp_lower(Q(128,9),25)>28672
assert exp_lower(Q(74,5),21)>2500000

# On the beta support, u,v in [4/5,5/4]; x in (6,8), z in (0,1/7).
den=2*Q(4,5)**2*(6-Q(1,7))
first=(2*Q(5,4)*Q(1,7)+Q(5,4)*8)/den
second=(2*Q(5,4)+Q(5,4))/den
assert first==Q(3625,2624)<Q(3,2)
assert second==Q(2625,5248)<Q(3,2)
kappa=Q(5,4)*Q(640,3)*(1+Q(1,7))
assert kappa==Q(6400,21)<320
# Bound e^3 above by Taylor series and a geometric tail.
e3hi=exp_lower(3,12)+Q(3**13,factorial(13))*Q(14,11)
assert e3hi<21
lam=Q(1,20)
delta=64*lam**28
assert 8*Q(3,2)**2*320*delta<1
assert Q(640,3)*192*lam**28<Q(1,2)
assert 2*200000*192*lam**28<lam/2
assert Q(7,10)*64/512==Q(7,80)<Q(1,10)
assert Q(1,256)*32/(1-Q(1,25600))<Q(1,4)

# Exact source two-equation elimination; c1=Delta/u-x*c2.
c,dl,u,v,w,x,z=symbols('c dl u v w x z')
alpha=dl/u
aa=w*(x*x+z)
bb=2*v*(z-x)-2*w*alpha*x
cc=2*v*alpha+w*alpha**2
assert expand(2*v*(alpha-x*c+z*c)+w*((alpha-x*c)**2+z*c*c) -
              (aa*c*c+bb*c+cc))==0
print('PASS exact inverse bound, A.2 contraction, beta curvature,')
print('  Tf=512, co=1/256, and scalar A.11 quadratic identity.')
print('OPEN: frozen complete source schedule, stress cone and unforced PDE.')
