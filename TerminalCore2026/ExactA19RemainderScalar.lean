import Mathlib

/-! Scalar checks for the exact Appendix-A (A.19) quadratic amplitude.
The smooth bump integrals, exterior schedule, and Navier--Stokes
equations are NOT formalized here. -/
namespace TerminalCore2026

theorem A19_disjoint_support (lam : ℝ)
    (h0 : 0 ≤ lam) (h1 : lam ≤ 1/20) :
    11 < 13-(63/20)*lam := by
  linarith

theorem A19_quadratic_identity
    (A K J₁ J₂ a₁ a₂ b₁ b₂ P D : ℝ) :
    K*A^2+P-D+J₁*(a₁+b₁*A)^2+J₂*(a₂+b₂*A)^2 =
    (K+J₁*b₁^2+J₂*b₂^2)*A^2+
    2*(J₁*a₁*b₁+J₂*a₂*b₂)*A+
    (P-D+J₁*a₁^2+J₂*a₂^2) := by
  ring

theorem A19_positive_quadratic_coefficient
    (K J₁ J₂ b₁ b₂ : ℝ)
    (hK : 0 < K) (h1 : 0 ≤ J₁) (h2 : 0 ≤ J₂) :
    0 < K+J₁*b₁^2+J₂*b₂^2 := by
  have p1 : 0 ≤ J₁*b₁^2 := mul_nonneg h1 (sq_nonneg _)
  have p2 : 0 ≤ J₂*b₂^2 := mul_nonneg h2 (sq_nonneg _)
  linarith

theorem A19_bump_tail_bound (lam : ℝ)
    (h : lam ≤ 1/20) :
    5137/200 ≤ 26-(63/10)*lam := by
  linarith

#print axioms A19_disjoint_support
#print axioms A19_quadratic_identity
#print axioms A19_positive_quadratic_coefficient
#print axioms A19_bump_tail_bound

end TerminalCore2026
