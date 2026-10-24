"""Source-local future tail rational gates; not a source-authenticated PDE proof."""
from fractions import Fraction as F
a=b=F(1,1000)
C=(2*(1+a)**2*F(2503,5000)+F(23,10)*(1+a)*b)/(1-a)
assert C==F(2513764253,2497500000) and C<F(11,10)
assert 8*F(1,100)**44<F(1,1000)
assert F(1280,3)*F(1,100)**28<F(1,1000)
assert F(640,3)*F(1,100)**28<F(1,1000)
assert F(93,20)+F(2,3)*F(1,10000)**7<5
assert F(11,10000)<F(1,500)<F(1,2)
print("CONDITIONAL_SCALAR_PASS")
print("MISSING SOURCE CERTIFICATES: authentic root; S/Pi infinity gauges; full exterior")
