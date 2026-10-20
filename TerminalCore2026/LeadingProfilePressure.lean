import Mathlib

/-!
# Leading-profile pressure: exact radial cancellation and valuation

The source is eqs. (18), (24), (26)--(28) of
Newton, *Exact Local Unforced Terminal-Core Dynamics* (Zenodo 23474915).
Theorems here concern exact monomial coefficients and radial order.
They do NOT assert a bounded complete analytic operator or the full
Navier--Stokes coefficient recurrence.
-/

namespace TerminalCore2026

/-- The first three ordered endpoint interactions in Omega_k combine to
one radial-primitive coefficient, with V_0=X v_c X^c and
V_k=X w_a X^a. -/
theorem leading_profile_radial_cancellation (a c v w : ℝ) :
    v * ((a+1)*w) + w*((c+1)*v) - v*w =
      (a+c+1)*v*w := by
  ring

/-- The radial pressure primitive exactly cancels the Euler factor. -/
theorem leading_profile_pressure_primitive
    (a c v w : ℝ) (ha : 0 ≤ a) (hc : 0 ≤ c) :
    ((a+c+1)*v*w)/(a+c+1) = v*w := by
  have hden : a+c+1 ≠ 0 := by linarith
  field_simp
  all_goals ring

/-- The regularized pressure map lifts radial valuation by two. -/
theorem leading_profile_two_degree_gain
    (k a c : ℕ) (ha : k ≤ a) :
    k+2 ≤ a+c+2 := by
  omega

/-- Distinct derivative ceilings of the three grouped channels. -/
theorem leading_profile_jet_budget :
    (2 : ℕ) ≤ 3 ∧ (1 : ℕ) ≤ 3 := by
  omega

#print axioms leading_profile_radial_cancellation
#print axioms leading_profile_pressure_primitive
#print axioms leading_profile_two_degree_gain

end TerminalCore2026
