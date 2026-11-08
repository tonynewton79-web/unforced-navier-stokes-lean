#!/usr/bin/env python3
"""Exact rational interval for original source Appendix A unit transition.
Not a full exterior or Navier--Stokes existence certificate.
"""
from fractions import Fraction as Q
D=2**44

def round_out(x):
    return Q(x.numerator*D//x.denominator,D), Q(-((-x.numerator*D)//x.denominator),D)

def epos(x):
    if x==0: return Q(1),Q(1)
    m=max(1,int(2*x)+1)
    z=x/m; t=Q(1); s=Q(1)
    for k in range(1,19):
        t=t*z/k; s+=t
    rem=t*z/19/(1-z/20)
    return s**m,(s+rem)**m

def eb(x):
    if x>=0: a,b=epos(x)
    else:
        a,b=epos(-x)
        a,b=1/b,1/a
    return round_out(a)[0],round_out(b)[1]

def sig(x):
    if x==0: return Q(0),Q(0)
    if x==1: return Q(1),Q(1)
    if x>Q(1,2):
        a,b=sig(1-x);return 1-b,1-a
    v=1/x**2-1/(1-x)**2
    if v>=40: return Q(0),Q(1,2**40)
    a,b=eb(v)
    return round_out(1/(1+b))[0],round_out(1/(1+a))[1]

def cert(N=4096):
    sigs=[sig(Q(i,N)) for i in range(N+1)]
    SL=[Q(0)]*(N+1);SU=[Q(0)]*(N+1)
    for i in range(N):
        SL[i+1]=SL[i]+sigs[i][0]/N
        SU[i+1]=SU[i]+sigs[i+1][1]/N
    assert SL[-1]<=Q(1,2)<=SU[-1]
    JL=Q(0);JU=Q(0)
    for i in range(N):
        left=Q(i,5*N)-Q(6,5)*SU[i+1]
        right=Q(i+1,5*N)-Q(6,5)*SL[i]
        el,_=eb(left);_,eu=eb(right)
        JL+=el/N;JU+=eu/N
    return JL,JU

if __name__=="__main__":
    L,U=cert()
    expectedL=Q(69086996650998241,72057594037927936)
    expectedU=Q(69108717989414755,72057594037927936)
    assert L==expectedL and U==expectedU,(L,U)
    el,eu=eb(Q(-2,5))
    assert 5+U+eu < Q(663,100)
    assert Q(9587746798,10**10)<L<U<Q(9590761240,10**10)
    print("PASS exact rational pressure-transition integral certificate")
    print("J_lower =",L,"J_upper =",U)
    print("TOTAL pressure moments I0,I1 < 6.63 P_*^2")
    print("Tail uncertainty <= P_*^2 exp(-2/5-T_d), symbolically.")
    print("G1 local and full exterior schedule are NOT certified.")


# Separate exact rational envelope for source equation (A.19) pulse.
# The cutoff has integral 1/2, so phi_b(x)=x-1/100 beyond x=1/50.
if __name__=="__main__":
    el,eu=eb(Q(-1,25))
    e20l,e20u=eb(Q(-20))
    e26l,e26u=eb(Q(-26))
    KL=Q(5101,20000)*el-Q(1102901,20000)*e20u
    KU=Q(5101,20000)*eu+Q(1,375000)
    assert Q(2450492327,10**10)<KL<KU<Q(2450520132,10**10)
    cL=(1-e26u)/4;cU=(1-e26l)/4
    assert Q(101004,100000)**2*KU<cL
    assert Q(101006,100000)**2*KL>cU
    assert Q(1008,1000)**2*KU<cL-Q(1,1000)
    assert Q(1013,1000)**2*KL>cU+Q(1,1000)
    print("PASS original A.19 pulse Kb and conditional amplitude interval")
