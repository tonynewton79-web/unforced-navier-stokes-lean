import Mathlib

/-!
# A.11 full-hull stress: finite conditional Lean gates

No genuine Appendix-A integrals, source interval enclosures, full
stress-cone certificate or unforced Navier--Stokes theorem is
formalized here.
-/
namespace TerminalCore2026

theorem exact_root_total_derivative_zero
    (residual : ℝ → ℝ) (hroot : ∀ η, residual η = 0) (η : ℝ) :
    deriv residual η = 0 := by
  have heq : residual = fun _ => (0 : ℝ) := by
    funext x
    exact hroot x
  simp [heq]

theorem a11_two_support_hull_arithmetic :
    ((-17 : ℚ)/20)-((-63 : ℚ)/20) = 23/10 ∧
    (2 : ℚ)*(3/10) = 3/5 := by
  constructor <;> norm_num

theorem a11_full_hull_strict_scalar
    (lam h E D P T : ℝ)
    (hlam : 0 < lam) (hlammax : lam ≤ 1/20)
    (hh0 : 0 ≤ h) (hh : h ≤ lam/100)
    (hE0 : 0 ≤ E) (hE : E ≤ lam/4)
    (hD0 : 0 ≤ D) (hD : D ≤ 233/100)
    (hP0 : 0 ≤ P) (hP : P ≤ 5000001/10000000)
    (hT0 : 0 ≤ T) (hT : T ≤ 1/100000) :
    E * (4*h*D + 4*(1/2+h)*P + T) < (503/2000)*lam := by
  have h4h : 0 ≤ 4*h := by linarith
  have hhmax : 4*h ≤ (1:ℝ)/500 := by linarith
  have hDprod : 4*h*D ≤ (1/500:ℝ)*(233/100) := by
    calc
      4*h*D ≤ 4*h*(233/100) := mul_le_mul_of_nonneg_left hD h4h
      _ ≤ (1/500:ℝ)*(233/100) := by nlinarith
  have hA : 0 ≤ 2+4*h := by linarith
  have hAmax : 2+4*h ≤ (1001:ℝ)/500 := by linarith
  have hPprod : (2+4*h)*P ≤ (1001/500:ℝ)*(5000001/10000000) := by
    calc
      (2+4*h)*P ≤ (2+4*h)*(5000001/10000000) :=
        mul_le_mul_of_nonneg_left hP hA
      _ ≤ (1001/500:ℝ)*(5000001/10000000) := by nlinarith
  have hB : 4*h*D + 4*(1/2+h)*P + T < (503:ℝ)/500 := by
    nlinarith [hDprod, hPprod, hT]
  have hBnonneg : 0 ≤ 4*h*D + 4*(1/2+h)*P + T := by
    have ha : 0 ≤ 1/2+h := by linarith
    positivity
  calc
    E*(4*h*D+4*(1/2+h)*P+T)
        ≤ (lam/4)*(4*h*D+4*(1/2+h)*P+T) :=
          mul_le_mul_of_nonneg_right hE hBnonneg
    _ < (lam/4)*(503/500) :=
          mul_lt_mul_of_pos_left hB (by positivity)
    _ = (503/2000)*lam := by ring

#print axioms exact_root_total_derivative_zero
#print axioms a11_two_support_hull_arithmetic
#print axioms a11_full_hull_strict_scalar

end TerminalCore2026
