"""Appendix W conditional pressure coefficient checks (not source authentication)."""
import sympy as sp
import numpy as np
import mpmath as mp

def test_critical_pressure_exponents():
    h=sp.symbols("h",real=True)
    D=sp.Rational(1,2)-h; A=sp.Rational(1,2)+h; p=sp.Rational(1,2)-3*h
    assert sp.simplify(sp.Rational(1,2)+D-sp.Rational(1,2)-2*A-(p-1))==0
    assert sp.simplify(1-sp.Rational(1,2)-2*A-(p-1+h))==0

def test_exact_anisotropic_cofactor_lateral():
    t,D=sp.symbols("t D",positive=True)
    v1,v2,v3,n1,n2,n3=sp.symbols("v1 v2 v3 n1 n2 n3",real=True)
    S=sp.diag(sp.sqrt(t),sp.sqrt(t),t**D)
    v=sp.Matrix([v1,v2,v3]);n=sp.Matrix([n1,n2,n3])
    oriented=sp.simplify(S.det())*S.inv().T*n
    assert sp.simplify(v.dot(oriented)-t**(sp.Rational(1,2)+D)*(v1*n1+v2*n2)-t*(v3*n3))==0

def moment(a,b,c):
    return sp.simplify(2*sp.gamma(sp.Rational(1,2)+a)*sp.gamma(sp.Rational(1,2)+b)*sp.gamma(sp.Rational(1,2)+c)/sp.gamma(sp.Rational(3,2)+a+b+c))

def test_sphere_signed_mode_overlap_and_gauge():
    a=moment(2,0,0);b=moment(1,1,0)
    assert a==4*sp.pi/5 and b==4*sp.pi/15
    norm=sp.simplify(2*a-2*b)
    assert norm==16*sp.pi/15
    assert sp.simplify(moment(1,0,0)-moment(0,1,0))==0
    for c in (-3,0,5):assert sp.sign(c*norm)==sp.sign(c)

def test_shell_count_and_explicit_tail():
    n=sp.symbols("n",positive=True,integer=True)
    assert sp.expand((2*n+1)**3-(2*n-1)**3)==24*n*n+2
    for k in (1,2,3,5,10,20):
        partial=sum((24*j*j+2)/(1+j*j)**3 for j in range(k+1,1500))
        assert partial<26/(3*k**3)

def test_analytic_terminal_dyad_coefficient():
    r,p,c,z=sp.symbols("r p c z",positive=True)
    got=sp.integrate(c*z**(p-1),(z,r/2,r))
    assert sp.simplify(got/(c*r**p)-(1-2**(-p))/p)==0

def test_fourier_multiplier_frobenius_one():
    rng=np.random.default_rng(567)
    for i in range(200):
        k=rng.integers(-7,8,size=3)
        if (k==0).all():continue
        a=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
        pi=-(np.outer(k,k)*a).sum()/np.dot(k,k)
        assert abs(pi)<=np.linalg.norm(a)+1e-12

def test_tail_constant_and_finite_mode_replay():
    mp.mp.dps=30
    for K in (1,2,4,8):
        c=mp.sqrt(mp.mpf(26)/3)*mp.power(K,-mp.mpf("1.5"))
        assert c>0
    modes=[(0,0,0),(1,2,0),(-1,-2,0),(4,0,0),(0,-4,0)]
    assert all(max(abs(j) for j in k)<=4 for k in modes)
