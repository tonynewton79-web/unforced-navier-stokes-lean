# Proof Attack 13 / Edition XVIII — source heat-exterior derivative certificate
Date: 23 October 2026

BASELINE SYNCHRONIZATION:
The shared branch already contained an independent source-axis third-jet
Edition XVI and conditional Cauchy-radius Edition XVII. Both were
preserved. This new exterior certificate is additive Edition XVIII.

EXACT SOURCE INPUT:
OpenAI's *Finite Time Blowup for Navier–Stokes* (FORCED), Theorem
4.6(v), equation (4.29): for X>=X_b,
E=c_inf X^(-A) H(2(1-eta^2)/X),
H(Z)=Gamma(1+h)^(-1) int_0^infty exp(-v) v^h (1+Zv)^(-h) dv,
A=1/2+h, D=1/2-h, 0<h<1/100, c_inf>0.

CRUCIAL EXACT CANCELLATION:
With tau=q(1-eta²), X=r²/(2q), R=r/sqrt(tau),
u_theta^(0)=tau^(-A) f(R),
f(R)=c_inf 2^A E_{V~Gamma(1+h,1)}[R^(-1)(R²+4V)^(-h)].
The exterior physical swirl is independent of z.

THIRD DERIVATIVE:
For a>=0 and h>0,
-g'''(R)=P_h(a,R)/(R^4(R²+a)^(h+3))>0 for
g(R)=R^(-1)(R²+a)^(-h), and
P_h=6a³+(6h+18)a²R²+(12h+18)aR⁴+
 (1+2h)(2+2h)(3+2h)R⁶.
Thus f'''(R)<0 everywhere in the exterior. This is an exact
SOURCE-leading profile result, independent of the Gaussian model
or the inner-axis Cauchy-radius input.

EXPLICIT L3 CERTIFICATE:
Take zeta=1/4, b>a>=2 sqrt(X_b), Q=q/tau.
For |Z|=|z|/tau^D<=zeta, 1<=Q<2 and X>=X_b. Let
m = c_inf 2^A e^-1 (1+2h)(2+2h)(3+2h) a² /
  [Gamma(h+2) (b²+4)^(h+3)] >0.
Then -f'''(R)>=m for R in [a,b] and the source leading field
has ||u^(0)||H3 >= m sqrt(pi(b²-a²)/12) tau^(-5/4-3h/2).
The constant is explicit in the published source's parameters,
but not numerically frozen by the source.

Independent SymPy polynomial differentiation and 10,000/10,000
exact rational controls PASSED. Three independent mpmath
60-digit gamma derivative evaluations and lower bounds PASSED.
Illustrative h=.005, c_inf=1, X_b=2, [a,b]=[4,5]:
m>=0.0020535346235764254 and
C_ext>=0.0031521552389978923, MODEL CHOICES ONLY.

BOUNDARY:
No claim that the FULL final forced or proposed unforced physical
velocity preserves this source-leading slab; oscillatory corrections,
localization, axis/exterior matching and residual cancellation are
still uncaptured. Neither a projected full physical residual nor
zero forcing or an unforced blowup theorem is proved.
Lean source N1ExteriorDerivativeScalar.lean formalizes finite scalar
polynomial/exponent consequences ONLY; the gamma integral,
Sobolev tensor estimate and PDE remain unformalized.
No Lean kernel PASS before completed GitHub CI logs.

Release: two-page Edition XVIII proof, continuity note for
editions XVI/XVII, prior full 31-page Edition XV cumulative PDF.
The new cumulative research PDF is 34 pages. XVI/XVII are
summarized from their canonical GitHub source rather than
reproduced as their standalone full PDFs. The full master TeX
is updated on GitHub; this is an assembled research addendum.
