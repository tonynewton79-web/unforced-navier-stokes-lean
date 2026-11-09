# A source-first compact-stress falsification audit

9 November 2026. **Two precise negative results, not a positive existence theorem.** A regular compact source-selected model has been independently verified in PR #30, but it does not solve the inverse for the preassigned singular H8 residual. The actual analytic G1/H8 carrier remains unbuilt as a fully authenticated source tuple.

## I. Vacuum-collar annihilator

Let \(\rho\ge0\) be smooth with an open vacuum \(V\subset \{\rho=0\}\). Any compact smooth tensor \(S\) supported where \(\rho\ne0\) obeys, for each solenoidal \(v\in C_c^\infty(V)\),
\[
 \langle \mathbb P\nabla\cdot S,v\rangle=-\int S:\nabla v=0.
\]
This is independent of periodic pressure and of seven-ray positivity. It proves that the set of projected sources compatible with one fixed compact support is contained in a proper closed hyperplane, hence is nowhere dense in the smooth mean-zero solenoidal source space. For the exact regular model of Theorem A.6 take \(v=\nabla\times[\prod_j \kappa(x_j-1/2)e_3]\), supported away from the model's compact \(\rho_\delta\). For every \(\epsilon\ne0\), \(f_\epsilon=\mathbb P\nabla\cdot S_\delta+\epsilon v\) CANNOT be matched by ANY stress on that same support: its pairing with \(v\) is \(\epsilon\|v\|_2^2\ne0\), even when \(|\epsilon|\ll\delta\). Thus ordinary source-smallness is NOT enough to transfer a manufactured stress to a preassigned residual.

## II. Explicit rational no-go for the old calibrated FROZEN diagnostic

This uses the pre-existing Attack 29 source identity, NOT the genuine B.12 analytic core. Set \(\tau=1-t\), \(0<h<1/100\), \(\beta_*=1/2-2h\), and the source's flat cutoff \(b\): \(b=1\) on \([0,1/2]\), \(b=0\) beyond 1, and \(b(y)+b(3/2-y)=1\) on \([1/2,1]\). For the EXACT globally torque-calibrated frozen source, the pressure-free central toroidal flux is \(4\pi aK\tau^{\beta_*}>0\), with
\[
 f(X)=b(64X),\quad a=\frac{C_1H_\mathrm{all}}{C_0G_\mathrm{all}},\quad
 C_0=\int f,\ C_1=\int Xf,\quad K=\int X f'(f+Xf').
\]
- By symmetry \(\int_0^1 b=3/4\), so \(C_0=3/256\). Since \(b\ge1/2\) on \([1/2,3/4]\), \(C_1/C_0\ge13/3072\).
- \(H_\mathrm{all}/G_\mathrm{all}\) is a weighted mean of \((1-\eta^2)^h>15/16\) on \(|\eta|\le1/4\), so \(a>65/16384\).
- At \(y_1=17/25,\ y_2=41/50\), the original bump has \(b(y_1)-b(y_2)=(e^{175/72}-1)/(e^{175/72}+1)>5/6\). The exponent inequality follows from only 6 exact rational Taylor terms. Weighted Cauchy--Schwarz gives \(\int y^2 b'^2>697/252\), while \(\int b^2\le3/4\); integrating by parts proves \(K>1205/32256\).
- On \(\eta=0\) the frozen density \(\rho=\tau^{-1-h} b(256X-3)b(4\eta)\), \(X=r^2/(2\tau)\), has \(\int r^2\rho dr\,d\theta=2\pi\sqrt2\tau^{\beta_*+h}I_b\) with \(I_b=4096^{-1}\int_0^1\sqrt{3+y}b(y)dy\le3/8192\).
- Consequently ANY stress satisfying the prescribed source needs the physical magnitude \(M=\sup |S_{z\theta}|/\rho > 78325/(96768\sqrt2)\tau^{-h}>78325/145152\tau^{-h}\). This lower bound is valid for any spatially rotating orthogonal frame. The original full one-sided cone implies \(\|\widehat H\|_F\le1/\sqrt2\), and the baseline has \(\|R_0\|_\mathrm{op}=2/3\), so its physical tensor has \(M<3/2\). **Contradiction whenever \(\tau^h\le1/3\)**. For \(h=1/200\), this is \(1-t\le3^{-200}\approx3.76486\times10^{-96}\). The previous asymptotic exclusion is thus sharpened to an explicit rational finite-time threshold without any quadrature.

The preceding result is a NO-GO for a **frozen non-authentic singular diagnostic** already known to fail at the inner axis by another argument; it is NOT a no-go theorem for the analytic B.12 core.

## III. Subleading corrections are insufficient in a differentiated graph topology

If the frozen velocity components scale \(|U_z|,|U_\theta|\le H\tau^{-A}\), \(A=1/2+h\), on radius \(r\le R\sqrt\tau\) and axial width \(|z|\le Z\tau^D\), \(D=1/2-h\), and if a correction has \(|w_z|,|w_\theta|\le\epsilon\tau^{-A}\), \(|w_{\theta,t}|\le\epsilon\tau^{-A-1}\), \(|w_{\theta,z}|\le\epsilon\tau^{-A-D}\), then the exact azimuthal source functional \(\mathscr T=J(0,t)+\partial_t\int_{-\infty}^0L(z,t)dz-\nu L_z(0,t)\) changes by at most
\[
 \frac{2\pi R^3}{3}\,[2H\epsilon+\epsilon^2+Z\epsilon+\nu\epsilon\tau^{2h}]\,\tau^{\beta_*}.
\]
Hence \(\epsilon(\tau)\to0\) cannot cancel the frozen model's nonzero leading source coefficient. It remains possible to choose a different carrier, a noncompact halo, or a correction outside this graph norm.

## Independent computational audit

- **12,500 EXACT rational** test covectors verified the genuinely oriented sharp seven-ray support against its extreme-point formula, not a surrogate symmetric cap. Every exact vertex also satisfies \(\|\widehat H\|_F^2<1/2\).
- Pure Fraction checks of the sharper cutoff / Cauchy--Schwarz inequalities, including \(e^{175/72}>11\).
- 65-digit independent integration of the original calibrated frozen source recovered \(4\pi aK=0.00326293848566880522976987763832\), and its exact shell integral gave a diagnostic required normalized amplitude of \(1.0919426612825569\tau^{-h}\).
- Explicit smooth collar test \(v=\nabla\times(\varphi e_3)\) has \(\|v\|_2^2\approx0.003627285717582\); the obstruction works even for \(\epsilon=10^{-1000}\).
- Symbolic checks of all three graph similarity exponents; independent replay of the older regular positive-control model and Attack29 physical-radial calibration.

The full three-page scholarly PDF, LaTeX, exact independent checker, separate numeric replay, vector plot, SHA-256-verified ZIP and scientific scope record are available as conversation artifacts. The GitHub verifier is an additional compact *finite* regression, not a Lean proof of Navier--Stokes existence.

**Next authentic gate:** Freeze the genuine full preassigned \(\mathbb P\)-projected residual, smooth compact density and spatially varying frame. Evaluate vacuum-collar tests, original one-sided cone dual tests and the axisymmetric pressure-free toroidal flux jointly. Then, if no necessary test fails, attempt an actual source-first right inverse and a terminal graph-norm nonlinear correction with one periodic pressure. No complete singular residual, inverse or unforced theorem has been certified. Keep this PR DRAFT.