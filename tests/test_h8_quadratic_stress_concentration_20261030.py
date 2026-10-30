"""Appendix AC exact identity tests: no singular H8 existence claim."""
import sympy as s
import numpy as np
def test_terminal_exponents():
    h=s.symbols('h',positive=True);p=s.Rational(1,2)-3*h;v=s.Rational(3,2)-h
    assert s.simplify(v-1-p-2*h)==0
    assert s.simplify(p/2-1-v/2+s.Rational(3,2)+h)==0
def test_stress_gradient_scale():
    h=s.symbols('h',positive=True);p=s.Rational(1,2)-3*h
    assert s.simplify(p/2-1+s.Rational(3,4)+3*h/2)==0
    assert (p/2-1).subs(h,s.Rational(1,10))==-s.Rational(9,10)
def test_fourier_multiplier_frobenius():
    rng=np.random.default_rng(20261030)
    for _ in range(1000):
        k=rng.integers(-30,31,size=3)
        if not np.any(k):continue
        a=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
        b=np.einsum('i,j,ij->',k,k,a)/np.dot(k,k)
        assert abs(b)<=np.linalg.norm(a)+1e-10
def test_exact_pressure_work_divergence():
    x,y=s.symbols('x y',real=True);g=s.cos(2*y);pi=s.cos(x)*s.cos(2*y)
    boundary=s.integrate((pi.subs(x,s.pi)-pi.subs(x,0))*g,(y,0,2*s.pi))*(2*s.pi)
    interior=s.integrate(g*s.diff(pi,x),(x,0,s.pi),(y,0,2*s.pi))*(2*s.pi)
    assert s.simplify(boundary+4*s.pi**2)==0
    assert s.simplify(interior-boundary)==0
def test_tensor_polarization():
    a,b,c,d,e,f=s.symbols('a b c d e f',real=True)
    U=s.Matrix([a,b,c]);w=s.Matrix([d,e,f])
    S=U*w.T+w*U.T+w*w.T
    assert (S-((U+w)*(U+w).T-U*U.T)).applyfunc(s.simplify)==s.zeros(3)
def test_independent_3d_fft_stress_gradient():
    n=24;t=np.arange(n)*2*np.pi/n
    x,y,z=np.meshgrid(t,t,t,indexing='ij')
    U=np.array([np.sin(y),np.cos(z),np.cos(x)])
    w=np.array([np.cos(z),np.sin(x),np.sin(y)])
    S=np.einsum('i...,j...->ij...',U,w)+np.einsum('i...,j...->ij...',w,U)+np.einsum('i...,j...->ij...',w,w)
    kk=np.fft.fftfreq(n,d=1/n);K=np.meshgrid(kk,kk,kk,indexing='ij')
    d=sum(k*k for k in K);d=np.where(d==0,1,d)
    sh=np.fft.fftn(S,axes=(-3,-2,-1),norm='ortho')
    ph=np.zeros((n,n,n),dtype=complex)
    for i in range(3):
        for j in range(3):ph-=K[i]*K[j]*sh[i,j]/d
    ph[0,0,0]=0
    a=sum(np.linalg.norm(k*ph)**2 for k in K)
    b=sum(np.linalg.norm(k*sh[i,j])**2 for i in range(3) for j in range(3) for k in K)
    assert a>0 and a<=b+1e-9
def test_terminal_dyad_constant():
    tau,p,R,M=s.symbols('tau p R M',positive=True);delta=s.symbols('delta',positive=True)
    Q=(1-2**(-p))/p*(R-p/2)*M
    bound=s.simplify((Q*tau**p/2)/((tau/2)*delta*tau**(p/2)))
    assert s.simplify(bound-Q*tau**(p/2-1)/delta)==0
def test_regular_correction_retention_ratio():
    h=s.symbols('h',positive=True);p=s.Rational(1,2)-3*h
    assert s.simplify((s.Rational(1,2)-h-p)/2-h)==0
def test_natural_stress_no_go_ratio():
    t,p,K,C,d=s.symbols('t p K C d',positive=True)
    assert s.simplify((K*t**(p/2-1)/d)/(C*t**(p/2-1))-K/(C*d))==0
def test_projector_matrix_hilbert_schmidt():
    a,b,c=s.symbols('a b c',real=True);k=s.Matrix([a,b,c]);Q=k*k.T
    assert s.expand(sum(Q[i,j]**2 for i in range(3) for j in range(3))-(k.dot(k))**2)==0
