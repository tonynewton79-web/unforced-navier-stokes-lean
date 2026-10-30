"""Exact rational C4 Poisson sign certificate; NOT an unforced H8 PDE witness."""
from collections import defaultdict
from fractions import Fraction as F
from math import factorial
import mpmath as mp
import numpy as np

def ss(k,l):
    o=defaultdict(F)
    for a in (-1,1):
        for b in (-1,1):o[(a*k,b*l)]+=F(-a*b,4)
    return o

def psi(a):
    o=defaultdict(F)
    for k in ((1,0),(-1,0),(0,1),(0,-1)):o[k]+=F(1,2)
    for k,v in ss(2,1).items():o[k]+=a*v/2
    for k,v in ss(1,2).items():o[k]-=a*v/2
    return {k:v for k,v in o.items() if v}

def pi_fourier(P):
    o=defaultdict(F)
    for a,x in P.items():
        for b,y in P.items():
            k=(a[0]+b[0],a[1]+b[1]);n=k[0]**2+k[1]**2
            if n:
                o[k]+=x*y*F((k[0]*a[1]-k[1]*a[0])*(k[0]*b[1]-k[1]*b[0]),n)
    return {k:v for k,v in o.items() if v}

def work_coefficients(P):
    o=defaultdict(F)
    for k,pk in pi_fourier(P).items():
        for l,sl in P.items():
            n=(k[0]+l[0])**2+(k[1]+l[1])**2
            if n:o[n]-=pk*sl*(l[1]*k[0]-l[0]*k[1])
    return {k:v for k,v in o.items() if v}

C={1:F(-2427,32000),5:F(21,100),9:F(-10791,64000),13:F(3,640),
   17:F(1047,32000),29:F(-81,16000),37:F(27,8000),41:F(-81,64000)}

def rigorous_interval(coeff,N=20):
    S=F(0);E=F(0)
    for n,c in coeff.items():
        S+=c*sum((F((-n)**j,4**j*factorial(j)*factorial(j+1)) for j in range(N+1)),F(0))/2
        E+=abs(c)*F(n**(N+1),2*4**(N+1)*factorial(N+1)*factorial(N+2))
    assert E<F(3,10**23)
    pi_lo=F(314159,100000);pi_hi=F(314160,100000)
    assert S+E<0
    return 2*pi_hi*(S-E),2*pi_lo*(S+E)

def test_stream_and_poisson_are_C4_invariant():
    for a in (F(0),F(3,10),F(-3,10)):
        P=psi(a);Z=pi_fourier(P)
        assert all(P.get((-k[1],k[0]),F(0))==v for k,v in P.items())
        assert all(Z.get((-k[1],k[0]),F(0))==v for k,v in Z.items())

def test_velocity_divergence_zero_modewise():
    for k,v in psi(F(3,10)).items():
        assert k[0]*k[1]*v-k[1]*k[0]*v==0

def test_exact_pressure_quadratic_coefficients():
    P=psi(F(3,10));Z=pi_fourier(P)
    assert (0,0) not in Z
    for k,v in Z.items():
        d=k[0]**2+k[1]**2
        rhs=sum(x*y*(k[0]*a[1]-k[1]*a[0])*(k[0]*b[1]-k[1]*b[0])
                for a,x in P.items() for b,y in P.items()
                if (a[0]+b[0],a[1]+b[1])==k)
        assert d*v==rhs

def test_eight_rational_bessel_coefficients_exact():
    assert work_coefficients(psi(F(3,10)))==C
    assert work_coefficients(psi(F(-3,10)))=={k:-v for k,v in C.items()}
    assert work_coefficients(psi(F(0)))=={}

def test_rational_Bessel_remainder_certifies_negative_sign():
    lo,hi=rigorous_interval(C)
    assert F(-79871,10000000)<lo<hi<F(-79870,10000000)

def test_high_precision_and_axial_normalization():
    mp.mp.dps=55
    W=2*mp.pi*mp.fsum([mp.mpf(v.numerator)/v.denominator*
                       mp.besselj(1,mp.sqrt(n))/mp.sqrt(n) for n,v in C.items()])
    assert abs(W-mp.mpf('-0.007987051101278976116349622261982257'))<mp.mpf('1e-33')
    assert abs((2*mp.pi*W)/W-2*mp.pi)<mp.mpf('1e-50')

def test_C4_angular_modes_and_tail_bound():
    # Scalar pressure modes are multiples of 4; slice mean radial normal flux is zero.
    p={0:8,4:5+2j,-4:5-2j,8:3+2j,-8:3-2j}
    q={0:0,4:2-3j,-4:2+3j,8:-1j,-8:1j}
    full=2*np.pi*sum(v*q.get(-m,0) for m,v in p.items())
    main=4*np.pi*(p[4]*np.conj(q[4])).real
    PP=np.sqrt(2*np.pi*sum(m**4*abs(v)**2 for m,v in p.items()))
    QQ=np.sqrt(2*np.pi*sum(abs(v)**2 for v in q.values()))
    assert abs(full-main)<(1/64)*PP*QQ

def test_signed_work_survives_independent_fft():
    n=48;t=np.arange(n)*2*np.pi/n;X,Y=np.meshgrid(t,t,indexing='ij')
    k=np.fft.fftfreq(n,d=1/n);K,L=np.meshgrid(k,k,indexing='ij')
    den=np.where(K*K+L*L==0,1,K*K+L*L)
    def vel(a,x,y):
        u=-np.sin(y)+a*(.5*np.sin(2*x)*np.cos(y)-np.sin(x)*np.cos(2*y))
        v=np.sin(x)-a*(np.cos(2*x)*np.sin(y)-.5*np.cos(x)*np.sin(2*y))
        return u,v
    for a in (-.3,.3):
        u,v=vel(a,X,Y)
        P=-(K*K*np.fft.fft2(u*u)+2*K*L*np.fft.fft2(u*v)+L*L*np.fft.fft2(v*v))/den/(n*n)
        P[0,0]=0
        theta=np.arange(2048)*2*np.pi/2048;xx=np.cos(theta);yy=np.sin(theta)
        bu,bv=vel(a,xx,yy);rad=bu*xx+bv*yy
        pressure=np.zeros(len(theta),dtype=complex)
        for k1 in range(-6,7):
            for k2 in range(-6,7):
                if k1 or k2:
                    pressure+=P[k1%n,k2%n]*np.exp(1j*(k1*xx+k2*yy))
        work=2*np.pi*np.mean(pressure.real*rad)
        assert (work<0)==(a>0)
        assert abs(abs(work)-.007987051101278976)<1e-11
