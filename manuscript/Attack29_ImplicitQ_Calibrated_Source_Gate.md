# Attack 29 — exact implicit-q slice flux and torque-calibrated diagnostic

Date: 8 November 2026. **Research scope: explicit frozen singular-seed diagnostic of Appendix A.5 of the 167-page integrated manuscript, not the normally convergent unforced local core.** No unforced finite-time singularity is claimed.

## General authentic-core decision functional

In the actual implicit chart
```
tau = q(1-eta^2), z = q^D eta,
D=1/2-h, alpha=3/2-2h, beta=1/2-2h,
d=1-eta^2, ell=1-2h eta^2,
```
suppose the compact azimuthal moments scale as `L=q^(1-h) ℒ(eta)` and `J=q^beta 𝒥(eta)`. Set

`ℋ(eta) = ∫_{−eta0}^eta ℒ(s) ell(s)/d(s)^(alpha+1) ds`.

Exact physical-coordinate differentiation yields

`q^(−beta)[J+∂_t∫_{−∞}^z L] = 𝒥(eta)−d(eta)^beta[alpha ℋ(eta)−D eta d(eta) ℋ'(eta)/ell(eta)]`.

A bounded-coefficient H8 baseline+correction with toroidal capacity `O(q^(beta+h))` requires this leading functional to vanish on every slice. It also requires total leading angular momentum `ℋ(eta0)=0`. This is a necessary functional condition, not sufficient for the full vector stress or nonlinear PDE correction.

## Exactly specified frozen A.38 seed

Use the paper's `h=1/200`, flat bump `b`, `f(X)=b(64X)`, `g(eta)=b(4eta)`, `chi=f*g`, `Psi=q^D X(1+4eta)chi`, `U_theta=r q^(−1−h)chi`, and the corresponding meridional velocity defined by the streamfunction. The complete pressure is the periodic Poisson pressure; its azimuthal slice integral vanishes.

Direct substitution proves
- `U_z=q^(−1/2−h)(1+4eta)g(f+X f')`.
- `J=0` on every slice by `∫ X f(f+X f')dX = [(Xf)^2]/2=0`.
- `L=4π C1 q^(1−h)g`, where `C1=∫Xf dX>0`.
- The original normalized centre flux is exactly `−4π C1 (3/2−2h)H_half<0`, numerically approximately `−0.00024952458487183328` at `h=1/200`.

## Global torque-neutral calibration, still no H8

Define `U^c=U+curl(c(t)chi e_z)`, which modifies only the azimuthal shell velocity and is identically solenoidal. Let

`C0=∫f dX=3/256`,
`H_all=∫_(−1/4)^(1/4) g(s)ell(s)/d(s)^(alpha+1) ds`,
`G_all=∫_(−1/4)^(1/4) g(s)ell(s)/d(s)^(D+2) ds`,
`a=C1 H_all/(C0 G_all)>0`, `c(t)=−a tau^(−h)`.

Then **total angular momentum vanishes identically for all preterminal times**: `∫L^c(z,t)dz=0`. By symmetry the half-slice temporal derivative and the centre viscous derivative vanish as well. The new nonlinear flux satisfies exactly

`tau^(−beta)J^c(0,t)=4π a K>0`,

where `K=∫Xf'(f+Xf')dX>1/128`. The strict inequality follows from
`64K=∫_(1/2)^1 y² b'(y)²dy−(1/2)∫_0^1 b(y)²dy>1/2` by Cauchy–Schwarz and `0≤b≤1`.

At the paper's h, the coefficient is approximately **0.0032629384856688052298**. This is checked by exact symbolic manipulations and independent high-precision direct physical-radial quadrature.

The paper's original shell envelope `rho=tau^(−1−h) b(256X−3)g(eta)` has toroidal capacity `O(tau^(1/2−h))`; the calibrated centre flux is `4πaK tau^(1/2−2h)`. Since h>0, **no uniformly normalized H8 seven-ray correction** with the paper's fixed baseline can match the modified source for all small tau. For the actual original paper's sign convention, source matching is `P div(S)=−P F`; this changes the required flux's sign, not its nonzero size. Recompute the Poisson pressure from the modified velocity before any full source comparison.

**Important limitation:** Appendix A.5's singular seed already fails a separate interior-axis residual condition (its Proposition A.16). The new calibrated torque obstruction is logically independent but does not apply to the separate normally convergent genuinely unforced local-core hierarchy without re-authenticating its radial/axial profiles, cutoff, scalar/vector-potential gauge, pressure and frame.

## Publication and verification

The conversation contains the four-page complete LaTeX proof note, an **181-page cumulative PDF** obtained by preserving all 177 earlier pages, an exact symbolic/55-digit numerical replay, an independent physical-radial flux integral, and fixed-physical-z off-axis time-derivative cross-checks.

No Lean module in this PR proves the PDE angular-momentum identity, its infinite-dimensional stress obstruction, or the final unforced singularity theorem. Any small Lean scalar arithmetic checks are auxiliary only.
