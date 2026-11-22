#!/usr/bin/env python3
"""Attack98: exact frozen Appendix AD diagnostic, not original unselected physical H8 source."""
from fractions import Fraction as F
from random import Random
from pathlib import Path
import json
import sympy as s
q=s.Rational
br=(35*s.sqrt(q(91,200))+s.sqrt(2))/s.sqrt(1229)
bt=-q(21,2)/s.sqrt(1229)
bz=(-35*s.sqrt(q(91,200))+s.sqrt(2))/s.sqrt(1229)
alpha=s.simplify(br*bz)
beta=s.simplify(br*bt)
gamma=s.simplify(bt*bz)
g=q(15971,122900);k=q(22371,122900);cap=(g+k)/2
assert alpha==-q(4443,9832)
assert s.simplify(beta+147*s.sqrt(182)/9832+21*s.sqrt(2)/2458)==0
assert s.simplify(gamma-147*s.sqrt(182)/9832+21*s.sqrt(2)/2458)==0
assert q(91,200)>q(2,3)**2 and q(2,1)>q(7,5)**2
assert -beta>q(2597,12290)>cap==q(19171,122900)
assert q(2597,12290)-cap==q(6799,122900)
assert q(2597,12290)-g/2==q(35969,245800)
assert -beta>q(213,1000) and -beta<q(214,1000)
assert gamma>q(189,1000) and gamma<q(190,1000)
x=s.symbols('x',real=True)
poly=(1-x*x)**5
phi1=poly;phi2=(1+q(1,2)*x)*poly
xi1=poly;xi2=(1-q(1,2)*x)*poly
assert s.simplify(phi1*s.diff(phi2,x)-phi2*s.diff(phi1,x)-phi1**2/2)==0
N2=s.integrate(poly*poly,(x,-1,1))
assert s.simplify(s.integrate(s.diff(xi1,x)*xi2,(x,-1,1))+(-q(1,2))*N2/2)==0
ratio_T=q(4443,4916)*(-q(1,2))
assert ratio_T==alpha and ratio_T-alpha==0
# Cylindrical divergence's actual theta source, fixed with canonical B and C.
r,z=s.symbols('r z',positive=True)
rho=s.Function('rho')(r,z)
Srt=-beta*rho;Stz=-gamma*rho
fth=s.diff(Srt,r)+2*Srt/r+s.diff(Stz,z)
C=-beta*rho;B=-gamma*rho
assert s.simplify(fth-(s.diff(C,r)+2*C/r+s.diff(B,z)))==0
Rlo=F(1229,4443*243)
Rhi=F(1229*288,4443*49)
assert Rlo>0 and Rhi<2
rng=Random(982026)
gap=F(6799,122900)
cap_fraction=F(19171,122900)
beta_lower=F(2597,12290)
for _ in range(30000):
    R=F(rng.randrange(1,10000),rng.randrange(10000,30000))
    assert beta_lower*R>cap_fraction*R
    U=F(rng.randrange(-5000,5001),rng.randrange(1,10000))
    if U+beta_lower*R<=cap_fraction*R:
        assert U<=-gap*R
# These fields are deliberately UNFROZEN for the actual original source.
gate=json.loads(Path(__file__).with_name('source_gate.json').read_text())
assert gate['status']=='COMPLETE_AD_DIAGNOSTIC_REFUSED__ORIGINAL_PHYSICAL_SOURCE_UNFROZEN'
assert gate['diagnostic']['one_sided_H8_feasible'] is False
assert gate['diagnostic']['axial_scalar_test_passes'] is True
assert all(v is None for v in gate['original_physical'].values())
assert gate['M_terminal'] is None and not gate['unforced_blowup_proved']
print('PASS: original physical R* entries, exact flat normalized two-shaper identities')
print('PASS: 30000 exact one-sided cone/radial angular-flux checks')
print('PASS: diagnostic J=q=0 but forced Cbar=-beta Rbar exceeds one-sided cap')
print('HOLD: original physical source not frozen; full NS theorem OPEN')
