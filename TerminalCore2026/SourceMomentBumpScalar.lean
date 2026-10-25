import Mathlib
/-! Finite scalar gates for the true Appendix-A smooth-step-derivative
bump and exact source moment transport. These do NOT formalize the
integrals, source schedule, or Navier--Stokes physical equations. -/
namespace TerminalCore2026
theorem source_bump_L2_exceeds_plateau : (27/5:ℚ)>5 := by norm_num
theorem source_bump_rational_upper : (0:ℚ)<640/3 := by norm_num
theorem source_bump_remainder_budget :
    (8:ℚ)*(640/3)*20*(1/100000000000)*
      ((57605/2000)*(4/10000000))^2
       < 5/100000000000000000 := by norm_num
theorem source_bump_derivative_budget :
    (16:ℚ)*(640/3)*20*(1/100000000000)*
      ((57605/2000)*(4/10000000))*((55/2)*(4/10000000))
       < 1/10000000000000000 := by norm_num
theorem reference_MJS_scalar_factors :
    (4:ℚ)*(5/8)=5/2 ∧ (1/2:ℚ)*(5/6)=5/12 := by
  constructor <;> norm_num
theorem terminal_energy_scalar_factor (h:ℝ) (hh:h≠0):
    (1/2:ℝ)/(2*h)=1/(4*h) := by field_simp; ring
theorem pulse_end_energy_exponent : (2:ℚ)*13=26 := by norm_num
#print axioms source_bump_L2_exceeds_plateau
#print axioms source_bump_remainder_budget
#print axioms source_bump_derivative_budget
#print axioms terminal_energy_scalar_factor
end TerminalCore2026