# Exact early-stage control of the prescribed exterior-pressure moment

Research supplement, 8 November 2026. **Restricted mathematical result. Neither the full original forced exterior parameter schedule nor the proposed unforced G1 core is certified.** The global unforced 3D Navier–Stokes problem remains OPEN.

The source is OpenAI's *Finite Time Blowup for Navier–Stokes* (2026), equations (A.5)–(A.10) and Lemma A.5, not an arbitrary replacement exterior.

## Source-native exact early stages

In the source's pressure reference, \(E_{\rm ref}(y,\eta)=c(y)f(\eta)^{\vartheta(y)}\), \(f=(1+\eta^2)^{-1}\), \(0\le\vartheta\le1\), \(y=\log(X/X_R)\). Pressure-neutral angular correction bumps are omitted as prescribed. Put \(I_0=\int c^2dy\), \(I_1=\int\vartheta c^2dy\), \(T_d=e^{M_d+10}\), and \(P_*\) the original exterior amplitude.

- \(y\le0\): \(c=P_*e^{y/10}\), \(\vartheta=1\); contribution to **both** moments \(5P_*^2\).
- \(0\le y\le1\): source slope \(l=(3/5)(1-\sigma(y))\), so \(c=P_*\exp(y/10-(3/5)\int_0^y\sigma)\), \(\vartheta=1\). Source's smooth step satisfies \(\sigma(1-y)=1-\sigma(y)\), thus \(\int_0^1\sigma=1/2\) and exactly \(c(1)=P_*e^{-1/5}\).
- \(1\le y\le1+T_d\): \(l=0\), so \(c=P_*e^{-1/5}e^{-(y-1)/2}\) and \(\vartheta=1\). Its exact moment contribution is \(P_*^2e^{-2/5}(1-e^{-T_d})\).
- \(y\ge1+T_d\): in the prescribed *pressure reference*, all further stages have \(l\le0\): intermediate transition/power law, axial pulse, profile interpolation, angular bump corrections omitted in Lemma A.5, exterior release and terminal \(l=-h+f_o'/f_o<-3h/4\). Since \(\partial_y\log c=l-1/2\le-1/2\), the entire late mass is bounded by \(P_*^2e^{-2/5-T_d}\).

Define \(J_\sigma=\int_0^1\exp(y/5-(6/5)\int_0^y\sigma(s)ds)dy\), \(B_d=P_*^2(5+J_\sigma+e^{-2/5}(1-e^{-T_d}))\), and \(\varepsilon_d=P_*^2e^{-2/5-T_d}\). Then the **exact original schedule** satisfies

\[
B_d\le I_1\le I_0\le B_d+\varepsilon_d,\qquad
0\le I_0-I_1\le\varepsilon_d.
\]

Since \(P_{\rm ax}(\eta)=-\tfrac12\int c^2(1+\eta^2)^{-2\vartheta}dy\), on \(|\operatorname{Im}\eta|\le1/4\),

\[
|P_{\rm ax}(\eta)+B_d/[2(1+\eta^2)^2]|
\le(128/225)\varepsilon_d.
\]

At any real axis point the m-th derivative of this difference has modulus at most \((128/225)\varepsilon_d4^m m!\). These bounds are independent of the unknown later matching amplitudes and heat corrections **provided the pressure datum is preserved as stipulated in the source**.

## Exact rational, reproducible quadrature (not floating point)

For the universal unit-interval transition \(J_\sigma\), monotonic step samples, lower/upper Riemann sums for the primitive \(S(y)=\int_0^y\sigma\), Taylor polynomial bounds of \(\exp\), and outward \(2^{-44}\) dyadic rounding give at mesh \(N=4096\)

\[
\frac{69086996650998241}{72057594037927936}
\le J_\sigma\le
\frac{69108717989414755}{72057594037927936}.
\]

Equivalently \(0.9587746798<J_\sigma<0.9590761240\). Taylor-to-degree-18 error is bounded by \(t^{19}/[19!(1-t/20)]\) for \(0\le t\le1/2\), scaling \(\exp(a)=[\exp(a/m)]^m\). At source nodes with \(a=1/y^2-1/(1-y)^2\ge40\), \(0<\sigma\le2^{-40}\) follows from \(e>2\). Every arithmetic enclosure uses Fraction/rational comparisons. A separate standard ODE quadrature gave approximately \(0.95892541\) **only as a diagnostic**, agreeing with the rigorous certificate.

Therefore \(I_0<(663/100)P_*^2\), so one may freeze a **schedule-independent sufficient axis screening value**
\[
\sigma_{\mathrm{ax}}=
\frac{j_0}{200(104+24(663/100)P_*^2)}
\]
which is no larger than the previous moment-dependent B.2 sufficient choice and preserves B.2's screening implication. It is not a full source parameter-admissibility certificate.

## Missing scientific work

This bypasses the later exterior for **pressure moments alone**. The original source still uses threshold-dependent \(M_d,T_d,P_*,\lambda,h\), unknown moment-correction amplitudes, strict cone inequalities and heat-compensation choices. No one fully admissible numerical tuple, complete matched exterior, radial leading holomorphic solution, noncircular finite startup threshold, full G1 correction or zero unforced PDE residual is certified. The OpenAI original theorem is **forced**, not unforced.

A polished 3-page LaTeX/PDF proof, exact rational Python certificate, validated ZIP, and 219-page cumulative research edition preserving all earlier 216 page text streams were produced in the conversation. Keep this PR DRAFT.


## Further exact original pulse integral, source (A.19)

The source uses \(\phi_b(\xi)=\int_0^\xi\sigma(v/(1/50))\,dv\), \(R_0(\xi)=\phi_b(\xi)[1-\sigma(\xi-10)]\), and \(K_b=\int_0^{13}e^{-2\xi}R_0(\xi)^2d\xi\). Cutoff symmetry implies \(\phi_b(\xi)=\xi-1/100\) **exactly for \(\xi\ge1/50\)**, \(R_0=\phi_b\) for \(\xi\le10\), and \(R_0=0\) for \(\xi\ge11\). Bound the early \(0\le\xi\le1/50\) mass by \(1/375000\) and the last cutoff by the explicit \(\int_{10}^\infty e^{-2\xi}(\xi-1/100)^2d\xi=(1102901/20000)e^{-20}\). Then

\[
(5101/20000)e^{-1/25}-(1102901/20000)e^{-20}
\le K_b\le(5101/20000)e^{-1/25}+1/375000.
\]

Exact rational exponential enclosures certify \(0.2450492327<K_b<0.2450520132\). The principal source A.19 amplitude satisfies \(K_b\mathsf A^2=(1-e^{-26})/4\), hence \(1.01004<\mathsf A_{\mathrm{principal}}<1.01006\). If the source's separate error \(|\mathcal E(\mathsf A,\eta)|\le10^{-3}\), then **conditionally** any positive corrected root lies in \(1.008<\mathsf A<1.013\). The source only establishes \(|\mathcal E|\le C_{\mathrm{pre}}\lambda(1+\log(1/\lambda))\) with unquantified \(C_{\mathrm{pre}}\), so the full corrected pulse and moment-restoring coefficients are **not certified**. The result is a universal source-shape calculation, not a complete exterior construction.
