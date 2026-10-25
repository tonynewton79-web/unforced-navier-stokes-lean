import Mathlib

/-!
# Finite coefficient algebra behind the ordered quadratic pressure sum

Source: equation (28), doi:10.5281/zenodo.23474915.
The full Banach-space estimate for the U_i Z_(0,j) V_j remainder
is NOT proved or formalized here.
-/
namespace TerminalCore2026

/-- After pairing (i,j) with (j,i), the V-V source has one Euler
factor on the product. -/
theorem quadratic_pressure_pair_cancellation
    (ai aj wi wj : ℝ) :
    wi*((aj+1)*wj) + wj*((ai+1)*wi) - wi*wj =
      (ai+aj+1)*wi*wj := by
  ring

/-- Radial total derivative cancels with the pressure primitive. -/
theorem quadratic_pressure_primitive_coefficient
    (t q : ℝ) (ht : 0 < t) :
    (t*q)/(4*t) = q/4 := by
  have hne : t ≠ 0 := ne_of_gt ht
  field_simp
  all_goals ring

/-- Quadratic radial valuation plus pressure and regular-singular lifts. -/
theorem quadratic_pressure_valuation (i j k : ℕ)
    (h : i+j = k) : i+j+2 = k+2 := by
  omega

#print axioms quadratic_pressure_pair_cancellation
#print axioms quadratic_pressure_primitive_coefficient
#print axioms quadratic_pressure_valuation

end TerminalCore2026
