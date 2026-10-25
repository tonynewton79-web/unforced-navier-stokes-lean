"""Adversarial independent real-angle replay for the two-frequency stress."""
import sympy as s
th=s.symbols("th",real=True)
r,z,L,f,fp,g=s.symbols("r z L f fp g",real=True)
A=s.cos(z); B=s.sin(z)
vr=2*f*A*s.cos(th)
vt=2*f*A*(-s.sin(th)+L*r*r*s.cos(th))
vz=-2*fp*B*s.cos(th)+2*L*r*f*B*s.sin(th)+2*g*s.cos(2*th)
v=[vr,vt,vz]
Q=s.Matrix(3,3,lambda i,j:s.trigsimp(
    s.integrate(v[i]*v[j],(th,0,2*s.pi))/(2*s.pi)))
a=s.Matrix([f*A,L*r*r*f*A,-fp*B])
b=s.Matrix([0,f*A,-L*r*f*B])
d=s.Matrix([0,0,g])
M=2*(a*a.T+b*b.T+d*d.T)
for i in range(3):
    for j in range(3):
        assert s.simplify(s.trigsimp(Q[i,j]-M[i,j]))==0
assert s.simplify(Q.det()-8*f**4*g**2*A**4)==0
assert s.simplify(Q[1,2]+L*r*f*(f+r*fp)*s.sin(2*z))==0
print("PASS: 9/9 independent real-angle covariance entries; determinant and torque")
print("No source-specific unforced Navier-Stokes PDE reconstructed.")
