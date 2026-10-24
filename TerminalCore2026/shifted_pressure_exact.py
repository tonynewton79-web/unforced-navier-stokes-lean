"""Exact-rational regression for the one-jet shifted pressure-space repair.

Source: Newton, Zenodo 23474915, equations (17),(18),(24),(27),(28),(37).
These finite tests do not replace the analytic proof or certify Theorem 1.1.
"""
from fractions import Fraction as F
from math import factorial, comb
import sympy as s

def w(a,b,R,rho):
    return R**(-a)*rho**(-b)*F(factorial(b)*comb(2*a+b,b),
                               (a+1)**2*(b+1)**2)
count=0
for R,rho in [(F(1),F(1,4)),(F(7,3),F(1,9)),(F(3,8),F(1,2))]:
    for n in range(2,18):
        for a in range(n-2,n+14):
            t=a+n+1
            for b in range(24):
                lhs=w(a,b+3,R,rho)/((a+1)**2*w(a+1,b+1,R,rho))
                exact=R/rho**2*F(
                    (2*a+1)*(2*a+2)*(a+2)**2,(a+1)**4)*F((b+2)**2,(b+4)**2)
                assert lhs==exact and lhs<=8*R/rho**2
                count+=1
                for j in range(4):
                    lhs=t**(3-j)*w(a,b+j,R,rho)/(
                         (a+1)**2*w(a+1,b+1,R,rho))
                    assert lhs<=32*3**(3-j)*R*rho**(1-j)
                    count+=1
print('PASS shifted-pressure four-jet weights:',count)
count=0
for R,rho in [(F(1),F(1,4)),(F(1,9),F(1,9))]:
    for n in range(1,25):
        q=F(n,100)-F(101,100)
        for a in range(n-1,n+20):
            for b in range(30):
                t1=w(a,b+1,R,rho)/(a+1)**2/w(a+1,b,R,rho)
                t2=w(a,b+2,R,rho)/(a+1)**2/w(a+1,b,R,rho)
                assert t1<=8*R/(rho*(a+1))
                assert t2<=8*R/rho**2
                assert abs(q-a)*t1<=8*R/rho
                count+=3
print('PASS pressure-to-velocity weights:',count)
count=0
for rho in (F(1,4),F(1,6)):
    for a in range(17):
        for b in range(60):
            for ell in range(b+1):
                ratio=comb(b,ell)*factorial(ell)*w(a,b-ell+1,F(1),rho)/w(a,b+1,F(1),rho)
                assert ratio<=rho**ell*(ell+1)**2
                count+=1
print('PASS pressure multiplier Leibniz:',count)
eta=s.symbols('eta')
h=s.Rational(1,200)
G=(1-eta**2)/(1-2*h*eta**2)
B=2*eta/(1-2*h*eta**2)
D=s.Rational(1,2)-h
r=2; lam=2*h
f=1/(1+4*s.I*eta)
W=B*(r-D-lam)*f/r-G*s.diff(f,eta)/r
Z=lambda x,q:s.cancel(G*s.diff(x,eta)+B*(q-r)*x)
p=s.cancel(Z(Z(W,lam),lam-D)/(2*r))
z=s.I/4
pole=s.simplify(s.limit((eta-z)**4*p,eta,z))
assert pole==-s.Rational(921187500,4103684801)*s.I
A=s.Rational(1,2)+h
v=s.cancel((G*s.diff(p,eta)+B*(2*h*3-2*A-2)*p)/18)
p5=s.simplify(s.limit((eta-z)**5*v,eta,z))
assert p5==s.Rational(1044012500000,19709998099203)*s.I
print('PASS exact pressure pole and regularized velocity restoration')
