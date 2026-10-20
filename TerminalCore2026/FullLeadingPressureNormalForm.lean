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

#print axioms full_leading_pressure_parameter_gate
#print axioms full_leading_pressure_radial_multiplier
#print axioms full_leading_pressure_third_jet

end TerminalCore2026
