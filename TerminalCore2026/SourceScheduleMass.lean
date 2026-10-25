import Mathlib

/-!
# Scalar proof gates for the Appendix-A pressure schedule mass

These statements formalize only polynomial, rational and denominator
arithmetic. They do NOT formalize the full pressure integral, exterior
moment matching, or any unforced Navier--Stokes solution.
-/
namespace TerminalCore2026

theorem inner_and_early_stage_mass_identity (P q : ℝ) :
    (5*P^2 + P^2*(1-q))/2 = (3-q/2)*P^2 := by
  ring

theorem source_tail_decay_positive (h : ℝ) (hh : 0 < h) :
    0 < 1+2*h := by
  linarith

theorem source_axis_norm_rational_budget :
    (2704:ℚ)/9 < 301 ∧
    (64:ℕ)*301 = 19264 ∧
    (40:ℕ)*19264 = 770560 := by
  constructor
  · norm_num
  constructor <;> norm_num

theorem source_parameter_magnitude (T P : ℝ)
    (hP : Real.exp T < P) :
    0 < P := by
  have he := Real.exp_pos T
  linarith

theorem source_early_mass_dominates_inner (T : ℝ) (hT : 0 < T) :
    (5:ℝ)/2 < 3 - (Real.exp (-1-T))/2 := by
  have hp : 0 < Real.exp (-1-T) := Real.exp_pos _
  have he : Real.exp (-1-T) < 1 := by
    have hx : -1-T < 0 := by linarith
    have hv : Real.exp (-1-T) < Real.exp 0 :=
      Real.exp_lt_exp.mpr hx
    simpa using hv
  linarith

#print axioms inner_and_early_stage_mass_identity
#print axioms source_tail_decay_positive
#print axioms source_axis_norm_rational_budget
#print axioms source_parameter_magnitude
#print axioms source_early_mass_dominates_inner

end TerminalCore2026
