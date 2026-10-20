import Mathlib

/-! Exact conditional real-algebra gates for the original forced-source
A.11 stress cone (4.22). This file does NOT prove actual source enclosures,
the complete Appendix-A cone, or any unforced Navier--Stokes PDE theorem. -/
namespace TerminalCore2026

theorem a11_normalized_cone_margin
    (a r w : ℝ)
    (ha : 2 ≤ a) (ha_upper : a ≤ 43/20)
    (hr_lower : 0 ≤ r) (hr_upper : r ≤ 1/2)
    (hw_lower : -1 ≤ w) (hw_upper : w ≤ 1) :
    7/20 ≤ 2*(1-r)^2 - (a-2)*w^2 := by
  have hd : 0 ≤ a-2 := by linarith
  have hdmax : a-2 ≤ 3/20 := by linarith
  have hnn : 0 ≤ (1-w)*(1+w) := mul_nonneg (by linarith) (by linarith)
  have hw : w^2 ≤ 1 := by nlinarith [hnn]
  have ht : (a-2)*w^2 ≤ 3/20 := by
    calc
      (a-2)*w^2 ≤ (a-2)*1 := mul_le_mul_of_nonneg_left hw hd
      _ ≤ 3/20 := by linarith
  have hrp : 0 ≤ (1/2-r)*(3/2-r) :=
    mul_nonneg (by linarith) (by linarith)
  have hrm : 1/4 ≤ (1-r)^2 := by nlinarith [hrp]
  nlinarith

theorem a11_cone_gap_factor (a p w : ℝ) (hp : p ≠ 0) :
    2*(p-a)^2-(a-2)*(p*w)^2 =
    p^2*(2*(1-a/p)^2-(a-2)*w^2) := by
  field_simp
  ring

theorem a11_shear_from_slope (ell lam : ℝ)
    (hl : -(3*lam)/2 ≤ ell) (hu : ell ≤ -lam/2) :
    2+lam ≤ 2-2*ell ∧ 2-2*ell ≤ 2+3*lam := by
  constructor <;> linarith

theorem a11_slope_alone_not_sufficient :
    ¬ ((21/10-2:ℝ)*(100*10)^2 < 2*(100-21/10)^2) := by
  norm_num

theorem a11_Q_initial_propagation :
    (80:ℚ)+3*(20/17)*76800000 < 300000000 := by norm_num
theorem a11_Q_eta_propagation :
    (5:ℚ)+3*(20/17)*5000000 < 20000000 := by norm_num
theorem a11_Q_eta_denominator :
    (20:ℚ)/17*5120+20000000 < 21000000 := by norm_num
theorem a11_Q_total_error :
    (300000000:ℚ)+(1/2)*21000000 < 320000000 := by norm_num
theorem a11_Q_small_parameter :
    (320000000:ℚ)*(1/20)^27 < 49/100 := by norm_num

#print axioms a11_normalized_cone_margin
#print axioms a11_cone_gap_factor
#print axioms a11_shear_from_slope
#print axioms a11_Q_small_parameter
end TerminalCore2026
