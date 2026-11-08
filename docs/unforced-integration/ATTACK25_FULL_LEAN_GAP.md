# Attack 25 — the full Lean theorem is blocked by mathematics, not syntax

Date: 2026-11-08. Target: **unforced** smooth three-dimensional
periodic Navier–Stokes finite-time speed blow-up.

## Status of the theorem

`UnforcedPatching.unforcedTargetStatement` remains **OPEN**.
No theorem constructed in Attack 25 proves this proposition without
hypotheses. In particular, `target_of_constructed_correction` is
**conditional**: its proof uses an actually constructed correction
satisfying the complete physical equation, regularity, periodicity,
energy, divergence, nonzero initial datum, and pointwise terminal
retention. None of those assumptions is licensed merely by the
finite Fourier-algebra certificate.

The upstream `openai/NavierStokesAndEuler` repository provides a Lean
formalization for a **forced** Navier–Stokes breakdown scenario. Removing
that force while maintaining finite-time blow-up is a different
mathematical problem; the upstream forced theorem is not an axiom or
proof of this unforced target.

## Exact target
An actual candidate must give explicit `U,w,p,π`, with
`u=U+w`, satisfying on the unit torus and for every `0<t<T`
the physical correction PDE
`
  w_t - νΔw + P div(U⊗w+w⊗U+w⊗w) = -Rν(U),
  Rν(U) = U_t - νΔU + P div(U⊗U).
`
No nonzero forcing may remain. Pressure needs torus Poisson
compatibility and reconstruction. For the actual physical solution
`u,p+π`, prove:
1. smoothness on each compact subinterval before `T`;
2. periodicity, solenoidality, nonzero smooth initial datum;
3. finite cell energy and exact energy/dissipation identity;
4. a proven quantitative coupling `U⊗w+w⊗U` including the
   frozen carrier's true Fourier coefficients and all generated
   mediator generations;
5. a rigorous terminal trace lower bound for `U+w`;
6. the final Lean existence witness using upstream physical PDE
   types with no new axioms or proof holes.

**Critical quantitative obstruction.** Under the conditional
full-solution estimates `E(T-τ) ≤ C τ^(1/5)` and
`||u(T-τ)||∞ ≥ c τ^(-3/5)`,
`N_eff(T-τ) ≥ (c²/C)τ^(-7/5)` where
`N_eff=(Σ ||û_k||)²/(Σ||û_k||²)`.
Thus a fixed finite support such as 20+108 cannot be an exact
terminal mechanism under these assumptions; for smooth solutions
infinite support is permitted, and the bound is a nontrivial
effective spectral participation constraint.

## Lean coverage

- `Attack25ConditionalTarget.lean`: actual physical endpoint,
  with fully exposed hypotheses, using existing
  `physicalCorrection_closes` and
  `speedUnbounded_add_subleading`.
- `Attack25FiniteSpectrumGate.lean`: fixed finite support,
  uniform energy, and carrier-coupling norm gate;
  exact `2π` viscous receiver threshold.
- `Attack25SpectralPopulation.lean`: finite
  Cauchy--Schwarz population inequality and exact exponent `7/5`.
- `Attack25` GitHub CI must **compile** these on frozen
  Lean 4.34.0-rc2, Mathlib and imported upstream dependencies.
  Currently the attempted hosted run failed **before typechecking**
  at the pinned Lean download with HTTP 504; code has not yet
  been kernel certified.

## Full-release rule

Never label the finite support inequality, a conditional target
theorem or a completed GitHub workflow as a proof of unforced
Navier–Stokes blow-up. The final theorem must be a closed
construction with all premises discharged, and its
`#print axioms` dependency list independently audited.

The immediate mathematical target is to find a controlled
infinite-dimensional, dynamically generated transfer process that
meets the effective-population lower bound, the viscous energy
identity, the exact carrier-coupling PDE and terminal non-cancellation
simultaneously. If that is impossible for the frozen carrier,
prove a carrier-specific obstruction instead.
