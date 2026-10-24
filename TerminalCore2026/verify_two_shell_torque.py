"""Exact rational two-shell torque cancellation; polynomial test profiles are C3."""
import sympy as s
r,z=s.symbols("r z",real=True)
f1=(r-1)**4*(2-r)**4
f2=(r-3)**4*(4-r)**4
I1=s.integrate(r**3*f1**2,(r,1,2))
I2=s.integrate(r**3*f2**2,(r,3,4))
assert I1==s.Rational(29,1847560)
assert I2==s.Rational(3269,16628040)
lam2=-I1/I2
assert lam2==s.Rational(-261,3269)
assert s.simplify(2*(I1+lam2*I2)*s.cos(2*z))==0
assert s.simplify(2*I1*s.cos(2*z))!=0
print("PASS exact two-shell cancellation",I1,I2,lam2)
