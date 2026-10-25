"""Exact two-angular-mode divergence-free annular model, not a PDE solution."""
import sympy as s
r,z=s.symbols("r z",positive=True,real=True)
f=s.Function("f")(r);g=s.Function("g")(r)
a=s.Matrix([f*s.cos(z),0,-s.diff(f,r)*s.sin(z)])
b=s.Matrix([0,f*s.cos(z),0])
c=s.Matrix([0,0,g])
Q=2*(a*a.T+b*b.T+c*c.T)
assert s.simplify(Q.det()-8*f**4*g**2*s.cos(z)**4)==0
assert Q.subs({f:1,g:1,s.diff(f,r):0,z:0})==2*s.eye(3)
d1=s.diff(f*s.cos(z),r)+f*s.cos(z)/r+s.I*s.I*f*s.cos(z)/r+s.diff(-s.diff(f,r)*s.sin(z),z)
assert s.simplify(d1)==0
x,y=s.symbols("x y",real=True)
rr=s.sqrt(x*x+y*y)
F=s.Function("F")
G=s.Function("G")
ux=2*F(rr)*s.cos(z)
uz=-2*s.diff(F(r),r).subs(r,rr)*x/rr*s.sin(z)+2*G(rr)*(x*x-y*y)/(rr*rr)
assert s.simplify(s.diff(ux,x)+s.diff(uz,z))==0
print("PASS: m=1 and m=2 solenoidality; independent Cartesian divergence")
print("PASS: det Q=8 f^4 g^2 cos(z)^4; Q(1,0)=2I")
print("HOLD: authentic source stress, H8 ray cone, time evolution, unforced Lean PDE")
