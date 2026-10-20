"""Independent exact symbolic source (4.16), (A.28)--(A.30) gates.
NO actual source interval data are provided. NOT a proof of pulse ratio.
"""
import sympy as s
from fractions import Fraction as Q
la,h,c,R,Rp,em,etam,dq,dn=s.symbols('la h c R Rp em etam dq dn')
D=s.Rational(1,2)-h;beta=s.Rational(1,2)-la
q0=(la-h+c)/(1-la)
Cd=la*(D+c)*(1-la)/(beta**2*(la-h+c));w0=2*R-Cd*Rp
m=R/beta-la*Rp/beta**2+em
n=-R+(D+c)*m-D*etam+dn
actual=n/(q0+dq)
claimed=(q0*la*R/beta+(D+c)*em-D*etam+dn-w0*dq)/(q0+dq)
assert s.cancel(actual-w0-claimed)==0
eta,X,E,S,Seta,Pi,Pieta,mm,meta,B=s.symbols('eta X E S Seta Pi Pieta mm meta B')
A=s.Rational(1,2)+h;d=1-eta**2;g=s.symbols('g')
M=X*E*mm;Me=X*E*(meta+g*mm)
W=1-(2*D*eta*M+d*Me)/X
ns=-W*(R+B)+D*(M-eta*Me)/(X*E)+(4*h*eta*S-d*Seta)/(X*E)+(4*A*eta*Pi-d*Pieta)/E
cn=-D*eta*g
en=(1-W)*R-W*B+(4*h*eta*S-d*Seta)/(X*E)+(4*A*eta*Pi-d*Pieta)/E
assert s.cancel(ns-(-R+(D+cn)*mm-D*eta*meta+en))==0
assert s.cancel(cn.subs(g,-2*eta/(1+eta**2))-2*D*eta**2/(1+eta**2))==0
lam=Q(1,10**14)
error=(12*lam/(Q(1,2)-lam)+3*Q(1,10**7)+1500*Q(1,10**10))/(1-Q(1,10**10))
assert error<Q(1,10**6)
assert Q(1280,3)*Q(20,9)*Q(1,400000)==Q(8,3375)>Q(1,10**7)
gain=Q(240)*720*Q(5,4)**6
assert gain==Q(10546875,16)
assert gain/(10**14)**4<Q(1,10**40)
mratio=(Q(2131000)*lam+Q(9,100)*lam**26+Q(1280,3)*Q(20,9)*Q(1,10**40))/Q(9999,10000)
assert mratio<Q(3,10**8)
print('PASS symbolic source residual and conditional rational gates')
print('Source-derived eQ,eN,eta*m_eta are UNVERIFIED')
