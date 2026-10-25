import Mathlib

/-! Conditional scalar certification for A.11 moving-endpoint plateau roots.
No physical source-derivative or full unforced PDE proof is asserted. -/
namespace TerminalCore2026

theorem a11_small_jacobian_jet
    (d cp q : ℝ)
    (hcp : 0 ≤ cp)
    (hsmall : (3 / 2 : ℝ) * q ≤ 1 / 4)
    (hlinear : cp ≤ (3 / 2 : ℝ) * d + (3 / 2 : ℝ) * q * cp) :
    cp ≤ 2 * d := by
  have hmul : ((3 / 2 : ℝ) * q) * cp ≤ (1 / 4 : ℝ) * cp :=
    mul_le_mul_of_nonneg_right hsmall hcp
  nlinarith

theorem a11_preplateau_deviation
    (r R : ℝ)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 20 / 17)
    (hR0 : 1 ≤ R) (hR1 : R ≤ 20 / 19) :
    |r - R| ≤ 20 / 19 := by
  apply abs_le.mpr
  constructor <;> linarith

theorem a11_transport_jet_bracket
    (M V : ℝ)
    (hM : M ≤ 1 / 4)
    (hV : V ≤ 1 / 8) :
    M + (20 / 19 : ℝ) * V ≤ 29 / 76 := by
  linarith

theorem a11_coefficient_release
    (L delta cn : ℝ)
    (hL : 0 ≤ L)
    (hdelta : delta ≤ (105 / 19 : ℝ) * L)
    (hroot : cn ≤ 3 * delta) :
    cn ≤ (315 / 19 : ℝ) * L := by
  linarith

theorem a11_angular_jet_release
    (L T deltaPrime cnPrime : ℝ)
    (hL : 0 ≤ L)
    (hT : T ≤ 1 / 4)
    (hdelta : deltaPrime ≤ (609 / 76 : ℝ) * L * T)
    (hroot : cnPrime ≤ 2 * deltaPrime) :
    cnPrime ≤ (609 / 152 : ℝ) * L := by
  have hproduct : L * T ≤ L / 4 :=
    mul_le_mul_of_nonneg_left hT hL
  nlinarith [hproduct]

theorem a11_new_thresholds :
    (315 / 19 : ℚ) < 17 ∧ (609 / 152 : ℚ) < 5 ∧
    (184320 : ℚ) / (20 ^ 28) < 1 / 4 := by
  constructor
  · norm_num
  constructor
  · norm_num
  · norm_num

#print axioms a11_small_jacobian_jet
#print axioms a11_preplateau_deviation
#print axioms a11_transport_jet_bracket
#print axioms a11_coefficient_release
#print axioms a11_angular_jet_release
#print axioms a11_new_thresholds
end TerminalCore2026
