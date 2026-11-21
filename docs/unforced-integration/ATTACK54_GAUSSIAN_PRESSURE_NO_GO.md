# Attack 54 — Nonlinear pressure compatibility and Gaussian-mode impossibility

**21 November 2026.** An actual-PDE exclusion theorem for the unforced backward Leray equation. No nonzero singular profile has been produced; the present analytical results are NOT a solution of the Millennium problem. The original paper and independent exact symbolic regression were created in the associated research session.

## Exact PDE

For smooth W: ℝ×ℝ³→ℝ³ and unrestricted C² pressure q, viscosity 1,

    ∂sW + ½(W+y·∇W) − ΔW + (W·∇)W + ∇q = 0,     div W=0.

These are the full equations; neither nonlinear convection nor pressure is omitted.

## Theorem 54.1 — Finite fixed-width Gaussian exclusion

Suppose

    W(s,y) = Σ_{j=1}^m exp(−λ_j|y|²) P_j(s,y),

where the distinct λ_j>0 are constants and each vector-valued P_j is polynomial in y with a uniform finite degree bound and C¹ time-dependent coefficients. If (W,q) solves the full PDE for some pressure q, then W=0. This needs no s-periodicity or pressure-decay hypothesis.

**Proof.** Distinct Gaussian exponentials with polynomial coefficients are linearly independent: multiply by the slowest inverse Gaussian and restrict to y=tω, t→∞. Incompressibility therefore implies separately for each j

    div P_j−2λ_j y·P_j=0.                                      (D)

Writing f_j=exp(−λ_j|y|²), the linear similarity-diffusion part is f_j A_j, where

    A_j=∂sP_j + (½+6λ_j)P_j +(½+4λ_j)y·∇P_j
          −ΔP_j−(λ_j+4λ_j²)|y|²P_j.                          (L)

The **real quadratic nonlinearity** is

    (W·∇)W =
      Σ_{i,j} exp[−(λ_i+λ_j)|y|²]
          [ (P_i·∇)P_j−2λ_j(y·P_i)P_j ].                     (N)

Take curl to eliminate the unrestricted scalar pressure. The smallest exponential rate is λ_min, and all quadratic rates are at least 2λ_min>λ_min. Exponential-polynomial independence therefore forces for the slowest component

    curl A_min−2λ_min y×A_min=0.                               (C)

Let d be the **uniform** degree bound and P_d(s,y) its homogeneous top component. The degree d+1 term of (D) gives y·P_d=0. The degree d+3 term of (C) is

    2λ_min(λ_min+4λ_min²)|y|² y×P_d =0.

Because λ_min>0, y×P_d=0 as well, hence P_d=0. This holds for every s, so the corresponding time derivative vanishes too. Descend in degree, then remove the slowest Gaussian and induct in m. QED.

**Crucial scope:** a finite Gaussian approximation can be the starting point of a validated *infinite-dimensional* Newton/fixed-point correction. The theorem only forbids the uncorrected finite ansatz being exact. Time-varying λ_j(s) are excluded from the hypothesis.

## Theorem 54.2 — Meridional flow is compulsory

Any smooth axisymmetric profile decaying along the axis and solving the full PDE with W_r=0 must be zero. Incompressibility yields ∂z W_z=0, hence W_z=0 by axial decay. The axial momentum equation yields ∂z q=0; radial momentum gives ∂r q = W_theta²/r. Thus W_theta² is z-independent, and the axial decay implies W_theta=0. The full pressure equation, rather than its gauge or an arbitrary forcing, produces the obstruction.

## Proposition 54.3 — Three-point exact curl certificate

Set f=exp(−x²−y²−z²) and

    S=f(−y,x,0),
    P=f(4xz,4yz,4(1−x²−y²)),
    W(s,x,y,z)=a(s)S+b(s)P.

Both S and P are globally smooth, solenoidal, and rapidly decreasing. Let

    F=∂sW+½(W+y·∇W)−ΔW+(W·∇)W.

The θ-component of curl F at y=0, cylindrical radius r>0, z=0 is **exactly**

    (curl F)_θ(s,r,0) =
      2r exp(−r²)[20 b r⁴−(132b+4b')r²+155b+10b'].

Any scalar pressure must satisfy curl grad q=0. Evaluation at (r,z)=(1,0) and (2,0) gives

    43 b+6 b'=0,  53 b+6 b'=0

and thus b=b'=0 at each s. At (1,1), the remaining curl component is

    (curl F)_θ(s,1,1)=4 exp(−4) a(s)²,

so a=0. Thus no choice of time-dependent amplitudes or pressure makes this two-mode family an exact nonzero solution.

**Full pressure determined:** for such a rapidly decreasing W its unique decaying pressure, modulo a time-dependent constant, solves

    −Δ q = Σ_{i,j}∂i∂j(W_i W_j),
    q= [1/(4π|·|)] * Σ_{i,j}∂i∂j(W_i W_j).

It exactly makes the residual divergence-free, but cannot cancel these nonzero curls.

## Nonzero full-PDE positive controls — deliberately outside the theorem

1. Exact stationary backward Leray with nonlinear pressure: W(y)=(y_1,−y_2,0), q(y)=−y_1². Direct substitution gives full PDE=0, div=0, but W grows linearly, the physical velocity has infinite kinetic energy and no decaying certificate exists.
2. The classical forward Lamb–Oseen vortex has v_theta(t,r)=(1−exp(−r²/(4t)))/r, v_r=v_z=0, and pressure p(t,r)=−∫_r^∞ v_theta(t,ρ)²/ρ dρ. This exactly solves the unforced PDE for t>0 but is forward in time and z-invariant, hence not the needed three-dimensional finite-energy singularity.

An independent SymPy verifier performs the complete 3D Cartesian PDE calculations, repeats the vorticity residual in independent cylindrical coordinates, checks all three exact pressure-free witnesses, and verifies both positive controls.

## Release gates

- **PASSED mathematical derivations:** finite-Gaussian impossibility via exponential separation; meridional necessity; three-point exact vorticity obstruction.
- **PASSED computational audit:** independent cylindrical/Cartesian symbolic checks, affine full-pressure Leray positive control, forward Oseen PDE control.
- **NOT PASSED:** actual nonzero decaying twisted-periodic profile; numerical self-similar certificate; proof of all 15 external cell conditions; nonlinear correction existence; Lean physical PDE formalization; independent referee verification and originality.
- **CI status:** the new workflow verifies symbolic calculations only. Do not describe it as Lean or a complete PDE certificate.

### Prior art boundary

Classical stationary backward self-similar L³ nonexistence: Nečas–Růžička–Šverák (Acta Math. 176, 1996) and Tsai (Arch. Rational Mech. Anal. 143, 1998). The 20 November 2026 Alpöge–Buckmaster conditional Lean package (https://github.com/tristanbuckmaster/navier-stokes) requires separate certificate data not present in the checked public repository. This note makes **no priority or novelty claim** without full literature and expert audit.
