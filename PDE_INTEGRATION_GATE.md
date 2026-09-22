# PDE-Specific Lean Integration Gate

This file defines the release conditions required before the repository may describe the **full unforced periodic finite-time blow-up theorem** as Lean verified.

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

## Required upgrade path

The full theorem gate is closed only when all of the following are true:

1. The frozen upstream repository is imported at the stated commit or as a cryptographically identified vendored dependency.
2. The manuscript's Appendix A hypotheses are mapped one-by-one to concrete upstream or newly proved Lean declarations.
3. The core defect estimate and the `2/5 -> 3/10` release are connected to the actual PDE objects, not only scalar abstractions.
4. The support-preserving Neumann inverse is instantiated for the actual core source/operator spaces.
5. The core/regular right-inverse identity `L G = I` is proved for the typed PDE operators, including the full coupling map.
6. The graph-norm bilinear estimate is instantiated for the actual harmonic/finite-jet spaces used in the construction.
7. The contraction theorem constructs the PDE correction rather than assuming a fixed point.
8. The solenoidal condition and periodic pressure reconstruction are connected to the constructed correction.
9. The asymptotic subleading bound is connected to the imported carrier coefficient, yielding the stated terminal singular behavior.
10. A final theorem compiles with no `sorry`, `admit`, unproved project-local axioms, or equivalent escape hatches.

## Target theorem shape

A final repository release should expose a theorem semantically equivalent to:

```lean
-- schematic target only; names/types will follow the upstream repository
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

The blow-up conclusion must be proved downstream of the construction; it must not appear as an assumption, axiom, opaque imported proposition that already contains the target, or unchecked external certificate.

## Final release audit

Before changing the manuscript to “formally verified in Lean”, record:

- Lean and Mathlib versions;
- upstream repository commit;
- final repository commit;
- CI run identifier;
- `#print axioms` output for the final theorem;
- an independent build from a clean checkout;
- hashes of the source files used for the release.
