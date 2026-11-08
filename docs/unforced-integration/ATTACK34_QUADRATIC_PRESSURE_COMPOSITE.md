# Source-native bilinear pressure composite in the inherited G1 norm

Research note — 8 November 2026. **The positive-index quadratic delayed-pressure estimate is proved under a common analytic-domain multiplier hypothesis; the full G1 convergence and global unforced Navier–Stokes theorems remain OPEN.**

## Exact source normalization

From the original local-core coefficient hierarchy, let
\(L=1-2h\eta^2,\ d=1-\eta^2,\ D=1/2-h,\ A=1/2+h,\ \mu_j=D+2hj\), and
\(a=2\eta/L,\ b=-2\eta/L,\ c=-d/L\). The actual incompressibility map is
\[
V_j=X[aU_j+b\mu_j\mathcal A_XU_j+c\mathcal A_X\partial_\eta U_j],
\quad
\mathcal A_XF=X^{-1}\int_0^XF.
\]
For \(i+j=n-1\) and positive \(i,j\), the complete ordered quadratic pressure source is exactly
\[
\Omega_{n-1}^{quad}=\tfrac12(\partial_X-X^{-1})S_{n-1}+Q_{n-1},\
S_{n-1}=\sum V_iV_j,\
Q_{n-1}=\sum U_iZ_{0,j}V_j.
\]
The source-normalized radial pressure primitive is
\(\Pi_n^{lag,quad}=-S_{n-1}/(4X)-\frac12\mathcal C_XQ_{n-1}\), where
\(\mathcal C_XF=\int_0^XF(s)/s\,ds\).

## New exact six-term decomposition

Write \(\alpha=4h\eta/L,\ \beta=d/L,\ \gamma=-2\eta/L\), so \(Z_{0,j}=j\alpha+\beta\partial_\eta+\gamma\mathcal D_X\), \(\mathcal D_X=X\partial_X\). Using \(\mathcal D_X(X\mathcal A_XF)=XF\) and \([\mathcal A_X,\partial_\eta]=0\),
\[
X^{-1}Z_{0,j}V_j=
H_{0,j}U_j+H_D\mathcal D_XU_j+H_1\partial_\eta U_j+
H_{A0,j}\mathcal A_XU_j+H_{A1,j}\mathcal A_X\partial_\eta U_j+
H_{A2}\mathcal A_X\partial_\eta^2U_j,
\]
where
\(H_{0,j}=j\alpha a+\beta a'+\gamma a+\gamma b\mu_j,\ 
H_D=\gamma a,\ H_1=\beta a+\gamma c,\ 
H_{A0,j}=\mu_j(j\alpha b+\beta b'),\
H_{A1,j}=j\alpha c+\beta b\mu_j+\beta c',\ H_{A2}=\beta c\).
Every fixed coefficient is rational analytic in \(\eta\); its first derivative has finite norm in a sufficiently small common inherited analytic strip.

## Exact positive coefficient lemma and main theorem

Use the doubled weights \(w_{r,k}=R^{-r}\varrho^{-k}(2r+k)!/[(2r)!(r+1)^2(k+1)^2]\) and inherited ideals \(\mathcal I_n=X^n\mathcal B\). The prior positive product-algebra proof yields for split derivatives \(u+v=k\le3\):
\[
\sum_{a+b=m}\sum_{\alpha+\delta=\beta}\binom\beta\alpha
w_{a,\alpha+u}w_{b,\delta+v}\le C_{\rm alg}w_{m,\beta+k},
\]
since \(\binom\beta\alpha\le\binom{\beta+k}{\alpha+u}\) and the terms form a subfamily of the positive Leibniz majorant.
The two-lift weight quotient obeys
\[
w_{m,\beta+k}/w_{m+2,\beta}
\le9\cdot4^kR^2\varrho^{-k}(m+1)^k\qquad(k\le3).
\]
Assume the fixed similarity multipliers and their first axial derivatives are bounded in that same space (automatic for the displayed rational multipliers on a sufficiently small common analytic domain).

**Theorem.** For every \(n\ge3\), all \(U_i\in\mathcal I_i\) and the corresponding physical \(V_i\),
\[
\left\|J_1Z_{-2A,n}\frac{S_{n-1}}X\right\|_{\mathcal B}
+\left\|J_1Z_{-2A,n}\mathcal C_XQ_{n-1}\right\|_{\mathcal B}
\le C_{\rm quad}\!\sum_{i+j=n-1,\ i,j\ge1}
\|U_i\|_{\mathcal B}\|U_j\|_{\mathcal B}.
\]
Here \(C_{\rm quad}\) is finite and independent of \(n\). Both outputs lie in the stronger ideal \(\mathcal I_{n+1}\).

**Proof kernel accounting.** For input monomial degrees \(a\ge i,\ b\ge j\), write \(m=a+b\ge n-1\). Both source branches produce output degree \(m+2\). In \(S/X\), each \(V/X\) component carries either zero axial derivatives with a bounded radial coefficient, or one axial derivative with divisor \(a+1\) or \(b+1\). The outer shifted \(Z\) costs one derivative or \(O(m+1)\); \(J_1\) divides by \((m+2)^2\). The worst kernel is
\[
\frac{(m+1)^{u+v+1}}{(m+2)^2(a+1)^u(b+1)^v}\le1,\quad u,v\in\{0,1\}.
\]
Use \((a+1)(b+1)\ge m+1\) when both inputs are differentiated.

In \(Q\), the six-term decomposition reduces to the three normalized monomial types
\((m+1)U_j,\ \partial_\eta U_j,\ (b+1)^{-1}\partial_\eta^2U_j\),
after bounding \(j\le b\) and \(j^2/(b+1)\le b+1\). The primitive \(\mathcal C_X\) divides by \(m+1\), and \(J_1\) by \((m+2)^2\); the outer \(Z\) is one additional derivative or \(O(m+1)\). The three worst kernels reduce to
\[
\frac{m+1}{(m+2)^2},\quad
\frac{m+1}{(m+2)^2},\quad
\frac{(m+1)^2}{(m+2)^2(b+1)},
\]
all at most one. The positive split-derivative lemma and bounded fixed multipliers complete the infinite-index proof; no finite case enumeration is used in the theorem.

## Additional exact delayed-viscous pressure cancellation

The original source contains a **linear** viscous term \(-2X V_{n-1,XX}\) in \(\Omega_{n-1}\). Its pressure derivative contribution is exactly \(V_{n-1,XX}\), since \(\Pi_{n,X}\supset-\Omega_{n-1}/(2X)\). For \(k=n-1\ge1\), the valuation \(V_k\in X^{k+1}\mathcal B\) implies \(V_{k,X}(0,\eta)=0\). Therefore its *entire axis-normalized pressure primitive* is
\[
\Pi_n^{lag,visc}=V_{n-1,X}=-Z_{-A,n-1}U_{n-1}
\]
by the exact incompressibility equation. The final composed pressure contribution is
\(-J_1Z_{-2A,n}Z_{-A,n-1}U_{n-1}\).

**Uniform one-lift bound:** If the fixed rational coefficients and their required axial derivatives belong to the common analytic \(\mathcal B\), there is \(C_{\rm visc}<\infty\) independent of n with
\[
\|J_1Z_{-2A,n}Z_{-A,n-1}U_{n-1}\|_{\mathcal B}
\le C_{\rm visc}\|U_{n-1}\|_{\mathcal B}.
\]
Proof: On each radial degree \(a\ge n-1\), the two Z operators produce \(r=0,1,2\) axial derivatives at coefficient cost at most \(C(a+1)^{2-r}\). The *one-radial-lift* ratio satisfies
\(\mathcal W_{a,\beta+r}/\mathcal W_{a+1,\beta}\le4\cdot4^r R\varrho^{-r}(a+1)^r\).
The final J1 contributes \(1/(a+1)^2\). All index growth cancels. This proof never estimates the unbounded bare \(XV_{k,XX}\).

The **other** delayed linear terms \(T_{0,n-1}V_{n-1}\), \(-Z^{[2]}_{0,n-2}V_{n-2}\), and the leading-index cross-interactions still require the corresponding complete pressure composition estimates.

## Verification and limits

Independent source identity: 12 symbolic tests. Independent exact rational checks: 11,520 split-derivative convolution bounds and 715,208 source-graded radial kernel inequalities, plus a second ordered quadratic \(\Omega\) normal-form replay. All passed. These checks are **diagnostic**, not a Lean proof of the analytic theorem.

A four-page LaTeX/PDF supplement and 201-page cumulative edition retaining the previous 197 pages were created and visually audited in this conversation. The source-level theorem is restricted to **positive-index quadratic** \(\Omega_{n-1}\); it does not prove the remaining delayed linear \(T_{0,n-1}V_{n-1}\), \(-Z^{[2]}_{0,n-2}V_{n-2}\) or index-zero cross channels, actual leading-profile multiplier authentication, finite startup recursion, differentiated PDE reconstruction, global H8 stress or an unforced finite-time singularity.
