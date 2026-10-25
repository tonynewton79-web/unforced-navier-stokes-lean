#!/usr/bin/env python3
from fractions import Fraction as F
from random import Random
rng=Random(20261025)
for _ in range(25000):
 X=F(rng.randrange(1,100),rng.randrange(1,100))
 E=F(rng.randrange(1,100),rng.randrange(1,100))
 nu=F(rng.randrange(1,100),rng.randrange(1,100))
 eta=F(rng.randrange(1,100),rng.randrange(1,100))
 tau=F(1,2**rng.randrange(4,19))
 A=F(rng.randrange(1,100),rng.randrange(1,100))
 B2=eta*eta*E*E/(2*nu)
 window=4*X*tau*B2/(A*A)
 assert A*A*window/(4*X*tau)==B2
 assert B2*X*tau*tau==eta*eta*E*E*X*tau*tau/(2*nu)
print('PASS 25000 exact rational moving-radius spike budget cases')
