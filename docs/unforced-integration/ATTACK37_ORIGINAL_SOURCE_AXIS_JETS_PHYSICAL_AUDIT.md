# Original source startup authentication and physical-coordinate residual audit

8 November 2026. **PARTIAL EXACT SOURCE RESULTS; G1 LOCAL UNFORCED EXISTENCE AND GLOBAL UNFORCED NAVIER–STOKES REMAIN OPEN.** Continue the actual Appendix B.1--B.3 + (5.2)--(5.6) source, not a surrogate manufactured seed.

## The original leading datum remains existentially parameterized

For \(0<h<1/100\), \(A=1/2+h,D=1/2-h\), \(0<j_0\le1/20\), source Appendix B defines
\[
U_*(\eta)=4\eta+j_0,\quad H_*=D\eta+(1-\eta^2)U_*,\quad
L=1-2h\eta^2,\quad
\zeta_*=-LH_*/(H_*^2+\sigma_*^2),\quad
\phi_*=\exp\left(\Lambda\int_0^\eta\zeta_*(s)\,ds\right).
\]
The axis pressure \(P_*(\eta)\) is **not freely chosen**: original Lemma A.5 gives
\(P_*(\eta)=-\frac12\int_{-\infty}^{+\infty}E_{\rm ref}(y,\eta)^2dy\).
The leading radial holomorphic solution exists in Proposition B.2, but the original full parameter schedule chooses \(h,\sigma_*,\Lambda,C\) by successive existence/smallness thresholds and does NOT give one fully explicit numerical tuple or certified analytic constants. In particular a diagnostic \(h=1/200\) is **not certified as the admissible actual source parameter** merely because it lies in the open interval.

## New exact first two startup radial jets

Let \(f_k=\phi_*^{(k)}(0)\), \(P_k=P_*^{(k)}(0)\) (so \(f_0=1,P_1=0\)). Direct coefficient extraction from the true n=0,1,2 equations gives:
\[
U_{0,X}(0,0)=\frac{A+4}{2}j_0,\quad
\phi_{0,X}(0,0)=\frac{h-3+j_0f_1}{4};
\]
\[
U_{1,X}(0,0)=Aj_0,\quad
\phi_{1,X}(0,0)=\frac{1+h}{2}-\frac{f_2}{4};
\]
\[
\Pi_{1,X}(0,0)=(1+2h)P_0-\frac12P_2-12,\quad
\Pi_{2,X}(0,0)=0;
\]
\[
U_{2,XX}(0,0)/2=\frac9{16}(1-4h^2)j_0,\quad
\phi_{2,XX}(0,0)/2=
\frac{f_4+(12h-24)f_2+24-12h-36h^2}{48}.
\]
Additionally,
\(f_1=-\Lambda j_0/(j_0^2+\sigma_*^2)\),
\(f_2=[\Lambda(D+4)(j_0^2-\sigma_*^2)+\Lambda^2j_0^2]/(j_0^2+\sigma_*^2)^2\).
The source exterior pressure has \(P_0\le-\frac52 P_{\rm ref}^2<0\), is even, and has \(\eta P_*'(\eta)>0\) off zero; hence \(P_2\ge0\) and the **strict source-specific sign**
\[
\Pi_{1,X}(0,0)\le-12-\frac52(1+2h)P_{\rm ref}^2<-12.
\]
Independent symbolic Python replay of actual n0/n1/n2 regular-singular coefficient equations passed. These are **necessary axis jets**, not numerical full analytic startup functions.

## Explicit conditional common axis strip, NOT a complete startup domain

Let \(\delta_P>0\) be an unspecified source-supported holomorphy radius for the exterior pressure \(P_*\) around real \([-1,1]\). Set
\[
\delta=\min\{1/10,\sigma_*^2/880,\delta_P/2\}.
\]
On the tube \(\operatorname{dist}(\eta,[-1,1])<\delta\), \(|L|>0.97\), \(|H_*|<11\), \(|H_*'|<20\), \(|H_*^2+\sigma_*^2|\ge \sigma_*^2/2\), and
\(|\zeta_*|<23/\sigma_*^2\),
\(|\phi_*|\le \exp(26\Lambda/\sigma_*^2)\).
These follow by a uniform rational polynomial bound, independent of the pressure equation; the actual \(\delta_P\), the full leading *radial* domain and startup orders still require source-specific evaluation.

## Independent physical cylindrical residual, not just a formal operator replay

At positive times the implicit chart obeys
\[
q_t=-L^{-1},\quad q_z=2\eta q^{1-D}/L,\quad
\eta_t=D\eta/(qL),\quad \eta_z=q^{-D}(1-\eta^2)/L,\quad
X_t=X/(qL),\quad X_z=-2\eta Xq^{-D}/L.
\]
For finite mode sums \(\phi=\sum q^{2hn}\phi_n,\ U=\sum q^{2hn}U_n,\ V=\sum q^{2hn}V_n,\ \Pi=\sum q^{2hn}\Pi_n\), set
\(u_\theta=rq^{-A-1/2}\phi/C,\ u_z=q^{-A}U,\ u_r=V/r,\ p=q^{-2A}\Pi\).
Exact *physical* cylindrical momentum residual coefficients are precisely the original (5.3)--(5.6) brackets. An **independent** 47-digit direct numerical differentiation of physical fields with a numerically inverted implicit \(q(z,t)\) verifies all three generically NONZERO components (azimuthal, axial, radial) against their full source-ledger sums with normalized differences <=1.8e-47. This checks coordinate/symbolic reconstruction, **not zero residual for the genuine original profile**.

## Key missing assumption: the startup-strip selection is circular as written

The abstract threshold \(N_*(\rho)=\lceil2C_*(\rho)\rceil\) depends on the chosen strip through fixed-multiplier and derivative constants. The existence of each startup coefficient on some order-dependent analytic neighborhood **does not imply** that one can choose all indices below \(N_*(\rho)\) and afterward shrink \(\rho\) while keeping the same threshold.

Exact logical counterexample (NOT from Navier--Stokes): let \(F_n(\eta)=1/[1+(n+1)^4\eta^2]\) with analytic radius \(r_n=(n+1)^{-2}\) and \(C_*(\rho)=1/\rho\). Then \(N_*=\lceil2/\rho\rceil\) and the last required startup profile has radius \(1/N_*^2\le \rho^2/4<\rho\) for every \(0<\rho<1\). Orderwise analytic startup plus nominal \(O(n^{-1})\) feedback is not enough.

**Next release-critical step** is to freeze one admissible source parameter set + exterior pressure integral and certify its leading holomorphic product domain and inherited-norm constants, compute \(N_*\) without later shrinking the domain, verify every complete \(1\le n<N_*\) startup function (not just jets), and establish uniform differentiated zero PDE residual on the same domain. This has NOT been done. Global H8 cone stress and nonlinear unforcing remain separate open gates.

A four-page scholarly standalone PDF/LaTeX and a 213-page cumulative paper preserving 209 prior pages, with exact symbolic and independent 47-digit physical checks and SHA-256 validated proof ZIP, were generated as conversation artifacts. The original OpenAI paper is **forced**: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf. No unforced blow-up or local G1 convergence theorem is certified in this audit.
