import NavierStokes.ProblemStatement
import Mathlib.MeasureTheory.Integral.IntegrableOn
import Mathlib.MeasureTheory.Measure.Haar.InnerProductSpace

/-!
# The unforced periodic Navier--Stokes research target

This module fixes the physical semantics of the proposed construction.
It does **not** assert that any candidate exists. In particular, this is
separate from the upstream *forced*, zero-initial-data candidate statement.

We use the upstream viscosity-one residual, the unit-period lift from the
three-torus to Euclidean space, and positive interior times. Initial data
are permitted to be nonzero and must in fact be nonzero somewhere.
-/

noncomputable section

open Set
open scoped ContDiff

namespace UnforcedPatching

open NavierStokes.ProblemStatement

/-- One closed fundamental spatial cell for the unit three-torus. The
overlap of neighboring cells is confined to their boundaries. -/
def unitSpatialCell : Set Space :=
  {x | ∀ i : Fin 3, 0 ≤ x i ∧ x i ≤ 1}

/-- Canonical Lebesgue measure on the Euclidean lift, normalized by its
orthonormal-coordinate fundamental cell. We specify the measure explicitly
because the EuclideanSpace lift has no implicit MeasureSpace instance here. -/
def spatialLebesgue : MeasureTheory.Measure Space :=
  (EuclideanSpace.basisFun (Fin 3) ℝ).toBasis.addHaar

/-- There is nontrivial initial velocity; no forcing is available to create
it after time zero. -/
def InitialNonzero (u : VelocityField) : Prop :=
  ∃ x : Space, u (0, x) ≠ 0

/-- The squared speed is Lebesgue integrable on a fundamental cell at every
physical time. This is the precise finite-torus-energy requirement. -/
def FiniteCellEnergy (u : VelocityField) : Prop :=
  ∀ t ∈ Ico (0 : ℝ) 1,
    MeasureTheory.IntegrableOn (fun x : Space => ‖u (t, x)‖ ^ 2)
      unitSpatialCell spatialLebesgue

/-- Full physical obligations for an **unforced** periodic candidate.
Neither a witness nor a proof of its existence is introduced here. -/
structure UnforcedPeriodicCandidate (u : VelocityField)
    (p : PressureField) : Prop where
  velocity_smooth : ContDiffOn ℝ ∞ u preSingularDomain
  pressure_smooth : ContDiffOn ℝ ∞ p preSingularDomain
  velocity_periodic : UnitSpatialPeriodsOn (Ico 0 1) u
  pressure_periodic : UnitSpatialPeriodsOn (Ico 0 1) p
  initial_nonzero : InitialNonzero u
  finite_cell_energy : FiniteCellEnergy u
  divergence_free : ∀ t ∈ Ico (0 : ℝ) 1, ∀ x : Space,
    spatialDivergence u t x = 0
  navier_stokes_zero : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
    navierStokesResidual u p t x = 0
  speed_unbounded : SpeedUnboundedAtOne u

/-- **OPEN**: the proposed viscosity-one three-torus singularity statement.
Defining this proposition is not a proof of it. -/
def unforcedTargetStatement : Prop :=
  ∃ u : VelocityField, ∃ p : PressureField, UnforcedPeriodicCandidate u p

/-- A proposed unforced candidate cannot be a zero-initial-data candidate. -/
theorem candidate_initial_not_zero {u : VelocityField} {p : PressureField}
    (h : UnforcedPeriodicCandidate u p) :
    ¬ ∀ x : Space, u (0, x) = 0 := by
  intro hz
  obtain ⟨x, hx⟩ := h.initial_nonzero
  exact hx (hz x)

end UnforcedPatching
