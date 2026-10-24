"""Exact A11 scalar smallness witness and conditional cone margin.
Fails closed: this is never a certificate of source field integrals/PDE.
"""
from fractions import Fraction as F
import json
checked=0
for td,lnp in [(11,20),(20,100),(100,10000),(100000,1000000)]:
 for extra in (0,1,113,10000):
  q=F(1+td+512+lnp+extra)
  lam=F(1,10**20*q)
  for eps in (F(1,2),F(1,10**9),F(1,10**100)):
   h=lam*eps/10**6
   assert 0<lam< F(1,10**14)
   assert lam<F(1,20)
   assert lam<=F(1,10**6*(td+513))
   assert lam<=F(1,10*(1+lnp))
   assert lam*512<F(1,10**6)
   assert 0<h<lam/10000 and h<eps/100 and h<F(1,10000)
   assert F(60+q-1,10**20*q)<F(1,10**18)
   checked+=1
cone=2*(1-F(1,4))**2-F(3,20)*F(4,49)**2
assert cone==F(107949,96040)>1
print('PASS',checked,'joint scalar smallness comparisons and exact conditional cone',cone)
print('UNPROVED: authentic A11 integral intervals, complete exterior stress, unforced Theorem 1.1')
