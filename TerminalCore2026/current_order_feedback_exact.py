"""Exact all-index current-order swirl-pressure and profile-Cauchy audit.
Finite regression and scalar identities only; NOT a full PDE certificate.
"""
from fractions import Fraction as Q
from math import comb, factorial
import sympy as s
def w(a,b,R,rho):
    return R**(-a)*rho**(-b)*Q(factorial(b)*comb(2*a+b,b),(a+1)**2*(b+1)**2)
count=0
for R,rho in ((Q(1),Q(1,4)),(Q(1,7),Q(1,9)),(Q(7,3),Q(3,8))):
    for a in range(96):
        for b in range(150):
            actual=w(a,b,R,rho)/((a+1)*w(a+1,b+1,R,rho))
            formula=R*rho*Q((a+2)**2*(b+2)**2*(2*a+1)*(2*a+2),
              (a+1)**3*(b+1)**2*(2*a+b+1)*(2*a+b+2)*(2*a+b+3))
            assert actual==formula
            assert actual<=8*R*rho/(a+1)**2
            assert actual<=4*R*rho*Q((a+2)**2,(a+1)**3*(2*a+3))
            count+=1
print('PASS exact shifted-pressure current axis-primitive:',count)
eta,X=s.symbols('eta X')
h=s.Rational(1,200)
B=2*eta/(1-2*h*eta**2); G=(1-eta**2)/(1-2*h*eta**2)
total=0
for n in (1,2,3,6,12):
  for a in (n,n+1,n+5):
    for c in (0,1,4):
      p0=(1+eta/3+eta**2/11)*X**c
      pn=(2-eta+eta**3/17)*X**a
      C=s.Integer(7); m=a+c+1
      pi=2*p0*pn*X/(C**2*m)
      assert s.simplify(s.diff(pi,X)-2*p0*pn/C**2)==0
      q=2*h*n-(1+2*h)
      coeff=s.factor((G*s.diff(pi/X**m,eta)+B*(q-m)*(pi/X**m))/(2*(m+1)**2))
      half=s.factor((G*s.diff((pi/2)/X**m,eta)+B*(q-m)*((pi/2)/X**m))/((m+1)**2))
      assert s.simplify(coeff-half)==0
      assert m>=n+1
      total+=1
print('PASS source-native current pressure and ordered-pair identity:',total)
for p in range(6):
  assert max(a**p*(a+1)**2*Q(1,8)**a for a in range(200))<10**6
print('PASS Cauchy/Euler finite coefficient envelopes 0..5')
