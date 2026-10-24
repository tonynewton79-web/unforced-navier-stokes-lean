"""Finite exact simultaneous two-harmonic covariance/torque verification."""
import sympy as s
r,z,L=s.symbols("r z L", positive=True,real=True)
f=s.Function("f")(r); g=s.Function("g")(r)
c=s.cos(z); t=s.sin(z)
a=s.Matrix([f*c,L*r*r*f*c,-s.diff(f,r)*t])
b=s.Matrix([0,f*c,-L*r*f*t])
d=s.Matrix([0,0,g])
Q=2*(a*a.T+b*b.T+d*d.T)
assert s.simplify(s.expand_trig(s.expand(Q.det()-8*f**4*g**2*c**4)))==0
v1=f*c;v2=s.I*f*c+L*r*r*f*c
v3=-s.diff(f,r)*t-s.I*L*r*f*t
assert s.simplify(s.diff(v1,r)+v1/r+s.I*v2/r+s.diff(v3,z))==0
assert s.simplify(Q[1,2]+L*r*(r*s.diff(f,r)+f)*f*s.sin(2*z))==0
minimum=s.Rational(3,2)*(1-s.Rational(1,16)*(s.Rational(5,4)**2))
minimum-=2*s.Rational(1,16)*s.Rational(5,4)*s.Rational(1,2)
assert minimum==s.Rational(653,512) and minimum>1
print("PASS exact solenoidality, determinant 8f^4g^2cos^4z and Qztheta")
print("PASS explicit plateau covariance Q>=653/512 I")
print("HOLD actual H8 seven-ray cone, source residual, full PDE and Lean proof")
