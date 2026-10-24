"""Exact source-native audit of remaining positive-order momentum terms,
complete direct delayed Z^[2] and pressure norm counterexample.

Local tests are not a Lean proof or physical solution. Main source:
DOI 10.5281/zenodo.23474915, equations (17),(18),(24)-(28),(37),(52).
"""
from fractions import Fraction as F
from math import comb, factorial
import sympy as s

eta=s.symbols("eta")
h=s.Rational(1,200); D=s.Rational(1,2)-h
B=2*eta/(1-2*h*eta**2)
G=(1-eta**2)/(1-2*h*eta**2)
U=2+eta+eta**2
P=3-eta+2*eta**3
bilinear=0
for i in range(1,7):
 for j in range(1,7):
  for ai in (i,i+1,i+3):
   for aj in (j,j+2):
    for beta,delta in ((-s.Rational(1,2)-h,0),(-1-h,1)):
     alpha=1-(D+2*h*i)/(ai+1)
     W=alpha*B*U-G*s.diff(U,eta)/(ai+1)
     original=W*(aj+delta)*P+U*(G*s.diff(P,eta)+B*(beta+2*h*j-aj)*P)
     normal=alpha*B*U*(aj+delta)*P-G*s.diff(U,eta)*(aj+delta)*P/(ai+1)+U*G*s.diff(P,eta)+U*B*(beta+2*h*j-aj)*P
     assert s.cancel(original-normal)==0
     assert 0<=alpha<=1
     assert abs(beta+2*h*j-aj)<=(1+abs(beta))*(ai+aj+1)
     bilinear+=1
print('PASS momentum source normal form:',bilinear)
delayed=0
for nu,beta in ((1,-s.Rational(1,2)-h),(2,-1-h)):
 for n in range(2,15):
  for a in (n-1,n,n+3,5*n):
   theta=beta+2*h*(n-1)-a;theta2=theta-D
   v=3+eta**2+eta**3
   Z1=G*s.diff(v,eta)+B*theta*v
   Z2=G*s.diff(Z1,eta)+B*theta2*Z1
   c2=G**2;c1=G*s.diff(G,eta)+G*B*(theta+theta2)
   c0=G*s.diff(B,eta)*theta+B**2*theta*theta2
   assert s.cancel(Z2-(c0*v+c1*s.diff(v,eta)+c2*s.diff(v,eta,2)))==0
   assert abs(theta)<=3*(a+1) and abs(theta2)<=3*(a+1)
   delayed+=1
print('PASS full delayed Z^2 expansion:',delayed)
def w(a,b,R,rho):
 return R**(-a)*rho**(-b)*F(factorial(b)*comb(2*a+b,b),(a+1)**2*(b+1)**2)
ratios=0
for R,rho in ((F(1),F(1,4)),(F(2,3),F(1,9)),(F(3,2),F(1,4))):
 for nu in (1,2):
  for n in range(2,25):
   for a in (n-1,n,n+4,2*n,5*n):
    for m in range(35):
     for d,cap in ((0,4*R),(1,8*R/rho),(2,8*R/rho**2)):
      actual=(a+1)**(2-d)*w(a,m+d,R,rho)/((a+1)*(a+nu)*w(a+1,m,R,rho))
      assert actual<=cap
      ratios+=1
print('PASS exact delayed inverse multiplier:',ratios)
mix=0
for m in range(160):
 for ell in range(m+1):
  assert comb(m,ell)<=comb(m+1,ell+1)
  assert comb(m,ell)<=comb(m+1,ell)
  mix+=1
print('PASS unsigned Leibniz comparisons:',mix)
z=s.I/4;r=s.Integer(2);lam=2*h
f=1/(1+4*s.I*eta)
W=B*(r-D-lam)*f/r-G*s.diff(f,eta)/r
Z=lambda f,q:s.cancel(G*s.diff(f,eta)+B*(q-r)*f)
p=s.cancel(Z(Z(W,lam),lam-D)/(2*r))
pole=s.simplify(s.limit((eta-z)**4*p,eta,z))
assert pole==-s.Rational(921187500,4103684801)*s.I
assert pole!=0
for m in range(100):
 assert 16*(m+1)**2-(m+4)**2==3*m*(5*m+8)
print('PASS exact nonzero order-four pressure pole and scalar norm divergence:',pole)
print('PASS total finite sample cases:',bilinear+delayed+ratios+mix+100+1)
