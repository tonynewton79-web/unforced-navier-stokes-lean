import Mathlib

/-!
Edition XI: abstract finite scalar implications of a pressure-free annular
witness. This is NOT a Lean formalization of the cylindrical field,
the continuum integral, the Leray projection or unforced NSE.
-/
namespace TerminalCore2026

theorem collar_positive_dual_mass
    (sourceLower mass : ℝ)
    (hsource : 0 < sourceLower)
    (hmass : 0 < mass) :
    0 < sourceLower * mass := by
  exact mul_pos hsource hmass

theorem pressure_gradient_cannot_cancel_witness
    (signal pressurePair : ℝ)
    (hs : 0 < signal)
    (hp : pressurePair = 0) :
    signal + pressurePair ≠ 0 := by
  rw [hp]
  simpa using (ne_of_gt hs)

theorem positive_projected_dual_lower
    (signal h1Norm projectedNorm : ℝ)
    (hs : 0 < signal)
    (hh1 : 0 < h1Norm)
    (hbound : signal ≤ projectedNorm * h1Norm) :
    0 < projectedNorm := by
  by_contra h
  have hnp : projectedNorm ≤ 0 := le_of_not_gt h
  have hmul : projectedNorm * h1Norm ≤ 0 :=
    mul_nonpos_of_nonpos_of_nonneg hnp (le_of_lt hh1)
  linarith

theorem positive_budget_is_necessary
    (signal time diffusion convection nonlinear : ℝ)
    (hsignal : 0 < signal)
    (hbudget : signal ≤ time + diffusion + convection + nonlinear) :
    0 < time + diffusion + convection + nonlinear := by
  linarith

theorem finite_test_point_cannot_be_pressure_only
    (residual pTheta : ℝ)
    (hresidual : 0 < residual)
    (hpressure : pTheta = 0) :
    residual + pTheta ≠ 0 := by
  rw [hpressure]
  simpa using (ne_of_gt hresidual)

#print axioms collar_positive_dual_mass
#print axioms pressure_gradient_cannot_cancel_witness
#print axioms positive_projected_dual_lower
#print axioms positive_budget_is_necessary
#print axioms finite_test_point_cannot_be_pressure_only
end TerminalCore2026
