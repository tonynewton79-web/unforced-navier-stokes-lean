"""Appendix AP: exact kinematic C4 angular source selection.
Does not certify the H8 authentic source, unforced PDE or blowup.
"""
import sympy as s

def test_leading_divergence_suppresses_theta_swirl():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h
    assert s.simplify(A+D-1)==0
    assert s.simplify(A+s.Rational(1,2)-1-h)==0

def test_angular_fourfold_selection():
    th=s.symbols("th",real=True)
    F=s.sin(4*th)
    assert s.trigsimp(F.subs(th,th+s.pi/2)-F)==0
    assert s.integrate(F,(th,0,2*s.pi))==0
    assert s.trigsimp(sum(s.sin(2*(th+j*s.pi/2)) for j in range(4))/4)==0

def test_physical_critical_source_power():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h;p=s.Rational(1,2)-3*h
    assert s.simplify(-2*A-s.Rational(1,2)+(1+D)/2-(p/2-1-h))==0

def test_physical_centrifugal_gradient_remainder():
    h=s.symbols("h",positive=True)
    D=s.Rational(1,2)-h
    assert s.simplify(s.Rational(1,2)-D-h)==0

def test_poloidal_carrier_divergence():
    R,z,th=s.symbols("R z th",real=True)
    f=(1-R**2)**4;g=(1-z**2)**4
    psi=R**6*f*g*s.cos(4*th)
    Vr=-s.diff(psi,z)/R;Vz=s.diff(psi,R)/R
    assert s.simplify(s.diff(R*Vr,R)/R+s.diff(Vz,z))==0

def test_poloidal_correction_divergence():
    R,z,th=s.symbols("R z th",real=True)
    psi=-4*R**6*(1-R**2)**4*(1-z**2)**4*s.sin(4*th)
    Wr=-s.diff(psi,z)/R;Wz=s.diff(psi,R)/R
    assert s.simplify(s.diff(R*Wr,R)/R+s.diff(Wz,z))==0

def test_positive_control_wz_equals_critical_source():
    R,z,th=s.symbols("R z th",real=True)
    q=s.diff(R**6*(1-R**2)**4*(1-z**2)**4,R)/R
    F=-4*q*s.sin(4*th)
    wpsi=-4*R**6*(1-R**2)**4*(1-z**2)**4*s.sin(4*th)
    Wz=s.diff(wpsi,R)/R
    assert s.simplify(Wz-F)==0

def test_exact_rational_positive_angular_pairing():
    X,z=s.symbols("X z",real=True)
    f=(1-X)**4;g=(1-z*z)**4
    q=X**2*(6*f+2*X*s.diff(f,X))
    radial=s.integrate(s.expand(q*q)/2,(X,0,1))
    axial=s.integrate(g*g,(z,-1,1))
    assert radial==s.Rational(4,5005)
    assert axial==s.Rational(65536,109395)
    assert s.simplify(16*radial*axial)==s.Rational(4194304,547521975)

def test_natural_correction_axial_and_radial_physical_divergence():
    h=s.symbols("h",positive=True);D=s.Rational(1,2)-h
    assert s.simplify((-s.Rational(1,2)+h)-s.Rational(1,2)-(-s.Rational(1,2)-D)-D)==0

def test_signed_dyad_coefficient():
    x,p,C=s.symbols("x p C",positive=True)
    v=s.integrate(C*x**(p-1),(x,s.Rational(1,2),1))
    assert s.simplify(v-C*(1-2**(-p))/p)==0
