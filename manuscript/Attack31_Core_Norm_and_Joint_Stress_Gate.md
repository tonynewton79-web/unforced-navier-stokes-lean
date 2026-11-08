# Attack 31: inherited analytic norm and joint H8 modal/torque dual (8 November 2026)

**Status: exact restricted operator estimates and a conditional, source-matched necessary inequality. Unforced 3D Navier–Stokes finite-time blowup remains OPEN.** Full standalone LaTeX/PDF note and exact rational replay were produced in the chat's research packet, and appended to the previous 184-page manuscript as a 189-page cumulative paper; prior pages are unchanged.

## G1: precise partial analytic-norm repair

The 29 October 83-page edition, Proposition A.29, correctly refutes a shifted \(J_\nu \partial_\eta\) estimate under the *factored* norm \(\|X^mF\|_{\mathcal I_m}=\|F\|_{\mathcal B}\). Do not reuse that false bound.

With doubled analytic coefficient weights

\[
 a_{j,\beta}=\frac{R^{-j}\varrho^{-\beta}\beta! \binom{2j+\beta}{\beta}}{(j+1)^2(\beta+1)^2}
\]

and **inherited** ideal norm \(\|F\|_{\mathcal I_m,\mathrm{inh}}=\|F\|_{\mathcal B}\), all \(F\in X^m\mathcal B\) satisfy, for \(\nu=1,2\),

\[
\|J_\nu F\|_{\mathcal B}\le \frac{4R}{(m+1)^2}\|F\|_{\mathcal B},\quad
\|J_\nu \partial_\eta F\|_{\mathcal B}\le \frac{8R}{\varrho(m+1)}\|F\|_{\mathcal B},\quad
\|J_\nu \partial_\eta^2 F\|_{\mathcal B}\le \frac{16R}{\varrho^2}\|F\|_{\mathcal B}.
\]

These follow from *exact* coefficient weight ratios and nonnegative polynomial slacks.

### Genuine incompressibility primitive: keep the radial lift

The source-native incompressibility formula is
\(V_n=\frac{X}{L}[2\eta U_n-2\eta(D+2hn)\mathcal A U_n-d\partial_\eta\mathcal A U_n]\),
where \(\mathcal AF=X^{-1}\int_0^X F\), \(L=1-2h\eta^2\), and \(d=1-\eta^2\).
The *bare* \(\partial_\eta\mathcal A\) is not bounded in a fixed analytic norm. The actual field uses \(X\partial_\eta\mathcal A\), which has the needed radial lift. In the inherited norm,
\[
\|XF\|_{\mathcal B}\le4R\|F\|_{\mathcal B},\quad
\|X\mathcal A F\|_{\mathcal B}\le \frac{4R}{m+1}\|F\|_{\mathcal B},\quad
\|X\mathcal A\partial_\eta F\|_{\mathcal B}\le\frac{8R}{\varrho}\|F\|_{\mathcal B}.
\]
For \(n\ge1\), \((D+2hn)/(n+1)\le D+2h\), so the complete \(\mathcal V_n:\mathcal I_n\to\mathcal I_{n+1}\) is uniformly bounded if the fixed analytic \(\eta/L,d/L\) multipliers satisfy their algebra bounds. This is a nontrivial **source-native kinematic block**, not merely a toy scalar radial inverse. It is still insufficient to establish the other variable-coefficient and nonlinear pressure blocks.

### Four transverse derivatives in the delayed pressure model

Let \(\mathcal P F(X)=\int_0^X s^{-1}\int_0^s F(u)\,du\,ds\). The model operator \(T=J_1\partial_\eta^4 \mathcal P\) has coefficient divisor \((j+1)^2(j+2)^2\) and

\[
 \frac{a_{j,\beta+4}}{(j+1)^2(j+2)^2 a_{j+2,\beta}}
 = \frac{4R^2}{\varrho^4}
\frac{(j+3)^2(2j+1)(2j+3)}{(j+1)^3(j+2)}
\frac{(\beta+1)^2}{(\beta+5)^2}.
\]

The exact slack
\(54(j+1)^3(j+2)-4(j+3)^2(2j+1)(2j+3)
=2j(19j^3+71j^2+69j+9)\ge0\)
proves \(\|TF\|_{\mathcal B}\le54R^2\varrho^{-4}\|F\|_{\mathcal B}\) uniformly over \(m\).
If one internal primitive is discarded, the coefficient majorant is \((j+1)\) times this ratio and grows as \(16jR^2/\varrho^4\) for large radial degree. This is a coefficient-level failure of that reduced argument; no claim about every physical pressure operator.

This **does not** close the full G1 source theorem: analytic multiplier/commutator bounds, all current-order blocks, complete lower-order pressure sources, the \(\sum_{i+j=n-1}A_i A_j\) term identified in the October 29 audit, finite startup data and differentiated physical reconstruction remain unproved in one common norm.

## New joint source-matched H8 necessary inequality

For ONE smooth periodic solenoidal prepared carrier \(U\), define
\(W=\partial_zU\), \(G=U_t-\nu\Delta U+\mathbb P\mathrm{div}(U\otimes U)\),
\(M=\|U\|_2^2>0\), \(N=\|W\|_2^2>0\),
\(c_A=\langle G,U\rangle/M\), \(g_T=\langle G,W\rangle/N\).

Assume a source-matched compact stress satisfies
\(\mathbb P\mathrm{div}S=-G\),
\(S=\rho R_*+E H(A,B,C,D)E^\top\),
\(H=[[-D,C,A],[C,0,B],[A,B,D]]\),
and the original *one-sided seven-ray floors*
\(c_i^{(0)}\rho+\delta c_i\ge\rho/100\).
Write \(\ell_E(K)\) for the physical frame-pulled four-dimensional gradient covector:
\[
\ell_E(K)=\bigl(\widetilde K_{13}+\widetilde K_{31},\
\widetilde K_{23}+\widetilde K_{32},\
\widetilde K_{12}+\widetilde K_{21},\
\widetilde K_{33}-\widetilde K_{11}\bigr),\
\widetilde K=E^\top K E.
\]

Let \(\sigma^+\) be the *already established* sharp support of the original one-sided cone, with \(g=15971/122900\), \(h_0=22371/122900\):
\[
\sigma^+(a,b,c,d)=\frac{h_0-g}{4}c+\frac g8|4a+b|+
\max\left\{\frac{3g+h_0}{4}|c|-\frac g4d,\
\frac{3g+h_0}{4}|a|+\frac{g+h_0}{8}d\right\}.
\]

For **every** triple \(\lambda,\mu,\zeta\in\mathbb R\) and compact smooth divergence-free test \(Z_\psi\), put
\(\Phi=\lambda U+\mu W+\zeta Z_\psi\). Then the source-matching identity and sharp pointwise cone support yield

\[
\lambda M c_A+\mu N g_T+\zeta\langle G,Z_\psi\rangle
-\int_{\mathbb T^3}\rho R_*:\nabla\Phi\,dx
\le \int_{\mathbb T^3}\rho\,\sigma^+\bigl(\ell_E(\nabla\Phi)\bigr)\,dx.
\]

The inequality with the negative triple supplies the opposite-sided gate. A violation for even one triple rules out that particular source-matched positive stress. It is NOT sufficient for existence.

For a compact axisymmetric swirl test \(Z_\psi(r,z)=r\,\xi(r)\psi(z)e_\theta\) with \(\xi=1\) on the support of the non-pressure residual, exact divergence-freeness gives \(\langle G,Z_\psi\rangle=\int \psi(z)m(z)\,dz\), \(m(z)=\int r^2 F_\theta\,dr\,d\theta\). This simultaneously probes amplitude, translation and the same toroidal slice moment, **without changing pressure conventions**.

The source's original one-sided polytope has exactly 8 rational vertices. The known support formula was independently verified against all eight vertices for 150 deterministic rational dual covectors. That formula itself is prior programme work, not a new cone discovery.

## What remains unproved

The genuine normally convergent local-core convergence argument needs the full common-norm G1 closure. No single periodic authentic tuple \(U_c,p_c,A_c,\chi,\) shapers, \(E,\rho,R_*,p\) has been jointly verified with all source-specific estimates. The earlier Appendix A.5 singular-seed diagnostic is already excluded by separate interior-axis and calibrated toroidal-flux obstructions; it is not a stand-in for the genuine core.

Thus \(c_A,g_T,m,\sigma^+\) are not yet evaluated together for the genuine core. Nor are both Appendix Q terminal-dyad injections, the complementary nonlinear PDE, global pressure/energy transport and pointwise retention established. No completed local convergence theorem, source-matched H8 inverse or unforced 3D blowup follows from this attack.
