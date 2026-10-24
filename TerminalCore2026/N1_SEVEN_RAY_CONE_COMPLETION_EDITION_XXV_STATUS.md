# Edition XXV — exact seven-ray completion, necessary carrier, and carrier curl

24 October 2026. **Mathematical status: source-independent exact pointwise tensor theorem. Full unforced Navier–Stokes and complete Lean proof OPEN.**

This continues the same cumulative Editions I–XXIV, using the seven-ray H8 architecture rather than introducing a separate Navier–Stokes paper.

## Exact H8 ray geometry

In an adapted local orthonormal frame \(e_1=e_r,e_2=e_\theta,e_3=e_z\), fix aperture \(t=1/4\) and
\[
v_1=e_1,\quad v_{2,3}=e_1\pm t e_2,\quad
v_{4,5}=e_1\pm t e_3,\quad v_{6,7}=e_1+t(e_2\pm e_3).
\]
The six-component symmetric-tensor synthesis map has rank 6, with the one-dimensional coefficient kernel
\((2,-2,0,-1,-1,1,1)\). This matches the previously retained H8 seven-ray system.

For coefficients \(d_j\ge\mu>0\), its stress \(S=\sum_jd_jv_j\otimes v_j\) satisfies
\[
S_{rr}-S_{\theta\theta}\ge (15/16)\sum_jd_j\ge105\mu/16.
\]
The Edition XXIV manufactured two-harmonic field has, on its annular plateau,
\(Q_{rr}-Q_{\theta\theta}=-2\lambda^2r^4\cos^2z\le0\).
Hence \(Q+\pi I\) cannot **directly** belong to this strict cone. An isotropic pressure gauge does not change the diagonal difference.

## Constructive exact *carrier-augmented* cone representation

Let \(3/4\le r\le5/4\), \(|z|\le\pi/6\), \(|\lambda|\le1/16\); put \(s=\sin z,c=\cos z\).
For the actual manufactured two-frequency *kinematic covariance*
\[
Q=2\begin{pmatrix}
c^2 &\lambda r^2c^2&0\\
\lambda r^2c^2&c^2(1+\lambda^2r^4)&-\lambda rcs\\
0&-\lambda rcs&1+\lambda^2r^2s^2
\end{pmatrix},
\]
set
\[
\begin{aligned}
d_1&=1,&d_2&=1+4\lambda r^2c^2,&d_3&=3-4\lambda r^2c^2,\\
d_4&=2+16s^2+16\lambda^2(r^2s^2-r^4c^2)+16\lambda rcs,\\
d_5&=2+16s^2+16\lambda^2(r^2s^2-r^4c^2)-16\lambda rcs,\\
d_6&=1-16\lambda rcs,&d_7&=1+16\lambda rcs,\\
\pi&=3/8-2c^2(1+\lambda^2r^4),\\
K&=85/8+32s^2+32\lambda^2r^2s^2-30\lambda^2r^4c^2.
\end{aligned}
\]
Then the exact identity holds in all six symmetric tensor components:
\[
\boxed{Q+K\,e_r\otimes e_r+\pi I=\sum_{j=1}^7d_jv_j\otimes v_j}.
\]
Analytic interval inequalities give \(d_1=1,\ d_2\ge39/64,\ d_3\ge167/64,\ d_{4,5}\ge5007/4096,\ d_{6,7}\ge3/8\), and \(K>0\). Thus \(\min_jd_j\ge3/8\) on the entire stated patch.

## Physical obstruction: the radial carrier is not free

For the spatially varying carrier \(K(r,z)e_r\otimes e_r\), cylindrical divergence gives
\[
\nabla\cdot(K e_r\otimes e_r)=(K_r+K/r)e_r
\]
and its azimuthal curl is
\[
\boxed{[\nabla\times\nabla\cdot(K e_r\otimes e_r)]_\theta
=(64/r+192\lambda^2r+300\lambda^2r^3)\sin z\cos z}.
\]
This is generally nonzero and **cannot be eliminated by pressure**. Spatial derivatives of the co-rotating ray frame are additional real PDE terms. Without a physical source/corrector supplying this carrier, the pointwise cone completion says nothing about zero forcing.

## Verification and honest theorem boundary

- Independent SymPy reconstruction: all six tensor entries match identically.
- Exact seven-ray tensor map: rank 6, kernel \((2,-2,0,-1,-1,1,1)\).
- Second independent 5,000/5,000 rational parameter replays: tensor equality and \(d_j\ge3/8\).
- Independent curl differentiation and pressure-only negative control pass.
- A finite scalar Lean module checks polynomial components and rational bounds; await pinned CI before claiming kernel success.

The original OpenAI Navier–Stokes theorem and its Lean formalization allow smooth forcing; unforced Euler is separate. The source-authentication ledger still reports **FAIL_CLOSED_MISSING_SOURCE_DATA** for A.11/A.19 matching, all collars, complete physical unforced PDE and end-to-end Lean theorem. No actual H8 source-specific four-field/virtual-work dual test, flow evolution, higher-harmonic convergence, physical singularity or full Lean result is proved.

**Next decisive target:** freeze the real source's projected radial and angular residual and solve the non-gradient carrier compensation together with the seven-ray source tensor and H8 virtual-work dual in one true physical coordinate system. Exact coefficient positivity alone is not enough.