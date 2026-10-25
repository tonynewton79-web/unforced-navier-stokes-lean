import Mathlib

/-!
Edition XXIV, scalar kernel witnesses for the co-rotating covariance
of ONE m=+/-1 Fourier pair. No Fourier/PDE stress representation
is formalized here. In particular, no complete H8 cone theorem.
-/
namespace TerminalCore2026

/-- Each of two real polarization vectors is orthogonal to their
algebraic cross product. This exhibits the rank-two obstruction
when the polarizations are linearly independent. -/
theorem single_pair_cross_orthogonal
    (a1 a2 a3 b1 b2 b3 : ℝ) :
    a1*(a2*b3-a3*b2)+a2*(a3*b1-a1*b3)+a3*(a1*b2-a2*b1)=0
    ∧
    b1*(a2*b3-a3*b2)+b2*(a3*b1-a1*b3)+b3*(a1*b2-a2*b1)=0 := by
  constructor <;> ring

/-- In an independent second frequency, a three-direction positive
fixture becomes possible: Q = 2 I_3, determinant 8. Finite only. -/
theorem two_frequency_strict_positive_fixture :
    ((2 : ℚ) * 2 * 2) = 8 := by
  norm_num

#print axioms single_pair_cross_orthogonal
#print axioms two_frequency_strict_positive_fixture
end TerminalCore2026
