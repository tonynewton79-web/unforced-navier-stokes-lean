import Mathlib

/-!
Edition XXIX: energy-budget algebra and normed-space reverse triangle
for a necessary zero-force startup condition. This is NOT a Lean
formalization of the Navier-Stokes PDE energy identity, Leray
projection, or a finite-time singularity.
-/
namespace TerminalCore2026

theorem source_startup_budget
    (background initialCost residualCost terminalCorrection complete : ℝ)
    (hFlow : complete ≤ initialCost + residualCost)
    (hTriangle : background ≤ complete + terminalCorrection) :
    background ≤ initialCost + residualCost + terminalCorrection := by
  linarith

theorem zero_data_zero_residual_gate
    (energy dissipation : ℝ)
    (henergy : 0 ≤ energy) (hdiss : 0 ≤ dissipation)
    (hidentity : energy + dissipation = 0) :
    energy = 0 ∧ dissipation = 0 := by
  constructor <;> linarith

theorem nonzero_target_requires_budget
    (background initialCost residualCost terminalCorrection : ℝ)
    (hbudget : background ≤ initialCost + residualCost + terminalCorrection)
    (hbackground : 0 < background) :
    0 < initialCost + residualCost + terminalCorrection := by
  linarith

/-- Reverse triangle inequality for arbitrary normed additive groups,
the functional-analytic part of the source-to-correction bound. -/
theorem normed_background_reverse_triangle
    {E : Type*} [NormedAddCommGroup E] (background correction : E) :
    ‖background‖ ≤ ‖background + correction‖ + ‖correction‖ := by
  have h : (background + correction) + (-correction) = background := by
    abel
  calc
    ‖background‖ = ‖(background + correction) + (-correction)‖ := by rw [h]
    _ ≤ ‖background + correction‖ + ‖-correction‖ := norm_add_le _ _
    _ = ‖background + correction‖ + ‖correction‖ := by simp

#print axioms source_startup_budget
#print axioms zero_data_zero_residual_gate
#print axioms nonzero_target_requires_budget
#print axioms normed_background_reverse_triangle
end TerminalCore2026
