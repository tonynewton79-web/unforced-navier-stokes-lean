# Quantitative corrected pulse amplitude and original axial two-moment restoration

Research note, 8 November 2026. The OpenAI 2026 source is a **forced** Navier–Stokes construction. This result certifies a conditional finite-dimensional stage of its prescribed exterior, **not** the full original exterior, local unforced G1 convergence, or global unforced singularity.

**Source**: OpenAI, *Finite Time Blowup for Navier–Stokes* (2026), Appendix A.3, source (A.19)–(A.20), [original PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf). Reuse the actual source-normalized upstream M_p,J_p and axial discrepancy from Attack 41; the original two-bump inverse from Attack 40; and the independently interval-certified original fixed-pulse K_b from Attack 39.

## 1. Explicit implicit-function theorem

The full scalar source equation is
\[
F(\mathsf A,\eta)=K_b\mathsf A^2-\frac{1-e^{-26}}4+\mathcal E(\mathsf A,\eta)=0,
\]
where \(0.2450492327<K_b<0.2450520132\). The source gives a joint \(C^1\) estimate \(\|\mathcal E\|_{C^1([0.9,1.2]\times[-1,1])}\le C_{\rm pre}\lambda(1+\log(1/\lambda))\), with C_pre unspecified but fixed after earlier parameters.

**Theorem.** If the actual remainder satisfies \(\|\mathcal E\|_{C^1}\le1/100\), there is a unique \(C^1\) corrected root in \([0.9,1.2]\), and
\[
49/50<\mathsf A(\eta)<26/25,\qquad
\|\partial_\eta\mathsf A\|_\infty<1/47.
\]
Proof: strict rational endpoint signs at A=49/50,26/25; positive derivative throughout the broad bracket, and
\[
\partial_{\mathsf A}F\ge2(0.2450492327)(49/50)-.01>.47
\]
on the root bracket. Implicit differentiation gives \(\mathsf A_\eta=-(\partial_\eta\mathcal E)/(\partial_{\mathsf A}F)\). More precisely
\(\|\mathsf A_\eta\|\le(100/47)C_{\rm pre}\lambda(1+\log(1/\lambda))\) whenever the initial tolerance is met.

## 2. Exact source-normalized axial correction, now in C1

The *actual* original axial discrepancy after all upstream reference and axial-transition stages (Attack 41) is
\[
d_{\rm ax}(\eta)=-
\binom{e^{-s_1Y_p}M_p/(X_pE_p)+\mathsf A(\eta)L_1(\lambda)}
{e^{-s_2Y_p}J_p/(X_pH_pE_p)+\mathsf A(\eta)L_2(\lambda)},
\]
where \(s_1=1/2-\lambda,s_2=1/2-2\lambda,Y_p=13/\lambda-3\), and
\(L_i=\int_0^{11/\lambda}e^{-s_i(Y_p-v)}R_0(\lambda v)dv\).
The original \(R_0\) is supported in \([0,11]\) and is between zero and 11.

For \(M_d\ge0,P_*\ge1,0<\lambda\le1/64\), the exact upstream pre-pulse normalized ratios have \(C^0\) bounds \(8e^{-499},58e^{-499}\); their analytic eta factors are proportional to \(\eta(1+\eta^2)\), so their combined scalar \(C^1\) bound is at most \(198e^{-499}\), before further \(e^{-s_iY_p}\) factors. Also
\[
0\le L_i\le\frac{352}{15}\exp[-(1/\lambda-11/2+6\lambda)].
\]
The exponent is at least \(1875/32\) on \(0<\lambda\le1/64\), and \(e^{-1875/32}<10^{-25}\).

Use the vector \(C^1\) norm **sup_eta \(\ell^\infty\) value + sup_eta \(\ell^\infty\) first derivative**, matched to the matrix \(\infty\)-operator norm. The exact original two-axial-bump inverse satisfies \(\|B^{-1}\|_\infty<15/(14\lambda)\). Crucially **do not bound \(1/\lambda\) by 64**: \(\lambda\) may be smaller. Instead
\[
\lambda^{-1}e^{-(1/\lambda-11/2+6\lambda)}
\]
and its upstream analogue \(\lambda^{-1}e^{-(13/(2\lambda)-55/2+6\lambda)}\) are increasing on \((0,1/64]\). For the stronger relative bound, the same holds after replacing \(\lambda^{-1}\) with \(\lambda^{-2}\).

**Theorem.** Under the \(\|\mathcal E\|_{C^1}\le1/100\) condition, for all allowed \(\lambda\)
\[
\|d_{\rm ax}\|_{C^1}<10^{-23},\qquad
\|c_{\rm ax}\|_{C^1}<4\cdot10^{-22},\qquad
\|c_{\rm ax}\|_{C^1}<3\cdot10^{-20}\lambda.
\]
The original axial matching equations are linear in the two added U-bump coefficients and therefore exactly solvable. The two normalized bumps are disjoint and satisfy \(\|\beta'\|_\infty<64000\); hence their combined log-radial derivative has magnitude \(<2\cdot10^{-15}\lambda\). This is NOT a certificate of the complete physical H8 stress cone.

## 3. Numerical C_pre remains a decisive obstruction

The source gives a finite \(C_{\rm pre}\) for each frozen earlier parameter schedule, but does not state a number. Therefore it guarantees \(\|\mathcal E\|_{C^1}\le1/100\) for sufficiently small \(\lambda\) **existentially**, but not at one certified numerical \(\lambda\). If an independent explicit bound \(C\ge\max\{1,C_{\rm pre}\}\) is known, one sufficient scalar selector is \(t=\max\{3,\log(100C)\},\ \lambda=e^{-2t}\), **provided** the source estimates apply at that \(\lambda\): then \(C\lambda(1+\log(1/\lambda))\le1/100\) and \(\lambda<1/64\). Other prior parameter-smallness constraints, heat matching and the separate three-/five-moment receiver systems are not covered.

**Verification:** the chat package has the polished 3-page complete LaTeX/PDF proof, independent exact-rational and symbolic checker, strict exponential Taylor witnesses, a source audit, and SHA-256 verified ZIP. The earlier 225-page cumulative manuscript's extracted text was exactly preserved, adding the 3-page note to produce 228 pages. The finite checker is not an infinite-dimensional Lean or PDE theorem.

**Unsolved**: quantify the actual source remainder constant, choose one fully admissible \(M_d,T_d,P_*,\lambda,h\), certify later heat/three-/five-moment and strict seven-ray stress, freeze a common analytic leading-core domain and all startups, prove local G1 convergence and actual zero unforced PDE residual. Global unforced Navier–Stokes finite-time blow-up remains OPEN.
