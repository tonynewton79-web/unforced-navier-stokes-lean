"""Exact source-conditional arithmetic regression, NOT source validation."""
from fractions import Fraction as F
assert (1+8*F(1,10000))*(F(93,40)+F(1,1000)) <F(233,100)
assert 4*F(1,2000)*F(233,100)<F(1,200)
assert 40960*F(1,20)**28<F(1,10**31)
assert 2*2560*F(1,20)**28/(1-F(1,10**31))*(F(233,100)+F(1,2))<F(1,200)
assert F(1,200)+F(1001,1000)+F(1,200)<F(51,50)
assert F(1,2)-F(51,200)==F(49,200)
assert F(1,2)-F(3,20)*F(51,100)**2==F(92197,200000)>F(9,20)
count=0
for N in (20,21,25,30,50,75,100,250,1000):
 lam=F(1,N)
 for j in (100,200,500,1000):
  h=lam/j
  for k in (0,1,5,20,50):
   delta=40960*lam**28
   D=(1+8*delta)*(F(93,40)+h**7/3)
   eps=2560*lam**28/(1-delta)
   assert D<F(233,100)
   bound=lam/4*(4*h*D+4*(F(1,2)+h)*F(1,2)
                +2*eps*(D+F(1,2)))
   assert bound<F(51,200)*lam
   count+=1
print("PASS",count,"exact scalar instances; source-field hypotheses not certified")
