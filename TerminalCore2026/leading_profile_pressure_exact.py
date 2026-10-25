"""Exact replay of the five leading-profile contributions to Omega_k.

Source: equations (18), (24), (26)-(28), Zenodo 23474915.
Tests exact algebra, radial primitive cancellation, two-degree valuation,
and the four scalar jet ratios. This is not an analytic norm or PDE proof.
"""
import sympy as s
from fractions import Fraction as F
from math import comb, factorial
from itertools import product

e=s.symbols('eta')
def Z(q,r,f,h):
    L=1-2*h*e**2
    return s.cancel((2*e*(q-r)*f+(1-e**2)*s.diff(f,e))/L)
checks=0
for h,k,a,c,t in product([s.Rational(1,200),s.Rational(1,500)],
                         [1,2,5],[1,2,6],[0,1,3],[0,1]):
    if a<k: continue
    D=s.Rational(1,2)-h
    A=s.Rational(1,2)+h
    B=2*e/(1-2*h*e**2)
    G=(1-e**2)/(1-2*h*e**2)
    lam=2*h*k
    r=a+1
    m=a+c+1
    f=(1+e+e**2) if t==0 else (3-2*e+e**3)
    v=(2+e) if t==0 else (1+e**2)
    u=(1-e) if t==0 else (2+e**2)
    W=s.cancel(B*(r-D-lam)/r*f-G/r*s.diff(f,e))
    source=s.cancel(v*r*W+W*(c+1)*v-v*W+
                    u*Z(lam,r,W,h)+f*Z(0,c+1,v,h))
    q_v=s.cancel(m*v*W)
    q_u=s.cancel(u*(G*s.diff(W,e)+B*(lam-r)*W))
    q_f=s.cancel(f*(G*s.diff(v,e)-B*(c+1)*v))
    assert s.cancel(source-(q_v+q_u+q_f))==0
    pressure=Z(2*h*(k+1)-2*A,m,-(q_v+q_u+q_f)/(2*m),h)/(2*(m+1)**2)
    reduced=-Z(2*h*(k+1)-2*A,m,v*W,h)/(4*(m+1)**2)
    reduced-=Z(2*h*(k+1)-2*A,m,q_u+q_f,h)/(4*m*(m+1)**2)
    assert s.cancel(pressure-reduced)==0
    assert m+1>=k+2
    checks+=1
print('PASS exact five-term source, pressure and valuation:',checks)

def weight(a,b,R,rho):
    return R**(-a)*rho**(-b)*F(factorial(b)*comb(2*a+b,b),
                               (a+1)**2*(b+1)**2)
count=0
for R,rho in [(F(1),F(1,4)),(F(7,3),F(1,8)),(F(3,11),F(1,5))]:
    for a in range(54):
        r=a+1
        for b in range(64):
            for j in range(4):
                lhs=r**(3-j)*weight(a,b+j,R,rho)/F(r*r*(r+1)**2)/weight(a+2,b,R,rho)
                rhs=F(54,r)*R**2*rho**(-j)*F(25,(j+1)**2)*3**(4-j)
                assert lhs<=rhs,(a,b,j)
                count+=1
print('PASS all four scalar jet ratios:',count)
