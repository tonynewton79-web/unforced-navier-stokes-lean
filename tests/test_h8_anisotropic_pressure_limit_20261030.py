"""Conditional H8 carrier-only periodic pressure limit; no NS blowup claim."""
import sympy as s
import numpy as np
from numpy.fft import fftn, fftfreq

def test_h8_exact_component_exponents():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h; D=s.Rational(1,2)-h
    assert s.simplify(A+D-1)==0
    assert s.simplify(A-s.Rational(1,2)-h)==0
    assert s.simplify(1+D-2*A-(s.Rational(1,2)-3*h))==0

def test_m4_leading_swirl_cannot_cancel_bounded_radial_axial():
    theta,r,e=s.symbols("theta r e",positive=True)
    v4=s.symbols("v4",real=True)
    az=v4*s.cos(4*theta)
    assert s.simplify(s.diff(az,theta)/r+4*v4*s.sin(4*theta)/r)==0

def test_fourth_swirl_is_permitted_at_subleading_order():
    theta,r,e=s.symbols("theta r e",positive=True)
    F=s.Function("F")(r)
    psi=e*F*s.cos(4*theta)
    vr=s.diff(psi,theta)/r
    vt=-s.diff(psi,r)
    assert s.simplify(s.diff(r*vr,r)/r+s.diff(vt,theta)/r)==0

def test_actual_3d_source_seed_not_planar_solenoidal():
    r,z=s.symbols("r z",positive=True)
    chi=s.Function("chi")(r,z)
    ur=-r*(chi+z*s.diff(chi,z))
    uz=z*(2*chi+r*s.diff(chi,r))
    assert s.simplify(s.diff(r*ur,r)/r+s.diff(uz,z))==0
    assert s.simplify((s.diff(r*ur,r)/r).subs(chi,1))==-2

def test_scaled_fourier_pressure_limit_for_nonzero_kperp():
    eps,a,b,c,d,f,g=s.symbols("eps a b c d f g",real=True)
    formula=-(a+4*b+4*c+eps*(6*d+12*f)+9*eps**2*g)/(5+9*eps**2)
    assert s.simplify(formula.subs(eps,0)+(a+4*b+4*c)/5)==0
    assert s.simplify(s.diff(formula,eps).subs(eps,0)+(6*d+12*f)/5)==0

def test_low_horizontal_frequency_needs_strong_not_uniform_limit():
    eps,z=s.symbols("eps z",positive=True)
    assert s.simplify(eps**2*z**2/(eps**2*z**2))==1

def test_periodic_image_error_exponent():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h
    p=s.Rational(1,2)-3*h
    assert s.simplify(p+2*A-(s.Rational(3,2)-h))==0

def test_outside_swirl_carrier_pressure_zero():
    r=s.symbols("r",positive=True)
    V=r*(1-r**2)**6
    P=-(1-r**2)**13/s.Integer(26)
    assert s.simplify(s.diff(P,r)-V**2/r)==0
    assert s.simplify(s.diff(P,r,2)+s.diff(P,r)/r-s.diff(V*V,r)/r)==0
    assert P.subs(r,1)==0

def test_remote_m4_taylor_critical_threshold():
    h=s.symbols("h",positive=True)
    assert s.simplify((3+2*h)/7-(s.Rational(3,7)+2*h/7))==0
    assert s.simplify(((3+2*h)/7).subs(h,s.Rational(1,10))-s.Rational(16,35))==0

def test_c4_cubic_taylor_has_no_nonzero_fourfold_mode():
    x,y,t=s.symbols("x y t",real=True)
    P=x*x+y*y+2*(x*x+y*y)*0+3
    assert s.simplify(P.subs({x:-y,y:x},simultaneous=True)-P)==0
    assert s.simplify(s.diff(P.subs({x:s.cos(t),y:s.sin(t)}),t))==0

def test_independent_3d_pressure_fourier_limit():
    n=20
    x=np.arange(n)*2*np.pi/n
    X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
    Ux=-np.sin(Y)*(1+.2*np.cos(Z))
    Uy=np.sin(X)*(1+.2*np.cos(Z))
    k=fftfreq(n,d=1/n)
    kx,ky,kz=np.meshgrid(k,k,k,indexing="ij")
    horiz=kx*kx+ky*ky
    numerator=kx*kx*fftn(Ux*Ux)+2*kx*ky*fftn(Ux*Uy)+ky*ky*fftn(Uy*Uy)
    P0=np.zeros_like(numerator,dtype=complex)
    mask=horiz>0
    P0[mask]=-numerator[mask]/horiz[mask]
    errors=[]
    for e in (.2,.1,.05,.025):
        den=horiz+e*e*kz*kz
        P=np.zeros_like(P0,dtype=complex)
        ok=den>0
        P[ok]=-numerator[ok]/den[ok]
        errors.append(np.linalg.norm(P-P0))
    assert all(errors[i+1]<errors[i] for i in range(3))
