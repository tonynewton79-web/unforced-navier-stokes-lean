"""Exact replay for the complete seven-channel H_k and eight-channel
symmetrized Q_k quadratic pressure sources (Zenodo 23474915).

Proves sample identities with exact symbolic arithmetic, and finite exact
checks of the all-index inequalities proved separately in the manuscript.
Does NOT verify the full Navier--Stokes PDE theorem or replace a Lean proof.
"""
import math
import sympy as s
from fractions import Fraction as F
from itertools import product
z=s.symbols('z')
def BG(h):
    L=1-2*h*z*z
    return 2*z/L,(1-z*z)/L
counts=[0,0]
for h,i,j,ao,bo in product(
    (s.Rational(1,200),s.Rational(1,500)),
    (1,2,4),(1,3,5),(0,2),(0,3)):
    a=i+ao;b=j+bo;k=i+j;N=a+b
    B,G=BG(h);D=s.Rational(1,2)-h
    r=b+1
    alpha=1-(D+2*h*j)/r
    e=2*h*j-1-b
    theta=2*h*k-N-2
    f=1+3*z-z**3/7;u=2-z/5+z*z
    W=alpha*B*f-G*s.diff(f,z)/r
    hsrc=u*(G*s.diff(W,z)+B*e*W)
    c=[alpha*(G*s.diff(B,z)+e*B*B),
       alpha*B*G-(G*s.diff(G,z)+e*B*G)/r,
       -G*G/r]
    dct={}
    for q,C in enumerate(c):
        for p,qq,term in ((0,q,B*theta*C+G*s.diff(C,z)),
                          (1,q,G*C),(0,q+1,G*C)):
            dct[(p,qq)]=dct.get((p,qq),0)+term
    assert len(dct)==7
    rex=-sum((co*s.diff(u,z,p)*s.diff(f,z,q)
             for (p,q),co in dct.items()),s.Integer(0))
    source=-(G*s.diff(hsrc,z)+B*theta*hsrc)
    for zz in (s.Rational(-1,2),s.Integer(0),s.Rational(2,3)):
        assert s.cancel((rex-source).subs(z,zz))==0
        counts[0]+=1

    ai=i+ao;aj=j+bo;ri=ai+1;rj=aj+1
    alphai=1-(D+2*h*i)/ri;alphaj=alpha
    wi=[alphai*B,-G/ri];wj=[alphaj*B,-G/rj]
    Wi=wi[0]*u+wi[1]*s.diff(u,z)
    Wj=wj[0]*f+wj[1]*s.diff(f,z)
    Q={}
    for p in range(2):
      for q in range(2):
        coef=wi[p]*wj[q]
        for pp,qq,v in ((p,q,B*theta*coef+G*s.diff(coef,z)),
                        (p+1,q,G*coef),(p,q+1,G*coef)):
            Q[(pp,qq)]=Q.get((pp,qq),0)+v
    assert len(Q)==8
    qu=-(G*s.diff(Wi*Wj,z)+B*theta*Wi*Wj)
    qi=-sum((v*s.diff(u,z,p)*s.diff(f,z,q)
             for (p,q),v in Q.items()),s.Integer(0))
    for zz in (s.Rational(-1,2),s.Integer(0),s.Rational(2,3)):
        assert s.cancel((qu-qi).subs(z,zz))==0
        counts[1]+=1
print('PASS exact source-native H and Q normal forms:',*counts)

def w(N,b,R,rho):
    return R**(-N)*rho**(-b)*F(math.factorial(b)*math.comb(2*N+b,b),(N+1)**2*(b+1)**2)

smooth=[0,0]
for R,rho in ((F(1),F(1)),(F(3,2),F(1,4)),(F(2,7),F(3,5))):
  for N in range(2,31):
    for k in (2,N):
      t=N+k+2
      for beta in range(30):
        for d in range(4):
          wr=w(N,beta+d,R,rho)/w(N+2,beta,R,rho)
          hrat=F(t**(3-d),(N+1)*(N+2)**2)*wr
          qrat=(F(t**(2-d)) if d<=2 else F(1,t))*wr/(N+2)**2
          assert hrat<=2304*2**(3-d)*R*R/rho**d
          assert qrat<=2304*2**max(2-d,0)*R*R/rho**d
          smooth[0]+=1
print('PASS exact all-four-jet smoothing tests:',smooth[0])
for p in range(2):
  for q in range(4-p):
    d=p+q
    for b in range(90):
      for ell in range(b+1):
        assert math.comb(b,ell)<=math.comb(b+d,p+ell)
        smooth[1]+=1
print('PASS exact unsigned mixed Leibniz comparisons:',smooth[1])
assert 11*64**2*25**3==704000000
assert 32*64**2*25**3==2048000000
print('PASS explicit multiplier majorant constants')
