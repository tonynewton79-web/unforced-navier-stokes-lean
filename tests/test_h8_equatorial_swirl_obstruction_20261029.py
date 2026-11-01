"""Exact Appendix P SymPy regressions. H8 authentic source remains OPEN."""
import sympy as s
x,r,tau=s.symbols("x r tau",positive=True)
A=s.Rational(3,5); h=s.Rational(1,10); D=s.Rational(2,5)
f=s.exp(-x/(1-x))
V=s.sqrt(2*x)*s.diff(x*f,x)/4
def D0(v):
    return A*v+x*s.diff(v,x)-2*s.diff(v,x)-2*x*s.diff(v,x,2)+v/(2*x)
def test_two_point_rational_separation():
    R=s.cancel(D0(V)/V)
    a=s.simplify(R.subs(x,s.Rational(1,4)))
    b=s.simplify(R.subs(x,s.Rational(1,2)))
    assert a==s.Rational(25819,810)
    assert b==-s.Rational(109,10)
    assert a-b==s.Rational(17324,405)
def test_nonzero_swirl_values():
    assert s.simplify(V.subs(x,s.Rational(1,4))-5*s.sqrt(2)*s.exp(-s.Rational(1,3))/72)==0
    assert s.simplify(V.subs(x,s.Rational(1,2))+s.exp(-1)/4)==0
def test_independent_physical_radial_calculation():
    u=tau**(-A)*V.subs(x,r*r/(2*tau))
    raw=-s.diff(u,tau)-(s.diff(u,r,2)+s.diff(u,r)/r-u/r**2)
    assert s.simplify(s.expand(raw-tau**(-A-1)*D0(V).subs(x,r*r/(2*tau))))==0
def test_source_exponent():
    assert s.simplify(-A-1+(1+D)/2+s.Rational(3,4)+3*h/2)==0
def test_angular_average_kills_nonaxisymmetric_pressure_gradient():
    th,R=s.symbols("th R",real=True)
    p=R**4*s.sin(4*th)+R**3*s.cos(3*th)
    assert s.integrate(s.diff(p,th),(th,0,2*s.pi))==0
