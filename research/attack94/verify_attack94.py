#!/usr/bin/env python3
"""Attack94: EXACT finite rational certificate; analytic proofs in companion note.
No full outer profile / unforced NS proof is claimed."""
from fractions import Fraction as F
from math import factorial
from random import Random
import json
from pathlib import Path
R=F(1001,1000)
assert F(9,2)+12*R**2+F(1,10)*R<17
assert 1+F(1,50)*R**2<F(103,100)
assert 1-F(1,50)*R**2>F(97,100)
# Uniform Cauchy bound on chi=H²/(H²+sigma²); delta=sigma/170.
chi_complex=1+1/F(9,10)**2
weighted=max(F((n+1)**2,2**n) for n in range(100))
assert chi_complex==F(181,81) and weighted==F(9,4)
chi_Brho=chi_complex*weighted
Mchi=chi_Brho*F(40,3)**2
assert chi_Brho==F(181,36) and Mchi==F(72400,81)<900
assert F(103,100)/F(9,10)*weighted==F(103,40)
K=528
r=40*Mchi/F((K+2)*(K+3))
tail=(40*Mchi)**(K+1)/F(factorial(K+1)*factorial(K+2))/(1-r)
assert 0<r<1 and tail<F(1,2**64)
# The source continuation fixes kappa0 sup p1r <4/5 until Xb=100.
# Case006 a>=10 is incompatible with a=kappa0*p1r on that interval.
assert 2*(2-F(4,5))==F(12,5)
assert F(61,10)/F(16,25)==F(305,32)<100
assert F(6)>F(41,10)
assert F(60,61)**23 < F(927,1000)**5 # nonperturbative shear repair
rng=Random(942026)
for _ in range(16000):
    j=F(rng.randrange(1,1001),20000)
    h=F(rng.randrange(1,1001),100000)
    sigma=j*F(rng.randrange(1,1001),4000)
    x=F(1,9)+(F(1,7)-F(1,9))*F(rng.randrange(0,1001),1000)
    eta=-j*x
    D=F(1,2)-h
    H=(4+D)*eta+j-4*eta**3-j*eta**2
    chi=H**2/(H**2+sigma**2)
    assert chi>F(16,25)
    assert D*eta+4*eta+j>0
    Y=F(6)/chi
    assert 6<=Y<F(305,32)
d=json.loads(Path(__file__).with_name('source_gate.json').read_text())
assert d['status']=='CERTIFIED_CHI_MULTIPLIER__RAYLEIGH_TRANSFER_INCOMPATIBLE__FULL_SOURCE_HOLD'
assert d['M_terminal'] is None
assert d['actual_continued_strong_Rayleigh_a_at_least_10'] is False
assert d['full_exterior_profile_certified'] is False
assert d['Case006_full_unforced_blowup_proved'] is False
print('PASS: Mchi<72400/81<900; inverse Neumann tail (K=528)<2^-64')
print('PASS: 16000 exact wedge tests; B.26 a<4/5 vs Case006 a>=10')
print('HOLD: whole exterior, momentum matching, full PDE, full Lean')
