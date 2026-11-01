"""Appendix AO exact radial primitive and H8 exponent checks.
Algebraic evidence, not a source-matched unforced PDE construction.
"""
import sympy as s

def test_centrifugal_potential_exact():
    r,z=s.symbols("r z",positive=True)
    U=r*(1-r**2)**2*(1-z**2)**2
    psi=(1-r**2)**5*(1-z**2)**4/s.Integer(10)
    assert s.simplify(s.diff(psi,r)+U**2/r)==0

def test_primitive_axial_derivative():
    r,z=s.symbols("r z")
    psi=(1-r**2)**5*(1-z**2)**4/s.Integer(10)
    assert s.simplify(s.diff(psi,z)+(s.Rational(4,5)*z*(1-r**2)**5*(1-z**2)**3))==0

def test_divergence_free_streamfunction():
    r,z=s.symbols("r z",positive=True)
    phi=(1-r**2)**5*(1-z**2)**5
    wr=-r*s.diff(phi,z);wz=2*phi+r*s.diff(phi,r)
    assert s.simplify(s.diff(r*wr,r)/r+s.diff(wz,z))==0

def test_cylindrical_potential_pairing_total_divergence():
    r,z=s.symbols("r z",positive=True)
    phi=(1-r**2)**5*(1-z**2)**5
    psi=(1-r**2)**5*(1-z**2)**4/s.Integer(10)
    wr=-r*s.diff(phi,z);wz=2*phi+r*s.diff(phi,r)
    lhs=s.expand(r*wr*s.diff(psi,r)+r*wz*s.diff(psi,z))
    rhs=s.expand(s.diff(r*wr*psi,r)+s.diff(r*wz*psi,z))
    assert s.simplify(lhs-rhs)==0

def test_scale_primitive_z_l2():
    h=s.symbols("h");A=s.Rational(1,2)+h;D=s.Rational(1,2)-h;p=s.Rational(1,2)-3*h
    assert s.simplify(-2*A-D+(1+D)/2-(p/2-1))==0

def test_scale_centrifugal_l2_worse_by_h():
    h=s.symbols("h");A=s.Rational(1,2)+h;D=s.Rational(1,2)-h;p=s.Rational(1,2)-3*h
    assert s.simplify(-2*A-s.Rational(1,2)+(1+D)/2-(p/2-1-h))==0

def test_scale_remaining_convection_l2():
    h=s.symbols("h");A=s.Rational(1,2)+h;D=s.Rational(1,2)-h;p=s.Rational(1,2)-3*h
    assert s.simplify(-2*A-D+(1+D)/2-(p/2-1))==0

def test_size_of_natural_correction_deficit():
    h=s.symbols("h");D=s.Rational(1,2)-h;p=s.Rational(1,2)-3*h
    assert s.simplify(-s.Rational(1,2)+(1+D)/2-p/2-h)==0

def test_retention_amp_floor():
    h=s.symbols("h");D=s.Rational(1,2)-h;p=s.Rational(1,2)-3*h
    assert s.simplify(p/2+h/2-(1+D)/2+s.Rational(1,2)+h/2)==0
    assert (-s.Rational(1,2)-h/2).subs(h,s.Rational(1,10)) == -s.Rational(11,20)

def test_axisymmetric_source_necessity():
    r,z,th=s.symbols("r z th")
    u=r*(1-r**2)**2*(1-z**2)**2
    assert s.diff(u,th)==0
    assert s.simplify(s.diff(u*(1+s.sin(th)),th))!=0
