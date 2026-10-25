"""Appendix A.5 exact-rational checks for the MAIN axial pulse.
The smooth-step estimates are proved in the cumulative mathematical note.
These checks DO NOT certify the A.29/A.30 source moment error.
"""
from fractions import Fraction as F
from math import factorial
assert F(256**2+3072,4)==17152
assert 4*4**6+6*4**4+20*4**3+44==19244
assert F(14**7,factorial(7))>19244
assert 50*64+2*64+11*17152==192000
assert F(192000)*F(1011,1000)*(F(20,9)**3)<2131000
q1=F(241,100)**2/8
q2=F(482,100)**2/14
assert q1==F(58081,80000) and q2==F(58081,35000)
assert q1+F(1,100)<F(74,100)
assert q2+F(1,100)<F(168,100)
lam=F(1,2_000_000_000)
cd=F(1,2)*F(10000,9999)/(F(1,2)-lam)**2
assert cd<F(2001,1000)
assert F(1453)*lam<F(1,10**6)
eps=F(1,10**6)
dbw=1512*eps+eps**2
dquad=3336*eps+4*eps**2
assert q1+dbw<F(74,100)
assert q2+2*lam*1500**2+dquad<F(168,100)
print("PASS exact main pulse curvature/Taylor constants, scalar cone maxima and robust margins")
print("UNRESOLVED actual axial corrections and w ratio from A.29/A.30")
