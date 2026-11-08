import Mathlib

/-!
# Attack 31: exact algebraic numerator bound for the model delayed pressure channel

This file proves the rational polynomial inequality behind the bound
54 * R^2 / varrho^4 for the model operator J_1 ∂η^4 P_2.

The analytic function-space norm theorem, all variable coefficients and
the full Navier--Stokes PDE are NOT formalized here. No singularity
existence theorem is claimed or assumed.
-/

namespace UnforcedPatching

theorem attack31_fourth_radial_slack (j : ℝ) (hj : 0 ≤ j) :
    4 * (j + 3)^2 * (2*j + 1) * (2*j + 3)
      ≤ 54 * (j + 1)^3 * (j + 2) := by
  have hpoly : 0 ≤ 19*j^3 + 71*j^2 + 69*j + 9 := by positivity
  have h2j : 0 ≤ 2*j := by positivity
  have hslack :
      0 ≤ 2*j*(19*j^3 + 71*j^2 + 69*j + 9) :=
    mul_nonneg h2j hpoly
  calc
    4 * (j + 3)^2 * (2*j + 1) * (2*j + 3)
        ≤ 4 * (j + 3)^2 * (2*j + 1) * (2*j + 3)
          + 2*j*(19*j^3 + 71*j^2 + 69*j + 9) :=
          le_add_of_nonneg_right hslack
    _ = 54 * (j + 1)^3 * (j + 2) := by ring

theorem attack31_fourth_beta_slack (β : ℝ) (hb : 0 ≤ β) :
    (β + 1)^2 ≤ (β + 5)^2 := by
  nlinarith

theorem attack31_fourth_ratio_numerator
    (j β : ℝ) (hj : 0 ≤ j) (hb : 0 ≤ β) :
    4 * (j + 3)^2 * (2*j + 1) * (2*j + 3) * (β + 1)^2
      ≤ 54 * (j + 1)^3 * (j + 2) * (β + 5)^2 := by
  have hrad := attack31_fourth_radial_slack j hj
  have hbeta := attack31_fourth_beta_slack β hb
  have hbase : 0 ≤ 54 * (j + 1)^3 * (j + 2) := by positivity
  calc
    4 * (j + 3)^2 * (2*j + 1) * (2*j + 3) * (β + 1)^2
        ≤ 54 * (j + 1)^3 * (j + 2) * (β + 1)^2 :=
          mul_le_mul_of_nonneg_right hrad (sq_nonneg (β + 1))
    _ ≤ 54 * (j + 1)^3 * (j + 2) * (β + 5)^2 :=
          mul_le_mul_of_nonneg_left hbeta hbase

#print axioms attack31_fourth_radial_slack
#print axioms attack31_fourth_beta_slack
#print axioms attack31_fourth_ratio_numerator

end UnforcedPatching
