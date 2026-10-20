"""Exact rational validation of fixed-radius, factorial inverse and two-shift majorant.

Does not verify analytic Banach operator norms, the imported profiles, the
PDE source normalization or a complete Lean proof.
"""
from fractions import Fraction as F
from math import factorial

cnt=0
for n in range(1,96):
 for m in range(n,120):
  h=F(1,200)
  for beta in (-F(101,100),-F(51,100),F(99,200)):
   assert abs(beta+2*h*n)/F(m+1) <= abs(beta)+2*h
   cnt+=1
print('PASS fixed-order parameters on higher radial ideals',cnt)

cnt=0
for n in range(1,50):
 for ell in range(90):
  product=F(factorial(n),factorial(n+ell))
  assert product<=F(1,factorial(ell))
  alt=F(1)
  for m in range(n,n+ell):alt*=F(1,m+1)
  assert alt==product
  cnt+=1
print('PASS factorial Volterra product inequalities',cnt)

cnt=0
for n in range(3,400):
 qn=sum((F(1,(i+1)**2*(n-i+1)**2) for i in range(1,n)),F())
 qm=sum((F(1,(i+1)**2*(n-i)**2) for i in range(1,n-1)),F())
 assert qn*(n+1)**2<=4
 assert qm*(n+1)**2<=4
 assert F((n+1)**2,n*n)<=2
 assert F((n+1)**2,(n-1)**2)<=4
 cnt+=4
print('PASS two-shift quadratic convolution comparisons',cnt)

for H in (F(0),F(1,50),F(1,5),F(1),F(11),F(1000)):
 M=F(1,32*(1+H))
 T=max(F(2),16*H,6*(H+1))
 assert 2*H/T+4*H/T**2+4*H*M*(1+1/T)<1
print('PASS constructive scalar majorant parameters')

for n in (1,2,5):
 for C in (F(1),F(7),F(80)):
  length=36
  u=[F(0)]*length
  u[0]=F(1)
  for ell in range(1,length):
   u[ell]=F(C,n+ell)*u[ell-1]
  for ell in range(length):
   left=u[ell]-(F(C,n+ell)*u[ell-1] if ell else F(0))
   assert left==(F(1) if ell==0 else F(0))
   assert u[ell]==C**ell*F(factorial(n),factorial(n+ell))
print('PASS exact finite triangular inverse with strong startup feedback')
