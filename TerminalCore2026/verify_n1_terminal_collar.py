#!/usr/bin/env python3
"""Exact first-order outer collar test; not a proof of the unforced NSE."""
import sympy as s
import mpmath as m
m.mp.dps=55
eta,h,D=s.symbols("eta h D",real=True)
L=1-2*h*eta**2
az=-2*eta/L
bz=s.simplify((-2*D*eta*az+(1-eta**2)*s.diff(az,eta))/L)
assert az.subs(eta,0)==0 and bz.subs(eta,0)==-2
t=s.symbols("t",positive=True)
g=-t**-2+(1-t)**-2
assert s.diff(g,t).subs(t,s.Rational(1,2))==32
assert s.Rational(1,4)*32==8
def sigmoid(x):
    if x<=0:return m.mpf(0)
    if x>=1:return m.mpf(1)
    return 1/(1+m.exp(-(-1/x**2+1/(1-x)**2)))
def fo(y,rho):return 1-rho*(1-sigmoid((y-1)/2))
def val(z,tau,DD,rho):
    q=m.findroot(lambda Q:Q-tau-z*z*Q**(1-2*DD),(tau,tau*(1+m.mpf(".001"))))
    return fo(2+m.log(tau/q),rho)
max_error=m.mpf(0)
for hs in ["0.005","0.008"]:
    hh=m.mpf(hs);dd=m.mpf("0.5")-hh;rho=hh/256
    for ts in ["0.2","0.6","0.9"]:
        tau=m.mpf(ts);truth=-8*rho*tau**(-2*dd)
        for zs in [".002",".001",".0005"]:
            z=m.mpf(zs)
            observed=(val(z,tau,dd,rho)-2*val(0,tau,dd,rho)+val(-z,tau,dd,rho))/z**2
            err=abs((observed-truth)/truth)
            max_error=max(max_error,err)
            assert err<m.mpf("0.0007"),(hs,ts,zs,err)
assert abs(val(m.mpf(".002"),m.mpf(".6"),m.mpf(".495"),0)-1)<m.mpf("1e-45")
print("PASS midpoint az=0 bz=-2 sigma_prime=8 and 18 physical-coordinate comparisons")
print("MAX RELATIVE ERROR",m.nstr(max_error,12))
print("NOT PROVED: unforced physical NSE and full Lean theorem")
