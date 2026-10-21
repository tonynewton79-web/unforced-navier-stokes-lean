import Mathlib

/-!
# A.11 final-source gate: scalar Lean proof candidates

Only algebraic stress dependence, exact rational constants and the
conditional scalar inequality are addressed. A physical Navier--Stokes
Theorem 1.1 is NOT formalized by this module.
-/
namespace TerminalCore2026

def A11StressN (h A eta X S Se Pi Pie : ℝ) : ℝ :=
  (4*h*eta*S - (1-eta^2)*Se)/X +
    4*A*eta*Pi - (1-eta^2)*Pie

theorem A11_stress_integration_data
    (h A eta X S Se Pi Pie CS CSe CP CPe : ℝ) :
    A11StressN h A eta X (S+CS) (Se+CSe) (Pi+CP) (Pie+CPe) -
      A11StressN h A eta X S Se Pi Pie =
      A11StressN h A eta X CS CSe CP CPe := by
  unfold A11StressN
  ring

theorem A11_axis_unfixed_moment (h A X k : ℝ) :
    A11StressN h A 0 X 0 k 0 0 = -k/X := by
  simp [A11StressN]

theorem A11_source_gated_ratio (lam E bracket : ℝ)
    (hlam : 0 < lam) (hE0 : 0 ≤ E)
    (hE : E ≤ lam/4) (hB : bracket ≤ 503/500) :
    E*bracket ≤ (503/2000)*lam ∧ E*bracket < lam/2 := by
  have h1 : E*bracket ≤ E*(503/500) :=
    mul_le_mul_of_nonneg_left hB hE0
  have h2 : E*(503/500) ≤ (lam/4)*(503/500) :=
    mul_le_mul_of_nonneg_right hE (by norm_num)
  have h3 : E*bracket ≤ (503/2000)*lam := by
    calc
      E*bracket ≤ E*(503/500) := h1
      _ ≤ (lam/4)*(503/500) := h2
      _ = (503/2000)*lam := by ring
  constructor
  · exact h3
  · have h4 : (503/2000)*lam < lam/2 := by nlinarith
    exact lt_of_le_of_lt h3 h4

theorem A11_cone_margin_rational :
    (85676973/76832000:ℚ) =
      2*(3/4)^2-(3/20)*(503/1960)^2 ∧
    (85676973/76832000:ℚ) > 9/20 := by
  constructor <;> norm_num

theorem A11_delta_eps_rational :
    (40960:ℚ)/(20:ℚ)^28 < 1/10^30 ∧
    ((2560:ℚ)/(20:ℚ)^28) /
      (1-(40960:ℚ)/(20:ℚ)^28) < 1/10^20 := by
  constructor <;> norm_num

#print axioms A11_stress_integration_data
#print axioms A11_axis_unfixed_moment
#print axioms A11_source_gated_ratio
#print axioms A11_cone_margin_rational
#print axioms A11_delta_eps_rational

end TerminalCore2026
