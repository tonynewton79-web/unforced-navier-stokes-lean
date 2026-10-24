import Mathlib

/-!
# Scalar A.11 support stress margins, *not* a full unforced NS proof

Full source integral, moment-constrained coefficient existence, analytic
profile and PDE reconstruction are tracked separately in the dependency
ledger. These lemmas formalize arithmetic only.
-/
namespace TerminalCore2026

theorem a11_energy_rational :
    (83/20:ℚ) + 1/2 + (2/3)*(1/100)^7 < 47/10 := by norm_num
theorem a11_stress_factor :
    (47/10:ℚ)*(51/25) = 2397/250 := by norm_num
theorem a11_support_final_margin :
    (2397/250:ℚ)/20 < 1/2 := by norm_num
theorem a11_coeff_bump_half :
    (640/3:ℚ)*(3/1280) = 1/2 := by norm_num
theorem a11_coeff_slope :
    (2:ℚ)*(2000000/9)*(9/8000000) = 1/2 := by norm_num
theorem a11_coeff_eta :
    (2:ℚ)*(640/3)*(3/10240) = 1/8 := by norm_num
theorem a11_source_margin :
    (1/2:ℚ)-1/8-1/16 = 5/16 := by norm_num
theorem a11_cone_gap :
    (9/8:ℚ)-12*(1/20)=21/40 := by norm_num
theorem a11_min_radius :
    (35/4:ℚ)>4*(2+3/20) := by norm_num

theorem a11_scalar_stress_finish (lam E N:ℝ)
    (hlam:0<lam) (hE:E≤lam/20)
    (hN:|N|≤E*(2397/250)) : |N|<lam/2 := by
  have hp:(0:ℝ)≤2397/250 := by norm_num
  have hmul:=mul_le_mul_of_nonneg_right hE hp
  nlinarith

#print axioms a11_support_final_margin
#print axioms a11_cone_gap
#print axioms a11_scalar_stress_finish

end TerminalCore2026