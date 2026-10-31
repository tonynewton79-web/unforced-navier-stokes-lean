"""Conditional axisymmetric swirl pressure-mode gate; not an H8 singularity proof."""
import sympy as sp

R, eta, theta, h, tau, x, y = sp.symbols(
    "R eta theta h tau x y", real=True, positive=True
)

def test_exact_compact_polynomial_swirl_pressure():
    v = R*(1-R**2)**3
    Pi = -(1-R**2)**7/sp.Integer(14)
    assert sp.simplify(sp.diff(Pi,R)-v**2/R)==0
    lap2 = sp.diff(Pi,R,2)+sp.diff(Pi,R)/R
    source = sp.diff(v**2,R)/R
    assert sp.simplify(lap2-source)==0
    assert Pi.subs(R,1)==0 and sp.diff(Pi,R).subs(R,1)==0
    assert sp.diff(Pi,R,2).subs(R,1)==0

def test_azimuthal_swirl_convective_centripetal_acceleration():
    F=(1-(x*x+y*y))**3
    vx=-y*F;vy=x*F
    assert sp.simplify(sp.diff(vx,x)+sp.diff(vy,y))==0
    cx=sp.expand(vx*sp.diff(vx,x)+vy*sp.diff(vx,y))
    cy=sp.expand(vx*sp.diff(vy,x)+vy*sp.diff(vy,y))
    assert sp.simplify(cx+x*F**2)==0
    assert sp.simplify(cy+y*F**2)==0

def test_leading_slice_solenoidality_scales():
    D=sp.Rational(1,2)-h; A=sp.Rational(1,2)+h
    p=sp.Rational(1,2)-3*h
    assert sp.simplify((-sp.Rational(1,2)-D)-(-1)-h)==0
    assert sp.simplify(sp.Rational(1,2)+D-sp.Rational(1,2)-2*A-(p-1))==0

def test_zero_normal_flux_for_planar_solen_example():
    a=sp.symbols('a',real=True,positive=True)
    v1=x*x-y*y;v2=-2*x*y
    assert sp.diff(v1,x)+sp.diff(v2,y)==0
    xx=a*sp.cos(theta);yy=a*sp.sin(theta)
    normal=v1.subs({x:xx,y:yy})*sp.cos(theta)+v2.subs({x:xx,y:yy})*sp.sin(theta)
    assert sp.simplify(sp.integrate(sp.expand_trig(normal),(theta,0,2*sp.pi)))==0

def test_angular_pressure_pair_can_be_signed():
    t=sp.symbols('t',real=True)
    normal=sp.cos(t)
    assert sp.integrate(normal,(t,0,2*sp.pi))==0
    assert sp.simplify(sp.integrate(sp.cos(t)*normal,(t,0,2*sp.pi))-sp.pi)==0
    assert sp.simplify(sp.integrate(-sp.cos(t)*normal,(t,0,2*sp.pi))+sp.pi)==0

def test_separable_axial_envelope():
    b=sp.Function('b')(eta)
    v=R*(1-R**2)**3*b
    Pi=-(1-R**2)**7*b*b/sp.Integer(14)
    assert sp.simplify(sp.diff(Pi,R)-v*v/R)==0

def test_pressure_polarization_preserves_cross_term():
    a,b,L=sp.symbols('a b L',real=True)
    assert sp.expand((a+L*b)**2-a*a-2*L*a*b-(L*b)**2)==0

def test_nonzero_mode_selection_and_zero_axisym_pairing():
    t=sp.symbols('t',real=True)
    q=2*sp.cos(t)+3*sp.sin(2*t)
    assert sp.integrate(q,(t,0,2*sp.pi))==0
    assert sp.integrate(7*q,(t,0,2*sp.pi))==0
    assert sp.simplify(sp.integrate(sp.cos(t)*q,(t,0,2*sp.pi))-2*sp.pi)==0
    assert sp.simplify(sp.integrate(sp.sin(2*t)*q,(t,0,2*sp.pi))-3*sp.pi)==0
    assert sp.integrate(sp.cos(3*t)*q,(t,0,2*sp.pi))==0

def test_circular_interface_axisym_vs_nonaxisym_pressure():
    t,a,c=sp.symbols('t a c',real=True,positive=True)
    q=sp.cos(t)
    assert sp.integrate(c*q*a,(t,0,2*sp.pi))==0
    assert sp.simplify(sp.integrate(c*a*sp.cos(t)*q*a,(t,0,2*sp.pi))-c*sp.pi*a*a)==0
