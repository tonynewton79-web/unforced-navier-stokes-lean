"""A.11 terminal-source exact identity regression; finite symbolic only.
The actual source interval enclosures and physical unforced theorem
are NOT checked here.
"""
import sympy as s
from fractions import Fraction as F
eta,X,h,lam,Xp,eb=s.symbols('eta X h lam Xp eb',positive=True)
d=1-eta*eta;A=s.Rational(1,2)+h
sig=s.Function('sigma')(eta);pi=s.Function('pi')(eta)
E=s.Function('E')(eta);D=s.Function('D')(eta);P=s.Function('P')(eta)
g=s.Function('g')(eta)
St=X*E**2*D+sig;Pt=-E**2*P+pi
N=(4*h*eta*St-d*s.diff(St,eta))/X+4*A*eta*Pt-d*s.diff(Pt,eta)
N=s.expand(N/E).subs(s.diff(E,eta),g*E)
want=E*(4*eta*(h*D-A*P)-d*(2*g*(D-P)+s.diff(D,eta)-s.diff(P,eta)))
want+=(4*h*eta*sig-d*s.diff(sig,eta))/(X*E)+(4*A*eta*pi-d*s.diff(pi,eta))/E
assert s.simplify(N-want)==0
f=1/(1+eta*eta);Fr=s.Function('A19Residual')(eta)
sigma=Xp*eb**2*f**2*Fr/lam
got=(4*h*eta*sigma-d*s.diff(sigma,eta))/(X*E)
expected=Xp*eb**2*f**2/(lam*X*E)*(
 (4*h*eta+4*eta*d/(1+eta**2))*Fr-d*s.diff(Fr,eta))
assert s.simplify(got-expected)==0
assert s.simplify((1+eta**2)-2*eta*(1-eta**2)-(1-eta)**2-2*eta**3)==0
assert F(1,2)-F(253,1000)==F(247,1000)
print('PASS general D_eta/P_eta and A19 total residual/gauge algebra')
print('Not source-authenticated: A11 support intervals or unforced PDE')
