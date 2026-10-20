import Mathlib

/-!
# Scalar pressure-integration factors and two radial maps
Directly sourced from Newton, Exact Local Unforced Terminal-Core Dynamics
(Zenodo 23474915), eqs. (17),(18),(24),(26)--(28).

These identities do not prove an analytic operator norm estimate nor
the complete lower-order forcing recurrence.
-/
namespace TerminalCore2026

/-- The -2 X V_XX pressure path maps input radial exponent a
to a+1. -/
theorem laplacian_pressure_radial_factor (r : ℝ)
    (hr : r ≠ 0) (hr1 : r - 1 ≠ 0) :
    (-2*r*(r-1)) * (-1/(2*(r-1))) *
    (1/2) * (1/r^2) = 1/(2*r) := by
  field_simp
  ring

/-- The T_(0,n-1) V pressure path maps radial exponent a
to a+2, rather than a+1. -/
theorem time_pressure_radial_factor (r : ℝ)
    (hr : r ≠ 0) (hr1 : r+1 ≠ 0) :
    (-1/(2*r))*(1/2)*(1/(r+1)^2)*(1/r) =
      -1/(4*r^2*(r+1)^2) := by
  field_simp
  ring

theorem pressure_order_radial_index (a n : ℝ)
    (ha : n-1 ≤ a) : n ≤ a+1 := by linarith

theorem pressure_normalform_constants :
    13 * 89 = (1157 : ℕ) ∧ 13 * 8 * 89 = (9256 : ℕ) := by
  constructor <;> norm_num

#print axioms laplacian_pressure_radial_factor
#print axioms time_pressure_radial_factor
#print axioms pressure_order_radial_index
#print axioms pressure_normalform_constants

end TerminalCore2026
