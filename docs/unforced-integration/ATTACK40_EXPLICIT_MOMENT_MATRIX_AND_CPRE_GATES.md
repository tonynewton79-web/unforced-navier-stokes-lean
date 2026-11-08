# Quantitative conditioning of source exterior moment corrections

Research update, 8 November 2026. **Restricted, source-specific partial theorem.** Neither a numerical bound for the entire \(C_{\rm pre}\) family, nor one fully matched original exterior, nor G1 local unforced convergence, nor global unforced Navier–Stokes blowup is proved.

Grounding: OpenAI's 2026 **forced** Navier–Stokes source, Appendix A (A.1)–(A.3), (A.10)–(A.12), (A.14)–(A.20). In both source two-bump corrections, the bump shape is the centred, width-\(3/10\) rescaling
\[
\beta(t)=(10/3)\sigma'((t+3/20)/(3/10)),\quad
\sigma(x)=\frac{e^{-1/x^2}}{e^{-1/x^2}+e^{-1/(1-x)^2}},
\]
extended by constants outside \([0,1]\). It is nonnegative, normalized, even, and supported on \([-3/20,3/20]\); hence \(b(s)=\int e^{st}\beta(t)\,dt\ge1\) for all real \(s\).

After the source's moment row normalizations and shifting the first bump centre to zero, its Jacobian is
\[
 B(s_1,s_2)=
 \begin{pmatrix}b(s_1)&e^{2s_1}b(s_1)\\b(s_2)&e^{2s_2}b(s_2)\end{pmatrix}.
\]
For \(0<\lambda\le1/16\), the pulse's \(s_1=1/2-\lambda,s_2=1/2-2\lambda\) yields the exact maximum-row-sum inverse bound
\[
\|B_{\rm axial}^{-1}\|_\infty<15/(14\lambda).
\]
For the later angular correction \(s_1=1-\lambda,s_2=-1-2\lambda\),
\[
\|B_{\rm angular}^{-1}\|_\infty<3/2.
\]
These are rigorous analytic bounds using the explicit determinant and \(b\ge1\). The standard numerical exponential inequalities are independently checked by exact rational Taylor intervals.

Source bump derivative bounds: \(\|\sigma'\|_\infty\le36,\|\sigma''\|_\infty\le5592\), so \(\|\beta\|_\infty\le120,\|\beta'\|_\infty<64000\).

For the source's angular correction after it has become \(\eta\)-independent, divide the quadratic pressure-moment row by 2 to normalize its linear part. The exact normalized nonlinear map is
\[
 F(c)=B_{\rm angular}c+Q(c,c),\quad Q(c,c)
 =\bigl(0,\tfrac12\int e^{s_2t}[c_1\beta(t)+c_2\beta(t-2)]^2dt\bigr).
\]
The supports are disjoint and \(\|Q\|\le(1/2)(6/5)(120)(1+1/7)=576/7<83\).
By the **original source's Lemma A.2**, if the *actual normalized discrepancy* satisfies
\[
\|d\|_{C^1[-1,1]}\le1/1500,
\]
there is a unique small solution \(\|c\|_{C^1}<3\|d\|_{C^1}\) because
\(8(3/2)^2(83)/1500=1494/1500<1\). Both rows are \(\eta\)-independent in this uniform angular stage, so the same bilinear estimate applies in the \(C^1\) Banach algebra. This is a **conditional quantitative nonlinear-moment theorem**, not an evaluation of \(d\) for one matched exterior.

If also \(\|d\|_{C^0}\le\lambda/10^6\), then \(|g_c|\le360\|d\|_\infty<1/4\), \(|g'_c|\le192000\|d\|_\infty\), and
\[
|\partial_y\log(1+g_c)|\le
192000\|d\|_\infty/[1-360\|d\|_\infty]<\lambda/2.
\]
Thus \(E>0\) and base \(l=-\lambda\) retains the strict \(l<-\lambda/2\) margin.

Two more original-source slope thresholds are **constructive**:
- A.10 profile interpolation: \(T_f=256\) ensures \(-\lambda-1/10<l\le-\lambda\) using \(\|\sigma'\|_\infty\le36\) and \(\log2<7/10\).
- A.12 final release: \(c_o=1/100,\ \rho_o=c_oh\) ensures \(-h\le l<-3h/4\) for \(0<h<1/100\).

The remaining global preliminary constant \(C_{\rm pre}\) is not a fixed numerical value in the original text: Appendix A.3 uses it for a family of bounds depending on earlier chosen \(M_d,T_d,P_*\) and on the finite derivative order. **No universal numerical bound for it is certified here.** Conditional on an independently established \(C\ge\max(1,C_{\rm pre})\), setting \(\lambda=e^{-2t}\) with \(t\ge\max\{5,2\log(1000C)\}\) guarantees \(C\sqrt\lambda[1+\log(1/\lambda)]\le10^{-3}\), but does NOT resolve the source's remaining stress-cone or heat/moment matching thresholds.

The actual normalized moment discrepancies, the additional 3×3 and 5×5 moment matching, the full source's \(C_{\rm pre}\), smallness of \(\lambda,h\) relative to ALL necessary conditions, radial leading analytic profile and all G1 startups remain OPEN. The original OpenAI theorem has a smooth compact force. The three-page scholarly PDF/LaTeX proof and 222-page cumulative edition preserving all earlier 219 pages, exact rational checker, visual audit and SHA-256 packet are separate conversation artifacts. Do not call this a numerical \(C_{\rm pre}\) certificate or a local/global unforced solution.