# Attack 32 — delayed \(\Omega_{n-1}\) pressure source and inherited-norm majorant

**8 November 2026. Status: partial exact results / G1 remains OPEN.** This note continues Attacks 30–31, reusing the genuine core recurrence in \`Exact_Local_Unforced_Terminal_Core_Dynamics_JFM_FINAL.tex\`, and Proposition A.29/A.65–A.66 in the October 29 83-page manuscript. No full unforced Navier–Stokes singularity or G1 local convergence theorem is claimed.

## I. Exact nonzero delayed pressure quadratic

The source hierarchy is
\[
\Pi_n' = C^{-2}\sum_{i+j=n}\phi_i\phi_j - \Omega_{n-1}/(2X),
\]
\[
\Omega_k=T_{0,k}V_k+\sum_{i+j=k}V_i(V_{j,X}-V_j/(2X))
+\sum_{i+j=k}U_i Z_{0,j}V_j-2X V_{k,XX}-Z^{[2]}_{0,k-1}V_{k-1}.
\]
Thus the *pressure* at order \(n\) contains an independent quadratic sum with \(i+j=n-1\).

For a valuation-compatible **algebraic diagnostic** set \(U_1=X\), \(\phi_1=0\), and order-two positive fields to zero. Using \(D=1/2-h\), \(L=1-2h\eta^2\) and exact incompressibility,
\[
V_1=\frac{(3/2-h)X^2\eta}{L}.
\]
The isolated quadratic component satisfies
\[
\Omega_{2,\mathrm{quad}}(X,0)=(3/2-h)X^3,\qquad
\Pi_{3,\mathrm{lag}}(X,0)=-(3/2-h)X^3/6.
\]
At \(h=1/200,\eta=1/3\), the full shifted physical derivative is
\[
Z_{-2A,3}\Pi_{3,\mathrm{lag}}
=\frac{2029547156783445}{2348867127617996}X^3\neq0.
\]
This diagnostic need not satisfy the complete coefficient hierarchy; it proves **no universal source-identity cancellation** permits deleting the lagged term. With only \(A_1\neq0\), \(\sum_{i+j=3,i,j\ge1}A_iA_j=0\), but \(\sum_{i+j=2,i,j\ge1}A_iA_j=A_1^2>0\).

## II. New uniform degree-four *model* estimate

For \(R,\varrho>0\) use the manuscript's doubled weights
\(a_{j,b}=R^{-j}\varrho^{-b}(2j+b)!/[(2j)!(j+1)^2(b+1)^2]\)
and **inherited** ideal norm \(\|F\|_{\mathcal I_m}=\|F\|_{\mathcal B}\), never the factored norm refuted by A.29.

For \(n\ge1\), \(k,p,s\ge0\), \(k+p+s\le4\), and \(F=\sum_{j\ge\max(0,n-2)}f_jX^j\), define
\[
\mathcal T_{n;k,p,s}F
=\sum_j \frac{n^s j^p}{(j+1)^2(j+2)^2}
\partial_\eta^k f_j\,X^{j+2}.
\]
Then, **uniformly in \(n\)**,
\[
\boxed{\|\mathcal T_{n;k,p,s}F\|_{\mathcal B}
\le9\,4^k2^sR^2\varrho^{-k}\|F\|_{\mathcal B}.}
\]
Proof: exact ratio
\[
\frac{a_{j,b+k}}{a_{j+2,b}}
=R^2\varrho^{-k}\frac{(j+3)^2}{(j+1)^2}
\frac{(b+1)^2}{(b+k+1)^2}
\frac{\prod_{t=1}^{4}(2j+t)}
{\prod_{t=k+1}^{4}(2j+b+t)}.
\]
Cancel the final \(4-k\) factors, bound by \(9R^2\varrho^{-k}(2j+4)^k\); use \(n\le j+2\le2(j+1)\), \(j\le j+1\), and \((j+1)^2(j+2)^2\ge(j+1)^4\).

**Do not overclaim:** This is a *single-input complete model-channel* bound. It is NOT a proof of the full split-derivative bilinear \(\Omega_{n-1}\) composition with physical variable-coefficient multipliers and individual radial denominators. That source-specific analytic lemma remains open.

Also the bare \(X\partial_X^2\) is **unbounded** in the inherited space:
for \(F_N=a_{N,0}X^N\), \(\|F_N\|=1\) but
\[
\|X\partial_X^2F_N\|
=\frac{N(N-1)}R\frac{N^2}{(N+1)^2}\to\infty.
\]
Thus no legal proof may control \(-2XV_{n-1,XX}\) separately by a uniform \(\mathcal B\to\mathcal B\) bound; it must retain the complete radial inverse / pressure composite.

## III. Explicit corrected majorant theorem (conditional on complete source estimate)

If \(A_n\ge0\), \(A_0=0\), and
\[
A_n\le p_n+a(A_{n-1}+A_{n-2})
+c\sum_{\substack{i+j=n\\i,j\ge1}}A_iA_j
+d\sum_{\substack{i+j=n-1\\i,j\ge1}}A_iA_j,
\]
with finite \(P(z)=\sum p_nz^n\) having nonnegative coefficients and \(P(0)=0\), then the nonnegative-coefficient majorant
\[
\boxed{Y=P+a(z+z^2)Y+(c+dz)Y^2}
\]
is analytic near \(z=0\) and coefficientwise dominates \(A_n\).

An explicit certified radius is any \(r>0\) with
\[
a(r+r^2)\le1/4,\qquad (c+dr)P(r)\le1/16,\qquad P(r)>0.
\]
Indeed its defining map contracts the closed analytic sup-norm ball of radius \(2P(r)\) with Lipschitz constant \(\le1/2\), giving
\[
A_n\le [z^n]Y\le2P(r)r^{-n}.
\]
This is an elementary contraction/majorant result and was **already structurally anticipated by October 29 A.66**; do not claim originality for the general recurrence.

## IV. Exact replay and remaining proof

The standalone Python/SymPy verifier checks 17,360 exact rational ratio instances across all \(k+p+s\le4\), proves the nonzero quadratic source and off-axis pressure action symbolically at \(h=1/200\), checks the bare radial derivative no-go, and verifies the first 12 positive rational majorant coefficients at \(P=z+2z^2\), \(a=3/2\), \(c=4/5\), \(d=5/7\), with explicit radius \(r=1/100\). The analytic proofs do not depend on finite verification samples.

**Still required to close G1:** uniform bilinear estimates for all split \(\eta\)/Euler derivatives and differently placed radial denominators in the genuine \(\Omega_{n-1}\) terms; fixed analytic multiplier/commutator and leading-profile bounds; the full four-block \(K_n\) estimate in the inherited norm; the startup hierarchy and differentiated physical PDE reconstruction. The main 16-page local-core existence claim remains in need of this independent reconciliation.

The four-page scholarly PDF/LaTeX note was appended to the prior 189-page cumulative manuscript, with all prior 189 pages' text preserved, producing a 193-page edition. Artifact and exact replay are available as chat files. The previous pinned Lean Attack 31 *finite polynomial* CI run passed; **the new infinite-dimensional claims are not kernel-checked in Lean**.
