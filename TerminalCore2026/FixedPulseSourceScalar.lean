import Mathlib
/-! Scalar checks for the A.5 fixed pulse. The analytic source
enclosure theorem, full stress cone and PDE are NOT formalized here. -/
namespace TerminalCore2026
theorem source_fixed_pulse_plateau (x : ℝ) (h : 1 ≤ x) :
    (99/100:ℝ) ≤ x-1/100 := by linarith
theorem source_fixed_pulse_positive_guard :
    (0:ℚ)<1/2^120 := by norm_num
theorem source_fixed_pulse_step_midpoint :
    (1:ℚ)/50*50=1 := by norm_num
theorem source_fixed_pulse_cutoff :
    (11:ℚ)-10=1 := by norm_num
theorem source_fixed_pulse_plateau_low :
    (1:ℚ)-1/100=99/100 := by norm_num
#print axioms source_fixed_pulse_plateau
#print axioms source_fixed_pulse_positive_guard
#print axioms source_fixed_pulse_step_midpoint
end TerminalCore2026
