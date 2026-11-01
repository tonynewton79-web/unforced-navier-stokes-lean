"""Exact algebraic H8 carrier-transfer gate; not a nonlinear PDE witness."""
import sympy as s
import numpy as np

def test_h8_transfer_energy_exponent():
    h=s.symbols("h",positive=True);p=s.Rational(1,2)-3*h
    A=s.Rational(1,2)+h
    assert s.simplify(p+2*A-1-(s.Rational(1,2)-h))==0

def test_convective_power():
    h=s.symbols("h",positive=True);p=s.Rational(1,2)-3*h
    A=s.Rational(1,2)+h
    assert s.simplify(-A+(p-1)/2-(p/2-1-h))==0

def test_quadratic_power():
    h=s.symbols("h",positive=True);p=s.Rational(1,2)-3*h
    assert s.simplify(p+(-1-h)+1-(p-h))==0

def test_general_threshold():
    h,k=s.symbols("h k",positive=True)
    for K in (s.Rational(0),h/2,h):
        m=s.Max(K,h/2)
        assert s.simplify(m-K).is_nonnegative is True
        assert s.simplify(2*m-h).is_nonnegative is True

def test_affine_no_swirl_power():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h
    p=s.Rational(1,2)-3*h
    assert s.simplify(-2*A-D+(1+D)/2-(p/2-1))==0

def test_affine_amplitude_exponent():
    h=s.symbols("h",positive=True)
    p=s.Rational(1,2)-3*h;D=s.Rational(1,2)-h
    assert s.simplify(p/2+h/2-(1+D)/2+s.Rational(1,2)+h/2)==0

def test_h_one_tenth_values():
    h=s.Rational(1,10);p=s.Rational(1,2)-3*h
    assert p==s.Rational(1,5)
    assert p/2+h/2==s.Rational(3,20)
    assert s.Rational(1,2)+h/2==s.Rational(11,20)

def test_exact_dyad_energy_coefficient():
    q,tau,M0,R0=s.symbols("q tau M0 R0",positive=True)
    s0=s.symbols("s0",positive=True)
    D=s.integrate(R0*M0*s0**(q-1),(s0,tau/2,tau))
    E=M0*((tau/2)**q-tau**q)/2
    K=M0*(1-2**(-q))*(R0/q-s.Rational(1,2))*tau**q
    assert s.simplify(D+E-K)==0

def test_unforced_exact_shear_transfer():
    k,K,Kp=s.symbols("k K Kp",real=True)
    wU=(k-K)*K/2
    derivative=(-k-Kp)*K/2+(k-K)*Kp/2
    Mprime=K*Kp;D=K*K/2
    J=(k-K)*(Kp-K)/2
    assert s.simplify(J-(Mprime/2+D+derivative))==0

def test_stress_polarization():
    U=s.Matrix(s.symbols("a b c"))
    w=s.Matrix(s.symbols("d e f"))
    S=U*w.T+w*U.T+w*w.T
    assert ((U+w)*(U+w).T-U*U.T-S).applyfunc(s.simplify)==s.zeros(3)

def test_dealiased_periodic_cancellation():
    n=24
    q=np.fft.fftfreq(n,d=1/n)
    kx,ky,kz=np.meshgrid(q,q,q,indexing="ij")
    kk=np.stack((kx,ky,kz));k2=np.sum(kk*kk,axis=0);k2[0,0,0]=1
    rng=np.random.default_rng(20261031)
    def df():
        v=rng.standard_normal((3,n,n,n))
        vhat=np.fft.fftn(v,axes=(-3,-2,-1))
        vhat-=kk*np.sum(kk*vhat,axis=0)/k2
        vhat[:,(kx*kx+ky*ky+kz*kz)>9]=0
        vhat[:,0,0,0]=0
        return np.fft.ifftn(vhat,axes=(-3,-2,-1)).real
    U=df();w=df();uh=np.fft.fftn(U,axes=(-3,-2,-1))
    grad=np.empty((3,3,n,n,n))
    for i in range(3):
        for j in range(3):
            grad[i,j]=np.fft.ifftn(1j*2*np.pi*kk[j]*uh[i]).real
    S=np.einsum("i...,j...->ij...",U,w)+np.einsum("i...,j...->ij...",w,U)+np.einsum("i...,j...->ij...",w,w)
    lhs=np.sum(S*grad,axis=(0,1)).mean()
    rhs=(np.einsum("i...,j...,ij...->...",w,U,grad)+np.einsum("i...,j...,ij...->...",w,w,grad)).mean()
    assert abs(lhs-rhs)<1e-10
