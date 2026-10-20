"""Appendix A pulse source A.5/A.19 and normalized moment matrix.
Independent exact-rational arithmetic. NOT the full moment-corrected
source schedule or a complete Navier-Stokes construction.
"""
from fractions import Fraction as Q
from math import factorial
d=Q(1,50); shift=d/2
base=Q(1,4)-shift/2+shift**2/2
assert base==Q(4901,20000)
assert sum((Q(20**i,factorial(i)) for i in range(36)),Q())>470000000
assert sum((Q(26**i,factorial(i)) for i in range(31)),Q())>100000000000
tail=(10-shift)**2/2+(10-shift)/2+Q(1,4)
assert tail==Q(1102901,20000)
Kl=base-d*shift**2-tail/470000000
Ku=base+d*shift**2
assert Kl>Q('0.2450478') and Ku==Q('0.245052')
print('PASS exact source K_b enclosure: 0.2450478<K_b<0.245052')
lo=Q('1.009');hi=Q('1.011');err=Q(1,2500)
assert lo**2*Ku-(1-Q(1,100000000000))/4<-err
assert hi**2*Q('0.2450478')-Q(1,4)>err
assert 2*lo*Q('0.2450478')-Q(1,100)>Q('0.48')
assert Q('1.010045')**2*Ku-(1-Q(1,100000000000))/4<0
assert Q('1.010055')**2*Q('0.2450478')-Q(1,4)>0
print('PASS principal source amplitude: 1.010045<A0<1.010055')
print('PASS conditional source Amp in (1.009,1.011), derivative gap >0.48')
det=4*Q(37,40)**2
assert det==Q(1369,400) and det>3
assert Q(13,2)/det<2
print('PASS normalized two-bump determinant >=1369/400 lambda, inverse <2/lambda')
print('OPEN: actual E(A,eta), correction discrepancies and moment-matched source parameters')
