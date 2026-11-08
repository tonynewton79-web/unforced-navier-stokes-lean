#!/usr/bin/env python3
"""Attack 32 exact finite verification; full analytic composition is NOT certified."""
from fractions import Fraction as Q
from math import factorial

def a(j,b,R=Q(2),rho=Q(3,2)):
    return R**(-j)*rho**(-b)*Q(factorial(2*j+b),factorial(2*j))/((j+1)**2*(b+1)**2)

count=0
for k in range(5):
    for s in range(5-k):
        for p in range(5-k-s):
            for j in range(21):
                for b in (0,1,2,3,5,9,15,40):
                    for n in {1,max(1,j+1),j+2}:
                        lhs=Q(n**s*j**p,(j+1)**2*(j+2)**2)*a(j,b+k)/a(j+2,b)
                        cap=9*4**k*2**s*Q(2)**2/Q(3,2)**k
                        assert lhs<=cap,(k,s,p,j,b,n)
                        count+=1
assert count==17360

h=Q(1,200)
# From the exactly differentiated lagged U1=X, V1=(3/2-h) X^2 eta/L
lag_omega_at_axis=Q(3,2)-h
lag_pi_at_axis=-lag_omega_at_axis/6
assert lag_omega_at_axis==Q(299,200)
assert lag_pi_at_axis==Q(-299,1200)
assert Q(2029547156783445,2348867127617996)>0

ratios=[Q(N*(N-1))*Q(N**2,(N+1)**2) for N in [2,4,8,16,32,64,128]]
assert all(y>x for x,y in zip(ratios,ratios[1:])) and ratios[-1]>10000

P=lambda n:Q(1) if n==1 else Q(2) if n==2 else Q(0)
a0,b0,c0,d0=Q(3,2),Q(2,3),Q(4,5),Q(5,7)
r=Q(1,100); Pr=r+2*r*r
assert a0*(r+r*r)<=Q(1,4)
assert (c0+d0*r)*Pr<=Q(1,16)
Y=[Q(0)]*13
for n in range(1,13):
    ordinary=sum((Y[i]*Y[n-i] for i in range(1,n)),Q(0))
    delayed=sum((Y[i]*Y[n-1-i] for i in range(1,n-1)),Q(0))
    Y[n]=P(n)+a0*(Y[n-1]+(Y[n-2] if n>=2 else 0))+c0*ordinary+d0*delayed
    assert Y[n]>=0
assert Y[1:5]==[Q(1),Q(43,10),Q(10881,700),Q(105801,1400)]
print("PASS_ATTACK32_EXACT_MODEL",count,"rational coefficient checks, 12 majorant terms")
print("WARNING: full source-specific G1 pressure and Navier-Stokes existential proof OPEN")
