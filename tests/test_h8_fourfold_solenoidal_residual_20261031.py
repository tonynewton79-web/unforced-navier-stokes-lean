"""AQ: finite exact symbolic controls for the fourfold solenoidal test.
These checks do NOT certify a full unforced NS PDE solution or Lean theorem.
"""
import sympy as s

h=s.symbols("h",positive=True)
A=s.Rational(1,2)+h
D=s.Rational(1,2)-h
p=s.Rational(1,2)-3*h

def test_carrier_volume():
    assert s.simplify(1+D-2*A-p)==0

def test_critical_source_inner_product():
    assert s.simplify(D-2*A-(p-1))==0

def test_detector_L2_scale():
    assert s.simplify(-s.Rational(1,2)+(1+D)/2-D/2)==0

def test_detector_divergence_powers():
    assert s.simplify(-s.Rational(1,2)+h-s.Rational(1,2)-(-s.Rational(1,2)-D))==0

def test_detector_time_diffusion_scale():
    assert s.simplify(p/2+D/2-(p+h))==0

def test_mixed_convective_exponents():
    assert s.simplify(p/2+D/2+s.Rational(1,2)-A-p)==0
    assert s.simplify(p/2+D/2-h-p)==0

def test_quadratic_concentration_exponent():
    assert s.simplify(p/2+D/2+s.Rational(1,2)-(p+s.Rational(1,2)+h))==0

def test_h_one_tenth_spike_threshold():
    assert (-s.Rational(1,2)-2*h).subs(h,s.Rational(1,10))==-s.Rational(7,10)

def test_solenoidal_detector_profile():
    R,th,eta,eps=s.symbols("R th eta eps",real=True)
    F=R**4*(1-R**2)**4*(1-eta**2)**4*s.sin(4*th)
    Ztheta=eps*R*s.diff(F,eta,th)
    Zz=-s.diff(F,th,2)
    assert s.simplify(s.diff(Ztheta,th)/R+eps*s.diff(Zz,eta))==0

def test_angular_positive_definiteness():
    th=s.symbols("th",real=True)
    f=s.sin(4*th)
    assert s.integrate(f*(-s.diff(f,th,2)),(th,0,2*s.pi))==16*s.pi

def test_exact_C4_polynomial_constant():
    X,eta=s.symbols("X eta",real=True)
    f=(1-X)**4;g=(1-eta**2)**4
    q=X**2*(6*f+2*X*s.diff(f,X))
    radial=s.integrate(s.expand(q*q)/2,(X,0,1))
    axial=s.integrate(g*g,(eta,-1,1))
    assert radial==s.Rational(4,5005)
    assert axial==s.Rational(65536,109395)
    assert s.simplify(16*16*radial*axial)==s.Rational(67108864,547521975)

def test_fourfold_angular_mean_zero():
    th=s.symbols("th",real=True)
    assert s.integrate(s.sin(4*th),(th,0,2*s.pi))==0

def test_dyadic_source_constant():
    x,t,q=s.symbols("x t q",positive=True)
    z=s.integrate(x**(q-1),(x,t/2,t))
    assert s.simplify(z-t**q*(1-2**(-q))/q)==0
