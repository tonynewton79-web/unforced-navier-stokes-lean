#!/usr/bin/env python3
"""Frozen exact 64-corner + multilinear interpolation seven-ray verification.
This is purely source-independent stress algebra. No unforced NSE proof.
"""
from fractions import Fraction as F
from pathlib import Path
from random import Random
from itertools import product

file=Path(__file__).with_name("XXVIII_64_CORNER_EXACT_CERTIFICATES.txt")
rows=[[F(x) for x in line.split()] for line in file.read_text().splitlines()
      if line.strip() and not line.lstrip().startswith("#")]
assert len(rows)==64 and all(len(row)==8 for row in rows)
signs=list(product((-1,1),repeat=6))
t=F(1,4)
rays=[(F(1),F(0),F(0)),(F(1),t,F(0)),(F(1),-t,F(0)),
      (F(1),F(0),t),(F(1),F(0),-t),(F(1),t,t),(F(1),t,-t)]
component=lambda v:(v[0]**2,v[1]**2,v[2]**2,
                    v[0]*v[1],v[0]*v[2],v[1]*v[2])
V=[component(v) for v in rays]
B=F(343,4)
for sg,row in zip(signs,rows):
    assert min(row[1:])>=0
    actual=tuple(sum((row[j+1]*V[j][k] for j in range(7)),F(0))
       -(row[0] if k<3 else 0)-(B if k==0 else 0) for k in range(6))
    assert actual==sg,(sg,actual)

# Independent exact LP dual certificate: for all positive ray weights
# the functional L(S)=(-Srr-15 Stt+16 Szz-31 Srt/4-46 Stz)
# is <= -85*mu/8; L(erer)=-1 and L(I)=0.
dual=(F(-1),F(-15),F(16),F(-31,4),F(0),F(-46))
ray_duals=[sum((dual[k]*V[j][k] for k in range(6)),F(0)) for j in range(7)]
assert ray_duals==[F(-1),F(-31,8),F(0),F(0),F(0),F(-23,4),F(0)]
assert sum(dual[:3])==0 and dual[0]==-1
assert -sum(ray_duals)==F(85,8)
critical=(-1,-1,1,-1,-1,-1)
assert sum((dual[i]*critical[i] for i in range(6)),F(0))==B

baseline=(F(1),F(1),F(3),F(2),F(2),F(1),F(1))
a0,b0=F(3,8),F(85,8)
assert tuple(sum((baseline[j]*V[j][k] for j in range(7)),F(0))
 -(a0 if k<3 else 0)-(b0 if k==0 else 0) for k in range(6))==(F(0),)*6

def interpolate(q,mu,M,chi=F(1)):
    """Only for a cutoff with chi=1 wherever q is nonzero."""
    if not M:
        assert all(x==0 for x in q)
        return a0*mu*chi,[mu*chi*x for x in baseline],b0*mu
    assert all(-M<=x<=M for x in q)
    assert chi==1 or all(x==0 for x in q)
    normalized=[x/M for x in q]
    W=[F(1)]*64
    for j,sg in enumerate(signs):
        for k in range(6):
            W[j]*=(1+sg[k]*normalized[k])/2
    assert sum(W)==1 and min(W)>=0
    a=chi*(a0*mu+M*sum((W[j]*rows[j][0] for j in range(64)),F(0)))
    d=[chi*(mu*baseline[k]+M*
       sum((W[j]*rows[j][k+1] for j in range(64)),F(0)))
       for k in range(7)]
    return a,d,b0*mu+B*M

rng=Random(20261024)
for i in range(750):
    M=F(rng.randrange(13),rng.randrange(1,9))
    mu=F(rng.randrange(1,13),rng.randrange(1,10))
    collar=(i%8==0)
    chi=F(rng.randrange(11),10) if collar else F(1)
    q=(F(0),)*6 if collar else tuple(
       F(rng.randrange(-10,11),10)*M for _ in range(6))
    a,d,b=interpolate(q,mu,M,chi)
    assert min(d)>=mu*chi
    actual=tuple(sum((d[j]*V[j][k] for j in range(7)),F(0))
       -(a if k<3 else 0)-(b*chi if k==0 else 0) for k in range(6))
    assert actual==q,(i,q,actual)
    S=[actual[j]+(a if j<3 else 0)+(b*chi if j==0 else 0)
       for j in range(6)]
    assert max(map(abs,S))<=90*M+11*mu
assert max(row[0] for row in rows)==F(13,4)
print("PASS 64/64 FROZEN exact signed stress-box vertex certificates")
print("PASS exact sharp dual slope 343/4 and baseline 85/8")
print("PASS 750/750 exact multilinear smooth-interpolation and collar fixtures")
print("PASS source-independent tensor size <= 90 M + 11 mu")
print("HOLD actual source/H8 budget, zero-force NSE, complete Lean theorem")
