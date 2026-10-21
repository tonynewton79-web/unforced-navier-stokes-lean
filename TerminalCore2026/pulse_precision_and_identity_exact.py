"""Exact source-normalized A.29--A.30 cancellation and precision budget.

The result is algebraic; it does not certify actual Appendix-A source
fields or the unforced Navier--Stokes theorem.
"""
from fractions import Fraction as Rat
import sympy as s
la,h,eta,R,Rp,em,meta,dq,en=s.symbols('la h eta R Rp em meta dq en',real=True)
D=s.Rational(1,2)-h
beta=s.Rational(1,2)-la
g=-2*eta/(1+eta**2)
c=-D*eta*g
q0=(la-h+c)/(1-la)
Cd=la*(D+c)*(1-la)/(beta**2*(la-h+c))
w0=2*R-Cd*Rp
m=R/beta-la*Rp/beta**2+em
NE=-R+(D+c)*m-D*eta*meta+en
actualQ=q0+dq
ratio=NE/actualQ-w0
normal=(q0*(la/beta)*R+(D+c)*em-D*eta*meta+en-w0*dq)/(q0+dq)
assert s.cancel(ratio-normal)==0
assert s.factor(c-2*D*eta**2/(1+eta**2))==0
assert s.cancel(q0.subs(eta,0)-(la-h)/(1-la))==0
print('PASS exact source A29/A30 normalized polynomial cancellation')
lam=Rat(1,10**14);hh=lam/Rat(10000)
q=(lam-hh)/(1-lam)
epsilonQ=q/Rat(10**10)
epsilonN=q/Rat(10**7)
assert Rat(9999,10000)*lam<=q<=lam/(1-lam)
assert Rat(9999,10000)*Rat(1,10**24)<epsilonQ<Rat(10001,10000)*Rat(1,10**24)
assert epsilonN<Rat(10001,10000)*Rat(1,10**21)
assert Rat(1,10**16)>epsilonQ and Rat(1,10**16)>epsilonN
print('PASS exact centerline target scales:',epsilonQ,epsilonN)
print('NEGATIVE CONTROL: 1e-16 absolute cancellation envelope is insufficient')
print('STATUS: no authenticated actual source full-pulse interval boxes')
