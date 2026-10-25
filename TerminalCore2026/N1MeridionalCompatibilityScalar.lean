import Mathlib

/-!
Edition IX: scalar consequences of cylindrical swirl compatibility.
NOT an end-to-end Lean proof of the unforced Navier--Stokes PDE.
-/
namespace TerminalCore2026

theorem swirl_radial_residual_factor (U W r : ℝ) :
    -(((U + W)^2 - U^2) / r) = -(2 * U * W + W^2) / r := by
  ring

theorem swirl_meridional_residual_difference (U W r : ℝ) :
    -((U + W)^2) / r - (-U^2 / r) =
      -(2 * U * W + W^2) / r := by
  ring

theorem frozen_meridional_small_swirl_no_go
    (U W : ℝ) (hU : 0 < U)
    (hsmall : |W| < 2 * U)
    (hcompat : 2 * U * W + W^2 = 0) : W = 0 := by
  have hfactor : W * (2 * U + W) = 0 := by
    nlinarith [hcompat]
  rcases mul_eq_zero.mp hfactor with hw | hw
  · exact hw
  · have hbound : -2 * U < W := (abs_lt.mp hsmall).1
    have hpos : 0 < 2 * U + W := by linarith
    exfalso
    linarith

theorem linear_swirl_force_nonzero
    (U W : ℝ) (hU : U ≠ 0) (hW : W ≠ 0) :
    2 * U * W ≠ 0 := by
  exact mul_ne_zero (mul_ne_zero (by norm_num) hU) hW

theorem shear_decay_amplitude_identity (A decay : ℝ) :
    (A * decay - A) + A = A * decay := by
  ring

#print axioms swirl_radial_residual_factor
#print axioms swirl_meridional_residual_difference
#print axioms frozen_meridional_small_swirl_no_go
#print axioms linear_swirl_force_nonzero
#print axioms shear_decay_amplitude_identity
end TerminalCore2026
