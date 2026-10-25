"""Exact A11 correction elimination; quadratic root input is still unverified."""
import sympy as s
u,v,w,x,z,q,t=s.symbols('u v w x z q t',real=True)
c1=q-x*t
expr=s.expand(2*v*(c1+z*t)+w*(c1**2+z*t**2))
a=w*(x*x+z);b=2*v*(z-x)-2*w*x*q;c=2*v*q+w*q*q
assert s.expand(expr-(a*t*t+b*t+c))==0
qp=s.symbols('qprime')
tp=-((-2*w*x)*t+2*v+2*w*q)*qp/(2*a*t+b)
assert s.cancel((2*a*t+b)*tp+((-2*w*x)*t+2*v+2*w*q)*qp)==0
assert s.expand(u*(c1+x*t)-u*q)==0
print("PASS exact A11 quadratic elimination and eta derivative; no numerical source root claimed")