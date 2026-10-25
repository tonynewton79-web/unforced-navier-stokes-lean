#!/usr/bin/env python3
"""Independent finite-mode exact Navier--Stokes projected transfer audit."""
from fractions import Fraction as F
from random import Random
rng=Random(20261024); Z=(F(0),F(0),F(0))
vecs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),
 (1,1,0),(-1,-1,0),(1,0,1),(-1,0,-1)]
dot=lambda a,b:sum((x*y for x,y in zip(a,b)),F(0))
for trial in range(1200):
    U={}
    for k in vecs:
        m=tuple(-x for x in k)
        pos=k if k>m else m
        if pos not in U:
            a,b,c=pos
            p=(F(-b),F(a),F(0)) if (a,b)!=(0,0) else (F(1),F(0),F(0))
            f=F(rng.randint(-7,7),rng.randint(1,9))
            U[pos]=tuple(f*x for x in p)
            U[tuple(-x for x in pos)]=U[pos]
    E=sum((dot(v,v) for v in U.values()),F(0))
    for k in [(1,0,0),(1,1,0),(2,1,1),(3,2,1)]:
        norm2=dot(k,k)
        raw=[F(0)]*3
        for l,v in U.items():
            m=tuple(k[i]-l[i] for i in range(3))
            w=U.get(m,Z); coeff=dot(k,v)
            raw=[raw[i]+coeff*w[i] for i in range(3)]
        para=dot(k,raw)/norm2
        N=tuple(raw[i]-para*k[i] for i in range(3))
        assert dot(N,k)==0 and dot(N,N)<=norm2*E*E
print("PASS 1200 rational divergence-free Fourier fields times 4 wavevectors")
print("PASS exact projected |N_k|^2 <= |k|^2 E^2")
