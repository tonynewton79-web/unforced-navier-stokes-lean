#!/usr/bin/env python3
"""Independent pure-Fraction source bound verifier; no SymPy or floating point."""
from fractions import Fraction as Q
from math import factorial
from random import Random
assert Q(91,200)>Q(2,3)**2
assert Q(2)>Q(7,5)**2
assert Q(1349,100)**2<182<Q(27,2)**2
assert Q(707,500)**2<2<Q(283,200)**2
beta_lower=Q(21,2458)*(35*Q(2,3)+Q(7,5))
assert beta_lower==Q(2597,12290)
g=Q(15971,122900);k=Q(22371,122900);cap=(g+k)/2
assert cap==Q(19171,122900)
assert beta_lower-cap==Q(6799,122900)>0
assert beta_lower-g/2==Q(35969,245800)>0
beta_low=147*Q(1349,100)/9832+21*Q(707,500)/2458
beta_hi=147*Q(27,2)/9832+21*Q(283,200)/2458
assert Q(213,1000)<beta_low<beta_hi<Q(214,1000)
gamma_low=147*Q(1349,100)/9832-21*Q(283,200)/2458
gamma_hi=147*Q(27,2)/9832-21*Q(707,500)/2458
assert Q(189,1000)<gamma_low<gamma_hi<Q(190,1000)
e5=sum((Q(1,factorial(i)) for i in range(6)),Q(0))
tail=Q(1,factorial(6))/(1-Q(1,7))
assert e5+tail<3
assert Q(1229,4443*243)>0
assert Q(1229*288,4443*49)<2
rng=Random(989826)
for _ in range(20000):
    rho=Q(rng.randrange(1,1000),rng.randrange(1,1000))
    a=Q(rng.randrange(-100,101),rng.randrange(1,100))
    b=Q(rng.randrange(-100,101),rng.randrange(1,100))
    c=Q(rng.randrange(-100,101),rng.randrange(1,100))
    d=Q(rng.randrange(-100,101),rng.randrange(1,100))
    if -2*c-4*d>=-k*rho and 2*a-8*b+4*d>=-g*rho and -2*a+8*b+4*d>=-g*rho:
        assert c<=cap*rho
    R=Q(rng.randrange(1,1000),rng.randrange(1,1000))
    assert beta_lower*R>cap*R
print('PASS independent rational radical bounds, 20000 ray checks and e<3 enclosure')
print('HOLD original physical source, weighted inverse and full Navier-Stokes PDE')
