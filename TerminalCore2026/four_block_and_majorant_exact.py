"""Exact checks of the four current-order sources and scalar majorant.
Uses SymPy identities from (17),(18),(24),(47)-(50), Zenodo 23474915.
No analytic norm estimate is inferred from the tests alone.
"""
import sympy as s
from fractions import Fraction as F
from math import isqrt
L, mu,D,eta,d,U0,v,phi,fe,fx=s.symbols("L mu D eta d U0 v phi fe fx")
G=(-1+2*eta*U0)/L
H=(D*eta+d*U0)/L
K=(1-2*eta*U0)/L+v
source=(-mu*phi+D*eta*fe+fx)/L+v*(fx+phi)+U0*(2*mu*eta*phi+d*fe-2*eta*fx)/L
assert s.cancel(source-(mu*G*phi+v*phi+H*fe+K*fx))==0
X,f0,f0x,u,AU,AUe,lambdaD,q=s.symbols("X f0 f0x u AU AUe lambdaD q")
Vn=X*(2*eta*u-2*eta*lambdaD*AU-d*AUe)/L
assert s.cancel(Vn*(f0x+f0/X)+q*u -
      ((X*f0x+f0)/L)*(2*eta*u-2*eta*lambdaD*AU-d*AUe)-q*u)==0
u0x,zc=s.symbols("u0x zc")
vsource=(-mu*u+D*eta*fe+fx)/L+v*fx+
         U0*(2*mu*eta*u+d*fe-2*eta*fx)/L+
         zc*u + (X*u0x/L)*(2*eta*u-2*eta*lambdaD*AU-d*AUe)
assert s.cancel(vsource-(mu*G*u+H*fe+K*fx+zc*u+
         (X*u0x/L)*(2*eta*u-2*eta*lambdaD*AU-d*AUe)))==0
p,pe,px,z=s.symbols("p pe px z")
assert s.cancel((2*z*eta*p+d*pe-2*eta*px)/L -
      (z*(2*eta/L)*p+(d/L)*pe+(-2*eta/L)*px))==0
print("PASS four exact block source identities")
for n in range(2,301):
    c=sum((F(1,(i+1)**2*(n-i+1)**2) for i in range(1,n)),F(0))
    assert c<=F(4,(n+2)**2),n
print("PASS 299 rational convolution inequalities")
for C0,C1,A1,A2 in [(F(1),F(1),F(2),F(7)),
                    (F(5),F(3),F(12),F(11)),
                    (F(1,7),F(5,4),F(100),F(1))]:
    M=F(1,16*(1+C1)); R=F(1)
    while not (R>=8*C0 and R*R>=16*C0 and
               M*R>=4*A1 and M*R*R>=9*A2):
        R*=2
    A=[F(0),A1,A2]
    for n in range(3,40):
        value=C0*(A[n-1]+A[n-2])+C1*sum(
            (A[i]*A[n-i] for i in range(1,n)),F(0))
        A.append(value)
        assert value<=M*R**n/F((n+1)**2)
    print("PASS constructive majorant:",C0,C1,A1,A2,M,R)
