import Mathlib

/-!
Edition XLII. This Lean source proves scalar bilinear identities
and positive initial-rate arithmetic only. It DOES NOT formalize
the unforced Navier--Stokes PDE, pressure Riesz transforms, heat
semigroup, axis Taylor remainder or finite-time singularities.
-/
namespace TerminalCore2026

theorem xlii_lambda_from_jet
    (a A b B qz L : ℝ)
    (h : L = -(a*A+b*B+qz)/2) :
    2*L+a*A+b*B+qz = 0 := by
  linarith

theorem xlii_axis_commutator
    (transportDerivative spatialDerivative cz qz : ℝ)
    (h : transportDerivative = spatialDerivative-cz*qz) :
    transportDerivative+cz*qz = spatialDerivative := by
  linarith

theorem xlii_even_odd_cross_vanish
    (cross : ℝ) (h : cross = -cross) : cross = 0 := by
  linarith

theorem xlii_positive_at_z_two (nu eps e8 : ℝ)
    (hnu : 0 < nu) (heps : eps ≠ 0)
    (hexp : 0 < e8) :
    0 < 16*nu*eps^2*e8 := by
  have hs : 0 < eps^2 := sq_pos_of_ne_zero heps
  positivity

theorem xlii_negative_at_axis (nu eps : ℝ)
    (hn : 0 < nu) (he : eps ≠ 0) :
    -(112*nu*eps^2) < 0 := by
  have hs : 0 < eps^2 := sq_pos_of_ne_zero he
  nlinarith

theorem xlii_gaussian_sign_threshold (z : ℝ)
    (h : 7 < 2*z^2) : 0 < 2*z^2-7 := by
  linarith

#print axioms xlii_lambda_from_jet
#print axioms xlii_axis_commutator
#print axioms xlii_even_odd_cross_vanish
#print axioms xlii_positive_at_z_two
#print axioms xlii_negative_at_axis
#print axioms xlii_gaussian_sign_threshold
end TerminalCore2026
