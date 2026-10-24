"""Exact rational constants for the actual Appendix-A (A.11)-(A.13)
parameter derivative and terminal Q-stopping certificate.

All claims about the full stress cone or unforced Navier-Stokes PDE
remain outside these finite arithmetic checks.
"""
from fractions import Fraction as Q
from math import factorial

def exp_partial(x,n):
    x=Q(x)
    return sum((x**k/Q(factorial(k)) for k in range(n+1)),Q(0))
def exp_upper(x,n):
    x=Q(x)
    return exp_partial(x,n)+(x**(n+1)/factorial(n+1))/(1-x/Q(n+2))
assert exp_upper(3,12)<21
assert exp_upper(1,8)<3
assert exp_upper(4,20)<100

assert Q(50,289)*21<4
assert Q(3,2)*640*192*Q(1,20)**28<Q(1,2)
assert 2*200000*12+4*200000*192*Q(640,3)*12*Q(1,20)**28<5000000
for h in (Q(1,100),Q(1,200),Q(1,10000)):
    co=Q(1,256)
    Qp_max=21*co*h/(1-co*h)
    Qp_min=co*h/(1-co*h)
    assert 0<Qp_min<=Qp_max<h/10
    assert Q(16,3)*(1-h)>5>Qp_max
print('PASS source: |Delta_eta|<4 lambda^28, |c_eta|<12 lambda^28')
print('PASS slope_eta<5e6 lambda^28 and terminal Q_start>5>Qp>0')
print('OUTSTANDING: stress cone, full schedule, actual unforced PDE')
