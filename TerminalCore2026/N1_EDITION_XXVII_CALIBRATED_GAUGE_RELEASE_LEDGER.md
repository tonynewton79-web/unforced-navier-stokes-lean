# Edition XXVII — sharper universal seven-ray gauge and the authentic-source gate

24 October 2026. **Exact pressure-quotient algebra: PASS on the stated geometry. Full unforced 3D NSE singularity and its Lean proof: OPEN.**

The previous global annular construction used large gauge amplitudes A_old=16M+1 and B_old=528M+30. This attack optimizes a simple source-independent inverse of the **same exact seven H8 rays** (aperture 1/4), while allowing an arbitrary strict coefficient floor μχ. Set
\[
a=\frac38\mu+\frac{13}{4}M,\quad
b=\frac{85}{8}\mu+\frac{471}{4}M,\quad
h=\mu+8M.
\]
For a smooth compact-annular, θ-independent co-rotating symmetric tensor Q with |Q_ij|≤M, choose χ smooth radial 0≤χ≤1, equal to one throughout its radial support. The seven coefficients are
\[
\begin{aligned}
d_1&=Q_{rr}-16(Q_{\theta\theta}+Q_{zz})+(\mu+33M)\chi,\\
d_2&=8Q_{\theta\theta}+2Q_{r\theta}+(\mu+10M)\chi,\\
d_3&=8Q_{\theta\theta}-2Q_{r\theta}+(3\mu+26M)\chi,\\
d_4&=8Q_{zz}+2Q_{rz}-8Q_{\theta z}+(2\mu+18M)\chi,\\
d_5&=8Q_{zz}-2Q_{rz}+8Q_{\theta z}+(2\mu+18M)\chi,\\
d_6&=8Q_{\theta z}+(\mu+8M)\chi,\quad
d_7=-8Q_{\theta z}+(\mu+8M)\chi.
\end{aligned}
\]
Exactly d_j≥μχ, and the seven-ray synthesis S obeys
\[
\boxed{S=Q+a\chi I+b\chi e_r\otimes e_r,\quad
\mathbb P\operatorname{div}S=\mathbb P\operatorname{div}Q}.
\]
The equality is globally valid for the periodic-axial cylinder R²×S¹ or an annular disk embedded in T³, not for arbitrary axially compact R³ shells.

**Quantitative gain:** b has M coefficient 471/4=117.75 versus 528 (4.48-fold improvement). The entrywise stress bound is
\[
\boxed{\|S\|_{L^\infty,\text{entry}}\le122M+11\mu.}
\]
For μ=κM, it becomes (122+11κ)M. If an externally proved physical source-stress budget allowed \(\|S\|\le\Lambda\), this construction would provide the sufficient numerical condition \(M\le\Lambda/(122+11\kappa)\). **Neither Λ nor source M is yet authenticated.**

**Sharpness without overclaiming:** For Q=0 and χ=1, every positive-ray representation of an isotropic plus radial carrier with each d_j≥μ needs b≥85μ/8. Equality holds for (μ,μ,3μ,2μ,2μ,μ,μ). A separate fixed-source-independent-splitting LP gives b≥85μ/8+471M/4 within that particular fixed-a,b,h inverse; the global optimization over all source-dependent inverses is NOT established.

## Independently replayed evidence

1. A first SymPy symbolic reconstruction checked all six tensor equations, and a 20,000/20,000 seeded Fraction box test checked all coefficient floors.
2. An independently parameterized scipy/HiGHS LP at μ=M=1 gave (a,h,b)=(29/8,9,1027/8), and a different seven-variable LP independently gave sharp zero-source b=85/8.
3. A second 25,000-case exact rational tensor reconstruction plus 1,000 radial collar cases and an adversarial undershoot control are in the committed reproducibility scripts.
4. A finite Lean module has all six polynomial tensor components, individual coefficient-floor inequalities, the sharp source-free scalar cost, and a fixed-inverse minimax statement. It uses no admitted declarations; it is **NOT kernel-confirmed until CI completes**, and it does not represent a Lean PDE proof.

## Mandatory fail-closed checks

The authentic A.11/A.19 source/profile hash, all piecewise collars and derivative bounds, residual force, pressure matching, H8 seven-ray small-norm/virtual-work feasibility, time-dependent multi-harmonic correction, actual zero-force NSE identity, blow-up preservation, and end-to-end Lean proof remain null/unproved in FULL_UNFORCED_SOURCE_CERTIFICATE_REQUIRED_20261022.json. The upstream OpenAI Navier–Stokes theorem is forced; the OpenAI unforced blow-up theorem is for Euler. The constructed radial pressure gauge changes no projected forcing, and therefore **cannot by itself turn a forced velocity field into an unforced one**.

**Next genuine milestone:** provide the source-authenticated projected forcing and one simultaneous space–time estimate of its compatible stress amplitude M versus the actual H8 budget Λ; then solve or refute the compact-source virtual-work and nonlinear all-mode gates, not merely repeat abstract cone inversions.