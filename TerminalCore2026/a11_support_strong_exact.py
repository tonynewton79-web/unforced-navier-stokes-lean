"""A.11 source two-bump stress certificate: exact rational gates.

Actual analytic theorem in A11_Support_Stress_Improved_20261021_Insert.tex.
Finite arithmetic and outward-interval examples are not a complete
source-parameter, Lean, or unforced PDE certificate.
"""
from fractions import Fraction as Q
from math import factorial

def exp_lo(x,n):
    return sum((x**k/Q(factorial(k)) for k in range(n+1)),Q(0))
def exp_hi(x,n):
    assert x/(n+2)<1
    p=exp_lo(x,n)
    return p+(x**(n+1)/Q(factorial(n+1)))/(1-x/Q(n+2))

assert exp_hi(Q(3),45)<21
assert exp_hi(Q(63,40),30)<5
assert exp_lo(Q(13,2),18)>500
assert exp_lo(Q(19,10),14)>6
assert exp_hi(Q(2),32)<8
assert exp_lo(Q(11,5),17)>9
assert exp_hi(Q(33,200),28)<2
assert exp_lo(Q(128,9),30)>1500000
assert exp_lo(Q(608,5),195)>10**50
assert Q(2)*Q(20,19)/10**50+Q(40,19)*(Q(1,1500000)+Q(1,10**50))<Q(1,700000)

la=Q(1,20)
assert Q(9,4)*21<50
assert 50*la**28<Q(1,10**6)
assert Q(21,700000)<=Q(3,100000)
assert Q(100,9)*20000<250000
assert Q(256**2+3072,4)<20000
assert Q(640,3)*50*la**28<Q(1,1000)
assert 250000*50*la**27<Q(1,4)
assert Q(640,3)*Q(3,100000)<Q(1,100)
assert Q(8,23)+743/Q(10**6)<1
assert 1485/Q(10**6)<Q(1,100)
assert Q(8,23)/(1-1485/Q(10**6))<1
assert 4*Q(1,100)*3+1+2*Q(1,100)+3*Q(1,100)<2
assert Q(20,500)<Q(1,4)
assert Q(2,25)<Q(1,2)

print('PASS exact source A.11 weight, entrance, contraction and stress margin gates')
from mpmath import iv
iv.dps=70
def fi(q):
    q=Q(q);return iv.mpf(q.numerator)/iv.mpf(q.denominator)
for lam in (Q(1,20),Q(1,100),Q(1,1000)):
    a=1-lam
    y1=30*iv.log(1/fi(lam))-3
    delta=fi(Q(9,4))*iv.exp(-fi(a)*y1)
    ddelta=fi(Q(1,700000))*iv.exp(-fi(a)*y1)
    # Diagnostic P*=exp(15) with bound lambda <=1/(1+log P*)
    emax=20*iv.exp(15)*iv.exp(-13/(2*fi(lam)))*fi(lam)**15
    assert lam<=Q(1,16)
    print('conditional diagnostic lambda',lam,'delta',str(delta),
          'delta_eta',str(ddelta),'E_bound',str(emax))
print('Global source gauges, stress cones and unforced PDE remain OPEN')
