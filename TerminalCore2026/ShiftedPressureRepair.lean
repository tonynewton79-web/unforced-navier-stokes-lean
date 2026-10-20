import Mathlib

/-!
# Scalar certificates for one-jet-shifted pressure weights

These statements address the all-index polynomial and valuation
parts of the pressure-space repair of Zenodo 23474915.
The analytic function spaces, Cauchy estimates, full Navier--Stokes
recurrence and PDE reconstruction remain outside this Lean file.
-/
namespace TerminalCore2026

theorem shifted_pressure_three_jet_identity (a : ℝ) :
    8*(a+1)^4-(2*a+1)*(2*a+2)*(a+2)^2 =
      2*a^2*(a+1)*(2*a+3) := by
  ring

theorem shifted_pressure_three_jet_bound
    (a : ℝ) (ha : 0 ≤ a) :
    (2*a+1)*(2*a+2)*(a+2)^2 ≤ 8*(a+1)^4 := by
  have hp : 0 ≤ 2*a^2*(a+1)*(2*a+3) := by
    positivity
  have hi := shifted_pressure_three_jet_identity a
  linarith

theorem shifted_pressure_axial_factor
    (b : ℝ) (hb : 0 ≤ b) :
    (b+2)^2 ≤ (b+4)^2 := by
  nlinarith

theorem shifted_pressure_valutation
    (a n : ℝ) (ha : 0 ≤ a) (hn : 2 ≤ n) (h : n-2 ≤ a) :
    a+n+1 ≤ 3*(a+1) := by
  linarith

/-- The pressure-to-velocity shifted-index parameter is at most
one radial index in absolute value. -/
theorem shifted_pressure_parameter_gate
    (a n t : ℝ)
    (ha : 0 ≤ a) (hn : 1 ≤ n) (hindex : n-1 ≤ a)
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    -(a+1) ≤ t*(n-1)-(a+1) ∧
        t*(n-1)-(a+1) ≤ 0 := by
  have hnl : 0 ≤ n-1 := by linarith
  have hprod : 0 ≤ t*(n-1) := mul_nonneg ht0 hnl
  have hmul : t*(n-1) ≤ t*a :=
    mul_le_mul_of_nonneg_left hindex ht0
  have hta : t*a ≤ a := by
    have hnonneg : 0 ≤ a*(1-t) :=
      mul_nonneg ha (by linarith)
    nlinarith
  constructor <;> nlinarith

#print axioms shifted_pressure_three_jet_identity
#print axioms shifted_pressure_three_jet_bound
#print axioms shifted_pressure_axial_factor
#print axioms shifted_pressure_valutation
#print axioms shifted_pressure_parameter_gate

end TerminalCore2026
