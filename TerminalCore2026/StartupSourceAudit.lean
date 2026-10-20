import Mathlib

/-!
# Exact low-order source-index and coordinate-algebra gates

From the formal Navier--Stokes hierarchy (5.2)--(5.6) in the
OpenAI Finite Time Blowup for Navier--Stokes paper. These are
only finite combinatorial and scalar source gates, not a
certification of the leading profile or an unforced solution.
-/
namespace TerminalCore2026

theorem first_order_source_pairs (i j : ℕ) (h : i+j=1) :
    (i=0 ∧ j=1) ∨ (i=1 ∧ j=0) := by omega

theorem second_order_source_pairs (i j : ℕ) (h : i+j=2) :
    (i=0 ∧ j=2) ∨ (i=1 ∧ j=1) ∨ (i=2 ∧ j=0) := by omega

theorem no_interior_first_order_pair (i j : ℕ)
    (hi : 1 ≤ i) (hj : 1 ≤ j) : i+j ≠ 1 := by omega

theorem unique_positive_pair_at_second_order (i j : ℕ)
    (hi : 1 ≤ i) (hj : 1 ≤ j) (h : i+j=2) :
    i=1 ∧ j=1 := by omega

theorem known_pressure_omega_order (n : ℕ) (hn : 1 ≤ n) :
    n-1 < n := by omega

theorem known_delayed_order (n : ℕ) (hn : 2 ≤ n) :
    n-2 < n := by omega

/-- The algebraic factor in the eta derivative at fixed time. -/
theorem eta_physical_chain_identity (h eta : ℝ) :
    (1-2*h*eta^2) - (1-2*h)*eta^2 = 1-eta^2 := by ring

theorem coordinate_jacobian_positive
    (h eta : ℝ) (hh : 0 < h) (hmax : h < 1/100)
    (heta : eta^2 ≤ 1) :
    0 < 1-2*h*eta^2 := by
  have hmul : h*eta^2 ≤ h := by
    nlinarith [mul_nonneg (le_of_lt hh) (sub_nonneg.mpr heta)]
  linarith

#print axioms first_order_source_pairs
#print axioms second_order_source_pairs
#print axioms no_interior_first_order_pair
#print axioms unique_positive_pair_at_second_order
#print axioms known_pressure_omega_order
#print axioms known_delayed_order
#print axioms eta_physical_chain_identity
#print axioms coordinate_jacobian_positive

end TerminalCore2026
