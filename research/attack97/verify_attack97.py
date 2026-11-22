#!/usr/bin/env python3
"""Attack97 exact source-derived Appendix AD/AC finite diagnostics.
NOT the actual 4-patch Case006 physical source or full NS theorem.
"""
from fractions import Fraction as F
from random import Random
import json
from pathlib import Path
import sympy as sp

alpha=-F(4443,9832)
kappa=F(15971,122900)
c=F(4443,4916)
assert alpha == -c/2
lo=-F(1,2)-kappa/c
hi=-F(1,2)+kappa/c
assert (lo,hi)==(-F(143017,222150),-F(79133,222150))
assert -F(1,2)-kappa/(2*c) == -F(63523,111075)
assert -F(1,2)+kappa/(2*c) == -F(47552,111075)
assert c-kappa==F(23776,30725)
assert c/kappa==F(111075,15971)
assert abs(alpha)-kappa==F(79133,245800)
assert alpha+kappa==-F(79133,245800)
for lam,admit in [(-F(1,2),True),(F(0),False),(F(1,2),False)]:
    assert (abs(c*(lam+F(1,2)))<=kappa)==admit

x,z,mu,lam=sp.symbols('x z mu lam',real=True)
# Even polynomial proxies verify the universal continuum Wronskian identity.
bx=(1-x*x)**4
bz=(1-z*z)**4
W=sp.expand(bx*sp.diff((1+mu*x)*bx,x)-(1+mu*x)*bx*sp.diff(bx,x))
assert sp.simplify(W-mu*bx**2)==0
Omega=sp.integrate(sp.expand(sp.diff(bz,z)*(1+lam*z)*bz),(z,-1,1))
B2=sp.integrate(bz**2,(z,-1,1))
assert sp.simplify(Omega+lam*B2/2)==0
assert sp.integrate(x*bx,(x,-1,1))==0
assert sp.integrate(z*bz,(z,-1,1))==0

rng=Random(972026)
for i in range(30000):
    j=F(rng.randrange(-50000,50001),rng.randrange(1,2000))
    opt=j/8
    assert max(8*abs(opt),2*abs(j-4*opt))==abs(j)
    b=F(rng.randrange(-50000,50001),rng.randrange(1,2000))
    assert max(8*abs(b),2*abs(j-4*b))>=abs(j)
    if abs(b)<=kappa/8 and abs(j-4*b)<=kappa/2:
        assert abs(j)<=kappa
for i in range(15000):
    lam=F(rng.randrange(-10000,10001),10000)
    baseline=c*(lam+F(1,2))
    e=F(rng.randrange(-50000,50001),rng.randrange(1,2000))
    if abs(baseline+e)<=kappa:
        assert abs(e)>=max(F(0),abs(baseline)-kappa)
for i in range(10000):
    R=F(rng.randrange(1,10000),rng.randrange(1,1000))
    assert abs(F(0)*R)<=kappa*R
    assert abs(c*R)>kappa*R

d=json.loads(Path(__file__).with_name('source_freeze.json').read_text())
assert d['status']=='PHYSICAL_SOURCE_TUPLE_UNFROZEN__EXACT_PROFILE_DISCRIMINATOR'
for field in ('physical_f_m','physical_B','physical_C','physical_rho','physical_T','boundary_q','actual_four_patch_maps'):
    assert d['unresolved_physical_inputs'][field] is None
assert d['actual_Y_dual_inequalities_tested'] is False
assert d['actual_AC_source_primitive_tested'] is False
assert d['actual_compact_weighted_inverse_proved'] is False
assert d['M_terminal'] is None and d['full_NS_singularity_proven'] is False
print('PASS: source-derived rational lambda interval and mandatory remainder')
print('PASS: Appendix AD Wronskian + axial antisymmetric overlap')
print('PASS: 30000 exact polar, 15000 remainder and 10000 source-family tests')
print('HOLD: physical Case006 f_m,B,C,rho,T,q,patch maps and complete PDE')
