import Mathlib
/-! Finite arithmetic and real-field implications for the whole A.11
correction hull. The continuous source integral and PDE are not proved. -/
namespace TerminalCore2026
theorem a11_full_hull_coeff_cap :
    (11520 : ℚ)/(20:ℚ)^28 < 1/10000 ∧
    (1280 : ℚ)/(20:ℚ)^28 < 1/10000 := by
  constructor <;> norm_num

theorem a11_full_hull_rational_cap :
    (1 + 2*(1/2000 : ℚ)*(1+47/10) +
     2*(1/2 + (1/2000:ℚ) + (23/10)*(1/2000)) *
       (2*(1/10000:ℚ) + (1/10000:ℚ)^2) +
     (23/10)*(1+(1/10000:ℚ))*(1/10000)) <
    (101/100 : ℚ)*(1-(1/10000:ℚ)) := by norm_num

theorem a11_full_hull_ratio_gate (lam Eb delta B N : ℝ)
    (hlam : 0 < lam) (hEb0 : 0 ≤ Eb) (hEb : Eb ≤ lam/4)
    (hd0 : 0 ≤ delta) (hd1 : delta ≤ 1/10000)
    (hfield : |N| ≤ Eb*B/(1-delta))
    (hbudget : B ≤ (101/100)*(1-delta)) :
    |N| ≤ (101/400)*lam := by
  have hd : 0 < 1-delta := by linarith
  have hm : Eb*B ≤ Eb*((101/100)*(1-delta)) :=
    mul_le_mul_of_nonneg_left hbudget hEb0
  have hq : Eb*B/(1-delta) ≤ Eb*(101/100) := by
    apply (div_le_iff₀ hd).2
    nlinarith [hm]
  have hc : Eb*(101/100) ≤ (lam/4)*(101/100) :=
    mul_le_mul_of_nonneg_right hEb (by norm_num)
  nlinarith

theorem a11_full_hull_gap_slack (lam N : ℝ)
    (hN : |N| ≤ (101/400)*lam) :
    |N|+(99/400)*lam ≤ lam/2 := by linarith

#print axioms a11_full_hull_coeff_cap
#print axioms a11_full_hull_rational_cap
#print axioms a11_full_hull_ratio_gate
#print axioms a11_full_hull_gap_slack
end TerminalCore2026
