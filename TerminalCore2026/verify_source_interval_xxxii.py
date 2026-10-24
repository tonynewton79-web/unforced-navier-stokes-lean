#!/usr/bin/env python3
"""Exact conditional shell-certificate checker. The actual source stays HOLD."""
from fractions import Fraction as F
from random import Random
from math import isqrt
import json
from pathlib import Path

def check(v):
    mandatory=['t','m_lower','R2_upper','V_upper','G_over_m_upper','L_rational']
    if any(v.get(k) is None for k in mandatory): raise ValueError('HOLD_SOURCE_DATA_NOT_FROZEN')
    t,m,R2,V,Q,L=[F(str(v[k])) for k in mandatory]
    if not(0<t<1 and min(m,R2,V,L)>0 and Q>=0):raise ValueError('HOLD_BAD_BOUNDS')
    if R2*V*L**5>F(45,4):raise ValueError('HOLD_LOW_FREQUENCY_GATE')
    N=1
    while (2**N)*L<4*Q:N+=1
    lower_squared=F(13,16*N)*m*m
    root=isqrt(lower_squared.numerator*10**18//lower_squared.denominator)
    assert F(root,10**9)**2<=lower_squared
    return N,lower_squared,F(root,10**9)

source=json.loads(Path(__file__).with_name('N1_SOURCE_NUMERICAL_FREEZE_GATE_XXXII.json').read_text())
v=source['actual_source_intervals']
try: check({'t':v['t'],'m_lower':v['m_lower'],'R2_upper':v['R2_upper'],
 'V_upper':v['V_upper'],'G_over_m_upper':v['G_over_m_upper'],'L_rational':v['L_rational']})
except ValueError as e: assert str(e)=='HOLD_SOURCE_DATA_NOT_FROZEN'
else: raise AssertionError('Source must fail closed')
# Explicitly synthetic, NOT an OpenAI numerical certificate.
fixture={'t':'1/2','m_lower':'1','R2_upper':'4','V_upper':'8',
 'G_over_m_upper':'3','L_rational':'1/2'}
assert check(fixture)[:2]==(5,F(13,80))
rng=Random(20261024)
for _ in range(15000):
 q={'t':'1/2','m_lower':str(F(rng.randrange(1,60),5)),
 'R2_upper':str(F(rng.randrange(1,20),6)),
 'V_upper':str(F(rng.randrange(1,20),6)),
 'G_over_m_upper':str(F(rng.randrange(0,80),7)),
 'L_rational':str(F(1,2**rng.randrange(7,14)))}
 n,z,lower=check(q)
 assert lower**2<=z and 2**n*F(q['L_rational'])>=4*F(q['G_over_m_upper'])
print('PASS 15000 exact rational conditional certificates')
print('ACTUAL SOURCE: HOLD, no numerical profile or validated bounds')
