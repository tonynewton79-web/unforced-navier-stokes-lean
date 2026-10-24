"""Source A11 algebra and rational gate. NOT authentic source intervals."""
from fractions import Fraction as F
import sympy as s
eta=s.symbols('eta',real=True)
X,h,A,D,P,g,dD,dP=s.symbols('X h A D P g dD dP')
S0=s.Function('Sinf')(eta);P0=s.Function('Pinf')(eta)
E=s.Function('E')(eta)
S=X*E**2*D+S0;Pi=-E**2*P+P0
Ns=(4*h*eta*S-(1-eta**2)*s.diff(S,eta))/X+4*A*eta*Pi-(1-eta**2)*s.diff(Pi,eta)
Ns=s.expand(Ns.subs(s.diff(E,eta),g*E)/E)
tail=E*(4*eta*(h*D-A*P)-(1-eta**2)*2*g*(D-P))
defect=(4*h*eta*S0-(1-eta**2)*s.diff(S0,eta))/(X*E)+(4*A*eta*P0-(1-eta**2)*s.diff(P0,eta))/E
assert s.simplify(Ns-tail-defect)==0
la=F(1,20);H=la/100;Dd=F(233,100);Pd=F(1,2);eps=F(1,1000)
B=4*H*Dd+4*(F(1,2)+H)*Pd+2*eps*Dd
assert B==F(25258,25000)
assert B/F(4)<F(253,1000)
assert F(1,2)-F(253,1000)==F(247,1000)
print("PASS exact A11 source decomposition and 0.247-lambda reserve")
print("NOT A SOURCE-AUTHENTICATED STRESS CERTIFICATE")
