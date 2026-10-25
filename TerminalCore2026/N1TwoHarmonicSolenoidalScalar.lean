import Mathlib

/-!
Edition XXIV: scalar determinant of the co-rotating covariance
for the explicit smooth two-angular-frequency divergence-free fixture.
The Fourier modes, smooth annular profiles, and PDE are not formalized.
-/
namespace TerminalCore2026

/-- The modal real amplitude x, axial derivative amplitude y, and
independent second-mode axial amplitude z yield a rank-three
covariance determinant 8*x^4*z^2, independent of y. -/
theorem two_harmonic_covariance_determinant (x y z : ℝ) :
    (2 * x ^ 2) *
      ((2 * x ^ 2) * (2 * (y ^ 2 + z ^ 2)) -
        (-2 * x * y) ^ 2)
      = 8 * x ^ 4 * z ^ 2 := by
  ring

/-- An explicit strictly positive-definite covariance Q = 2 I3
is algebraically possible with two angular frequencies. -/
theorem two_harmonic_identity_determinant :
    (2 : ℚ) * 2 * 2 = 8 := by
  norm_num

/-- A conservative rational lower bound for the two-frequency
strict covariance fixture on its annular plateau. Scalar only. -/
theorem two_mode_strict_floor_fraction :
    ((3 / 2 : ℚ) * (1 - (1 / 16) * (5 / 4) ^ 2) -
      2 * (1 / 16) * (5 / 4) * (1 / 2)) =
        653 / 512 := by
  norm_num

#print axioms two_mode_strict_floor_fraction

#print axioms two_harmonic_covariance_determinant
#print axioms two_harmonic_identity_determinant
end TerminalCore2026
