# Edition XXVI — global annular seven-ray quotient cone, necessary gauge cost, axial-support no-go

24 October 2026. **Exact source-independent tensor theorem; full unforced PDE and Lean proof not established.**

## Mathematical advance

Let Q(r,z) be any smooth symmetric co-rotating tensor on R²×S¹_z, radially compactly supported inside an annulus away from the axis. Let 0≤χ(r)≤1 be a smooth compact radial cutoff with χ=1 throughout the radial projection of supp Q. M=max_{i,j}||Q_ij||∞, A=16M+1, B=29A+64M+1=528M+30.

For the seven H8 ray directions with aperture 1/4, define:
\[
\begin{aligned}
d_1&=Q_{rr}-16(Q_{\theta\theta}+Q_{zz})+(B-29A)\chi,\\
d_2&=8Q_{\theta\theta}+6A\chi+2Q_{r\theta},\\
d_3&=8Q_{\theta\theta}+8A\chi-2Q_{r\theta},\\
d_4&=8Q_{zz}+7A\chi+2Q_{rz}-8Q_{\theta z},\\
d_5&=8Q_{zz}+7A\chi-2Q_{rz}+8Q_{\theta z},\\
d_6&=A\chi+8Q_{\theta z},\quad d_7=A\chi-8Q_{\theta z}.
\end{aligned}
\]
Direct exact tensor inversion proves **all seven coefficients d_j≥χ**, including radial cutoff collar, and
\[
S:=\sum_jd_jv_j\otimes v_j
=Q+A\chi I+B\chi e_r\otimes e_r.
\]
The added tensor has *exactly gradient* divergence:
\[
\nabla\cdot(S-Q)=\nabla\Phi,\quad
\Phi=(A+B)\chi+B\int_0^r\chi(s)/s\,ds.
\]
Thus P div S=P div Q exactly on R²×S¹_z or on a T³ with the annulus inside an embedded disk. This is a **global** coefficient-floor cone completion modulo the Leray pressure quotient for the specified geometry; no claim is made for a full spatially compact R³ shell.

The result even holds for any symmetric Q; no PSD assumption is needed. This is an algebraic/geometric positivity lemma rather than a new PDE theorem or original generic geometric-lemma principle.

## Necessary gauge cost

For any representation S=Q+AχI+Bχ e_r⊗e_r with d_j≥μχ, the ray aperture forces:
\[
B\chi\ge Q_{\theta\theta}-Q_{rr}+(105/16)\mu\chi.
\]
Large gauge amplitudes are **not** harmless for the source-stage coefficient magnitudes or q^{1/2} stress budget. Our explicit B=528M+30 can be vastly too large to satisfy authentic H8 quantitative constraints.

## Sharp axial-localization boundary

For a smooth pure radial carrier k(r,z)e_r⊗e_r with compact support in both radial and axial directions on R³, if its divergence is curl-free then k=0. Because
\[
(\nabla\times\nabla\cdot(k e_r\otimes e_r))_\theta
=\partial_z(k_r+k/r),
\]
compact z support makes k_r+k/r=0, and radial compact support implies k=0. Therefore simply multiplying the radial gauge by a compact axial cutoff does **not** preserve the pressure quotient; the full H8 whole-space shell needs a coupled additional tensor.

This resolves an overstrong reading of Edition XXV's pressure neutrality: it is genuinely global for periodic-axial geometry but **not** a free compact three-dimensional correction.

## Verification

An independently authored SymPy implementation gives six exact universal tensor identities; 10,000/10,000 independent exact rational arbitrary-symmetric reconstructions cover both source and cutoff regions and verify d_j≥χ. An independent Cartesian derivative test confirms the radial carrier-gradient identity, and symbolic axial-modulation tests exhibit a nonzero curl. The no-go itself is an analytic integration argument. A Lean 4 module states only the six finite algebraic identities and a necessary carrier budget; it awaits a successful kernel CI run, and does not formalize tensor differential calculus or the full PDE.

## Exact open gates

The repository source certificate remains FAIL_CLOSED_MISSING_SOURCE_DATA: real A.11/A.19 corrections and hashes, source interval bounds, physical pressure and collars, H8 small-stress and virtual-work dual, full all-harmonic inverse, nonzero smooth initial datum with **zero forcing**, singularity survival, and end-to-end Lean declaration are not proved. OpenAI's source theorem proves blow-up with smooth forcing for Navier–Stokes and unforced Euler; it is not the requested unforced Navier–Stokes theorem.

**Next mathematically decisive attack**: derive a support-compatible *two- or four-field* compensating gauge for the compact axial source shell (not pure radial alone), with explicit size and derivatives; simultaneously authenticate its source residual. On the torus, a cheaper carrier/pressure gauge satisfying the original H8 quantitative scale is the alternative route. Until then, local/global cone algebra alone is not evidence of an unforced singularity.

## Sharp whole-space affine virtual-work gate (independent third check)

For a compact smooth seven-ray stress S=sum d_j v_j⊗v_j on R³, d_j≥0, and compact Q with div(S-Q)=grad p, test against the divergence-free affine field psi=(x,y,-2z). Its diagonal strain in Cartesian coordinates is diag(1,1,-2), and its exact values on rays (1)–(7) are
\[
1,\ 17/16,\ 17/16,\ 7/8,\ 7/8,\ 15/16,\ 15/16.
\]
After integration by parts (normalizing p=0 outside the support), any compact whole-space realization requires
\[
\boxed{\int_{\mathbb R^3}(Q_{xx}+Q_{yy}-2Q_{zz})\,dx
\ge(7/8)\int_{\mathbb R^3}\sum_{j=1}^7d_j\,dx.}
\]
The 7/8 coefficient is sharp for this ray family. No *nonzero* compact seven-ray cone tensor with nonnegative coefficients can have gradient-only divergence on R³ if Q=0. This strengthens the earlier pure-radial no-go and instantiates the established H8 virtual-work dual with an explicit affine witness.

The periodic-axial global cone construction is not contradicted, because this affine psi is not a periodic axial test field. On a compact actual R³ source shell the inequality is an unavoidable global moment gate and may reject inadequate stress/source configurations before any all-harmonic PDE work. All seven ray strain factors are independently verified with exact Fraction arithmetic, and the new finite Lean scalar inequality is committed but GitHub kernel certification is queued.
