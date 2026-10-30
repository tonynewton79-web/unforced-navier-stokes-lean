"""Appendix AF tests: local source seed, not authenticated full H8."""
import sympy as s
import numpy as np

def test_affine_curl_and_divergence():
    x,y,z,t=s.symbols("x y z t",positive=True)
    A=s.Matrix([-y*z/t,x*z/t,0])
    U=s.Matrix([s.diff(A[2],y)-s.diff(A[1],z),
                s.diff(A[0],z)-s.diff(A[2],x),
                s.diff(A[1],x)-s.diff(A[0],y)])
    assert U==s.Matrix([-x/t,-y/t,2*z/t])
    assert sum(s.diff(U[i],q) for i,q in enumerate((x,y,z)))==0

def test_local_affine_unforced_navier_stokes():
    x,y,z,t=s.symbols("x y z t",positive=True)
    M=s.diag(-1,-1,2);q=s.Matrix([x,y,z]);U=M*q/t
    p=-3*z*z/t**2
    # tau=T-time, so time derivative is -partial_tau
    a=-U.diff(t)+s.Matrix([sum(U[j]*s.diff(U[i],v)
          for j,v in enumerate((x,y,z))) for i in range(3)])
    g=s.Matrix([s.diff(p,v) for v in (x,y,z)])
    assert (a+g).applyfunc(s.simplify)==s.zeros(3,1)
    assert s.simplify(-sum(s.diff(p,v,2) for v in (x,y,z))-6/t**2)==0

def test_exact_curl_of_three_variable_cutoff():
    x,y,z,t=s.symbols("x y z t",positive=True)
    c=s.Function("c")(x,y,z)
    V=s.Matrix([-x*(c+z*s.diff(c,z))/t,
                -y*(c+z*s.diff(c,z))/t,
                 z*(2*c+x*s.diff(c,x)+y*s.diff(c,y))/t])
    assert s.simplify(sum(s.diff(V[i],v)
                 for i,v in enumerate((x,y,z))))==0

def test_exact_cylindrical_cutoff_divergence():
    R,Z,t=s.symbols("R Z t",positive=True)
    c=s.Function("c")(R,Z)
    ur=-R*(c+Z*s.diff(c,Z))/t
    uz=Z*(2*c+R*s.diff(c,R))/t
    assert s.simplify(s.diff(R*ur,R)/R+s.diff(uz,Z))==0

def test_h8_similarity_exponents():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h;p=s.Rational(1,2)-3*h
    assert s.simplify(1+D-2*A-p)==0
    assert s.simplify(2*A+D-(s.Rational(3,2)+h))==0
    assert s.simplify(p+2*A+D-(2-2*h))==0

def test_normalized_affine_pressure():
    h,t,eta=s.symbols("h t eta",positive=True)
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h
    P=s.simplify(t**(2*A)*(-3*(t**D*eta)**2/t**2))
    assert P==-3*eta**2
    assert s.diff(P,eta)==-6*eta

def test_scaled_poisson_source():
    h,t,eps=s.symbols("h t eps",positive=True)
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h
    assert s.simplify(t**(2*A+1)*(6/t**2)-6*t**(2*h))==0
    assert s.simplify(t**(1-2*D)-t**(2*h))==0

def test_fourier_vertical_factor_nonzero_horizontal():
    e=s.symbols("e",positive=True)
    for k,l,xi in [(1,0,1),(1,2,4),(2,-3,5)]:
        f=e**2*xi**2/(k*k+l*l+e**2*xi**2)
        assert s.limit(f,e,0,dir="+")==0
    # horizontal-zero line is exceptional in full-space Fourier
    assert s.simplify(e**2*4/(e**2*4))==1

def test_full_four_patch_cross_term_share():
    v=s.symbols("v")
    diag=sum(v*v for _ in range(4))/16
    off=sum(v*v for i in range(4) for j in range(4) if i!=j)/16
    assert s.simplify(diag-v*v/4)==0
    assert s.simplify(off-3*v*v/4)==0

def test_signed_axial_pressure_jump():
    eta,a,b=s.symbols("eta a b",real=True)
    P=-3*eta**2
    assert s.diff(P,eta)==-6*eta
    assert s.simplify(P.subs(eta,b)-P.subs(eta,a)+3*(b*b-a*a))==0

def test_numerical_anisotropic_multiplier_decay():
    n=30;k=np.fft.fftfreq(n,d=1/n)
    kx,ky,kz=np.meshgrid(k,k,k,indexing="ij")
    horiz=kx*kx+ky*ky
    keep=horiz>0
    out=[]
    for e in (.5,.25,.125,.0625):
        factor=e**2*kz**2/(horiz+e**2*kz**2+1e-100)
        out.append(np.linalg.norm(factor[keep]))
    assert all(out[j+1]<out[j] for j in range(3))
