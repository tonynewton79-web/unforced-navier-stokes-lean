import Mathlib

/-!
Attack102 exact algebra and finite-sum identities. NOT an unforced
Navier–Stokes PDE/continuum source certification or blow-up proof.
-/
namespace UnforcedPatching.Attack102

theorem source_quadratic_centered (U m R Rc E : ℝ) :
    U - (m/4)*R^2 + E =
    (U + (m/4)*Rc^2) - (m*Rc/2)*R
      - (m/4)*(R-Rc)^2 + E := by
  ring

theorem fourth_moment_centered (R Rc : ℝ) :
    R^4 - 2*Rc*R^3 + Rc^2*R^2 = R^2*(R-Rc)^2 := by
  ring

theorem torque_identity_pointwise (U m R E : ℝ) :
    R^2*(U - m*R^2/4 + E) =
    U*R^2 - (m/4)*R^4 + R^2*E := by
  ring

theorem torque_neutrality_implies_fourth_moment
    (m M4 E2 : ℝ) (h : (0:ℝ) = -(m/4)*M4 + E2) :
    (m/4)*M4 = E2 := by
  linarith

theorem finite_weighted_torque_identity
    (n : ℕ) (w R tau E : Fin n → ℝ) (U m : ℝ) :
    (∑ i, w i * (R i)^2 * (U - (m/4)*(R i)^2 + E i) * tau i) =
      U * (∑ i, w i * (R i)^2 * tau i)
      - (m/4) * (∑ i, w i * (R i)^4 * tau i)
      + (∑ i, w i * (R i)^2 * E i * tau i) := by
  calc
    _ = ∑ i, (U * (w i * (R i)^2 * tau i)
             - (m/4) * (w i * (R i)^4 * tau i)
             + (w i * (R i)^2 * E i * tau i)) := by
      apply Finset.sum_congr rfl
      intro i hi
      ring
    _ = _ := by
      simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.mul_sum]
      ring

theorem shell_left_rational : (239:ℚ)^2 / 240^2 < 120/121 := by
  norm_num

theorem shell_right_rational : (122:ℚ)/121 < (241/240)^2 := by
  norm_num

theorem shell_quadratic_bound : (1:ℚ)/(2*240^2) = 1/115200 := by
  norm_num

theorem atomic_second_moment_zero :
    (5:ℚ)*1^2 - 2*2^2 + (1/3)*3^2 = 0 := by
  norm_num

theorem atomic_fourth_moment_zero :
    (5:ℚ)*1^4 - 2*2^4 + (1/3)*3^4 = 0 := by
  norm_num

theorem atomic_third_moment_nonzero :
    (5:ℚ)*1^3 - 2*2^3 + (1/3)*3^3 = -2 := by
  norm_num

theorem coordinate_pullback_counterexample :
    (1:ℚ)/10*(4*(19/10)^2-(2:ℚ)^2) = 261/250 := by
  norm_num

#print axioms source_quadratic_centered
#print axioms fourth_moment_centered
#print axioms torque_identity_pointwise
#print axioms torque_neutrality_implies_fourth_moment
#print axioms finite_weighted_torque_identity
#print axioms shell_left_rational
#print axioms shell_right_rational
#print axioms shell_quadratic_bound
#print axioms atomic_second_moment_zero
#print axioms atomic_fourth_moment_zero
#print axioms atomic_third_moment_nonzero
#print axioms coordinate_pullback_counterexample

end UnforcedPatching.Attack102
