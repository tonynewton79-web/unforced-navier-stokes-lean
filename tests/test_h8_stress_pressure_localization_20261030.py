"""Source-seed pressure localization checks, not an H8 existence certificate."""
import sympy as s
import numpy as np

def test_distance_exponent():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h; D=s.Rational(1,2)-h
    b=(2*A+D)/4
    assert s.simplify(b-(s.Rational(3,8)+h/4))==0

def test_axial_coincidence_at_one_tenth():
    h=s.symbols("h")
    D=s.Rational(1,2)-h;b=s.Rational(3,8)+h/4
    assert s.solve(D-b,h)==[s.Rational(1,10)]
    assert b.subs(h,s.Rational(1,10))==s.Rational(2,5)

def test_physical_rescaling():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h
    assert s.simplify(2*A+D-s.Rational(3,2)-h)==0

def test_periodic_pressure_distance_power():
    h,a=s.symbols("h a",positive=True)
    b=s.Rational(3,8)+h/4
    assert s.simplify(s.Rational(3,2)+h-4*(b-a)-4*a)==0

def test_kernel_derivative_exact():
    d=s.symbols("d",positive=True)
    K=1/(2*s.pi*d**3)
    assert s.simplify(s.diff(K,d)+3/(2*s.pi*d**4))==0

def test_signed_axial_jump():
    y,a,b=s.symbols("y a b",real=True)
    assert s.simplify(s.integrate(-6*y,(y,a,b))+3*(b*b-a*a))==0

def test_quadratic_stress_polarization():
    U=s.Matrix(s.symbols("u v z"))
    w=s.Matrix(s.symbols("a b c"))
    S=U*w.T+w*U.T+w*w.T
    assert ((U+w)*(U+w).T-U*U.T-S).applyfunc(s.simplify)==s.zeros(3)

def test_pressure_linear_cutoff_fft():
    n=14;rng=np.random.default_rng(10)
    F=rng.standard_normal((3,3,n,n,n))
    q=np.fft.fftfreq(n,d=1/n);k=np.meshgrid(q,q,q,indexing="ij")
    den=sum(t*t for t in k);den[0,0,0]=1
    def pi(S):
        sh=np.fft.fftn(S,axes=(-3,-2,-1))
        ph=np.zeros((n,n,n),dtype=complex)
        for i in range(3):
            for j in range(3):ph-=k[i]*k[j]*sh[i,j]/den
        ph[0,0,0]=0
        return np.fft.ifftn(ph).real
    cutoff=(1+np.sin(np.arange(n)*2*np.pi/n))/2
    cutoff=cutoff[None,None,:,None,None]
    assert np.max(abs(pi(cutoff*F)+pi((1-cutoff)*F)-pi(F)))<1e-10

def test_global_stress_mass_bound():
    rng=np.random.default_rng(33)
    for _ in range(20):
        u=rng.standard_normal((3,8,9,7));U=rng.standard_normal((3,8,9,7))
        S=np.einsum("i...,j...->ij...",u,u)-np.einsum("i...,j...->ij...",U,U)
        assert np.sum(np.linalg.norm(S,axis=(0,1)))<=np.sum(u*u)+np.sum(U*U)+1e-8
