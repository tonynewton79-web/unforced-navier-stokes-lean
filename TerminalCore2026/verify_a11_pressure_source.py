#!/usr/bin/env python3
"""Actual A.11 sigma-prime bump replay; not an unforced PDE certificate."""
import mpmath as m
m.mp.dps=60
half=m.mpf(3)/20
def prime(s):
    if not 0<s<1:return m.mpf(0)
    g=-1/s**2+1/(1-s)**2
    f=1/(1+m.exp(-g))
    return f*(1-f)*(2/s**3+2/(1-s)**3)
def beta(t):return m.mpf(10)/3*prime(m.mpf(10)*t/3+m.mpf('0.5'))
def quad(f):return m.quad(f,[-half,-half/2,0,half/2,half])
assert abs(quad(beta)-1)<m.mpf('1e-40')
n=0
for lam in [m.mpf('.01'),m.mpf('.05')]:
    b=1+2*lam; z=m.exp(-2*b); x=m.exp(2*(1-lam))
    v=quad(lambda t:m.exp(-b*t)*beta(t))
    w=quad(lambda t:m.exp(-b*t)*beta(t)**2)
    u=quad(lambda t:m.exp((1-lam)*t)*beta(t))
    for eta in [-1,m.mpf('-.35'),0,m.mpf('.7'),1]:
        delta=m.mpf('1e-7')*(1+m.mpf(eta)**2/5)
        a=delta/u
        A=w*(x*x+z); B=2*v*(z-x)-2*w*a*x; C=2*v*a+w*a*a
        assert B*B-4*A*C>0
        q2=2*C/(m.sqrt(B*B-4*A*C)-B);q1=a-x*q2
        r2=2*v*(q1+z*q2)+w*(q1*q1+z*q2*q2)
        direct=quad(lambda t:m.exp(-b*t)*(2*q1*beta(t)+q1*q1*beta(t)**2))
        direct+=z*quad(lambda t:m.exp(-b*t)*(2*q2*beta(t)+q2*q2*beta(t)**2))
        assert abs(r2)<m.mpf('1e-50')
        assert abs(direct-r2)<m.mpf('1e-48')
        n+=1
assert 2*m.mpf(1)*(m.mpf(1)/10)+20*(m.mpf(1)/10)**2==m.mpf('0.4')
print('PASS source A11 smooth-step numerical moment cancellation:',n)
print('HOLD: complete unforced Navier-Stokes source and PDE proof')
