import UnforcedPatching.NonlinearEnergyGate
import UnforcedPatching.Correction
import Mathlib.Tactic

/-!
# Attack 19: quantitative dyadic escape and physical source interface

The dyadic lemmas formalize the *rational last step* of the terminal
energy proof.  They do not assert or prove radial Poincare, the carrier's
Laplacian estimate, the Navier--Stokes energy identity, or the Version 17
stress-source identity.

The bridge below uses the physical NavierStokes.ProblemStatement residual.
Its physical source-match and regularity assumptions are explicit.
-/

namespace UnforcedPatching

open NavierStokes.ProblemStatement
open Set

/-- An explicit rational contradiction.  Uearly and Ulate denote the
carrier *squared* L2 energies at T-2tau and T-tau.  Eearly and Elate
denote the total squared energies.  A correction of L2 norm <= 1/16 of
the carrier gives the 15/16,17/16 energy bounds below. -/
theorem dyadic_close_energy_contradiction
    (Uearly Ulate Eearly Elate : ℝ)
    (hU : 0 < Uearly)
    (hCarrier : (3 / 4 : ℝ) * Uearly < Ulate)
    (hLower : ((15 / 16 : ℝ) ^ 2) * Ulate ≤ Elate)
    (hUpper : Eearly ≤ ((17 / 16 : ℝ) ^ 2) * Uearly)
    (hDissipation : 2 * Elate ≤ Eearly) : False := by
  nlinarith

/-- A radial Poincare lower bound and two uniform comparison bounds give
the required dissipative differential inequality.  The hypothesis
`hRadial` is the physical analytic input still requiring formalization. -/
theorem radial_energy_transfer_scalar
    (tau Ugrad2 Uenergy Vgrad2 Venergy : ℝ)
    (htau : 0 ≤ tau) (hUenergy : 0 ≤ Uenergy)
    (hRadial : Uenergy ≤ tau * Ugrad2)
    (hGrad : ((15 / 16 : ℝ) ^ 2) * Ugrad2 ≤ Vgrad2)
    (hNorm : Venergy ≤ ((17 / 16 : ℝ) ^ 2) * Uenergy) :
    Venergy ≤ 2 * tau * Vgrad2 := by
  have hscaled :
      tau * (((15 / 16 : ℝ) ^ 2) * Ugrad2) ≤ tau * Vgrad2 :=
    mul_le_mul_of_nonneg_left hGrad htau
  nlinarith

/-- A finite Laplacian constant gives a strictly positive, explicit
relative-norm exclusion radius.  The inequalities are scalar, not a
formalization of the carrier Laplacian on the torus. -/
theorem quantitative_radius_bounds
    (C delta : ℝ)
    (hC : 0 ≤ C) (hdelta : 0 ≤ delta)
    (hsmall : 16 * (1 + C) * delta ≤ 1) :
    delta ≤ (1 / 16 : ℝ) ∧ C * delta ≤ (1 / 16 : ℝ) := by
  constructor <;> nlinarith [mul_nonneg hC hdelta]

/-- A fully typed physical *assumption* that Version 17's stress
divergence equals the complete viscosity-one Navier--Stokes residual.
No theorem here constructs or certifies Sigma17. -/
def PhysicalSourceMatched
    (U : VelocityField) (p : PressureField)
    (stressDivergence : VelocityField) : Prop :=
  ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
    navierStokesResidual U p t x = stressDivergence (t, x)

/-- Physical source-match plus an actual nonlinear correction equation
would produce zero full residual.  Existence and singularity retention are
distinct, and neither is deduced. -/
theorem physical_source_and_correction_imply_unforced_residual
    (U w stressDivergence : VelocityField)
    (p pi : PressureField)
    (hsource : PhysicalSourceMatched U p stressDivergence)
    (hregU : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      ResidualRegularAt U p t x)
    (hregW : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      ResidualRegularAt w pi t x)
    (hcorrection : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      navierStokesResidual w pi t x +
        spatialDerivative U t x (w (t, x)) +
        spatialDerivative w t x (U (t, x)) =
        -stressDivergence (t, x)) :
    ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      navierStokesResidual (U + w) (p + pi) t x = 0 := by
  intro t ht x
  apply physicalCorrection_closes U w p pi t x (hregU t ht x) (hregW t ht x)
  unfold PhysicalCorrectionEquation
  rw [hcorrection t ht x, ← hsource t ht x]

#print axioms dyadic_close_energy_contradiction
#print axioms radial_energy_transfer_scalar
#print axioms quantitative_radius_bounds
#print axioms physical_source_and_correction_imply_unforced_residual

end UnforcedPatching
