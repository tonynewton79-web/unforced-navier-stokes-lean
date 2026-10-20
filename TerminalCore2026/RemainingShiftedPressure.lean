import Mathlib

/-!
# Exact scalar gates for the remaining shifted-pressure primitives

Source: the unforced terminal-core coefficient identities in Zenodo 23474915.
These elementary lemmas DO NOT claim the Banach-space multiplication
theorem, the complete coupled recurrence, or a Navier--Stokes solution.
-/
namespace TerminalCore2026

/-- Integration by parts in the five leading-profile pressure terms:
the Euler derivative on W cancels the pressure primitive. -/
theorem leading_pressure_radial_ibp (a c lam : ℝ)
    (hden : a+c+1 ≠ 0) :
    (lam-1-a)/(a+c+1) =
      -1+(lam+c)/(a+c+1) := by
  field_simp
  ring

/-- The ordered quadratic transport factor is at most one.
The expansion shift is bounded by the other input's radial valuation. -/
theorem quadratic_pressure_transport_gate
    (a b lam : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hlam0 : 0 ≤ lam) (hlam : lam ≤ b) :
    0 ≤ a+lam ∧ a+lam ≤ a+b+1 := by
  constructor <;> linarith

/-- Two radial averages compensate one radial pressure lift. -/
theorem quadratic_pressure_double_average
    (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    a+b+1 ≤ (a+1)*(b+1) := by
  nlinarith [mul_nonneg ha hb]

/-- The product of two positive-radial inputs stays positive-radial. -/
theorem quadratic_pressure_valuation
    (i j a b : ℕ) (hai : i ≤ a) (hbj : j ≤ b) :
    i+j+1 ≤ a+b+1 := by
  omega

/-- The leading-profile pressure primitive gains one radial degree. -/
theorem leading_pressure_valuation (k a c : ℕ)
    (hk : k ≤ a) :
    k+1 ≤ a+c+1 := by omega

#print axioms leading_pressure_radial_ibp
#print axioms quadratic_pressure_transport_gate
#print axioms quadratic_pressure_double_average
#print axioms quadratic_pressure_valuation
#print axioms leading_pressure_valuation

end TerminalCore2026
