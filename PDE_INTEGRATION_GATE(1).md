# PDE-Specific Lean Integration Gate

This file defines the release conditions required before this repository may describe the **full unforced periodic finite-time blow-up theorem** as Lean-verified.

## Frozen upstream dependency

The manuscript audits the OpenAI repository

`https://github.com/openai/NavierStokesAndEuler`

at frozen commit

`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

The manuscript identifies the relevant upstream modules as including:

- `ResidualCalculus.lean`
- `PhysicalResidualBridge.lean`
- `HarmonicMeanInteraction.lean`
- `CorrectionState.lean`
- `ValidDyadicBandCover.lean`
- `MixedDiagonalExtensions.lean`
- `ActualCurrentWaveSupport.lean`
- `R3PressureFourier.lean`
- `CandidateFromLimits.lean`
- `MixedCandidateAssembly.lean`
- `ComparatorSolution.lean`

## Current status

The abstract closure layer in `UnforcedClosure.lean` has already been kernel-checked successfully in the pinned Lean/Mathlib environment.

That result does **not** close the PDE-specific gate.

The full theorem remains on **HOLD** until the conditions below are discharged for the actual PDE spaces and operators.

## Required upgrade path

The full theorem gate is closed only when all of the following are true.

### 1. Frozen upstream import

The frozen upstream repository is imported at the stated commit, or as a cryptographically identified vendored dependency, in the same pinned Lean/Mathlib environment.

### 2. Appendix A hypothesis map

Every analytic hypothesis used in the manuscript is mapped one-by-one to either:

- a concrete upstream Lean declaration at the frozen commit, or
- a new local Lean theorem proved in this repository.

No manuscript hypothesis may remain as an untracked prose assumption in the final Lean theorem.

### 3. Core defect and release exponent

The core defect estimate and the exact release

`2/5 -> 3/10`

must be connected to the actual PDE objects rather than only to scalar abstractions.

### 4. Core source space and support/range preservation

The support-preserving Neumann inverse must be instantiated for the actual core source/operator spaces.

In addition, the full core/regular coupling mismatch must be proved to land in the domain on which the core right inverse is valid.

Schematically, if

`S_c` and `S_r`

split the source space and

`K_full`

is the full core/regular coupling term, the required range condition is

```text
K_full G_reg S_r(Y) ⊆ Y_c.
```

This is a genuine range/support statement and must not be replaced by a norm-smallness estimate alone.

### 5. Exact global right inverse

For the actual typed PDE operators, define

```text
G = G_c S_c + G_reg S_r - G_c K_full G_reg S_r
```

and prove

```text
L G = I.
```

The proof must explicitly use the core-range condition from Gate 4 so that

```text
L G_c K_full G_reg S_r
=
K_full G_reg S_r.
```

### 6. Correct periodic pressure reconstruction

The pressure reconstruction must be proved for the actual imported carrier and correction.

Unless the imported forcing has first been explicitly decomposed by the Leray projection and its gradient part absorbed into the carrier pressure, the correction pressure must satisfy the Poisson equation containing the force divergence:

```text
-Δπ
=
div F_*
+
∂_i ∂_j
(
  U_{*,i} v_j
  + v_i U_{*,j}
  + v_i v_j
).
```

The final proof must also establish the appropriate periodic compatibility / zero-mean normalization needed for inversion of the torus Laplacian.

### 7. Graph-norm bilinear estimate

The graph-norm bilinear estimate must be instantiated in the actual harmonic / finite-jet spaces used by the correction construction.

The proof must show that the one-derivative reserve is sufficient for every nonlinear term entering the fixed-point map.

### 8. Full contraction quantity

The contraction argument must use the full slab-dependent quantity

```text
Γ(T) = 4 M_G(T) C_B(T) η(T),
```

with

```text
η(T) = ||G(T) F_*||_X.
```

The release condition is

```text
Γ(T) < 1
```

for a sufficiently short late slab.

It is not enough to prove only

```text
η(T) -> 0
```

unless uniform bounds on `M_G(T)` and `C_B(T)` are separately established.

### 9. Banach completeness

The actual fixed-point space `X` must be proved complete, or explicitly defined as a Banach completion in which the PDE operators and nonlinear map are well-defined.

The Banach fixed-point theorem must then construct the correction rather than assume the existence of a fixed point.

### 10. Solenoidal condition and residual identity

The correction must be proved divergence-free in the actual PDE variables, and the pressure reconstruction must be connected to the unprojected Navier–Stokes residual so that the final velocity/pressure pair satisfies the **unforced** equation exactly.

### 11. Smoothness / regularity bootstrap

Starting from the fixed-point regularity class, prove the correction has the smoothness claimed in the manuscript on every compact subslab strictly before the singular time.

This may be achieved by an explicit parabolic regularity/bootstrap argument, but the upgrade must be a theorem rather than an informal assertion.

### 12. Blow-up inheritance

The asymptotically subleading correction estimate must be connected to the imported carrier coefficient so that the corrected solution retains the stated terminal singular behavior.

In particular, the proof must show that the correction does not cancel or alter the leading carrier blow-up coefficient.

### 13. Final theorem

A final theorem must compile with no:

- `sorry`,
- `admit`,
- unproved project-local axioms,
- opaque imported proposition already containing the desired target,
- unchecked external certificate,
- or equivalent escape hatch.

## Target theorem shape

A final repository release should expose a theorem semantically equivalent to:

```lean
-- schematic target only; exact names/types will follow the upstream repository
theorem unforced_finite_time_blowup_periodic :
  ∃ u p T,
    0 < T ∧
    PeriodicVelocity u ∧
    SmoothInitialData u ∧
    DivergenceFree u ∧
    NavierStokesUnforced ν u p ∧
    FiniteTimeBlowup u T := by
  ...
```

The blow-up conclusion must be proved downstream of the construction.

It must not appear as an assumption, axiom, or opaque imported statement that already contains the target theorem.

## Final release audit

Before changing the manuscript or repository wording to **“formally verified in Lean”**, record all of the following:

- Lean version;
- Mathlib commit;
- frozen upstream repository commit;
- final repository commit;
- CI workflow run identifier;
- exact final theorem name;
- `#print axioms` output for the final theorem;
- clean-checkout build instructions;
- independent clean-checkout CI replay;
- hashes of the source files used for the release.

## Permitted wording before this gate closes

The following wording is accurate:

> The abstract nonlinear closure layer has been kernel-checked in Lean in a pinned reproducible environment. The full PDE-specific unforced Navier–Stokes theorem remains subject to explicit analytic hypotheses and a separate Lean integration gate.

The following wording is **not** yet justified:

> The full unforced three-dimensional Navier–Stokes finite-time blow-up theorem has been formally verified in Lean.
