"""Exact conditional H8 moving-core energy-flux audits; not a blow-up proof."""
import sympy as sp
import mpmath as mp

def test_moving_boundary_energy_identity_nontrivial_heat_shear():
    t,y=sp.symbols('t y',real=True)
    low=sp.Rational(1,4)+t/10
    high=sp.Rational(3,4)-t/20
    u=sp.exp(-t)*sp.sin(y)
    e=u**2/2
    energy=sp.integrate(e,(y,low,high))
    diss=sp.integrate(sp.diff(u,y)**2,(y,low,high))
    J=-sp.diff(e,y)
    outward=J.subs(y,high)-J.subs(y,low)-e.subs(y,high)*sp.diff(high,t)+e.subs(y,low)*sp.diff(low,t)
    assert sp.trigsimp(sp.diff(energy,t)+diss+outward)==0

def test_energy_dyad_transport_coefficient_and_positivity():
    p,R,M,tau=sp.symbols('p R M tau',positive=True)
    r=sp.symbols('r',positive=True)
    E_drop=M*tau**p*(1-2**(-p))/2
    D=R*M*sp.integrate(r**(p-1),(r,tau/2,tau))
    Phi=sp.simplify(E_drop-D)
    expected=M*tau**p*(1-2**(-p))*(sp.Rational(1,2)-R/p)
    assert sp.simplify(Phi-expected)==0

def test_quantitative_global_relative_error_budget():
    p,R,k,d=sp.symbols('p R k d',positive=True)
    left=(1+d)**2-2**(-p)*(1-d)**2
    right=(2*R/p)*(1-2**(-p))*(1-k*d)**2
    assert sp.simplify((left-right).subs(d,0)-(1-2**(-p))*(1-2*R/p))==0

def test_h8_similarity_volume_and_energy_exponents():
    h=sp.symbols('h',positive=True)
    A=sp.Rational(1,2)+h
    D=sp.Rational(1,2)-h
    p=sp.Rational(1,2)-3*h
    assert sp.simplify(1+D-2*A-p)==0
    assert sp.simplify(1+D-(2*A+1)-(p-1))==0
    assert sp.simplify(-A+(1+D)/2-p/2)==0

def test_axisymmetric_rigorous_spectral_influx_lower_bound():
    mp.mp.dps=30
    j01=mp.besseljzero(0,1)
    j11=mp.besseljzero(1,1)
    j21=mp.besseljzero(2,1)
    R2=mp.mpf(8)/3
    p=mp.mpf(1)/5
    Rmin=j11**2/R2
    inflow=(1-mp.power(2,-p))/p*(Rmin-p/2)
    assert j01**2/R2<Rmin<j21**2/R2
    assert mp.mpf('5.5057')<Rmin<mp.mpf('5.5058')
    assert mp.mpf('3.4988')<inflow<mp.mpf('3.4989')

def test_zero_collar_reduces_to_complementary_flux():
    wu,pu,V,ge=sp.symbols('wu pu V ge',real=True)
    e=wu**2/2
    flux=(e+pu)*wu-ge-e*V
    expected=wu**3/2+pu*wu-ge-wu**2*V/2
    assert sp.expand(flux-expected)==0

def test_bounded_exterior_collar_flux_is_subcritical():
    h=sp.symbols('h',positive=True)
    A=sp.Rational(1,2)+h
    D=sp.Rational(1,2)-h
    p=sp.Rational(1,2)-3*h
    boundary_area=sp.Rational(1,2)+D
    worst_speed_exponent=-A
    dyadic_total=1+boundary_area+worst_speed_exponent
    assert sp.simplify(dyadic_total-p)==1+h
    assert sp.simplify(dyadic_total-(sp.Rational(3,2)-2*h))==0
