"""Independent exact tests for complete radial convolution and two-lift smoothing.

Tests the multiplier coefficient inequalities and radial indices. The
mathematical paper proves the all-index theorem. The full Navier--Stokes
leading-pressure and nonlinear H_k operators are NOT represented here.
"""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product

def w(a,b,R,rho):
    return R**(-a)*rho**(-b)*Q(factorial(b)*comb(2*a+b,b),(a+1)**2*(b+1)**2)

for N in range(500):
    s=(N+1)**2 * sum((Q(1,(i+1)**2*(N-i+1)**2) for i in range(N+1)),Q(0))
    assert s<=8
print("PASS 500 exact one-index convolution bounds")

count=0
for a,b in product(range(20),range(21)):
    for i in range(a+1):
        for u in range(b+1):
            j,v=a-i,b-u
            assert comb(2*i+u,u)*comb(2*j+v,v)<=comb(2*a+b,b)
            radial=Q((a+1)**2,(i+1)**2*(j+1)**2)
            axial=Q((b+1)**2,(u+1)**2*(v+1)**2)
            for R,rho in ((Q(1),Q(1)),(Q(3,2),Q(2,5))):
                actual=comb(b,u)*w(i,u,R,rho)*w(j,v,R,rho)/w(a,b,R,rho)
                assert actual<=radial*axial
            count+=1
print("PASS",count,"two-index Vandermonde and Leibniz inequalities")

count=0
for R,rho in ((Q(1),Q(1)),(Q(3,2),Q(1,4)),(Q(2,7),Q(7,5))):
    for n in range(1,15):
        for a in range(n,n+13):
            t=a+n+2
            for b in range(22):
                for d in range(4):
                    actual=Q(t**(3-d),(a+1)**2*(a+2)**2)*w(a,b+d,R,rho)/w(a+2,b,R,rho)
                    D=675*R**2*rho**(-d)*Q(2**(4-d),(d+1)**2)
                    assert actual<=D/(n+1),(n,a,b,d)
                    count+=1
print("PASS",count,"two-lift O(1/n) jet-weight bounds")

count=0
for n in range(1,30):
    for a in (n,n+1,n+7):
        for c in (0,1,2,3,11,100,1000):
            t,N=a+n+2,a+c+2
            for j in range(4):
                p=3-j
                assert (N+n)**p==sum(comb(p,s)*t**(p-s)*c**s for s in range(p+1))
                assert (N-1)**2*N**2 >=(a+1)**2*(a+2)**2
                assert sum(comb(p,s)*t**p*c**s for s in range(p+1)) >=(N+n)**p
                count+=1
print("PASS",count,"full multiplier polynomial and denominator bounds")
