#!/usr/bin/env python3
"""Attack55 full physical Poisson pressure for a rational 1/r Leray trial.
Verifies exact source, radial pressure ODE and momentum obstruction.
This does NOT validate existence, an inverse, a singularity or any Lean certificate.
"""
import sympy as S
R,r,z,mu,a,b=S.symbols('R r z mu a b',positive=True,real=True)
H=1+r*r+z*z
ur=b*r*z/H**S.Rational(3,2)
ut=a*r/H
uz=b*(2+r*r+2*z*z)/H**S.Rational(3,2)
assert S.simplify(S.diff(r*ur,r)/r+S.diff(uz,z))==0
src_a=S.factor((-2*(ut/r)*S.diff(ut,r)).subs({a:1,b:0}))
src_b=S.factor((S.diff(ur,r)**2+(ur/r)**2+S.diff(uz,z)**2+
                 2*S.diff(ur,z)*S.diff(uz,r)).subs({a:0,b:1}))
A0=2*(R*R-3)/(3*(1+R*R)**3)
A2=-8*R*R/(3*(1+R*R)**3)
B0=2*R*R*(R*R-5)/(3*(1+R*R)**4)
B2=4*R*R*(4*R*R+7)/(3*(1+R*R)**4)
P2=(3*mu**2-1)/2
for source,coeff0,coeff2 in ((src_a,A0,A2),(src_b,B0,B2)):
  expanded=(coeff0+coeff2*P2).subs(
      {R:S.sqrt(r*r+z*z),mu:z/S.sqrt(r*r+z*z)})
  assert S.simplify(source-expanded)==0

qa0=-1/(3*(1+R*R))
qb0=-(2*R*R+1)/(6*(1+R*R)**2)
qa2=((1+R*R)*S.atan(R)-R-S.Rational(2,3)*R**3)/(R**3*(1+R*R))
qb2=(16*R**5+35*R**3+21*R-21*(1+R*R)**2*S.atan(R))/(12*R**3*(1+R*R)**2)
for q,source,ell in ((qa0,A0,0),(qa2,A2,2),(qb0,B0,0),(qb2,B2,2)):
  assert S.factor(S.diff(q,R,2)+2*S.diff(q,R)/R-ell*(ell+1)*q/R**2+source)==0
  assert S.limit(q,R,S.oo)==0
assert S.limit(qa2,R,0)==0 and S.limit(qb2,R,0)==0
assert S.series(qa2,R,0,4).removeO()==-2*R**2/15
assert S.series(qb2,R,0,4).removeO()==2*R**2/5
q=a*a*(qa0+qa2*P2)+b*b*(qb0+qb2*P2)
assert S.simplify(q.subs({R:1,mu:0,a:1,b:1})-(-S.Rational(5,8)+3*S.pi/32))==0

# The full axial PDE at origin with arbitrary time-dependent b has:
# (d_s W_z)(0)=2b', linear drift b, -Delta W_z=10b,
# nonlinear advection=0, grad q=0.
axial=(uz+r*S.diff(uz,r)+z*S.diff(uz,z))/2-(
 S.diff(uz,r,2)+S.diff(uz,r)/r+S.diff(uz,z,2))+
 ur*S.diff(uz,r)+uz*S.diff(uz,z)
assert S.limit(S.limit(S.simplify(axial),r,0),z,0)==11*b

# On the z=0 plane nonlinear angular convection vanishes for all a,b.
th=(ut+r*S.diff(ut,r)+z*S.diff(ut,z))/2-(
 S.diff(ut,r,2)+S.diff(ut,r)/r+S.diff(ut,z,2)-ut/r**2)+(
 ur*S.diff(ut,r)+uz*S.diff(ut,z)+ur*ut/r)
assert S.simplify(th.subs(z,0)-a*r*(11+3*r*r)/(1+r*r)**3)==0

# Independent direct Cartesian pressure-source regression at three points.
x,y=S.symbols('x y',real=True); HH=1+x*x+y*y+z*z
V=S.Matrix([-y/HH+x*z/HH**S.Rational(3,2),
            x/HH+y*z/HH**S.Rational(3,2),
            (2+x*x+y*y+2*z*z)/HH**S.Rational(3,2)])
D=S.Matrix(3,3,lambda i,j:S.diff(V[i],(x,y,z)[j]))
for xx,yy,zz in ((1,0,0),(1,0,1),(2,1,1)):
  pt={x:xx,y:yy,z:zz};rad=S.sqrt(xx*xx+yy*yy+zz*zz)
  lhs=S.simplify(sum(D[i,j].subs(pt)*D[j,i].subs(pt) for i in range(3) for j in range(3)))
  rhs=S.simplify((A0+B0+(A2+B2)*P2).subs({R:rad,mu:S.Rational(zz)/rad}))
  assert S.simplify(lhs-rhs)==0

print("PASS: exact nonlinear source and all four closed Poisson pressure modes")
print("PASS: exact independent Cartesian spot checks and full angular/axial PDE obstruction")
print("HOLD: genuine nonzero profile, bounded inverse, all 15 cell conditions, Lean singularity")
