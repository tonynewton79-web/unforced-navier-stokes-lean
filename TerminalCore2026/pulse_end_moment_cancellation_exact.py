"""Exact source pulse-end algebra and negative-control test.
No numerical Appendix-A source realization or unforced PDE is certified.
"""
import sympy as s
eta=s.symbols('eta',real=True)
ka,kb,p,q=s.symbols('ka kb p q',positive=True)
r=s.Matrix([s.Function('rm')(eta),s.Function('rj')(eta)])
B=s.Matrix([[ka,p*ka],[kb,q*kb]])
assert s.factor(B.det()-ka*kb*(q-p))==0
c=-B.inv()*r
assert all(s.simplify(v)==0 for v in B*c+r)
assert all(s.simplify(v)==0 for v in B*s.diff(c,eta)+s.diff(r,eta))
# Negative control: freezing the correction coefficients breaks the jets.
rf=s.Matrix([eta+1,3*eta+2])
bf=B.subs({ka:2,kb:7,p:5,q:3})
cf=-bf.inv()*rf
assert all(s.simplify(x)==0 for x in bf*s.diff(cf,eta)+s.diff(rf,eta))
assert any(s.simplify(x)!=0 for x in s.diff(rf,eta))
# Reduced stress formulas after m=j=m_eta=j_eta=U=0.
D,h,A,E,g,z=s.symbols('D h A E g z',real=True)
m,j,me,je,i,ie,S,Se,P,Pe,a=s.symbols('m j me je i ie S Se P Pe a')
d=1-z*z
W=1-E*(2*D*z*m+d*(me+g*m))
Q=-W+(1-h)*i-D*z*(ie+g*i)-d*E*(je+2*g*j)+2*(h-D)*z*E*j
N=-W*a+D*(m-z*(me+g*m))+E*(4*h*z*S-d*(Se+2*g*S)+4*A*z*P-d*(Pe+2*g*P))
sub={m:0,j:0,me:0,je:0,a:0}
assert s.simplify(Q.subs(sub)-(-1+(1-h)*i-D*z*(ie+g*i)))==0
assert s.simplify(N.subs(sub)-E*(4*h*z*S-d*(Se+2*g*S)+4*A*z*P-d*(Pe+2*g*P)))==0
print('PASS exact 2x2 determinant, two terminal moment zeros, two jet zeros and stress reduction')
print('PASS negative control for omitted eta derivative; source numerical certificate remains OPEN')
