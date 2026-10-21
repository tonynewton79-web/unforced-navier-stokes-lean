"""Independent exact A11 source scalar envelope. Fixture is NOT source certified."""
from fractions import Fraction as F
lam,h,E,c0,ceta=F(1,20),F(1,10**6),F(1,10**6),F(1,10**8),F(1,10**8)
B0,B1=F(640,3),F(1715200,9)
qminus,qplus=1-B0*c0,1+B0*c0
D=F(93,20)+F(2,3)*h**7
stress=E/qminus*(2*qplus**2*(F(1,2)+h+h*D)+qplus*B0*ceta*D)
slope=B1*c0/qminus
assert stress<lam/2 and slope<lam/2
def g(e,ci,ce):
 q=1-B0*ci
 if q<=0:return False,False
 d=F(93,20)+F(2,3)*h**7
 return (e/q*(2*(1+B0*ci)**2*(F(1,2)+h+h*d)+(1+B0*ci)*B0*ce*d)<=lam/2,
         B1*ci/q<=lam/2)
assert g(E,F(1,10**4),ceta)[1] is False
assert g(E,c0,F(100))[0] is False
assert g(F(1),c0,ceta)[0] is False
print('PASS exact rational A11 alternative stress/slope fixture and three falsifiers')
print('FAIL CLOSED: no certified A11 source-data tuple supplied')
