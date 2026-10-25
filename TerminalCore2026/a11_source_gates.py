"""Exact source A.10/A.11 finite scalar and symbolic replay.
The A.19 root, all post-pulse slope assumptions and unforced PDE
are NOT source-certified by this finite test.
"""
import mpmath as mp
import sympy as s
mp.mp.dps=85
I,J,C,Jp,rp=s.symbols("I J C Jp rp")
assert s.expand(-Jp*C*(rp+I)+Jp*C*(I-J)+Jp*C*(rp+J))==0
u1,u2,v1,v2,k,c1,c2=s.symbols("u1 u2 v1 v2 k c1 c2")
assert s.expand(v1*(c1+k*c1**2)+v2*(c2+k*c2**2)-
   (v1*c1+v2*c2+k*(v1*c1**2+v2*c2**2)))==0
e,h,A,d,W1,W0,W1e,W0e=s.symbols("e h A d W1 W0 W1e W0e")
lhs=4*h*e*W1/2-d*W1e/2-4*A*e*W0/2+d*W0e/2
rhs=2*e*(h*W1-A*W0)+d*(W0e-W1e)/2
assert s.expand(lhs-rhs)==0
print("PASS exact entrance differentiation, true quadratic row, full N_s kernel")
lam=mp.mpf(1)/20;a=1-lam;b=1+2*lam
sq=1/(1+mp.exp(mp.mpf(128)/9))
rfd=2/a*(mp.exp(-a*512)+sq+mp.exp(-a*128))
assert rfd<mp.mpf("1.41e-6")
assert 64*mp.log(2)/512<mp.mpf('.1')
detlo=mp.exp(mp.mpf('1.7'))-mp.exp(mp.mpf('-1.4425'))
assert detlo>5 and 33/detlo<7
assert mp.exp(mp.mpf('.33'))*(mp.mpf(640)/3)/2<150
epsmax=3*lam**mp.mpf('28.5')
assert epsmax<mp.mpf('1e-9')
assert 7*10800*14*epsmax<mp.mpf('.5')
assert 17976*lam**mp.mpf('28.5')<mp.mpf('.25')
assert 29960*lam**mp.mpf('28.5')<1
assert 4704000*lam**mp.mpf('27.5')<mp.mpf(3)/8
print("PASS endpoint derivative, B inverse, contraction, q/q_eta/q_y margins")
hmax=mp.mpf(1)/100
T1=mp.mpf(93)/20+mp.mpf(2)/3*hmax**7
const=(2*(mp.mpf(5)/4)**2*(hmax*T1+mp.mpf(51)/100)
      +mp.mpf(3)/5*(mp.mpf(5)/4))/(mp.mpf(3)/4)
assert const<4
assert 8*mp.exp(mp.mpf(63)/40)<40
print("PASS uniform conditional future-energy and N_s/E envelope")
Td=mp.exp(10)+10
lam=mp.mpf('1e-12')
logcond=mp.log(80)+(Td+1)+14*mp.log(lam)-mp.mpf(13)/(2*lam)
assert logcond<mp.mpf('-1e9')
assert lam<mp.mpf('1e-6')/(Td+512+1)
assert -2*Td<mp.log(lam)
print("PASS DIAGNOSTIC local parameter envelope; not full Appendix-A source")
