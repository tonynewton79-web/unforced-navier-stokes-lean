import Mathlib

/-!
# Finite scalar proof gates for the complete leading-profile pressure normal form

The source expansion has 27 normal-form terms at eta orders 0,1,2,3.
These Lean theorems verify the scalar bounds on the shifted radial indices
and highest-jet coefficient. The entire Banach space and imported physical
leading profiles are not yet formalized. DOI: 10.5281/zenodo.23474915.
-/
namespace TerminalCore2026

theorem full_leading_pressure_parameter_gate
    (r m k lam D : ℝ)
    (hk : 0 ≤ k) (hr : k+1 ≤ r) (hm : r ≤ m)
    (hlam0 : 0 ≤ lam) (hlam : lam ≤ k/50)
    (hD0 : 0 ≤ D) (hD1 : D ≤ 1) :
    0 ≤ r-D-lam ∧
    r-D-lam ≤ m+k+1 ∧
    lam-r ≤ 0 ∧
    -(m+k+1) ≤ lam-r ∧
    lam-1-m ≤ 0 ∧
    -(m+k+1) ≤ lam-1-m := by
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  · linarith

theorem full_leading_pressure_radial_multiplier
    (r c : ℝ) (hr : 1 ≤ r) (hc : 0 ≤ c) :
    r+c ≤ (1+c)*r := by
  have hp : 0 ≤ c*(r-1) :=
    mul_nonneg hc (by linarith)
  nlinarith [hp]

theorem full_leading_pressure_third_jet
    (r m N u G : ℝ) (hr : r ≠ 0) (hm : m ≠ 0)
    (hN : N ≠ 0) :
    -(G*(-u*G^2))/(4*r*m*N^2) = u*G^3/(4*r*m*N^2) := by
  ring

/-- Quadratic-pressure inverse denominator dominates two radial
lifts of the second input, uniformly in the first radial index. -/
theorem quadratic_pressure_highest_jet_denominator
    (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    (b+1)*(b+2)^2 ≤ (a+b+1)*(a+b+2)^2 := by
  have h1 : b+1 ≤ a+b+1 := by linarith
  have hprod : 0 ≤ a*(2*b+4) :=
    mul_nonneg ha (by linarith)
  have h2 : (b+2)^2 ≤ (a+b+2)^2 := by
    nlinarith [sq_nonneg a, hprod]
  calc
    (b+1)*(b+2)^2 ≤ (a+b+1)*(b+2)^2 :=
      mul_le_mul_of_nonneg_right h1 (sq_nonneg _)
    _ ≤ (a+b+1)*(a+b+2)^2 :=
      mul_le_mul_of_nonneg_left h2 (by linarith)

#print axioms quadratic_pressure_highest_jet_denominator

#print axioms full_leading_pressure_parameter_gate
#print axioms full_leading_pressure_radial_multiplier
#print axioms full_leading_pressure_third_jet

end TerminalCore2026
