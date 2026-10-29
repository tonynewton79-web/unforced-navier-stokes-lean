"""Exact H8 Appendix U anisotropic interface and pressure thresholds.
These regressions test necessary identities, not an NS existence theorem.
"""
import sympy as s
import mpmath as mp

def test_anisotropic_cofactor_normal_velocity_identity():
    tau,D=s.symbols('tau D',positive=True)
    y1,y2,y3,n1,n2,n3=s.symbols('y1 y2 y3 n1 n2 n3',real=True)
    a=s.diag(s.sqrt(tau),s.sqrt(tau),tau**D)
    v=-a.diff(tau)*s.Matrix([y1,y2,y3])
    oriented_area=s.simplify(a.det())*a.inv().T*s.Matrix([n1,n2,n3])
    value=s.simplify((v.T*oriented_area)[0])
    want=-tau**D*(s.Rational(1,2)*(y1*n1+y2*n2)+D*y3*n3)
    assert s.simplify(value-want)==0

def test_exact_surface_area_and_motion_exponents():
    h=s.symbols('h',positive=True)
    D=s.Rational(1,2)-h
    assert s.simplify(1+D-s.Rational(1,2)-(1-h))==0
    assert s.simplify(D-(s.Rational(1,2)-h))==0

def test_critical_interface_exponents():
    h=s.symbols('h',positive=True)
    D=s.Rational(1,2)-h
    p=s.Rational(1,2)-3*h
    assert s.simplify(2-h-p-(s.Rational(3,2)+2*h))==0
    assert s.simplify(1+D-p-(1+2*h))==0
    assert s.simplify((1+2*h)/2-(s.Rational(1,2)+h))==0

def test_strictly_subcritical_traces_fail_for_h_one_tenth():
    h=s.Rational(1,10); L=s.Rational(3,2)+2*h
    sigma=s.Rational(1,2);rho=s.Integer(1);kappa=s.Integer(1)
    assert 3*sigma<L and rho+sigma<L and sigma+kappa<L
    assert sigma<s.Rational(1,2)+h

def test_gauge_invariant_pressure_threshold():
    h=s.Rational(1,10); sigma=s.Rational(1,2)
    L=s.Rational(3,2)+2*h
    required=s.simplify(L-sigma)
    assert required==s.Rational(6,5)
    p=s.Rational(1,2)-3*h
    assert s.simplify(2-h-sigma-required-p)==0

def test_consistency_with_appendix_T_influx_coefficient():
    p,R=s.symbols('p R',positive=True)
    f=(1-2**(-p))*(R/p-s.Rational(1,2))
    assert s.simplify(f-(1-2**(-p))/p*(R-p/2))==0
    mp.mp.dps=40
    q=mp.mpf('0.2');Rmin=mp.mpf(3)*mp.besseljzero(1,1)**2/8
    value=(1-mp.power(2,-q))*(Rmin/q-mp.mpf('0.5'))
    assert mp.mpf('3.4988')<value<mp.mpf('3.4989')
