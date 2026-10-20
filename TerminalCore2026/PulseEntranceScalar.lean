import Mathlib
/-! Finite scalar gates only. The stagewise analytic comparisons and
source-admissibility selection are not formalized in this file. -/
namespace TerminalCore2026
theorem pulse_first_moment_margin :
    (40:ℚ)/1000000 + 8/90 < 9/100 := by norm_num
theorem pulse_first_energy_margin :
    (11:ℚ)/12 + 320/10000 < 1 := by norm_num
theorem pulse_rate_margin :
    (120:ℚ)*(1/1000000)*(17/11) < 1/5000 := by norm_num
theorem pulse_forward_energy_margin :
    ((1:ℚ)/1000000)*(5000/4999)*(9/16)*(15/11)
      + 1/(4*4999) < 1/10000 := by norm_num
theorem pulse_backward_energy_margin :
    ((1:ℚ)/1000000)/2+15*(1/1000000)*(17/11)
      + ((3:ℚ)/4+1/(3*100^7))*(1/1000000)/11
      < 1/40000 := by norm_num
theorem pulse_true_A19_value_margin :
    (1:ℚ)/10000+1/40000+5/10^17 < 1/2500 := by norm_num
#print axioms pulse_first_moment_margin
#print axioms pulse_forward_energy_margin
#print axioms pulse_backward_energy_margin
#print axioms pulse_true_A19_value_margin
end TerminalCore2026
